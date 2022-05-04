import matplotlib.pyplot as plt
from data import make_x_and_y

x, y = make_x_and_y(n=100)

fig, ax = plt.subplots()
ax.scatter(x, y)
fig
