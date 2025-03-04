saraksts = ["banānkoks", "krūmmellenes", "pīlādzis", "ķiršu","nektarīns", "bumbieris"]
print(saraksts[0])
print(saraksts[-1])
if "nektarīns" in saraksts:
    print("IR")
else:
    print("NAV")
for i in range(len(saraksts)):
    if i%2==0:
        saraksts.insert(i, saraksts[i])
        i+1
print(saraksts)