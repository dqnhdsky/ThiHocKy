import math
name = input("Họ tên:")
print ("",name)
def ThuanNghich(n):
    str1 = str(n);     
    str2 = str1[::-1]; 
    if (str1 == str2):
        return True;
    else:
        return False; 
n = int(input("Nhập n = "));
print("Tổng các số của", n , "là", ThuanNghich(n));
