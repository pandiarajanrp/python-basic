class Enemy:
  type_of_enemy = "Zombie"
  health_points = 10
  attack_damage = 1

  def __init__(self, type_of_enemy, health_points, attack_damage):
    self.type_of_enemy = type_of_enemy
    self.health_points = health_points
    self.attack_damage = attack_damage

  def talk(self):
    print(f"Talk to your enemy {self.type_of_enemy}")

  def walk_forward(self):
    print(f"Move forward towards to your enemy to attack {self.health_points}")

  def attack(self):
    print(f"Attack your enemy {self.attack_damage}")

 