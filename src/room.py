# Implement a class to hold room information. This should have name and
# description attributes.

class Room: 
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.current_items = []

    def add_items(self, *item):
        self.current_items = []
        self.current_items.append(item)
        
    def __str__(self):
        return f"{self.title}\n\n{self.description}"

class Treasure(Room):
    def __init__(self,  title, description, items):
        super().__init__(title, description)
        self.items = items
    def __str__(self):
        return f"There are {self.items} in {self.title}"