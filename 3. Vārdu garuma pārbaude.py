teikums = input()
garums=len(teikums)
saraksts = teikums.split()
print(saraksts)
burtu_saraksts=[]
for i in range(len(saraksts)):
    if (len(saraksts[i]))>5:
        burtu_saraksts.append(saraksts[i])
print(burtu_saraksts)
vardi_pec_garuma=sorted(burtu_saraksts, key=len)
print(vardi_pec_garuma)