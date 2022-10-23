import PySimpleGUI as sg
import signup
import validate
import sqlite3
import main

sg.theme("DarkBlack1")

layout = [[sg.Text('Username'), sg.Input(key='-USERNAME-', do_not_clear=True, size=(30, 10))],
          [sg.Text('Password'), sg.Input(key='-PASSWORD-', password_char='*', do_not_clear=True, size=(30, 10))],
          [sg.Text("Don't have an account?"), sg.Button('Create Account', key='-CREATE_ACCOUNT-', size=(15, 1))],
          [sg.Text("")],
          [sg.Button("Login", key='-LOGIN-', size=(20, 1), enable_events=True)],
          [sg.Exit(key='-EXIT-', size=(10, 1))]
          ]

window = sg.Window("Login Window", layout, size=(300, 200), element_justification='c')


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, '-EXIT-'):
        break

    elif event == '-CREATE_ACCOUNT-':
        signup.open_window()

    elif event == '-LOGIN-':
        validation_result = validate.validate_login(values)
        if validation_result[0]:
            conn = sqlite3.connect('reservation_information.db')
            cursor = conn.cursor()
            cursor.execute("SELECT USERNAME, PASSWORD FROM USER_INFORMATION WHERE (USERNAME = ? AND PASSWORD = ?)",
                           (str(values['-USERNAME-']), str(values['-PASSWORD-'])))
            data = cursor.fetchone()
            if data:
                main.open_main()
            else:
                sg.popup("Incorrect Username or Password")

        else:
            error_message = validate.generate_error_message(validation_result[1])
            sg.popup(error_message)


window.close()
