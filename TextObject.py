from DescriptionTicket import DescriptionTicket

#Classe pour une description de type texte
class TextObject(DescriptionTicket):
#Fonction pour charger le texte
    def load(self)->str:
        return f"Chargement du texte : {self.chemin}"