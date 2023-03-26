import hou
import os

def apply_textures(path, material):
    # show files in path
    files = os.listdir(path) 
    for image in files:
        if 'test.jpg' in image:
            material.parm('metallic_useTexture').set(True)
            material.parm('metallic_texture').set(path + os.sep + image)
     
            material.parm('baseBumpAndNormal_enable').set(True)
            material.parm('baseNormal_texture').set(path + os.sep + image)
            material.parm('baseNormal_scale').set(-.01)
            
            material.parm('dispTex_enable').set(True)
            material.parm('dispTex_texture').set(path + os.sep + image)
            material.parm('dispTex_scale').set(.05)

material = hou.selectedNodes()[0]
path = (r'C:\Users\JMJS\Desktop\y_test')
apply_textures(path, material)
