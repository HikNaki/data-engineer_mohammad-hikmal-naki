
class Pelanggan:
    
    def __init__(self, nama, usia, idPelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__idPelanggan = idPelanggan

    # GETTER
    def getNama(self):
        return self.__nama

    def getUsia(self):
        return self.__usia

    def getIdPelanggan(self):
        return self.__idPelanggan
    
    # SETTER
    def setNama(self, inputNama):
        self.__nama = inputNama
    
    def setUsia(self, inputUsia):
        self.__nama = inputUsia
    
    def setIdPelanggan(self, inputIdPelanggan):
        self.__nama = inputIdPelanggan
    
    def tampilkanInfo(self):
        print("==Informasi Pelanggan==")
        print(f"Nama   : {self.__nama}\nUsia   : {self.__usia}\nid     : {self.__idPelanggan}" ) 

class Pelatih:
    
    def __init__(self, nama, spesialisasi, tahunPengalaman):
        self.__nama = nama
        self.__spesialisasi = spesialisasi
        self.__tahunPengalaman = tahunPengalaman
        
    # GETTER
    def getNama(self):
        return self.__nama

    def getSpesialisasi(self):
        return self.__spesialisasi

    def getTahunPengalaman(self):
        return self.__tahunPengalaman
    
    # SETTER
    def setNama(self, inputNama):
        self.__nama = inputNama
    
    def setSpesialisasi(self, inputSpesialisasi):
        self.__spesialisasi = inputSpesialisasi
    
    def setTahunPengalaman(self, inputTahunPengalamn):
        self.__tahunPengalaman = inputTahunPengalamn
    
    def tampilkanInfo(self):
        print("==Informasi Pelatih==")
        print(f"Nama : {self.__nama}\nSpesialisasi : {self.__spesialisasi}\nTahun Pengalaman : {self.__tahunPengalaman}" ) 
    
class KelasLatihan(Pelatih):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal):
        super().__init__(nama, spesialisasi, tahunPengalaman)
        self.__jenisLatihan = jenisLatihan
        self.__jadwal = jadwal
        self.__statusPesan = False
        
    def pesanKelas(self):
        if not self.__statusPesan:
            print(f"Kelas {self.__jenisLatihan} telah berhasil dipesan.")
            self.__statusPesan = True
        else:
            print("Anda telah memesan kelas ini sebelumnya")
    
    def batalkanKelas(self):
        if self.__statusPesan:
            print(f"Pemesanan kelas {self.__jenisLatihan} telah dibatalkan.")
            self.__statusPesan = False
        else:
            print("Anda belum memesan kelas ini.")
        
    def tampilkanInfo(self):
        super().tampilkanInfo()
        print(f"Jenis Latihan : {self.__jenisLatihan}\nJadwal : {self.__jadwal}")

class Yoga(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal, tingkatKesulitan):
        super().__init__(nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal)
        self.__tingkatKesulitan = tingkatKesulitan
        
    def aturPosisiYoga(self, posisi):
        print("Posisi Yoga diatur menjadi:", posisi)
        
    def pesanKelas(self):
        if not self._KelasLatihan__statusPesan:
            print(f"Kelas {self._KelasLatihan__jenisLatihan} telah berhasil dipesan.")
            self._KelasLatihan__statusPesan = True
            print("Harap datang tepat waktu untuk kelas yoga ini.")
        else:
            print("Anda telah memesan kelas yoga ini sebelumnya.")
            
    
    def batalkanKelas(self):
        if self._KelasLatihan__statusPesan:
            print(f"Pemesanan kelas {self._KelasLatihan__jenisLatihan} telah dibatalkan.")
            self._KelasLatihan__statusPesan = False
        else:
            print("Anda belum memesan kelas yoga ini.")
        
    def tampilkanInfo(self):
        print("Informasi Kelas Yoga:")
        super().tampilkanInfo()
        print(f"Tingkat Kesulitan: {self.__tingkatKesulitan}")

class AngkatBeban(KelasLatihan):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal, beratMaksimum):
        super().__init__(nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal)
        self.__beratMaksimum = beratMaksimum
        
    def pesanKelas(self):
        if not self._KelasLatihan__statusPesan:
            print(f"Kelas {self._KelasLatihan__jenisLatihan} telah berhasil dipesan.")
            self._KelasLatihan__statusPesan = True
            print("Harap datang tepat waktu untuk kelas angkat beban ini.")
        else:
            print("Anda telah memesan kelas yoga ini sebelumnya.")
            
    
    def batalkanKelas(self):
        if self._KelasLatihan__statusPesan:
            print(f"Pemesanan Kelas {self._KelasLatihan__jenisLatihan} telah dibatalkan.")
            self._KelasLatihan__statusPesan = False
        else:
            print("Anda belum memesan kelas angkat beban ini.")

    def aturBeratBeban(self, berat):
        print("Berat Beban diatur menjadi:", berat)

    def tampilkanInfo(self):
        print("Informasi Kelas Angkat Beban:")
        super().tampilkanInfo()
        print(f"Berat Maksimum yang Dapat Diangkat: {self.__beratMaksimum}")







client1 = Pelanggan("Hikmal", 20, "A1")
pelatih1 = Pelatih("Yasir", "Senam", 10)
kelasYasir = KelasLatihan("Yasir", "Senam", 5, "Aerobik", "Senin, Rabu, & Jumat")

client1.tampilkanInfo()
print("-----------------------------------")
pelatih1.tampilkanInfo()
print("-----------------------------------")
kelasYasir.tampilkanInfo()
print("-----------------------------------")


#Penggunaan Polymorphism
kelasLatihan = [
    Yoga("Muthiah", "Yoga", 3, "Yoga Sore", "Senin, Rabu", "Menengah"),
    AngkatBeban("Rafli", "Angkat Beban", 5, "Angkat Beban", "Selasa, Kamis", 70)
]

for kelas in kelasLatihan:
    kelas.tampilkanInfo()
    print("-----------------------------------")

kelasLatihan[0].aturPosisiYoga("Berdiri")
kelasLatihan[1].aturBeratBeban(60)


#Method Polymorphism Lanjutan
def ubahAtribut(kelasLatihan):
    for kelas in kelasLatihan:
        if isinstance(kelas, Yoga):
            kelas.aturPosisiYoga("Duduk bersila")
        elif isinstance(kelas, AngkatBeban):
            kelas.aturBeratBeban(70)


ubahAtribut(kelasLatihan)

kelasAbid = Yoga("Abid", "Yoga", 5, "Yoga Pagi", "Senin, Kamis", "Expert")
print("-----------------------------------")
kelasAbid.pesanKelas()
kelasAbid.batalkanKelas()
