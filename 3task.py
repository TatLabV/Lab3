import numpy as np

#Создаем матрицу 5x5 со случайными целыми числами от 1 до 10
matrix = np.random.randint(1, 11, size=(5, 5))

#Выводим матрицу
print("Сгенерированная матрица:")
print(matrix)

#Вычисляем среднее значение всех элементов
mean_value = np.mean(matrix)
print(f"\nСреднее значение всех элементов: {mean_value:.2f}")

#Находим максимальный элемент
max_value = np.max(matrix)
print(f"Максимальный элемент: {max_value}")

#Находим минимальный элемент
min_value = np.min(matrix)
print(f"Минимальный элемент: {min_value}")

#Вычисляем сумму по столбцам
col_sums = np.sum(matrix, axis=0)
print("\nСуммы по столбцам:")
for i, col_sum in enumerate(col_sums):
    print(f"Столбец {i+1}: {col_sum}")

