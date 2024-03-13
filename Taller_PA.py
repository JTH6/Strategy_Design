class ImovementBehavior():
    def unitMovement(self):
        pass

class WalkMovement(ImovementBehavior):
    def unitMovement(self):
        print("Yo me desplazo caminando")

class RideMovement(ImovementBehavior):
    def unitMovement(self):
        print("Yo me desplazo en caballo")

class IattackBehavior():
    def unitAttackMode(self):
        pass

class SwordMode(IattackBehavior):
    def unitAttackMode(self):
        print("Yo ataco con espada")

class BowMode(IattackBehavior):
    def unitAttackMode(self):
        print("Yo ataco con arco")

class SpellMode(IattackBehavior):
    def unitAttackMode(self):
        print("Yo ataco con hechizos")

class HealsMode(IattackBehavior):
    def unitAttackMode(self):
        print("Yo no ataco, yo curo a mis aliados")

class Military_units:
    def __init__(self, movement_behavior: ImovementBehavior, attack_behavior: IattackBehavior) -> None:
        self.movement_behavior = movement_behavior
        self.attack_behavior = attack_behavior
    
    def perform_movement(self):
        self.movement_behavior.unitMovement()
    
    def perform_attack(self):
        self.attack_behavior.unitAttackMode()
    
    def display(self):
        print("Soy una unidad militar")
    
    def health(self):
        print("Tengo 100 de vida")

class Soldier(Military_units):
    def __init__(self) -> None:
        super().__init__(WalkMovement(), SwordMode())
    
    def display(self):
        print("Soy un soldado")

class Archer(Military_units):
    def __init__(self) -> None:
        super().__init__(WalkMovement(), BowMode())
    
    def display(self):
        print("Soy un arquero")
    
    def health(self):
        print("Tengo 80 de vida")

class Knight(Military_units):
    def __init__(self) -> None:
        super().__init__(RideMovement(), SwordMode())
    
    def display(self):
        print("Soy un caballero")
    
    def health(self):
        print("Tengo 120 de vida")

class Priest(Military_units):
    def __init__(self) -> None:
        super().__init__(WalkMovement(), HealsMode())
    
    def display(self):
        print("Soy un sacerdote")
    
    def health(self):
        print("Tengo 70 de vida")

class Wizard(Military_units):
    def __init__(self) -> None:
        super().__init__(WalkMovement(), SpellMode())
    
    def display(self):
        print("Soy un mago")

if __name__ == '__main__': 

# Soldier Zone 
    soldier = Soldier()  
    soldier.perform_movement()
    soldier.perform_attack()
    soldier.display()
    soldier.health()

# Archer Zone
    archer = Archer()  
    archer.perform_movement()
    archer.perform_attack()
    archer.display()
    archer.health()

# Knight Zone
    knight = Knight()  
    knight.perform_movement()
    knight.perform_attack()
    knight.display()
    knight.health()

# Priest Zone
    priest = Priest()
    priest.perform_movement()
    priest.perform_attack()
    priest.display()
    priest.health()

# Wizard Zone
    wizard = Wizard()
    wizard.perform_movement()
    wizard.perform_attack()
    wizard.display()
    wizard.health()