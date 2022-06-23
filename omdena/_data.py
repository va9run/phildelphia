from omdena._library import *

def _datacollect():
    data = pd.read_parquet('C:/Users/v4run/omdena/phildelphia-1/omdena/traindata.parquet')
    return data