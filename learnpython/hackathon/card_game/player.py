from card import Card
#from game import Game
class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self, name):  # dễ
        self.name=name
        # self.card= Card()
        self.card=[]
        

    @property
    def point(self):  # trung bình
        #'''Tính điểm cho bộ bài'''
        sum=0
        # card=Card()
        for card in self.card:
            sum += card.r
        # print (sum%10)
        return sum%10
        

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        max = self.card[0]
       
        for card in self.card:
             if card > max:  # sử dụng hàm Magic Method:__gt__
                max = card
        # print (max)
        return max
    def add_card(self,card):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        self.card.append(card)

       
    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self.card=[]
    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
            
        for i in self.card:
            print(i)

    def __str__(self):
        return self.name
    def ghep_card(self):
         chuoi=""
         for i in self.card:
           chuoi=i.__str__()+chuoi
         return chuoi