d=input("entrez la densité: ")
vc=input("entrez la valeur de la viscosité cénimatique en stockes: ")
try:
    d=float(d)
    vc=float(vc)
    u= vc * 1000 * d * 0.0001
    print("la viscosité dynamique est : ",u, "PI")
except:
    print("la valeur de la densité et/ou la viscosité que vous avez donné pas correcte")