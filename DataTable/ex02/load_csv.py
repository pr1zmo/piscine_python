import pandas as pd
import numpy as np

def load(path: str):
   fl = pd.read_csv(path)
   return (fl)