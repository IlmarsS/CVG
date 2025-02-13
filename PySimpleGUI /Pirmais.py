# PySimpleGUI kalkulators
from cmath import *
import PySimpleGUIWeb as sg
if not hasattr(html, 'unescape'):
    import html.parser
    html.unescape = html.parser.HTMLParser()

layout = [[sg.Text('Ievadiet izteiksmi', size = (16,1)),sg.Input(k='-IN-'), sg.Button('=')],
          [sg.Text('Rezultāts: ', size = (16,1)), sg.Input(k='-OUT-')] ]
window = sg.Window('kalkulators', layout)

while True:
    event, values = window.read()
    # print(event, values)
    if event == sg.WIN_CLOSED:
        break
    elif event == "=" :
        window['-OUT-'].update(eval(values['-IN-']))

window.close()
