# 전역변수와 지역변수


# 각 함수들은 함수 내에 선언된 변수들이 먼저 지역 변수인지를 확인한다.
# 확인 결과 지역 변수가 아니라면 전역 변수인지를 확인한다.
def DFS1():
    cnt = 3 #  cnt변수를 생성하고 3을 할당. 지역 변수
    print(cnt)


def DFS2():
    global cnt  # 하지만, global이라고 선언하므로써 cnt변수가 전역변수임을 알려주게됨!
    if cnt == 5:
        cnt = cnt + 1  # " cnt = "의 구조를 보아 cnt라는 변수가 생성되는 것을 알 수 있고
        # 이것은 지역 변수로 선언됨. 따라서 cnt라는 변수의 값이 존재하지 않음!!
        print(cnt)

if __name__ == "__main__":
    cnt = 5  # 변수 생성 및 값을 할당한다는 의미. 전역 변수 - 모든 함수가 접근할 수 있음
    DFS1()
    DFS2()
    print(cnt)
    

# 리스트의 경우 지역과 전역의 차이
# 리스트의 경우 변수와는 다르게 global없이 제대로 작동함
def DFS():
    a[0] = 7  # " a[0] = "라는 표현은 " a = "와는 다르게 변수를 생성하는 것이 아님!
    # 그냥 a리스트의 0번 index를 참조한다는 의미!!
    print(a)

def DFS():
    global a
    a = a + [4]  # " a = "라는 표현을 통해 a리스트가 생성되는 것을 알 수 있다.
    # 하지만, a리스트가 초기화 되어있지 않기 때문에 에러가 발생한다.
    # 이때, global을 통해 에러를 제거할 수 있다.
    print(a)


if __name__ == "__main__":
    a = [1, 2, 3]
    DFS()
    print(a)