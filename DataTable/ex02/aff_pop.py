from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def aff(path: str):
   pd = load(path)
   pd = pd.set_index(pd.columns[0])
   ma = pd.loc["Morocco"]
   po = pd.loc["Portugal"]
   
   ma = ma.astype(int)
   po = po.astype(int)
   
   ax = ma.plot(
		title="Population Projections",
		ylabel="Population"
	)
   ax.set_xlabel("Year")
   ax.xaxis.set_major_locator(MaxNLocator(nbins=8, integer=True))
   plt.tight_layout()
   plt.show()
   
   return(pd)