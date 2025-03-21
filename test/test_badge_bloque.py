import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lecteur_fake import Lecteurfake
from porte_spy import PorteSpy, Portedefaillante
from controleur_acces import ControleurAcces
from badge import Badge

class TestBadgeBloque(unittest.TestCase):

    def test_badge_bloque_led_rouge(self):
        # Étant donné: Un badge bloqué par l'administrateur
        badge = Badge()
        badge.simuler_badge_bloque_admin()
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge(badge)
        
        # ET une porte fonctionnelle
        porte = PorteSpy()
        
        # Quand: interrogation du lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        
        # Alors: La led rouge s'allume 2 fois
        self.assertEqual([(True, False, False), (True, False, False)], lecteur.couleur_affiches)
        
        # Et: La porte ne s'ouvre pas
        self.assertFalse(porte.signal_ouverture_reçu)
    
    def test_badge_bloque_led_rouge_porte_defaillante(self):
        # Étant donné: Un badge bloqué par l'administrateur
        badge = Badge()
        badge.simuler_badge_bloque_admin()
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge(badge)
        
        # ET une porte défaillante
        porte = Portedefaillante()
        
        # Quand: interrogation du lecteur
        try:
            ControleurAcces(porte, lecteur).interroger_lecteur()
        except Exception:
            pass  # On capture l'exception pour tester la led
        
        # Alors: La led rouge s'allume 2 fois
        self.assertEqual([(True, False, False), (True, False, False)], lecteur.couleur_affiches)
        
        # Et: La porte reste bloquée
        self.assertFalse(hasattr(porte, 'signal_ouverture_reçu'))  # Vérifie qu'aucune ouverture n'a été enregistrée
    
    def test_badge_bloque_avec_led_defaillante(self):
        # Étant donné : Un badge bloqué par l’administrateur
        badge = Badge()
        badge.simuler_badge_bloque_admin()
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge(badge)

        # ET une porte fonctionnelle
        porte = PorteSpy()

        # ET une défaillance de la LED
        lecteur.simuler_defaillance_led()

        # Quand : interrogation du lecteur
        with self.assertRaises(Exception):
            ControleurAcces(porte, lecteur).interroger_lecteur()

        # Alors : aucun bip n’a retenti car la LED a provoqué une exception avant
        self.assertEqual(0, lecteur.nombre_appels_bip)

if __name__ == "__main__":
    unittest.main()