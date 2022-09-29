while True:
    num1 = int(input("Lütfen 1. sayıyı giriniz: "))
    num2 = int(input("Lütfen 2. sayıyı giriniz: "))
    
    op = input("Yapmak istediğiniz işlemi seçiniz(+, -, *, /): ")
    if op == '+':
        print(num1, "+", num2, "=", num1 + num2)
    elif op == '-':
        print(num1, "-", num2, "=", num1 - num2)
    elif op == '*':
        print(num1, "*", num2, "=", num1 * num2)
    elif op == '/':
        print(num1, "/", num2, "=", num1 / num2)    
    else:
        print("Hatalı seçim, tekrar deneyeiniz")