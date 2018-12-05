#This code creates a bar graph for general mental health stats - all data referenced later

#############################################
#Graph 3 showing prevalence of any mental illness in the US in 2016
############################################

import matplotlib.pyplot as plt
import numpy as np

#Defining variables
demographics = ('Male', 'Female', '18-25yrs', '26-49yrs', '50+yrs')
y_height=np.arange(len(demographics))
prevalence = [4.8,8.5,10.9,7.4,4.8]

#Plotting graph
plt.bar(y_height,prevalence, align='center',alpha=0.75,color='g')

#Adding labels
plt.xticks(y_height,demographics)
plt.ylabel('Percent of population')
plt.title('Prevalence of any mental illness in the US in 2016')
plt.show()

