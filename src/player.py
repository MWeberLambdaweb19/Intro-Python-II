# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.current_inventory = None

    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction")

    def inventory(self):
        if self.current_inventory is []:
            print("I have nothing in my inventory")
        else: 
            print(self.inventory)

    def search(self):
        current_room = self.current_room
        room_items = current_room.current_items
        if room_items is None:
            print("There are no items in this room!")
        else: 
            print(f"There are items!"),
            for x in room_items:
                print(type(x))
                print('-', x)

    def take_item(self, item):
        self.current_inventory = []
        self.current_inventory.append(item)
        print(f"I have taken {item}. My inventory is now: {self.current_inventory}")
        