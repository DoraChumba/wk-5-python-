# Define the Superhero class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I'm {self.name} from {self.origin}, and I can {self.power}!")

class FlyingHero(Superhero):
    def __init__(self, name, origin, flight_speed):
        super().__init__(name, "fly", origin)
        self.flight_speed = flight_speed

    def introduce(self):
        print(f"I'm {self.name}, I fly at {self.flight_speed} km/h from {self.origin}!")


if __name__ == "__main__":
    hero1 = Superhero("TechMan", "machines", "Nakuru")
    hero2 = FlyingHero("Sky", "home", 300)

    hero1.introduce()
    hero2.introduce()
