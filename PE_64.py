from math import sqrt as rt
from math import gcd
from tqdm import tqdm
n = 10000
lengths = []

for i in tqdm(range(1,n+1)):
    pr = int(rt(i))
    seq = set()
    if pr*pr != i :
        
        a = 1
        b = -pr
        c = 1
        series = [pr]
        seq.add((a,b,c))
        while True :
            c2 = a*a*i - b*b
            a2 = c*a
            b2 = -b*c
                       
            GCD = gcd(gcd(a2,b2),c2)
            a = a2//GCD
            b = (b2//GCD)
            c = c2//GCD
            pr2 = (a*pr + b)//c
            b -= c*pr2
            series.append(pr2)
            if (a,b,c) in seq :
                break
            else :
                seq.add((a,b,c))
        lengths.append(len(series))

print(len([x for x in lengths if x%2 == 0 ]))
print(max(lengths))
        

            


