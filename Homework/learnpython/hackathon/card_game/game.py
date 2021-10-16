from player import Player
# from deck import Deck
import deck
class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        self.number = []
        self.deck = deck.Deck()
        self.deck.build()

    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        print("Welcome..., có mấy người chơi")
        number_player = int(input())
        
        for i in range(number_player):
           n_player=input("Nhập tên người chơi thứ "+ str(i+1))
           self.number.append(Player(n_player))


    def guide(self):
        #'''Hiển thị menu chức năng/hướng dẫn chơi'''
        print ("1. Danh sách người chơi (" + str(len(self.number)) + ")")
        print ("2. Thêm người chơi (có thể thêm)")
        print ("3. Loại người chơi (số người chơi tối thiểu rồi)")
        print ("4. Chia bài (có thể chia)")
        print ("5. Lật bài")
        print ("6. Xem lại game vừa chơi")
        print ("7. Xem lịch sử chơi hôm nay")
        print ("8. Thêm người chơi (có thể thêm")
        

    def list_players(self):
        #'''Hiển thị danh sách người chơi'''
      print ("Danh sách người chơi:")
      for player in self.number:
          print(player)
        

    def add_player(self):
        #'''Thêm một người chơi mới'''
         n_player= ("Nhập thêm người chơi thứ", len(self.number))
         self.number.append(Player(n_player))

    def remove_player(self):
        #'''
        #Loại một người chơi
       # Mỗi người chơi có một ID (có thể lấy theo index trong list)
       # '''
       print("Nhập thứ tự người muốn xóa" )
       delete_number=int(input())
       del self.number[delete_number-1]

        

    def deal_card(self):
        '''Chia bài cho người chơi'''
        n=len(self.number)
        for i in self.number:
            i.add_card(self.deck.deal_card(self.number.index[i]))
            i.add_card(self.deck.deal_card(self.number.index[i]+n))
            i.add_card(self.deck.deal_card(self.number.index[i]+2*n))
        
    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        for Player in self.number:
            Player.point()
    