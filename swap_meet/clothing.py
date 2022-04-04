class Clothing:
    def __init__(self, category = "Clothing", condition = 0):
        self.condition = condition
        self.category = category

    def __str__(self):
        return "The finest clothing you could wear."

    def condition_description(self):
        if self.condition == 0.0:
            return "Poor"
        elif self.condition == 1.0:
            return "Acceptable"
        elif self.condition == 2.0:
            return "Good" 
        elif self.condition == 3.0:
            return "Very Good" 
        elif self.condition == 4.0:
            return "Like New" 
        elif self.condition == 5.0:
            return "Brand New" 