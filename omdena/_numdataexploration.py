from  omdena._library import *
from omdena._data import _datacollect


numtrain = _datacollect()
numtraindata = numtrain.select_dtypes('number')
numtraindata.head()

numtraindata.nunique()

# These are few factors which has very few unique value in whole dataset
numtraindata['Year_Factor'].unique()
numtraindata['days_above_110F'].unique()
numtraindata['year_built'].unique()
numtraindata['year_built'].value_counts()

# We have to handle or change Year Factor to categorical variable because it is the year in which data had been collected so it makes more sense for it to be a categorical
numtraindata['Year_Factor'] = numtraindata['Year_Factor'].astype('category')

# Basic statistical analysis
numtraindata.describe().T
# Flags from statistical analysis:
# 1) year_built has minimum value 0 which can't be because it is an year data and year can't be 0
# 2) days_below _0F, days_above_100 and 110F has most data as 0 (Drop these columns)
# 3) direction_max_wind_speed, direction_peak_wind_speed and max_wind_speed has most data as 1 where as first two looks more skewed data 
# 4) year_built is in float data type
# 5) missing factors :
    # a) year_built
    # b) energy_star_rating
    # c) direction_max_wind_speed
    # d) direction_peak_wind_speed
    # e) max_wind_speed
    # f) days_with_fog

# Fix the issues from the top of the flag list
numtraindata['year_built'].replace(0,np.nan,inplace=True)
numtraindata.drop(['days_below_0F', 'days_above_100F', 'days_above_110F'],axis=1,inplace=True)
numtraindata.info()

# Null columns
nullcolumns = numtraindata.columns[numtraindata.isna().any()].to_list()

def missingpattern(col):
    viz = mno.matrix(numtraindata[col])
    return viz



data = numtraindata[nullcolumns].isna()
fig = px.imshow(data)
fig.show()

# Things to notice:
# 1) direction_max_wind_speed, direction_peak_wind_speed and max_wind_speed have missing values from same spot
    # Reason could be malfunction of instrument
