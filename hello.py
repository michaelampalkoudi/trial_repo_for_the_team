print("Hello, Georgia here")

print('this is a stupid futile try')

print('to add my git code')

print('to our playground')

# import required modules
import pandas as pd
import numpy as np

# create dataset
df = pd.DataFrame({'Temperature': ['Hot', 'Cold', 'Warm', 'Cold'],
				})

# display dataset
print(df)

# create dummy variables
pd.get_dummies(df)
