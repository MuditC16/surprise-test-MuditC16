n=eval(input())
def expand(n):
    l=[]
    d=1
    while d <len(n):
        if n[d]>n[d-1]:
            a=n[d]-n[d-1]
        elif n[d]<n[d-1]:
            a=n[d-1]-n[d]
        l.append(a)
        d+=1
    b=l.copy()
    return sorted(b)==l
    b.sort()
    i=0
    while i <len(b):
        if b[i]==b[i+1]:
            return False
d=expand(n)
print(d)