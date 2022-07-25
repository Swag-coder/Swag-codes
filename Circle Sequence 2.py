import math

def nxt_permut(seq):
    swap_ind = seq.index(max(seq))
    swap = False
    for i in range(-2, -len(seq) - 1, -1):
        if seq[i] < seq[i + 1]:
            swap = True
            break
    if swap:
        for j in range(i + 1, 0):
            if (seq[j] > seq[i]) and (seq[swap_ind] > seq[j]):
                swap_ind = j
        temp = seq[i]
        seq[i] = seq[swap_ind]
        seq[swap_ind] = temp
        seq = seq[-len(seq) : i + 1] + sorted(seq[i + 1:])

    return seq

n = int(input("Enter the number: "))
sqr = []
for num in range(1, int(math.sqrt(2 * n)) + 1):
    sqr.append(num ** 2)
    
seq = list(range(1, n + 1))
while seq != [1] + list(range(n, 1, -1)):
    for i in range(n):
        if seq[i] + seq[(i + 1) % n] not in sqr:
                break
    else:
        print(*seq)
        
    seq = nxt_permut(seq)
