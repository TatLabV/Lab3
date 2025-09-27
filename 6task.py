import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Создаем фигуру и оси
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)  #пределы оси X
ax.set_ylim(-1.5, 1.5)  #пределы оси Y
ax.set_title('Анимация sin(x)')  #заголовок
ax.set_xlabel('x')  #подпись оси X
ax.set_ylabel('sin(x)')  #подпись оси Y
ax.grid(True)  #сетка

#Инициализируем пустой график
line, = ax.plot([], [], 'b-') 

#Функция инициализации (пустая)
def init():
    line.set_data([], [])
    return line,

#Функция анимации для каждого кадра
def animate(i):
    x = np.linspace(0, 10, 200)  #200 точек от 0 до 10
    y = np.sin(x)  #вычисляем sin(x)
    
    #Берем только первые i точек
    x_data = x[:i]
    y_data = y[:i]
    
    #Обновляем данные графика
    line.set_data(x_data, y_data)
    return line,

#Создаем анимацию
ani = FuncAnimation(fig, animate, frames=200, 
                    init_func=init, blit=True, interval=20)

#Показать анимацию
plt.show()

