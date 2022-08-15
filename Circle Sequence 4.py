import time
import math

sqr = []
n = int(input('Enter the number: '))
start = time.monotonic()
i = 1
while i * i < n * 2:
    sqr.append(i * i)
    i += 1
    
remaining = list(range(2, n + 1))
chain = [1]
ind = 0
found = False
while len(remaining) != n:
    for i in range(ind, len(remaining)):
        if remaining[i] + chain[-1] in sqr:
            if len(remaining) == 1 and remaining[i] + 1 not in sqr:
                continue
            chain.append(remaining[i])
            del remaining[i]
            ind = 0
            if len(remaining) != 0:
                break
            else:
                found = True
                print(*chain)
                    
    else:
        last = chain[-1]
        j = 0
        while j < len(remaining):
            if remaining[j] > last:
                remaining.insert(j, last)
                ind = j + 1
                break
            j += 1
        else:
            remaining.append(last)
            ind = len(remaining)
        del chain[-1]
        
t = time.monotonic() - start
if not found:
    print("No circle exists for the number", n)
print("Time taken: {}s".format(t))
        
            
           
