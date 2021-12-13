import math
import decimal
def chanle():
    try:
        a=float(input('nhap so tu ban phim: '))
        if a%2==0:
            print('so chan')
        else:
            print('so le')
    except:
        print('nhap dau vao chua dung')
if __name__=="__main__":
    chanle()