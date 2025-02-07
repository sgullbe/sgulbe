pirmais_v = input()
otrais_v = input()
sakrita=0
for p in range(len(pirmais_v)):
    for o in range(len(otrais_v)):
        if pirmais_v[p]==otrais_v[o]:
            sakrita+=1
            otrais_v = otrais_v[:o]+'#' + otrais_v[o+1:]
            break
if sakrita==len(otrais_v):
    print("VAR")
else:
    print("NEVAR")