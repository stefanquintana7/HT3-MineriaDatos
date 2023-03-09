import pandas as pd
from pandas_profiling import ProfileReport

datos = pd.read_csv('C:\\Stefan\\MineriaDatos\\train.csv')

profile = ProfileReport(datos, title="Pandas Profiling Report")