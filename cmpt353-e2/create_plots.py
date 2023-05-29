import sys
import pandas as pd
import matplotlib.pyplot as plt

# Check if the correct number of command line arguments are provided
if len(sys.argv) != 3:
    print("Please provide two text files as command line arguments.")
    sys.exit(1)

# Get the filenames from command line arguments
file1 = sys.argv[1]
file2 = sys.argv[2]

# Read data from the text files using pandas
data1 = pd.read_csv(file1, delimiter=' ', header=None, names=['lang', 'page', 'views', 'bytes'])
data2 = pd.read_csv(file2, delimiter=' ', header=None, names=['lang', 'page', 'views', 'bytes'])

# For Plot 1
sorted_data1 = data1.sort_values('views', ascending=False)

# For Plot 2
merged_df = pd.merge(data1, data2, left_index=True, right_index=True)

# Create plt
plt.figure(figsize=(10, 5)) # change the size to something sensible

# Plot 1
plt.subplot(1, 2, 1) # subplots in 1 row, 2 columns, select the first

plt.plot(sorted_data1["views"].values) # build plot 1

plt.title('Popularity Distribution')
plt.xlabel('Rank')
plt.ylabel('Views')

# Plot 2
plt.subplot(1, 2, 2) # ... and then select the second

plt.scatter(merged_df["views_x"], merged_df["views_y"])

# Set log-scale on both axes
plt.xscale('log')
plt.yscale('log')

# Set axis labels and title
plt.title('Hourly Correlation')
plt.xlabel('Hour 1 Views')
plt.ylabel('Hour 2 Views')

plt.savefig('wikipedia.png')
