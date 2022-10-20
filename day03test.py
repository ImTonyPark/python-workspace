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


