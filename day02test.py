avgHeight = int(input ('키를 입력하세요? : '))
avgWeight = (avgHeight - 100)*0.9
print('표준 체중은 {}입니다'.format(avgWeight))

weight = int(input('체중 입력 :'))
obesity = (weight/avgWeight) * 100
print('표준 체중 :',avgWeight)
print('비만도 :', obesity)

studentname = input('학생 이름:')
korean =  int (input('국어점수 입력:'))
english  =  int (input('영어점수 입력:'))
math  =  int (input('수학점수 입력:'))
print ("{:=^40}".format("학생 정보"))
print ("이름\t국어\영어\t수학\t합계\t평균")
print("-"*30)
total = korean + english + math
avg = round(total / 3,2)
print(f'{studentname}\t{korean}\t{english}\t{math}\t{total}\t{avg}')
