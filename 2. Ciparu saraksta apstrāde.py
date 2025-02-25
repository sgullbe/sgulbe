saraksts = [1, 2, 3, 4, 5, 6, 7, 8]
saraksts.sort()
print(saraksts[0])
print(saraksts[-1])
summa=sum(saraksts)
print(summa)
para_saraksts=[]
for i in range(len(saraksts)):
    if (saraksts[i])%2==0:
        para_saraksts.append(saraksts[i])
print(para_saraksts)