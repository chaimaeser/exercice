def my_function () :
  print("Question 1")
  MV1 = input("Entrez la masse volumique de la partie inférieure: ")
  MV2 = input ("Entrez la masse volumique de la partie supérieure: ")
  try:
    MV1 = float(MV1)
    MV2= float(MV2)
    MV=1000
    min = (MV1-MV)//(MV-MV2)
    print("La valeur minimale de h1/h2 est ", min)
  except:
     print("erreur")
  print("Question 2")
  import numpy as np
coeff = (1, -2,4, -3,62)
sol= np.roots(coeff)
print(sol (0).real)
my_function