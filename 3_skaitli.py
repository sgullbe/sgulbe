print("Ievadiet 3 skaitļus")
skaitlis1 = int(input())
skaitlis2 = int(input())
skaitlis3 = int(input())

if skaitlis1+skaitlis2>0 or skaitlis1+skaitlis3>0 or skaitlis2+skaitlis3>0:
    print("VAR")

else:
    print("NEVAR")
if skaitlis1+skaitlis2==0 or skaitlis1+skaitlis3==0 or skaitlis2+skaitlis3==0:
    print("VAR")
else:
    print("NEVAR")
    
if skaitlis1+skaitlis2<0 or skaitlis1+skaitlis3<0 or skaitlis2+skaitlis3<0:
    print("VAR")

else:
    print("NEVAR")