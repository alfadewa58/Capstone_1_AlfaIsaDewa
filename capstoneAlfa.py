
# * * * * * PROGRAM YELLOW PAGES * * * * *

# * * * * * PEMBUATAN DICTIONARY * * * * *

YellowPages = [
    {'kode' : 'P001','nama' : 'Wahyu Budiono','jam_buka' : '07.00','jam_tutup' : '20.00','kota' : 'Semarang','no_telpon' : '082227171938','keterangan' : 'Kepailitan'},
    {'kode' : 'P021','nama' : 'Wahyu Siregar','jam_buka' : '08.00','jam_tutup' : '20.00','kota' : 'Binjai','no_telpon' : '08212345677','keterangan' : 'Kepailitan'},
    {'kode' : 'P002','nama' : 'Denis Abdulah','jam_buka' : '08.00','jam_tutup' : '21.00','kota' : 'Banyumanik','no_telpon' : '08222222938','keterangan' : 'Pembela Pidana'},
    {'kode' : 'P003','nama' : 'Alqoiru Humar','jam_buka' : '08.00','jam_tutup' : '21.00','kota' : 'Mataram','no_telpon' : '0898222938','keterangan' : 'Pembela Pidana'},
    {'kode' : 'R001','nama' : "Mc Donald's",'jam_buka' : '00.00', 'jam_tutup' : '00.00', 'kota' : 'Semarang', 'no_telpon' : '14045', 'keterangan':'Resto Cepat Saji'},
    {'kode' : 'R002','nama' : 'KFC','jam_buka' : '06.00', 'jam_tutup' : '21.00', 'kota' : 'Jakarta Selatan', 'no_telpon' : '14022', 'keterangan':'Resto Cepat Saji'},
    {'kode' : 'R003','nama' : 'OTI','jam_buka' : '08.00', 'jam_tutup' : '17.00', 'kota' : 'Bandung', 'no_telpon' : '12099', 'keterangan':'Resto Cepat Saji'},
    {'kode' : 'Pp001','nama' : 'Kamto','jam_buka' : '07.00','jam_tutup' : '22.00','kota' : 'Jogja','no_telpon' : '087767281738','keterangan':'Pembangunan Rumah'},
    {'kode' : 'Pp002','nama' : 'TB Marko','jam_buka' : '08.00','jam_tutup' : '21.00','kota' : 'Solo','no_telpon' : '08222222938','keterangan':'Toko Bangunan'}
]

kabkot = ['Semarang','Surabaya','Bandung','DIY', 'Jakarta Selatan', 'Jakarta Barat','Jakarta Pusat','Jakarta Timur','Bekasi','Demak','Aceh Barat','Aceh Barat Daya','Aceh Jaya','Aceh Selatan','Aceh Singkil','Aceh Tamiang ','Aceh Tenggara',' Aceh Timur','Aceh Utara','Bener Meriah','Bireuen','Gayo Lues','Nagan Raya','Pidie','Pidie Jaya','Simeulue','Banda Aceh','Langsa','Lhokseumawe',
          'Sabang','Subulussalam','Asahan','Batubara','Dairi','Deli Serdang','Humbang Hasundutan','Karo','Labuhanbatu','Labuhanbatu Selatan','Labuhanbatu Utara','Langkat','Mandailing Natal','Nias','Nias Barat', 'Nias Selatan', 'Nias Utara', 'Padang Lawas','Padang Lawas Utara',
          'Pakpak Bharat','Samosir','Serdang Bedagai','Simalungun','Tapanuli Selatan','Tapanuli Tengah','Tapanuli Utara','Toba Samosir','Binjai','Gunungsitoli','Medan','Padangsidempuan','Pematangsiantar','Sibolga','Tanjungbalai','Tebing Tinggi','Agam']

# * * * * * READ FUNCTION * * * * *
def ReadYellowBooks():
    k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

    print('\n\t\t\t\t\t\t+-------------------------+')
    print('\t\t\t\t\t\t|\tYELLOW PAGES\t  |')
    print('+'+'-'*117+'+')
    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
    print('+'+'-'*117+'+')

    for i in range(len(YellowPages)):
            print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'], YellowPages[i]['jam_buka'], YellowPages[i]['jam_tutup'],YellowPages[i]['kota'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan']))
            if i+1 == len(YellowPages):
                print('+'+'-'*117+'+')

def ReadPengacara():
    k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

    print('\n\t\t\t\t\t\t+-------------------------+')
    print('\t\t\t\t\t\t|\tYELLOW PAGES\t  |')
    print('+'+'-'*117+'+')
    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
    print('+'+'-'*117+'+')
    
    for i in range(len(YellowPages)):
        if 'P' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 4:
            print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'], YellowPages[i]['jam_buka'], YellowPages[i]['jam_tutup'],YellowPages[i]['kota'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
        else:
            continue
    if i+1 == len(YellowPages):
                print('+'+'-'*117+'+')
def ReadRestoran():
    k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

    print('\n\t\t\t\t\t\t+-------------------------+')
    print('\t\t\t\t\t\t|\tYELLOW PAGES\t  |')
    print('+'+'-'*117+'+')
    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
    print('+'+'-'*117+'+')
    
    for i in range(len(YellowPages)):
        if 'R' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 4:
            print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'], YellowPages[i]['jam_buka'], YellowPages[i]['jam_tutup'],YellowPages[i]['kota'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
        else:
            continue
    if i+1 == len(YellowPages):
                print('+'+'-'*117+'+')
def ReadPerbaikan():
    k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

    print('\n\t\t\t\t\t\t+-------------------------+')
    print('\t\t\t\t\t\t|\tYELLOW PAGES\t  |')
    print('+'+'-'*117+'+')
    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
    print('+'+'-'*117+'+')
    
    for i in range(len(YellowPages)):
        if 'Pp' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 5:
            print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'], YellowPages[i]['jam_buka'], YellowPages[i]['jam_tutup'],YellowPages[i]['kota'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
        else:
            continue
    if i+1 == len(YellowPages):
                print('+'+'-'*117+'+')

# * * * * *  FUNGSI JAM, KOTA, NO TELPON, KETERANGAN, dll * * * * *
def NamaPengacara():
    while True:
        namaPengacara = input('Masukkan Nama Pengacara (maks 20 karakter): ').title()
        special_characters = "!@#$%^&*()-+?_=,<>/[]}{:;" #tidak boleh menggunakan karakter spesial
        if len(namaPengacara)>20:
            print('Maks Karakter adalah 20 !!')
        else:
            res = any(chr.isdigit() for chr in namaPengacara)
            if res == False:
                if any(c in special_characters for c in namaPengacara): # JELASKAN ANY
                    print('Tidak boleh ada karakter spesial selain spasi (" ")')
                    continue
                else:
                    break
            else:
                print('Inputan Nama Pengacara Hanya Diperbolehkan Huruf!! ')
                continue
    return namaPengacara    
