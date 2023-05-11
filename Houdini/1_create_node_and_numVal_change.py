import hou

# getting the obj context
obj = hou.node("/obj")

# create geo node in /obj
myGeo = obj.createNode('geo' ,'myGeo')

# create box inside of myGeo
box = myGeo.createNode('box', 'myBox')

# create var to use
height = 1
width = 3
depth = 2

# assign var to box parameters
box.parm('sizex').set(width)
box.parm('sizey').set(height)
box.parm('sizez').set(depth)

# assign an expression to the box parameter
# center
box.parm('ty').set(height/2)

