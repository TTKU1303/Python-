n = int(input("Nhap mot so nguyen duong bat ki:"))
a = 0
if (n < 0): 
   print ("Sai so. Xin vui long nhap so khac:")
elif (n <= 1):
   print ("So ", n, "khong phai la so nguyen to")
else: 
   for i in range (2,n):
       if (n % i == 0):
          a = 1 
if (a == 0):
   print ("So ", n, "la so nguyen to")
else: 
   print ("So ", n, "khong phai la so nguyen to")

   
       