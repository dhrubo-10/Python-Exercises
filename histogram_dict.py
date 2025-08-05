import matplotlib
matplotlib.use('TkAgg')  # Force interactive backend

import matplotlib.pyplot as plt

names = ["A", "B", "C", "D", "E", "F", "A", "E", "E", "A", "C", "C", "C", "A", "A"]

# Count frequencies
d = dict()
for name in names:
    d[name] = d.get(name, 0) + 1

# Plot histogram
plt.bar(d.keys(), d.values(), color='skyblue')
plt.xlabel('Names')
plt.ylabel('Frequency')
plt.title('Name Frequency Histogram')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
