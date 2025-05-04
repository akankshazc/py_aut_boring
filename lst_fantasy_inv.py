# list to dict function for fantasy game inventory in chapter 5
import fantasy_inv

# current inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# items to be added as a list
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


# function takes current inventory and items to be added and updates the dict
def add_to_inventory(inventory_dict, added_items_lst):
    for x in added_items_lst:
        if x not in inventory_dict.keys():                  # if item isn't present in dict, create a new item
            inventory_dict[x] = 1
        else:
            inventory_dict[x] += 1
    # return the updated dict
    return inventory_dict


inv = add_to_inventory(stuff, dragonLoot)

fantasy_inv.display_inventory(inv)
