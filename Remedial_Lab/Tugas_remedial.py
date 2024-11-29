import re

class Mahasiswa:
    def __init__(self, nama, nim, email, nilai_akhir):
        """
        Inisialisasi objek Mahasiswa dengan atribut nama, NIM, email, nilai akhir, dan status.
        """
        self.nama = nama
        self.nim = nim
        self.email = email
        self.nilai_akhir = nilai_akhir
        self.status = "Tidak Lulus"

    def hitung_status(self):
        """
        Menentukan status kelulusan mahasiswa berdasarkan nilai akhir.
        Status 'Lulus' jika nilai >= 75, selain itu 'Tidak Lulus'.
        """
        if self.nilai_akhir >= 75:
            self.status = "Lulus"
        else:
            self.status = "Tidak Lulus"

    def tampilkan_info(self):
        """
        Menampilkan informasi lengkap mahasiswa, termasuk nama, NIM, email, nilai akhir, dan status.
        """
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Email: {self.email}")
        print(f"Nilai Akhir: {self.nilai_akhir}")
        print(f"Status: {self.status}")

def validasi_email(email):
    """
    Memvalidasi format email menggunakan pola regex.
    Return True jika email valid, False jika tidak valid.
    """
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def hitung_rata_rata(nilai_list):
    """
    Menghitung rata-rata dari daftar nilai yang diberikan.
    Return nilai rata-rata sebagai float.
    """
    return sum(nilai_list) / len(nilai_list)

def main():
    """
    Fungsi utama yang mengelola sistem manajemen mahasiswa:
    - Menambah data mahasiswa.
    - Menampilkan daftar mahasiswa.
    - Menampilkan statistik mahasiswa.
    - Keluar dari sistem.
    """
    mahasiswa_list = []
    nim_set = set()

    while True:
        print("\n=== Sistem Manajemen Mahasiswa ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Tampilkan Statistik")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            print("\n-- Tambah Data Mahasiswa --")

            while True:
                nama = input("Masukkan Nama: ").strip()
                if nama:
                    break
                else:
                    print("Nama tidak boleh kosong. Silakan coba lagi.")

            while True:
                nim = input("Masukkan NIM: ").strip()
                if not nim:
                    print("NIM tidak boleh kosong. Silakan coba lagi.")
                elif nim in nim_set:
                    print("NIM sudah ada! Silakan masukkan NIM yang berbeda.")
                else:
                    nim_set.add(nim)
                    break

            while True:
                email = input("Masukkan Email: ").strip()
                if validasi_email(email):
                    break
                else:
                    print("Email tidak valid! Coba lagi.")

            nilai_akhir = None
            while True:
                try:
                    nilai_akhir = float(input("Masukkan Nilai Akhir: "))
                    break
                except ValueError:
                    print("Nilai harus berupa angka. Coba lagi.")
            
            mahasiswa = Mahasiswa(nama, nim, email, nilai_akhir)
            mahasiswa.hitung_status()
            mahasiswa_list.append(mahasiswa)
            print("Data berhasil ditambahkan!")

        elif pilihan == "2":
            print("\n-- Data Mahasiswa --")
            if not mahasiswa_list:
                print("Belum ada data mahasiswa.")
            else:
                for idx, mhs in enumerate(mahasiswa_list):
                    print(f"\nMahasiswa {idx+1}:")
                    mhs.tampilkan_info()

        elif pilihan == "3":
            print("\n-- Statistik Mahasiswa --")
            if not mahasiswa_list:
                print("Belum ada data mahasiswa.")
                continue

            nilai_list = [mhs.nilai_akhir for mhs in mahasiswa_list]
            rata_rata = hitung_rata_rata(nilai_list)
            print(f"Jumlah Mahasiswa: {len(mahasiswa_list)}")
            print(f"Rata-rata Nilai Akhir: {rata_rata:.2f}")

            print("Daftar Mahasiswa yang Lulus:")
            for mhs in mahasiswa_list:
                if mhs.status == "Lulus":
                    print(f"- {mhs.nama.upper()} ({mhs.nim})")

        elif pilihan == "4":
            print("Keluar dari sistem. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

main()
