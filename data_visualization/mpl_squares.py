import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn-v0_8-dark')
# tuple unpacking
# result = plt.subplots() then fig = result[0] and ax = result[1]
# subplots function can generate one or more plots in the same figure
# the variable figure represents the entire figure (collection of plots that are generated)
# ax represents a single plot in the figure
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()