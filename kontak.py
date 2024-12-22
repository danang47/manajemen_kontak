'Berisi kelas kontak untuk menjalankan program kontak'

import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()

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
        dokumen.menyimpan_kontak(isi=self.kontak)