'''khởi tạo nhận 2 giá trị nr (tử số) và dr (mẫu số)
Nếu dr âm, chuyển dấu cho nr (VD: 1/-2 => -1/2)
Triển khai phương thức phù hợp để in ra phân số (VD: print(fr) => -1/2)
Viết hàm hcf tìm ước chung lớn nhất của nr và dr
Thêm phương thức reduce rút gọn phân số (gọi trong __init__)
Nếu nr == 0, chỉ in ra 0
Nếu dr == 0, raise ZeroDevisonError
Nếu dr == 1, chỉ in ra nr
Triển khai các phương thức phù hợp cho phép +-*/ với 2 Fraction hoặc 1 Fraction với 1 số (int hoặc float), kết quả trả về 1 Fraction mới
'''
class phanso:
    def __init__(self,nr,dr):
        self.nr=nr
        self.dr=dr
        self.set_lai_nr_dr()
        self.reduce()


    def set_lai_nr_dr(self):
        if self.dr==0:
            print("lỗi chia cho 0")
        elif(self.dr<0):
            self.nr=-self.nr
            self.dr=-self.dr
        else:
            self.nr = self.nr
            self.dr = self.dr

    def dislay(self):
        print(f'phân số vừa nhâp: {self.nr}/{self.dr}')

    def uscln(self,a, b):
        if (b == 0):
            return a
        return self.uscln(b, a % b)
    def reduce(self):
       if self.nr==0:
            print(0)
       elif self.dr==0:
           print("raise ZeroDevisonError")
       elif self.dr==1:
           print(self.nr)
       else:
           print(f'giá trị rút gọn của phân số:{int(self.nr/self.uscln(self.dr,self.nr))}/{int(self.dr/self.uscln(self.dr,self.nr))}')


ps= phanso(15,20)








