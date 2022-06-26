from omdena._library import *
from omdena._data import _datacollect

def process():
    df = _datacollect()
    # Fix Numerical variables
    df['Year_Factor'] = df['Year_Factor'].astype('category')
    df['year_built'].replace(0,np.nan,inplace=True)
    df.drop(['id','days_below_0F', 'days_above_100F', 'days_above_110F'],axis=1,inplace=True)
    df.dropna(subset=['year_built'],axis=0,inplace=True)
    df['year_built'] = df['year_built'].astype('int64')
    
    # Fix Categorical variable
    df[['State_Factor','building_class','facility_type']] = df[['State_Factor','building_class','facility_type']].astype('category')
    facility = []
    return df

x = process()
x.info()