# Finishing-Python-in-One-Book
Following the guide of the book named 'Finishing Python in One Book'
import random

# 무작위 난수 생성
ranNum = random.sample(range(1, 100), 1)
print("난수 : ",ranNum)

# 난수 testNum 변수에 저장
testNum = ranNum[0]

# 기억력 테스트 게임 시작
print("당신의 기억력을 테스트합니다.")
print("준비되셨습니까?")
print("1. yes / 2.no")

# 1 또는 2를 입력하였는지 확인
while True:
    try:
        # 1을 입력하였을 때
        inputNum = int(input())
        type(inputNum)
        if inputNum == 1:
            # 난수를 가리기 위해 공백 문자는 50번 출력
            for i in range(50):
                print( )
                
            print("난수는?")

            # 난수에 숫자를 입력하였을 때
            while True:
                try:
                    myNum = int(input( ))
                    # 사용자 입력 수와 난수 비교
                    if myNum == testNum:
                        print("빙고~ 훌륭합니다.")
                    else:
                        print("아쉽습니다.")
                    break
                    
                # 난수에 숫자가 입력되지 않았을 때
                except ValueError:
                    print("1 또는 2만 입력 받습니다. 난수를 다시 입력해 보세요.")
            break
            
        # 2를 입력하였을 때
        elif inputNum == 2:
            print("게임을 종료합니다.")
            break
            
        # 2가 아닌 숫자를 입력하였을 때
        else:
            print("1 또는 2만 입력 받습니다. 다시 입력해 보세요.")
            
    # 숫자를 입력하지 않았을 떄
    except ValueError:
        print("1 또는 2만 입력 받습니다. 다시 입력해 보세요.")

# 아무 키나 눌러서 끝내기
print("아무 키나 눌러서 끝내기")
input()
print("기억력 게임을 종료합니다.")
