from fractions import Fraction
from itertools import product

p = set([0,1,2,3])
p_indices = []
for i in p :
    for j in p - set([i]) :
        for k in p - set([i,j]):
            l = list(p-set([i,j,k]))[0]
            p_indices.append([i,j,k,l])

def gen_permutations(ls):
    return [(ls[i],ls[j],ls[k],ls[l]) for i,j,k,l in p_indices]

def calc(permutation):
    permutation = [Fraction(x) for x in permutation]
    eval_order = [
        [0,2,1],
        [0,1,2],
        [1,0,2],
        [1,2,0],
        [2,1,0]
    ]
    ops = ["-",'/','+','*']
    
    op_prod = list(product(ops,repeat=3))
    evals = set()
    for ev_ord in eval_order :
        for operators in op_prod :
            p = permutation[:]
            evaluation = 0
            updates = set()
            for i in range(3):
                opi = ev_ord[i]
                op1 = p[opi]
                op2 = p[opi+1]
                res = 0 
                if operators[opi] == '+' :
                    res = op1 + op2
                if operators[opi] == '-' :
                    res = op1 - op2
                if operators[opi] == '/' :
                    if op2 != 0 :
                        
                        res = op1 / op2
                    else :
                        res = -1
                if operators[opi] == '*' :
                    res = op1 * op2
                
                updates.add(opi)
                updates.add(opi+1)
                
                for i in updates :
                    p[i] = res
                evaluation = res
            if evaluation.denominator == 1 and evaluation.numerator > 0:
                evals.add(evaluation.numerator)
    return evals
            
def solve():
    tuples = [
        (i,j,k,l) for i in range(1,10) \
            for j in range(i,10) \
                for k in range(j,10) \
                    for l in range(k,10)
    ]
    results = []
    for t in tuples :
        res = set()
        for p in gen_permutations(t) :
            res = res.union(calc(p))
        #print(len(res))
        for i in range(1,len(res)+1) :
            if i not in res :
                results.append((t,i-1))
                #print(results[-1])
                break
    rt = None
    rl = 0 
    for x,y in results :
        if y > rl :
            rt = x
            rl = y 
    print(rt,rl)

solve()

    