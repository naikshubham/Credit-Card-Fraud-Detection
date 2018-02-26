import pandas as pd
import cmath
import numpy as np
cc = pd.read_csv('creditcard.csv')

#Create Numpy array f_arr of all the transcations
f_arr =np.array(cc)

# Enter the transcation index value corresponding to which you need to find similar transcations #n
n = int(input("Enter a trancation index value corresponding to which you need to find similar trancations :"))
l_data = []  #array to store similarity values
l_index=[]   #array to store indexes of similarity values
l_class=[]   #array to store class values 
for i in range(0,len(f_arr)):
        numerator = np.dot(f_arr[n],f_arr[i])     #computing dot product #numertor dot product (vi, vj)
        sqa= np.square(f_arr[n])                  #computing square to find length(vi)
        sqb= np.square(f_arr[i])                  #computing square to find length(vj)
        sum_a=np.sum(sqa)                         #sum up the squared values
        sum_b=np.sum(sqb)                         #sum up the squared values
        da = np.sqrt(sum_a)                       #take sqrt of the sum of squared values #length(vi)
        db = np.sqrt(sum_b)                       #take sqrt of the sum of squared values #length(vj)
        denominator = da * db                     #denominator length(vi) * length(vj)
        value = numerator/denominator             #similarity(i,j) value
        fvalue = cmath.acos(value)                 #taking inverse cosine
        l_data.append(fvalue)                     #appending similarity values to l_data
        l_index.append(i)                         #appending index values to l_index
        l_class.append(cc['Class'][i])            #appending class values to l_class

f_res = pd.DataFrame({'Similarity':l_data,'Index':l_index,'Class':l_class})  #create DF with columns 'Similarity','Index','Class'
f_sorted = f_res.sort_values('Similarity',axis =0,ascending=True)            #Sort the DF to get top 10 transactions in the dataset which have the lowest similarity(i,j).
print(f_sorted.head(10))                                                     #top 10 lowest similar values  
print('--------------------\n')
print('Given transcation id :',n,'Class:',f_res['Class'][n])
print('--------------------------------------\n Similar transcations\n ---------------------------\n')
for i in range(0,10):
     print('Class:',f_res['Class'][f_sorted.index[i]],'Similarity = ',f_sorted['Similarity'][f_sorted.index[i]] ,'#trancation id = ',f_sorted.index[i])
	 
#Sample Output
'''
Enter a trancation index value corresponding to which you need to find similar trancations :541
      Class  Index            Similarity
541       1    541                   -0j
460       0    460  (0.0166922986392-0j)
8296      1   8296  (0.0216110277492-0j)
8615      1   8615  (0.0217160642217-0j)
9035      1   9035   (0.021940381583-0j)
8335      1   8335  (0.0219718650971-0j)
9252      1   9252  (0.0220768521941-0j)
9487      1   9487  (0.0222108920308-0j)
9509      1   9509  (0.0222138461766-0j)
9179      1   9179  (0.0223664265243-0j)
--------------------

Given transcation id : 541 Class: 1
--------------------------------------
 Similar transcations
 ---------------------------

Class: 1 Similarity =  -0j #trancation id =  541
Class: 0 Similarity =  (0.0166922986392-0j) #trancation id =  460
Class: 1 Similarity =  (0.0216110277492-0j) #trancation id =  8296
Class: 1 Similarity =  (0.0217160642217-0j) #trancation id =  8615
Class: 1 Similarity =  (0.021940381583-0j) #trancation id =  9035
Class: 1 Similarity =  (0.0219718650971-0j) #trancation id =  8335
Class: 1 Similarity =  (0.0220768521941-0j) #trancation id =  9252
Class: 1 Similarity =  (0.0222108920308-0j) #trancation id =  9487
Class: 1 Similarity =  (0.0222138461766-0j) #trancation id =  9509
Class: 1 Similarity =  (0.0223664265243-0j) #trancation id =  9179
'''