def nama_resto_perbaikan():
    while True:
        namaRestoranPerbaikan = input('Masukkan Nama Restoran (maks 20 karakter): ')
        if len(namaRestoranPerbaikan)>20:
            print('Maks Karakter adalah 20 !!')
        else:
            break
    return namaRestoranPerbaikan
def jamBuka():
    while True:
        try:
            input_jam_buka = int(input('Masukkan Jam Buka (hhmm) : '))
            if(input_jam_buka > 2400):
                print('Jam maksimal hanya 24.00')
                continue
            else:
                pindah = str(input_jam_buka).zfill(4)
                if(pindah[2]=='6' or pindah[2]=='7' or pindah[2]=='8' or pindah[2]=='9'): #ANTISIPASI MENIT KARENA MAKSIMAL HANYA 59
                    print('Menit maksimal adalah 59')
                    continue
                else:
                    if(pindah == '2400'): #KARENA TIDAK ADA PUKUL 24.00 MAKA AKAN DIGANTI PUKUL 00.00
                        jamB = '0000' 
                        break
                    else:
                        jamB = pindah
                        break
        except ValueError:
            print('Inputan Harus Angka!')   
    jam_buka = jamB[0:2]+'.'+jamB[2:4]
    return jam_buka
def jamTutup():
    while True:
        try:
            input_jam_tutup = int(input('Masukkan Jam Tutup (hhmm) : '))
            if(input_jam_tutup > 2400):
                print('Jam maksimal hanya 24.00') #ANTISIPASI JAM KARENA MAKSIMAL HANYA 24
                continue
            else:
                move = str(input_jam_tutup).zfill(4)
                if(move[2]=='6' or move[2]=='7' or move[2]=='8' or move[2]=='9'):#ANTISIPASI MENIT KARENA MAKSIMAL HANYA 59
                    print('Menit maksimal adalah 59')
                    continue
                else:
                    if(move == '2400'): #KARENA TIDAK ADA PUKUL 24.00 MAKA AKAN DIGANTI PUKUL 00.00
                        jamT = '0000' 
                        break
                    else:
                        jamT = move
                        break
        except ValueError:
            print('Inputan Harus Angka!')
    jam_tutup = jamT[0:2]+'.'+jamT[2:4]
    return jam_tutup
def namaKabKot():
    while True:
        KabKot = input('Masukkan Nama Kabupaten atau Kota : ')
        if KabKot in kabkot:
            break
        else:
            print('Nama Kabupaten atau Kota tidak ada di Indonesia!')
            continue
    return KabKot
def has_alpha(inputString):
    return any(char.isalpha() for char in inputString)
def noTlpn():
    while True:
        try:
            pilihno = int(input('Pilih 1 untuk no. perusahaan, pilih 2 untuk nomor biasa : '))
            if pilihno == 2:
                telpon = input('Masukkan no telpon (digit depan harus 0, min digit:10, maks digit:15): ')
                # x = re.search('[a-zA-Z]', telpon)
                if (has_alpha(telpon) == False):
                    if len(telpon)>=10 and len(telpon)<=15:
                        if telpon[0]=='0':
                            if in_dictlist('no_telpon',telpon,YellowPages)==True:
                                print('sudah ada, mohon ulangi')
                                continue
                            else:
                                break
                        else:
                            print('Jenis nomor ini harus diawali dengan 0')
                            continue
                    else:
                        print('Digit nomor tidak sesuai aturan!!')
                        continue
                else:
                    print('Inputan Hanya Boleh Angka!!')
                    continue
            elif pilihno == 1:
                telpon = input('Masukkan no telpon (maks digit : 15): ')
                if (has_alpha(telpon) == False):
                    if len(telpon)>=5 and len(telpon)<=15:
                        if in_dictlist('no_telpon',telpon,YellowPages)==True:
                            print('sudah ada, mohon ulangi')
                            continue
                        else:
                            break
                    else:
                        continue
                else:
                    print('Inputan Hanya Boleh ANGKA!!')
            else:
                print('Hanya Pilih 1 atau 2 SAJA!!')
        except ValueError:
            print('HANYA BOLEH ANGKA !')
    return telpon
def Ket():
    while True:
        keterangan = input('Masukkan Keterangan : ')
        if len(keterangan)>17:
            print(f'jumlah karakter {len(keterangan)}')
            print('Maksimal 17 Karakter!!!')
            continue
        elif len(keterangan)==0:
            print('Inputan tidak boleh kosong')
            continue
        else:
            print('Keterangan Berhasil Ditambah')
            break
    return keterangan        
def kelompokkan():
    while True:
        try:
            pilih = int(input("""Kelompok Berdasarkan : 
                    1. Kota/Kabupaten
                    2. Jam Buka
                    3. Jam Tutup
                    Pilih antara 1 - 3 : """))
            if pilih == 1:
                while True:
                    nama_kab_kota = input('Masukkan Nama Kota : ').title()
                    if nama_kab_kota in kabkot:
                        k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                        print('\n\t\t\t\t\t\t+-------------------------+')
                        print('\t\t\t\t\t\t|\tYELLOW PAGES\t  |')
                        print('+'+'-'*117+'+')
                        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
                        print('+'+'-'*117+'+')
                        cek = 0
                        for i in range(len(YellowPages)):
                            if nama_kab_kota == YellowPages[i]['kota']:
                                print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'], YellowPages[i]['jam_buka'], YellowPages[i]['jam_tutup'],YellowPages[i]['kota'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan']))
                                cek+=1
                        if i+1 == len(YellowPages):
                            print('+'+'-'*117+'+')
                        if cek == 0:
                            print('Kota Tersedia tapi Belum Pernah ada yang didaftarkan!')
                    else:
                        print('Nama Kota belum terdaftar atau tidak ada!')
                        break
                    break

            elif pilih == 2:
                jam_buka = str(jamBuka())
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                print('\n\t\t\t\t\t\t+-------------------------+')
                print('\t\t\t\t\t\t|\tYELLOW PAGES\t  |')
                print('+'+'-'*117+'+')
                print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
                print('+'+'-'*117+'+')
                cek = 0
                for i in range(len(YellowPages)):
                    if jam_buka == YellowPages[i]['jam_buka']:
                        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'], YellowPages[i]['jam_buka'], YellowPages[i]['jam_tutup'],YellowPages[i]['kota'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan']))
                        cek+=1
                if i+1 == len(YellowPages):
                    print('+'+'-'*117+'+')
                if cek == 0:
                    print(f'Belum ada pendaftar dengan jam buka pukul {jam_buka}')
            
            elif pilih == 3:
                jam_tutup = str(jamTutup())
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                print('\n\t\t\t\t\t\t+-------------------------+')
                print('\t\t\t\t\t\t|\tYELLOW PAGES\t  |')
                print('+'+'-'*117+'+')
                print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
                print('+'+'-'*117+'+')
                cek = 0
                for i in range(len(YellowPages)):
                    if jam_tutup == YellowPages[i]['jam_tutup']:
                        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'], YellowPages[i]['jam_buka'], YellowPages[i]['jam_tutup'],YellowPages[i]['kota'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan']))
                        cek+=1
                if i+1 == len(YellowPages):
                    print('+'+'-'*117+'+')
                if cek == 0:
                    print(f'Belum ada pendaftar dengan jam tutup pukul {jam_tutup}')

            else:
                print('pilih hanya nomer 1 - 3!!')
                continue
            break # BREAK FULL
        except ValueError:
            print('Inputan Harus Angka dari 1 - 3!!')
