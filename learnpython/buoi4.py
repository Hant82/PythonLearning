# Bài 1  Viết hàm có đầu vào là 1 chuỗi, trả ra số chữ cái, số ký tự viết hoa, số ký tự viết thường và số chữ số trong chuỗi đó. Giả sử đầu vào sau được cấp cho hàm:
#s = "Hello World! 123"
#Hàm count_char_type(s) sẽ trả ra 1 dict {"LETTERS":10, "CASE": {"UPPER CASE":2, "LOWER CASE":8}, "DIGITS":3}. Lưu ý: value của key "CASE" là một dict có 2 keys là "UPPER CASE", "LOWER CASE".
#a) Viết hàm trên dùng bất kỳ hàm built in nào của python
var_s=input("Bạn hãy nhập chuỗi:")
def count_char_type(s):
  i_chu=0
  i_so=0
  i_hoa=0
  i_thuong=0
  for i in var_s:
    if i.isalpha()==True:
       i_chu += 1
    if i.islower()==True:
      i_thuong+=1
    if i.isupper()==True:
      i_hoa+=1
    if i.isdigit()==True:
       i_so += 1
    else:
      continue
  print("số ký tự chữ",i_chu )
  print("số ký tự số",i_so )
  print("số ký tự hoa",i_hoa )
  print("số ký tự thường",i_thuong)
  d_dict={"LETTERS":i_chu,"CASE":{"UPPER CASE":i_hoa, "LOWER CASE":i_thuong},"DIGITS":i_so}
  print ("Kết quả phân tích chuỗi", d_dict)
  return d_dict
count_char_type(var_s)
#b) Viết hàm chỉ dùng 1 hàm built in duy nhất.
var_s=input("Bạn hãy nhập chuỗi:")
def count_char_type(s):
  i_chu=0
  i_so=0
  i_hoa=0
  i_thuong=0
  for i in var_s:
    if ord(i) in range (65,90):
      i_chu += 1
      if ord(i) in range (65,90):
        i_hoa+=1
    if ord(i) in range (97,122):
      i_chu += 1
      if ord(i) in range (97,122):
        i_thuong+=1
    if ord(i) in range (48,57):
      i_so += 1
    else:
      pass
  d_dict={"LETTERS":i_chu,"CASE":{"UPPER CASE":i_hoa, "LOWER CASE":i_thuong},"DIGITS":i_so}
  print ("Kết quả phân tích chuỗi", d_dict)
  return d_dict
count_char_type(var_s)

#Bài 2 Cho một list A các điểm thi (từ 0-10) của các học viên trong lớp. Viết 3 hàm tính:

#giá trị trung bình (mean) của dãy.
#trung vị (median) của dãy A. trung vị là một số đứng ở vị trí giữa trong dãy số đã được sắp xếp theo thứ tự tăng dần, median chia dãy số cho trước thành 2 nửa bằng nhau. Nếu độ dài của dãy số là số lẻ, thì số ở giữa là median, nếu chiều dài của dãy số là số chẵn thì median được xác định bằng cách lấy trung bình của hai số ở giữa.
#mode của dãy A. Mode là phần tử có số lần xuất hiện nhiều nhất trong dãy. Mode sẽ giúp ta trả lời câu hỏi: "Trong lớp này, học viên đạt Điểm số nào nhiều nhất?".
#Lưu ý: kết quả trả ra sẽ là 1 list vì mode có thể nhiều hơn 1 giá trị.

#Vd:

#A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10] ==> (mean(A), median(A), mode(A)) == (6.55, 7.0, [9])
#B=[4,4,5,4,5,5] thì (mean(B), median(B), mode(B)) == (4.5, 4.5, [4,5])
#import numpy
import statistics
d_list=[]
d_diem=[]
i_soluong=int(input("Hãy nhập số lượng điểm thi:"))
for i in range (0,i_soluong):
   i_diemthi=int(input("Hãy nhập điểm thi:"))
   d_list.append(i_diemthi)
print ("Danh sách", d_list)
def giatritrungbinh(s):
  statistics.mean(d_list)
  print ("Giá trị trung bình",statistics.mean(d_list) )
  return statistics.mean(d_list)
giatritrungbinh(d_list)
def giatritrungvi(s):
  statistics.median(d_list)
  print ("Giá trị trung vị",statistics.median(d_list) )
  return statistics.median(d_list)
giatritrungvi(d_list)
def giatrimode(s):
  for i in d_list:
    statistics.mode(d_list)
  print ("Giá trị mode",statistics.mode(d_list) )
  return statistics.mode(d_list)
giatrimode(d_list)

 