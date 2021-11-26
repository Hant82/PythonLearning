# Medium [1] Anagram Number:
i_chuoinguyen=input ("Hãy nhập vào chuỗi số")
def anagram_number(number):
  i_daochuoi= list(i_chuoinguyen)
  i_daochuoi.reverse()
  i_moi = ''.join(i_daochuoi)
  print ("Chuỗi mới sau khi đảo", i_moi)
  if i_moi==i_chuoinguyen:
    print ("Kết quả sau khi đảo chuỗi là True")
  else:
    print ("Kết quả sau khi đảo chuỗi là False")
#Chạy hàm
anagram_number(i_chuoinguyen)

# Medium [2] Roman to Integer
def roman_to_int(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 0
    num = 0
    while i < len(s):
        #Bắt thằng IV, IX, XL.. trước
        if i+1<len(s) and s[i:i+2] in roman: #cắt chuỗi s (do user nhập vào từ vị trí thứ i đến vị trí thứ i+2. Ví dụ chuỗi nhập vào là ABCD --> i đi từ A--> Chuỗi cắt là AB, ko lấy C)
            num+=roman[s[i:i+2]] # lấy giá trị của chuỗi cắt được so sánh với key trong roman, có 1 key trùng với chuỗi cắt được
            i+=2
        else:
            num+=roman[s[i]]
            i+=1
    print (num)
    return(num)
#Chạy hàm
roman_to_int ("XIIIVIIIXL") 
#1. i+1<s và XI không thuộc roman
#2 Nhảy đến else num=X=10 tăng i lên 1
#3 Tiếp tục chạy vòng while: đọc được II không tồn tại trong roman --> đến bước else num=10+1=11, tăng i lên 1 vị trí
#4 Tiếp tục chạy vòng while: đọc được II không tồn tại trong roman --> đến bước else num=11+1=12, tăng i lên 1 ví trí
#5 Tiếp tục chạy vòng while: đọc được IV có tồn tại trong roman --> vào bước if num=12+4=16, tăng i lên 2 vị trí