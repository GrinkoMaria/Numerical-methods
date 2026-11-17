import time
import numpy as np

rng = np.random.default_rng(42)
m = rng.normal(size=(200_000, 5))

# циклы
def loop_version(mat):
    n, k = mat.shape

    row_sums = [0.0] * n
    for i in range(n):
        s = 0.0
        for j in range(k):
            s += mat[i, j]
        row_sums[i] = s

    col_max = [-float('inf')] * k
    col_arg = [0] * k
    for j in range(k):
        max_val = -float('inf')
        max_idx = -1
        for i in range(n):
            if mat[i, j] > max_val:
                max_val = mat[i, j]
                max_idx = i
        col_max[j] = max_val
        col_arg[j] = max_idx

    return row_sums, col_max, col_arg


# NumPy
def numpy_version(mat):
    row_sums = mat.sum(axis=1)

    col_max = mat.max(axis=0)

    col_arg = mat.argmax(axis=0)

    return row_sums, col_max, col_arg


# Замер
def measure(fn, x, repeat=3):
    best = float("inf")
    result = None
    for _ in range(repeat):
        t0 = time.perf_counter()
        result = fn(x)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return result, best


(r_loop, t_loop) = measure(loop_version, m)
(r_numpy, t_numpy) = measure(numpy_version, m)

print(f"цикл:   {t_loop * 1000:10.2f} мс")
print(f"NumPy:  {t_numpy * 1000:10.2f} мс")
print(f"ускорение: {t_loop / t_numpy:.1f}×")
print()
print("суммы строк совпадают:  ", np.allclose(r_loop[0], r_numpy[0]))
print("максимумы совпадают:    ", np.allclose(r_loop[1], r_numpy[1]))
print("индексы совпадают:      ", np.array_equal(r_loop[2], r_numpy[2]))
print()
print("NumPy, максимумы по столбцам:", np.round(r_numpy[1], 4))
print("NumPy, их индексы:           ", r_numpy[2])