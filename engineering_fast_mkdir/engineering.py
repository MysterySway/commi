#输入：项目名称、素材文件路径、目标路径、楼号                                     完成
#确认信息                                                                      完成
#在目标路径新建母文件夹
#在目标路径新建楼号文件夹
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
material_path   = input('输入素材文件夹路径：')
target_path     = input('输入要建立文件夹的目标路径：')
input_floor     = input('输入楼号')

#输入信息函数
def input_information():
    project_name    = input('请输入项目名称：')
    material_path   = input('请输入素材文件夹路径：')
    target_path     = input('请输入要建立文件夹的目标路径：')
    input_floor           = input('输入楼号')


#楼号函数的调用
list_floor=floor_sub(input_floor,list_floor = [0])

#主体信息的确定
information = [project_name,material_path,target_path]+list_floor
print(information)
infcom = input('信息是否正确？Y/N：')
while infcom == 'N':
    input_information()
    list_floor=floor_sub(input_floor,list_floor = [0])
    information = [project_name,material_path,target_path]+list_floor
    print(information)
    infcom = input('信息是否正确？Y/N：')
else:
    print('信息确认')

#切换文件夹
print('目标路径',target_path,'正在切换工作目录')
os.chdir(target_path)
retval = os.getcwd()
print('当前工作文件夹',retval)
print('正在准备向目标文件夹中创建主体框架')

#要创建的文件夹列表
project_name = project_name +'创建人:'              #创建人
os.mkdir(project_name)





print('创建框架完成')
print('正在准备在文件夹中创建楼号')