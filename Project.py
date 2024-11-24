import pandas as pd
import matplotlib.pyplot as mp
years = [[' 1978 Jan ',' 1987 Dec '],[' 1988 Jan ',' 1997 Dec '],[' 1998 Jan ',' 2007 Dec '],[' 2008 Jan ',' 2017 Nov ']]
countries = [[' Brunei Darussalam ',' UAE '],[' United Kingdom ',' CIS & Eastern Europe '],[' USA ',' Africa ']]
class Data:
    country = 0
    year = 0
    def __init__(self):
        self.printing()
        self.getData()
    def getData(self):
        excel = pd.read_excel('Int Monthly Visitor.xlsx')
        excel.index = excel['   ']
        del excel['   ']
        print(years[self.year][0],"To",(years[self.year] [1]))
        excel = excel.loc[years[self.year][0]:years[self.year][1],countries[self.country][0]:countries[self.country][1]]
        excel = excel.replace(to_replace = ' na ',value = 0)
        excel_2 = excel.sum(skipna=True)
        excel_2 = pd.Series.sort_values(excel_2)
        excel_2 = excel_2.sort_values(ascending=False)
        excel_2 = excel_2.nlargest(3)
        table = pd.DataFrame({'Countries':[excel_2.index[0],excel_2.index[1],excel_2.index[2]],'Visitors':[excel_2[0],excel_2[1],excel_2[2]]})
        print(table)
        self.graphs(table)
    def graphs(self,table):
        graph = table.plot.barh(figsize=(20,5),x = 'Countries',y = 'Visitors', rot = 0)
        mp.xlabel('',fontsize = 2)
        mp.ylabel('Number Of Visitors', fontsize=10)
        mp.title('Total Number Of Visitors')
        mp.show()
    def printing(self):
        while(True):
            print("1 = Asia")
            print("2 = Europe")
            print("3 = Others")
            try:
                self.country = int(input("Please Pick Continental(1-3)"))-1
                if(self.country < 3):
                    break
                print("Numbers from 1 to 3 ONLY")
            except ValueError:
                print("Please pick a Number")
        while(True):
                print("1 = 1978 - 1987")
                print("2 = 1988 - 1997")
                print("3 = 1998 - 2007")
                print("4 = 2008 - 2017")
                try:
                    self.year = int(input("Please Pick a Year"))-1
                    if(self.year < 4):
                        break
                    print("Numbers from 1 to 3 ONLY")
                except ValueError:
                    print("Please pick a number between 1 and 3")

trial = Data()
