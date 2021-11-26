# Medium [1] Anagram Number:
#Viết hàm anagram_number() có đầu vào là một số nguyên và trả ra True nếu sau khi đảo ngược thứ tự các chữ số của số đó vẫn cho ta số ban đầu. Trả ra False nếu không giống.
def anagram_number(num):
    strnumber=str(num)
    str_reversenum = strnumber[::-1]
    reversenum = int(str_reversenum)
    if(num==reversenum):
        return True
    else:
        return False

# Đổi số la mã
def from_roman(num):
    roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    for i,c in enumerate(num):
        if (i+1) == len(num) or roman_numerals[c] > roman_numerals[num[i+1]]:
            result += roman_numerals[c]
        else:
            result -= roman_numerals[c]
    return result
