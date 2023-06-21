#!/usr/bin/env python
# coding: utf-8

# In[32]:


#Using NumPy create random vector of size 15 having only Integers in the range 1-20.

import numpy as np    #importing numpy module
a = np.random.randint(1,21,15)      #np.random imports random function and randint method creates a array of size 15 elements varying between 1 to 20. 
a  #print


# In[33]:


#Using NumPy create random vector of size 15 having only Integers in the range 1-20.

import numpy as np    #importing numpy module
a = np.random.randint(1,21,15)      #np.random imports random function and randint method creates a array of size 15 elements varying between 1 to 20. 
a  #print


# In[34]:


#Print array shape.
a2.shape 


# In[35]:


#Replace the max in each row by 0
a3 = np.where(a2 == a2.max(axis=1)[:,None], 0, a2)    
a3


# In[ ]:





# In[36]:


#Write a program to compute the eigenvalues and right eigenvectors of a given square array given below:
#[[ 3 -2],[ 1 0]]
import numpy as np # importing numpy module 
m=np.array([[3,-2],
           [1,0]])
ev, rev = np.linalg.eig(m) # eigen value(ev),right eigen value(rev)
print("eigen value",ev) #print eigen value
print("right eigen values",rev) #print right eigen value


# In[37]:


#Compute the sum of the diagonal element of a given array.
#[[0 1 2],[3 4 5]]

import numpy as np # importing numpy module 
m=np.array([[0,1,2],
           [3,4,5]])
trace=np.trace(m)  #calculating the trace of matrix
trace  #printing the trace


# In[38]:


#Write a NumPy program to create a new shape to an array without changing its data.
#Reshape 3x2:
#[[1 2],[3 4],[5 6]]
#Reshape 2x3:
#[[1 2 3],[4 5 6]]

import numpy as np # importing numpy module 
m1=np.array([[1,2],
           [3,4],
           [5,6]])   
reshaped_array1=np.reshape(m1,(2,3)) #reshaping the array 1
m2=np.array([[1,2,3],
            [4,5,6]])
reshaped_array2 = np.reshape(m2,(3,2))  #reshapping the array 2
print("reshaped array1=",reshaped_array1)
print("reshaped array2=",reshaped_array2)




# In[39]:


#Write a Python programming to create a below chart of the popularity of programming Languages.
#Sample data:
#Programming languages: Java, Python, PHP, JavaScript, C#, C++
#Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7


import matplotlib.pyplot as plot  #importing matplotlib to plot in pie chart
prog_languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']   #labels 
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]   
explode = (0.2, 0, 0, 0,0,0)  #explode to highlight the specific wedge.
plot.pie(popularity, labels=prog_languages, autopct='%1.1f%%', shadow=True, explode=explode, startangle=140)
#plot.pie to plot the pie chart 
plot.axis('equal')
plot.show()


# In[ ]:




