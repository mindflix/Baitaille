import random

menu = str(input("Saisir le mode de jeu (26 cartes ou classique): "))

class Carte():
    def __init__(self):
        self.valeurs = ["2","3","4","5","6","7","8","9","10","Valet","Dame","Roi","As"]
        self.couleurs = ["♠","♣","♥","♦"]
        self.jeu_carte = []
        self.pot = []
    
    def jeu(self):
        for valeur in self.valeurs:
            for couleur in self.couleurs:
                self.jeu_carte.append(str(valeur)+" de "+str(couleur))

    def melange(self):
        random.shuffle(self.jeu_carte)

    def divise(self):
        self.joueur_1 = []
        self.joueur_2 = []
        self.joueur_1 = self.jeu_carte[0:len(self.jeu_carte)//2]
        self.joueur_2 = self.jeu_carte[len(self.jeu_carte)//2:]

    def bataille_class(self):
        while len(self.joueur_1) != 0 and len(self.joueur_2) != 0:
            cA = self.joueur_1.pop()
            cB = self.joueur_2.pop()
            print(cA+" contre "+cB)
            print("Joueur 1: ",len(self.joueur_1),"Joueur 2: ",len(self.joueur_2))
            self.cA_ = cA.split()
            self.cB_ = cB.split()
            
            hasard = [0,1]
            hasard = random.choice(hasard)
            if hasard == True:
                self.pot.append(cA)
                self.pot.append(cB)
            else:
                self.pot.append(cB)
                self.pot.append(cA)

            if self.valeurs.index(self.cA_[0]) < self.valeurs.index(self.cB_[0]):
                self.pot.reverse()
                self.joueur_2 = self.pot + self.joueur_2
                self.pot = []
                print("_____________________________________")
            
            elif self.valeurs.index(self.cA_[0]) > self.valeurs.index(self.cB_[0]):
                self.pot.reverse()
                self.joueur_1 = self.pot + self.joueur_1
                self.pot = []
                print("_____________________________________")

            else:
                if (len(self.joueur_1) == 0 or len(self.joueur_2) == 0):
                    if len(self.joueur_2) == 0:
                        self.joueur_1 = self.pot + self.joueur_1
                        self.pot = []
                        print("______________SUPRÊME1_______________")
                    else:
                        self.joueur_2 = self.pot + self.joueur_2
                        self.pot = []
                        print("______________SUPRÊME2_______________")

                elif (len(self.joueur_1) == 1 or len(self.joueur_2) == 1):
                    if len(self.joueur_2) == 1:
                        self.joueur_1 = self.pot + self.joueur_1
                        self.pot = []
                        print("______________SUPRÊME1_______________")
                    else:
                        self.joueur_2 = self.pot + self.joueur_2
                        self.pot = []
                        print("______________SUPRÊME2_______________")
        
                else:
                    cCA = self.joueur_1.pop()
                    cCB = self.joueur_2.pop()
                    print(cCA+" contre "+cCB+" (Carte Cachée)")
                    self.pot.append(cCA)
                    self.pot.append(cCB)


        print(len(self.joueur_1),len(self.joueur_2))
        if len(self.joueur_2) == 0:
            print("> VICTOIRE1 <")
        else:
            print("> VICTOIRE2 <")


    def option1(self):
        self.jeu()
        self.melange()
        self.divise()
        self.bataille_class()

    def bataille_26(self):
        while len(self.joueur_1) != 0 and len(self.joueur_2) != 0:
            cA = self.joueur_1.pop()
            cB = self.joueur_2.pop()
            print(cA+" contre "+cB)
            print("Joueur 1: ",len(self.joueur_1),"Joueur 2: ",len(self.joueur_2))
            self.cA_ = cA.split()
            self.cB_ = cB.split()

            hasard = [0,1]
            hasard = random.choice(hasard)
            if hasard == True:
                self.pot.append(cA)
                self.pot.append(cB)
            else:
                self.pot.append(cB)
                self.pot.append(cA)

            if self.valeurs.index(self.cA_[0]) < self.valeurs.index(self.cB_[0]):
                self.pot2.append(cB) 
                print("_____________________________________")
            
            elif self.valeurs.index(self.cA_[0]) > self.valeurs.index(self.cB_[0]):
                self.pot1.append(cA)
                print("_____________________________________")

            if self.valeurs.index(self.cA_[0]) == self.valeurs.index(self.cB_[0]):
                cCA = self.joueur_1.pop()
                cCB = self.joueur_2.pop()
                print(cCA+" contre "+cCB+" (Carte Cachée)")
                self.pot.append(cCA)
                self.pot.append(cCB)
                
            if len(self.pot1) > len(self.pot2):
                print("> VICTOIRE1 <")

            elif len(self.pot1) < len(self.pot2):
                print("> VICTOIRE2 <")

            elif len(self.pot1) == len(self.pot2):
                print("> EGALITE <")

    def option2(self):
        self.jeu()
        self.melange()
        self.divise()
        self.pot1 = []
        self.pot2 = []
        self.bataille_26()


if __name__ == "__main__":
    if menu == "classique":
        Config1 = Carte().option1()
    elif menu == "26":
        Config2 = Carte().option2()