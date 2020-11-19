import pickle
import numpy as np

# Load ML model
with open('knn_model.pkl','rb') as file:
    model = pickle.load(file)

# Define property
class Property:

    def __init__(self):
        # To make the instantiation more interactive we will use `input`
        self.rooms = int(input("Rooms: "))
        self.bedrooms = int(input("Bedrooms: "))
        self.bathrooms = int(input("Bathrooms: "))
        self.surface_total = int(input("Surface Total (m2): "))
        self.surface_covered = int(input("Surface Covered (m2): "))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.rooms}, {self.bedrooms}, {self.bathrooms},'
                f' {self.surface_total}, {self.surface_covered})')

    def predictValue(self, printable = False):
        '''
        Returns an estimate price in dollars for the property
        :param printable: Bool - Default: False
        :return: float
        '''
        # Create an array with the object attributes
        property_values = [att for att in self.__dict__.values()]
        property_values = np.array(property_values).reshape(1, -1)
        # Feed the array to our model
        price_pred = model.predict(property_values)
        if printable:
            print('Esta propiedad tiene un valor estimado de: {price_pred:.0f}')
        else:
            return price_pred