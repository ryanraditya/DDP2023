#soal 2 list append
list=["aerox","matic","150","hitam","roda2"]
list.append("26,000.000",)
list.append("motor laki")
list.insert(2,"yamaha")
print(list)


#soal 2 match case luas bangun datar
print("""pilih luas:
1=Persegi
2=Lingkaran
3=Segitiga""")

bangun=int(input("anda memilih nomor"))
match bangun:
    case 1: 
        sisi=int(input("masukan sisi"))
        hasil=(sisi*sisi)
        print("hasil luas dari persegi adalah",hasil)
    case 2:
        phi=int(3.14)
        r=int(input("masukan jari jari"))
        hasil2=(phi)*(r*r)
        print("hasil luas dari lingkaran adalah",hasil2)
    case 3:
       a=int(input("masukan alas"))
       t=int(input("masukan tinggi"))
       hasil3=(1/2*a*t)
       print("hasil luas segitiga adalah",hasil3)
         







