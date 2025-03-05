import unittest
from lecteur_fake import Lecteur
from porte_spy import PorteSpy
from controleur_acces import ControleurAcces



class TestBadge(unittest.TestCase):
    def test_badge_nominal(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteur()
        porte = PorteSpy()
        lecteur.simuler_presentation_badge()

        # Quand: Interrogation lecteur
        controller = ControleurAcces()
        controller.interoger_lecteur(lecteur, porte)

        # Alors: signal d’ouverture (accès donné ou pas)

        self.assertTrue(porte.ouverture_porte)
    
    def test_badge_invalid_badge(self):
        # Étant donné: Un badge non-valide présenté au lecteur

        # Quand: interrogation lecteur
        
        # Alors: la porte se déverrouille (accès donné ou pas)
        self.assertEqual(1, 1)




