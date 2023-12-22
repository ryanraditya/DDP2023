class Animal:
    def __init__(self,nama,makanan,hidup,berkembang_biak):
        self.nama=nama
        self.makanan=makanan
        self.hidup=hidup
        self.berkembang_biak=berkembang_biak
        

#menambahkan class baru dengan parent Animal
class Badak(Animal):
        def __init__(self, nama, makanan, hidup, berkembang_biak,bertahan,menyerang):
             super().__init__(nama, makanan, hidup, berkembang_biak)
             self.bertahan=bertahan
             self.menyerang=menyerang

        def cetak(self):
             print(f"""
                    Nama \t\t:{self.nama}
                    Makanan\t \t:{self.makanan}
                    Hidup \t\t:{self.hidup}
                    Berkembang biak\t:{self.berkembang_biak}
                    Bertahan \t\t:{self.bertahan}
                    Menyerang\t\t:{self.menyerang}""")

class Hiu(Animal):
        def __init__(self, nama, makanan, hidup, berkembang_biak,bertahan,menyerang):
             super().__init__(nama, makanan, hidup, berkembang_biak)
             self.bertahan=bertahan
             self.menyerang=menyerang
        
        def cetak(self):
             print(f"""
                    Nama\t\t:{self.nama}
                    Makanan\t\t:{self.makanan}
                    Hidup\t\t:{self.hidup}
                    Berkembang biak\t:{self.berkembang_biak}
                    Bertahan\t\t:{self.bertahan}
                    Menyerang\t\t:{self.menyerang}""")
             
class Singa(Animal):
        def __init__(self, nama, makanan, hidup, berkembang_biak,bertahan,menyerang):
             super().__init__(nama, makanan, hidup, berkembang_biak)
             self.bertahan=bertahan
             self.menyerang=menyerang

        def cetak(self):
             print(f"""
                    Nama\t\t:{self.nama}
                    Makanan\t\t:{self.makanan}
                    Hidup\t\t:{self.hidup}
                    Berkembang biak\t:{self.berkembang_biak}
                    Bertahan\t\t:{self.bertahan}
                    Menyerang\t\t:{self.menyerang}""")
#membuat variable             
Ikan_hiu=Hiu("Hiu","Ikan","Air","Bertelur didalam perut induk nya","Ekor nya","Gigi yang bertaring")
badak_jawa = Badak("Badak","sayur","darat","melahirkan","menyeruduk","memakai cula yang ada dikepala nya")
Raja=Singa("Singa","Karnivora pemakan daging","Didarat","Melahirkan","Dengan auman","Mengigit mangasa nya")
#memanggil nama variable
badak_jawa.cetak()
Ikan_hiu.cetak()
Raja.cetak()