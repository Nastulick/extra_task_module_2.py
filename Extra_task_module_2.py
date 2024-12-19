string = ''
k = range(3,21)
for k in range (3,21):
    print(f'Пары значений для k = {k}:')
    for i in range (1,k+1):
        print(f'(i = {i},k = {k})')
        print()
        for j in range (i+1,k-1):
            if j>i:
                print(f'(j = {j})')
            if k % (i+j) == 0:
                print()
string += str(i) + str(j)
print(string)






