num1 = 9; num2 = 2

print(f'{num1} / {num2} = {num1 / num2}') #나누기
print(f'{num1} // {num2} = {num1 // num2}')  #몫을 구해준다
print(f'{num1} % {num2} = {num1 % num2}') #% 나머지 값을 구해준다
print(f'{num1} ** {num2} = {num1 ** num2}') # ** = 9에 2승

'''
관계연산자  
- >, < <= ,,,,,
- 참(True) 또는 거짓(False)표현
'''

su1 = 3.1; su2 = 3
print("su1 >= su2 : ", su1 >= su2)
print("su1 < su2 : ", su1 < su2)
print("su1 == su2 : ", su1 == su2) #== 서로 같냐 x
print("su1 != su2 : ", su1 != su2) #!= 같지 않다 = true


#복합대입 연산자
'''
+=, -=, *= ,,,
ex)
a=10; => a = a + 100 => a += 100
         a = a * 100 => a *= 100
'''

su1 = su2 = 5
su1 += 1; print("su1 +=1 => ",su1) #su1 = 5 + 1 =6

su1 -= 1; print("su1 -=1 => ",su1) #su1 = 6 -1 = 5

su1 *= su2; print("su1 *= su2 => ",su1) #su1 = 5 * su2(5) = 25

su1 // su2; print("su1 // su2 => ",su1) #su1 = 25 // su2(5) = 5
 
su1 %= su2; print("su1 %= su2 => ",su1) # su1(5) % su2(5) = 0 #나눴을떄 나머지값0

su1 = 5; su2 = 3;  
su1 **= su2                    #su1 = su1 ** su2 5에 3승 ; 125
su1 -= 2                      #125-2 = 123
print ("su1 / 4 : ", su1 / 4) # 123 /4 = 30.75
print ("su1 // 4 : ", su1 // 4) # 몫을 구해라 = 30 그리고 몫은 소수점 해당안됨. 
print ("su1 %  : ", su1 % 4) # #나머지값 3


#논리연산자
'''
-참 또는 거짓 표현
-and, or, not
- and  : 값 and 값 => 하나라도 거짓이면 거짓 그리고 모두가 참일떄 참
- or : 값 or 값 => 하나라도 참이라면 결과는 참
- not  : not 값 => 결과값을 반전 시켜준다
'''

print(False or False)
print((10>20) or ( 10%2 == 0) )  #10이 20보다 크냐/ 10/2 나머지값이 0이랑 같냐 

print (False and True) #하나라도 거짓있음 거짓
print (True and True) #그렇기에 참참이기에 참이 된다.

a = 100
print( a>10 and a%2==0 ) # 10보다 큰 짝수

print ( not True)  #아닌값이기에 반대로 False 값이 나온다
print ( not False) #아닌값이기에 반대로 True 값이 나온다

'''
제어문
-if , 반복문, break, continue
ex)
if 조건식:
    종속문장
'''
print('1. 쉬운 게임')
print('2. 어려운 게임')
print('3. 게임 종료')

num = int( input(">>>> : "))
num = 1
if num == 1:
    print("쉬운 게임이 실행 됩니다")
if num == 2:
    print("어려운 게임이 실행 됩니다")
if num == 3:
    print("게임을 종료 합니다")
print ('다음문장')
num1 = 10; num2 = 5
if num1 > num2:
    print("참인경우 실행")   #해당 조건이 참이면 실행/ 아닐시 실행 안되고
print("다음 문장 실행") #아닐시 다음내용 진행
    
        
