import os
import pandas as pd 

# print(os.path.abspath(__file__))
file_folder = os.path.dirname(__file__) # misc
machine_learning_folder = os.path.dirname(file_folder) # machine-learning-AI22

data_folder = os.path.join(machine_learning_folder, "data") # machine-learning-AI22/data


df = pd.DataFrame([1,2,3,4])

print(df)



print(data_folder)

df.to_csv(os.path.join(data_folder, "test.csv"))

# print(os.path.abspath(""))