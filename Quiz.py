import numpy as np
import pandas as pd
import random
filename = 'input.csv'
data = pd.DataFrame(data = pd.read_csv(filename))
options = np.array(data.iloc[:,1:-1])
ans = np.array(data.iloc[:,-1])
ques = np.array(data.iloc[:,0])
no=random.sample(range(5),2)
val=0
no=random.sample(range(5),2)
for i in no:
    print(ques[i])
    for j, option in enumerate(options[i]):
        print(j+1, option)
    answer=int(input("Enter your option\n"))
    if answer==ans[i]:
        val+=1
        print("Correct\n")
    else:
        print("Wrong\n")
print(f"Score={val}\n")