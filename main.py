import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame for the processes
processes = {
    'Process': ['A','B','C','D','E','F','G','A','B','C'],
    'Start': [0,6,12,18,24,30,36,42,48,54],
    'End': [5,11,17,23,29,35,41,47,53,59]
}
df = pd.DataFrame(processes)

# Define a color map for the processes
color_map = {
    'A': 'red',
    'B': 'orange',
    'C': 'yellow',
    'D': 'green',
    'E': 'cyan',
    'F': 'blue',
    'G': 'purple'
}

# FILEPATH: /d:/CODES/jupyter/123.ipynb

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each process as a horizontal bar with the same color for the same process
for index, row in df.iterrows():
    ax.barh(row['Process'], row['End'] - row['Start'], left=row['Start'], color=color_map[row['Process']])

# Set labels and title
ax.set_xlabel('Time')
ax.set_ylabel('Processes')
ax.set_title('Round Robin Gantt Chart of Processes')

# Show the plot
plt.show()