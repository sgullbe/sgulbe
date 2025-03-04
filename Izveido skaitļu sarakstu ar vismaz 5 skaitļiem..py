saraksts = [1, 2, 3, 4, 5, 6, 13, 2]
print(saraksts[0])
print(saraksts[-1])
reizdivi=[]
reizminuss=[]
parasaraksts=[]
neparasaraksts=[]
tirssaraksts=[]
if (len(saraksts))%2==0:
    print(saraksts[len(saraksts)//2-1])
    print(saraksts[len(saraksts)//2])
if (len(saraksts))%2!=0:
    print(saraksts[len(saraksts)//2])
if 13 in saraksts:
    print("IR")     
else: 
    print("NAV")
for i in range(len(saraksts)):
    if i%2!=0:
        saraksts[i]=saraksts[i]*2
    reizdivi.append(saraksts[i])
print(reizdivi)
for d in range(len(reizdivi)):
    if d%2!=0:
        reizdivi[d]=reizdivi[d]*(-1)
    reizminuss.append(reizdivi[d])
print(reizminuss)
for k in range(len(reizminuss)):
    if reizminuss[k]%2==0:
        parasaraksts.append(reizminuss[k])
    else :
        neparasaraksts.append(reizminuss[k])
print(parasaraksts)
print(neparasaraksts)
for sk in reizminuss:
    if tirssaraksts.count(sk)==0:
        tirssaraksts.append(sk)
print(tirssaraksts)