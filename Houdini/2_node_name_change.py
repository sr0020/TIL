import hou

# get the currently selected node
node = hou.selectedNodes()[0]

# get the name of selected node
name = node.name()

# with prefix
prefix = 'Out_'

fullName = f'{prefix}{name}' # f'{var_name}'
upper_name = fullName.upper()

node.setName(upper_name) 

print(name)