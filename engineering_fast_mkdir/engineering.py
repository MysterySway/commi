#输入：项目名称、素材文件路径、目标路径、楼号                                     完成
#确认信息                                                                      完成
#在目标路径新建母文件夹                                                         完成
#在素材路径新建楼号文件夹
#在素材文件夹下的特定文件夹内提取照片和视频的修改日期
#命名目标文件夹
#移动照片和视频！！注意是移动
#查重查缺
#输出缺少的文件夹名称
#结束
#os.path.getmtime(file)最近修改时间输出时间戳
#print "time.ctime() : %s" % time.ctime()转化时间戳
#print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 格式化时间


import os
import sys
import time
import shutil


folder_name_main_01 = '01、原貌及拆迁'
folder_name_main_02 = '02、整体外观进展及现场管理'
folder_name_main_03 = '03、基础'
folder_name_main_04 = '04、主体'
folder_name_main_05 = '05、防水、保温、防腐'
folder_name_main_06 = '06、室内管道'
folder_name_main_07 = '07、室外管线'
folder_name_main_08 = '08、电气'
folder_name_main_09 = '09、建筑智能'
folder_name_main_10 = '10、通风与空调'
folder_name_main_11 = '11、消防'
folder_name_main_12 = '12、重大事故'
folder_name_main_13 = '13、开工、封顶、竣工仪式及质检验收等活动'
folder_name_main_14 = '14、竣工面貌'
folder_name_main_15 = '15、内部功能、附属配套、装修及使用情况'


#楼号输入函数
def floor_sub(input_floor,list_floor):
    list_floor = []
    while input_floor != 'pass':
        list_floor.append(input_floor)
        input_floor = input('请继续输入楼号，退出请输入pass：')
    else:
        pass
    return list_floor



project_name    = input('输入项目名称：')
staff = input('输入移交人：')
material_path   = input('输入素材文件夹路径：')
target_path     = input('输入要建立文件夹的目标路径：')
input_floor     = input('输入楼号')

#输入信息函数
def input_information():
    project_name = input('请输入项目名称：')
    staff = input('输入移交人：')
    material_path = input('请输入素材文件夹路径：')
    target_path = input('请输入要建立文件夹的目标路径：')
    input_floor = input('输入楼号：')
    information_list = [project_name,staff,material_path,target_path,input_floor]
    print(information_list)

#楼号函数的调用
list_floor=floor_sub(input_floor,list_floor = [0])

#主体信息的确定
'''
信息集合
information = [project_name,material_path,target_path]+list_floor
print(information)
'''
print('\n请确认信息：')
print('项目名称：' + project_name)
print('移交人：' + staff)
print('素材路径：'+ material_path)
print('目标路径：'+ target_path)
print('楼号：'+ str(list_floor))
infcom = input('\n信息是否正确？Y/N：')
while infcom != 'Y' and 'y':
    input_information()
    list_floor=floor_sub(input_floor,list_floor = [0])
    '''
    信息集合
    information = [project_name,material_path,target_path]+list_floor
    print(information)
    '''
    print('\n请确认信息：')
    print('项目名称：' + project_name)
    print('移交人：' + staff)
    print('素材路径：'+ material_path)
    print('目标路径：'+ target_path)
    print('楼号：'+ str(list_floor))
    infcom = input('\n信息是否正确？Y/N：')
else:
    print('\n信息已确认\n')

#切换文件夹
print('目标路径',target_path,'正在切换工作目录')
os.chdir(target_path)
print('当前工作文件夹',os.getcwd())
print('\n正在准备向目标文件夹中创建主体框架\n')

#要创建的文件夹列表
print('创建工程文件夹')
project_name = project_name +'工程声像档案（移交人：'+ staff +'，移交日期：' +time.strftime('%Y.%m.%d',time.localtime()) +')'              #创建人
os.mkdir(project_name)
target_path_main =target_path +'\\'+ project_name
print('切换目录')
os.chdir(target_path_main)
print('当前工作文件夹',os.getcwd())

