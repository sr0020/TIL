# unreal python script 실습

# from importlib import reload
# import tutorial_script as TS
# reload(TS)

import unreal

# asset path
def listAssetPaths():
    EAL = unreal.EditorAssetLibrary

    assetPaths = EAL.list_assets('/Game')

    for assetPath in assetPaths:
        print(assetPath)

# 선택한 asset 콘솔창에 띄우기
def getSelectionContentsBrower():
    EUL = unreal.EditorUtilityLibrary
    selectedAssets = EUL.get_selected_assets()

    for selectedAsset in selectedAssets:
        print(selectedAsset)

# obj 가져오기
def getAllActors():
    EAS = unreal.EditorLevelLibrary
    actors = EAS.get_all_level_actors()

    for actor in actors:
        print(actor)

# 에셋 클래스 검색
def getAssetClass(classType):

    EAL = unreal.EditorAssetLibrary
    assetPaths = EAL.list_assets('/Game')
    
    assets = []

    for assetPath in assetPaths:
        assetData = EAL.find_asset_data(assetPath)
        # print(assetData) # get asset name, class, path

        assetClass = assetData.asset_class
        if assetClass == classType:
            # print(assetClass) # get every single obj's class
            assets.append(assetData.get_asset())

    for asset in assets: print(asset)
    return assets

# 에디터 프로퍼티로 작업하기
def getStaticMeshData():
    staticMeshes = getAssetClass('StaticMesh')

    for staticMesh in staticMeshes:
        # assetImportData = staticMesh.get_editor_property('asset_import_data')
        # # print(assetImportData) # asset obj property (class) 출력
        # fbxFilePath = assetImportData.extract_filenames()
        # print(fbxFilePath) # 특정 확장자를 가진 파일들 경로와 함께 출력

        lod_group = staticMesh.get_editor_property('lod_group')
        # print(lod_group)

        if lod_group == 'None':

            # print(staticMesh.get_name())
            # print(staticMesh.get_num_lods())

            if staticMesh.get_num_lods() == 1:
                staticMesh.set_editor_property('lod_group', 'LargeProp')

# staticMesh의 상세정보 수집
# 긱 staticMesh 별 (vertices, triangles, normals, u_vs, tangents)
def getStaticMeshLODData():

    PML = unreal.ProceduralMeshLibrary

    staticMeshes = getAssetClass('StaticMesh')

    staticMeshLODData = []

# 각 staticmesh의 triangle 갯수
    for staticMesh in staticMeshes:

        staticMeshTriCount = []
        # if staticMesh.get_name() =='Shape_Sphere':

        numLODs = staticMesh.get_num_lods()

        for i in range(numLODs):
            numSections = staticMesh.get_num_sections(i)
            LODTriCount = 0
            # print(numSections)

            for j in range(numSections):
                sectionData = PML.get_section_from_static_mesh(staticMesh, i, j)
                
                # for item in sectionData[0]: print(item)
                # print(len(sectionData[1])) # 인덱스 넘버 == return value (vertices, triangles, normals, u_vs, tangents)

                # for item in sectionData[1]:
                #     print(item)

                sectionTriCount = (len(sectionData[1]) / 3)     
                LODTriCount += sectionTriCount

            staticMeshTriCount.append(LODTriCount)

        staticMeshReductions = [100]

        for i in range(1, len(staticMeshTriCount)):
            staticMeshReductions.append(int(staticMeshTriCount[i] / staticMeshTriCount[0] * 100))

        # print(staticMesh.get_name())
        # print(staticMeshTriCount)
        # print(staticMeshReductions)
        # print('------')

        try:
            LODData = (staticMesh.get_name(), staticMeshTriCount[1])
            # print('LODData\n')
            # print(LODData) # type: tuple
        except:
            pass
        staticMeshLODData.append(LODData)

    # print(staticMeshLODData)
    return staticMeshLODData

