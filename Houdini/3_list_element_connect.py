import hou

# got selected objects
selected = hou.selectedNodes()

# convert to list
selected_list = list(selected)

# set input
# connect select_list[0], select_list[1]
selected_list[0].setInput(0, selected_list[1], 0) # connect select_list[0], select_list[1]
selected_list[1].setInput(0, selected_list[2], 0)

print(selected_list)