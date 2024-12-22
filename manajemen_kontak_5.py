"Program Manajemen Kontak"

class Kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak(self):
        # Melihat Semua Kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'\n{num}. {item["Nama"]} ({item["HP"]}, {item["Email"]})')
        else:
            print("\nKontak Kosong!")
            return 1

    def menambah_kontak(self):
        # Menambahkan Kontak
        Nama = input("Masukan Nama Kontak Baru: ")
        HP = input("Masukan Nomor HP Baru: ")
        Email = input("Masukan Email Kontak Baru: ")
        Kontak_Baru = {'Nama': Nama, 'HP': HP, 'Email': Email}
        self.kontak.append(Kontak_Baru)
        print("Kontak Baru Berhasil Ditambahkan!")

    def menghapus_kontak(self):
        # Menghapus Kontak
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input("\nMasukan Nomor Kontak Yang Akan Dihapus: "))
            del self.kontak[i_hapus - 1]
            print("Kontak Dihapus")

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
       break
    else:
        print("Anda Memasukan Pilihan Yang Salah")