from omdena._data import _datacollect
from omdena._library import *

def _dataexploration():
    train = _datacollect()
    return train

targetvariable = 'site_eui'

# Basic Data Explore
trainexplore = _dataexploration()

# Look the the number of columns and rows
trainexplore.shape # 75757 * 64

# Basic info about the columns
trainexplore.info()

trainexplore.head(10)
# There are 3 categorical Variables 
# 1) State_Factor
# 2) Building_Class
# 3) Facility_Type

# Explore Unique Values in Categorical data

def uniquevalue(col):
    print("Unique: ", trainexplore[col].nunique()) # & unique values
    print("Unique Values: ", trainexplore[col].unique().tolist())

# State_Factor
uniquevalue('State_Factor')
# Names >>>>> 
# 1) State_1
# 2) State_2
# 3) State_4
# 4) State_6
# 5) State_8
# 6) State_10
# 7) State_11

# Building_Class
uniquevalue('building_class') # 2 Unique Types
# 1) Commercial
# 2) Residential

# Facility Type
uniquevalue('facility_type')
# 60 different types

# Data Count
def datacount(col):
    valuec = trainexplore[col].value_counts().reset_index()
    valuec.rename(columns={'index':'Category',col:'Count'},inplace=True)
    valuec['countper'] = round((valuec['Count']/trainexplore.shape[0])*100,2)
    return valuec

# Building Class
datacount('building_class')

# State_Factor
datacount('State_Factor')

# Facility Type
datacount('facility_type')