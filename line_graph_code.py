#This script creates two line graphs which imports data from excel (our data was taken from papers, world databank etc, referenced
#at the end of the presentation).

#Generating the first graph showing obesity rates across the US for all genders (1991-2014)

import pandas as pd
import matplotlib.pyplot as plt

#Assigning a variable to the datasheet in excel
data = pd.read_excel(r'C:\Users\Louise\Documents\NIH_docs\Python Scripts\fig1_obesity_gen.xlsx')

#Defining variables
year = data['Year']
male_obesity=data['Male']
female_obesity=data['Female']
both_genders=data['Both sexes']

#Plotting graph
plt.figure(1)
plt.subplot(211)

plt.plot(year,male_obesity, color='b',label='Male')
plt.plot(year,female_obesity,color='r', label='Female')
plt.plot(year,both_genders, color='g', label='Both genders')


#Adding labels
plt.xlabel('Year')
plt.ylabel('Percent of population')
plt.title('Obesity rates in the US by gender from 1991-2014')
plt.legend(loc='lower right')


#######################################################################################
#Graph 2 showing depression stats in the US between 2009-2012 by age group
#######################################################################################

#Assign a variable to the data to plot from excel
data2 = pd.read_excel(r'C:\Users\Louise\Documents\NIH_docs\Python Scripts\depression_by_age.xlsx')

#Defining variables
age=data2['Age']
male_depression=data2['Male depression']
female_depression=data2['Female depression']
both_depression=data2['Both gender depression']

#Plotting graphs
plt.figure(1)
plt.subplot(212)

plt.plot(age,male_depression,color='b',label='Male')
plt.plot(age,female_depression, color='r', label='Female')
plt.plot(age,both_depression,color='g', label = 'Both genders')


#Adding labels
plt.xlabel('Age')
plt.ylabel('Percent of US population with depression')
plt.title('Depression rates in the US by gender between 2009-2012')
plt.legend(loc='upper right')
plt.show()
