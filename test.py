import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')

# Read the CSV file
df = pd.read_csv("gender_submission.csv")

# Check if the data is read correctly
print(df.head())

# Extract data
x = df['PassengerId']
y = df['Survived']

# Plot the scatter graph
plt.figure(figsize=(10, 6))  # Optional: Adjust figure size
plt.scatter(x, y, color='green', edgecolor='black', s=100, alpha=0.7)  # Customize scatter points
plt.xlabel('PassengerId', fontsize=18)
plt.ylabel('Survived', fontsize=16)
plt.title('Passenger Survival Data (Scatter Plot)', fontsize=20)
plt.grid(True)  # Optional: Add grid lines
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()  # Adjust layout to prevent clipping

# Show the plot
plt.show()
