# writeData 라는 모듈 생성

# 변수 선언

# 함수 선언

# 클래스 선언
# f = open('새파일.txt','w') #Positional Argument
# f = open(file='./새파일.txt',mode='w',encoding='utf-8') #Keyword Argument

# for i in range(1,11):
#     data = f'{i} 번째 줄입니다.\n'
#     f.write(data)
# f.close() # 반드시 해야 한다. close 처리 => with

with open(file='./새파일.txt',mode='w',encoding='utf-8') as f:
    for i in range(1,11):
        data = f'{i} 번째 줄.\n'
        f.write(data)
