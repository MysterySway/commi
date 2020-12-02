@echo off       #关闭文件整体回显
@               #关闭本行命令回显
call 文件名 %1 %2    #再不终止父文件的情况下调用另一个批处理文件，并且传递参数
pause               #暂停执行批处理文件并挂起，知道按下按键
rem             #注释
goto lable      #跳转到指定标签

    if {%1} == goto noparms
    if {%2} == goto noparms
    @rem check parameters if null show usage
    :noparms
    echo usage:monitor,bat serverip portnumber
    goto end

if [not] errorlevel number command [else expression]        #前一个程序输出大于等于number的退出码时为真
if [not] string1==string2 commandd [else expression]        #数值相同为真
if [not] exist filename command [else expression]           #文件存在则为真

choice [/c[choices]][/n][/cs][/t timeout /d choice][/m text]    #让用户在选项中做出选择
/c  #指定用户选择键
/n  #隐藏用户选择键
/cs #区分大小写
/t  #timeout 后的行为
/m  #提示符前面的文字

for {%variable|%%varable} in(set) do command[commandlineoptions]    #对一组文件中的每个文件运行指定的命令
{%variable|%%varable}       #必须的参数，代表可替换的参数，使用%variable通过命令提示符执行for命令。
                            使用%%variable在批处理文件中执行for命令。变量要区分大小写，并且要用alpha值表示如%A，%B.
(set)       #必须的参数，指定要用命令处理的文件、目录、数值范围和文本字符串。
commandd    #必须的参数，指定对文件进行的命令
commandlineoptions      #指定与命令同时使用的命令选项