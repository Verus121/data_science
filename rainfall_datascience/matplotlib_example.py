import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime
import re


file_name = "sample2.csv"

line_list = [line for line in open(file_name)]
line_list = [s.rstrip().split(",") for s in line_list]

column_names = line_list.pop(0)

date_list = []

eventdates_list = []
chantrellcreekelementary_list = []
portkells_list = []
semiamoofishgameclub_list = []
surreykwantlenpark_list = []
surreymunicipalhall_list = []
whiterockstp_list = []

for line in line_list:
    # https://stackoverflow.com/questions/466345/converting-string-into-datetime
    # https://strftime.org/
    datestring = line[1]
    clean_datestring = datestring[:-7] # don't need milliseconds
    datetime_object = datetime.strptime(clean_datestring, '%Y-%m-%d %H:%M')
    date_list.append(datetime_object)

    chantrellcreekelementary_list.append(line[2])
    portkells_list.append(line[3])
    semiamoofishgameclub_list.append(line[4])
    surreykwantlenpark_list.append(line[5])
    surreymunicipalhall_list.append(line[6])
    whiterockstp_list.append(line[7])

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(date_list, chantrellcreekelementary_list)
ax.plot(date_list, portkells_list)
ax.plot(date_list, semiamoofishgameclub_list)
ax.plot(date_list, surreykwantlenpark_list)
ax.plot(date_list, surreymunicipalhall_list)
ax.plot(date_list, whiterockstp_list)
