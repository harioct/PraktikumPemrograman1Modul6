def Biodata(tahunLahir, A, B):
    tahun_sekarang = 2020
    tahunLahir = int(tahunLahir)
    print("\nPerkenalkan Nama Saya :", A)
    print("Umur Saya :", tahun_sekarang-tahunLahir)
    print("Saya Adalah Angkatan :", tahun_sekarang)
    print("Asal Saya dari :", B)

tahunLahir = int(input())
A = input()
B = input()
Biodata(tahunLahir, A, B)