class Enemy:
  def __init__(self, type_of_enemy, health_points, attack_damage):
    self.__type_of_enemy = type_of_enemy
    self.health_points = health_points
    self.attack_damage = attack_damage

  def talk(self):
    print(f"Talk to your enemy {self.__type_of_enemy}")

  def walk_forward(self):
    print(f"Move forward towards to your enemy to attack {self.health_points}")

  def attack(self):
    print(f"Attack your enemy {self.attack_damage}")

  def get_enemy(self):
    return self.__type_of_enemy

 