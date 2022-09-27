# вывести четные числа от 2 до N по пять в строку

N = int(input())
c = 0
for i in range(2, N+1, 2):
    if c != 5:
        c += 1
    else:
        c = 1
        print()
    print(i, end=' ')



