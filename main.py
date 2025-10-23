# Nạp thư viện tự định nghĩa
from myLib import myMath
from myLib import myStringLib

# Main module
if __name__ == '__main__':
    print('Hello world')
    s=myMath.add(3,8)
    print(s)
    myStringLib.sayHi("trongdepzai")