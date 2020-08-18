import pandas as pd

# Read String from file
f = open("my_text.txt", "r")
print(f"The string from the file is - {f.read()} \n")

# Pandas Dataframe
data = {
    "Year": [2020, 2020, 2020, 2020],
    "Quarter": [1, 2, 3, 4],
    "Revenue": [100, 200, 500, 600]
}
df = pd.DataFrame(data)

# Print Dataframe
print(df)
