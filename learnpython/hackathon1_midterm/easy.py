# Easy [1] Day different:
from datetime import date
from datetime import time
from datetime import datetime
import datetime
d_re=input ("Hãy nhập ngày release (dd/mm/yyyy):")
d_co=input ("Hãy nhập ngày complete (yyyy-dd-mm):")
def day_diff(re,co):
  d1=datetime.datetime.strptime(d_re, "%d/%m/%Y")
  print ("Ngày release:", d1)
  while True: 
            try:
                d2=datetime.datetime.strptime(d_co, "%Y-%d-%m")
                print ("Ngày complete:", d2)
                break
            except:
                print ("Định dạng ngày tháng phải là (yyyy-dd-mm)")
                d_co=input ("Hãy nhập ngày complete (yyyy-dd-mm):")
  if d1<d2: 
      print ("Ngày complete không hợp lệ!")
  else:
      print ("Số ngày team test có thể test sản phẩm", d1-d2 )

#Chạy hàm
day_diff(d_re,d_co)


# Easy [2] Alphabet and Number:
s_string= input ("Hãy nhập vào một chuỗi:")
print ("Chuỗi nhập vào là:",s_string)
def alpha_num(s):
  s_chuso=[]
  s_phantach =s_string.split()
  for s_tu  in s_phantach:
    if s_tu.isalpha()!=True and s_tu.isdecimal()!=True:
      s_chuso.append(s_tu)
    else:
      continue
  print ("Các từ trong chuỗi vừa có chữ và có số là:", s_chuso)
  
#Chạy hàm  
alpha_num(s_string)