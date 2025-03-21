import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lecteur_fake import Lecteurfake
from porte_spy import Portedefaillante
from controleur_acces import ControleurAcces

class TestBadgeBloque(unittest.TestCase):

    def test_badge_bloque_led_rouge(self):
        # Étant donné: Un badge bloqué présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte qui refuse l'ouverture (badge bloqué)
        porte = Portedefaillante()
        # Quand: interrogation du lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: la led violette (rouge + bleu) clignote deux fois
        self.assertEqual([(True, False, True), (True, False, True)], lecteur.couleur_affiches)

    def test_badge_bloque_acces_refuse(self):
        # Étant donné: Un badge bloqué présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte qui refuse l'ouverture
        porte = Portedefaillante()
        # Quand: interrogation du lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: accès non autorisé (pas d'ouverture)
        # Et led violette clignote deux fois
        self.assertEqual([(True, False, True), (True, False, True)], lecteur.couleur_affiches)

if __name__ == "__main__":
    unittest.main()
