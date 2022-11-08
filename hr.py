import xlrd
import pandas as pd
import numpy as np
import keyboard
import time

employee_data = pd.read_excel('./Dataset.xlsx')

array_data_form = np.array(employee_data)

state = None

def check_employee():
    Id = int(input("Enter employee I.D.: "))

    employee_data_array = np.array(array_data_form[Id])

    employee_data_tree = {
        'name_first': str(employee_data_array[0]),
        'name_last': str( employee_data_array[1]),
        'salary': int(employee_data_array[2]),
        'leaves_last_month': int(employee_data_array[-1]),
        'abscences': int(employee_data_array[-2]),
        'speciality': str(employee_data_array[3]),
        'occupation':str(employee_data_array[4])
    }

    print('Name: ', employee_data_tree['name_first'], employee_data_tree['name_last'])
    print('Speciality: ',employee_data_tree['speciality'])
    print('Abscences and leaves: ',employee_data_tree['abscences'],'and',employee_data_tree['leaves_last_month'],' respectively.')
    print('Occupation: ',employee_data_tree['occupation'])
    print('Salary: ',employee_data_tree['salary'])

def commands():
    if state == True:
        check_employee()

while True:
    if state == None:
        print('Waiting for command...')
        time.sleep(1)

    if keyboard.is_pressed('space'):
        state = True

    commands()

    



                              