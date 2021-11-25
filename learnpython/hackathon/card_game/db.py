'''Kết nối CSDL'''
from pymysql import connect, cursors, Error
from game import Game 
from datetime import datetime
from datetime import date
config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "game_card",
    # "cursorclass": cursors.DictCursor
}
cnx = connect(**config)

def logs(game_1,dem):
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs

    Bảng games gồm tên người chiến thắng

    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game

    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''
   
  
    for i in range(0,len(game_1.number)):
        sql="INSERT INTO logs (gamer,deck,point,biggest_card,route) VALUES (%s, %s,%s,%s,%s)"
        # print(game_1.number[i].name)
        # print(game_1.number[i].ghep_card())
        # print(game_1.number[i].point)
        # print(game_1.number[i].biggest_card.__str__())
        value=(game_1.number[i].name,game_1.number[i].ghep_card(),game_1.number[i].point,game_1.number[i].biggest_card.__str__(),dem)
        cur = cnx.cursor()    
        try:
            cur.execute(sql,value)
            cnx.commit()
        except:
            cnx.rollback()
   
    
    
def games(game_1,dem):
    sql1="INSERT INTO games (winner,date_time,route) VALUES (%s,%s,%s)"
    value1=(game_1.flip_card().name,datetime.now(),dem)
    cur1 = cnx.cursor()
    try:
            cur1.execute(sql1,value1)
            cnx.commit()
    except:
            cnx.rollback()

def get_thutulanchoi():
    sql="SELECT MAX(route) as luot FROM `logs` "
    cur = cnx.cursor()
    cur.execute(sql)
    for i in cur:
        # print(i[0])
        result= i[0]
    return result


def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    "Lấy thông tin số người chơi, người chiến thắng, số điểm từng người chơi, bộ bài từng người chơi, lá bài lớn nhất của từng người chơi"
    "Đếm số người chơi trong lượt "
    # sql="SELECT * FROM games AS g ORDER BY g.`date_time` DESC"
    # cur = cnx.cursor()
    # cur.execute(sql)
    sql = '''
    SELECT * FROM games AS g ORDER BY g.`date_time` DESC
    '''
    cur = cnx.cursor()
    cur.execute(sql)
    game = cur.fetchone()

    # if not game:
    #     raise Exception('Không có lịch sử game\nChơi vài game vui vẻ đi 😉\n')

    sql = f'''
    SELECT *
    FROM logs
    WHERE route = {game[2]}
    '''
    cur.execute(sql)
    players = cur.fetchall()
    for i in players:
        print(f"Tên người chơi:{i[1]} Các lá bài:{i[2]} Điểm:{i[3]} Lá bài lón nhất: {i[4]}")

    # sql = f'''
    # SELECT MAX(route) as luot FROM `games`
    # '''
    sql="SELECT winner,date_time FROM `games` WHERE `route`=(SELECT max(route) FROM `games`)"
    cur.execute(sql)
    winner = cur.fetchall()
    for j in winner:
        print(f"Tên người chiến thắng lượt chơi này là:{j[0]} Thời gian: {j[1]}" )
    # return game, players

def history():
    '''
    Lấy thông tin về lịch sử chơi

    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
    '''
    # số ván bài chơi trong ngày
    # thông tin bàn thắng của từng người
    sql1 = '''
    SELECT COUNT(winner) AS game_won FROM games AS g
    WHERE DATE(g.date_time) = CURDATE()
    
    '''
    cur = cnx.cursor()
    cur.execute(sql1)
    for i in cur:
        print (f"Số ván bài chơi trong ngày hôm nay ({date.today()}) là: {i[0]} ván")

    sql = '''
    SELECT
        winner,
        COUNT(winner) AS game_won
    FROM games AS g
    WHERE DATE(g.date_time) = CURDATE()
    GROUP BY winner
    ORDER BY game_won DESC
    '''
    cur = cnx.cursor()
    cur.execute(sql)
    ls = cur.fetchall()
    if len(ls)==0:
        print ("Chưa có người chơi trong ngày hôm nay")
    else:
        print ("Danh sách người chiến thắng là:")
    for j in ls:
        print(f"{j[0]} đã thắng {j[1]} ván" )

    # sql1 = '''
    # SELECT COUNT(winner) AS game_won FROM games AS g
    # WHERE DATE(g.date_time) = CURDATE()
    
    # '''
    # cur = cnx.cursor()
    # cur.execute(sql1)
    # for i in cur:
    #     print ("Số ván bài chơi trong ngày là", i[0])
    # records = cur.fetchall()

    # if not records:
    #     raise Exception('Không có lịch sử game\nChơi vài game vui vẻ đi 😉\n')

    # total_game = sum([r['game_won'] for r in records])
    # return total_game, recordszx
# g=Game()
# g.setup()
# g.deal_card()
# log(g)
# g.flip_card()

