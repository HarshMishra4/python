# Class creation
class Player:
    def __init__(self, playerType, hairColor):
        self.playerType = playerType
        self.hairColor = hairColor
    
    def run(self):
        print("Running.....")

    def shoot(self):
        print("Shooting.....")

    def crouch(self):
        print("Crouch.....")
    
    def jump(self):
        print("Jump.....")

    def printData(self):
        print("Player Type : " + self.playerType)
        print("Player Hair Color : " + self.hairColor)

# Object creation by using our Player class
player1 = Player('Female', 'Brown')

# player1.printData()
player1.run() 
player1.jump()
player1.shoot()
player1.crouch()

print("===========================")
# 2nd Object 
player2 = Player('Male', 'Brown')
player2.printData()