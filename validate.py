from datetime import datetime


def validate_login(values):
    is_valid = True
    values_invalid = []
    if len(values['-USERNAME-']) == 0:
        values_invalid.append('Username cannot be blank')
        is_valid = False

    if len(values['-PASSWORD-']) == 0:
        values_invalid.append('Password cannot be blank')
        is_valid = False

    result = [is_valid, values_invalid]
    return result

def validate_signup(values):
    is_valid = True
    values_invalid = []
    if len(values['-REAL_NAME-']) == 0:
        values_invalid.append('Name is blank')
        is_valid = False

    if len(values['-AGE-']) == 0:
        values_invalid.append('Age is blank')
        is_valid = False

    if len(values['-ADDRESS-']) == 0:
        values_invalid.append('Address is blank')
        is_valid = False

    if len(values['-CONTACT_NUMBER-']) == 0:
        values_invalid.append('Contact number is blank')
        is_valid = False

    if len(values['-USERNAME-']) == 0:
        values_invalid.append('Username cannot be blank')
        is_valid = False

    if len(values['-USERNAME-']) < 3:
        values_invalid.append('Username should at least be 3 characters')
        is_valid = False

    if len(values['-PASSWORD-']) == 0:
        values_invalid.append('Password cannot be blank')
        is_valid = False

    if (values['-CON_PASSWORD-']) != (values['-PASSWORD-']):
        values_invalid.append('Incorrect confirmed password')
        is_valid = False

    result = [is_valid, values_invalid]
    return result


def is_date_before_now(date_sched):
    # 2021-08-01 13:09:43
    date_object = datetime.strptime(date_sched, '%Y-%m-%d')
    now_object = datetime.now()
    return date_object < now_object


def validate(values):
    is_valid = True
    values_invalid = []

    if len(values['-PAX-']) == 0:
        values_invalid.append('No. of Attendees')
        is_valid = False

    if len(values['-EVENT-']) == 0:
        values_invalid.append('Type of Event')
        is_valid = False

    if len(values['-DURATION-']) == 0:
        values_invalid.append('Event duration')
        is_valid = False

    if is_date_before_now(values['-DATE-']):
        values_invalid.append("The event can't be in the past")
        is_valid = False

    if len(values['-DATE-']) == 0:
        values_invalid.append('Event Date')
        is_valid = False

    result = [is_valid, values_invalid]
    return result


def generate_error_message(values_invalid):
    error_message = ''
    for value_invalid in values_invalid:
        error_message += ('\nInvalid' + ':' + value_invalid)

    return error_message
