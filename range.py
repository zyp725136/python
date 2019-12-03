fib = [0,1]
n = int(input('长度:'))
for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])
print(fib)

result = 0
for i in range(0,10000001):
    result += i
print(result)

a=['192.168.1.%s'  % i for i in range(1,255)]
print(a)