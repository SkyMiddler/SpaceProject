  class Planet:
    def __init__ (self, name):
        self.name=name
    def distanceFromSun(self):
        if self.name=="Mercury":
            return 35.98
        elif (self.name=="Venus"):
            return 67.24
        elif self.name=="Earth":
            return 92.96
        elif self.name=="Mars":
            return 141.6
        elif self.name=="Jupiter":
            return 483.8
        elif self.name=="Saturn":
            return 888.2
        elif self.name=="Uranus":
            return 1.784
        elif self.name=="Neptune":
            return 2.795
        else:
            return -1
    def type(self):
        if self.name=="Mercury" or self.name=="Venus" or self.name=="Earth" or self.name=="Mars":
            return "Terrestrial"
        elif self.name=="Jupiter" or self.name=="Saturn" or self.name=="Uranus" or self.name=="Neptune":
            return "Gas Giant"
        else:
            return "Planet not found"
    def numOfMoons(self):
        if self.name=="Mercury":
            return 0
        elif self.name=="Venus":
            return 0
        elif self.name=="Mars":
            return 1
        elif self.name=="Jupiter":
            return 67 
        elif self.name=="Saturn":
            return 62
        elif self.name=="Uranus":
            return 27
        elif self.name=="Neptune":
            return 14
        else:
            return -1
    def radius(self):
        if self.name=="Mercury":
            return 1516
        elif self.name=="Venus":
            return 3760
        elif self.name=="Earth":
            return 3959
        elif self.name=="Mars":
            return 2106
        elif self.name=="Jupiter":
            return 43441
        elif self.name=="Saturn":
            return 36184
        elif self.name=="Uranus":
            return 15759
        elif self.name=="Neptune":
            return 15299
        else:
            return -1
    def density(self):
        if self.name=="Mercury":
            return 5.43
        elif self.name=="Venus":
            return 5.24
        elif self.name=="Earth":
            return 5.51
        elif self.name=="Mars":
            return 3.93
        elif self.name=="Jupiter":
            return 1.33
        elif self.name=="Saturn":
            return 0.687
        elif self.name=="Uranus":
            return 1.27
        elif self.name=="Neptune":
            return 1.638
        else:
            return -1

class Star():
    def __init__ (self, temp):
    	self.temp=temp
    def color(self):
        if self.temp<3700:
            return "red"
        elif self.temp<5200:
               return "orange"
        elif self.temp<6000:
            return "yellow"
        elif self.temp<7500:
            return "yellow white"
        elif self.temp<10000:
            return "white"
        elif self.temp<33000:
            return "blue white"
        else:
            return "blue"
    def classification(self):
        if self.temp<3700:
            return "M"
        elif self.temp<5200:
            return "K"
        elif self.temp<6000:
            return "G"
        elif self.temp<7500:
            return "F"
        elif self.temp<10000:
            return "A"
        elif self.temp<33000:
            return "B"
        else:
            return "O"

class SmallBodies():
    def __init__ (self, kind):
        self.kind=kind
    def avgSize(self):
        if self.kind=="asteroid":
            return "The largest asteroid is about 240km"
        elif self.kind=="comet":
            return "The nucleus of a comet is about 100-200 meters"
        elif self.kind=="meteor":
            return "Meteors can be about 10 meters in diameter"
        else:
            return ""
