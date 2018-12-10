# Loading of libraries:

# 1) Fuzzy matching libraries
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# 2) Libarary to import from excel
import pandas as pd


# Creating an export txt file:
# w - write from scratch (deletes everything in the file)
# a- append (adds new lines in the end of the file)
# The name of the output file needs to be changed.
print("Opening companies file")
Data_out = open("Comp_duplicates_match.txt", 'w',encoding='utf-8')

#
#print("Truncating...")
#Data_out.truncate()

# File names need to be changed
df_A = pd.read_excel("data_A.xlsx",encoding='utf-8')
df_B = pd.read_excel("data_B.xlsx",encoding='utf-8')

# The column name needs to be changed
df_A_list = df_A['Publisher'].tolist()
df_B_list = df_B['Publisher'].tolist()


for p in range(0,len(df_A_list)):
	# look for the 3 best matches from B
	result = process.extract(str(df_A_list[p]),choices=df_B_list, limit=3)
	# write the result
	Data_out.write(str(df_A_list[p])+"^"+str(result[0][0])+"^"+str(result[0][1])+"^"+str(result[1][0])+"^"+str(result[1][1])+"^"+str(result[2][0])+"^"+str(result[2][1]))
	# go to the next line
	Data_out.write("\n")
#	print(str(df_dx_list[p])+"^"+str(result[0])+"^"+str(result[1]))
	print(p)


print("Closing companies file")
Data_out.close()
