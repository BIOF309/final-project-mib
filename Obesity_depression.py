##############################################################
#Graph 4 showing the prevalence of patients with BOTH depression and obesity
##############################################################

import numpy as np
import matplotlib.pyplot as plt

#Male stats in first subplot
plt.figure(1)
plt.subplot(211)

#Defining variables and groups with data
age_groupM=('20-39yrs w/ dep', '20-39yrs w/o dep', '40-59yrs w/ dep', '40-59yrs w/o dep', '60+yrs w/ dep', '60+yrs w/o dep')
y_height=np.arange(len(age_groupM))
depression_rateM = [30.9,29.4, 41.9, 36.9,46.6,35.1]

#Plotting the data in a bar graph
plt.bar(y_height,depression_rateM, align='center',alpha=0.75,color='b')
plt.xticks(y_height,age_groupM)
plt.ylabel('Percent of Population')
plt.title('Prevalence of Males with Depression and Obesity in the US by Age Group from 2005-2010')


#Female stats in second subplot
plt.figure(1)
plt.subplot(212)

#Defining variables with stats to plot
age_groupF=('20-39yrs w/ dep', '20-39yrs w/o dep', '40-59yrs w/ dep', '40-59yrs w/o dep', '60+yrs w/ dep', '60+yrs w/o dep')
y_height=np.arange(len(age_groupF))
depression_rateF = [45.3,30,49.2,37.6,46.6,36.6]

plt.bar(y_height,depression_rateF, align='center', alpha=0.75,color='r')
plt.xticks(y_height,age_groupF)
plt.ylabel('Percent of Population')
plt.title('Prevalence of Females with Depression and Obesity in the US by Age Group from 2005-2010')
plt.show()