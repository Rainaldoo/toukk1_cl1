import os

def urutasc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)

def urutdesc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)

z="y"
while (z=="y") or (z=="Y"):
    os.system("cls")
    print("Program Mengurutkan Data")
    print("Dengan Metode bubble Sort")
    a=int(input("Masukkan Bilangan Ke 1 : "))
    b=int(input("Masukkan Bilangan Ke 2 : "))
    c=int(input("Masukkan Bilangan Ke 3 : "))
    d=int(input("Masukkan Bilangan Ke 4 : "))
    e=int(input("Masukkan Bilangan Ke 5 : "))
    f=int(input("Masukkan Bilangan Ke 6 : "))
    g=int(input("Masukkan Bilangan Ke 7 : "))
    h=int(input("Masukkan Bilangan Ke 8 : "))
    i=int(input("Masukkan Bilangan Ke 9 : "))
    j=int(input("Masukkan Bilangan Ke 10 : "))

    urut=[a,b,c,d,e,f,g,h,i,j]

    print("================================")
    print("Pilihan metode pengurutan:")
    print("1. Sorting ascending")
    print("2. Sorting descending")
    pilih=int(input("Metode yang dipilih : "))
    print("================================")
    print("Data sebelum diurutkan :")
    print(urut)
    print("Data setelah diurutkan :")

    if pilih==1:
        urutasc(urut)
    elif pilih==2:
        urutdesc(urut)
    else:
        print("Tidak ada pilihannya")

    z=input("Kembali ke menu utama (Y/N)? : ")

print("Terima Kasih :)")