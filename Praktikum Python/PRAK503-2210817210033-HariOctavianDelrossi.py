def maksimal (maks, nilai):
    if(maks > nilai): 
        return maks
    else: 
        return nilai

def minimal (min, nilai):
    if(min < nilai) : 
        return min
    else: 
        return nilai

batas = 0 
maks = -100000
min = 100000 
bilangan = int(input())
while batas < bilangan:
    nilai = map(int,input().split())
    for angka in nilai:
        maks = maksimal(maks, angka)
        min = minimal(min, angka)
        batas+=1
    print("%d %d"%(maks,min))