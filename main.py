import os
import tkinter as tk

#Importation des classes metier
from Statut import Statut
from Priorite import Priorite
from TypeDescription import TypeDescription
from DescriptionFactory import DescriptionFactory
from Ticket import Ticket
from User import User
from Developpeur import Developpeur
from GestionnaireTickets import GestionnaireTickets

#Importation de la classe d'interface graphique
from ApplicationGUI import ApplicationGUI

def main():
    # 1. Creation du gestionnaire de tickets centralise
    gestionnaire = GestionnaireTickets()

    # 2. Creation des utilisateurs et developpeurs
    user1 = User("Alpha", "alpha@uqac.ca")
    user2 = User("bob", "bob@uqac.ca")
    dev1 = Developpeur("Abdramane", "abdramane@uqac.ca")
    dev2 = Developpeur("Ibrahim", "ibrahim@uqac.ca")

    utilisateurs = [user1, user2]
    developpeurs = [dev1, dev2]

    # 3. Chargement des donnees de test initiales
    dossier_courant = os.path.dirname(os.path.abspath(__file__))
    image_erreur = os.path.join(dossier_courant, "images", "capture_erreur.png")

    # Ticket 1 : Contient TEXTE et IMAGE
    ticket1 = Ticket(title="Erreur d'affichage au demarrage", priority=Priorite.HAUTE)
    desc_texte1 = DescriptionFactory.createDescription(
        TypeDescription.TEXTE,
        "L'application plante lors de l'ouverture sur Windows."
    )
    desc_image1 = DescriptionFactory.createDescription(TypeDescription.IMAGE, image_erreur)
    ticket1.addDescription(desc_texte1)
    ticket1.addDescription(desc_image1)
    user1.createTicket(ticket1)
    gestionnaire.ajouter(ticket1)

    # Ticket 2 : Contient TEXTE uniquement
    ticket2 = Ticket(title="Bouton mal aligne", priority=Priorite.BASSE)
    desc_texte2 = DescriptionFactory.createDescription(
        TypeDescription.TEXTE,
        "Le bouton Quitter depasse de la fenetre."
    )
    ticket2.addDescription(desc_texte2)
    user2.createTicket(ticket2)
    dev1.assignTicket(ticket2, dev1)
    gestionnaire.ajouter(ticket2)

    # 4. Lancement de la fenetre principale Tkinter via ApplicationGUI
    fenetre = tk.Tk()
    app = ApplicationGUI(fenetre, gestionnaire, utilisateurs, developpeurs)
    fenetre.mainloop()

if __name__ == "__main__":
    main()
