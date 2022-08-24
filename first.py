import PySimpleGUI as sg
import layout as layout

layout = [

    [sg.Text('请输入你的信息')],
    [sg.Text('姓名'), sg.InputText('韩巍')],
    [sg.Text('性别'), sg.InputText('男')],
    [sg.Text('国籍'), sg.InputText('中国')],
    [sg.Button('确认'), sg.Button('取消')]

]

window = sg.Window('PySimpleGUI', layout)

# 读取窗口
while True:
    event, value = window.read()
    if event == None:
        break

window.close()
