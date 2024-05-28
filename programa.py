def soma(num1,num2):
    total = num1 + num2
    return total

a,b = map(int, input().split())
x = soma(a,b)
print(x)