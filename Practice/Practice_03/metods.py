import numpy as np

def run_numpy_exercise():
    # 1. Создание массива и его свойства
    arr = np.arange(24).reshape(6, 4)
    print(arr.shape, arr.ndim, arr.size, arr.dtype)

    # 2. Перестройка формы
    arr_2 = arr.reshape(4, 6)
    arr_3 = arr.reshape(2, 3, 4)
    arr_flat = arr.reshape(24)
    print(np.array_equal(arr, arr_flat.reshape(6, 4)))

    # 3. Срезы
    col_slice = arr[:, 2]
    col_slice[0] = 999
    print(arr)

    # 4. Булева маска и среднее
    filtered_elements = arr[arr > 10]
    print(filtered_elements.mean())

    # 5. Вычитание среднего по строкам
    row_means = arr.mean(axis=1, keepdims=True)
    centered_arr = arr - row_means
    print(centered_arr.shape)

    row_sums = centered_arr.sum(axis=1)
    print(np.allclose(row_sums, 0))


run_numpy_exercise()