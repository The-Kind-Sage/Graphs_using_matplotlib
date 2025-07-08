import matplotlib.pyplot as plt

N = [100, 1000, 5000, 10000, 50000, 100000]
quick = [50, 400, 2500, 6000, 40000, 90000]   
merge = [60, 500, 3000, 7000, 45000, 100000]  

plt.plot(N, quick, marker='o', label='Quick Sort')
plt.plot(N, merge, marker='s', label='Merge Sort')
plt.xlabel('Input Size (N)')
plt.ylabel('Time (microseconds)')
plt.title('Sorting Runtime vs Input Size')
plt.legend()
plt.xscale('log')
plt.yscale('log')
plt.grid(True)
plt.show()