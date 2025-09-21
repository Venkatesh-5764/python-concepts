import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("C:\\Users\\venkatesh\\python-concepts\\plottingswithpython\\sales_data.xlsx")

x = range(len(df["Year"]))
plt.bar([i - 0.2 for i in x], df["Product_A_Sales"], width=0.2, label="Product A")
plt.bar(x, df["Product_B_Sales"], width=0.2, label="Product B")
plt.bar([i + 0.2 for i in x], df["Product_C_Sales"], width=0.2, label="Product C")
plt.xticks(x, df["Year"])
plt.title("Grouped Bar Chart")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend()
plt.show()