
class CelestialObject {

	public:

		CelestialObject(string name);
		~CelestialObject();
		string[] composition(); //returns composition of object
double radius(); //returns average radius
double density(); //returns average density

};

class Planet:CelestialObject{

	public:
		Planet(string name);
		~Planet();
		double distanceFromSun(); //returns the distance from the sun in AU
		string type(); //returns terrestrial, gas giant, or dwarf
		int numberOfMoons(); //returns the number of moons the planet has
};

class Star:CelestialObject{

	public:

		Star(double temp, double luminosity);
		~Star();
string type(); //returns type of star (white dwarf, main sequence, etc.)
		string color(); //returns color
		string classification(); //returns classification of star
		double lifetime(); //returns the lifetime of the star
};

class SmallBodies(){

	public:

		SmallBodies(string type); //inputs a small body (asteroid, comet, moon, etc.)
		~SmallBodies();
		double avgSize(); //returns average size of the small body
		string[] composition(); //returns the composition of the small body


class Moon(){

public:

	Moon(name);
	~Moon();
	string planet(); //returns planet the moon orbits
	double distanceToSun(); //returns the distance to the sun
	};


};

