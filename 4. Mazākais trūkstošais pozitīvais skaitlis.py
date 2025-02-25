skaitli = [3, 7, 1, 2, 8, 4, 5]
skaitli.sort()
for i in range(len(skaitli)-1):
    if skaitli[i]+1!=skaitli[i+1]:
        print(skaitli[i]+1)
        break
