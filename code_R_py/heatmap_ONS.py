'''
Business Contingency Plan script for wrongpipeline isolates
Adam Crewdson April 2023

'''

#imports

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



csv_file = r'/home/phe.gov.uk/adam.crewdson/Downloads/ONS_course/DS4Policy_10/clean_IOT_data.csv'

csv_data = pd.read_csv(csv_file)
csv_data = csv_data.fillna(0)

#print(csv_data)

lol_new_data = []

for index,row in csv_data.iterrows():
	#per_row_list = []
	#per_row_list.append(str(row['industries_clean']))

	for col in csv_data.columns:
		per_col_list = []
		per_col_list.append(str(row['industries_clean']))
		if(col != 'industries_clean' and col != 'total'):
			mutated_by_total = round(int(row[col]) / int(row['total']), 5)
			#mutated_by_total = int(row[col]) / int(row['total'])
			per_col_list.append(str(col))
			per_col_list.append(mutated_by_total)


		lol_new_data.append(per_col_list)

print(lol_new_data)


#column_list = [col for col in csv_data.columns if col != 'total']

#print(len(column_list))

mutated_df = pd.DataFrame.from_records(lol_new_data, columns =['Input','Output','Value'])
print(mutated_df)

df_pivot = mutated_df.pivot_table(index='Input', columns='Output', values='Value')

sns.set(font_scale=0.5)
#sns.color_palette("Blues", as_cmap=True)
sns.heatmap(df_pivot,xticklabels=True, yticklabels=True, cmap='Blues')

plt.show()

