from imports.Enemy import Enemy

# enemy = Enemy()

# print("Zombie")
# enemy.talk()
# enemy.walk_forward()
# enemy.attack()

print("===== Diaster =====")
enemy_with_effect = Enemy("Diaster", 25, 1)
enemy_with_effect.talk()
enemy_with_effect.walk_forward()
enemy_with_effect.attack()
# enemy_with_effect.__type_of_enemy = "Test Modify" # dont change the attribute and no error thrown
print(enemy_with_effect.get_enemy())
