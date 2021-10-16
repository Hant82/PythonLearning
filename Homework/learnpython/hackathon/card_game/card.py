class Card:
   # '''Class đại diện cho mỗi lá bài

    # '''Mỗi lá bài bao gồm rank ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    #r= [{'A':1}, {'2':2},{'3':3}, {'4':4},{'5':5}, {'6':6},{'7':7},{'8':8},{'9':9}]
    #s= ["♠","♣", "♦", "♥"]
    #r = ["A","2", "3","4", "5", "6", "7","8", "9"]
    r= [2, 3,1]
    #v= ["♠","♣", "♦", "♥"]
    s= ["♠","♦"]

    def __init__(self,r,s):
        self.s=s
        self.r=r
        pass

    def __str__(self):
       #'''Hiển thị lá bài'''
       return  (str(self.r)+self.s)
        #pass
    #    v = self.r +\
    #         " of " + \
    #         self.suits[self.suit]
    #     return v

    def __gt__(self, other):
        if Card.r.index(self.r)== Card.r.index(other.r):
            return Card.s.index(self.s)> Card.s.index(other.s)
        else:
            return Card.r.index(self.r)> Card.r.index(other.r)
        

