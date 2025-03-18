import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lecteur_fake import Lecteurfake
from porte_spy import PorteSpy
from controleur_acces import ControleurAcces

class TestBadge(unittest.TestCase):
    def test_badge_nominal(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte
        porte = PorteSpy()
        # Quand: Interrogation du lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: signal d’ouverture (accès donné ou pas)
        self.assertTrue(porte.signal_ouverture_reçu)
    
    def test_badge_invalid_badge(self):
        # Étant donné: pas de bagde présenté
        lecteur = Lecteurfake()
        # ET une porte
        porte = PorteSpy()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: la porte ne doit pas se déverrouiller
        self.assertFalse(porte.signal_ouverture_reçu)
        self.assertEqual([], lecteur.couleur_affiches)  

if __name__ == "__main__":
    unittest.main()

