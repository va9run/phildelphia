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
    facility = ['Commercial','Education','Food','Health','Industrial','Lodging','Multifamily','Office','Public_Assembly','Public_Safety','Retail','Service','Warehouse']
    facility1 = ['Parking','Laboratory','Nursing','Building','Data','Religious']
    categorytype = ['Commercial','Education','Food','Health','Industry','Lodging','Multifamily','Office','Public_area','Public_safety','Retail','Service','Warehouse']
    categorytype1 = ['Commercial','Health','Lodging','Multifamily','Office','Public_area']
    for i, j in zip(facility,categorytype):
        df.loc[df['facility_type'].str.contains(i,case=False), 'facility_type_1'] = j
    for i1, j1 in zip(facility1,categorytype1):
        df.loc[df['facility_type'].str.contains(i1,case=False), 'facility_type_1'] = j1
    df.fillna({'facility_type_1':'Multifamily'},inplace=True)
    return df

x = process()
x.info()
