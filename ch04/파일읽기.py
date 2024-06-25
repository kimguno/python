# 파일 읽기 메소드
# readline() : 첫번째 한줄 읽기 => 문자열 반환 => 한 줄만 반환
# readlines() : 한줄씩 읽어서 리스트로 반환 => 전체 반환
# read() : 전체를 문자열로 읽기 => 문자열을 반환 => 전체 반환


# 한줄 읽기 코드
with open('./새파일.txt','r',encoding='utf-8') as f:
    line = f.readline() #한줄 읽기
    
    print(line)
    
# 전체 줄단위로 읽기 출력
with open('./새파일.txt','r',encoding='utf-8') as f:
    while True:
        line = f.readline() #한줄 읽기
        print(line)
        if not line: # 값이 있으면 True, line이 False(None)
            break

# 전체 줄단위로 읽기 출력
with open('./새파일.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
    
    for line in lines:
        print(line)


# 전체 통으로 읽기 : read()
with open('./새파일.txt','r',encoding='utf-8') as f:
    lines = f.read()

print(lines)


