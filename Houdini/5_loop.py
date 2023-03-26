import hou

# get selection
selection = hou.selectedNodes()

x = 0

for node in selection:
    node.parm('tx').set(x)
    node.parm('ty').set(0)
    node.parm('tz').set(0)
    
    x += 10
    