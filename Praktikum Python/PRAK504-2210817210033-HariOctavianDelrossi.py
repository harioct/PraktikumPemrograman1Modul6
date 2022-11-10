def reverse (a):
    reverse = 0 
    while a != 0:
        b = a % 10
        reverse = reverse * 10 + b
        a //= 10
    return reverse

A, B = map(int,input().split())
A = reverse(A)
B = reverse(B)
C = A + B
print("%d"%(reverse(C)))