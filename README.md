# Siper kural listesi

Bu depo, Siper iPhone uygulamasının uzaktan güncellediği doğrulanmış SMS filtre kurallarını içerir.

## Güvenlik ilkeleri

- Kanıtı ve kaynağı incelenmemiş hiçbir telefon numarası listeye eklenmez.
- Örnek, test veya rastgele üretilmiş telefon numarası yayımlanmaz.
- Resmî kurumlar yalnızca tam gönderici başlığı eşleşmesiyle güvenilir kabul edilir.
- Tek başına yaygın kullanılan kelimeler engelleme kuralı yapılmaz.
- Her değişiklikte `version` ve `updated_at` alanları güncellenir.
- Her sürüm çevrimdışı tutulan Ed25519 anahtarıyla imzalanır. Uygulama imzasız veya değiştirilmiş kuralları reddeder.

## Alanlar

- `trusted_senders`: Banka ve kamu kurumlarının tam gönderici başlıkları.
- `licensed_betting_senders`: Kullanıcının ayarına göre ayrıca engellenebilen lisanslı bahis göndericileri.
- `extra_keywords`: Yüksek güvenli, kategoriye ayrılmış ek ifadeler.
- `signature`: Diğer tüm alanların standart JSON gösterimi için Ed25519 imzası.

## Yayımlama

1. `version` ve `updated_at` alanlarını güncelleyin.
2. Kural değişikliklerini gözden geçirin.
3. `./scripts/sign_rules.py fraud_numbers.json` komutuyla dosyayı imzalayın.
4. İmzalanmış dosyayı commit edin. Özel anahtarı hiçbir zaman bu depoya eklemeyin.
