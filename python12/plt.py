import matplotlib.pyplot as plt

# Create some data
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 21]# Create a plot
plt.plot(x,y)

# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Plot')

# Display the plot
plt.show()