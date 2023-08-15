# 3:30 ~ 6:30

t = int(input())

for _ in range(t):
    s = list(input())
    stack = []

    # 입력받은 각 s 기준으로 YES, NO 평가
    for i in s:
        if i == '(':
            stack.append(i)
            print('after append ( = ',stack)
        elif i == ')': # 이 부분 stack 자료구조 이해가 좀 어려웠음
            if len(stack) == 0:
                stack.append(i)
                print('after append ) = ',stack)
                break # 2. 해당 경우는 False 처리 됨 (= ')'가 스택에 append 되는 경우)
            else:
                print('before pop = ', stack)
                stack.pop() # 1. if, i == ')'인 경우에 '('가 남아있으면, '('를 스택에서 pop  
                            #    참고로, 해당 경우 ')'는 스택에 append 되지 않음 (= 여는, 닫는 괄호 입력이 순서대로 처리 된 경우)

    if stack:
        print('NO') # stack의 길이가 0이 아닐 때(= 괄호가 남아있는 경우) NO 출력
    else:
        print('YES') # stack에서 pop 후 valid PS가 된 경우