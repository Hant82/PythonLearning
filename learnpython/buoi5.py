#Điểm thi học kỳ của sinh viên được lưu ở định dạng 1 tuple có 3 phần tử (m1, m2, e) gồm:
#m1 = midterm1
#m2 = midterm2
#e = endterm
#Cho một list gồm danh sách điểm thi của sinh viên 1 lớp. Viết chương trình Python để sắp xếp danh sách trước theo thứ tự tăng dần theo phần tử cuối cùng trong mỗi tuple (sắp xếp theo điểm cuối kỳ - endterm tăng dần).
#vd sort_list_last([(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]) == [(10, 2, 1), (9, 1, 2), (3, 2, 3), (6, 4, 4), (1, 2, 5)
i_soluongsv=int (input("Hãy nhập số lượng sinh viên:"))
t_diemthi=[]
a_tuple=()
for i in range (1,i_soluongsv+1):
  print("Sinh viên thứ", i) 
  m1= int (input("Hãy nhập số điểm midterm1:"))
  m2= int (input("Hãy nhập số điểm midterm2:"))
  e= int (input("Hãy nhập số điểm endterm:"))
  a_tuple=(m1,m2,e)
  t_diemthi.append(a_tuple)
print ("Danh sách điểm thi:", t_diemthi)
print ("Thứ tự sắp xếp:",sorted(t_diemthi, key=lambda x: x[::-1]))

#Cho 1 chuỗi A (vd: "tHE fOX iS cOMING fOR tHE cHICKEN"). Viết hàm đảo ngược thứ tự các từ trong chuỗi và đổi tất cả các chữ cái từ hoa thành thường và ngược lại. (kết quả là "Chicken The For Coming Is Fox The")

s_chuoi=input ("Hãy nhập chuỗi:")
def thaydoichuoi(s):
  s_chuoimoi=[]
  sort_chuoi= sorted(s_chuoi.split())
  print ("Chuỗi thay đổi thứ tự so với lúc đầu",sorted (sort_chuoi, key=lambda x: x[::-1]))
  for i in range (0, len (sort_chuoi)):
    u_viethoa=sort_chuoi[i].capitalize()
    s_chuoimoi.append(u_viethoa)
  print ("Ký tự đầu mỗi từ viết hoa:",s_chuoimoi)
  s_noi=' '.join(sorted (s_chuoimoi, key=lambda x: x[::-1]))
  print ("Kết quả là:", s_noi ) 
thaydoichuoi(s_chuoi)