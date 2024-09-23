# 16defreturn.py = 15defreturn.py 비슷


def book():
   title = '몽블랑' #지역변수=local variable=휘발성
   return title

def pay():
   m = 7800        #지역변수=local variable=휘발성
   return m 

#리턴값X 없는호출해서 출력하면 None 
def blue():
   color = 'dark'


def main():
   print("main함수")
   print("책제목 " , book())
   print("책가격 ",  pay())
   print("블루색 ",  blue()) #None필드/pass필드  


#함수단독기술해서 호출 
main()    










print()
print()
