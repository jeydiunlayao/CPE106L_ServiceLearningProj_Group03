import PySimpleGUI as sg
import validate
import database_interface

def open_window():
    layout = [[sg.Text("SIGN UP", key="new")],
              [sg.Text('Name:'), sg.Input(key='-REAL_NAME-', do_not_clear=True, size=(30, 10))],
              [sg.Text('Age:'), sg.Input(key='-AGE-', do_not_clear=True, size=(30, 10))],
              [sg.Text('Address: '), sg.Input(key='-ADDRESS-', do_not_clear=True, size=(30, 10))],
              [sg.Text('Contact No. '), sg.Input(key='-CONTACT_NUMBER-', do_not_clear=True, size=(30, 10))],
              [sg.Text('Username:'), sg.Input(key='-USERNAME-', do_not_clear=True, size=(30, 10))],
              [sg.Text('Password:'), sg.Input(key='-PASSWORD-', password_char='*',do_not_clear=True, size=(30, 10))],
              [sg.Text('Confirm Password:'), sg.Input(key='-CON_PASSWORD-', password_char='*',do_not_clear=True, size=(30, 10))],
              [sg.Button("Create an Account", key='-SIGNUP-', size=(20, 1), enable_events=True)],
              [sg.Exit(size=(10, 1))],
              ]
    window = sg.Window("Second Window", layout, modal=True, size=(300, 300), element_justification='c')
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == '-SIGNUP-':
            validation_result = validate.validate_signup(values)
            if validation_result[0]:
                database_interface.insert_user_details(values['-REAL_NAME-'], values['-AGE-'],
                                                       values['-ADDRESS-'], values['-CONTACT_NUMBER-'],
                                                       values['-USERNAME-'], values['-PASSWORD-'])
                sg.popup('Account creation successful!')
                window.close()
            else:
                error_message = validate.generate_error_message(validation_result[1])
                sg.popup(error_message)

    window.close()
