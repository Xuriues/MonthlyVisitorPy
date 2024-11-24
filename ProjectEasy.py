import pandas as pd
import matplotlib.pyplot as mp
Visitor = pd.read_excel("Int Monthly Visitor.xlsx", index_col = 0, na_values=" na ").fillna(0)
Visitor.index = pd.to_datetime(Visitor.index)
Visitor.columns = Visitor.columns.str.strip()
Count = Visitor.loc["1998 Jan":"2007 Dec", "Brunei Darussalam":"UAE"]
Both = Count.sum()
Both = pd.Series.sort_values(Both)
Both = Both.sort_values(ascending=True)
Both = Both.nlargest(3)
table = pd.DataFrame({"Countries" : [Both.index[0],Both.index[1],Both.index[2]],"Visitors": [Both[0],Both[1],Both[2]]})
print(table)
graph = table.plot.barh(x = 'Countries',y = 'Visitors')
mp.xlabel('',fontsize = 2)
mp.ylabel('Number Of Visitors', fontsize=10)
mp.title('Total Number Of Visitors')
mp.show()
