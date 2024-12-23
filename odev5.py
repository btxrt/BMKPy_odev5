# Bankamatik Uygulaması
# Hesap bilgileri tutulacak. (dictionary)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.

def menu():
  print("1. Para Çekme")
  print("2. Bakiye Sorgulama")
  print("3. Para Yatırma")



def paraCekme(hesap):
  cekilmekIstenenTutar = float(input("Çekmek istediğiniz tutarı giriniz: "))
  if cekilmekIstenenTutar <= hesap['bakiye']:
    hesap['bakiye'] -= cekilmekIstenenTutar
    print("Para çekme işlemi başarılı.")
  else:
    ekHesapKullan = input("Yetersiz bakiye. Ek hesabınızı kullanınmak ister misiniz?(evet,hayır) ")
    if ekHesapKullan.lower() == 'evet':
      if cekilmekIstenenTutar <= hesap['ek_hesap']:
        hesap['ek_hesap'] -= cekilmekIstenenTutar
        print("Ek hesaptan para çekme işlemi başarılı.")
      else:
        print("Ek hesapta da yeterli bakiye bulunmamaktadır.")
    else:
      print("İşlem iptal edildi.")


hesap = {'bakiye': 1000, 'ek_hesap': 500}

def bakiyeSorgula(hesap):
  print("Hesap bakiyesi:", hesap['bakiye'])
  

def paraYatirma(hesap):
  yatirilanTutar = float(input("Yatırmak istediğiniz tutarı giriniz: "))
  hesap['bakiye'] += yatirilanTutar
  print("Para yatırma işlemi başarılı.")



while True:
  menu()
  secim = int(input("Yapmak istediğiniz işlemi seçiniz: "))

  if secim == 1:
    paraCekme(hesap)
  elif secim == 2:
    bakiyeSorgula(hesap)
  elif secim == 3:
    paraYatirma(hesap)
    break
  else:
    print("Geçersiz seçim.")
    break