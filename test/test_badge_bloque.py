import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from .utils.lecteur_fake import Lecteurfake
from .utils.porte_spy import PorteSpy
from controleur_acces import ControleurAcces

class TestBadgeBloque(unittest.TestCase):

    def test_badge_bloque_acces_refuse(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        porte = PorteSpy()
        controleur = ControleurAcces(porte, lecteur)

        # Quand: Le badge est bloqué
        controleur.bloquer_badge()
        controleur.interroger_lecteur()

        # Alors: La porte ne doit pas se déverrouiller et la lumière rouge s'allume
        self.assertFalse(porte.signal_ouverture_reçu)
    
    def test_bip_badge_bloque(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        porte = PorteSpy()
        controleur = ControleurAcces(porte, lecteur)

        # Quand: Le badge est bloqué
        controleur.bloquer_badge()
        controleur.interroger_lecteur()
        # Alors: 2 bips retentissent
        self.assertEqual(2, lecteur.nombre_appels_bip)
    
    def test_led_badge_bloque(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        porte = PorteSpy()
        controleur = ControleurAcces(porte, lecteur)

        # Quand: Le badge est bloqué
        controleur.bloquer_badge()
        controleur.interroger_lecteur()

        # Alors: la led rouge clignote deux fois
        self.assertEqual([(True, False, False), (True, False, False)], lecteur.couleur_affiches)

    def test_debloquer_badge(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        porte = PorteSpy()
        controleur = ControleurAcces(porte, lecteur)

        # Quand: Le badge est bloqué puis débloqué
        controleur.bloquer_badge()
        controleur.debloquer_badge()
        controleur.interroger_lecteur()

        # Alors: La porte doit se déverrouiller et la lumière verte s'allume
        self.assertTrue(porte.signal_ouverture_reçu)
        self.assertEqual([(False, True, False)], lecteur.couleur_affiches)
        
if __name__ == "__main__":
    unittest.main()
