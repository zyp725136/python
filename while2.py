#1到100以内偶数的和
result = 0
counter = 0

while counter < 100:
    counter +=1

    if counter % 2 == 1:
        continue
    else:
        result +=counter

print(result)