def search_Name_Pengacara(): #Dipisah dengan jenis lain karena memiliki aturan khusus dalam pembuatan namanya
    while True:
        nama = input('Masukkan Nama Yang Ingin Dicari : ').title()
        cek = 0
        k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'
        print('\n\t\t\t\t\t\t+-------------------------+')
        print('\t\t\t\t\t\t|\tYELLOW PAGES\t  |')
        print('+'+'-'*117+'+')
        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
        print('+'+'-'*117+'+')
        for i in range(len(YellowPages)):
            if nama in YellowPages[i]['nama']:
                print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'], YellowPages[i]['jam_buka'], YellowPages[i]['jam_tutup'],YellowPages[i]['kota'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
                cek+=1
            else:
                continue
        if i+1 == len(YellowPages):
            print('+'+'-'*117+'+')
            break
        if cek == 0:
            print('Nama Tidak Terdaftar')
            break
        elif cek != 0:
            print(f'Terdapat sejumlah {cek} nama {nama} di Yellow Books')
            break
def search_Name_Restoran_Perbaikan():
    while True:
        nama = input('Masukkan Restoran Yang Ingin Dicari : ').lower()
        cek = 0
        k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'
        print('\n\t\t\t\t\t\t+-------------------------+')
        print('\t\t\t\t\t\t|\tYELLOW PAGES\t  |')
        print('+'+'-'*117+'+')
        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
        print('+'+'-'*117+'+')
        for i in range(len(YellowPages)):
            if nama in YellowPages[i]['nama'].lower():
                print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'], YellowPages[i]['jam_buka'], YellowPages[i]['jam_tutup'],YellowPages[i]['kota'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
                cek+=1
            else:
                continue
        if i+1 == len(YellowPages):
            print('+'+'-'*117+'+')
            break
        if cek == 0:
            print('Nama Tidak Terdaftar')
            break
        elif cek != 0:
            print(f'Terdapat sejumlah {cek} nama {nama} di Yellow Books')
            break
