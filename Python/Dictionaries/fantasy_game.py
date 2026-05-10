#####stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(dictionary):
    print("Inventory: ")
    total_item=0
    for k in dictionary.items():
        print(k[1]," : ",k[0])
        total_item+=k[1]
    print("total number of items are :",end="")
    return total_item

#print(display_inventory(stuff))

""""

def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i not in inventory:
            inventory[i]=1
        else:
            inventory[i]+=1
    return inventory

def display_inevntory(inventory):
    print("inventory: ")
    item_total=0

    for k,v in inventory.items():
        item_total+=v
        print(k,":"," ",v)
    print("total items are : ",str(item_total))



inv={'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inevntory(inv)"""

inv={'gold coin':42,'rope':1}
dragon_loot=['gold coin','dagger','gold coin','gold coin','ruby']

def add_to_inventory(inventory,item):
    for i in item:
        if i not in inventory:
            inventory[i]=1
        else:
            inventory[i]+=1
    return inventory
add_to_inventory(inv,dragon_loot)

print(display_inventory(inv))