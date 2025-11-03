import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def life():
	# 1) Load the CSV file into a DataFrame
	fl = pd.read_csv("life_expectancy_years.csv")
	# → Reads your CSV into a pandas DataFrame called 'fl'
	#   Each column becomes a labeled Series (e.g., years),
	#   and the first column (countries) contains the country names.

	# 2) Set the first column (country names) as the index
	fl = fl.set_index(fl.columns[0])
	# → The first column is now the DataFrame index.
	#   This allows easy lookup by country name, like fl.loc["France"]

	# 3) Extract the row for France
	fr = fl.loc["France"]
	# → Selects the data for 'France' as a pandas Series,
	#   where the index are years (like '1800', '1801', ...).

	# 4) Convert the index (year labels) from strings to integers
	fr.index = fr.index.astype(int)
	# → Ensures that the years are treated as numeric values
	#   instead of text, which allows numeric plotting on the x-axis.

	# 5) Sort the index just in case it’s unordered
	fr = fr.sort_index()
	# → Makes sure the years go from smallest to largest.

	# 6) Plot France’s life expectancy
	ax = fr.plot(
		title="France Life expectancy Projections",  # chart title
		ylabel="Life expectancy"                     # label for y-axis
	)
	# → Creates a line plot of life expectancy over years.
	#   Returns the Matplotlib Axes object for further customization.

	# 7) Label the x-axis
	ax.set_xlabel("Year")
	# → Adds a label under the x-axis.

	# 8) Set the number of x-axis ticks and force them to be integers
	ax.xaxis.set_major_locator(MaxNLocator(nbins=9, integer=True))
	# → Limits the number of x-axis ticks to ~8 evenly spaced ones.
	#   Ensures they are shown as whole years (no decimals).

	# 9) Adjust layout to prevent label overlap
	plt.tight_layout()
	# → Automatically adjusts spacing so labels and titles fit nicely.

	# 10) Show the final plot
	plt.show()
	# → Displays the graph window.
