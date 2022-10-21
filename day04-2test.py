while True:
    print('='*30)
    print("\tM E N U")
    print("1. 학생 이름 입력")
    print("2. 성적 3과목(국,영.수) 입력")
    print("3. 학생 이름 출력")
    print("4. 합계 출력")
    print("5. 평균 출력")
    print("6. 종료")
    print('='*30)
    num = int(input('선택 >>>: '))
    if num == 1:
        name = input('학생의 이름을 입력하십시요 => ')
    elif num == 2:
        kor = input('국어 점수 =>')
        eng = input('영어 점수 =>')
        math = input('수학 점수 =>')
    elif num == 3:
        print('이름:',name)
    elif num == 4:
        print('3과목 성적 합계 : ',kor+eng+math)
    elif num == 5:
        print('평균 출력 : ', round((kor+eng+math)/3,2))
    else:
        break
        
