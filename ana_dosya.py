print("hello world")
print("""
HESAP MAKİNESİ
TOPLAMA İŞLEMİ YAPMAK İÇİN 1 'e BASIN.
ÇIKARMA İŞLEMİ YAPMAK İÇİN 2 'e BASIN.
""")
islem = str(input("İşlem seçiniz: "))
if islem == "1":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 + sayi2)
if  islem == "2":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 - sayi2)
