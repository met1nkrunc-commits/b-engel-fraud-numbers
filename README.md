# Siper kural listesi

Bu depo, Siper iPhone uygulamasının uzaktan güncellediği doğrulanmış SMS filtre kurallarını içerir.

## Güvenlik ilkeleri

- Kanıtı ve kaynağı incelenmemiş hiçbir telefon numarası listeye eklenmez.
- Örnek, test veya rastgele üretilmiş telefon numarası yayımlanmaz.
- Resmî kurumlar yalnızca tam gönderici başlığı eşleşmesiyle güvenilir kabul edilir.
- Tek başına yaygın kullanılan kelimeler engelleme kuralı yapılmaz.
- Her değişiklikte `version` ve `updated_at` alanları güncellenir.

## Alanlar

- `numbers`: İncelenmiş ve engellenmesi doğrulanmış telefon numaraları.
- `trusted_senders`: Banka ve kamu kurumlarının tam gönderici başlıkları.
- `licensed_betting_senders`: Kullanıcının ayarına göre ayrıca engellenebilen lisanslı bahis göndericileri.
- `extra_keywords`: Yüksek güvenli, kategoriye ayrılmış ek ifadeler.
