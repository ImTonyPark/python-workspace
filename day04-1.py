'''
if 조건식:
    종속문장
elif 조건식:
종속문장
elif ,,,,

else:
    종속문장
'''

# if문은 반복실행이기에 else if를 사용하는것이 편리하다.
num = int(input("수 입력 : "))
if num > 100:
    print("100보다 크다")
elif num > 50: #이렇게도됨 and num <= 100:
    print("50보다 크다")
elif num > 0: #이렇게도됨 and num <= 50:
    print("0보다 크다")
else:
    print("그 외의 값 입력")
print("다음 문장들 실행")

#while True: = 반복 실행 된다..  종료 ctrl c
data = '저장값이 없습니다!'
while True:
    print('='*20)
    print("1. 데이터 입력")
    print("2. 데이터 입력")
    print("3. 종료")
    print('='*20)
    #data = '저장값이 없습니다!'
#반복문을 바깥에 안적으면 계속 돌아서 안된다고 뜰것이다 참고.
    num = int(input('>>> :'))
    if num == 1:
        data = input('데이터 입력 : ')
    elif num == 2:
        print('입력 데이터 :', data)
    else:
        print('종료합니다')
        break
