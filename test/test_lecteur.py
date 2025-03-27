import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from .utils.lecteur_fake import Lecteurfake
from .utils.lecteur_dummy import LecteurDummy
from controleur_acces import ControleurAcces
from .utils.porte_spy import PorteSpy


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
        #Quand lecteur redémarre
        lecteur.redemarrer()
        #Alors aucun badge n'est conservé en mémoire.
        self.assertIsNone(lecteur.poll())
    
    def test_lecteur_defaillant(self):
        #Etant donné un lecteur défaillant
        lecteur= LecteurDummy()
        # ET une porte
        porte = PorteSpy()
        # Quand: Interrogation du lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        #Alors une erreur apparait
        self.assertEqual([(True, False, True), (True, False, True)], lecteur.couleur_affiches)
        
if __name__ == "__main__":
    unittest.main()

