from interface import IBuildings
import copy
class ResidentialBuilding(IBuildings):

    """Жилой дом

    Args:
        IBuildings (_type_): _description_
    """

    def copy(self):
        return copy.deepcopy(self)
    

