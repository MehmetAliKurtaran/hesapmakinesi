# class Araba:
#     def __init__(self, renk, marka, motor):
#         self.renk = renk
#         self.marka = marka
#         self.motor = motor
#
#         print(f"{self.marka} - {self.motor} - {self.renk}")
#
#
# araba_mavi = Araba("Mavi","Audi","1.6")
# araba_beyaz = Araba("Beyaz","Audi","1.6")



# class Araba:
#     def __init__(self, renk, marka, motor):
#         self.renk = renk
#         self.marka = marka
#         self.motor = motor
#
#         self.araba_bilgileri = (f"{self.marka} - {self.motor} - {self.renk}")
#
#
#     def bilgileri_goster(self):
#         print(self.araba_bilgileri)
#
# araba_mavi = Araba("Mavi","Audi","1.6")
# araba_beyaz = Araba("Beyaz","Audi","1.6")
# araba_mavi.bilgileri_goster()
# araba_beyaz.bilgileri_goster()
#
#
# class Ogrenci:
#     def __init__(self):
#         pass
#     def bilgi_al(self, ad, no, sinif):
#         self.ad = ad
#         self.no = no
#         self.sinif = sinif
#
#     def bilgileri_goster(self):
#         print(f"Öğrencinin Adı: {self.ad}")
#         print(f"Öğrencinin No'su: {self.no}")
#         print(f"Öğrencinin Sınıfı: {self.sinif}")
#
# ogrenci1 = Ogrenci()
# ogrenci1.bilgi_al("Mehmet", 25, "5-B")
# ogrenci1.bilgileri_goster()
#
# print()
#
# ogrenci2 = Ogrenci()
# ogrenci2.bilgi_al("Ahmet", 21, "6-C")
# ogrenci2.bilgileri_goster()


# class Personal:
#     def __init__(self):
#         pass
#     def personel_ekle(self, ad, soyad, tc):
#         self.ad = ad
#         self.soyad = soyad
#         self.tc = tc
#     def maas_belirle(self,tcc):
#         if tcc % 2 == 0:
#             return 5000
#         else:
#             return 10000
#     def bilgileri_goster(self):
#         print(f"Personel adı: {self.ad}")
#         print(f"Personel soyadı: {self.soyad}")
#         print(f"Personel tc: {self.tc}")
#         print(f"Maaşı: ", maas)
#
# adi = input("Ad gir")
# soyadi = input("Soyad gir")
# tcsi = int(input("tc gir: "))
#
# personel = Personal()
# personel.personel_ekle(adi, soyadi, tcsi)
# maas = personel.maas_belirle(tcsi)
# personel.bilgileri_goster()




#KAPSÜLLEME

# class Personel:
#     def __init__(self, ad, yas):
#         self.ad = ad
#         self.yas = yas
#
#     def yas_goster(self):
#         return self.yas
#
#     def yas_guncelle(self, yeni_yas):
#         if yeni_yas > self.yas:
#             self.yas = yeni_yas
# calisan = Personel("Ahmet", 25)

import random

class banka:
    def __init__(self):
        pass
    def hesap_olustur(self, ad, soyad, hesap, bakiye):
        self.ad = ad
        self.soyad = soyad
        self.hesap = hesap
        self.bakiye = bakiye
    def para_cek(self,cekilecel_tutar):
        self.cekilecek_tutar = cekilecel_tutar
        if cekilecel_tutar <= self.bakiye:
            self.bakiye -= self.cekilecek_tutar
            return cekilecel_tutar
        else:
            return "Yetersiz bakiye"
    def bilgileri_goster(self):
        print("ad ",self.ad)
        print("soyad: ", self.soyad)
        print("hesap no: ", self.hesap)
        print("bakiye: " , self.bakiye)
        print("cekilen tutar: ", self.para_cek(self.cekilecek_tutar))




adi = input("Ad gir: ")
soyadi = input("Soyad gir: ")
baki = int(input("Bakiye gir: "))
hesapp = random.randint(100000,1000000)
cekilecek = int(input("tutar gir"))

bank = banka()
bank.hesap_olustur(adi, soyadi,hesapp,baki)
bank.para_cek(cekilecek)
bank.bilgileri_goster()























