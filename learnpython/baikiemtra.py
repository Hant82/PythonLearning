#Bài 1:
from datetime import date
from datetime import time
from datetime import datetime
import datetime
d_re=input ("Hãy nhập ngày release (dd/mm/yyyy):")
d_co=input ("Hãy nhập ngày complete (yyyy-dd-mm):")
def day_diff(re,co):
  d1=datetime.datetime.strptime(d_re, "%d/%m/%Y")
  print ("Ngày release:", d1)
  d2=datetime.datetime.strptime(d_co, "%Y-%d-%m")
  print ("Ngày complete:", d2)
  print ("Số ngày team test có thể test sản phẩm", d1-d2 )
day_diff(d_re,d_co)

#Bài 3:
i_chuoinguyen=input ("Hãy nhập vào chuỗi số")
def alpha_num(s):
  i_daochuoi= list(i_chuoinguyen)
  i_daochuoi.reverse()
  i_moi = ''.join(i_daochuoi)
  print ("Chuỗi mới sau khi đảo", i_moi)
  if i_moi==i_chuoinguyen:
    print ("Kết quả sau khi đảo chuỗi là True")
  else:
    print ("Kết quả sau khi đảo chuỗi là False")
alpha_num(i_chuoinguyen)
#Bài 2
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
alpha_num(s_string)