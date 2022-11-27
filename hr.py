import pandas as pd
import numpy as np

#collecting data from file
data = pd.read_excel("./assets/datasets/Data.xlsx")
 
array_data = np.array(data)

state = None

#check employee stats
def check_employee(name):     
    names = pd.DataFrame(data['Employee_Name'].str.lower())
    names_array = np.array(names)
    
    count = 0
    
    for i in names_array:
        if i != name:
            count += 1
        else:
            employee_data = array_data[count]
    
            employee_info = np.array(employee_data)
    
            ID = int(input('Enter the I.D.: '))
             
            if ID == employee_info[1]:
                
                namee = str(employee_info[0]),
                identity =  int(employee_info[1]),
                married = int(employee_info[2]),
                score =  int(employee_info[3]),
                position = str(employee_info[5]),
                sex = str(employee_info[6]),
                yoh = int(employee_info[7]),
                s_projects =  int(employee_info[9]),
                absences = int(employee_info[11]),
                leaves =  int(employee_info[12]),
                qualification = str(employee_info[13]),
                salary = int(employee_info[4])  
                
                employee = [namee,identity,married,score,position,sex,yoh,s_projects,absences,leaves,qualification,salary]        
                
                return  employee   



#sort employees according to performance                   
def sort_employees():
    global state
    
    employees = []
    count = 0
    working = []
    arrays = None

    #essentials
    leaves = None
    absences = None
    last_perf = None
    s_pro = None
    perf_score = None

    for employee in array_data:
        count += 1
        name = employee[0]

        if name not in employees:
            leaves = employee[-2]
            absences = employee[-3]
            last_perf = employee[-4]
            s_pro = employee[-5]
            perf_score = employee[3]

            score = (int(last_perf + s_pro + perf_score) - int(leaves + absences))
            
            working.append({"Name":name, "Score":score})
            employees.append(name)

    arrays = sorted(working, key=lambda i: i["Score"])

    return arrays