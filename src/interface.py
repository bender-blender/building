
class IBuildings:
    """Здание
    """
    def __init__(self,name:str,size_x:int,size_y:int,room:int,color:str):
        self.name = name
        self.size_x = size_x
        self.size_y = size_y
        self.room = room
        self.color = color
        
    def copy(self):
        raise NotImplementedError
    

    def __str__(self) -> str:
        return f"{self.name}\nРазмер:{self.size_x}x{self.size_y}\nКомнаты:{self.room}\nЦвет:{self.color}"
