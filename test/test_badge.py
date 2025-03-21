import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lecteur_fake import Lecteurfake
from porte_spy import PorteSpy, Portedefaillante
from controleur_acces import ControleurAcces
from badge import Badge

class TestBadge(unittest.TestCase):

    def test_badge_nominal(self):
        # Étant donné: Un badge valide présenté au lecteur
        badge = Badge()
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge(badge)

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

    def test_enchainement_badges(self):
        # Étant donné : Deux badges valides présentés successivement
        lecteur = Lecteurfake()
        porte = PorteSpy()

        badge1 = Badge()
        badge2 = Badge()
        badge2.numero = 42

        lecteur.simuler_presentation_badge(badge1)
        ControleurAcces(porte, lecteur).interroger_lecteur()

        lecteur.simuler_presentation_badge(badge2)
        ControleurAcces(porte, lecteur).interroger_lecteur()

        # Alors : deux bips retentissent (un pour chaque badge)
        self.assertEqual(2, lecteur.nombre_appels_bip)
        # Et : deux signaux lumineux ont été affichés
        self.assertEqual(2, len(lecteur.couleur_affiches))


    def test_badge_avec_numero_unique(self):
        # Étant donné : Un badge avec un numéro spécifique
        badge = Badge()
        badge.numero = 999
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge(badge)
    
        # ET une porte
        porte = PorteSpy()

        # Quand : interrogation du lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()

        # Alors : la porte s’ouvre
        self.assertTrue(porte.signal_ouverture_reçu)


    def test_badge_non_represente_apres_poll(self):
        # Étant donné : Un badge valide présenté une seule fois
        badge = Badge()
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge(badge)
        porte = PorteSpy()

        # Quand : interrogation une première fois (le badge est consommé)
        ControleurAcces(porte, lecteur).interroger_lecteur()

        # Et : interrogation une seconde fois sans re-présenter le badge
        ControleurAcces(porte, lecteur).interroger_lecteur()

        # Alors : un seul bip doit avoir retenti
        self.assertEqual(1, lecteur.nombre_appels_bip)

   
if __name__ == "__main__":
    unittest.main()

