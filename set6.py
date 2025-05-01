
# # 1.Create a file with file name sample.txt, accept some data from the user and store it in the file
# with open('sample.txt', 'w') as f:
#     data = input("Enter some data to store in file: ")
#     f.write(data)
# print("Data written to file.")


# # 2.Display the data stored in the sample.txt file (created in question 1).
# with open("sample.txt", "r") as f:
#     content = f.read()
#     print("File Content:\n", content)


# # 3.Accept some data from the user and append it into the file sample.txt (created in question 1),
# # also the data in the file.

# with open("sample.txt", "a") as f:
#     more_data = input("Enter data to append: ")
#     f.write("\n" + more_data)

# with open("sample.txt", "r") as f:
#     content = f.read()
#     print("Updated File Content:\n", content)


# # 4.Accept the file name from the user, check the availability of the file: i). If the file exists display
# # the data on the screen, ii). If the file is not available, display the appropriate message.

# import os
# filename = input("Enter the file name: ")
# if os.path.isfile(filename):
#     with open(filename, "r") as f:
#         print("File Content:\n", f.read())
# else:
#     print("File does not exist.")

# 5. Accept the file name from the user, check the availability of the file:
# a. If the file exists, display: i). No. of characters, ii). No. of words and iii). No. of lines
# b. If the file does exist, than display the appropriate message.

# import os,sys
# file_name=input('enter the file name')
# if os.path.isfile(file_name):
# 	f=open(file_name,'r')
# else:
# 	print(file_name+'does not exist')
# 	sys.exit()
# lc=wc=cc=0
# for line in f:
# 	words=line.split()
# 	lc=lc+1
# 	wc=wc+len(words)
# 	cc=cc+len(line)
# print('number character',cc)
# print('number words',wc)
# print('number line',lc)


# # 6.Create and open the binary file with ‘with’ option. Store names of all the subjects you study in
# # semester 2. Ask user to enter the subject number they wanted to see and display that subject name.

# num_subjects = int(input("Enter the number of subjects you study in semester 2: "))
# subjects = []
# for i in range(num_subjects):
#     subject_name = input("Enter the name of subject: ")
#     subjects.append(subject_name)

# with open('subjects_semester_2.bin', 'wb') as f:
#     for i in subjects:
#         f.write(i.encode() + b'\n') 

# loaded_subjects = []
# with open('subjects_semester_2.bin', 'rb') as f:
#     for i in f:
#         loaded_subjects.append(i.decode().strip())  

# sub=(input('enter subject:-'))
# if sub in loaded_subjects:
#     print('subject is:',sub)


# 7.Create a file named ‘img1’, store an image into it. Open another file named ‘img2’, copy the
# same image as in the file ’img1’. Also store both files into the zip file named ‘imp_img’.

# import zipfile
# from zipfile import *

# f1=open('img1.jpg','rb')
# f2=open('img2.jpg','wb')
# read_f1=f1.read()
# f2.write(read_f1)

# f=ZipFile('imp_img.zip','w')
# f.write('img1.jpg')
# f.write('img2.jpg')
# f.close()

# 8.Create a file with ‘with’ option, name it as ‘marks.dat’.
# i). Accept subject name and marks from the user, store the data in the file.
# ii). Give three options to the user: a). To view whole file, b). Accept and edit the marks of a
# subject user want to change.
# iii). Exit

# def display_menu():
#     print("\n--- Menu ---")
#     print("1. View whole file")
#     print("2. Edit marks of a subject")
#     print("3. Exit")
#     choice = input("Enter your choice (1/2/3): ")
#     return choice
# def add_marks():
#     with open('marks.dat', 'a') as file:  
#         subject = input("Enter subject name: ")
#         marks = input(f"Enter marks for {subject}: ")
#         file.write(f"{subject}: {marks}\n")
#     print(f"Marks for {subject} added successfully.")
# def view_marks():
#     try:
#         with open('marks.dat', 'r') as file:
#             contents = file.readlines()
#             if contents:
#                 print("\nSubject and Marks in the file:")
#                 for line in contents:
#                     print(line.strip())
#             else:
#                 print("No data available in the file.")
#     except FileNotFoundError:
#         print("No data file found. Please add some marks first.")
# def edit_marks():
#     subject_to_edit = input("Enter the subject name you want to edit: ")
#     try:
#         with open('marks.dat', 'r') as file:
#             lines = file.readlines()
#         found = False
#         for i in range(len(lines)):
#             subject, marks = lines[i].strip().split(": ")
#             if subject == subject_to_edit:
#                 new_marks = input(f"Enter new marks for {subject_to_edit}: ")
#                 lines[i] = f"{subject_to_edit}: {new_marks}\n"
#                 found = True
#                 break
#         if found:
#             with open('marks.dat', 'w') as file:
#                 file.writelines(lines)
#             print(f"Marks for {subject_to_edit} updated successfully.")
#         else:
#             print(f"Subject '{subject_to_edit}' not found.")
#     except FileNotFoundError:
#         print("No data file found. Please add some marks first.")
# def main():
#     while True:
#         print("\n--- Marks Data Program ---")
#         print("1. Add marks for a subject")
#         print("2. View marks in the file")
#         print("3. Edit marks for a subject")
#         print("4. Exit")
#         choice = input("Enter your choice (1/2/3/4): ")
#         if choice == '1':
#             add_marks()
#         elif choice == '2':
#             view_marks()
#         elif choice == '3':
#             edit_marks()
#         elif choice == '4':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice. Please try again.")
# if __name__ == "__main__":
#     main()



