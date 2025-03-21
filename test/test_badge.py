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
        self.assertEqual([(False, False, False)], lecteur.couleur_affiches)  
    def test_poll_consomme_le_badge(self):
        # Étant donné: Un badge valide simulé
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # Quand: appel à poll
        badge_1 = lecteur.poll()
        badge_2 = lecteur.poll()
        # Alors: le premier appel détecte un badge
        self.assertIsNotNone(badge_1)
        # ET le deuxième retourne None (badge consommé)
        self.assertIsNone(badge_2)

    def test_plusieurs_badges_a_la_suite(self):
        # Étant donné: Plusieurs badges valides présentés successivement
        lecteur = Lecteurfake()
        porte = PorteSpy()
        for _ in range(3):
            lecteur.simuler_presentation_badge()
            ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: chaque badge déclenche lumière verte
        self.assertEqual([(False, True, False)] * 3, lecteur.couleur_affiches)
        # ET un bip par badge
        self.assertEqual(3, lecteur.nombre_appels_bip)
        
if __name__ == "__main__":
    unittest.main()

