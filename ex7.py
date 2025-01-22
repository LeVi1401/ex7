import csv
import os
from token import STRING

# Global BST root
ownerRoot = None

########################
# 0) Read from CSV -> HOENN_DATA
########################


def read_hoenn_csv(filename):
    """
    Reads 'hoenn_pokedex.csv' and returns a list of dicts:
      [ { "ID": int, "Name": str, "Type": str, "HP": int,
          "Attack": int, "Can Evolve": "TRUE"/"FALSE" },
        ... ]
    """
    data_list = []
    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',')  # Use comma as the delimiter
        first_row = True
        for row in reader:
            # It's the header row (like ID,Name,Type,HP,Attack,Can Evolve), skip it
            if first_row:
                first_row = False
                continue

            # row => [ID, Name, Type, HP, Attack, Can Evolve]
            if not row or not row[0].strip():
                break  # Empty or invalid row => stop
            d = {
                "ID": int(row[0]),
                "Name": str(row[1]),
                "Type": str(row[2]),
                "HP": int(row[3]),
                "Attack": int(row[4]),
                "Can Evolve": str(row[5]).upper()
            }
            data_list.append(d)
    return data_list


HOENN_DATA = read_hoenn_csv("hoenn_pokedex.csv")

########################
# 1) Helper Functions
########################

def read_int_safe(prompt):
    """
    Prompt the user for an integer, re-prompting on invalid input.
    """
    x = input(prompt)
    while not x.isdigit():
        x = input("input is invalid " + prompt)
    return (int)(x)
    pass

def get_poke_dict_by_id(poke_id):
    """
    Return a copy of the Pokemon dict from HOENN_DATA by ID, or None if not found.
    """
    for pokemon in HOENN_DATA:
        if pokemon['ID'] == poke_id:
            return pokemon
    return None
    pass

def get_poke_dict_by_name(name):
    """
    Return a copy of the Pokemon dict from HOENN_DATA by name, or None if not found.
    """
    for pokemon in HOENN_DATA:
        if pokemon['Name'] == name:
            return pokemon
    return None

    pass

def display_pokemon_list(poke_list):
    """
    Display a list of Pokemon dicts, or a message if empty.
    """
    flag = False
    for pokemon in poke_list:
        flag = True
        print(pokemon)
    if not flag:
        print("There are no Pokemons in this Pokedex that match the criteria.")
    pass


########################
# 2) BST (By Owner Name)
########################

def create_owner_node(owner_name, first_pokemon=None):
    """
    Create and return a BST node dict with keys: 'owner', 'pokedex', 'left', 'right'.
    """
    pokedex = [first_pokemon] if first_pokemon is not None else []
    owner = {
        "owner": owner_name,
        "pokedex": pokedex,
        "left": None,
        "right": None,
    }
    print("New Pokedex created for " + owner_name + " with starter " + first_pokemon["Name"] + '.')
    return owner
    pass

def insert_owner_bst(root, new_node):
    """
    Insert a new BST node by owner_name (alphabetically). Return updated root.
    """
    if root is None:
        return new_node
    if new_node is None:
        return root
    if new_node['owner'].lower() < root['owner'].lower():
        if root['left'] is None:
            root['left'] = new_node
            return root
        root["left"] = insert_owner_bst(root["left"], new_node)
    elif new_node['owner'].lower() > root['owner'].lower():
        if root['right'] is None:
            root['right'] = new_node
            return root
        root["right"] = insert_owner_bst(root["right"], new_node)


    pass

def find_owner_bst(root, owner_name):
    """
    Locate a BST node by owner_name. Return that node or None if missing.
    """
    if root is None:
        return None
    if root["owner"].lower() == owner_name.lower():
        return root
    left = find_owner_bst(root["left"], owner_name)
    right = find_owner_bst(root["right"], owner_name)
    if not left is None:
        return left
    elif not right is None:
        return right
    return None
    pass

