menu = int(input("1.입력한 수식 계산 2.두 수 사이의 합계 :"))
sum = 0

if menu == 1:
    cal = input("***수식을 입력하세요.:")
    print(cal+"의 결과는",float(eval(cal)),"입니다다")

elif menu == 2:
    num1 = int(input("***첫 번째 숫자를 입력하세요:"))
    num2 = int(input("***두 번째 숫자를 입력하세요:"))
    for i in range(num1, num2 + 1):
        sum = sum + i
    print(num1,"+ ... +",num2,"는",sum,"입니다")
    
else:
    print("1 또는 2만 입력해주세요")