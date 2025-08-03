import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(16,10))
ax.plot(x_values, y_values, linewidth=3)

# Set chart title and label axes.
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

plt.show()
