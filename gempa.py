class Gempa:
    def __init__(self,lokasi,skala):
        self.lokasi= lokasi
        self.skala= skala
    
    def dampak(self):
        if self.skala <2:
            return f"Gempa di {self.lokasi} dengan sekala {self.skala}:Dampak gempa tidak berasa"
        elif 2 <=self.skala <4:
            return f"Gempa di {self.lokasi} dengan sekala {self.skala}:Dampak gempa bangunan retak-retak"
        elif 4 <=self.skala <6:
            return f"Gempa di {self.lokasi} dengan sekala {self.skala}:Dampak gempa bangunan roboh"
        else:
            return f"Gempa di {self.lokasi} dengan sekala {self.skala}:Dampak gempa bangunan roboh dan berpotensi tsunami"
