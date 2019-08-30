checklist = list()
# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

# List
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        # print(str(index) + list_item)
        index += 1

def mark_completed(index):
    print("√" + str(checklist[index]))

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def select(function_code):
    function_code = function_code.upper()

    try:

        if function_code == "C":
            input_item = user_input("Input item:")
            create(input_item)
        elif function_code == "R":
            item_index = user_input("Index Number?")
            read((int)(item_index))
        elif function_code == "P":
            list_all_items()
        elif function_code == "U":
            item_index = user_input ("Index Number?")
            item = user_input("Item")
            update((int)(item_index), item)
        elif function_code == "D":
            index = user_input("Index Number?")
            destroy((int)(index))
        elif function_code == "Q":
            return False

        else:
            print("Unknown Option")
        return True

    except IndexError:
        print("\033[1;32;40m Invalid User Index \x1b[0m")

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))
    list_all_items()
    mark_completed(0)
    select("C")

    user_value = user_input("Please Enter a value:")
    print(user_value)

test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)
