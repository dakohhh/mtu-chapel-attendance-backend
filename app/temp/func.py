import pandas as pd
import numpy as np





def read_file(df):
    mtu_databse = pd.read_csv("MTU Student Database.csv")

    mtu_databse_arr = np.array(mtu_databse)
    present_students_arr = np.array(df)

    first_data = []

    absentees = []


    for i in mtu_databse_arr:
        emp = []
        for j in range(0, 4):
            emp.append(i[j+1])
        first_data.append(emp[2])

    for i in present_students_arr:
        if i[5] in first_data:
            first_data.remove(i[5])

    for i in first_data:
        for j in mtu_databse_arr:
            if i == list(j)[3]:
                absentees.append(list(j)[1:5])

    return absentees


