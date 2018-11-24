
# Import modules
import pandas as pd

# Read colors data
colors = pd.read_csv('datasets/colors.csv')

# Print the first few rows
colors.head()


# How many distinct colors are available?
num_colors = len(colors)
print(num_colors)




# colors_summary: Distribution of colors based on transparency
colors_summary = colors.groupby('is_trans').count()
print(colors_summary)



get_ipython().magic('matplotlib inline')
# Read sets data as `sets`
sets = pd.read_csv('datasets/sets.csv')
# Create a summary of average number of parts by year: `parts_by_year`
parts_by_year = sets.groupby('year')['num_parts'].mean()

# Plot trends in average number of parts by year
import matplotlib.pyplot as plt
plt.plot(parts_by_year)
plt.show()


# themes_by_year: Number of themes shipped by year

import numpy as np
sets.drop(['set_num','name','num_parts'], axis=1)
themes_by_year = pd.DataFrame(sets.groupby('year').theme_id.nunique())
themes_by_year.set_index(np.arange(0,66), inplace=True)
themes_by_year['year'] = themes_by_year.index
themes_by_year

