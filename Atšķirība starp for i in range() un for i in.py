teikums = input()
lielo_sk=0
lielo_sk_varda=0
lielo=0
for i in range(len(teikums) ):
    if teikums[i]>='A' and teikums[i]<='Z':
        lielo_sk+=1
if lielo_sk>0:
    print("IR DRUKATIE")
else :
    print("NAV")
vardi=teikums.split() 
# tiek sadalīts pa vārdiem, iegūstot vārdu sarakstu.
for vards in vardi:
    lielo_sk_varda=0
    for i in range(len(vards) ):
        if vards[i]>='A' and vards[i]<='Z':
            lielo_sk_varda+=1
        print(lielo_sk_varda, end=" ")
for i in range(len(vards)):
    lielo=0
    for j in range(len(vards[i]) ):
        if vards[i][j]>='A' and vards[i][j]<='Z':
            lielo+=1
    if lielo==len(vardi[i])
        print(i+1, end=" ")
