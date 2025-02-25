skaitli = [1, 2, 3, 4, 5, 6]
n = input()
for i in range(n):
    i=skaitlis[-1]
    skaitli.remove(skaitli[-1])
    skaitli.insert(0, i)
print(skaitli) 