
PI = 3.141592

class Math:
    '''
    [summary]
    수학관련 기능 클래스
    '''
    def solv(self, r):
        '''
        [summaty]
        
        '''
        return PI * (r**2)

def sum_(a,b):
    return a+b

if __name__ == '__main__':
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum_(PI,4.4))
