import pandas as pd
import numpy as np

def load(path: str):
   fl = pd.read_csv(path)
   array = np.asarray(fl.to_numpy)
   # print(array.size)
   return (array)