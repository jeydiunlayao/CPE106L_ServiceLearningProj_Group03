import PySimpleGUI as sg
import database_interface
import validate
import db_info


def open_main():
    sg.theme('DarkBlack1')

    event_types = ("Basketball", "Volleyball", "School Event", "Community Event", "Contest", "Local Concert",)
    start_time = ("9:00 am", "9:30 am", "10:00 am", "10:30 am", "11:00 am", "11:30 am", "12:00 nn", "12:30 pm", "1:00 pm",
                  "1:30 pm", "2:00 pm", "2:30 pm", "3:00 pm", "3:30 pm", "4:00 pm", "4:30 pm", "5:00 pm", "5:30 pm",
                  "6:00 pm", "6:30 pm", "7:00 pm", "7:30 pm", "8:00 pm", "8:30 pm", "9:00 pm")
    event_duration = ("30 minutes", "1 hour", "1 hour 30 minutes", "2 hours")

    layout = [[sg.Text("Expected amount of Attendees:"), sg.Input(key="-PAX-", do_not_clear=True, size=(20, 1))],
              [sg.Text("Type of event: "), sg.InputCombo(event_types, key="-EVENT-", size=(30, 1), enable_events=True)],
              [sg.Text("Start Time: "), sg.InputCombo(start_time, key="-START-", size=(35, 1), enable_events=True)],
              [sg.Text("Duration: "), sg.InputCombo(event_duration, key="-DURATION-", size=(35, 1), enable_events=True)],
              [sg.Button("End Time: ", size=(15, 1)), sg.Text("", key="-END-", size=(10, 1))],
              [sg.CalendarButton("DATE OF EVENT", close_when_date_chosen=True, target="-DATE-", location=(0, 0),
                                 no_titlebar=False, format='%Y-%m-%d', size=(15, 1)), sg.Input(key="-DATE-", size=(25, 1))],
              [sg.Button('Reserve Time', size=(15, 1)), sg.Button('See Reservations', size=(15, 1)), sg.Exit(size=(10, 1))]
              ]

    reservations_array = []

    window = sg.Window('Barangay Court Scheduling', layout, size=(350, 220))


    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        elif event == 'End Time: ':
            if values['-START-'] in start_time:
                time_index = start_time.index(values['-START-'])
                duration_index = event_duration.index(values['-DURATION-'])
                end_index = time_index + duration_index + 1
                end_time = start_time[end_index]
                window['-END-'].Update(end_time)

        elif event == 'Reserve Time':
            validation_result = validate.validate(values)
            if validation_result[0]:
                event = values['-EVENT-']
                duration = values['-DURATION-']
                database_interface.insert_contact(values['-PAX-'], event, values['-START-'], end_time, duration,
                                                  values['-DATE-'])
                sg.popup('Reservation submitted!')
            else:
                error_message = validate.generate_error_message(validation_result[1])
                sg.popup(error_message)
        elif event == 'See Reservations':
            db_info.create()

    window.close()
