#Bài 2
#Viết chương trình trả ra từ điển với key là các số trong #list, value là số lần xuất hiện của số trong list
#my_list=[10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
while True:
 z_phan_tu = input (" Hãy nhập độ dài chuỗi:")
 if z_phan_tu!="":
   try:
     z_phan_tu=int(z_phan_tu)
     if z_phan_tu>0:
       acb=()
       break;
     else:
       print ("Phải khác không và âm")
     
   except ValueError:
        print("Một trong các giá trị bạn nhập vào không phải dạng số, vui lòng nhập lại!")
 else:
      print("Trường độ dài chuỗi cần có giá trị!")
x_string = []
i_string=1
while i_string < z_phan_tu+1:
  print ("Nhập số thứ",i_string,":" )
  c_nhap = input ()
  if c_nhap !="":
    try:
     c_nhap=int(c_nhap)
     x_string.append (c_nhap)
     y_string=x_string
     i_string+=1
    except ValueError:
        print("Một trong các giá trị bạn nhập vào không phải dạng số, vui lòng nhập lại!")
  else:
      print("Cần nhập một giá trị!")

print ("Chuỗi là", y_string)
print ("Số lần xuất hiện của các số trong danh sách như sau:")
i_dem ={}
for i_kytu in y_string:
  if i_kytu in i_dem:
    i_dem [i_kytu] += 1
  else:
    i_dem [i_kytu] =1
print (i_dem)
#Bài 3:
#Viết chương trình in ra thời gian đếm ngược đến XMas 2021 sau mỗi khoảng thời gian nhất định.
#from datetime import date
#from datetime import time
#from datetime import datetime
#import time

#t_ngay=datetime.fromisoformat("2021-12-25")
#t_today=datetime.today()
#while t_today < t_ngay:
#   t_dem_nguoc= t_ngay- t_today
#    print("Còn", t_dem_nguoc, "sẽ đến Noel")
#    time.sleep(5)
#else:
#  print("Noel đến rồi")
# Bài 1
#Hãy viết chương trình in ra các hình sau (dùng ký tự '*' #và ký tự space) với n là số dòng. Vd: n i= 4:
m=4
print ("Hình thứ 1:")
for a_sao in range (1,m+1):
  #chạy 1 vòng của i_sao, in ra 1 khoảng cách ở đằng trước
  for b_sao in range (1, (m+1)-a_sao):
   print (" ",end=" ")
  #chạy x vòng của i_sao
  for c_sao in range(1, a_sao+1):
   print("*", end=" ")
  print()
print()
print ("Hình thứ 2:")
n=4
for i_sao in range (1,n+1):
  #chạy 1 vòng của i_sao, in ra 1 khoảng cách ở đằng trước
  for j_sao in range (1, (n+1)-i_sao):
   print (" ",end=" ")
  #chạy x vòng của i_sao
  for k_sao in range(1, i_sao+1):
   if k_sao <n:
    print("*", end=" ")
   else:
    print("* * * * *", end=" ")
  print()
for b_sao in range (n, 1,-1):
  for c_sao in range (n+1,1,-1):
    print (" ",end= " ")
  for d_sao in range(b_sao,1,-1):
    print("*", end=" ")
  print()
print()

#print ("Hình thứ 3:")
#k=4
#for h_sao in range (1,k+1):
 # for p_sao in range(1, h_sao+1):
 #  if p_sao <k:
  #  print("*", end=" ")
   #else:
   # print("* * * * *")
  #for q_sao in range (1, (k+1)-h_sao):
    
     #print ("", end="")
    
  #print()
#for z_sao in range (k, 1,-1):
#  for v_sao in range(z_sao,1,-1):
 #   print("*", end=" ")
 # for w_sao in range (k,0,-1):
 #  print (" ", end=" ")
  
  
 # print()
#print()

#for b_sao in range (n, 1,-1):
#  for c_sao in range (n+1,1,-1):
#    print (" ",end= " ")
#  for d_sao in range(b_sao,1,-1):
#    print("*", end=" ")
#  print()
#Bài 5:
#Cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.
#Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum
#vd ở đây nếu sum = 18 thì kết quả là [(7,11), (6,12)]. #Nếu không có cặp số nào thỏa mãn thì in ra list rỗng []
while True:
 i_phan_tu = (input (" Hãy nhập độ dài chuỗi:"))
 d_sum = (input ("Nhập vào tổng"))
 if (i_phan_tu!="") and (d_sum!=""):
   try:
     i_phan_tu=int(i_phan_tu)
     d_sum=int(d_sum)
     if i_phan_tu>0:
       acb=()
       break;
     else:
       print ("Độ dài chuỗi phải lớn hơn 0")
     
   except ValueError:
        print("Một trong các giá trị bạn nhập vào không phải dạng số, vui lòng nhập lại!")
 else:
      print("Trường độ dài chuỗi và tổng cần có giá trị!")

a_string = []
b_string=1
while b_string < i_phan_tu+1:
  print ("Nhập số thứ",b_string,":" )
  c_nhap = input ()
  if c_nhap !="":
    try:
     c_nhap=int(c_nhap)
     a_string.append (c_nhap)
     b_string+=1
    except ValueError:
        print("Một trong các giá trị bạn nhập vào không phải dạng số, vui lòng nhập lại!")
  else:
      print("Cần nhập một giá trị!")
print ("Chuỗi vừa nhập là", a_string )
b_tuple=()
c_tuple= ()
c_string=[]
d_string=[]
for d_i in range (0,(i_phan_tu)):
  for d_j in range ((i_phan_tu)-1, d_i,-1):
   if a_string[d_i]+a_string[d_j]==d_sum:
    b_tubple= (a_string[d_i],a_string[d_j])
    c_string.append (b_tubple)
    d_string=c_string
  else:
      c_tuple= ()
if d_string != []:
 print ("Các cặp số trong chuỗi có tổng bằng", d_sum,"là:", d_string)
else:
  print ("Không có cặp số nào phù hợp", d_string)
#Bài 4
#Unique value Dictionary:
#Cho một list gồm 1 hoặc nhiều từ điển (Dictionary). Viết #chương trình để trả ra tập hợp tất cả các giá trị (values) duy nhất trong tất cả danh sách các từ điển trên.
#my_dict=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
my_dict=[dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]
d_dict={}
c_dict={}
d_string=[]
for i_dict in range (0, len(my_dict)):
  b= my_dict[i_dict].values()
  c= list (my_dict[i_dict].values())
  for myvalue in c:
    d=myvalue
    d_string.append(d)
    g= d_string
  
print ("Các giá trị trong Dict là", g)
#d_dem =[]
#g_dem=[]
#set_1={}
#for i_kytu in g:
 #if i_kytu in d_dem:
  # c_dem=[]
 #else:
  #  d_dem.append (i_kytu)
  #  g_dem=d_dem
set_1= set(g)

print ("Các giá trị duy nhất trong Dict là:",set_1)