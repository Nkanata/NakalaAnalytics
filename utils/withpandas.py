import pandas

df = pandas.read_csv('owid-covid-data.csv')
types = open('types.txt', 'w')
# df.info(verbose=True)
types.write(df.dtypes.to_string())
print(df.dtypes)
types.close()
