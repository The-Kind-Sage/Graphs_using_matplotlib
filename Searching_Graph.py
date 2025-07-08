import matplotlib.pyplot as plt

N = [100, 1000, 5000, 10000, 50000, 100000]
binary = [0, 0, 1, 1, 2, 2]  
expo = [0, 0, 1, 1, 2, 2]    

plt.plot(N, binary, marker='o', label='Binary Search')
plt.plot(N, expo, marker='s', label='Exponential Search')
plt.xlabel('Input Size (N)')
plt.ylabel('Time (microseconds)')
plt.title('Runtime vs Input Size')
plt.legend()
plt.xscale('log')
plt.grid(True)
plt.show()