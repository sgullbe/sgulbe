from math import sqrt
print("Ievadiet 4 skaitļus, lai noskaidrotu nogriežņa garumu!")
Xa = int(input())
Ya = int(input())
Xb = int(input())
Yb = int(input())
Xc = int(input())
Yc = int(input())
garumsAB=((Xa-Xb)**2+(Ya-Yb)**2)
print(garumsAB)
garumsAC=((Xa-Xc)**2+(Ya-Yc)**2)
garumsBC=((Xb-Xc)**2+(Yb-Yc)**2)
if garumsAB>garumsAC and garumsAB>garumsBC
   if (garumsAB)==(garumsAC)+(garumsBC) and garumsAC==(garumsAB)-(garumsBC) and garumsBC==(garumsAB)-(garumsAC)
   print("Taisnleņķa trijstūris")

elif garumsAC>garumsAB and garumsAC>garumsBC
   if (garumsAC)==(garumsAB)+(garumsBC) and garumsAB==(garumsAC)-(garumsBC) and garumsBC==(garumsAC)-(garumsAB)
   print("Taisnleņķa trijstūris")

elif garumsBC>garumsAB and garumsBC>garumsAC
   if (garumsBC)==(garumsAB)+(garumsAC) and garumsAB==(garumsBC)-(garumsAC) and garumsAC==(garumsBC)-(garumsAB)
   print("Taisnleņķa trijstūris")
else : 
   print("Nav taisnleņķa trijstūris")


