import matplotlib.pyplot as plt
import numpy as np
d = []
s = []

type_ax = int(
    input("Выберите тип графика: \n 1)y=x^2 \n 2)y=kx+b \n 3)Свой  \n"))
# if(type_ax==1)

# if (type_ax == 3)
if type_ax == 3:
    abciss = str(input("Значение по оси х:"))
    ordinata = str(input("Значение по оси y:"))

    data_x = int(input("Введите колво точек:"))

    data_x = int(input("Введите колво точек:"))

    data_y = data_x

while data_x > 0:
    s.append(int(input("Введите значение x:")))
    data_x -= 1
while data_y > 0:
    d.append(int(input("Введите значение y:")))
    data_y -= 1
y = np.array(d)
x = np.array(s)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.xlabel(abciss)
plt.ylabel(ordinata)
plt.title("Physics graphic")
plt.show()
