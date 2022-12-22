import services

class User :

    def __init__(self,firstname,lastname,weight,height,gender):
        self.firstname = firstname
        self.lastname = lastname
        self.weight = weight
        self.height = height
        self.gender = gender

    
    def __str__(self):
            return f"{self.firstname}\n{self.lastname}\n{self.weight}\n{self.height}\n{self.gender}"
        
    def GetListFood(self):
        """Get all food in FoodDb
        """
        file = services.GetPath("FoodDb","r")
            
        lines = file.readlines()
        
        for l in lines:
            print(l)
        
        file.close()

    def HistoricFood(self):
        # TODO A REGARDER
        
        file = self.GetPath("HistoricFoodUser","a") 
        

    def AddFood(self,food):
        """_summary_

        Args:
            food (Food): Add an element(food) to FoodDb
        """
        file = services.GetPath("FoodDb","a")
        file.write(f"{food} \n")

        file.close()
        
class Food:
    def __init__(self,name,weight,kcal,carbohydrate,lipid,protein):
        self.name = name
        self.weight = weight
        self.kcal = kcal
        self.carbohydrate = carbohydrate
        self.lipid = lipid
        self.protein = protein
        self.iron = None
        self.magnesium = None
        self.calcium = None
        
    def __str__(self):
        return f"{self.name},{self.weight},{self.kcal},{self.carbohydrate},{self.lipid},{self.protein},{self.iron},{self.magnesium},{self.calcium}"
        
user = User("quentin","fzd","z","z","e")
food = Food("Carrot","150","35","65","55","6")
food1 = Food("poireau","520","375","675","755","76")
user.AddFood(food)
user.AddFood(food1)

user.GetListFood()

