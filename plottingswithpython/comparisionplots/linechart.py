import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("C:\\Users\\venkatesh\\python-concepts\\plottingswithpython\\sales_data.xlsx")

plt.plot(df["Year"], df["Product_A_Sales"], marker="o", label="Product A")
plt.plot(df["Year"], df["Product_B_Sales"], marker="o", label="Product B")
plt.plot(df["Year"], df["Product_C_Sales"], marker="o", label="Product C")
plt.title("Line Chart of Sales")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend()
plt.show()