class Moon(SmallBodies):
    def __init__ (self, name):
        self.name=name
    def planet(self):
        if self.name=="Luna":
            return "Earth"
        elif self.name=="Deimos" or self.name=="Phobos":
            return "Mars"
        elif self.name=="Ganymede" or self.name=="Callisto" or self.name=="Io" or self.name=="Europa":
            return "Jupiter"
        elif (self.name=="Titan" or self.name=="Rhea" or self.name=="Iapetus" or self.name=="Dione" or self.name=="Tethys" or 
            self.name=="Enceladus" or self.name=="Mimas" or self.name=="Hyperion"):
            return "Saturn"
        elif (self.name=="Titania" or self.name=="Oberon" or self.name=="Umbriel" or self.name=="Ariel" or
             self.name=="Miranda"):
            return "Uranus"
        elif (self.name=="Triton" or self.name=="Proteus" or self.name=="Nereid"
             or self.name=="Larissa"):
            return "Neptune"
        elif (self.name=="Charon" or self.name=="Hydra" or self.name=="Nix"
         or self.name=="Kerberos"):
            return "Pluto"
    def distanceToPlanet(self):
        if self.name=="Luna":
            return 238900
        elif self.name=="Deimos":
            return 14573
        elif self.name=="Phobos":
            return 5826
        elif self.name=="Ganymede":
            return 665000
        elif self.name=="Callisto":
            return 1168000
        elif self.name=="Io":
               return 262219
        elif self.name=="Europa":
            return 416940
        elif self.name=="Titan":
            return 759234
        elif self.name=="Rhea":
            return 327500
        elif self.name=="Iapetus":
            return 2213000
        elif self.name=="Dione":
            return 234000
        elif self.name=="Tethys":
            return 183100
        elif self.name=="Enceladus":
            return 147886
        elif self.name=="Mimas":
            return 115280
        elif self.name=="Hyperion":
               return 932637
        elif self.name=="Titania":
            return 271000
        elif self.name=="Oberon":
            return 362880
        elif self.name=="Umbriel":
            return 165000
        elif self.name=="Ariel":
            return 118060
        elif self.name=="Miranda":
            return 80716
        elif self.name=="Triton":
            return 205000
        elif self.name=="Proteus":
            return 57700
        elif self.name=="Nereid":
            return 841100
        elif self.name=="Larissa":
            return 45733
        elif self.name=="Charon":
            return 12200
        elif self.name=="Hydra":
            return 40264
        elif self.name=="Nix":
            return 30260
        elif self.name=="Kerberos":
            return 36660
def main():
	intro= ["Hello! This program gives the user information about a celestial object", "Input a type of object and the program will give you information about it", "(Make inputs lowercase unless it is the name of a planet or moon)", "Do you want information about a planet, star, or object?"]
	for i in range(0, len(intro)):
		print(intro[i])
	choice = input()
	if choice=="planet":
		print("What planet would you like information on")
		planets=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
		for i in range(0, len(planets)):
			print(planets[i])
		newPlanet=Planet(input())
		if newPlanet.distanceFromSun()>10:
			print("The distance to the sun from " + newPlanet.name + " is " + str(newPlanet.distanceFromSun()) + " million miles")
		else:
			print("The distance to the sun from " + newPlanet.name + " is " + str(newPlanet.distanceFromSun()) + "billion miles")	
		print(newPlanet.name + " is a " + newPlanet.type()+ " planet.")
		print(newPlanet.name + " has " + str(newPlanet.numOfMoons())+ " moons.")
		print("The radius of " + newPlanet.name + " is " + str(newPlanet.radius()))
		print("The density of " + newPlanet.name + " is " + str(newPlanet.density()))
	elif choice=="star":
		print("Input the temperature of a star (between 390 and 40000K) you would like information on")
		newStar=Star(int(input()))
		print("The color of the star with the temperature " + str(newStar.temp) + " is " + newStar.color())
		print("The classification of the star with the temperature " + str(newStar.temp) + " is "+ newStar.classification())
	elif choice=="object":
		print("What type of small body would you like information on? (asteroid, meteor, comet, or moon)")
		newObj=SmallBodies(input())
		if newObj.kind=="moon":
			print("Input the name of a moon you would like information on")
			newMoon=Moon(input())
			print(newMoon.name + " is a moon of " + newMoon.planet())
			print(newMoon.name + " is " + str(newMoon.distanceToPlanet()) + " million miles from " + newMoon.planet())
		else:
			print(newObj.avgSize())
	else:
		print("You didn't input a type of celestial object")
		main()

main()