def min_node(node):
    """
    Return the leftmost node in a BST subtree.
    """
    if node["left"] is None:
        return node
    else:
        return min_node(node["left"])
    pass

def delete_owner_bst(root, owner_name):
    """
    Remove a node from the BST by owner_name. Return updated root.
    """
    pass


########################
# 3) BST Traversals
########################

def bfs_traversal(root):
    """
    BFS level-order traversal. Print each owner's name and # of pokemons.
    """
    pass

def pre_order(root):
    """
    Pre-order traversal (root -> left -> right). Print data for each node.
    """
    pass

def in_order(root):
    """
    In-order traversal (left -> root -> right). Print data for each node.
    """
    pass

def post_order(root):
    """
    Post-order traversal (left -> right -> root). Print data for each node.
    """
    pass


########################
# 4) Pokedex Operations
########################

def add_pokemon_to_owner(owner_node):
    """
    Prompt user for a Pokemon ID, find the data, and add to this owner's pokedex if not duplicate.
    """
    id = read_int_safe("Enter Pokemon ID to add: ")
    for pokemon in owner_node["pokedex"]:
        if pokemon['ID'] == id:
            print("Pokemon already in the list. No changes made.")
            return
    new_pokemon = get_poke_dict_by_id(id)
    owner_node["pokedex"].append(new_pokemon)
    print("Pokemon " + new_pokemon["Name"] + " (ID " + str(id) + ") added to " + owner_node["owner"] + "'s Pokedex.")
    pass

def release_pokemon_by_name(owner_node):
    """
    Prompt user for a Pokemon name, remove it from this owner's pokedex if found.
    """
    pass

def evolve_pokemon_by_name(owner_node):
    """
    Evolve a Pokemon by name:
    1) Check if it can evolve
    2) Remove old
    3) Insert new
    4) If new is a duplicate, remove it immediately
    """
    pass


########################
# 5) Sorting Owners by # of Pokemon
########################

def gather_all_owners(root, arr):
    """
    Collect all BST nodes into a list (arr).
    """
    pass

def sort_owners_by_num_pokemon():
    """
    Gather owners, sort them by (#pokedex size, then alpha), print results.
    """
    pass


########################
# 6) Print All
########################

def print_all_owners():
    """
    Let user pick BFS, Pre, In, or Post. Print each owner's data/pokedex accordingly.
    """
    pre_order_print(ownerRoot)
    pass

def pre_order_print(node):
    """
    Helper to print data in pre-order.
    """
    if node is None:
        return
    print(node["owner"])
    pre_order_print(node["left"])
    pre_order_print(node["right"])
    pass

def in_order_print(node):
    """
    Helper to print data in in-order.
    """
    pass

def post_order_print(node):
    """
    Helper to print data in post-order.
    """
    pass


########################
# 7) The Display Filter Sub-Menu
########################

