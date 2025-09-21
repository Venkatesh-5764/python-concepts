import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("C:\\Users\\venkatesh\\python-concepts\\plottingswithpython\\sales_data.xlsx")
print(df)
plt.bar(abs(df["Year"]), df["Product_A_Sales"])
plt.title("Product A Sales (Bar Chart)")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()