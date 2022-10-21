name = input('이름 입력 : ')
su = input('학번 입력 : ')

print('3과목의 성적을 입력하시오')
kor = int(input('국어 성적 입력 : '))
eng = int(input('영어 성적 입력 : '))
math = int(input('수학 성적 입력 : '))
sum_ = kor + eng + math;avr = sum_ / 3

if avr >= 90:    result = 'A'
elif avr >= 80:    result = 'B'
elif avr >= 70:    result = 'C'
elif avr >= 60:    result = 'D'
else:    result = 'FFFFFFFF'

print('============== 학생 정보 ==================')
print('이름 : ',name,'\n학번 : ',su)
print('국 영 수 의 합 :',sum_,'\n평균 : ',avr,'\n등급 :',result)

money=0
coffee = int(input('커피의 개수를 입력 하십시오: '))
if coffee > 10: money += 20000 +(num-10)*1500;
elif coffee >0 and coffee<=10:
    money = coffee*2000;
print(money,"원 입니다.\n");

num = int(input('정수를 입력 하시요 : '))
if num == 0:
    print(num,"은(는)3의 배수도 4의 배수도 아닙니다");
elif num % 3 == 0 and num% 4 ==0:
    print(num,"은(는)3의 배수이면서,4의 배수입니다");
elif num % 3 == 0:
    print(num,"은(는)3의 배수입니다.");
elif num % 4 == 0:
    print(num,"은(는)4의 배수입니다.");
else:
    print(num,"은(는)3의 배수도 4의 배수도 아닙니다");
            
money=30000;
time = int(input("비행기 탄 시간(분): "))
time-=30
if time > 0:
   # money += (5000+((time-1)//10)*5000)또는 이거만적어서 처리가능.
    if (time%10) == 0:
        money=money+time//10*5000
    else:
        money=money+time//10*5000+5000
print(money,"원 입니다.")          
             
