import time
import numpy as np


def task_1():
    print("--- Задача 1")

    def measure(fn, arr, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = fn(arr)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_sum(arr):
        total = 0.0
        for x in arr:
            total += x
        return total

    def numpy_sum(arr):
        return arr.sum()

    print(f"{'n':>10} | {'Цикл (мс)':>10} | {'NumPy (мс)':>10} | {'Ускорение':>10}")
    print("-" * 52)

    rng = np.random.default_rng(42)

    for n in [10 ** 5, 10 ** 6, 10 ** 7]:
        a = rng.normal(size=n)

        r_loop, t_loop = measure(loop_sum, a)
        r_numpy, t_numpy = measure(numpy_sum, a)

        # Выводим результаты
        print(f"{n:>10} | {t_loop * 1000:>10.2f} | {t_numpy * 1000:>10.2f} | {t_loop / t_numpy:>9.1f}×")

    print("\nВывод:")
    print("1. При n = 10^5 разница уже заметна, но настоящий разрыв виден на 10^6 и 10^7.")
    print("2. Ускорение растёт вместе с размером массива, так как накладные расходы")
    print("   интерпретатора Python на циклы (сложение, проверки) становятся огромными.")
    print("   NumPy делает эту же работу внутри быстрого C-цикла.")


import time
import math
import numpy as np

def task_2():
    print("--- Задача 2 ---")

    def measure(fn, arr, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = fn(arr)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_mean_std(arr):
        n = len(arr)
        s = 0.0
        s_sq = 0.0
        for x in arr:
            s += x
            s_sq += x ** 2
        mean = s / n
        # Формула дисперсии: E[x^2] - (E[x])^2
        var = (s_sq / n) - (mean ** 2)
        return mean, math.sqrt(var)

    def numpy_mean_std(arr):
        return arr.mean(), arr.std()

    # Создаем данные
    n = 10 ** 6
    rng = np.random.default_rng(42)
    a = rng.normal(size=n)

    # Замеряем
    (m_loop, s_loop), t_loop = measure(loop_mean_std, a)
    (m_numpy, s_numpy), t_numpy = measure(numpy_mean_std, a)

    print(f"Размер массива: n = {n}")
    print(f"Цикл:  время = {t_loop * 1000:>8.2f} мс | mean = {m_loop:.10f} | std = {s_loop:.10f}")
    print(f"NumPy: время = {t_numpy * 1000:>8.2f} мс | mean = {m_numpy:.10f} | std = {s_numpy:.10f}")
    print(f"Ускорение: {t_loop / t_numpy:.1f}×")

    is_close = np.isclose(m_loop, m_numpy, atol=1e-12) and np.isclose(s_loop, s_numpy, atol=1e-12)
    print(f"Результаты совпадают до 1e-12: {is_close}")

    print("\nВывод:")
    print("1. NumPy работает в десятки раз быстрее.")
    print("2. NumPy считает std устойчивее (точнее). Формула 'в лоб' (E[x^2] - (E[x])^2)")
    print("   в чистом Python приводит к потере точности при вычитании двух больших чисел.")
    print("   NumPy использует более стабильные алгоритмы (компенсированное суммирование).")

import time
import math
import numpy as np

def task_3():
    print("--- Задача 3 ---")

    def measure(fn, arr, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = fn(arr)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_calc(arr):
        result = []
        for x in arr:
            result.append(math.sin(x) + x * x)
        return result

    def numpy_calc(arr):
        return np.sin(arr) + arr**2

    # Создаем данные
    n = 10**6
    rng = np.random.default_rng(42)
    a = rng.normal(size=n)

    # Замеряем
    r_loop, t_loop = measure(loop_calc, a)
    r_numpy, t_numpy = measure(numpy_calc, a)

    print(f"Размер массива: n = {n}")
    print(f"Цикл (список Python):  время = {t_loop*1000:>8.2f} мс")
    print(f"NumPy (векторизация):  время = {t_numpy*1000:>8.2f} мс")
    print(f"Ускорение: {t_loop / t_numpy:.1f}×")

    is_close = np.allclose(r_loop, r_numpy)
    print(f"Результаты совпадают: {is_close}")

    print("\nВывод:")
    print("1. NumPy-версия короче и быстрее.")
    print("2. Цикл выделяет огромный список Python (накладные расходы на каждый объект).")
    print("3. NumPy использует временные массивы. В выражении np.sin(a) + a**2 создаются:")
    print("   - массив для np.sin(a)")
    print("   - массив для a**2")
    print("   - массив для их суммы")
    print("   Итого: 3 временных массива в памяти (по 8 МБ каждый для n=10^6).")


import numpy as np


def task_4():
    print("--- Задача 4 ---")

    def measure(fn, arr, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = fn(arr)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_clip(arr):
        result = []
        for x in arr:
            if x < 0:
                result.append(0.0)
            elif x > 1:
                result.append(1.0)
            else:
                result.append(x)
        return result

    def numpy_clip(arr):
        # Встроенная функция
        return np.clip(arr, 0, 1)

    # Создаем данные
    n = 10 ** 6
    rng = np.random.default_rng(42)
    a = rng.normal(size=n)
    changed_count = np.sum((a < 0) | (a > 1))

    # Замеряем
    r_loop, t_loop = measure(loop_clip, a)
    r_numpy, t_numpy = measure(numpy_clip, a)

    print(f"Размер массива: n = {n}")
    print(f"Цикл (if/elif):  время = {t_loop * 1000:>8.2f} мс")
    print(f"NumPy (np.clip): время = {t_numpy * 1000:>8.2f} мс")
    print(f"Ускорение: {t_loop / t_numpy:.1f}×")

    print(f"\nСтатистика: было изменено {changed_count} элементов из {n}.")

    # Проверка
    is_close = np.allclose(r_loop, r_numpy)
    print(f"Результаты совпадают: {is_close}")

    print("\nВывод:")
    print("1. NumPy в разы короче и быстрее.")
    print("2. У цикла 2 условия (if) и 1 цикл (for).")
    print("3. У NumPy — 0 циклов и 0 условий (всё скрыто внутри C-функции np.clip),")
    print("   что делает код максимально читаемым.")


import time
import numpy as np


def task_5():
    print("--- Задача 5 ---")

    def measure(fn, arr, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = fn(arr)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_sum_rows(mat):
        n_rows = mat.shape[0]
        n_cols = mat.shape[1]
        result = [0.0] * n_rows
        for i in range(n_rows):
            s = 0.0
            for j in range(n_cols):
                s += mat[i, j]
            result[i] = s
        return result

    def numpy_sum_rows(mat):
        return mat.sum(axis=1)

    # Создаем матрицу (n, 10)
    n = 100_000
    rng = np.random.default_rng(42)
    matrix = rng.normal(size=(n, 10))

    # Замеряем
    r_loop, t_loop = measure(loop_sum_rows, matrix)
    r_numpy, t_numpy = measure(numpy_sum_rows, matrix)

    print(f"Размер матрицы: {matrix.shape[0]} строк, {matrix.shape[1]} столбцов")
    print(f"Цикл (вложенный for): время = {t_loop * 1000:>8.2f} мс")
    print(f"NumPy (m.sum(axis=1)): время = {t_numpy * 1000:>8.2f} мс")
    print(f"Ускорение: {t_loop / t_numpy:.1f}×")

    # Проверка
    is_close = np.allclose(r_loop, r_numpy)
    print(f"Результаты совпадают: {is_close}")

    print("\nВывод:")
    print("1. NumPy-версия (m.sum(axis=1)) читается буквально как 'сумма по строкам'.")
    print("2. В цикле используются счётчики i и j, код похож на математическую запись,")
    print("   но с точки зрения программиста это лишние сущности (индексы).")
    print("3. NumPy-код намного легче поддерживать: меньше шансов ошибиться в индексах.")


import time
import numpy as np

def task_6():
    print("--- Задача 6 ---")

    def measure(fn, arr, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = fn(arr)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_normalize(mat):
        n_rows, n_cols = mat.shape

        means = [0.0] * n_cols
        for j in range(n_cols):
            s = 0.0
            for i in range(n_rows):
                s += mat[i, j]
            means[j] = s / n_rows

        result = np.zeros_like(mat)
        for i in range(n_rows):
            for j in range(n_cols):
                result[i, j] = mat[i, j] - means[j]
        return result

    def numpy_normalize(mat):
        return mat - mat.mean(axis=0)

    # Создаем матрицу (n, 10)
    n = 100_000
    rng = np.random.default_rng(42)
    matrix = rng.normal(size=(n, 10))

    # Замеряем
    r_loop, t_loop = measure(loop_normalize, matrix)
    r_numpy, t_numpy = measure(numpy_normalize, matrix)

    print(f"Размер матрицы: {matrix.shape[0]} строк, {matrix.shape[1]} столбцов")
    print(f"Цикл (ручной расчет):  время = {t_loop * 1000:>8.2f} мс (SLOC: ~15 строк)")
    print(f"NumPy (m - m.mean()):  время = {t_numpy * 1000:>8.2f} мс (SLOC: 1 строка)")
    print(f"Ускорение: {t_loop / t_numpy:.1f}×")

    # Проверка
    is_close = np.allclose(r_loop, r_numpy)
    print(f"Результаты совпадают: {is_close}")

    # Проверяем, что средние после нормировки равны нулю
    means_after = r_numpy.mean(axis=0)
    is_zero = np.allclose(means_after, 0)
    print(f"Средние после нормировки ≈ 0: {is_zero}")
    print(f"Пример средних: {np.round(means_after, 5)}")

    print("\nВывод:")
    print("1. NumPy-версия состоит всего из одной строки и использует broadcasting.")
    print("2. Циклу требуется минимум 6-15 строк кода (цикл подсчета, цикл вычитания, индексы).")
    print("3. Разница в количестве ошибок индексации (index out of bounds) огромна.")


import time
import numpy as np


def task_7():
    print("--- Задача 7 ---")

    def measure(fn, arr, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = fn(arr)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_max(arr):
        max_val = -float('inf')
        max_idx = -1
        for i in range(len(arr)):
            if arr[i] > max_val:
                max_val = arr[i]
                max_idx = i
        return max_val, max_idx

    def numpy_max(arr):
        return arr.max(), arr.argmax()

    # Создаем данные
    n = 10 ** 6
    rng = np.random.default_rng(42)
    a = rng.normal(size=n)

    print("1. Тест на чистых данных (без NaN):")
    (m_loop, idx_loop), t_loop = measure(loop_max, a)
    (m_numpy, idx_numpy), t_numpy = measure(numpy_max, a)

    print(f"Цикл:  время = {t_loop * 1000:>8.2f} мс | max = {m_loop:.6f} | idx = {idx_loop}")
    print(f"NumPy: время = {t_numpy * 1000:>8.2f} мс | max = {m_numpy:.6f} | idx = {idx_numpy}")
    print(f"Ускорение: {t_loop / t_numpy:.1f}×")

    print("\n2. Тест на 'грязных' данных (с NaN):")
    # Добавляем NaN в данные
    a_nan = a.copy()
    a_nan[::100] = np.nan

    try:
        m_loop_nan, idx_loop_nan = loop_max(a_nan)
        print(f"Цикл (с NaN): max = {m_loop_nan}, idx = {idx_loop_nan}")
    except Exception as e:
        print(f"Цикл (с NaN) выдал ошибку: {e}")

    m_np_nan, idx_np_nan = numpy_max(a_nan)
    print(f"NumPy .max() (с NaN): max = {m_np_nan}")

    # Специальная функция для NaN
    m_np_nanmax = np.nanmax(a_nan)
    print(f"NumPy np.nanmax() (с NaN): max = {m_np_nanmax:.6f}")

    print("\nВывод:")
    print("1. На чистых данных NumPy быстрее, так как поиск идет в C-цикле.")
    print("2. Цикл с NaN 'ломается', потому что любое сравнение с NaN дает False.")
    print("3. Функции с префиксом nan (np.nanmax) — это не прихоть, а защита от")
    print("   реальных данных, где пропуски (NaN) встречаются постоянно.")


import time
import numpy as np
import sys  # Импортируем sys, чтобы оценить размер объектов в памяти


def task_8():
    print("--- Задача 8 ---")

    def measure(fn, arr, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = fn(arr)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_filter(arr):
        return [x for x in arr if x > 0]

    def numpy_filter(arr):
        return arr[arr > 0]

    # Создаем данные
    n = 10 ** 6
    rng = np.random.default_rng(42)
    a = rng.normal(size=n)  # Около половины чисел будет > 0

    # Замеряем время
    r_loop, t_loop = measure(loop_filter, a)
    r_numpy, t_numpy = measure(numpy_filter, a)

    print(f"Размер массива: n = {n}")
    print(f"Цикл (список): время = {t_loop * 1000:>8.2f} мс")
    print(f"NumPy (маска): время = {t_numpy * 1000:>8.2f} мс")
    print(f"Ускорение: {t_loop / t_numpy:.1f}×")
    print(f"Количество отобранных элементов: {len(r_loop)}")

    mem_list_mb = (sys.getsizeof(r_loop) + len(r_loop) * 24) / (1024 ** 2)

    mem_numpy_mb = r_numpy.nbytes / (1024 ** 2)

    print(f"\nОценка занимаемой памяти результатом:")
    print(f"Список Python: ~{mem_list_mb:.1f} МБ")
    print(f"Массив NumPy:  ~{mem_numpy_mb:.1f} МБ")
    print(f"NumPy-массив компактнее в ~{mem_list_mb / mem_numpy_mb:.1f} раз(а).")

    print("\nВывод:")
    print("1. NumPy работает в десятки раз быстрее.")
    print("2. Список Python хранит каждый элемент как отдельный объект с кучей служебной")
    print("   информации (тип, счетчик ссылок), занимая ~24-32 байта на число.")
    print("3. Массив NumPy хранит данные плотным блоком памяти по 8 байт на число (float64).")
    print("   Поэтому на больших данных NumPy экономит гигабайты оперативной памяти.")


import time
import numpy as np


def task_9():
    print("--- Задача 9 ---")

    def measure(fn, arr, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            arr_copy = arr.copy()
            t0 = time.perf_counter()
            result = fn(arr_copy)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_abs_inplace(arr):
        for i in range(len(arr)):
            if arr[i] < 0:
                arr[i] = -arr[i]
        return arr

    def numpy_abs_inplace(arr):
        arr[arr < 0] *= -1
        return arr

    # Создаем данные
    n = 10 ** 6
    rng = np.random.default_rng(42)
    a = rng.normal(size=n)

    # Замеряем
    r_loop, t_loop = measure(loop_abs_inplace, a)
    r_numpy, t_numpy = measure(numpy_abs_inplace, a)

    print(f"Размер массива: n = {n}")
    print(f"Цикл (по индексам): время = {t_loop * 1000:>8.2f} мс")
    print(f"NumPy (маска *= -1): время = {t_numpy * 1000:>8.2f} мс")
    print(f"Ускорение: {t_loop / t_numpy:.1f}×")

    # Проверка, что результаты совпадают
    is_close = np.allclose(r_loop, r_numpy)
    print(f"Результаты совпадают: {is_close}")

    # Проверка, что массив действительно изменён
    no_negatives = np.all(r_numpy >= 0)
    print(f"В массиве не осталось отрицательных чисел: {no_negatives}")

    print("\nВывод:")
    print("1. Оба варианта не создают новый массив в памяти, а меняют существующий.")
    print("2. Цикл for по массиву NumPy медленный, потому что каждый arr[i] —")
    print("   это создание Python-объекта и вызов C-функции.")
    print("3. In-place операции в NumPy (через маски или out=) критически важны")
    print("   для больших данных, когда памяти на создание копии просто нет.")


import time
import numpy as np


def task_10():
    print("--- Задача 10 ---")

    def measure(fn, arr, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = fn(arr)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_filter(arr):
        return [x for x in arr if -1 < x < 1]

    def numpy_filter_correct(arr):
        return arr[(arr > -1) & (arr < 1)]

    # Создаем данные
    n = 10 ** 6
    rng = np.random.default_rng(42)
    a = rng.normal(size=n)  # Стандартное нормальное распределение

    # Замеряем
    r_loop, t_loop = measure(loop_filter, a)
    r_numpy, t_numpy = measure(numpy_filter_correct, a)

    print(f"Размер массива: n = {n}")
    print(f"Цикл (-1 < x < 1):      время = {t_loop * 1000:>8.2f} мс")
    print(f"NumPy ((a > -1) & (a < 1)): время = {t_numpy * 1000:>8.2f} мс")
    print(f"Ускорение: {t_loop / t_numpy:.1f}×")

    # Проверка
    is_close = np.allclose(r_loop, r_numpy)
    print(f"Результаты совпадают: {is_close}")
    print(f"Количество отобранных элементов: {len(r_numpy)}")

    print("\nДемонстрация ошибки без скобок:")
    try:
        _ = a > -1 & a < 1
    except Exception as e:
        print(f"Ошибка: {type(e).__name__}")

    print("\nВывод:")
    print("1. В Python условие -1 < x < 1 читается отлично.")
    print("2. В NumPy нужно писать (a > -1) & (a < 1). Скобки обязательны!")
    print("3. Без скобок (a > -1 & a < 1) интерпретатор сначала выполнит побитовое И")
    print("   над числами -1 и a, что даст совершенно неправильный результат или ошибку.")
    print("   Приоритет & выше, чем у операторов сравнения (>, <).")


import time
import numpy as np


def task_11():
    print("--- Задача 11 ---")

    def measure(fn, x, y, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = fn(x, y)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_distances(X, Y):
        n, m = X.shape[0], Y.shape[0]
        D = np.zeros((n, m))
        for i in range(n):
            for j in range(m):
                s = 0.0
                for k in range(X.shape[1]):
                    diff = X[i, k] - Y[j, k]
                    s += diff * diff
                D[i, j] = np.sqrt(s)
        return D

    def numpy_distances_broadcasting(X, Y):
        return np.sqrt(((X[:, None, :] - Y[None, :, :]) ** 2).sum(axis=2))

    n, m, dim = 1000, 1000, 3
    rng = np.random.default_rng(42)
    X = rng.normal(size=(n, dim))
    Y = rng.normal(size=(m, dim))

    # Замеряем
    r_loop, t_loop = measure(loop_distances, X, Y)
    r_numpy, t_numpy = measure(numpy_distances_broadcasting, X, Y)

    print(f"Точек в X: {n}, Точек в Y: {m}, Размерность: {dim}")
    print(f"Цикл (вложенный for):    время = {t_loop * 1000:>8.2f} мс")
    print(f"NumPy (broadcasting):    время = {t_numpy * 1000:>8.2f} мс")
    print(f"Ускорение: {t_loop / t_numpy:.1f}×")

    # Проверка
    is_close = np.allclose(r_loop, r_numpy)
    print(f"Результаты совпадают: {is_close}")

    mem_bytes = n * m * dim * 8
    mem_mb = mem_bytes / (1024 ** 2)
    print(f"\nВнимание, память:")
    print(f"При операции X[:, None, :] - Y[None, :, :] создается временный массив формы {n}x{m}x{dim}.")
    print(f"Он занимает ~ {mem_mb:.1f} МБ оперативной памяти!")

    print("\nВывод:")
    print("1. NumPy-версия быстрее в десятки раз.")
    print("2. Однако broadcasting создает огромный временный 3D-массив.")
    print("   Если n и m будут по 10 000, этот массив займет уже 2.4 ГБ памяти и код упадет.")
    print("3. Чтобы уменьшить память, можно использовать формулу: D^2 = X^2 + Y^2 - 2*X@Y.T")
    print("   или функцию scipy.spatial.distance.cdist.")


import time
import numpy as np


def task_12():
    print("--- Задача 12 ---")

    def measure(fn, arr, k, repeat=3):
        best = float("inf")
        result = None
        for _ in range(repeat):
            t0 = time.perf_counter()
            result = fn(arr, k)
            t1 = time.perf_counter()
            best = min(best, t1 - t0)
        return result, best

    def loop_moving_average(arr, k):
        n = len(arr)
        result = np.zeros(n - k + 1)
        for i in range(n - k + 1):
            s = 0.0
            for j in range(k):
                s += arr[i + j]
            result[i] = s / k
        return result

    def numpy_moving_average(arr, k):
        window = np.ones(k) / k
        return np.convolve(arr, window, mode='valid')

    # Создаем данные
    n = 10 ** 5
    k = 10
    rng = np.random.default_rng(42)
    a = rng.normal(size=n)

    # Замеряем
    r_loop, t_loop = measure(loop_moving_average, a, k)
    r_numpy, t_numpy = measure(numpy_moving_average, a, k)

    print(f"Размер массива: n = {n}, окно k = {k}")
    print(f"Цикл (вложенный for):  время = {t_loop * 1000:>8.2f} мс")
    print(f"NumPy (np.convolve):   время = {t_numpy * 1000:>8.2f} мс")
    print(f"Ускорение: {t_loop / t_numpy:.1f}×")

    # Проверка
    is_close = np.allclose(r_loop, r_numpy)
    print(f"Результаты совпадают: {is_close}")

    print("\nВывод:")
    print("1. Наивный цикл выполняет O(n * k) операций.")
    print("2. NumPy через свертку (np.convolve) делает те же O(n * k) операций.")
    print("3. Алгоритмического ускорения (снижения сложности) здесь нет.")
    print("4. Ускорение достигается за счет 'константного фактора': C-цикл внутри")
    print("   NumPy работает в десятки раз быстрее, чем цикл интерпретатора Python.")
    print("   На практике этого ускорения более чем достаточно.")


import time
import math
import sys
import numpy as np

if __name__ == "__main__":
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА: СРАВНЕНИЕ ЦИКЛОВ И NUMPY")
    print("=" * 60)

    start_time = time.perf_counter()

    # Список всех задач для удобного запуска
    tasks = [
        task_1, task_2, task_3, task_4,
        task_5, task_6, task_7,
        task_8, task_9, task_10,
        task_11, task_12
    ]

    for i, task in enumerate(tasks, start=1):
        task()
        print("\n" + "." * 60 + "\n")
