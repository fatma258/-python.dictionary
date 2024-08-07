ogrenciler = {
  101: {
    'isim' :"yiğit",
    'dogum' : 2010,
    'notlar' : (40,80,90)
}
,
    102 : {
    'isim' :"ada",
    'dogum' : 2012,
    'notlar' : (80,80,80)
}
,
    103 : {
    'isim' :"çınar",
    'dogum' : 2017,
    'notlar' : (70,70,70)
}
}

ogrno = int(input('öğrenci no :'))
            
ogrenci = ogrenciler[ogrno]
 

print(f"{ogrno} numaralı öğrencinin adı {ogrenci['isim']} ve doğum tarihi {2024 -ogrenci['dogum']} ve not ortalması {((ogrenci['notlar'][0] + ogrenci['notlar'][1] + ogrenci['notlar'][2])/3)}")

