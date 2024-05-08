# Membuat list berbagai makanan dan harga
daftar_makanan = [
    {"nomor": 1, "nama": "Nasi Goreng", "harga": 15000},
    {"nomor": 2, "nama": "Ayam Bakar", "harga": 25000},
    {"nomor": 5, "nama": "Es Teh", "harga": 5000}
]

# Menampilkan daftar makanan beserta harga
print("\nDaftar Makanan:")
for makanan in daftar_makanan:
    print("-", makanan["nomor"], ".", makanan["nama"], "(Rp", makanan["harga"], ")")

# Meminta pengguna untuk memilih opsi
pilihan = input("\nMenu:\n1. Pilih Makanan\n2. Tambahkan Makanan\n3. Ubah Makanan\n4. Hapus Makanan\n5. Keluar\nPilih opsi (1/2/3/4/5): ")

while pilihan != "5":
    if pilihan == "1":
        # Memilih makanan dari daftar
        nomor_pilihan = int(input("Masukkan nomor makanan yang ingin dipesan: "))
        for makanan in daftar_makanan:
            if makanan["nomor"] == nomor_pilihan:
                print(f"Anda memesan {makanan['nama']} seharga Rp {makanan['harga']}.")
                break
        else:
            print("Nomor makanan tidak valid.")
    elif pilihan == "2":
        # Menambahkan makanan baru ke daftar
        nomor_makanan_baru = int(input("Masukkan nomor makanan baru: "))
        nama_makanan_baru = input("Masukkan nama makanan baru: ")
        harga_makanan_baru = int(input("Masukkan harga makanan baru: "))
        daftar_makanan.append({"nomor": nomor_makanan_baru, "nama": nama_makanan_baru, "harga": harga_makanan_baru})
        print(f"\n{nama_makanan_baru} (Rp {harga_makanan_baru}) berhasil ditambahkan ke dalam daftar.")
    elif pilihan == "3":
        # Mengubah makanan dalam daftar
        nomor_makanan_ubah = int(input("Masukkan nomor makanan yang ingin diubah: "))
        for makanan in daftar_makanan:
            if makanan["nomor"] == nomor_makanan_ubah:
                nama_makanan_baru = input("Masukkan nama makanan baru: ")
                harga_makanan_baru = int(input("Masukkan harga makanan baru: "))
                makanan["nama"] = nama_makanan_baru
                makanan["harga"] = harga_makanan_baru
                print("Makanan berhasil diubah.")
                break
        else:
            print("Nomor makanan tidak ditemukan dalam daftar.")
    elif pilihan == "4":
        # Menghapus makanan dari daftar
        nomor_makanan_hapus = int(input("Masukkan nomor makanan yang ingin dihapus: "))
        for makanan in daftar_makanan:
            if makanan["nomor"] == nomor_makanan_hapus:
                daftar_makanan.remove(makanan)
                print("Makanan tersebut berhasil dihapus dari daftar.")
                break
        else:
            print("Nomor makanan tidak ditemukan dalam daftar.")
    else:
        print("\nMohon masukkan pilihan yang valid.")

    # Menampilkan daftar makanan terkini beserta nomor dan harga
    print("\nDaftar Makanan Terkini:")
    for makanan in daftar_makanan:
        print("-", makanan["nomor"], ".", makanan["nama"], "(Rp", makanan["harga"], ")")
    
    # Meminta pengguna untuk memilih opsi lagi
    pilihan = input("\nMenu:\n1. Pilih Makanan\n2. Tambahkan Makanan\n3. Ubah Makanan\n4. Hapus Makanan\n5. Keluar\nPilih opsi (1/2/3/4/5): ")

print("\nTerima kasih!")
