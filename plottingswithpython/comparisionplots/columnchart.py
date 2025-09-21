import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("C:\\Users\\venkatesh\\python-concepts\\plottingswithpython\\sales_data.xlsx")
plt.bar(df["Year"], df["Product_B_Sales"], color="orange")
plt.title("Product B Sales (Column Chart)")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()