class Badge():
    def __init__(self):
        self.numero = 0
        self.bloque_admin = False

    def is_badge_bloque(self) -> bool:
        return self.bloque_admin
    
    def get_numero_badge(self) -> int:
        return self.numero
    
    def simuler_badge_bloque_admin(self):
        self.bloque_admin = True