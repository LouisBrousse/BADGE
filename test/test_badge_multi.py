import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from .utils.lecteur_fake import Lecteurfake
from .utils.porte_spy import PorteSpy
from controleur_acces import ControleurAcces

class TestBadgeMulti(unittest.TestCase):

    def test_poll_consomme_le_badge(self):
        # Étant donné: Un badge valide présenté au lecteur
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
        # Étant donné: Un lecteur, une porte et un controller.
        lecteur = Lecteurfake()
        porte = PorteSpy()
        controleur = ControleurAcces(porte, lecteur)
        # Quand: Présentation de plusieurs badges valides successivement
        for _ in range(2):  # On simule 3 badges présentés
            lecteur.simuler_presentation_badge()
            controleur.interroger_lecteur()
        # Alors: chaque badge déclenche lumière verte
        self.assertTrue(porte.signal_ouverture_reçu)
        

    def test_led_plusieurs_badges_bloques_a_la_suite(self):
        # Étant donné: Deux badges bloqués présentés successivement
        lecteur = Lecteurfake()
        porte = PorteSpy()
        controleur = ControleurAcces(porte, lecteur)

        # Quand: on présente deux fois un badge bloqué
        
        for _ in range(2):
            lecteur.simuler_presentation_badge()
            controleur.bloquer_badge()
            controleur.interroger_lecteur()
        
        # Alors: chaque badge déclenche la LED rouge clignotante deux fois
        self.assertEqual([(True, False, False), (True, False, False)] * 2, lecteur.couleur_affiches)

    def test_bip_plusieurs_badges_bloques_a_la_suite(self):
        # Étant donné: Deux badges bloqués présentés successivement
        lecteur = Lecteurfake()
        porte = PorteSpy()
        controleur = ControleurAcces(porte, lecteur)
        # Quand: on présente deux fois un badge bloqué
        for _ in range(2):
            lecteur.simuler_presentation_badge()
            controleur.bloquer_badge()
            controleur.interroger_lecteur()
        
        # ET deux bips par badge bloqué (donc 4 au total)
        self.assertEqual(4, lecteur.nombre_appels_bip)   

if __name__ == "__main__":
    unittest.main()
