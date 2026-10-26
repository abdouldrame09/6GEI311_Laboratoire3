from abc import ABC, abstractmethod

#Classe abstraite pour les descriptions
class DescriptionTicket(ABC):
    def __init__(self,chemin:str):
        self.chemin=chemin

#Fonction pour retourner le chemin
    def getChemin(self)->str:
        return self.chemin

#Fonction abstraite pour charger la description
    @abstractmethod
    def load(self)->str:
        pass

#Fonction pour afficher la description
    def __str__(self)->str:
        return f"{self.__class__.__name__} : {self.chemin}"








