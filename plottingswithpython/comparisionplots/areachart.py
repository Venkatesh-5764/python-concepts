import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("C:\\Users\\venkatesh\\python-concepts\\plottingswithpython\\sales_data.xlsx")

plt.stackplot(df["Year"], df["Product_A_Sales"], df["Product_B_Sales"], df["Product_C_Sales"], 
              labels=["Product A", "Product B", "Product C"], alpha=0.8)
plt.title("Area Chart of Sales")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend()
plt.show()