import numpy as np
import matplotlib.pyplot as plt

#Создаем матрицу 5x5 со случайными числами от 1 до 10
matrix = np.random.randint(1, 11, size=(5, 5))

#Создаем фигуру
plt.figure(figsize=(8, 6))

#Создаем тепловую карту
heatmap = plt.imshow(matrix, cmap='viridis')

#Добавляем цветовую шкалу
plt.colorbar(heatmap, label='Значение')

#Добавляем заголовок
plt.title('Тепловая карта матрицы')

#Добавляем подписи осей
plt.xlabel('Столбцы')
plt.ylabel('Строки')

#Добавляем числа в ячейки
for i in range(matrix.shape[0]):  # для каждой строки
    for j in range(matrix.shape[1]):  # для каждого столбца
        # Добавляем текст в центр ячейки
        # ha: горизонтальное выравнивание ('center')
        # va: вертикальное выравнивание ('center')
        # color: белый текст для темных ячеек, черный - для светлых
        text_color = 'white' if matrix[i, j] < 6 else 'black'
        plt.text(j, i, str(matrix[i, j]), 
                 ha='center', va='center', 
                 color=text_color, fontsize=12)

#Отображаем график
plt.show()

