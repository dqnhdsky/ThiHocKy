import math
name = 'Quang'
print(name)
def tong(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
 
n = int(input("Nhập số nguyên n = "));
print("Tổng các chữ số của", n , "là", tong(n));