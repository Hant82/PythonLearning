from player import Player
from deck import Deck
#import deck
class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        self.number = [] # Khởi tạo danh sách người chơi, khởi tạo một mảng 
        self.deck = Deck() # cài đặt 1 bộ bài, do Class Deck ko có giá trị khởi tạo nên sau khi
        #cài đặt phải gọi hàm build của Class Deck
        self.deck.build()
        self.playing=False

    def setup(self): # điền thông tin vào mảng được khởi tạo
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        print("Welcome..., có mấy người chơi")
        # number_player = int(input())
        while True: 
            try:
                number_player = int(input())
                if number_player >=2 and number_player <=6:
                    break
                else:
                    print("Số lượng người chơi tối thiểu là 2 tối đa là 6")
            except:
                
                print ("Bạn phải nhập số")
        
        for i in range(1,number_player+1):
           n_player=input("Nhập tên người chơi thứ "+ str(i))
           self.number.append(Player(n_player))
        return self.number

    def guide(self):
        #'''Hiển thị menu chức năng/hướng dẫn chơi'''
        print ("1. Danh sách người chơi (" + str(len(self.number)) + ")")
        print ("2. Thêm người chơi (có thể thêm)")
        print ("3. Loại người chơi (số người chơi tối thiểu rồi)")
        print ("4. Chia bài (có thể chia)")
        print ("5. Lật bài")
        print ("6. Xem lại game vừa chơi")
        print ("7. Xem lịch sử chơi hôm nay")
        print ("8. Thoát game")
        

    def list_players(self):
        #'''Hiển thị danh sách người chơi'''
      print ("Danh sách người chơi:")
      for player in self.number:
          print(player)
        

    def add_player(self):
        #'''Thêm một người chơi mới'''
        #  
        print("Số lượng người chơi cần thêm mới")
        number_player = int(input())
        if (number_player+len(self.number))>6:
            print ("Không thêm được người chơi do đã quá số lượng người được chơi")
        else:
            for i in range(1,number_player+1):
                print ("Nhập tên người chơi thứ", len(self.number)+1)
                n_player= input()
                self.number.append(Player(n_player))
            print ("Thêm người chơi thành công")
        #  else:
        #     print ("Không thêm được người chơi do đã quá số lượng người được chơi")

    def remove_player(self):
        #'''
        #Loại một người chơi
       # Mỗi người chơi có một ID (có thể lấy theo ind6ex trong list)
       # '''
        print("Nhập thứ tự người muốn xóa" )
        delete_number=int(input())
    #    del self.number[delete_number-1]
        if len(self.number)>2:
            if delete_number <= len(self.number):
                self.number.pop(delete_number)
                print ("Xóa thành công")
            else:
                print('Khong tim thay nguoi choi!')
        else:
            print ("Không thể xóa do số lượng người chơi đã là tối thiểu")
            
        

    def deal_card(self):
        '''Chia bài cho người chơi'''
        #n=len(self.number)
        self.deck.shuffle_card()
        for j in range (0,3):
            for i in self.number:
            
                i.add_card(self.deck.deal_card()) # do khai báo bên trên self.deck.build()
        self.playing=True
    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        
        p=None
        for Player in self.number:
                print (Player)
                Player.flip_card() #Lật bài từng người chơi
                if p==None:
                    p=Player
                else:
                    if p.point == Player.point:
                        if Player.biggest_card > p.biggest_card:
                            p = Player
                    elif Player.point > p.point:
                            p = Player
                print ("Số điểm của", Player.name, "là:", Player.point)
                print ("Lá bài có giá trị lớn nhất", Player.biggest_card)
        print(f'Nguoi chien thang:{p.name}')
        self.playing=False
        return p
       
       
# g=Game()
# g.setup()
# # d=Deck()
# # p1=Player()
# # p2=Player()
# # p3=Player()
# g.list_players()
# i=int(input())
# if i==2:
#     g.add_player()
# g.list_players()
# d.shuffle_card()
# g.deal_card()
# g.flip_card()