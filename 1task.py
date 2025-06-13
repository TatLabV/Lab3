# Импортируем необходимые библиотеки
import numpy as np
import matplotlib.pyplot as plt

# Создаем массив x из 100 точек от 0 до 10
x = np.linspace(0, 10, 100)

# Рассчитываем y = sin(x) и z = cos(x)
y = np.sin(x)
z = np.cos(x)

# Создаем новую фигуру размером 10x5 дюймов
plt.figure(figsize=(10, 5))

# Рисуем график sin(x) синей сплошной линией с меткой 'sin(x)'
plt.plot(x, y, 'b-', label='sin(x)')

# Рисуем график cos(x) красной сплошной линией с меткой 'cos(x)'
plt.plot(x, z, 'r-', label='cos(x)')

# Добавляем заголовок графика
plt.title('Графики функций sin(x) и cos(x)')

# Добавляем подписи осей
plt.xlabel('Ось X (радианы)')
plt.ylabel('Ось Y')

# Добавляем легенду (справа вверху)
plt.legend(loc='upper right')

# Включаем сетку для лучшей читаемости
plt.grid(True)

# Отображаем график
plt.show()
