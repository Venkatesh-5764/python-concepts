import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("C:\\Users\\venkatesh\\python-concepts\\plottingswithpython\\sales_data.xlsx")

plt.bar(df["Year"], df["Product_A_Sales"], label="Product A")
plt.bar(df["Year"], df["Product_B_Sales"], bottom=df["Product_A_Sales"], label="Product B")
plt.bar(df["Year"], df["Product_C_Sales"], bottom=df["Product_A_Sales"] + df["Product_B_Sales"], label="Product C")
plt.title("Stacked Bar Chart")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.legend()
plt.show()