import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lecteur_fake import Lecteurfake
from porte_spy import PorteSpy, Portedefaillante
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

    def test_badge_lumiere_verte(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte
        porte = PorteSpy()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: la lumière vert s'allume
        self.assertEqual([(False, True, False)], lecteur.couleur_affiches)

    def test_badge_lumiere_violet(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte défaillante
        porte = Portedefaillante()
        # Quand: interrogation lecteur
        try:
            ControleurAcces(porte, lecteur).interroger_lecteur()
        except Exception as e:
            # Alors: la lumière violet s'allume
            self.assertEqual([(True, False, True), (True, False, True)], lecteur.couleur_affiches)
            self.assertIsInstance(e, Exception)
    
    def test_signal_ouvert_bip(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte
        porte = PorteSpy()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: un bip retentit
        self.assertEqual(1, lecteur.nombre_appels_bip)

    def test_signal_non_ouvert_bip(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte défaillante
        porte = Portedefaillante()
        # Quand: interrogation lecteur
        try:
            ControleurAcces(porte, lecteur).interroger_lecteur()
        except Exception as e:
            # Alors: 2 bips retentissent
            self.assertEqual(2, lecteur.nombre_appels_bip)
            self.assertIsInstance(e, Exception)
    
    def test_lumiere_et_signal_ouvert(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte
        porte = PorteSpy()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: un bip retentit
        self.assertEqual(1, lecteur.nombre_appels_bip)
        # Et la lumière verte s'allume
        self.assertEqual([(False, True, False)], lecteur.couleur_affiches)
    
    def test_lumiere_et_signal_non_ouvert_bip(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte défaillante
        porte = Portedefaillante()
        # Quand: interrogation lecteur
        try:
            ControleurAcces(porte, lecteur).interroger_lecteur()
        except Exception as e:
            # Alors: 2 bips retentissent
            self.assertEqual(2, lecteur.nombre_appels_bip)
            self.assertIsInstance(e, Exception)
            # Et la lumière violet s'allume 2 fois
            self.assertEqual([(True, False, True), (True, False, True)], lecteur.couleur_affiches)
    

if __name__ == "__main__":
    unittest.main()

