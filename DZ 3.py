#1
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(3, 6))
#использовано, что НОД(x,0)=x и НОД(x,y)=НОД(y,остаток от деления x на y)

#3
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

s = str(input("Введите строку: "))
if (is_palindrome(s) == True):
    print("Это палиндром!")
else:
    print("Это не палиндром!")

#4
def T(size, symb):
    m = (size + 1) // 2 #середина треугольника
    for i in range(1, m + 1):
        print(symb * i)
    for i in range(m - 1, 0, -1):
        print(symb * i)
T(7, 'c')