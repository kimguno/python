# mod1.py

# 불안전한 sum 메소드
# a,b 숫자가 아닌 경우 문제 발생
def sum1(a,b):
    return a + b

# 안전한 sum 메소드 : a,b 타입 체크
def safe_sum(a,b):
    if type(a) == type(b):
        return sum1(a,b)
    else:
        print('같은 타입 아님 븅신새끼야 똑바로 확인해라 ')
        return None

# 모듈 사용하는 방식
# 1. 모듈을 직접 사용 : python mod1.py (직접 실행)
# __name__ = '__main__'
# 2. 다른 모듈에서 임포트해서 사용
# __name__ = '모듈명'
# 위 함수들을 테스트
# 다른 모듈에서 import 할때는 아래 코드 실행되면 안된다
if __name__ == '__main__':
    print('mod1.py에서 실행')
    print(safe_sum(1,3))
    print(safe_sum(1,'hi'))
