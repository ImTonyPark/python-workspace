'''
if 조건식:
    종속문장
else:
    종속문장
다음문
'''
'''
num = int(input('수 입력 :'))
if num == 1:
    print('1입력')
else:
    print('그 외의 값 입력')
print('다음 문장들 실행')
'''

save_id = input('저장할 id 입력 : ')
print('인증 프로그램')
input_id = input('비교할 id 입력 :')
if save_id == input_id:
    print('인증 통과')
else:
    print('인증 실패')


num = 9
if num % 3 == 0:
    if num % 2 == 0:
        print ('num 2,3의 배수 입니다.')
        print ('num 짝수이며 3의 배수 입니다.')
    else:
        print('num은 3의 배수이며 짝수는 아닙니다')
else:
    print('num은 3의 배수가 아닙니다')
print('다음 문장들 실행')

    
