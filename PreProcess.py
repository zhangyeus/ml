"""try basic data preprocessing techniques"""

import numpy as np
import pandas as pd
    
def pre_process(filename):
    """step 1: read file"""
    dataset = pd.read_csv('Data.csv')
    X = dataset.iloc[ : , :-1].values
    Y = dataset.iloc[ : , 3].values  
    print(X)
    print(Y)
    """Step 2: handle null data"""

pre_process("Data.csv")
