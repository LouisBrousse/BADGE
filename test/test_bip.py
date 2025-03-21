import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lecteur_fake import Lecteurfake
from porte_spy import PorteSpy, Portedefaillante
from controleur_acces import ControleurAcces
from badge import Badge

class TestBip(unittest.TestCase):
    def test_signal_ouvert_bip(self):
        # Étant donné: Un badge valide présenté au lecteur
        badge = Badge()
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge(badge)
        # ET une porte
        porte = PorteSpy()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: un bip retentit
        self.assertEqual(1, lecteur.nombre_appels_bip)

    def test_signal_non_ouvert_bip(self):
        # Étant donné: Un badge valide présenté au lecteur
        badge = Badge()
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge(badge)
        # ET une porte défaillante
        porte = Portedefaillante()
        # Quand: interrogation lecteur
        try:
            ControleurAcces(porte, lecteur).interroger_lecteur()
        except Exception as e:
            # Alors: 2 bips retentissent
            self.assertEqual(2, lecteur.nombre_appels_bip)
            self.assertIsInstance(e, Exception)
    
    def test_badge_invalid_bip(self):
        # Étant donné: pas de bagde présenté
        lecteur = Lecteurfake()
        # ET une porte
        porte = PorteSpy()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: aucun bip ne retentit
        self.assertEqual(0, lecteur.nombre_appels_bip)

    def test_badge_bip_defaillant(self):
        # Étant donné: Un badge valide présenté au lecteur
        badge = Badge()
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge(badge)   
        # ET une porte
        porte = PorteSpy()
        # ET une défaillance du bip
        lecteur.simuler_defaillance_bip()
        # Quand: interrogation lecteur
        try:
            ControleurAcces(porte, lecteur).interroger_lecteur()
        except Exception as e:
            # Alors: aucun bip ne retentit
            self.assertEqual(0, lecteur.nombre_appels_bip)
            # Et: une exception est levée
            self.assertIsInstance(e, Exception)

    def test_badge_bip_badge_bloque(self):
        # Étant donné: Un badge valide bloqué par l'administrateur
        badge = Badge()
        lecteur = Lecteurfake()
        badge.simuler_badge_bloque_admin()
        lecteur.simuler_presentation_badge(badge)
        # ET une porte
        porte = PorteSpy()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: 2 bips retentissent
        self.assertEqual(2, lecteur.nombre_appels_bip)

if __name__ == "__main__":
    unittest.main()