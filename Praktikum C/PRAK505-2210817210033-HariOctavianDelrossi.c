#include<stdio.h>
void Biodata(int tahunLahir, char A[20], char B[15]){
    int tahun_sekarang = 2020;
    printf("\nPerkenalkan Nama Saya : %s\n", A);
    printf("Umur Saya : %d\n", tahun_sekarang - tahunLahir);
    printf("Saya Adalah Angkatan : %d\n", tahun_sekarang);
    printf("Asal Saya dari : %s", B);
}
int main(){
    int tahunLahir;
    char A[20], B[15];
    scanf("%d",&tahunLahir);
    scanf(" %[^\n]",&A);
    scanf(" %[^\n]",&B);
    Biodata(tahunLahir, A, B);
    return 0;
}