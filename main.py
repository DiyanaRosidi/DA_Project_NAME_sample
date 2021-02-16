#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: Diyana Rosidi
#Group Name: <TheBlue757>
#Class: <PN2004J>
#Date: <16 Feb 2020>
#Version: <...>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pie chart
import matplotlib.pyplot as pit
#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):

    #load excel data (CSV format) to dataframe - 'df'
    dataframe = pd.read_csv('MonthyVisitors.csv')
    #show specific country dataframe
    sortCountry(dataframe)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

  #print number of rows in dataframe
  print("There are " + str(len(df)) + " data rows read. \n")

  #display dataframe (rows and columns)
  print("The following dataframe are read as follows: \n")
  print(df)

  #display a specific country (Australia) in column #33
  country_label1 = df.columns[14]
  print("\n" + country_label1 + "was selected.")
  country_label2 = df.columns[15]
  print("\n" + country_label2 + "was selected.") 
  country_label3 = df.columns[16]
  print("\n" + country_label3 + "was selected.") 
  country_label4 = df.columns[17]
  print("\n" + country_label4 + "was selected.") 
  country_label5 = df.columns[18]
  print("\n" + country_label5 + "was selected.")
  country_label6 = df.columns[19]
  print("\n" + country_label6 + "was selected.")

  #reading columns 
  df.columns

  #sorting dataframe (rows and columns)
  print("\nThe following dataframe are read as follows: \n")
  SortedDF = (df[['Year','Month',' India ',' Pakistan ',' Sri Lanka ',' Saudi Arabia ', ' Kuwait ', ' UAE ']][350:480])

  
  #Printing the data

  print(SortedDF)


  # This will convert dtypes from object to int
  SortedDF[' India '] = SortedDF[' India '].astype(int)
  SortedDF[' Pakistan '] = SortedDF[' Pakistan '].astype(int)
  SortedDF[' Sri Lanka '] = SortedDF[' Sri Lanka '].astype(int)
  SortedDF[' Saudi Arabia '] = SortedDF[' Saudi Arabia '].astype(int)
  SortedDF[' Kuwait '] = SortedDF[' Kuwait '].astype(int)
  SortedDF[' UAE '] = SortedDF[' UAE '].astype(int)


  #Removing unwanted Columns
  New = SortedDF.drop(['Year','Month'], axis=1)
  # Add up the total amount of visitors
  total = New.sum()

    #Sorting on descending order
  Sortedvalue = total.sort_values(ascending=False)

  #Sorting toward top 3 countries
  print("The Top 3 countries of visitors to Singapore from the span of 10 years are: ")
  print(Sortedvalue.head(n=3))  
  #pie chart
  activities = ['India', 'Sri Lanka', 'UAE']
  slices = [9896496, 940176, 700994]
  colours = ['r', 'g', 'm']

  pit.pie(slices,
        labels=activities,
        startangle=90,
        shadow=True,
        explode=(0.2, 0, 0),
        autopct='%1.2f%%')

  pit.legend(loc="upper left")

  pit.show()








  return

#########################################################################
#FUNCTION Branch: End of Code
#########################################################################
#Pie chart



  return
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################