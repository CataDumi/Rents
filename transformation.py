import pandas as pd
import csv



class Transformation():
    def __init__(self, name, dict):
        self.name = name
        with open(f'{name}.csv', 'w', encoding="utf-8") as file:
            file.write('Rent,Address\n')
            writer = csv.writer(file)
            for key, value in dict.items():

                if len(key) >= 4:
                    new_key = round(float(key) / 4.90 * 1000)
                    new_key = int(new_key)
                    writer.writerow([new_key, value])
                else:
                    key = int(key)
                    writer.writerow([key, value])

    def content(self):
        print(pd.read_csv(f'{self.name}.csv'))




# with open ('test.csv','w', encoding="utf-8") as file:
#     file.write('Rent,Address\n')
#     writer=csv.writer(file)
#     for key,value in dict.items():
#
#         if len(key)>=4:
#             new_key=round(float(key)/4.90*1000)
#             new_key=int(new_key)
#             writer.writerow([new_key, value])
#         else:
#             key=int(key)
#             writer.writerow([key, value])
#
# df=pd.read_csv('test.csv')
# print(df)