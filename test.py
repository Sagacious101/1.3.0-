from createhero import *
import os


os.system("cls")
player = make_hero(name="Искатель", money=1000000, mp_curret=10, mage=True, defense_base=1)
enemy = make_hero(ATK_base=1, lvl=6, inventory=["сало", "рыба"])

game = True
while game:
	visit_hub(player)
	