print('创建次级文件夹')
folder_name_main_pictur = project_name +'工程照片档案（移交人：'+ staff +'，移交日期：' +time.strftime('%Y.%m.%d',time.localtime()) +')'
folder_name_main_video = project_name +'工程录像档案（移交人：'+ staff +'，移交日期：' +time.strftime('%Y.%m.%d',time.localtime()) +')'
target_path_main_pictur = target_path_main + '\\' + folder_name_main_pictur
target_path_main_video = target_path_main + '\\' + folder_name_main_video
os.mkdir(folder_name_main_pictur)
os.mkdir(folder_name_main_video)
print('当前工作文件夹',os.getcwd())

print('切换目录')
os.chdir(target_path_main_pictur)
print('当前工作文件夹',os.getcwd())
os.mkdir(folder_name_main_01)
os.mkdir(folder_name_main_02)
os.mkdir(folder_name_main_03)
os.mkdir(folder_name_main_04)
os.mkdir(folder_name_main_05)
os.mkdir(folder_name_main_06)
os.mkdir(folder_name_main_07)
os.mkdir(folder_name_main_08)
os.mkdir(folder_name_main_09)
os.mkdir(folder_name_main_10)
os.mkdir(folder_name_main_11)
os.mkdir(folder_name_main_12)
os.mkdir(folder_name_main_13)
os.mkdir(folder_name_main_14)
os.mkdir(folder_name_main_15)

print('切换目录')
os.chdir(target_path_main_video)
print('当前工作文件夹',os.getcwd())
os.mkdir(folder_name_main_01)
os.mkdir(folder_name_main_02)
os.mkdir(folder_name_main_03)
os.mkdir(folder_name_main_04)
os.mkdir(folder_name_main_05)
os.mkdir(folder_name_main_06)
os.mkdir(folder_name_main_07)
os.mkdir(folder_name_main_08)
os.mkdir(folder_name_main_09)
os.mkdir(folder_name_main_10)
os.mkdir(folder_name_main_11)
os.mkdir(folder_name_main_12)
os.mkdir(folder_name_main_13)
os.mkdir(folder_name_main_14)
os.mkdir(folder_name_main_15)

print('创建框架完成')


#素材文件夹操作
os.chdir(material_path)
folder_directory = os.listdir(material_path)

while '录像' and '照片' not in folder_directory:
    print('缺少录像或者照片文件夹')
    os.system('pause')
    folder_directory = os.listdir(material_path)
else:
    print('素材主文件校验成功')

#切换到素材文件夹的子文件夹
folder_name_material_pictur = material_path + '\\' + '照片'
folder_name_material_video = material_path + '\\' + '录像'

#命名文件夹
def material_folder_name(material_path_name,floor_number,parent_directory_path,directory_name):
    date_variable = time.strftime("%Y%m%d",time.gmtime(os.path.getmtime(material_path_name)))
    name_variable = date_variable + '_' + floor_number + '#' + directory_name + '（拍摄人：钟畅）'
    os.chdir(parent_directory_path)
    os.mkdir(name_variable)
    destination_folder_path = parent_directory_path + '\\' + name_variable
    shutil.move(material_path_name,destination_folder_path)
    return destination_folder_path

#为一栋楼挑选文件,存储在素材文件夹下
def pick_file(pick_floor_number,folder_material_path,material_name):
    pick_floor_number_path = material_path + '\\' + pick_floor_number + material_name
    pick_folder_directory = os.listdir(folder_material_path)
    for pick_folder_directory_loop in pick_folder_directory:
        pick_folder_directory_path = folder_material_path + '\\' + pick_folder_directory_loop
        material_path_name_list =  os.listdir(pick_folder_directory_path)
        material_path_name_list_path0 = pick_folder_directory_path + '\\' + material_path_name_list[0]
        pick_destination_folder_path = material_folder_name(material_path_name_list_path0,pick_floor_number,pick_folder_directory_path,pick_folder_directory_loop)
        os.chdir(material_path)
        shutil.move(pick_destination_folder_path,pick_floor_number_path)


#在素材文件夹下创建楼号文件夹
print('创建照片暂存文件夹')
for floor_number_loop_pictur in list_floor:
    material_name = 'pictur'
    pick_file(floor_number_loop_pictur,folder_name_material_pictur,material_name)

print('创建录像暂存文件夹')
for floor_number_loop_video in list_floor:
    material_name = 'video'
    pick_file(floor_number_loop_video,folder_name_material_video,material_name)


#日志文件





#移动编辑好的文件夹
#def move_folder():
