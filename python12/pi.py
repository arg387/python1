import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [130.677, 725.779, 20, 25]  # Sizes or proportions for each category

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# Set a title
plt.title('Pie Chart Example')

# Display the chart
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
plt.show()