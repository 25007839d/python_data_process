import numpy as nm

a=nm.array([1,2,3,5,4])

# print(type(a))
# print(a)

# two type array single dim and multiple

#-------------------- zeros method to create 0 matrix

n1 = nm.zeros((5))
# print("single dim. array",n1)

n2 =nm.zeros((5,6))
# print("multi dim array",n2)

# -----------------full method for apply the value in matrix
n3 = nm.full((5,5),10)
# print(n3)

# ------------------arange for single diamention
n4 = nm.arange(2,10) # as like range
# print(n4)
n5 = nm.arange(5,50,5) # for continues secquencial gap
# print(n5)

# ---------------randome finction to generate value within
import numpy as np
rand = np.random.randint(1,100,10) # 1 to 100 need 10 random intiger change every time when run
# print(rand)

# -----------------shape function for change the dimention
ar = np.array([[1,3,4,5],[2,4,5,4]])
# print(ar)
# print(ar.shape)
ar.shape = (4,2) # first value represent column and second value represent column
# print(ar)

# stack function for join the array
n1 = np.array([1,3,2,5,6,5])
n2 = np.array([9,8,7,7,6,5])
v_stack =np.vstack((n1,n2)) # for vertical join
# print(v_stack)

hstack = np.hstack((n1,n2)) # for horizental join
# print(hstack)

column_stack= np.column_stack((n1,n2)) # for column wise join
# print(column_stack)


intersect1d = np.intersect1d(n1,n2) # to find comman data from two array
# print(intersect1d)

setdiff1d = np.setdiff1d(n1,n2) # to find left unique array value
# print(setdiff1d)

# ------------axis 0 = vertical(y), 1 =  horizental(x)

sum_array = np.sum([n1,n2])
# print(sum_array)

sum_array_0_axis = np.sum([n1,n2],axis=0)
# print(sum_array_0_axis)

sum_array_1_axis= np.sum([n1,n2],axis=1)
# print(sum_array_1_axis)



# -----------------numpy mathematical scaler operation

m1 =np.array([34,5,66,70])
# print(m1+5)
# print(m1-5)
# print(m1*5)
# print(m1/5)

# numpy math function
random = np.random.randint(1,100,7)
mean = np.mean(random)  # find the mean of array
# print(mean)

std = np.std(random)
# print(std)

median = np.median(random)
# print(median)

#----------------save and load array

np.save("random_val",random)

load_np_array=np.load("random_val.npy")
# print(load_np_array)


