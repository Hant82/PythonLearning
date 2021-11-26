# Easy [1] Day different:
#Viết hàm day_diff() nhận vào ngày phải release sản phẩm và ngày đội dev viết xong code. Tính số ngày mà team test có để test sản phẩm (= release_date - code_complete_day). Lưu ý, ngày release sản phẩm sẽ ở định dạng 19/12/2021 còn ngày code_complete có định dạng 2021-17-05
import time
import datetime
from datetime import datetime as date
def day_diff(release,donecode):
    date_release = date.strptime(release, "%d/%m/%Y")
    date_donecode = date.strptime(donecode, "%Y-%d-%m")
    date_test = date_release-date_donecode
    return date_test.days

print(day_diff("21/11/2021","2021-19-11"))

# Easy [2] Alphabet and Number:
#Viết hàm alpha_num() tìm tất cả những từ trong một câu có chứa cả chữ cái và số. Trả ra danh sách các từ như vậy trong một câu.
import re
def alpha_num(str):
    find = re.findall("\w*\d\w*|\d\w*",str)
    return find

str1 = "Emma25aaa is Data scientist50 and AI Expert 99abc999 9nex90"
print(alpha_num(str1))
