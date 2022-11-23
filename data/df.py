import pandas as pd

df = pd.read_csv('충청북도.csv')
print(df)
print(df[df['4'] == '대성로'])
# df_sample = df.iloc[:,[2,3,4,5,10]]

# df_sample.loc[0] = ['강원도','춘천시','봉의동','0','중앙로']
# print(df_sample)
# df_sample2 = df_sample.drop_duplicates()
# print(df_sample2)
# df_sample2.columns = ['0','1','2','3','4']
# print(df_sample2)
# df_sample2.to_csv('충청북도.csv')
# print(df_sample2)
# df_sample2.to_csv('충북.csv')