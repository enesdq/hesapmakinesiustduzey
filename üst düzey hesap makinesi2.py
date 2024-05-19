import math

def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b != 0:
        return a / b
    else:
        return "Bölme işlemi için ikinci sayı sıfır olamaz."

def us_alma(a, b):
    return a ** b

def karekok(a):
    return math.sqrt(a)

def faktoriyel(a):
    if a < 0:
        return "Negatif sayıların faktöriyeli alınamaz."
    else:
        return math.factorial(a)

def trigonometrik_islem(islem, a):
    if islem == "sin":
        return math.sin(math.radians(a))
    elif islem == "cos":
        return math.cos(math.radians(a))
    elif islem == "tan":
        return math.tan(math.radians(a))
    else:
        return "Geçersiz trigonometrik işlem."

def hesap_makinesi():
    print("Gelişmiş Hesap Makinesi")
    print("İşlemler:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Üs Alma")
    print("6. Kare Kök Alma")
    print("7. Faktöriyel Hesaplama")
    print("8. Trigonometrik İşlemler (sin, cos, tan)")

    secim = input("İşlemi seçin (1/2/3/4/5/6/7/8): ")

    if secim in ['1', '2', '3', '4', '5']:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))

        if secim == '1':
            print("Sonuç:", toplama(sayi1, sayi2))
        elif secim == '2':
            print("Sonuç:", cikarma(sayi1, sayi2))
        elif secim == '3':
            print("Sonuç:", carpma(sayi1, sayi2))
        elif secim == '4':
            print("Sonuç:", bolme(sayi1, sayi2))
        elif secim == '5':
            print("Sonuç:", us_alma(sayi1, sayi2))
    elif secim == '6':
        sayi = float(input("Sayiyi girin: "))
        print("Sonuç:", karekok(sayi))
    elif secim == '7':
        sayi = int(input("Sayiyi girin: "))
        print("Sonuç:", faktoriyel(sayi))
    elif secim == '8':
        islem = input("Trigonometrik işlemi girin (sin/cos/tan): ")
        sayi = float(input("Açıyı derece cinsinden girin: "))
        print("Sonuç:", trigonometrik_islem(islem, sayi))
    else:
        print("Geçersiz giriş")

hesap_makinesi()
