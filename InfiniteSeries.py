class Term:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp

    def times(self,t2):
        coeff = self.coeff*t2.coeff
        exp = self.exp+t2.exp
        return Term(coeff, exp)

    def __eq__(self, other):
        return self.exp == other.exp and self.coeff == other.coeff

    def __gt__(self, other):
        return self.exp>other.exp

    def to_string(self):
        s = ""
        return str(self.coeff) + "q^" + str(self.exp)

# comparison from this link: https://stackoverflow.com/questions/5824382/enabling-comparison-for-classes
# or here: https://www.mostlypython.com/oop-in-python-part-8-comparing-objects/

# ts = [Term(1,2),Term(1,0),Term(1,1)]
# ts.sort()
# for t in ts:
#     print(t.to_string())


class Factor:
    def __init__(self, terms = []):
        self.terms = terms

    def times(self,f2):
        trms = []
        for term1 in self.terms:
            for term2 in f2.terms:
                trms.append(term1.times(term2))
        trms.sort()
        rtrn = Factor(trms)
        rtrn.combine()
        return rtrn

    def combine(self):
        exp = -1
        sum = None
        trms2 = []
        for t in self.terms:
            if t.exp > exp:
                if sum is not None:
                    trms2.append(sum)
                exp = t.exp
                sum = t
            else:
                sum.coeff += t.coeff
        if sum is not None:
            trms2.append(sum)
        self.terms = trms2

    def to_string(self):
        s = ""
        self.terms.sort()
        for i,term in enumerate(self.terms):
            if(term.coeff!=0):
                s += term.to_string()
                if i < len(self.terms) - 1:
                    s += " + "
        return s

# f1 = Factor([Term(1,2),Term(2,1),Term(1,0)])
# f2 = Factor([Term(2,2),Term(-1,1),Term(-2,0)])
# p = f1.times(f2)
# print(p.to_string())

terms = []
prdct = Factor([Term(1, 1)])
for i in range(1,100):
    print(i)
    f1 = Factor([Term(1,0),Term(-1,i)])
    f2 = Factor([Term(1,0),Term(-1,11*i)])
    sq1 = f1.times(f1)
    # print("sq1 = " + sq1.to_string())
    sq2 = f2.times(f2)
    # print("sq2 = " + sq2.to_string())
    prdct = sq1.times(sq2).times(prdct)
    # print("prdct = " + prdct.to_string())
f = open("coeffs.txt","w")
for term in prdct.terms:
    f.write(str(term.coeff)+"\n")
f.close()
