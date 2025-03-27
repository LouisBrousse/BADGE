import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from .utils.lecteur_fake import Lecteurfake
from .utils.porte_spy import PorteSpy, Portedefaillante
from controleur_acces import ControleurAcces

class TestLed (unittest.TestCase):
    
    def test_led_badge(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte
        porte = PorteSpy()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: la lumière vert s'allume
        self.assertEqual([(False, True, False)], lecteur.couleur_affiches)

    def test_led_badge_porte_defaillante_violette(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte défaillante
        porte = Portedefaillante()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: la lumière violette s'allume
        self.assertEqual([(True, False, True), (True, False, True)], lecteur.couleur_affiches)
    
    def test_led_no_badge(self):
        # Étant donné: pas de bagde présenté
        lecteur = Lecteurfake()
        # ET une porte
        porte = PorteSpy()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: aucune lumière ne s'allume
        self.assertEqual([(False, False, False)], lecteur.couleur_affiches)
    
    def test_led_defaillant_badge(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte
        porte = PorteSpy()
        # ET une défaillance de la lumière
        lecteur.simuler_defaillance_led()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: aucun signal lumineux
        self.assertEqual([(False, False, False)], lecteur.couleur_affiches)
    
        
if __name__ == "__main__":
    unittest.main()