# # 9)
# # 1)
# import re
# # a)
# # str='soon,sined,sima,meera,disha,soo'
# # f=re.findall(r's\w{0,3}',str)
# # print(f)

# # b)
# str='soon,si!ned,sima,mee;ra,di@sha,soo'
# f=re.split(r'\W',str)
# print(f)

# # c)
# # str='soon,si!ned,1sima,4mee;ra,5di@sha,soo'
# # f=re.findall(r'\d\w*',str)
# # print(f)

# # d)
# # str='soon,sined,sima,meera,disha,soo'
# # f=re.findall(r'\b\w{3,5}\b',str)
# # print(f)

# # f)
# # str='meera 123456789098'
# # f=re.findall(r'\b\d+\b',str)
# # print(f)

# # g)
# import re
# str='atjff apdcnj meera disha satduh sapdnb'
# f=re.findall(r'\b[at|ap]\w*\b',str)
# print(f)

# # h)
# str='atjff apdcnj meera disha'
# if str.startswith('at'):
#     print('starting with at')
# else:
#     print('no')


# 10.Do as directed:
# # a). Name the package used to deal with data frame.
# Pandas (Package: pandas)
# # b). Name the package used to deal with data .xlsx file.
# OpenPyXL (openpyxl) or Pandas (with read_excel() function)
# # c). Name the function used to read the .csv file.
# read_csv() 
# # d). Name the function used to read the .xlsx file.
# read_excel() 
# # e). Name the function used to read the tuple.
# Data_Frame()

# 11.Create a dictionary which stores (at least 10 records)empid, name, city, salary and perform
# following operations:
# a). Display first three records
# b). Display last five records
# c). Display only Name and City
# d). Display employee who belongs to Mumbai
# e). Display employee name who belongs to Mumbai
# f). Display employee whose salary is more than 25000
import pandas as pd
employees = {'empid':[1,2,3,4,5,6,7,8,9,10],'name':['dharvi','dhruvi','khushi','vishva','riva','yash','parv','harsh','keval','fenil'],'city':['rjk','ahm','surat','broda','rjk','ahm','surat','rjk','ahm','broda'],'salary':[5674,475,3466,6789,5677,3454,3465,3465,3567,8976]}
   
df=pd.DataFrame(employees)
# print("First three records:")
# print(df.head(3))

# print("\nLast five records:")
# print(df.tail(5))

# print(df[['name','city']])

# print(df[['name']][df.city=='rjk'])

# print(df[['name']][df.salary>4000])



# 12.Create an xlsx file store marks of five subjects, plot the data on the bar graph.


# import pandas as pd
# import matplotlib.pyplot as plt
# df=pd.read_excel('bargraph.xlsx')
# print(df)
# x=df['subject']
# y=df['marks']
# plt.xlabel('subjects')
# plt.bar(x,y,label='graph',color='red')
# plt.ylabel('marks of sub..')
# plt.title('bar graph')
# plt.legend()
# plt.show()


# 13.Take five income source of the Government and display it on the pie chart.
# import matplotlib.pyplot as plt
# income_sources = ['Income Tax', 'Custom Duties', 'Excise Duties', 'GST', 'Borrowing and Loans']
# income_values = [40, 20, 15, 10, 15]  
# plt.pie(income_values, labels=income_sources, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'])
# plt.title('Government Income Sources')
# plt.legend()
# plt.show()

# import pandas as pd 
# import matplotlib.pyplot as plt
# df=pd.read_excel('tex.xlsx')
# print(df)
# x=df['income_values']
# labels = df['income_sources']
# plt.pie(x,labels=labels)
# plt.title('Government Income Sources')
# plt.legend()
# plt.show()

# 14.Draw the line chart representing BSE (Bombay Stock Exchange) index in last 10 years.
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_excel('BSE_Sensex_Historical_Data.xlsx')
# df['Value'] = pd.to_datetime(df['Value'])
# df.set_index('Value', inplace=True)
# plt.figure(figsize=(10, 6))
# plt.plot(df.index, df['Year'], label='BSE Sensex Closing Value', color='b')
# plt.title('BSE Sensex Index - Last 10 Years')
# plt.xlabel('Year')
# plt.ylabel('Closing Value')
# plt.grid(True)
# plt.legend()
# plt.tight_layout()
# plt.show()

# 15.Plot the grouped bar graph using the appropriate data.
# import matplotlib.pyplot as plt
# import numpy as np
# subjects = ['Math', 'Science', 'English']
# exam1 = [80, 75, 90]
# exam2 = [85, 78, 88]
# x = np.arange(len(subjects))
# width = 0.4
# plt.bar(x - width/2, exam1, width, label='Exam 1', color='skyblue')
# plt.bar(x + width/2, exam2, width, label='Exam 2', color='orange')
# plt.xlabel('Subjects')
# plt.ylabel('Marks')
# plt.title('Marks in Exam 1 and Exam 2')
# plt.xticks(x, subjects)
# plt.legend()
# plt.show()
