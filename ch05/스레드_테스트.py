import threading
import time

# 스레드로 실행될 함수 선언
def say(msg):
    while True:
        print(msg)
        time.sleep(1)

# 3개
for msg in ['you','need','python']:
    t = threading.Thread(target=say, args=(msg,)) # 스레드 생성
    t.daemon = True # main threed 주된 스레드, t 자식 스레드
    t.start()
    
for i in range(100):
    print(i)
    time.sleep(0.1)