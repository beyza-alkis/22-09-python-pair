
"""2)Bir okul kayıt sistemi kodlayalım;
Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.
Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım. Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.

Classlarımız içerisinde self keywordü kullanalım. Class içi fonksiyonlarda içerideki propertylerden yararlanalım. """

from students import ogrenci
from teachers import ogretmen

ogrenci_1 = ogrenci("Kaan","27")
ogrenci_2 = ogrenci("Beyza","23")

ogretmen_1 = ogretmen("Ahmet","B")
ogretmen_2 = ogretmen("Sıla","A")

ogrenciler = [ogrenci_1,ogrenci_2]
ogretmenler = [ogretmen_1,ogretmen_2]

def adding_student(object):
    ogrenciler.append(object)

def adding_teacher(object):
    ogretmenler.append(object)

def show():
    print("************************************")
    print("Öğrenciler ve yaşları sırası ile; ")
    for i in range(len(ogrenciler)):
        print([ogrenciler[i].name,ogrenciler[i].age])
    print("************************************")
    print("Öğretmenler ve şubeleri sırası ile;")
    for i in range(len(ogretmenler)):
        print([ogretmenler[i].name,ogretmenler[i].classroom])




ogrenci_3 = ogrenci("Nursena","27")
adding_student(ogrenci_3)
ogretmen_3 = ogretmen("Elif","A")
adding_teacher(ogretmen_3)
show()



    

#adding_student("Kaan","27")
#print(ogrenciler)