def display_filter_sub_menu(owner_node):
    """
    1) Only type X
    2) Only evolvable
    3) Only Attack above
    4) Only HP above
    5) Only name starts with
    6) All
    7) Back
    """

    print("-- Display Filter Menu --\n"
        "1. Only a certain Type\n"
        "2. Only Evolvable\n"
        "3. Only Attack above __\n"
        "4. Only HP above __\n"
        "5. Only names starting with letter(s)\n"
        "6. All of them!\n"
        "7. Back")
    choice = read_int_safe("Your choice: ")
    while choice != 7:
        if choice == 1:
            type = str(input("Which Type? (e.g. GRASS, WATER): "))
            display_pokemon_list([pokemon for pokemon in owner_node["pokedex"] if pokemon["Type"].lower() == type.lower()])
        if choice == 2:
            display_pokemon_list([pokemon for pokemon in owner_node["pokedex"] if pokemon["Can Evolve"].upper() == "TRUE"])
        if choice == 3:
            attack = read_int_safe("Enter Attack threshold: ")
            display_pokemon_list([pokemon for pokemon in owner_node["pokedex"] if pokemon["Attack"] > attack])
        if choice == 4:
            hp = read_int_safe("Enter HP threshold: ")
            display_pokemon_list([pokemon for pokemon in owner_node["pokedex"] if pokemon["HP"] > hp])
        if choice == 5:
            letters = str(input("Starting letter(s): "))
            display_pokemon_list([pokemon for pokemon in owner_node["pokedex"] if pokemon["Name"].lower()[:len(letters)] == letters.lower()[:len(letters)]])
        if choice == 6:
            display_pokemon_list(owner_node["pokedex"])

        if choice > 7 or choice <= 0:
            print("Invalid choice. Please try again.")
        print("-- Display Filter Menu --\n"
              "1. Only a certain Type\n"
              "2. Only Evolvable\n"
              "3. Only Attack above __\n"
              "4. Only HP above __\n"
              "5. Only names starting with letter(s)\n"
              "6. All of them!\n"
              "7. Back")
        choice = read_int_safe("Your choice: ")
    pass


########################
# 8) Sub-menu & Main menu
########################

def existing_pokedex():
    """
    Ask user for an owner name, locate the BST node, then show sub-menu:
    - Add Pokemon
    - Display (Filter)
    - Release
    - Evolve
    - Back
    """
    name = str(input("Owner name: "))
    if not find_owner_bst(ownerRoot, name):
        print("Owner '" + name + "' not found.")
        return
    owner = find_owner_bst(ownerRoot, name)
    print("-- " + name + "'s Pokedex Menu --\n"
        "1. Add Pokemon\n"
        "2. Display Pokedex\n"
        "3. Release Pokemon\n"
        "4. Evolve Pokemon\n"
        "5. Back to Main\n")
    choice = read_int_safe("Your choice: ")
    while choice != 5:
        if choice == 1:
            add_pokemon_to_owner(owner)
        if choice == 2:
            display_filter_sub_menu(owner)


        if choice > 5 or choice <= 0:
            print("Invalid choice. Please try again.")
        print("-- " + name + "'s Pokedex Menu --\n"
            "1. Add Pokemon\n"
            "2. Display Pokedex\n"
            "3. Release Pokemon\n"
            "4. Evolve Pokemon\n"
            "5. Back to Main\n")
        choice = read_int_safe("Your choice: ")

    pass

def main_menu():
    """
    Main menu for:
    1) New Pokedex
    2) Existing Pokedex
    3) Delete a Pokedex
    4) Sort owners
    5) Print all
    6) Exit
    """
    print("=== Main Menu ===\n"
        "1. New Pokedex\n"
        "2. Existing Pokedex\n"
        "3. Delete a Pokedex\n"
        "4. Display owners by number of Pokemon\n"
        "5. Print All\n"
        "6. Exit")
    pass

def main():
    global ownerRoot
    main_menu()
    choice = read_int_safe("Your choice: ")
    while (choice != "6"):
        if choice == 1:
            name = str(input("Owner name: "))
            if find_owner_bst(ownerRoot, name):
                print("Owner '" + name + "' already exists. No new Pokedex created.")
            else:
                print("Choose your starter Pokemon:\n"
                    "1) Treecko\n"
                    "2) Torchic\n"
                    "3) Mudkip")
                starter = read_int_safe("Your choice: ")
                if starter == 2:
                    starter = 4
                elif starter == 3:
                    starter = 7
                starter = get_poke_dict_by_id(starter)
                owner = create_owner_node(name, starter)
                ownerRoot = insert_owner_bst(ownerRoot, owner)
        if choice == 2:
            existing_pokedex()


        if choice > 6 or choice <= 0:
            print("Invalid choice. Please try again.")
        main_menu()
        choice = read_int_safe("Your choice: ")
    """
    Entry point: calls main_menu().
    """
    pass

if __name__ == "__main__":
    main()
