# Path variables
# import the os module to access automated os pathing
import os

# get the local working directory for your current application
print(os.getcwd()) #get current working directory
print("")

# set variables for the file path, and file name
# paths can be lengthy
path = os.getcwd()
filename = 'data/data_1.txt'  #folder/file

# print the proper absolute path of your file
print(path+'/'+filename)
print("")
