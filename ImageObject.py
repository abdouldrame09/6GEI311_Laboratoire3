from DescriptionTicket import DescriptionTicket

#Classe pour une description de type image
class ImageObject(DescriptionTicket):
#Fonction pour charger l'image
    def load(self)->str:
        return f"Chargement de l'image : {self.chemin}"