def kelompokkan_pengacara():
    while True:
        try :
            komb = int(input("""Masukkan kombinasi tampilan : 
                            1. Kode & No. Telpon, Keterangan  
                            2. Nama & No. Telpon, Keterangan
                            3. Jam Buka, Jam Tutup & No. Telpon, Keterangan
                            Masukkan Input (1-3) : """))
            if(komb == 1):
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                print('\n\t+-------------------------+')
                print('\t|\tYELLOW PAGES\t  |')
                print('+'+'-'*42+'+')
                print('|{:5} | {:15}| {:17}|'.format(k,nt,ke))
                print('+'+'-'*42+'+')
                
                for i in range(len(YellowPages)):
                    if 'P' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 4:
                        print('|{:5} | {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
                    else:
                        continue
                if i+1 == len(YellowPages):
                            print('+'+'-'*42+'+')
                break
            elif(komb == 2):
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                print('\n\t\t\t+-------------------------+')
                print('\t\t\t|\tYELLOW PAGES\t  |')
                print('+'+'-'*67+'+')
                print('|{:30} | {:15}| {:17}|'.format(n,nt,ke))
                print('+'+'-'*67+'+')
                # print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
                for i in range(len(YellowPages)):
                    if 'P' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 4:
                        print('|{:30} | {:15}| {:17}|'.format(YellowPages[i]['nama'],YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
                    else:
                        continue
                if i+1 == len(YellowPages):
                    print('+'+'-'*67+'+')
                break
            elif(komb == 3):
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                print('\n\t\t+-------------------------+')
                print('\t\t|\tYELLOW PAGES\t  |')
                print('+'+'-'*58+'+')
                print('|{:10}| {:10}| {:15}| {:17}|'.format(jb,jt,nt,ke))
                print('+'+'-'*58+'+')
                # print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
                for i in range(len(YellowPages)):
                    if 'P' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 4:
                        print('|{:10}| {:10}| {:15}| {:17}|'.format(YellowPages[i]['jam_buka'],YellowPages[i]['jam_tutup'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
                    else:
                        continue
                if i+1 == len(YellowPages):
                    print('+'+'-'*58+'+')
                break
            else:
                print('Pilih hanya 1-3 !!')  
                continue
        except ValueError:
            print('Inputan Hanya Boleh Angka!!')
def kelompokkan_restoran():
    while True:
        try :
            komb = int(input("""Masukkan kombinasi tampilan : 
                            1. Kode & No. Telpon, Keterangan  
                            2. Nama & No. Telpon, Keterangan
                            3. Jam Buka, Jam Tutup & No. Telpon, Keterangan
                            Masukkan Input (1-3) : """))
            if(komb == 1):
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                print('\n\t+-------------------------+')
                print('\t|\tYELLOW PAGES\t  |')
                print('+'+'-'*42+'+')
                print('|{:5} | {:15}| {:17}|'.format(k,nt,ke))
                print('+'+'-'*42+'+')
                
                for i in range(len(YellowPages)):
                    if 'R' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 4:
                        print('|{:5} | {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
                    else:
                        continue
                if i+1 == len(YellowPages):
                            print('+'+'-'*42+'+')
                break
            elif(komb == 2):
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                print('\n\t\t\t+-------------------------+')
                print('\t\t\t|\tYELLOW PAGES\t  |')
                print('+'+'-'*67+'+')
                print('|{:30} | {:15}| {:17}|'.format(n,nt,ke))
                print('+'+'-'*67+'+')
                # print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
                for i in range(len(YellowPages)):
                    if 'R' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 4:
                        print('|{:30} | {:15}| {:17}|'.format(YellowPages[i]['nama'],YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
                    else:
                        continue
                if i+1 == len(YellowPages):
                    print('+'+'-'*67+'+')
                break
            elif(komb == 3):
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                print('\n\t\t+-------------------------+')
                print('\t\t|\tYELLOW PAGES\t  |')
                print('+'+'-'*58+'+')
                print('|{:10}| {:10}| {:15}| {:17}|'.format(jb,jt,nt,ke))
                print('+'+'-'*58+'+')
                # print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
                for i in range(len(YellowPages)):
                    if 'R' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 4:
                        print('|{:10}| {:10}| {:15}| {:17}|'.format(YellowPages[i]['jam_buka'],YellowPages[i]['jam_tutup'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
                    else:
                        continue
                if i+1 == len(YellowPages):
                    print('+'+'-'*58+'+')
                break
            else:
                print('Pilih hanya 1-3 !!')  
                continue
        except ValueError:
            print('Inputan Hanya Boleh Angka!!')
def kelompokkan_perbaikan():
    while True:
        try :
            komb = int(input("""Masukkan kombinasi tampilan : 
                            1. Kode & No. Telpon, Keterangan  
                            2. Nama & No. Telpon, Keterangan
                            3. Jam Buka, Jam Tutup & No. Telpon, Keterangan
                            Masukkan Input (1-3) : """))
            if(komb == 1):
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                print('\n\t+-------------------------+')
                print('\t|\tYELLOW PAGES\t  |')
                print('+'+'-'*42+'+')
                print('|{:5} | {:15}| {:17}|'.format(k,nt,ke))
                print('+'+'-'*42+'+')
                
                for i in range(len(YellowPages)):
                    if 'Pp' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 5:
                        print('|{:5} | {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
                    else:
                        continue
                if i+1 == len(YellowPages):
                            print('+'+'-'*42+'+')
                break
            elif(komb == 2):
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                print('\n\t\t\t+-------------------------+')
                print('\t\t\t|\tYELLOW PAGES\t  |')
                print('+'+'-'*67+'+')
                print('|{:30} | {:15}| {:17}|'.format(n,nt,ke))
                print('+'+'-'*67+'+')
                # print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
                for i in range(len(YellowPages)):
                    if 'Pp' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 5:
                        print('|{:30} | {:15}| {:17}|'.format(YellowPages[i]['nama'],YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
                    else:
                        continue
                if i+1 == len(YellowPages):
                    print('+'+'-'*67+'+')
                break
            elif(komb == 3):
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ke='Keterangan'

                print('\n\t\t+-------------------------+')
                print('\t\t|\tYELLOW PAGES\t  |')
                print('+'+'-'*58+'+')
                print('|{:10}| {:10}| {:15}| {:17}|'.format(jb,jt,nt,ke))
                print('+'+'-'*58+'+')
                # print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
                for i in range(len(YellowPages)):
                    if 'Pp' in YellowPages[i]['kode'] and len(YellowPages[i]['kode']) == 5:
                        print('|{:10}| {:10}| {:15}| {:17}|'.format(YellowPages[i]['jam_buka'],YellowPages[i]['jam_tutup'], YellowPages[i]['no_telpon'], YellowPages[i]['keterangan'])) 
                    else:
                        continue
                if i+1 == len(YellowPages):
                    print('+'+'-'*58+'+')
                break
            else:
                print('Pilih hanya 1-3 !!')  
                continue
        except ValueError:
            print('Inputan Hanya Boleh Angka!!')
def sort_by_kode():
    newlist = sorted(YellowPages, key=lambda d: d['kode'])

    k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota'; ke = 'Keterangan'
    print('\t\t\t\t\t\t  +---------+')
    print('\t\t\t\t\t\t  |KODE URUT|')

    print('+'+'-'*116+'+')
    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
    print('+'+'-'*116+'+')
    for i in range(len(newlist)):
        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(newlist[i]['kode'],newlist[i]['nama'],newlist[i]['jam_buka'],newlist[i]['jam_tutup'],newlist[i]['kota'], newlist[i]['no_telpon'], newlist[i]['keterangan']))
        if i+1 == len(newlist):
            print('+'+'-'*116+'+')
            break
def sort_by_name():
    newlist = sorted(YellowPages, key=lambda d: d['nama'])#JELASIN

    k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota'; ke = 'Keterangan'
    print('\t\t\t\t\t\t  +---------+')
    print('\t\t\t\t\t\t  |NAMA URUT|')

    print('+'+'-'*116+'+')
    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
    print('+'+'-'*116+'+')
    for i in range(len(newlist)):
        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(newlist[i]['kode'],newlist[i]['nama'],newlist[i]['jam_buka'],newlist[i]['jam_tutup'],newlist[i]['kota'], newlist[i]['no_telpon'], newlist[i]['keterangan']))
        if i+1 == len(newlist):
            print('+'+'-'*116+'+')
            break
def sort_by_jam_buka():
    newlist = sorted(YellowPages, key=lambda d: d['jam_buka'])#JELASIN

    k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota'; ke = 'Keterangan'
    print('\t\t\t\t\t\t  +-------------+')
    print('\t\t\t\t\t\t  |JAM BUKA URUT|')

    print('+'+'-'*116+'+')
    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
    print('+'+'-'*116+'+')
    for i in range(len(newlist)):
        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(newlist[i]['kode'],newlist[i]['nama'],newlist[i]['jam_buka'],newlist[i]['jam_tutup'],newlist[i]['kota'], newlist[i]['no_telpon'], newlist[i]['keterangan']))
        if i+1 == len(newlist):
            print('+'+'-'*116+'+')
            break
def sort_by_jam_tutup():
    newlist = sorted(YellowPages, key=lambda d: d['jam_tutup'])#JELASIN

    k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota'; ke = 'Keterangan'
    print('\t\t\t\t\t\t  +--------------+')
    print('\t\t\t\t\t\t  |JAM TUTUP URUT|')

    print('+'+'-'*116+'+')
    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
    print('+'+'-'*116+'+')
    for i in range(len(newlist)):
        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(newlist[i]['kode'],newlist[i]['nama'],newlist[i]['jam_buka'],newlist[i]['jam_tutup'],newlist[i]['kota'], newlist[i]['no_telpon'], newlist[i]['keterangan']))
        if i+1 == len(newlist):
            print('+'+'-'*116+'+')
            break
def sort_by_kabkot():
    newlist = sorted(YellowPages, key=lambda d: d['kota'])#JELASIN

    k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota'; ke = 'Keterangan'
    print('\t\t\t\t\t\t  +---------------------+')
    print('\t\t\t\t\t\t  |KABUPATEN / KOTA URUT|')

    print('+'+'-'*116+'+')
    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ke))
    print('+'+'-'*116+'+')
    for i in range(len(newlist)):
        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(newlist[i]['kode'],newlist[i]['nama'],newlist[i]['jam_buka'],newlist[i]['jam_tutup'],newlist[i]['kota'], newlist[i]['no_telpon'], newlist[i]['keterangan']))
        if i+1 == len(newlist):
            print('+'+'-'*116+'+')
            break

# * * * * *  CREATE FUNCTION * * * * *
def CreateYellowBooks():
    #MEMBUAT UNIQUE KEY SECARA OTOMATIS
    while True:
        try:
            pilih = int(input("""Pilih Kategori Yellow Books Yang Akan Ditambah :
                              1. Pengacara
                              2. Restoran
                              3. Perbaikan
                              Masukkan Pilihan (1-3) : """))
            if pilih == 1:
                while True:
                    try:
                        no_pengacara = int(input('Masukkan Nomor Kode Yang Diinginkan (maksimal 999):'))
                        if(no_pengacara > 999):
                            print('Inputan Maks Adalah 999')
                            continue
                        else:
                            strNoPengacara = str(no_pengacara)
                            kodePengacara = 'P'+strNoPengacara.zfill(3)
                            if in_dictlist('kode',kodePengacara,YellowPages)==True:
                                print('KODE sudah ada, mohon ulangi!')
                                continue
                            else:
                                break
                    except ValueError:
                        print('Inputan Harus Angka')

                #INPUT NAMA PENGACARA
                #NAMA hanya boleh Huruf
                namaPengacara = str(NamaPengacara())
                #INPUT JAM BUKA OPERASIONAL YANG MASUK AKAL
                jam_buka = str(jamBuka())
                jam_tutup = str(jamTutup())
                kabkot = str(namaKabKot())
                telpon = str(noTlpn())
                ket = str(Ket())
                YellowPages.append({'kode':kodePengacara,'nama':namaPengacara,'jam_buka':jam_buka,'jam_tutup':jam_tutup,'kota':kabkot,'no_telpon':telpon,'keterangan':ket })
            
            #JIKA MEMILIH RESTORAN
            if pilih == 2:
                while True:
                    try:
                        no_restoran = int(input('Masukkan Nomor Kode Yang Diinginkan (maksimal 999):'))
                        if(no_restoran > 999):
                            print('Inputan Maks Adalah 999')
                            continue
                        else:
                            strNoRestoran = str(no_restoran)
                            kodeRestoran = 'R'+strNoRestoran.zfill(3)
                            if in_dictlist('kode',kodeRestoran,YellowPages)==True:
                                print('KODE sudah ada, mohon ulangi!')
                                continue
                            else:
                                break
                    except ValueError:
                        print('Inputan Harus Angka')

                #NAMA boleh dengan tanda baca
                while True:
                        namaRestoran = input('Masukkan Nama Restoran (maks 20 karakter): ').title()
                        #special_characters = "!@#$%^&*()-+?_=,<>/[]}{:;" #tidak boleh menggunakan karakter spesial
                        if len(namaRestoran)>20:
                            print('Maks Karakter adalah 20 !!')
                        else:
                            break
                               
                #INPUT JAM BUKA OPERASIONAL YANG MASUK AKAL
                jam_buka = str(jamBuka())
                jam_tutup = str(jamTutup())
                kabkot = str(namaKabKot())
                telpon = str(noTlpn())
                ket = str(Ket())
                YellowPages.append({'kode':kodeRestoran,'nama':namaRestoran,'jam_buka':jam_buka,'jam_tutup':jam_tutup,'kota':kabkot,'no_telpon':telpon,'keterangan':ket })

            #MEMBUAT DAFTAR PERBAIKAN
            if pilih == 3:
                while True:
                    try:
                        no_perbaikan = int(input('Masukkan Nomor Kode Yang Diinginkan (maksimal 999):'))
                        if(no_perbaikan > 999):
                            print('Inputan Maks Adalah 999')
                            continue
                        else:
                            strNoPerbaikan = str(no_perbaikan)
                            kodePerbaikan = 'Pp'+strNoPerbaikan.zfill(3)
                            if in_dictlist('kode',kodePerbaikan,YellowPages)==True:
                                print('KODE sudah ada, mohon ulangi!')
                                continue
                            else:
                                break
                    except ValueError:
                        print('Inputan Harus Angka')

                #NAMA boleh dengan tanda baca
                while True:
                        namaPerbaikan = input('Masukkan Nama Orang / Perusahaan (maks 20 karakter): ').title()
                        #special_characters = "!@#$%^&*()-+?_=,<>/[]}{:;" #tidak boleh menggunakan karakter spesial
                        if len(namaPerbaikan)>20:
                            print('Maks Karakter adalah 20 !!')
                        else:
                            break
                               
                #INPUT JAM BUKA OPERASIONAL YANG MASUK AKAL
                jam_buka = str(jamBuka())
                jam_tutup = str(jamTutup())
                kabkot = str(namaKabKot())
                telpon = str(noTlpn())
                ket = str(Ket())
                YellowPages.append({'kode':kodePerbaikan,'nama':namaPerbaikan,'jam_buka':jam_buka,'jam_tutup':jam_tutup,'kota':kabkot,'no_telpon':telpon,'keterangan':ket })

        except ValueError:
            print('Inputan Harus Angka Dari 1 - 3')
        break

# * * * * * DELETE FUNCTION * * * * *
def DeleteYellowBooks():
    while True:
        while True:
            haps = input("Masukkan Kode yang akan dihapus (EX : 'P','R','Pp') : ")
            if haps == 'P' or haps == 'R' or haps == 'Pp':
                digit_kode = int(input('Masukkan digit Kode (maks 999) : '))
                if digit_kode > 999 or digit_kode < 0:
                    print('Maksimal 999 !')
                    continue
                else:
                    strdigit_kode = str(digit_kode).zfill(3)
                    break
            else:
                print('Kode salah!')
                continue
        hapus = haps+strdigit_kode

        if in_dictlist('kode',hapus,YellowPages)==True:
            i = 0
            while i<=len(YellowPages):
                if(hapus == YellowPages[i]['kode']):
                    del YellowPages[i]
                    break
                else:
                    i+=1
                    continue
        else:
            continue
        break

# * * * * * UPDATE FUNCTION * * * * *
def UpdateYellowBooks():
    while True:
        kodeinput = input("Masukkan Kode yang mau diganti : ")
        if(kodeinput == 'P'):
            while True:
                try:
                    digit = int(input('Masukkan Digit Kode Yang Akan Diganti (maks 999): '))
                    if digit > 999 or digit < 0:
                        print('Digit melebihi batas atau tidak ada!')
                        continue
                    else:
                        strdigit = str(digit).zfill(3)
                        kode = 'P'+strdigit
                        break
                except ValueError:
                    print('Inputan Harus Angka Dari 1 - 999!')
                    continue
            #TAMPILKAN ROW YANG MAU DIGANTI
            if in_dictlist('kode',kode,YellowPages)==True:
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ket='Keterangan'
                print('+'+'-'*117+'+')
                print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ket))
                print('+'+'-'*117+'+')
                for i in range(len(YellowPages)):
                    if(kode == YellowPages[i]['kode']):
                        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'],YellowPages[i]['jam_buka'],YellowPages[i]['jam_tutup'],YellowPages[i]['kota'],YellowPages[i]['no_telpon'],YellowPages[i]['keterangan']))
                        break
                    else:
                        continue
            else:
                print('Data TIDAK TERSEDIA!!')
                break
            
            
            while True:
                try:
                    kolom = int(input("""Pilih kolom yang hendak diganti:
                            1. Nama
                            2. Jam Buka
                            3. Jam Tutup
                            4. Kota
                            5. No. Telpon
                            6. Keterangan
                            Pilih antara 1-6 : """))
                    if kolom == 1:
                        gantinama = str(NamaPengacara())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['nama'] = gantinama 
                                break
                            else:
                                continue
                        break
                    elif kolom == 2:
                        jam_buka = str(jamBuka())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['jam_buka'] =jam_buka 
                                break
                            else:
                                continue
                        break
                    elif kolom == 3:
                        jam_tutup = str(jam_tutup())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['jam_tutup'] =jam_tutup 
                                break
                            else:
                                continue
                        break
                    elif kolom == 4:
                        kota = str(namaKabKot())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['kota'] = kota 
                                break
                            else:
                                continue
                        break
                    elif kolom == 5:
                        nomer = str(noTlpn())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['no_telpon'] = nomer 
                                break
                            else:
                                continue
                        break
                    elif kolom == 6:
                        ket = str(Ket())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['keterangan'] = ket 
                                break
                            else:
                                continue
                        break
                except ValueError:
                    print('Inputan Hanya Boleh Angka dari 1-6 !')
                    continue
            k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ket='Keterangan'
            print('+'+'-'*117+'+')
            print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ket))
            print('+'+'-'*117+'+')
            for i in range(len(YellowPages)):
                if(kode == YellowPages[i]['kode']):
                    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'],YellowPages[i]['jam_buka'],YellowPages[i]['jam_tutup'],YellowPages[i]['kota'],YellowPages[i]['no_telpon'],YellowPages[i]['keterangan']))
                    break
                else:
                    continue 
            print('+'+'-'*117+'+')
            print('Data Berhasil Dirubah !!')           
        elif(kodeinput == 'R'):
            while True:
                try:
                    digit = int(input('Masukkan Digit Kode Yang Akan Diganti (maks 999): '))
                    if digit > 999 or digit < 0:
                        print('Digit melebihi batas atau tidak ada!')
                        continue
                    else:
                        strdigit = str(digit).zfill(3)
                        kode = 'R'+strdigit
                        break
                except ValueError:
                    print('Inputan Harus Angka Dari 1 - 999!')
                    continue
            #TAMPILKAN ROW YANG MAU DIGANTI
            if in_dictlist('kode',kode,YellowPages)==True:
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ket='Keterangan'
                print('+'+'-'*117+'+')
                print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ket))
                print('+'+'-'*117+'+')
                for i in range(len(YellowPages)):
                    if(kode == YellowPages[i]['kode']):
                        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'],YellowPages[i]['jam_buka'],YellowPages[i]['jam_tutup'],YellowPages[i]['kota'],YellowPages[i]['no_telpon'],YellowPages[i]['keterangan']))
                        break
                    else:
                        continue
            else:
                print('Data TIDAK TERSEDIA!!')
                break
            
            while True:
                try:
                    kolom = int(input("""Pilih kolom yang hendak diganti:
                            1. Nama
                            2. Jam Buka
                            3. Jam Tutup
                            4. Kota
                            5. No. Telpon
                            6. Keterangan
                            Pilih antara 1-6 : """))
                    if kolom == 1:
                        gantinama_restoran = str(nama_resto_perbaikan())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['nama'] = gantinama_restoran
                                break
                            else:
                                continue
                        break
                    elif kolom == 2:
                        jam_buka = str(jamBuka())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['jam_buka'] =jam_buka 
                                break
                            else:
                                continue
                        break
                    elif kolom == 3:
                        jam_tutup = str(jam_tutup())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['jam_tutup'] =jam_tutup 
                                break
                            else:
                                continue
                        break
                    elif kolom == 4:
                        kota = str(namaKabKot())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['kota'] = kota 
                                break
                            else:
                                continue
                        break
                    elif kolom == 5:
                        nomer = str(noTlpn())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['no_telpon'] = nomer 
                                break
                            else:
                                continue
                        break
                    elif kolom == 6:
                        ket = str(Ket())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['keterangan'] = ket 
                                break
                            else:
                                continue
                        break
                except ValueError:
                    print('Inputan Hanya Boleh Angka dari 1-6 !')
                    continue
            k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ket='Keterangan'
            print('+'+'-'*117+'+')
            print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ket))
            print('+'+'-'*117+'+')
            for i in range(len(YellowPages)):
                if(kode == YellowPages[i]['kode']):
                    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'],YellowPages[i]['jam_buka'],YellowPages[i]['jam_tutup'],YellowPages[i]['kota'],YellowPages[i]['no_telpon'],YellowPages[i]['keterangan']))
                    break
                else:
                    continue 
            print('+'+'-'*117+'+')
            print('Data Berhasil Dirubah !!')
        #JIKA KODENYA KODE PERBAIKAN
        elif(kodeinput == 'Pp'):
            while True:
                try:
                    digit = int(input('Masukkan Digit Kode Yang Akan Diganti (maks 999): '))
                    if digit > 999 or digit < 0:
                        print('Digit melebihi batas atau tidak ada!')
                        continue
                    else:
                        strdigit = str(digit).zfill(3)
                        kode = 'Pp'+strdigit
                        break
                except ValueError:
                    print('Inputan Harus Angka Dari 1 - 999!')
                    continue
            #TAMPILKAN ROW YANG MAU DIGANTI
            if in_dictlist('kode',kode,YellowPages)==True:
                k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ket='Keterangan'
                print('+'+'-'*117+'+')
                print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ket))
                print('+'+'-'*117+'+')
                for i in range(len(YellowPages)):
                    if(kode == YellowPages[i]['kode']):
                        print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'],YellowPages[i]['jam_buka'],YellowPages[i]['jam_tutup'],YellowPages[i]['kota'],YellowPages[i]['no_telpon'],YellowPages[i]['keterangan']))
                        break
                    else:
                        continue
            else:
                print('Data TIDAK TERSEDIA!!')
                break
            
            while True:
                try:
                    kolom = int(input("""Pilih kolom yang hendak diganti:
                            1. Nama
                            2. Jam Buka
                            3. Jam Tutup
                            4. Kota
                            5. No. Telpon
                            6. Keterangan
                            Pilih antara 1-6 : """))
                    if kolom == 1:
                        gantinama_perbaikan = str(nama_resto_perbaikan())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['nama'] = gantinama_perbaikan
                                break
                            else:
                                continue
                        break
                    elif kolom == 2:
                        jam_buka = str(jamBuka())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['jam_buka'] =jam_buka 
                                break
                            else:
                                continue
                        break
                    elif kolom == 3:
                        jam_tutup = str(jamTutup())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['jam_tutup'] =jam_tutup 
                                break
                            else:
                                continue
                        break
                    elif kolom == 4:
                        kota = str(namaKabKot())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['kota'] = kota 
                                break
                            else:
                                continue
                        break
                    elif kolom == 5:
                        nomer = str(noTlpn())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['no_telpon'] = nomer 
                                break
                            else:
                                continue
                        break
                    elif kolom == 6:
                        ket = str(Ket())
                        for i in range(len(YellowPages)):
                            if(kode == YellowPages[i]['kode']):
                                YellowPages[i]['keterangan'] = ket 
                                break
                            else:
                                continue
                        break
                    
                except ValueError:
                    print('Inputan Hanya Boleh Angka dari 1-6 !')
                    continue
            k='Kode'; n='Nama'; jt='Jam Tutup'; nt='No. Telpon'; jb='Jam Buka' ; ko='Kab/Kota' ; ket='Keterangan'
            print('+'+'-'*117+'+')
            print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(k,n,jb,jt,ko,nt,ket))
            print('+'+'-'*117+'+')
            for i in range(len(YellowPages)):
                if(kode == YellowPages[i]['kode']):
                    print('|{:5} | {:30}| {:10}| {:10}| {:17}| {:15}| {:17}|'.format(YellowPages[i]['kode'],YellowPages[i]['nama'],YellowPages[i]['jam_buka'],YellowPages[i]['jam_tutup'],YellowPages[i]['kota'],YellowPages[i]['no_telpon'],YellowPages[i]['keterangan']))
                    break
                else:
                    continue 
            print('+'+'-'*117+'+')
            print('Data Berhasil Dirubah !!')
        else:
            print("Kode Hanya ada 'P','R' dan 'Pp'")
            continue
        break
