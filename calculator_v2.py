"""
1) Kullanıcıyı sürekli konsolda tutarak istediği kadar işlem yapmasını sağlayacak bir hesap makinesi
programlayacağız. Hesaplama işlemlerinin her biri ayrı fonksiyon olmalıdır.
Kullanıcı klavyeden ilk olarak istediği işlemi ( + - / * %) girmelidir. Dört işleme ek olarak mod operatörü de dahil. Daha 
sonra gireceği iki sayının kullanıcının istediği işleme yönlendirilmesini eğer kullanıcıdan alınan değer yukarıdaki beş sembolden 
biri değilse programın hata vermesini sağlayalım.
Kullanıcı işlem seçmek yerine "q" harfi girişi yaparsa programı sonlandıralım aksi takdirde program her hesaplama sonrası tekrar işlem
yapabiliyor olmalıdır. 
"""
def toplama(x,y):
    sonuc = x + y
    return sonuc
def cikarma(x,y):
    sonuc = x - y
    return sonuc
def carpma(x,y):
    sonuc = x * y
    return sonuc
def bolme(x,y):
    sonuc = x / y
    return sonuc
def mod(x,y):
    sonuc = x % y
    return sonuc

while True:
    secim = input("Yapmak Istediginiz Islemi Seciniz: ")
    if secim == "q":
        break
    elif secim == "+":
        sayi1 = int(input("Ilk Sayiyi Giriniz: "))
        sayi2 = int(input("Ikinci Sayiyi Giriniz: "))
        sonuc = toplama(sayi1,sayi2)
        print(f"Toplama Isleminin Sonucu:{sonuc} ")
        c = input("Hesap makinesini kullanmaya devam etmek istiyor musunuz? (Çıkmak için q'ya, devam etmek için ise q dışında bir tuşa basınız.): ")
        if c == "q":
            break
    elif secim == "-":
        sayi1 = int(input("Ilk Sayiyi Giriniz: "))
        sayi2 = int(input("Ikinci Sayiyi Giriniz: "))
        sonuc = cikarma(sayi1,sayi2)
        print(f"Cikarma Isleminin Sonucu:{sonuc} ")
        c = input("Hesap makinesini kullanmaya devam etmek istiyor musunuz? (Çıkmak için q'ya, devam etmek için ise q dışında bir tuşa basınız.): ")
        if c == "q":
            break
    elif secim == "*":
        sayi1 = int(input("Ilk Sayiyi Giriniz: "))
        sayi2 = int(input("Ikinci Sayiyi Giriniz: "))
        sonuc = carpma(sayi1,sayi2)
        print(f"Carpma Isleminin Sonucu:{sonuc} ")
        c = input("Hesap makinesini kullanmaya devam etmek istiyor musunuz? (Çıkmak için q'ya, devam etmek için ise q dışında bir tuşa basınız.): ")
        if c == "q":
            break
    elif secim == "/":
        sayi1 = int(input("Ilk Sayiyi Giriniz: "))
        sayi2 = int(input("Ikinci Sayiyi Giriniz: "))
        sonuc = bolme(sayi1,sayi2)
        print(f"Bolme Isleminin Sonucu:{sonuc} ")
        c = input("Hesap makinesini kullanmaya devam etmek istiyor musunuz? (Çıkmak için q'ya, devam etmek için ise q dışında bir tuşa basınız.): ")
        if c == "q":
            break
    elif secim == "%":
        sayi1 = int(input("Ilk Sayiyi Giriniz: "))
        sayi2 = int(input("Ikinci Sayiyi Giriniz: "))
        sonuc = mod(sayi1,sayi2)
        print(f"Mod Isleminin Sonucu:{sonuc} ")
        c = input("Hesap makinesini kullanmaya devam etmek istiyor musunuz? (Çıkmak için q'ya, devam etmek için ise q dışında bir tuşa basınız.): ")
        if c == "q":
            break
    else:
        print("Hatali Giris Yaptiniz Lutfen Gecerli Bir Islem Giriniz (Cikmak icin q'ya basabilirsiniz.): ")

        