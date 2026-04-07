#發瘋的教授
N = eval(input())
keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
for i in range(N):
    S = input()
    result = ''
    for s in S:
        if s == ' ':
            result += ' '
        else:
            idk = keyboard.find(s)
            result += keyboard[idk-2]
    print(result)