#!/usr/bin/env python3
"""Sign Siper's rules file with its offline Ed25519 release key."""

import argparse
import base64
import json
import os
import subprocess
import tempfile
from pathlib import Path


def canonical_payload(document: dict) -> bytes:
    unsigned = dict(document)
    unsigned.pop("signature", None)
    return json.dumps(
        unsigned,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("rules", nargs="?", default="fraud_numbers.json")
    parser.add_argument(
        "--key",
        default=os.path.expanduser("~/.config/siper/rules-signing-key.pem"),
        help="Ed25519 private key path (kept outside the repository)",
    )
    args = parser.parse_args()

    rules_path = Path(args.rules)
    key_path = Path(args.key)
    if not key_path.is_file():
        raise SystemExit(f"Signing key is missing: {key_path}")

    document = json.loads(rules_path.read_text(encoding="utf-8"))
    payload = canonical_payload(document)
    with tempfile.NamedTemporaryFile() as payload_file:
        payload_file.write(payload)
        payload_file.flush()
        signature = subprocess.run(
            [
                "openssl", "pkeyutl", "-sign", "-rawin",
                "-inkey", str(key_path), "-in", payload_file.name,
            ],
            check=True,
            capture_output=True,
        ).stdout

    document["signature"] = base64.b64encode(signature).decode("ascii")
    rules_path.write_text(
        json.dumps(document, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Signed {rules_path} (version {document.get('version', '?')})")


if __name__ == "__main__":
    main()
