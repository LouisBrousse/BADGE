import unittest
import sys
import os

# Ajouter le dossier 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lecteur_fake import Lecteurfake
from porte_spy import PorteSpy, Portedefaillante
from controleur_acces import ControleurAcces

class TestBip(unittest.TestCase):
    def test_bip_badge(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte
        porte = PorteSpy()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: un bip retentit
        self.assertEqual(1, lecteur.nombre_appels_bip)

    def test_bip_badge_porte_defaillante(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte défaillante
        porte = Portedefaillante()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: 2 bips retentissent
        self.assertEqual(2, lecteur.nombre_appels_bip)
            
    def test_bip_no_badge(self):
        # Étant donné: pas de bagde présenté
        lecteur = Lecteurfake()
        # ET une porte
        porte = PorteSpy()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: aucun bip ne retentit
        self.assertEqual(0, lecteur.nombre_appels_bip)

    def test_bip_defaillant_badge(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()   
       # ET une porte
        porte = PorteSpy()
        # ET une défaillance du bip
        lecteur.simuler_defaillance_bip()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: aucun bip ne retentit
        self.assertEqual(0, lecteur.nombre_appels_bip)
    
    def test_bip_defaillant_badge_bloque(self):
        # Étant donné: Un badge valide présenté au lecteur
        lecteur = Lecteurfake()
        lecteur.simuler_presentation_badge()
        # ET une porte défaillante
        porte = Portedefaillante()
        # ET une défaillance du bip
        lecteur.simuler_defaillance_bip()
        # Quand: interrogation lecteur
        ControleurAcces(porte, lecteur).interroger_lecteur()
        # Alors: aucun bip ne retentit malgré l'accès refusé
        self.assertEqual(0, lecteur.nombre_appels_bip)

if __name__ == "__main__":
    unittest.main()
            