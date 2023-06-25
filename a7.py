def ds(roll_no, name):
    # Add parameters to a list
    my_list = []
    my_list.append(roll_no)
    my_list.append(name)
    print("List:", my_list)

    # Add parameters to a tuple
    my_tuple = (roll_no, name)
    print("Tuple:", my_tuple)

    # Add parameters to a set
    my_set = set()
    my_set.add(roll_no)
    my_set.add(name)
    print("Set:", my_set)

    # Add parameters to a dictionary
    my_dict = {}
    my_dict['Roll No'] = roll_no
    my_dict['Name'] = name
    print("Dictionary:", my_dict)

    # Change values during runtime
    roll_no_new = input("Enter new Roll No: ")
    name_new = input("Enter new Name: ")
    my_list[0] = roll_no_new
    my_list[1] = name_new
    my_tuple = (roll_no_new, name_new)
    my_set.remove(roll_no)
    my_set.add(roll_no_new)
    my_set.remove(name)
    my_set.add(name_new)
    my_dict['Roll No'] = roll_no_new
    my_dict['Name'] = name_new

    # Delete data structures
    del my_list
    del my_tuple
    del my_set
    del my_dict