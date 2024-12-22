"Program Manajemen Kontak"

def melihat_kontak():
    # Melihat Semua Kontak
    if Kontak:
        for num, item in enumerate(Kontak, start=1):
            print(f'{num}. {item["Nama"]} ({item["HP"]}, {item["Email"]})')
    else:
        print("\nKontak Kosong!")
        return 1

def menambah_kontak():
    # Menambahkan Kontak
    Nama = input("Masukan Nama Kontak Baru: ")
    HP = input("Masukan Nomor HP Baru: ")
    Email = input("Masukan Email Kontak Baru: ")
    Kontak_Baru = {'Nama': Nama, 'HP': HP, 'Email': Email}
    Kontak.append(Kontak_Baru)
    print("Kontak Baru Berhasil Ditambahkan!")

def menghapus_kontak():
    # Menghapus Kontak
    if melihat_kontak() == 1:
        return
    else:
        i_hapus = int(input("Masukan Nomor Kontak Yang Akan Dihapus: "))
        del Kontak[i_hapus - 1]
        print("Kontak Dihapus")

Kontak1 = {'Nama': 'Papa', 'HP': '085555', 'Email': 'aa@gmail.com'}
Kontak2 = {'Nama': 'Mama', 'HP': '086666', 'Email': 'bb@gmail.com'}
Kontak = [Kontak1, Kontak2]

while True:
    print("\nMenu Kontak :")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak")
    print("3. Menghapus Kontak")
    print("4. Keluar")

    Pilihan = input("Masukan Pilihan Menu Kontak (1,2,3 dan 4): ")

    if Pilihan == '1':
        melihat_kontak()

    elif Pilihan == '2':
        menambah_kontak()

    elif Pilihan == '3':
        menghapus_kontak()

    elif Pilihan == '4':
        # Keluar
       break
    else:
        print("Anda Memasukan Pilihan Yang Salah")