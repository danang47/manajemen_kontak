"Program Manajemen Kontak"

def membuka_kontak(path='kontak.txt'):
    with open(path, mode='r') as file:
        kontak = file.readlines()
    return kontak

def menyimpan_kontak(path='kontak.txt', isi=[]):
    with open(path, mode='w') as file:
        file.writelines(isi)

class Kontak:
    def __init__(self):
        self.kontak = membuka_kontak()

    def melihat_kontak(self):
        # Melihat Semua Kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'\n{num}.' + item)
        else:
            print("\nKontak Kosong!")
            return 1

    def menambah_kontak(self):
        # Menambahkan Kontak
        Nama = input("Masukan Nama Kontak Baru: ")
        HP = input("Masukan Nomor HP Baru: ")
        Email = input("Masukan Email Kontak Baru: ")
        Kontak_Baru = f'{Nama} ({HP}, {Email})' + '\n'
        self.kontak.append(Kontak_Baru)
        print("Kontak Baru Berhasil Ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus Kontak
        if self.melihat_kontak() == 1:
            return
        else:
            try:
                i_hapus = int(input("\nMasukan Nomor Kontak Yang Akan Dihapus: "))
                del self.kontak[i_hapus - 1]
                print("Kontak Dihapus")
            except:
                print("\nInput yang anda masukan salah")

    def keluar_kontak(self):
        menyimpan_kontak(isi=self.kontak)


Kontak_Kantor = Kontak()
Kontak_Keluarga = Kontak()

while True:
    print("\nMenu Kontak :")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak")
    print("3. Menghapus Kontak")
    print("4. Keluar")

    Pilihan = input("Masukan Pilihan Menu Kontak (1,2,3 dan 4): ")

    if Pilihan == '1':
        Kontak_Kantor.melihat_kontak()

    elif Pilihan == '2':
        Kontak_Kantor.menambah_kontak()

    elif Pilihan == '3':
        Kontak_Kantor.menghapus_kontak()

    elif Pilihan == '4':
        # Keluar
        Kontak_Kantor.keluar_kontak()

        break
    else:
        print("Anda Memasukan Pilihan Yang Salah")