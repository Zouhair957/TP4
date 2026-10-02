class Noeud:

    def __init__(self, val, enfant=None):

        self.valeur=val
        self.liste_enfants= []
        if not enfant == None:
            self.liste_enfants=enfant
       

    def add_noeud(self, n):
        self.liste_enfants.append(n)

    def affiche_expression(self):

        texte=str(self.valeur)
        for i in self.liste_enfants:

            texte=texte + " " + i.affiche_expression()

        return texte

        
    def evaluer(self, dico):

        if type(self.valeur) in [int,float]:
            return self.valeur
        
        elif type(self.valeur)==str and len(self.liste_enfants)==0:
            if self.valeur in dico:
                return float(dico[self.valeur])
            else:
                raise ValueError("Variable manquante")

        elif type(self.valeur)==str and len(self.liste_enfants)>0:
            feuille1=self.liste_enfants[0].evaluer

            feuille2=self.liste_enfants[1].evaluer

            if self.valeur == "+":
                return feuille1 + feuille2

            if self.valeur == "-":
                return feuille1 - feuille2

            if self.valeur == "*":
                return feuille1 * feuille2


