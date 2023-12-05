import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('/content/marine debris remote sensing with year.csv')
plt.hist(df['Depth'],color=['black'],ec='red')
plt.xlabel('ItemName',color='green')
plt.ylabel('Depth',color='green')
plt.title('DEPTH OF THE ITEM',color='blue')
plt.show()



import matplotlib.pyplot as plt
import pandas as pd
df2=pd.read_csv('/content/marine debris remote sensing with year.csv')
df2=df2.head(25)
plt.bar(df2['Location'],df2['Quantity'],color=['orange','black','green'],label='Bar')
plt.xlabel('Location',color='blue')
plt.ylabel('Quantity',color='blue')
plt.legend()
plt.title('LOCATION OF THE QUANTITY',color='magenta')
plt.xticks(rotation=90)
plt.show()



import matplotlib.pyplot as plt
import pandas as pd
df3=pd.read_csv('/content/marine debris remote sensing with year.csv')
df3=df3.head(50)
plt.scatter(df3['Material Description'],df3['ItemName'],marker='D',color='red',label='scatter')
plt.xlabel('Item',color='red')
plt.ylabel('Item Type',color='red')
plt.legend()
plt.title('ITEM ACCORDING TO ITS TYPE',color='purple')
plt.xticks(rotation=90)
plt.show()


  
import matplotlib.pyplot as plt
import pandas as pd
df4=pd.read_csv('/content/marine debris remote sensing with year.csv')
df4=df4.head(25)
plt.plot(df4['Latitude'],df4['Longitude'],color='purple',label='line')
plt.xlabel('Latitude',color='red')
plt.ylabel('Longitude',color='red')
plt.title('LATITUDE VS LONGITUDE',color='green')
plt.legend()
plt.xticks(rotation=90)
plt.show()
