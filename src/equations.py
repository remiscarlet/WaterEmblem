import random

# Provided args should be the class instances of each item. Global modifies should be listed as a kwargs
# attackerFormation should be supplied as a string, as should engagementForm
def battle(attacker, defender, attackerTerrain, defenderTerrain, attackerFormation, engagementForm, **globalModifiers):
	#These are all modifier variables with their respective values. FPR = Flagship Protection Rate.
	#
	# I don't think we can actually incorporate formations... Ideas?
	#
	#formationModifiers = {"Line Ahead":{"Firepower":1."ASW":.45,"AA":1,"Shelling Acc":"Medium","Torp Acc":"High","FPR":"Low"},
	#					  "Double Line":{"Firepower":.8."ASW":.6,"AA":1.2,"Shelling Acc":"High","Torp Acc":"Medium","FPR":"Medium"},
	#					  "Diamond":{""}
	#
	# But for now keeping a temp formation modifier as copying the damage calculations from wiki.
	#

	formationModifiers = {"Firepower":1,"ASW":1,"AA":1,"Shelling Acc":"Medium","Torp Acc":"Medium","FPR":"Medium"}

	#
	# Are we also not doing remaining ammo? Cuz that's a relatively important modifier... We'll prob want to make our own modifiers.
	#
	attackPower = (attacker.firepower*formationModifiers["Firepower"])
	defendingPower = (defender.armor)*(random.randint(66,133)/100.0)
	
	damage = (attackPower-defendingPower)#*attacker.remainingAmmo
	defenderRemainingHP = defender.currentHP-damage if damage>0 else defender.currentHP

	return defenderRemainingHP