# StaticMesh의 Instance 갯수 conut
# num of triangle in >> staticMeshTriCount[1] (LOD[1]의 삼각형 갯수 반환함. (전체 staticMesh의))
def getStaticMeshInstanceCounts():
    levelActors = unreal.EditorLevelLibrary().get_all_level_actors()

    staticMeshActors = []
    staticMeshActorCounts = []
    
    for levelActor in levelActors:
        if(levelActor.get_class().get_name()) == 'StaticMeshActor':
            staticMeshComponent = levelActor.static_mesh_component
            staticMesh = staticMeshComponent.static_mesh
            staticMeshActors.append(staticMesh.get_name())

    processedActors = []
    for staticMeshActor in staticMeshActors:
        if staticMeshActor not in processedActors:
            actorCounts = (staticMeshActor, staticMeshActors.count(staticMeshActor))
            staticMeshActorCounts.append(actorCounts)
            processedActors.append(staticMeshActor)

    staticMeshActorCounts.sort(key=lambda a:a[1], reverse=True)

    # for item in staticMeshActorCounts:
    #     print(item)

    LODData = getStaticMeshLODData() 
    # print(type(LODData))

    # for item in LODData:
    #     print(item)

    aggregateTriCounts = []

    for i in range(len(staticMeshActorCounts)):
        for j in range(len(LODData)):
            if staticMeshActorCounts[i][0] == LODData[j][0]: # iteration over everything in staticMeshActorCounts and LODData
                aggregateTriCount = (staticMeshActorCounts[i][0], staticMeshActorCounts[i][1] * LODData[j][1]) 
                aggregateTriCounts.append(aggregateTriCount)

    aggregateTriCounts.sort(key=lambda a:a[1], reverse=True)

    # print overall aggregate triangle for its LOD
    # 각 메시 안에 있는 전체 triangle 갯수를 반환 (ex sphere가 3개인 경우 각 sphere별 triangle 갯수인 480 * 3 = 1440개 (LOD 0 기준))
    for item in aggregateTriCounts:
        print(item)

# unreal.InstancedStaticMeshComponent의 전체 메서드 출력
# for item in dir(unreal.InstancedStaticMeshComponent): print(item)

# help(unreal.StaticMeshComponent.get_materials)
# 해당 함수는 실행인자 필요없고, 머터리얼 인터페이스 오브젝트의 배열을 반환함
# LogPython: help(unreal.StaticMeshComponent.get_materials)
# LogPython: Help on methodwithclosure_descriptor:
# get_materials(...)
#     x.get_materials() -> Array(MaterialInterface) # 실행인자 필요없음
#     Get Materials
    
#     Returns:
#         Array(MaterialInterface):

# help(unreal.StaticMeshComponent.set_material)
# element_index, material 매개변수로 필요함.
# LogPython: help(unreal.StaticMeshComponent.set_material)
# LogPython: Help on methodwithclosure_descriptor:
# set_material(...)
#     x.set_material(element_index, material) -> None
#     Changes the material applied to an element of the mesh.
    
#     Args:
#         element_index (int32): The element to access the material of.
#         material (MaterialInterface):

# LogPython: help(unreal.StaticMeshComponent.get_num_materials)
# LogPython: Help on methodwithclosure_descriptor:
# get_num_materials(...)
#     x.get_num_materials() -> int32
#     Return number of material elements in this primitive
    
#     Returns:
#         int32:

def returnMaterialInformationSMC():

    levelActors = unreal.EditorLevelLibrary().get_all_level_actors()

    testMat = unreal.EditorAssetLibrary.find_asset_data('/Game/StarterContent/python/MI_test_2').get_asset()

    for levelActor in levelActors:
        if(levelActor.get_class().get_name()) == 'StaticMeshActor':
            staticMeshComponent = levelActor.static_mesh_component

            # print(levelActor.get_name())
            # materials = staticMeshComponent.get_materials()

            # for material in materials:
            #     print(material.get_name())

            #     try:
            #         for item in material.texture_parameter_values:
            #             print(item)
            #     except:
            #         pass
            #     print('___')

            # 레벨에 있는 모든 staticMeshActor의 엘리먼트를 지정한 material로 설정
            for i in range(staticMeshComponent.get_num_materials()):
                staticMeshComponent.set_material(i, testMat)