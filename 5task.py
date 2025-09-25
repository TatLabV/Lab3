import numpy as np
import matplotlib.pyplot as plt

# Создаем фигуру с 3 областями (1 строка, 3 столбца)
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

#  Первый график: y = x^2 
x = np.linspace(0, 5, 50)  # 50 точек от 0 до 5
y = x ** 2  # квадрат x

axs[0].plot(x, y, 'r-')  # красная сплошная линия
axs[0].set_title('Квадратичная функция')  # заголовок
axs[0].set_xlabel('x')  # подпись оси X
axs[0].set_ylabel('y = x²')  # подпись оси Y
axs[0].grid(True)  # сетка

# Второй график: случайные точки 
x = np.random.rand(30)  # 30 случайных чисел X (0-1)
y = np.random.rand(30)  # 30 случайных чисел Y (0-1)

axs[1].scatter(x, y, c='green', alpha=0.7)  # зеленые точки с прозрачностью
axs[1].set_title('Случайные точки')  # заголовок
axs[1].set_xlabel('X')  # подпись оси X
axs[1].set_ylabel('Y')  # подпись оси Y
axs[1].grid(True)  # сетка

#  Третий график: столбчатая диаграмма 
categories = ['A', 'B', 'C']  # названия категорий
values = [3, 7, 2]  # значения
colors = ['red', 'green', 'blue']  # цвета столбцов

axs[2].bar(categories, values, color=colors)  # столбчатая диаграмма
axs[2].set_title('Категорийные данные')  # заголовок
axs[2].set_xlabel('Категория')  # подпись оси X
axs[2].set_ylabel('Значение')  # подпись оси Y
axs[2].grid(True, axis='y')  # сетка только по оси Y

# Автоматическая настройка расстояний между графиками
plt.tight_layout()

# Отображаем все графики
plt.show()

