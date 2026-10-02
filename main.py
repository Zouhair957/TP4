from noeud import Noeud
"""
noeud_parent= Noeud(5)
noeud_enfant= Noeud(6)

noeud_parent.add_noeud(noeud_enfant)

print("le noeud enfant contient une liste qui a ceci:",noeud_enfant.liste_enfants)
print("le noeud enfant a une valeur de:",noeud_enfant.valeur)
print("nombre d'enfant:",len(noeud_parent.liste_enfants))

n1 = Noeud(5)
n2 = Noeud("-", [noeud_parent, noeud_enfant])

"""

# question 4


plus= Noeud("+",[Noeud(2),Noeud("y")])

exp=Noeud("exp",[plus])

print(exp.affiche_expression())

# question 5
mes_valeur={"y":2}

res=plus.evaluer(mes_valeur)

print("résultat:",res)