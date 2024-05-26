# APLIKASI YELLOW PAGES

### JDSOL-014 Grup 2 (Alfa Isa Dewa)
Aplikasi Yellow Pages ini merupakan aplikasi untuk melihat daftar nomor telpon dari berbagai jenis cabang (Pengacara, Restoran, Perbaikan) dengan Aturan yang ada di Indonesia.

### Features Aplikasi Yellow Pages:
- Create Data
- Read Data
- Update Data
- Delete Data
- Search By Name
- Pengelompokan Kolom
- Pengurutan Data Secara Ascending

### Tech:
Aplikasi ini dibangun dengan:
- [Python 3.12.3] - Adalah salah satu bahasa pemrograman komputer yang biasa dipakai untuk membangun berbagai hal seperti desktop app, mobile app, website, dan lain-lain.
- [Visual Studio Code] - Kode editor gratis yang dibuat untuk membangun web modern, aplikasi cloud, dan aplikasi lain.

### Teknik Yang Digunakan:
Adalah basic dari pemrograman seperti Conditional Statement, Loop, Dictionary List, dan Function. Dan semua fitur yang tertulis di atas akan dibuatkan sebuah fungsi.

## Struktur file capstoneAlfa.py:
Struktur yang dimaksud adalah bagian yang terdapat di awal, tengah, dan akhir dari file capstoneAlfa.py
1. Assign Var Dictionary in List.
2. Fungsi Create, Read, Update, Delete, Search by Name, Pengelompokan Kolom, Pengurutan Data Secara Ascending.
3. Alur aplikasi dari mulai, pemanggilan fungsi, sampai keluar aplikasi.
* variable YellowPages akan menggunakan kolom:
    1. Kode ('P' = Pengacara, 'R' = Restoran, Pp = 'Perbaikan') 
        -> Sebagai Primary Key.
    2. Nama
    3. Jam Buka
    4. Jam Tutup
    5. Kab/Kota
        -> Beberapa Kab/Kota diassign ke variable agar tidak ada kota mengasal di Indonesia (bisa ditambahkan di varible list kabkot jika kota memang ada, namun belum di assign ke variable).
    6. No Telpon
        -> Sebagai Unique Key.
    7. Keterangan

### Requirements:
- Python (lebih baik dengan versi sama atau terbaru agar tidak mengalami perubahan atau kendala saat menjalankan file).
- Terminal seperti cmd atau yang lain.

### Instalasi Dengan VsCode:
1. Taruh file capstoneAlfa.py ke dalam folder apapun
2. Buka VsCode dan arahkan ke file capstoneAlfa.py
3. Run code.

### Credit:
Terima kasih untuk Purwadhika, lecture Purwadhika yang dengan sabar mengajari siswanya.