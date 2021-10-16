from card import Card
import random
class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    r= [2, 3,1]
    #v= ["♠","♣", "♦", "♥"]
    s= ["♠","♦"]
    
    def build(self):
       #'''Tạo bộ bài'''
        self.deck=[]
        for i in Deck.r:
            for j in Deck.s:
                self.deck.append(Card(i,j))
      
    def shuffle_card(self):
        random.shuffle(self.deck)

    def deal_card(self,index_card):
        '''Rút một lá bài từ bộ bài'''
     
        return self.deck[index_card]
    
        
d=Deck()
d.build()
print (d.deal_card(1))