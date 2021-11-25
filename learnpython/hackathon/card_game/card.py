class Card:
   # '''Class đại diện cho mỗi lá bài

    # '''Mỗi lá bài bao gồm rank ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    #r= [{'A':1}, {'2':2},{'3':3}, {'4':4},{'5':5}, {'6':6},{'7':7},{'8':8},{'9':9}]
    #s= ["♠","♣", "♦", "♥"]
    #r = ["A","2", "3","4", "5", "6", "7","8", "9"]
    # r= [2, 3,1]
    # #v= ["♠","♣", "♦", "♥"]
    # s= ["♠","♦"]

    def __init__(self,r,s):
        
        self.r=r
        self.s=s
        if r=="A":
            self.r=1
        else:
            pass
        
        if self.s=="♦":
            self.s=4
        if  self.s=="♥":
            self.s=3
        if  self.s=="♣":
            self.s=2
        if  self.s=="♠":
            self.s=1    

    def __str__(self):
       #'''Hiển thị lá bài'''
        r=self.r
        if r==1:
            r="A"
        else:
           r=self.r 
        s = self.s
        if (s == 1):
            s = '♠'
        if (s == 2):
            s = '♣'
        if (s == 3):
            s = '♥'
        if (s == 4):
            s = '♦'
        return f'{r}{s}'
    #    return  (str(self.r)+str(self.s))
    
    def __gt__(self, other):
        #so sánh giá trị lá bài. Phải có giá trị là bài được khởi tạo trước đó rồi mới đi so
        #sánh được
       
        #Nếu rank bằng nhau so sánh đến chất. Nếu chất của C1> C2 trả về kết quả phép so sánh lớn hơn là True, ko thì kết quả là False
        
        if self.s== other.s:
            if self.r> other.r:
                return True #Phép toán 3 ngôi
            else:
                return False
        if self.s< other.s:
            return False
        else:
            return True
        

# c1 = Card(2, "♦")
# c2 = Card ("A","♦")
# print (c1)
# print (c2)
# if c1>c2:
#  print ("Đúng")
# else:
#  print ("Sai")
