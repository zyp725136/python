# for i in range(1,10):
#     for j in rangen(1,i+1):
#         print('hello',end=' ')
#     print()

for i in range(1,10):
    for j in range(1,i+1):
        print('%sx%s=%s' % (j,i,i*j), end=' ')
    print()