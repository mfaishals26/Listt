# Membuat list berbagai baju dan harga
daftar_baju = [
    {"nomor": 1, "nama": "Kaos Polos", "harga": 50000},
    {"nomor": 2, "nama": "Kemeja Lengan Panjang", "harga": 100000},
    {"nomor": 3, "nama": "Celana Jeans", "harga": 150000},
    {"nomor": 4, "nama": "Hoodie", "harga": 120000},
]

# Menampilkan daftar baju beserta harga
print("\nDaftar Baju:")
for baju in daftar_baju:
    print(baju["nomor"], ".", baju["nama"], "(Rp", baju["harga"], ")")

# Meminta pengguna untuk memilih opsi
pilihan = input("\nMenu:\n1. Pilih Baju\n2. Tambahkan Baju\n3. Ubah Baju\n4. Hapus Baju\n5. Keluar\nPilih opsi (1/2/3/4/5): ")

while pilihan != "5":
    if pilihan == "1":
        # Memilih baju dari daftar
        nomor_pilihan = int(input("Masukkan nomor baju yang ingin dibeli: "))
        for baju in daftar_baju:
            if baju["nomor"] == nomor_pilihan:
                print(f"Anda memesan {baju['nama']} seharga Rp {baju['harga']}.")
                break
        else:
            print("Nomor baju tidak valid.")
    elif pilihan == "2":
        # Menambahkan baju baru ke daftar
        nomor_baju_baru = int(input("Masukkan nomor baju baru: "))
        nama_baju_baru = input("Masukkan nama baju baru: ")
        harga_baju_baru = int(input("Masukkan harga baju baru: "))
        daftar_baju.append({"nomor": nomor_baju_baru, "nama": nama_baju_baru, "harga": harga_baju_baru})
        print(f"\n{nama_baju_baru} (Rp {harga_baju_baru}) berhasil ditambahkan ke dalam daftar.")
    elif pilihan == "3":
        # Mengubah baju dalam daftar
        nomor_baju_ubah = int(input("Masukkan nomor baju yang ingin diubah: "))
        for baju in daftar_baju:
            if baju["nomor"] == nomor_baju_ubah:
                nama_baju_baru = input("Masukkan nama baju baru: ")
                harga_baju_baru = int(input("Masukkan harga baju baru: "))
                baju["nama"] = nama_baju_baru
                baju["harga"] = harga_baju_baru
                print("Baju berhasil diubah.")
                break
        else:
            print("Nomor baju tidak ditemukan dalam daftar.")
    elif pilihan == "4":
        # Menghapus baju dari daftar
        nomor_baju_hapus = int(input("Masukkan nomor baju yang ingin dihapus: "))
        for baju in daftar_baju:
            if baju["nomor"] == nomor_baju_hapus:
                daftar_baju.remove(baju)
                print("Baju tersebut berhasil dihapus dari daftar.")
                break
        else:
            print("Nomor baju tidak ditemukan dalam daftar.")
    else:
        print("\nMohon masukkan pilihan yang valid.")

    # Menampilkan daftar baju terkini beserta nomor dan harga
    print("\nDaftar Baju Terkini:")
    for baju in daftar_baju:
        print("-", baju["nomor"], ".", baju["nama"], "(Rp", baju["harga"], ")")
    
    # Meminta pengguna untuk memilih opsi lagi
    pilihan = input("\nMenu:\n1. Pilih Baju\n2. Tambahkan Baju\n3. Ubah Baju\n4. Hapus Baju\n5. Keluar\nPilih opsi (1/2/3/4/5): ")

print("\nTerima kasih!")
