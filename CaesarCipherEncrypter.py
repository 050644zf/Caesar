"""
CaesarCipherEncrypter v1.0
by 050644zf
Lisence: CC0
"""
upAlp=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
loAlp=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def shift(v):
    try:
        n=list(range(52))
        print(n)
        d={}
        upAlp=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        loAlp=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        alp=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        for i in range(26):
            n[i]=i+v
            n[i+26]=i+v+26
            if n[i]>25:
                n[i]-=26
                n[i+26]-=26
            elif n[i]<0:
                n[i]+=26
                n[i+26]+=26
        print(n)
        for i in range(52):
            d[alp[i]]=alp[n[i]]
        return d
    except:
        print("Invaild Input")

