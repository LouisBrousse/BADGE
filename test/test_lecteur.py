import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lecteur_fake import Lecteurfake
from porte_spy import PorteSpy
from controleur_acces import ControleurAcces

class TestBadge(unittest.TestCase):

    def test_lecteur_poll(self):
        # Étant donné un lecteur
        lecteur = Lecteurfake()
        # Quand on présente un badge
        lecteur.simuler_presentation_badge()
        #Alors un poll est bien détecté
        self.assertIsNotNone(lecteur.poll())
        #Et le badge est consommé.
        self.assertIsNone(lecteur.poll())
    
    def test_lecteur_poll_redemarrage(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # Quand lecteur redémarre
        lecteur.redemarrer()
        #Alors aucun badge n'est conservé en mémoire.
        self.assertIsNone(lecteur.poll())

        
if __name__ == "__main__":
    unittest.main()

