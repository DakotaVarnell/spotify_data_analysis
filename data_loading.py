#import csv library
import csv
import cx_Oracle


#create a list where we will be storing the row information
row_information = []

#open the csv file and read it 
with open('Spotify_final_dataset.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #iterate through each row and read them into a python list
    for row in csv_reader:
        row_information.append(row)

#open the file we will be writing to
file = open('load_spotify_table.sql', 'a', encoding='utf-8')

#dynamically create the sql to insert each of the values, i being the particular row and the other index being the data member of the list that corresponds to the value in oracle
for i in range(len(row_information)):
    insert_stmt = 'INSERT INTO spotify_data VALUES(' + row_information[i][0] + ',' + "'" + str(row_information[i][1]).replace("'", "").replace(",","") + "'" + ',' + "'" + str(row_information[i][2]).replace(",", "").replace("'", "") + "'" + ',' + row_information[i][3] + ',' + row_information[i][4] + ',' + "'" + row_information[i][5] + "'" + ',' + "'" + row_information[i][6] + "'" + ',' + row_information[i][7] + ');\n'
    file.write(insert_stmt)

#-----TO DO
#-----Delete the old oracle from your system
#-----Download the newest version of oracle
#-----Get the connection information and connect it to python
#-----Get Cx_Oracle to run your table creation commands
#-----Get Cx_Oracle to run your insertion statements
