nbcookie = int(input("Combien de cookies voulez vous cuisinez ? : "))
#variable ingrédients :
beurre = nbcookie*8.33
sucre = nbcookie*13.33
oeufs = nbcookie*0.1
farine = nbcookie*20
levure_chim = nbcookie*0.0333334
chocolat = nbcookie*0.0333334
#liste ingrédients :
print("Vous aurez besoin pour cette recettes de :")
print(beurre," g de beurre")
print(sucre," g de sucre")
if oeufs > 1 :
    print(oeufs," oeufs")
else :
    print(oeufs," oeuf")
print(farine," g de farine")
if levure_chim > 1 :
    print(levure_chim," sachets de levure chimique")
else :
   print(levure_chim," sachet de levure chimique")
print(chocolat," tablette de chocolat")
#pret ?
rep = int(input("Etes vous prêts ? Répondez 1 pour commencer : "))
if rep==1 :
#instructions
    print("Pour commencer, préchauffez le four à 210°C")
    print("Mettre dans un grand bol tout les ingrédients sauf le chocolat et mélanger")
    print("Une fois que la pâte est prête, coupez les carreaux de chocolat en 3 ou 4 et les ajouter puis mélanger")
    print("Prenez un plaque de cuisson puis mettre du papier cuisson")
    print("Faire des boules uniforme légèrement applati et les disposer sur la plaque de cuisson de manière à ce qu'ils ne se touchent pas")
    print("Mettez au four pendant 10 minutes, et ça y est ! Vos cookies sont prêts")
else :
    print("Mince, relancez le programme")
