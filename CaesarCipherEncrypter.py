"""
CaesarCipherEncrypter v1.0
by 050644zf
Lisence: CC0
"""
upAlp=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
loAlp=('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
alp=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def shift(v):
    try:
        n=list(range(52))
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
        for i in range(52):
            d[alp[i]]=alp[n[i]]
        return d
    except:
        print("Invaild Input")

#main
print("Welcome to use the Caesar Cipher Encrypter.")
print("="*16)
ofPath=input("Origin text path: ")
of=open(ofPath,"r")
s=len(of.read())
of=open(ofPath,"r")
efPath=input("Encrypted Text Name: ")+".txt"
ef=open(efPath,"a")
ef.close()
ef=open(efPath,"r")
while len(ef.read())!=0:
    print("The file "+efPath+" already exist. Do you want to overwrite it?(Y/N):")
    if input()=="N":
       print("Please input a new name:")
       efPath=input("Encrypted Text Name: ")+".txt"
    else:
        ef.close()
        open(efPath,"w")
        ef.close()
        break
    ef=open(efPath,"r")
ef.close()
ef=open(efPath,"a")
dict=shift(int(input("Shift Value (Integer Only): ")))
for i in range(s):
    ot=of.read(1)
    if ot in dict:
        ef.write(dict[ot])
    else:
        ef.write(ot)
of.close()
ef.close()
print("Encrypt Complete!")
