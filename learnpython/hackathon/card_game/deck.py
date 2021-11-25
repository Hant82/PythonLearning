from card import Card
import random
class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    r= ["A",2, 3, 4, 5, 6, 7, 8, 9]
    s= ["♠","♣","♦","♥"]
    #s= ["♠","♦"]
    # def __init__(self):
    
    def build(self):
       #'''Tạo bộ bài'''
        self.deck=[]
        for i in Deck.r:
            for j in Deck.s: #chạy hết vòng lắp for hiện tại rồi mới chạy vòng for trên
                self.deck.append(Card(i,j))
        return self.deck 
    def shuffle_card(self):  #tráo bài
        random.shuffle(self.deck)

    # def deal_card(self,index_card):
    def deal_card(self):  
    #Khi gọi Class build của bộ bài đã tạo được 1 bộ bài với giá trị biến
    #self.deck, hàm này chỉ sử dụng lại biến đó  
        '''Rút một lá bài từ bộ bài'''
     
        return self.deck.pop(0)
    
        
# d=Deck()
# d.build()

# d.shuffle_card()
# for i in d.build():
#     d.shuffle_card()
#     print (i)
# print ("Rút lá bài từ bộ bài:")
# print (d.deal_card())