# * * * FUNGSI CEK ISI List Dictionary * * *
def in_dictlist(key, value, my_dictlist):
    for entry in my_dictlist:
        if entry[key] == value:
            return True
    return False


# * * * * * * * MENU UTAMA * * * * * * *
judul = '''\
██╗   ██╗███████╗██╗     ██╗      ██████╗ ██╗    ██╗ 
╚██╗ ██╔╝██╔════╝██║     ██║     ██╔═══██╗██║    ██║ 
 ╚████╔╝ █████╗  ██║     ██║     ██║   ██║██║ █╗ ██║ 
  ╚██╔╝  ██╔══╝  ██║     ██║     ██║   ██║██║███╗██║ 
   ██║   ███████╗███████╗███████╗╚██████╔╝╚███╔███╔╝ 
   ╚═╝   ╚══════╝╚══════╝╚══════╝ ╚═════╝  ╚══╝╚══╝  
                                                     
██████╗  █████╗  ██████╗ ███████╗███████╗            
██╔══██╗██╔══██╗██╔════╝ ██╔════╝██╔════╝            
██████╔╝███████║██║  ███╗█████╗  ███████╗█████╗█████╗
██╔═══╝ ██╔══██║██║   ██║██╔══╝  ╚════██║╚════╝╚════╝
██║     ██║  ██║╚██████╔╝███████╗███████║     
-----------------------------------------------------'''

