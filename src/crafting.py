import os
import random

class shipClasses:
	def __init__:
		self.regcraft = {self.DD:750, self.Rare_DD:0, self.CL:200, self.CA:50, self.Fast_BB:0, self.BBV:0, self.Rare_BB:0, self.CVL:0, self.CV:0, self.SS:0, self.AV:0}
		self.DD = ("Fubuki", "Shirayuki", "Murakumo", "Sazanami", "Ushio", "Akatsuki", "Inazuma", "Ikazuchi", "Hibiki", "Shigure", "Yuudachi", "Samidare") #incomplete
		self.Rare_DD = ("Shimakaze", "Yukikaze")
		self.DE_DD = ("Z1", "Z3")
		self.CL = ("Tenryuu", "Tatsuta", "Kuma", "Tama", "Kiso", "Sendai", "Jintsuu", "Naka", "Ooi", "Kitakami", "Yuubari") #incomplete
		self.LSC_CL = ("Agano", "Noshiro", "Yahagi") 
		self.CA = ("Furutaka", "Kako", "Choukai", "Tone", "Mogami", "Suzuya", "Kumano") #incomplete
		self.LSC_CA = ("Mikuma")
		self.Fast_BB = ("Kongou", "Hiei", "Kirishima", "Haruna")
		self.BBV = ("Ise", "Hyuuga", "Fusou", "Yamashiro")
		self.Rare_BB = ("Nagato", "Mutsu")
		self.LSC_BB = ("Yamato")
		self.CVL = ("Houshou", "Ryuujou", "Hiyou", "Junyou", "Zuihou", "Shouhou")
		self.CV = ("Akagi", "Kaga", "Souryuu", "Hiryuu", "Shoukaku", "Zuikaku")
		self.LSC_CV = ("Taihou")
		self.SS = ("Hachi", "Imuya", "Goya")
		self.LSC_SS = ("Maruyu")
		self.AV = ("Chitose", "Chiyoda")
		self.LSD = ("Akitsumaru")





def shipCraft(fuel, steel, ammo, baux):
	craft = shipClasses()
	#Fuel Calculations
	if fuel < 240:
		craft.CL += (fuel-30)/2
		craft.CA += (fuel-30)/4
	if fuel > 240:
		craft.CL += (fuel-240)/4
		craft.CA += (fuel-240)/2
		craft.Rare_DD += (fuel-240)/3
	if fuel > 400:
		craft.DD = 0
		craft.CL = 0

def LSC(fuel, steel, ammo, baux, dev):
	pass

def eqCraft(fuel, steel, ammo, baux):
	pass
