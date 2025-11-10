class Vehicule:
    def __init__(self,marque,annee,kilometrage,numero_serie):
        self._marque=marque
        self.__annee=annee
        self.kilometrage=kilometrage
        self.numero_serie=numero_serie
    @property
    def annee(self):
        return self.__annee
    
    @annee.setter
    def annee(self,nouvel_val):
        self.__annee=nouvel_val

    def __str__(self):
        return f"les informations du véhicule sont {self._marque} et {self.__annee}"
class Voiture(Vehicule):
    def __init__(self, marque, annee, kilometrage, numero_serie,color,prix):
        super().__init__(marque, annee, kilometrage, numero_serie)
        self.prix=prix
        self.color=color
    def __str__(self):
        return f"les informations du voiture sont {self.prix} et {self.color}"
v=Vehicule("Toyota",2023,20000,"240TU2765")

voiture=Voiture("Toyota",2025,40000,"210TU2765","rouge",10000)
print(voiture.__class__)
print(voiture)
print(v)
print(v.__dict__)
v.annee=20
print(v._marque)
print(v._Vehicule__annee)
