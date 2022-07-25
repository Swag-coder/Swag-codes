seq = input("Enter the sequence of nos separated by spaces and terminated by '.' : ").split()
seq[-1] = seq[-1][:len(seq[-1])-1]
for i in range(len(seq)):
    seq[i] = int(seq[i])
print(seq)

def nxt_permut(seq):
    swap_ind = seq.index(max(seq))
    swap = 'no'
    for i in range(-2, -len(seq) - 1, -1):
        for j in range(i + 1, 0):
            if seq[j] > seq[i]:
                swap = 'yes'
                if seq[swap_ind] > seq[j]:
                    swap_ind = j
        if swap == 'yes':
            temp = seq[i]
            seq[i] = seq[swap_ind]
            seq[swap_ind] = temp
            seq = seq[-len(seq) : i + 1] + sorted(seq[i + 1:])
            break
    return seq

seq = nxt_permut(seq)        
print("The next permutation is:")
print(seq)
