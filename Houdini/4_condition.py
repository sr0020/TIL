import hou

# got selected objects
selected_nodes = hou.selectedNodes()
selected_nodes = list(selected_nodes)

if len(selected_nodes) > 0:
    print(f"Selected nodes: {selected_nodes}")
else:
    print('No nodes selected')
    
    