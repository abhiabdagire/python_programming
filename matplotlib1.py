from matplotlib import pyplot as plt
names = ["Abhijit", "Soham", "Dhiraj"]
marks = [80,85,90]
plt.subplot(1,3,1)
plt.bar(names, marks)
plt.subplot(1,3,2)
plt.scatter(names, marks)
plt.subplot(1,3,3)
plt.plot(names, marks)
plt.suptitle("Ploting Graphs in python")
plt.show()