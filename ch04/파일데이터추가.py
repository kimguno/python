# 파일 추가

with open('./새파일.txt','a',encoding='utf-8') as f:
    for i in range(11,20):
        data = f'{i}번째 줄\n'
        f.write(data)
        
