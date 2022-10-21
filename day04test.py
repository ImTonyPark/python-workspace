Gbyte = int(input('Gbyte 입력 : '))
num = int(input('1.byte 2.Kbyte 3.Mbyte >>'))
if num == 1:
    print(Gbyte*1024**3, "byte")
if num == 2:
    print(Gbyte*1024**2, "kb")
if num == 3:
    print(Gbyte*1024, "mb")

#40byte, 5120Kbyte, 5Mbyte >>>1
#5: 5368709120 byte

'''
bit : 8 -> 1byte
byte : 1024 -> 1KB
KByte : 1024 -> 1MB
MByte : 1024 -> 1GB
GByte : 1024 -> 1TB

'''

save_id = input('저장할 id 입력 : ')
save_pw = input('저장할 pw 입력 : ')

input_id = input(' id 입력 :')
input_pw = input(' pw 입력 :')


if save_id == input_id:
    if save_pw == input_pw:
        print('인증 통과')
    else:
        print('등록되지 않은 아이디입니다')
else:
    print('비밀번호가 틀렸습니다')

