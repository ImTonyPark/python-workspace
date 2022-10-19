num1 = 5
num2 = 10
sum = num1 + num2
print ('n1 :',num1)
print ('n2 :',num2)
print ('sum :', sum)

num1 = 10
num2 = 20
print('num1(',num1,') + num2(' ,num2,') =',num1+num2)
print(f'num1({num1}) + num2({num2})={num1+num2}')

#소수점끼리 반올림 : round
flt = 123.567
print (flt)
print ('round(flt) : ', round(flt) )
print ('round(flt,1) : ', round(flt,1) )
print ('round(flt,2) : ', round(flt,2) )

#합 평균
py=80
c=75
jy=63
sum_ = py + c + jy
print ("합 : ",sum_)
print("평균:", round( sum_/3 ,2 ))

#역 평균
station = 11
minute = 37
average = minute / station
print ('역의 평균 시간 :', round(average, 2))


#건물 높이 
oneFloorHeight = 500.23
avgFloorHeight = 260
cntFloor = 13

buildingHeight = oneFloorHeight + cntFloor*avgFloorHeight
print('건물 높이 : ', round(buildingHeight/100,3)) 

flt = 123.123
print (flt + 20 )

# 문자끼리 연산 가능
st = '자'; st1 = '바'
print (st + st1)

num = 100
print (type(num))
num1 = 100.1123
print (type(num1))
print (type(1.123))
st = "ㅎㅇㅎ"
print (type (st))
print (type (str(num)))

#문자로 변환해서 연산  가능
print ('안녕하세요'+ str(num))

su1 = 100
num1 = '100'
flt1 = "1.111"

print (su1 + int(num1))
print (su1 + float(flt1))
print (int(float(flt1)))
print (str(su1) + num1)

num = input ('숫자 입력 :')
print('입력받는 수 :', num)

name = input ('이름 입력 :')
age = input ('나이 입력 :')
print('결과 출력 :', name, '님의 나이는',age,'입니다')
#저렇게도 되지만 이렇게 해도 된다.
print(f'{name}님의 나이는 {age}살 입니다')

print("두 수의 합을 구해 주십시요!!!")
n1 = input('수 입력 :')
n2 = input('수 입력 :')
n3 = n1 + n2
print('두 수의 합 : ', n3) #문자 형식으로 되버리기에 연산해도 문자+문자가됨

#test
print("두 수의 합을 구해 주십시요!!!")
n1 = input('수 입력 :')
n2 = input('수 입력 :')
n3 = int(n1) + int(n2) #int를 넣음으로써 문자끼리 연산에서 숫자끼리 연산으로 바뀜
print('두 수의 합 : ', n3) 
#다른 방법
print('두 수의 합 ; {}+{}={}'.format(n1,n2,n3))

name = input('이름 입력 :')
age = int( input('나이 입력 :'))
flt2 = float( input('실수 입력 :'))
print (f'{name}, type:{ type(name)}')
print (f'{age}, type:{ type(age)}')
print (f'{flt2}, type:{ type(flt2)}')
             
#test
year = int( input('올해의 년도를 4자리 입력하세요?' ))
born =int( input('당신의 태어난 년도를 4자리 입력하세요?'))
print('당신의 나이는 {}살 입니다'.format(year-born))


#test 600kg 엘리. 2개 물건 무게 실수 입력 현재 엘리 무게 구하시오
weight =600
weight1 =  float ( input('첫 번째 물건의 무게를 입력 하시오?'))
weight2 = float ( input('두 번째 물건의 무게를 입력 하시오?'))
print ('현재 엘리베이터에 허용 무게는 {}kg입니다'.format(weight-weight1-weight2)


#test 비교 글
nowYear = input('올해 년도 4자리 입력 :')
birthYear = input('당신 태어난 년도 4자리 :')
age = int (nowYear)- int(birthYear) + 1
print('나이는 {} 살 입니다'.format(age))

firstWeight = float(input('첫 무게 입력:'))
secondWeight = float(input('두 무게 입력:'))
weight = 600 - (firstWeight+secondWeight)
print('허용 무게 :', weight, 'kg입니다')

