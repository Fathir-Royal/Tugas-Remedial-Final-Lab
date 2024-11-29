# Sistem Manajemen Mahasiswa

Sistem Manajemen Mahasiswa adalah aplikasi Python sederhana untuk mengelola data mahasiswa. Aplikasi ini memungkinkan pengguna untuk menambahkan data mahasiswa, menampilkan daftar mahasiswa, melihat statistik nilai, dan memvalidasi email.

## Fitur

- **Tambah Data Mahasiswa**: 
  Memasukkan data mahasiswa berupa nama, NIM, email, dan nilai akhir. Program memvalidasi email dan memastikan NIM tidak duplikat.
  
- **Tampilkan Semua Mahasiswa**: 
  Menampilkan daftar lengkap data mahasiswa yang telah dimasukkan, termasuk status kelulusan.

- **Tampilkan Statistik**: 
  Menghitung dan menampilkan jumlah mahasiswa, rata-rata nilai akhir, dan daftar mahasiswa yang lulus.

- **Validasi Email**: 
  Memastikan email mahasiswa sesuai dengan format yang benar.

## Prasyarat

Pastikan Anda memiliki **Python 3.6+** terinstal di komputer Anda.

## Cara Menjalankan Program

1. Unduh atau salin kode dari file `sistem_manajemen_mahasiswa.py`.
2. Jalankan file menggunakan Python:
   ```bash
   python sistem_manajemen_mahasiswa.py
   ```
3. Ikuti instruksi di layar untuk menggunakan aplikasi.

## Struktur Program

- **`class Mahasiswa`**: 
  - Mengelola data mahasiswa (nama, NIM, email, nilai akhir, status kelulusan).
  - Menentukan status kelulusan berdasarkan nilai akhir.

- **Fungsi utama**:
  - `validasi_email(email)`: Memvalidasi format email menggunakan regex.
  - `hitung_rata_rata(nilai_list)`: Menghitung rata-rata nilai akhir mahasiswa.
  - `main()`: Mengelola menu dan alur aplikasi.

## Contoh Penggunaan

**1. Menambah Data Mahasiswa**

Program akan meminta Anda memasukkan:
- Nama mahasiswa.
- NIM (tidak boleh duplikat).
- Email (akan divalidasi dengan regex).
- Nilai akhir (harus berupa angka).

**2. Menampilkan Data Mahasiswa**

Program akan menampilkan informasi lengkap untuk setiap mahasiswa yang telah dimasukkan.

**3. Menampilkan Statistik**

Program menghitung:
- Jumlah total mahasiswa.
- Rata-rata nilai akhir.
- Daftar mahasiswa yang lulus (nilai akhir ≥ 75).

**4. Keluar**

Program akan berhenti ketika Anda memilih opsi **Keluar**.

## Contoh Output

```
=== Sistem Manajemen Mahasiswa ===
1. Tambah Data Mahasiswa
2. Tampilkan Semua Mahasiswa
3. Tampilkan Statistik
4. Keluar
Pilih menu: 1

-- Tambah Data Mahasiswa --
Masukkan Nama: John Doe
Masukkan NIM: 12345
Masukkan Email: johndoe@example.com
Masukkan Nilai Akhir: 85
Data berhasil ditambahkan!
```
