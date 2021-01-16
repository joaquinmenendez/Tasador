import pickle
import numpy as np

# Load ML model and Scaler
with open('tmp/model.pickle', 'rb') as file:
    model = pickle.load(file)


# Define property
class Property:

    def __init__(self,rooms, bedrooms, bathrooms, surface_total, surface_covered, lat, lon, Departamento = 0, Casa = 0, PH = 0):
        self.rooms = rooms
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.surface_total = surface_total
        self.surface_covered = surface_covered
        self.lat = lat
        self.lon = lon
        self.Departamento = Departamento
        self.Casa = Casa
        self.PH = PH


    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.rooms}, {self.bedrooms}, {self.bathrooms},'
                f'{self.surface_total}, {self.surface_covered},'
                f'{self.lat}, {self.lon},'
                f'{self.Departamento}, {self.Casa}, {self.PH})')


    def predictValue(self, printable=False):
        """
        Returns an estimate price in dollars for the property
        :param printable: Bool - Default: False. Prints a message with the estimated value
        :return: float
        """
        # Create an array with the object attributes
        property_values = [att for att in self.__dict__.values()]
        property_values = np.array(property_values).reshape(1, -1)
        property_values = model["scaler"].transform(property_values)
        price_pred = model["modelo"].predict(property_values)[0]
        if printable:
            print(f'Esta propiedad tiene un valor estimado de: {price_pred:.0f}')
        else:
            return price_pred


if __name__ == "__main__":
    nueva_prop = Property()
    nueva_prop.predictValue(printable=True)
