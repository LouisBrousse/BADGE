import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lecteur_fake import Lecteurfake
from porte_spy import PorteSpy
from controleur_acces import ControleurAcces

class TestBadgeBloque(unittest.TestCase):

    def test_badge_bloque_acces_refuse(self):
        # Étant donné: Un badge bloqué présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte
        porte = PorteSpy()
        # ET un badge bloqué
        lecteur.simuler_badge_bloque()
        # Quand: interrogation du lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: la porte ne doit pas se déverrouiller
        self.assertFalse(porte.signal_ouverture_reçu)
    
    def test_bip_badge_bloque(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte
        porte = PorteSpy()
        # ET un badge bloqué
        lecteur.simuler_badge_bloque()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: 2 bips retentissent
        self.assertEqual(2, lecteur.nombre_appels_bip)
    
    def testled_badge_bloque(self):
        # Étant donné: Un badge bloqué présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte
        porte = PorteSpy()
        # ET un badge bloqué
        lecteur.simuler_badge_bloque()
        # Quand: interrogation du lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: la led rouge clignote deux fois
        self.assertEqual([(True, False, False), (True, False, False)], lecteur.couleur_affiches)

if __name__ == "__main__":
    unittest.main()
