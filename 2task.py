import numpy as np
import matplotlib.pyplot as plt

# Генерируем 1000 случайных чисел с нормальным распределением
data = np.random.normal(0, 1, 1000)

# Создаем новую фигуру
plt.figure(figsize=(10, 5))

# Строим гистограмму с 20 столбцами
# color: цвет столбцов
# edgecolor: цвет границ столбцов
# alpha: прозрачность (0-1)
plt.hist(data, bins=20, color='skyblue', edgecolor='black', alpha=0.7)

# Добавляем заголовок
plt.title('Гистограмма нормального распределения')

# Подписи осей
plt.xlabel('Значения')
plt.ylabel('Количество значений')

# Включаем сетку
plt.grid(True, linestyle='--', alpha=0.7)

# Отображаем график
plt.show()
