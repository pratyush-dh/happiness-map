import pandas as pd
import geopandas as gpd

df = pd.read_csv('happiness.csv')
gdf = gpd.read_file('countries.geojson')
gdf["geometry"] = gdf.simplify(0.05)

df_wide = df.pivot(index = ['Entity', 'Code'], columns = 'Year', values = 'Cantril ladder score')
df_wide = df_wide.reset_index()

merged = gdf.merge(df_wide, left_on = 'CNTRY_NAME', right_on = 'Entity', how  = 'left')

merged.drop(['OBJECTID', 'Entity', 'Code'], axis = 1, inplace = True)

merged.rename(columns = {2011: 'Y2011', 2014:'Y2014', 2015:'Y2015', 2016:'Y2016', 2017:'Y2017', 2018:'Y2018', 2019:'Y2019', 2020: 'Y2020', 2021:'Y2021', 2022:'Y2022'}, inplace = True)
 
merged['Rank2011'] = merged['Y2011'].rank(ascending = False)
merged['Rank2014'] = merged['Y2014'].rank(ascending = False)
merged['Rank2015'] = merged['Y2015'].rank(ascending = False)
merged['Rank2016'] = merged['Y2016'].rank(ascending = False)
merged['Rank2017'] = merged['Y2017'].rank(ascending = False)
merged['Rank2018'] = merged['Y2018'].rank(ascending = False)
merged['Rank2019'] = merged['Y2019'].rank(ascending = False)
merged['Rank2020'] = merged['Y2020'].rank(ascending = False)
merged['Rank2021'] = merged['Y2021'].rank(ascending = False)
merged['Rank2022'] = merged['Y2022'].rank(ascending = False)

merged.to_file('mgd.geojson')