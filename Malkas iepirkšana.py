
#H kilogrami malkas
#N malkas piegadataji
#P kilogrami sainos par C centi par saini
#H min kg malkas

N = int(input())
H = int(input())
maza_cena=10000000000
for i in range (N): #for cikls
    P = int(input())
    C = int(input())
    Saini=H//P
    if H%P>0:
        Saini+=1
    Cena=Saini*C
    if Cena <= maza_cena:
        maza_cena=Cena
        atbilde=Saini*C
print(atbilde)
    