new_num_list = [] #3의 배수를 저장할 리스트 생성
for num in num_list:
    if num % 3 == 0: #입력 받은 수가 3으로 나누어 떨어지면
        new_num_list.append(num) #생성한 리스트에 추가
print(new_num_list)
