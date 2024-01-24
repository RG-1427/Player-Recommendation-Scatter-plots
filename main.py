import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

#shots vs xg - takes shots from dangerous places
data = pd.read_csv('Search results.csv')
data.columns = ["V"+str(i) for i in range(1, len(data.columns)+1)]
sns.lmplot(x="V10", y="V44", data=data, hue="V2", fit_reg=False)
plt.show()

#shots vs goal conversion - converts shots into goals
data.columns = ["V"+str(i) for i in range(1, len(data.columns)+1)]
sns.lmplot(x="V44", y="V46", data=data, hue="V2", fit_reg=False)
plt.show()

#xg vs touches in opposition area - creating chances by entering opp area
data.columns = ["V"+str(i) for i in range(1, len(data.columns)+1)]
sns.lmplot(x="V10", y="V59", data=data, hue="V2", fit_reg=False)
plt.show()

#non penalty goals vs assists - involvement in goals
data.columns = ["V"+str(i) for i in range(1, len(data.columns)+1)]
sns.lmplot(x="V39", y="V47", data=data, hue="V2", fit_reg=False)
plt.show()

#dinterception vs duels - defensive involvement
data.columns = ["V"+str(i) for i in range(1, len(data.columns)+1)]
sns.lmplot(x="V29", y="V23", data=data, hue="V2", fit_reg=False)
plt.show()

#key passes vs crosses - chance creation
data.columns = ["V"+str(i) for i in range(1, len(data.columns)+1)]
sns.lmplot(x="V85", y="V48", data=data, hue="V2", fit_reg=False)
plt.show()

