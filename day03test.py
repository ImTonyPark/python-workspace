num = int( input("수 입력 : "))
if num % 3 == 0:
    print("{}는 3의 배수입니다")

if num % 2 == 0:
    print("{}는 짝수입니다.")
if num % 2 != 0: # num%2 == 1 
    print("{}는 홀수입니다.")    

num1 = int(input("큰수 비교 수 입력 : "))
num2 = int(input("큰수 비교 수 입력 : "))
if num1 > num2:
    print(num1,"큰 수")
if num2 > num1:
    print(num2,"큰 수")
#이런 방법도 있다.
if num1 > num2:
    max_ = num1
    #print(num1,"큰 수")
if num2 > num1:
    max_ = num2
    #print(num2,"큰 수")
print(max_, "큰 수")

num1 = int(input("절대값 수 입력 :"))
if num1 > 0:
    print(num1, "의 절대값은 :", num1)
if num1 < 0:    #이렇게도 표현된다. num * -1 => -num1
    print(num1, "의 절대값은 :",num1 * -1)


num = int(input("수 입력 : "))
if num%7 == 1: print(num," : 월요일")
if num%7 == 2: print(num," : 화요일")
if num%7 == 3: print(num," : 수요일")
if num%7 == 4: print(num," : 목요일")
if num%7 == 5: print(num," : 금요일")
if num%7 == 6: print(num," : 토요일")
if num%7 == 0: print(num," : 일요일")

print("=====세 수중 가장 큰 수======")
n1 = int(input("수 입력 : "))
n2 = int(input("수 입력 : "))
n3 = int(input("수 입력 : "))
if n1 > n2 and n1 > n3: print(n1,"가장 큰 수")
if n2 > n1 and n2 > n3: print(n2,"가장 큰 수")
if n3 > n1 and n3 > n2: print(n3,"가장 큰 수")

print("=====두 수중 큰 수가 짝수======")
n1 = int(input("수 입력 : "))
n2 = int(input("수 입력 : "))
if n1>n2 and n1%2==0:
    print(n1,"은 크며 짝수다")
if n2>n1 and n2%2==0:
    print(n2,"은 크며 짝수다")

print("=====두 수 합이 짝수며 3의 배수======")
n1 = int(input("수 입력 : "))
n2 = int(input("수 입력 : "))
sum_ = n1 + n2
if sum_ % 2==0 and sum_%3==0: #sum_ % 6==0
    print("짝수며 3의 배수다")






