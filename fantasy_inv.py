# fantasy game inventory from chapter 5
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


# takes a dictionary and formats and displays it as inventory in a game
def display_inventory(dict):
    print("Inventory:")
    x = 0
    for key in dict.keys():
        print(dict[key], key)
        x = x + dict[key]
    print("Total number of items:", x)
