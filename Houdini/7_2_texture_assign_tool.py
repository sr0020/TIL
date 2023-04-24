# 실습
# Assign Texture

import PySide2 as ps
import hou
import os

# apply_textures
def apply_textures(path, material):
    files = os.listdir(path)
    for image in files:
        if 'test.jpg' in image:
        # change to material paramter as True
            material.parm('metallic_useTexture').set(True)
            material.parm('metallic_texture').set(path + image)
            
            material.parm('baseBumpAndNormal_enable').set(True)
            material.parm('baseNormal_texture').set(path + image)
            material.parm('baseNormal_scale').set(-.01)
            
            material.parm('dispTex_enable').set(True)
            material.parm('dispTex_texture').set(path + image)
            material.parm('dispTex_scale').set(.05)
            
def QtMainWindow():
    return hou.qt.mainWindow()
    
class Texture(ps.QtWidgets.QDialog):

    # 기본 pyside UI setting 
    def __init__(self, parent=QtMainWindow()):
        super(Texture, self).__init__(parent)
    
        # 기본 window UI setting
        self.setWindowTitle("Apply Texture Window")
        self.setMinimumSize(300, 80)
        self.setWindowFlags(self.windowFlags() ^ ps.QtCore.Qt.WindowContextHelpButtonHint) # 도움말 표시 삭제 
        
        # window element creation
        self.CreateWidgets() # widget
        self.CreateLayouts() # widget Layout
        self.CreateConnection() # UI + hou module
        
    def CreateWidgets(self):
        self.texturePathLineEdit = ps.QtWidgets.QLineEdit()
        self.texturePathButton = hou.qt.FileChooserButton()
        self.textureButton = ps.QtWidgets.QPushButton('Assign Texture')
        
        # texturePathButton properties
        self.texturePathButton.setFileChooserTitle('Select a directory contain your texture')
        self.texturePathButton.setFileChooserMode(hou.fileChooserMode.Read)
        self.texturePathButton.setFileChooserFilter(hou.fileType.Directory)
        
    def CreateLayouts(self):
            
        # directory path (line, button)
        directoryPathLayout = ps.QtWidgets.QHBoxLayout()
        directoryPathLayout.addWidget(self.texturePathLineEdit)
        directoryPathLayout.addWidget(self.texturePathButton)
        
        createAgentLayout = ps.QtWidgets.QHBoxLayout()
        createAgentLayout.addWidget(self.textureButton)
        
        formLayout = ps.QtWidgets.QFormLayout()
        formLayout.addRow('Folder Path: ', directoryPathLayout)
        formLayout.addRow(createAgentLayout)
        
        mainLayout = ps.QtWidgets.QVBoxLayout(self) 
        mainLayout.addLayout(formLayout) 
    
    def CreateConnection(self):
        self.texturePathButton.fileSelected.connect(self.setTexturePathLineEditText)
        self.textureButton.clicked.connect(self.assignTexture)
       
    def setTexturePathLineEditText(self, file_path):
        self.texturePathLineEdit.setText(file_path)
       
    def assignTexture(self):
        material = hou.selectedNodes()[0]
        path = self.texturePathLineEdit.text()
        apply_textures(path, material)
        
try:
    Texture.close()
    Texture.deleteLater()
except:
    pass
    
# call qt
Texture = Texture()
Texture.show()

print('DONE')