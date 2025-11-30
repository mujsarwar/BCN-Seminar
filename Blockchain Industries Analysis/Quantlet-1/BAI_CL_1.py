


# Example main code script
import numpy  as np

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print("\n\n")

# Load the CSV now that it's on the server
df = pd.read_csv("bcn.csv")
print("\n\n")
print(df.head())
print("\n\n")
print(df.isna().sum())
print("\n\n")
print(df.info())


#-------------------------------------
cols_to_remove = {
    "Transaction ID",
    "Item ID",
    "Supplier ID",
    "Customer ID",
    "GPS Coordinates",
    "Transaction Hash"
}
existing_cols = list(set(df.columns) & cols_to_remove)
df.drop(existing_cols, axis=1, inplace=True)
print("\n\n")
print(df.head())


#-------------------------------------

print("\n\n")
print(df.head())

#-------------------------------------
# Load your dataset
df = pd.read_csv("bcn.csv")

# Convert the original timestamp column to datetime format
df['OrderDateTime'] = pd.to_datetime(df['Timestamp'])

# Create new features based on the datetime
df['Weekday_Num'] = df['OrderDateTime'].dt.weekday  # 0 = Monday, 6 = Sunday
df['Month_Num'] = df['OrderDateTime'].dt.month
df['Year_Num'] = df['OrderDateTime'].dt.year

# Calculate the time difference in seconds between consecutive orders
df['TimeGap_Seconds'] = df['OrderDateTime'].diff().dt.total_seconds()

# Remove the original timestamp column and the time gap helper column
df.drop(columns=['Timestamp', 'TimeGap_Seconds'], inplace=True)

# Display the first few rows of the updated DataFrame
print("\n\n")
print(df.head())

#-------------------------------------
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
print("\n\n")

# Load your dataset
df = pd.read_csv("bcn.csv")

# List of categorical columns to encode
categorical_cols = ["Smart Contract Status", "Order Status", "Payment Status"]

# Keep only columns that exist in the DataFrame
existing_categorical_cols = [col for col in categorical_cols if col in df.columns]

# Convert categorical columns into numerical dummy variables
df = pd.get_dummies(df, columns=existing_categorical_cols, drop_first=False)

# Display the updated DataFrame
print("\n\n")
print(df.head())

#-------------------------------------
gp=df.groupby("Location")[["Order Amount", "Quantity Shipped", "Quantity Mismatch"]].mean()
print("\n\n")
print(gp)

#-------------------------------------
print("\n\n")
print(df[df["Fraud Indicator"] == 1].groupby("Location")[["Order Amount",
                                                          "Quantity Mismatch"]].mean())

print("\n\nThis is an Example of a Quantlet")
print("\n\nThat was easy?")
print("\n\nThat was never easy!")

print("\n\nThat was easy?")
print("\n\nThat was never easy!")
print("\n\nshit happensy!")
print("\n\nshit !")