terimakasih = '''\
   ████████╗███████╗██████╗ ██╗███╗   ███╗ █████╗     ██╗  ██╗ █████╗ ███████╗██╗██╗  ██╗      
   ╚══██╔══╝██╔════╝██╔══██╗██║████╗ ████║██╔══██╗    ██║ ██╔╝██╔══██╗██╔════╝██║██║  ██║      
█████╗██║   █████╗  ██████╔╝██║██╔████╔██║███████║    █████╔╝ ███████║███████╗██║███████║█████╗
╚════╝██║   ██╔══╝  ██╔══██╗██║██║╚██╔╝██║██╔══██║    ██╔═██╗ ██╔══██║╚════██║██║██╔══██║╚════╝
      ██║   ███████╗██║  ██║██║██║ ╚═╝ ██║██║  ██║    ██║  ██╗██║  ██║███████║██║██║  ██║      
      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝                                                                                                     
'''



while True:
    print(judul)
    print('''Menu Yang Tersedia : 
1. Tampilkan Data Yellow Pages
2. Edit Data Yellow Pages
3. Hapus Data Yellow Pages
4. Tambahkan Data Yellow Pages        
5. Exit''')
    try:
        pilih_menu_awal = int(input('Masukkan Pilihan yang tersedia (1-5) : '))
        if pilih_menu_awal == 1: 
            while True:
                try:    
                    print('''Menu Tampil : 
1. Tampilkan Seluruh Yellow Pages
2. Yellow Pages Pengacara
3. Yellow Pages Restoran
4. Yellow Pages Perbaikan
5. Kembali''')
                    pilih_menu_tampil = int(input('Masukkan Pilihan Yang Tersedia (1-5) : '))
                    if pilih_menu_tampil == 1:
                        ReadYellowBooks()
                        while True:
                            pilih_sort = input('\nIngin Mengurutkan Yellow Pages ? (y/n) : ').lower()
                            if pilih_sort == 'y':
                                print('''Urutkan Berdasarkan :
1. Kode
2. Nama
3. Jam Buka
4. Jam Tutup
5. Kota''')
                                while True:
                                    try:
                                        sort=int(input('Input antara 1-5 : '))
                                        if sort == 1:
                                            sort_by_kode()
                                            print('Di atas adalah pengurutan berdasarkan Kode')
                                        elif sort == 2:
                                            sort_by_name()
                                            print('Di atas adalah pengurutan berdasarkan Nama')
                                        elif sort == 3:
                                            sort_by_jam_buka()
                                            print('Di atas adalah pengurutan berdasarkan Jam Buka')
                                        elif sort == 4:
                                            sort_by_jam_tutup()
                                            print('Di atas adalah pengurutan berdasarkan Jam Tutup')
                                        elif sort == 5:
                                            sort_by_kabkot()
                                            print('Di atas adalah pengurutan berdasarkan Kabupaten / Kota')    
                                        else:
                                            print('Inputan Hanya 1-5!!')
                                            continue
                                        break
                                    except ValueError:
                                        print('Inputan Hanya Boleh Angka!!!')
                                    break
                            elif pilih_sort == 'n':
                                break
                            else:
                                print('INPUTAN Hanya boleh y atau n!!')
                    elif pilih_menu_tampil == 2:
                        ReadPengacara()
                        while True:
                            print('''Menu Yellow Pages Pengacara:
1. Pengelompokkan Kolom
2. Mencari Data Berdasarkan Nama
3. Kembali''')              
                            try:
                                pilih_menu_tampil_1 = int(input('Masukkan Pilihan Yang Tersedia (1-3) : '))
                                if pilih_menu_tampil_1 == 1:
                                    while True:
                                        pilih_menu_tampil_1_1 = input('Ingin Mengelompokkan Data? (y/n) : ').lower()
                                        if pilih_menu_tampil_1_1 == 'y':
                                            kelompokkan_pengacara()
                                            print('Data Berhasil Dikelompokkan !')
                                            continue
                                        elif pilih_menu_tampil_1_1 == 'n':
                                            break
                                        else:
                                            print('Inputan Hanya Boleh y/n!!')  
                                            continue
                                elif pilih_menu_tampil_1 ==2:
                                    while True:
                                        pilih_menu_tampil_1_2 = input('Ingin Mencari Data? (y/n) : ').lower()
                                        if pilih_menu_tampil_1_2 == 'y':
                                            search_Name_Pengacara()
                                            print('Di atas adalah hasil pencarian dengan kata kunci') #EDIT DI FUNGSI SEARCH
                                            continue
                                        elif pilih_menu_tampil_1_2 == 'n':
                                            break
                                        else:
                                            print('Inputan Hanya Boleh y/n!!')  
                                            continue
                                elif pilih_menu_tampil_1 == 3:
                                    break
                                break
                            except ValueError:
                                print('Inputan hanya boleh ANGKA!!')
             
                    elif pilih_menu_tampil == 3:
                        ReadRestoran()
                        while True:
                            print('''Menu Yellow Pages Restoran:
1. Pengelompokkan Kolom
2. Mencari Data Berdasarkan Nama
3. Kembali''')              
                            try:
                                pilih_menu_tampil_3 = int(input('Masukkan Pilihan Yang Tersedia (1-3) : '))
                                if pilih_menu_tampil_3 == 1:
                                    while True:
                                        pilih_menu_tampil_3_1 = input('Ingin Mengelompokkan Data? (y/n) : ').lower
                                        if pilih_menu_tampil_3_1 == 'y':
                                            kelompokkan_restoran()
                                            print('Data Berhasil Dikelompokkan !')
                                            continue
                                        elif pilih_menu_tampil_3_1 == 'n':
                                            break
                                        else:
                                            print('Inputan Hanya Boleh y/n!!')  
                                            continue
                                elif pilih_menu_tampil_3 ==2:
                                    while True:
                                        pilih_menu_tampil_3_2 = input('Ingin Mencari Data? (y/n) : ').lower()
                                        if pilih_menu_tampil_3_2 == 'y':
                                            search_Name_Restoran_Perbaikan()
                                            print('Di atas adalah hasil pencarian dengan kata kunci') 
                                            continue
                                        elif pilih_menu_tampil_3_2 == 'n':
                                            break
                                        else:
                                            print('Inputan Hanya Boleh y/n!!')  
                                            continue
                                elif pilih_menu_tampil_1 == 3:
                                    break
                                break
                            except ValueError:
                                print('Inputan hanya boleh ANGKA!!')
                    elif pilih_menu_tampil == 4:
                        ReadPerbaikan()
                        while True:
                            print('''Menu Yellow Pages Pengacara:
1. Pengelompokkan Kolom
2. Mencari Data Berdasarkan Nama
3. Kembali''')              
                            try:
                                pilih_menu_tampil_4 = int(input('Masukkan Pilihan Yang Tersedia (1-3) : '))
                                if pilih_menu_tampil_4 == 1:
                                    while True:
                                        pilih_menu_tampil_4_1 = input('Ingin Mengelompokkan Data? (y/n) : ').lower()
                                        if pilih_menu_tampil_4_1 == 'y':
                                            kelompokkan_perbaikan()
                                            print('Data Berhasil Dikelompokkan !')
                                            continue
                                        elif pilih_menu_tampil_4_1 == 'n':
                                            break
                                        else:
                                            print('Inputan Hanya Boleh y/n!!')  
                                            continue
                                elif pilih_menu_tampil_4 ==2:
                                    while True:
                                        pilih_menu_tampil_3_2 = input('Ingin Mencari Data? (y/n) : ')
                                        if pilih_menu_tampil_3_2 == 'y':
                                            search_Name_Restoran_Perbaikan()
                                            print('Di atas adalah hasil pencarian dengan kata kunci') 
                                            continue
                                        elif pilih_menu_tampil_3_2 == 'n':
                                            break
                                        else:
                                            print('Inputan Hanya Boleh y/n!!')  
                                            continue
                                elif pilih_menu_tampil_4 == 3:
                                    break
                                break
                            except ValueError:
                                print('Inputan hanya boleh ANGKA!!')
                    elif pilih_menu_tampil == 5:
                        break
                    else:
                        print('Inputan Angka hanya 1-5')
                except ValueError:
                    print('Inputan harus ANGKA!!')
                    
        elif pilih_menu_awal == 2:
            ReadYellowBooks()
            while True:
                edit = input('Ingin Edit Data ? (y/n) : ').lower()
                if edit == 'y':
                    UpdateYellowBooks()
                    continue
                elif edit == 'n':
                    break
                else:
                    print('Inputan Hanya Boleh y/n!!!')
                    continue
        elif pilih_menu_awal == 3:
            ReadYellowBooks()
            while True:
                edit = input('Ingin Hapus Data ? (y/n) : ').lower()
                if edit == 'y':
                    DeleteYellowBooks()
                    ReadYellowBooks()
                    print('Data Berhasil Dihapus')
                    continue
                elif edit == 'n':
                    break
                else:
                    print('Inputan Hanya Boleh y/n!!!')
                    continue
        elif pilih_menu_awal == 4:
            while True:
                tambah = input('Ingin Menambah Data ? (y/n) : ')
                if tambah == 'y':
                    CreateYellowBooks()
                    print('Data Berhasil Ditambahkan!')
                elif tambah == 'n':
                    break
                else:
                    print('Inputan Hanya Boleh y atau n!!')
        elif pilih_menu_awal == 5:
            print()
            print(terimakasih)
            break
        else:
            print('Input Hanya 1 - 5 !!')
           
    except ValueError:
        print('INPUTAN HANYA BOLEH ANGKA!!!')

