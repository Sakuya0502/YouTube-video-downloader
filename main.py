import PySimpleGUI as sg

from data.download import Download

output_loc = ''

menu = [["Settings", ["About", "Exit"]]]

frame1 = [[sg.T("YOUTUBE URL")],
[sg.I(key="INPUT")]]
frame2 = [[sg.T("FILE NAME")],
[sg.I(key="INPUT2")]]
frame3 = [[sg.T("OUTPUT FILE")],
[sg.B("Find in my computer", key="BUTTON1", visible=True)],
[sg.Text("SUCCESS", key="Success_Text", visible=False)]
]

layout = [
    [sg.Menu(menu, key="-menu-")],
    [sg.Frame("INPUT URL", frame1)],
    [sg.Frame("INPUT FILENAME", frame2)],
    [sg.Frame("CHOOSE OUTPUT FILE", frame3)],
    [sg.B("DOWNLOAD", key="_DOWNLOAD_")],
    [sg.Text("[ERROR] Something went wrong, please try again!", key="Error_Text", visible=False, text_color="Red")]
    ]

window = sg.Window("Simple YouTube Video Downloader", layout, size=(724, 520))

while True:
    event, values = window.read()
    if event in (None, 'Exit', 'Cancel', sg.WIN_CLOSED):
        break
    elif event == 'BUTTON1':
        folder = sg.popup_get_folder("Please select a folder")
        output_loc = str(folder)
        window['Success_Text'].update(visible=True)
    elif event == '_DOWNLOAD_':
        ERROR = Download().is_error(values["INPUT"], values["INPUT2"], str(output_loc))
        if ERROR == False:
            window['Error_Text'].update(visible=True)
        elif ERROR == True and values["INPUT2"] == '':
            Down = Download().nofileName(values["INPUT"], str(output_loc))
            window['Error_Text'].update(visible=False)
            window['Success_Text'].update(visible=False)
            if Down == True:
                sg.popup("Download success!")
            else:
                sg.popup_error("Something went wrong, please try again!")
        elif ERROR == True and values["INPUT2"] != '':
            Down = Download().download_vids(values["INPUT"], values["INPUT2"], str(output_loc))
            window['Error_Text'].update(visible=False)
            window['Success_Text'].update(visible=False)
            if Down == True:
                sg.popup("Download success!")
            else:
                sg.popup_error("Something went wrong, please try again!")
    elif event == "About":
        sg.popup('Application Info:\nVersion 0.1', 'Other Info:\n{}'.format(str(sg.get_versions())))
    print(event, values)

window.close()