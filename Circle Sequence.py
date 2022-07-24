import math

n = int(input("Enter the number: "))
sqr = []
for num in range(1, int(math.sqrt(2 * n)) + 1):
    sqr.append(num ** 2)
    
seq = [1] + [2] * (n - 1)
while seq != [1] + [n] * (n - 1):
    for i in range(n):
        for j in range(i + 1, n):
            if seq[i] == seq[j]:
                break
        else:
            continue
        break

    else:
        for i in range(n):
            if seq[i] + seq[(i + 1) % n] not in sqr:
                break
        else:
            print(*seq)

    if seq[-1] == n:
        seq[-1] = 2
        inc = 'yes'
    else:
        seq[-1] += 1
        inc = 'no'
    for i in range(n - 2, 0, -1):
        if inc == 'yes':
            if seq[i] == n:
                seq[i] = 2
                inc = 'yes'
            else:
                seq[i] += 1
                inc = 'no'
