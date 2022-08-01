import time
import math

sqr = []
n = int(input('Enter the number: '))
start = time.monotonic()
for i in range(2, int(math.sqrt(n * 2)) + 1):
    sqr.append(i ** 2)
    
lst = list(range(2, n + 1))
seq = [1]
ind = 0
while len(lst) != 0 and len(lst) != n:
    for i in range(ind, len(lst)):
        if lst[i] + seq[-1] in sqr:
            if len(lst) != 1:
                seq.append(lst[i])
                del lst[i]
                ind = 0
                break
            else:
                if lst[i] + 1 in sqr:
                    seq.append(lst[i])
                    del lst[i]
                    ind = 0
                    break
                else:
                    continue
                    
    else:
        lst.append(seq[-1])
        lst.sort()
        ind = lst.index(seq[-1]) + 1
        del seq[-1]
t = time.monotonic() - start
if len(lst) == n:
    print("No circle exists for the number", n)
else:
    print(*seq)
print("Time taken: {}s".format(t))
        
            
           
