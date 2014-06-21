import equations

TERRAINMAPPING = {"o":"ocean","s":"shallow"}
#Provided attacker and defender args should be provided as the instances of kanmusu and enemy vessels from kanmusuDict and enemyDict. Self should be provided as... well, self.
def cannonAttack(self, attacker, defender):
	cursor = self.currentLevel.cursor
	attackerTerrainLetter = self.currentLevel.map[attacker.pos[0]][attacker.pos[1]] #Making the letter a variable cuz it was ugly to have it in one line...
	defenderTerrainLetter = self.currentLevel.map[defender.pos[0]][defender.pos[1]]
	attackerTerrain = eval("self.currentLevel.tiles."+TERRAINMAPPING[attackerTerrainLetter])
	defenderTerrain = eval("self.currentLevel.tiles."+TERRAINMAPPING[defenderTerrainLetter])
	newDefenderHP = equations.battle(attacker,defender,attackerTerrain,defenderTerrain,None,None)
	print newDefenderHP
	defender.currentHP = newDefenderHP