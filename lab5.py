import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_csv(filepath): #loads a csv filePATH
  csv_file = pd.read_csv(filepath)
  return csv_file
def load_column_data(csv_file , variable_name): #loads the particular column from the given csv file
  column_data = csv_file[variable_name]
  return column_data
def calculate_statistics(column_data): #calculate the count , mean , std_dev , minimum , maximum of the give distribution
  column_data = np.array(column_data).astype(float).flatten()
  count = column_data.shape[0]
  mean = np.mean(column_data)
  std_dev = np.std(column_data)
  minimum = np.min(column_data)
  maximum = np.max(column_data)
  return count , mean , std_dev , minimum , maximum
def display_histogram(column_data , column_name): #displays the histogram of the given distribution.
  plt.hist(column_data , density = True , bins = 15)
  plt.ylabel(column_name)
  plt.show()
if __name__ == "__main__":
  print("***************** Welcome to the Python Data Analysis App**********")
  # loop untill user exits
  while True:
   print("Select the file you want to analyze: ")
   print("1.Population Data")
   print("2.Housing Data")
   print("3.Exit the program")
   # loop until user enters right value
   while True:
    try:
     option = int(input())
     if option>3:
      print("Enter the option from above")
     else:
      break
    except ValueError:
     print("Enter a valid value for option")
   # Load population data if user enters 1
   if option ==1:
    print("You have entered Population Data.")
    filepath = "PopChange.csv"
    csv_file = load_csv(filepath)
    while True:
     print("Select the Column you want to analyze:")
     start_option ="a"
     iter =0
     for column in csv_file.columns[4:]:
      option_char =chr(ord(start_option) + iter)
      print(option_char+f". {column}")
      iter+=1
     print(f"{chr(ord(start_option) + iter)}. Exit the column") 
     # prompt the user for column value.We take only last three columns for population data as specified in the question
     while True:
          try:
           user_input = str(input())
           break
          except ValueError:
           print("Enter a valid value for option")
     # exit or analyze the column based on user input using your helper functions
     if user_input.lower() == chr(ord(start_option) + iter):
       print("You have selected to exit the column menu")
       break
     else:
      while True:
       if len(list(csv_file.columns)[4:])>abs(ord(user_input.lower())-ord(start_option)):
        column_name = list(csv_file.columns)[4:][abs(ord(user_input.lower())-ord(start_option))]
        column_data = load_column_data(csv_file, column_name)
        count , mean , std_dev , min , max = calculate_statistics(column_data)
        print(f"You have selected {column_name}")
        print(f"count : {count} , mean : {mean} , standard_deviation : {std_dev} ,min : {min} , max : {max}")
        print(f"The histogram of {column_name} is now displayed: ")
        list_of_column_data = column_data.to_list()
        # Creating histogram
        fig, ax = plt.subplots(figsize =(10, 7))
        bins= [ value for value in range(0, 250000, 1000)]
        ax.hist(list_of_column_data, bins)
        # Show plot 
        plt.show()
        break
       else:
        print("Enter a valid option")
   # fetch housing data.Repeat the same above steps  
   if option ==2:
    filepath = "Housing.csv"
    print("You have entered Housing Data.")
    csv_file = load_csv(filepath)
    while True:
     print("Select the Column you want to analyze:")
     start_option ="a"
     iter =0
     for column in csv_file.columns:
      option_char =chr(ord(start_option) + iter)
      print(option_char+f". {column}")
      iter+=1
     print(f"{chr(ord(start_option) + iter)}. Exit the column") 
     while True:
          try:
           user_input = str(input())
           break
          except ValueError:
           print("Enter a valid value for option")
     if user_input.lower() == chr(ord(start_option) + iter):
       print("You have selected to exit the column menu") 
       break
     else:
      while True:
       if len(list(csv_file.columns))>abs(ord(user_input.lower())-ord(start_option)):
        column_name = list(csv_file.columns)[abs(ord(user_input.lower())-ord(start_option))]
        column_data = load_column_data(csv_file, column_name)
        count , mean , std_dev , min , max = calculate_statistics(column_data)
        print(f"You have selected {column_name}")
        print(f"count : {count} , mean : {mean} , standard_deviation : {std_dev} ,min : {min} , max : {max}")
        print(f"The histogram of {column_name} is now displayed: ")
        list_of_column_data = column_data.to_list()
        # Creating histogram
        fig, ax = plt.subplots(figsize =(10, 7))
        bins= [ value for value in range(0, 250, 10)]
        ax.hist(list_of_column_data, bins)
        # Show plot
        plt.show() 
        break
       else:
        print("Enter a valid option")
    # now if user exits the program display the histogram if the user has selected any column.This was done in accordance with the output of the question 
   if option ==3:
    try:
     column_data
    except NameError:
     print("*************** Thanks for using NICOLAI'S Data Analysis App**********.")
    else:
     print("*************** Thanks for using NICOLAI'S Data Analysis App**********.The histogram of the column will be displayed")
     display_histogram(column_data , column_name)
    break