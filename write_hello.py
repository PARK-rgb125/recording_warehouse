print("< : 입력, ?: 질의, q: 종료")
dictionary = {}

while True:
    st = input('$ ')
    command = st[0]       # 첫 입력 문자를 추출한다
    if command == '<':
        st = st[1:]
        inputStr = st.split(':')
        if len(inputStr) < 2 :
            print('입력 오류가 발생했습니다.')
        else:
            dictionary[inputStr[0].strip()] = inputStr[1].strip()
    elif command == '?':
        st = st[1:]
        inputStr = st.strip()
        if inputStr in dictionary:
            print(dictionary[inputStr])
        else :
            print('{}가 사전에 없습니다.'.format(inputStr))
    elif command == 'q':
       break
    else :
        print('입력 오류가 발생했습니다.')
print("사전 프로그램을 종료합니다.")
print(dictionary)

#for key,value in dictionary.items():
f = open('dictionary.txt','w')
f.write(f' dictionary= {dictionary.keys()}: {dictionary.values()}\n')
#이거 왜 마지막 key:value만 저장되는거지??????
print('print right ok!')
f.close()
f = open('dictionary.txt','r')
s = f.read()
print("file read:", s)
f.close()

'''
print(key, ":", phone_book[key])


f = open('dictionary.txt','r')
s = f.read()
print("file read:", s)
f.close()


딕셔너리 데이터 파일 쓰기
f,write{f' key{key}: {value}\n'}

딕셔너리 데이터 파일 읽기
data = f.readlines()

'''
