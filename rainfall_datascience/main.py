# To show the graph, Run Current File in Python Interactive Window
from matplotlib import pyplot as plt

# file_name = "SurreyRainfall2020.csv"
file_name = "sample.csv"

lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)

# The first line in the csv file is the name of the columns.
# When the next method is used, the generator iterator list_line is permenantly moved to the next line in lines. 
column_names = next(list_line)


# This section defeats the purpose of generating! 
list_length = 0
eventdates_list = []
chantrellcreekelementary_list = []
portkells_list = []
semiamoofishgameclub_list = []
surreykwantlenpark_list = []
surreymunicipalhall_list = []
whiterockstp_list = []

for line in list_line:
    list_length += 1
    eventdates_list.append(line[1])
    chantrellcreekelementary_list.append(line[2])
    portkells_list.append(line[3])
    semiamoofishgameclub_list.append(line[4])
    surreykwantlenpark_list.append(line[5])
    surreymunicipalhall_list.append(line[6])
    whiterockstp_list.append(line[7])

print(list_length)
# print(eventdates_list)
# print(chantrellcreekelementary_list)



# plt.plot(eventdates_list, chantrellcreekelementary_list, color='pink', marker='o', linestyle='solid')
# plt.title("Weather in chantrell creek elementary")
# plt.ylabel("rainfall in cm")
# plt.show()

# bar chart 
plt.bar(eventdates_list, chantrellcreekelementary_list) 