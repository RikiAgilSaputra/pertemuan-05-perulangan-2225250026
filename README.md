# Pertemuan 05 Perulangan Python
Nama: Riki Agil Saputra


NIM: 2225250026


Kelas: 3A

## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan
python3 kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
for:
1. objek ditentukan, semisal pada for (1,4)
2. pengecekan ketersediaan data
3. memasukkan nilainya ke dalam variabel kontrol, semisal i
4. menjalankan kode program yang termasuk ke dalam blok for
5. kembali ke poin 2

while:
1. variabel harus dibuat dahulu sebelum kode while
2. menentukan kondisi untuk menilai variabel sesuai atau tidak
3. menjalankan kode program yang termasuk blok while
4. pembaruan nilai supaya tidak infinite loop
5. kembali ke poin 2


## Hasil Pengujian
| Input | | | Keluaran yang Diharapkan | | Keluaran Aktual | | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **a** | **d** | **n** | **Suku** | **Jumlah** | **Suku** | **Jumlah** | |
| 2 | 3 | 5 | 2, 5, 8, 11, 14 | 40 | 2, 5, 8, 11, 14 | 40 | Sesuai |
| 10 | -2 | 4 | 10, 8, 6, 4 | 28 | 10, 8, 6, 4 | 28 | Sesuai |
| 1.5 | 0.5 | 3 | 1.5, 2.0, 2.5 | 6.0 | 1.5, 2.0, 2.5 | 6.0 | Sesuai |
| 5 | 2 | -1 | - | - | - | - | Sesuai |
| -3 | 1 | 2 | -3, -2 | -5 | -3, -2 | -5 | Sesuai |

## Refleksi
Menggunakan nama variabel yang dideklarasikan di awal ke dalam fungsi perulangan for, misalkan terdapat nama variabel di awal yaitu angka, kemudian nama variabel tersebut saya gunakan di dalam fungsi perulangan menjadi for angka in range (1, 0). Hal tersebut dapat membuat hasil menjadi berbeda. Kemudian, saya menangani permasalahan tersebut dengan cara mengganti nama variabel angka pada fungsi perulangan for dengan yang benar, yaitu i sehingga menjadi for i in range (1, 0).