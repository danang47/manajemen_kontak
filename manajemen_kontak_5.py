"Program Manajemen Kontak"
import kontak

def main():
    Kontak_Kantor = kontak.Kontak()
    Kontak_Keluarga = kontak.Kontak()


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

if __name__ == "__main__":
    main()