def task_1():
    print("--- Задача 1 ---")

    data = [
        ("x = 3.14, x* = pi", 3.14, 3.141592653589793),
        ("x = 2.718, x* = e", 2.718, 2.718281828459045),
        ("x = 9.8, x* = 9.81", 9.8, 9.81),
        ("x = 0.333, x* = 1/3", 0.333, 1 / 3)
    ]

    print(f"{'Значения':<30} | {'Абс. погрешность':<18} | {'Отн. погрешность'}")
    print("-" * 75)

    for name, x_approx, x_exact in data:
        abs_err = abs(x_approx - x_exact)

        rel_err = (abs_err / abs(x_exact)) * 100

        print(f"{name:<30} | {abs_err:<18.4e} | {rel_err:.4f}%")

    print("\nВывод:")
    print("1. Расположение по качеству приближения:")
    print("   e (отн. ошибка ~0.01%) -> pi (~0.05%) -> 1/3 (~0.1%) -> 9.81 (~0.1%).")
    print("   Самое точное приближение — для числа e (2.718).")
    print("2. Порядок по абсолютной и относительной погрешности не совпадает. У pi абсолютная ошибка больше (~0.0016), чем у e (~0.00028),")
    print("   но относительные ошибки у них обеих очень малы. Если бы мы сравнивали")
    print("   совершенно разные по масштабу числа (например, 1000 и 0.001), порядок бы сильно отличался.")


def task_2():
    print("\n--- Задача 2 ---")

    data = [
        ("Длина моста", 1247.0, 1250.0),
        ("Диаметр болта", 9.7, 10.0)
    ]

    print(f"{'Величина':<15} | {'Абс. погрешность (dx)':<22} | {'Отн. погрешность (dx/x)'}")
    print("-" * 65)

    for name, x_approx, x_exact in data:
        abs_err = abs(x_approx - x_exact)
        rel_err = (abs_err / abs(x_exact)) * 100

        print(f"{name:<15} | {abs_err:<22.2f} | {rel_err:.2f}%")

    print("\nВывод:")
    print("1. Абсолютная погрешность больше у моста (3 метра против 0.3 см).")
    print("2. Относительная погрешность больше у болта (3% против 0.24%).")
    print("3. С точки зрения инженера, погрешность моста в 3 метра — это катастрофа,")
    print("   но в масштабах 1250 метров это всего 0.24%. А для болта ошибка в 3% (0.3 мм)")
    print("   может привести к тому, что он не влезет в гайку.")
    print("4. Для оценки качества измерений нужно брать относительную погрешность, так как она не зависит от масштаба величины.")


import math

def task_3():
    print("--- Задача 3 ---")

    def relative_error(approx, exact):
        if exact == 0:
            return float('inf')

        return abs(approx - exact) / abs(exact)

    test_data = [
        ("x = 3.14, x* = pi", 3.14, math.pi),
        ("x = 2.718, x* = e", 2.718, math.e),
        ("x = 9.8, x* = 9.81", 9.8, 9.81),
        ("x = 0.333, x* = 1/3", 0.333, 1 / 3)
    ]

    print(f"{'Пара значений':<25} | {'Относительная погрешность'}")
    print("-" * 55)

    for name, approx, exact in test_data:
        res = relative_error(approx, exact)
        print(f"{name:<25} | {res:.6e}")

    print("\nПроверка защиты от ошибок:")
    res_zero = relative_error(1.0, 0.0)
    print(f"1. exact = 0: relative_error(1.0, 0.0) = {res_zero}")

    huge_num = 1e308
    res_inf = relative_error(huge_num * 2, huge_num)
    print(f"2. Огромные числа: relative_error(2e308, 1e308) = {res_inf}")

    print("\nВывод:")
    print("1. Функция корректно считает относительную погрешность для обычных чисел.")
    print("2. Без проверки 'if exact == 0' программа упала бы с ошибкой ZeroDivisionError.")
    print("3. При огромных числах результат сам становится inf")


def task_4():
    print("--- Задача 4 ---")

    x_approx = 47.3
    rel_error_percent = 0.1  # 0.1%

    rel_error = rel_error_percent / 100.0

    a = x_approx / (1 + rel_error)
    b = x_approx / (1 - rel_error)

    a_rounded = round(a, 2)
    b_rounded = round(b, 2)

    print(f"Приближенное значение: x = {x_approx}")
    print(f"Максимальная относительная погрешность: {rel_error_percent}%")
    print(f"\nВычисление границ:")
    print(f"a = x / (1 + d) = {x_approx} / {1 + rel_error} = {a:.4f}")
    print(f"b = x / (1 - d) = {x_approx} / {1 - rel_error} = {b:.4f}")

    print(f"\nИнтервал с разумным числом значащих цифр:")
    print(f"x* ∈ [{a_rounded}, {b_rounded}]")

    delta = x_approx * rel_error
    a_alt = x_approx - delta
    b_alt = x_approx + delta
    print(f"\n(Для сравнения, простой способ x ± x*d: [{a_alt:.2f}, {b_alt:.2f}])")

    print("\nВывод:")
    print("1. Так как относительная погрешность задана в процентах, переводим её в доли.")
    print("2. Точное значение x* лежит в интервале [47.25, 47.35].")
    print("3. Запись в виде интервала с двумя знаками после запятой: x* ∈ [47.25, 47.35].")


def task_5():
    print("--- Задача 5 ---")

    sensors = [
        ("Датчик А", 25.0, "abs", 0.3),
        ("Датчик Б", 25.0, "rel", 0.05)
    ]

    deltas = [
        err if err_type == "abs" else (val * err)
        for _, val, err_type, err in sensors
    ]

    results = [
        f"{name}: Delta = {delta:.3f} °C {'<= 0.3 (Годен)' if delta <= 0.3 else '> 0.3 (Брак)'}"
        for (name, _, _, _), delta in zip(sensors, deltas)
    ]

    print("\nПроверка температурных датчиков (T = 25°C, допустимая Delta <= 0.3°C):")
    print("\n".join(results))

    print("\nВывод:")
    print("1. Для Датчика А абсолютная погрешность задана напрямую (0.3°C <= 0.3°C). Он годен.")
    print("2. Для Датчика Б задана относительная погрешность 5%. Переводим её в абсолютную:")
    print("   Delta = 25°C * 0.05 = 1.25°C. Это больше 0.3°C. Датчик Б не подходит.")
    print("3. Выбор датчика зависит от диапазона: если относительная погрешность фиксирована,")
    print("   то с ростом температуры абсолютная погрешность будет расти. При измерении")
    print("   низких температур такой датчик может быть точнее.")


def task_6():
    print("--- Задача 6 ---")

    numbers = [0.004520, 1200, 1.200, 10.03, 0.03050, 250000]

    def count_sig_figs(num):
        s = f"{num:.10e}"
        mantissa = s.split('e')[0].replace('.', '').rstrip('0')
        return len(mantissa)

    sig_figs = [count_sig_figs(num) for num in numbers]

    sci_notation = [f"{num:.4e}" for num in numbers]

    table = [
        f"{num:<10} | {sci:<15} | {count}"
        for num, sci, count in zip(numbers, sci_notation, sig_figs)
    ]

    print(f"{'Число':<10} | {'Эксп. форма':<15} | {'Значащих цифр'}")
    print("-" * 45)
    print("\n".join(table))

    print("\nВывод:")
    print("1. Запись в экспоненциальной форме однозначна, так как мантисса")
    print("   показывает только реально известные цифры (например, 1.200e+03).")
    print("2. Обычная запись неоднозначна, когда в числе есть нули на конце")
    print("   (например, 1200 — это 2, 3 или 4 значащие цифры? Непонятно,")
    print("   это 1.2 * 10^3 или 1.200 * 10^3?).")
    print("3. Экспоненциальная форма устраняет эту двусмысленность.")


def task_7():
    print("--- Задача 7 ---")

    measured_value = 4.738291
    measurement_error = 0.02

    print(f"Измерение: {measured_value} ± {measurement_error}")

    rounded_value = round(measured_value, 2)
    rounded_error = round(measurement_error, 2)

    print("\nАнализ:")
    print(f"Погрешность {measurement_error} имеет значащую цифру в разряде сотых.")
    print("Следовательно, результат нужно округлить до сотых.")

    print("\nИтоговый результат:")
    print(f"x = {rounded_value} ± {rounded_error}")

    value_str = str(rounded_value).replace('.', '').lstrip('0')
    significant_digits = len(value_str)

    print(f"Количество значащих цифр в результате: {significant_digits}")

    print("\nОтвет на вопрос 'Что было бы, если бы записали 4.738291 ± 0.02?':")
    print("Такая запись была бы некорректной. Погрешность говорит о том, что мы ошиблись")
    print("на 2 сотых. Записывать при этом миллионные доли (0.000001) не имеет физического смысла.")


def task_8():
    print("--- Задача 8 ---")

    test_values = [0.5, 1.5, 2.5, 3.5, -0.5, -1.5, -2.5]
    print("Проверка встроенного round() в Python:")
    results = [f"round({val}) = {round(val)}" for val in test_values]
    print("\n".join(results))

    print("\nСравнение со школьным правилом:")
    import math
    school_results = [f"round({val}) = {round(val)} | школа: {math.floor(val + 0.5)}" for val in test_values]
    print("\n".join(school_results))

    print("\nМассовый тест (1 000 000 случайных чисел вида k + 0.5):")
    import random

    random_numbers = [random.randint(0, 99) + 0.5 for _ in range(1_000_000)]

    true_sum = sum(random_numbers)

    py_rounded_sum = sum(round(num) for num in random_numbers)
    school_rounded_sum = sum(math.floor(num + 0.5) for num in random_numbers)

    error_py = abs(true_sum - py_rounded_sum)
    error_school = abs(true_sum - school_rounded_sum)

    print(f"Истинная сумма (до округления): {true_sum:,.0f}")
    print(f"Сумма после Python round():    {py_rounded_sum:,.0f} (отклонение: {error_py:,.0f})")
    print(f"Сумма после школьного метода:{school_rounded_sum:,.0f} (отклонение: {error_school:,.0f})")

    print("\nВывод:")
    print("1. Python использует 'банковское округление' - округление до ближайшего чётного.")
    print("   Поэтому 0.5 -> 0, 1.5 -> 2, 2.5 -> 2, 3.5 -> 4.")
    print("2. Школьное правило '0.5 всегда вверх' при массовых вычислениях дает систематическую ошибку (сумма 'уезжает' вверх).")
    print("3. В финансах систематические ошибки недопустимы. Банковское округление")
    print("   компенсирует себя: половина чисел округляется вниз, половина вверх.")
    print("   Поэтому отклонение (error_py) практически равно 0.")


import math

def task_9():
    print("--- Задача 9 ---")

    n = 1000

    sum_no_round = 0.0
    for i in range(1, n + 1):
        sum_no_round += 1.0 / i

    sum_rounded_terms = 0.0
    for i in range(1, n + 1):
        term = 1.0 / i
        rounded_term = round(term, 3)
        sum_rounded_terms += rounded_term

    exact_terms = [1.0 / i for i in range(1, n + 1)]
    ideal_sum = math.fsum(exact_terms)

    delta_s_no_round = abs(sum_no_round - ideal_sum)
    delta_s_rounded = abs(sum_rounded_terms - ideal_sum)

    print(f"Эталонная сумма (math.fsum): {ideal_sum:.10f}\n")

    print(f"1. Без промежуточного округления (float):")
    print(f"   Сумма: {sum_no_round:.10f}")
    print(f"   Delta S: {delta_s_no_round:.2e}\n")

    print(f"2. С округлением каждого слагаемого до 3 знаков:")
    print(f"   Сумма: {sum_rounded_terms:.10f}")
    print(f"   Delta S: {delta_s_rounded:.2e}\n")

    print(f"Во сколько раз вариант (б) хуже: {delta_s_rounded / delta_s_no_round:.1f} раз\n")

    print("Вывод:")
    print("1. Округление каждого слагаемого до 3 знаков накапливает огромную ошибку.")
    print("   Мы отбрасываем 'хвостики' чисел на каждом шаге, и в сумме теряем много.")
    print("2. Сформулированное правило: НИКОГДА не округляйте промежуточные результаты")
    print("   в длинных цепочках вычислений. Округлять нужно только финальный ответ.")
    print("   Внутри вычислений всегда сохраняйте максимальную точность (float64 или Decimal).")


import math

def task_10():
    print("--- Задача 10 ---")

    a = 0.1
    b = 0.2
    c = 0.3

    result = a + b

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"a + b = {result}")
    print(f"c = {c}\n")

    print("Сравнение результатов:")
    print(f"1. Через '==':           {result == c}")
    print(f"2. Через math.isclose:   {math.isclose(result, c)}")

    delta = abs(result - c)

    print(f"\nРазница (Delta): {delta:.20e}")
    print(f"Разница в обычном виде: {delta}")

    print("\nВывод (почему 0.1 не представимо в двоичной системе):")
    print("1. В десятичной системе мы легко записываем 1/10 (0.1). Но в двоичной")
    print("   системе счисления дробь 1/10 превращается в бесконечную периодическую дробь,")
    print("   как 1/3 в десятичной (0.33333...).")
    print("2. Компьютер хранит числа в формате float64 (64 бита). Он просто обрезает")
    print("   эту бесконечную двоичную дробь, оставляя только 53 бита на мантиссу.")
    print("3. Из-за этого число 0.1 хранится в памяти не как точное 0.1, а как")
    print("   чуть-чуть большее число (примерно 0.10000000000000000555...).")
    print("4. Когда мы складываем два таких 'неточных' числа (0.1 и 0.2), ошибки")
    print("   складываются, и мы получаем 0.30000000000000004.")
    print("5. Поэтому в коде никогда не сравнивайте float через '=='. Используйте isclose!")


import math

def task_11():
    print("--- Задача 11 ---")

    a = 1.0 + 1e-15
    b = 1.0
    result = a - b

    print("1. Вычитание близких чисел:")
    print(f"   a = {a}")
    print(f"   b = {b}")
    print(f"   a - b = {result:.1e} (ожидалось 1e-15)")

    expected = 1e-15
    rel_error = abs(result - expected) / expected
    print(f"   Относительная погрешность: {rel_error:.1%}\n")

    b_coef = 100000001.0
    c_coef = 100000000.0

    print("2. Решение квадратного уравнения:")
    print(f"   Уравнение: x^2 - {b_coef:.0f}x + {c_coef:.0f} = 0")
    print("   Ожидаемые корни: 1 и 100000000 (1e8)\n")

    # Плохая формула
    discriminant = b_coef ** 2 - 4 * c_coef
    x1_bad = (b_coef - math.sqrt(discriminant)) / 2

    # Хорошая формула
    x2_good = (b_coef + math.sqrt(discriminant)) / 2
    x1_good = c_coef / x2_good

    print(f"   Плохая формула (x1):  {x1_bad:.6f}")
    print(f"   Хорошая формула (x1): {x1_good:.6f}")
    print(f"   Абсолютная разница:   {abs(x1_bad - x1_good):.2e}")

    eq_rel_err = abs(x1_bad - x1_good) / x1_good
    print(f"   Относительная погрешность плохого корня: {eq_rel_err:.1%}")

    print("\nВывод:")
    print("1. При вычитании a - b (где a=1+1e-15) мы получили 0.0 или 1.1e-16 вместо 1e-15,")
    print("   потому что число 1e-15 просто не влезло в мантиссу float64 рядом с 1.0.")
    print("2. В квадратном уравнении плохая формула теряет почти всю точность (или дает 0),")
    print("   так как вычитает из 1.00000001e8 число 1.00000000e8.")
    print("3. Спасение — правильная математика: используем теорему Виета (c / x2), чтобы")
    print("   избежать вычитания. Хорошая формула дает точный корень.")


import math
import numpy as np
from decimal import Decimal, getcontext

def task_12():
    print("--- Задача 12 ---")

    n = 10 ** 6
    rng = np.random.default_rng(42)
    arr = rng.uniform(0.1, 1.0, size=n)

    getcontext().prec = 50
    exact_sum = float(sum(Decimal(x) for x in arr))

    sum_naive = 0.0
    for x in arr:
        sum_naive += x

    sum_builtin = sum(arr)
    sum_math = math.fsum(arr)

    results = [
        ("Наивный цикл", sum_naive),
        ("Функция sum()", sum_builtin),
        ("math.fsum()", sum_math)
    ]

    print(f"{'Способ':<15} | {'Сумма':<20} | {'Абс. ошибка':<15} | {'Отн. ошибка'}")
    print("-" * 70)

    table_rows = [
        f"{name:<15} | {val:<20.10f} | {abs(val - exact_sum):<15.2e} | {abs(val - exact_sum) / exact_sum:.2e}"
        for name, val in results
    ]
    print("\n".join(table_rows))

    print(f"\nЭталонное значение: {exact_sum:.10f}")

    print("\nВывод:")
    print("1. math.fsum() показывает самую маленькую ошибку (близкую к 0),")
    print("   так как использует алгоритм компенсированного суммирования (Кэхана).")
    print("2. Наивный цикл и встроенная функция sum() накапливают погрешность,")
    print("   потому что каждый раз прибавляют маленькое число к уже большому.")
    print("3. Встроенная sum() на самом деле использует тот же наивный цикл внутри,")
    print("   поэтому её ошибка практически совпадает с ручным циклом.")
    print("4. Вывод: для критически важных вычислений с большими массивами float")
    print("   всегда используйте math.fsum() (или np.sum для NumPy, если точность не критична).")


import math
import numpy as np

def task_13():
    print("--- Задача 13 ---")

    n = 10 ** 6
    half_n = n // 2

    arr_small = np.random.default_rng(42).uniform(1e-10, 1e-9, size=half_n)
    arr_large = np.random.default_rng(43).uniform(1e5, 1e6, size=half_n)

    sum_small_first = 0.0
    for x in arr_small:
        sum_small_first += x
    for x in arr_large:
        sum_small_first += x

    sum_large_first = 0.0
    for x in arr_large:
        sum_large_first += x
    for x in arr_small:
        sum_large_first += x

    arr_all = np.concatenate((arr_small, arr_large))
    exact_sum = math.fsum(arr_all)

    print(f"{'Стратегия':<30} | {'Сумма':<18} | {'Абс. ошибка'}")
    print("-" * 65)

    results = [
        ("А: сначала маленькие", sum_small_first),
        ("Б: сначала большие", sum_large_first),
        ("Эталон (math.fsum)", exact_sum)
    ]

    for name, val in results:
        err = abs(val - exact_sum)
        print(f"{name:<30} | {val:<18.2f} | {err:.2e}")

    print("\nВывод:")
    print("1. Стратегия А (сначала маленькие) дает результат, который идеально")
    print("   совпадает с эталоном (ошибка 0).")
    print("2. Стратегия Б (сначала большие) теряет все маленькие числа.")
    print("   Когда мы прибавляем число 10^-10 к числу 10^5, компьютер просто")
    print("   игнорирует его, так как оно не влезает в мантиссу (машинная точность).")
    print("3. Правило: при суммировании массива, где есть и большие, и очень маленькие")
    print("   числа, всегда начинайте с наименьших. Это сохранит их вклад в общую сумму.")
    print("   (Или используйте math.fsum, который делает это автоматически).")


import math

def task_14():
    print("--- Задача 14 ---")

    x = 1.0
    errors = []

    exact_val = math.exp(10000 * math.log(1.0001))

    for i in range(10000):
        x *= 1.0001
        rel_err = abs(x - exact_val) / exact_val
        errors.append(rel_err)

    print(f"Точное значение (эталон): {exact_val:.6f}")
    print(f"Результат цикла:          {x:.6f}\n")

    thresholds = [1e-9, 1e-6, 1e-3]
    print("На каком шаге (итерации) погрешность превысила порог:")

    for t in thresholds:
        step = next((i + 1 for i, err in enumerate(errors) if err > t), None)
        if step:
            print(f"  Порог {t:.0e}: превышен на шаге {step}")
        else:
            print(f"  Порог {t:.0e}: НЕ превышен за 10 000 шагов")

    print("\nГрафик роста погрешности (каждая строка = 1000 итераций):")
    print(f"{'Шаг':<8} | {'Отн. погрешность':<20} | {'Визуализация (log10)'}")
    print("-" * 65)

    for i in range(0, 10000, 1000):
        err = errors[i]
        log_err = math.log10(err) if err > 0 else -16
        bar_len = int(log_err + 16)
        bar = "#" * max(0, bar_len)
        print(f"{i + 1000:<8} | {err:<20.2e} | {bar}")

    print("\nВывод:")
    print("1. Ошибка растет экспоненциально. При 10 000 умножений ошибка становится")
    print("   колоссальной (относительная погрешность достигает 10^-1 или 10^-2).")
    print("2. При каждом умножении мы теряем часть точности.")
    print("   Эти микроскопические потери накапливаются и умножаются друг на друга.")
    print("3. Это называется 'раздуванием ошибки' (error growth). В финансовых или")
    print("   физических симуляциях такие цепочки умножений могут полностью исказить результат.")


from decimal import Decimal

def task_15():
    print("--- Задача 15 ---")

    n = 10 ** 6
    amount = 0.01

    sum_float = 0.0
    for _ in range(n):
        sum_float += amount

    sum_decimal = Decimal('0.0')
    amount_decimal = Decimal('0.01')
    for _ in range(n):
        sum_decimal += amount_decimal

    sum_kopecks = 0
    for _ in range(n):
        sum_kopecks += 1

    sum_int_as_rubles = sum_kopecks / 100.0

    expected = 10000.0

    print("Результаты начисления 1 000 000 раз по 0.01 рубля:")
    print(f"(a) float:       {sum_float}")
    print(f"(б) Decimal:     {sum_decimal}")
    print(f"(в) int (копейки): {sum_kopecks} копеек = {sum_int_as_rubles} руб.\n")

    print("Разница с ожидаемым (10 000 руб):")
    print(f"(a) float:       {abs(sum_float - expected)} руб.")
    print(f"(б) Decimal:     {abs(float(sum_decimal) - expected)} руб.")
    print(f"(в) int (копейки): {abs(sum_int_as_rubles - expected)} руб.\n")

    print("Вывод:")
    print("1. Результат (а) с float неправильный с точки зрения бухгалтерии.")
    print("   Ошибка (разница) составляет около 0.000000000001, но если бы это были")
    print("   миллиарды транзакций, недостача накопилась бы катастрофическая.")
    print("   Float хранит числа в двоичной системе, а 0.01 —")
    print("   это бесконечная дробь в двоичном виде, поэтому при каждом сложении")
    print("   теряются микроскопические кусочки.")
    print("2. Результат (б) с Decimal идеально точен. Decimal работает с десятичными")
    print("   дробями так же, как человек на бумаге, поэтому 0.01 + 0.01 всегда дают ровно 0.02.")
    print("3. Результат (в) с int (копейки) также идеально точен. Целые числа")
    print("   в компьютере складываются без ошибок. Это самый быстрый и надежный")
    print("   способ работы с деньгами (в банках часто используют именно int).")
    print("4. Вывод: в финансовых системах НИКОГДА не используйте float для денег.")
    print("   Используйте либо целые числа (копейки/центы), либо Decimal.")


if __name__ == "__main__":
    task_1()
    print("\n" + "=" * 60 + "\n")

    task_2()
    print("\n" + "=" * 60 + "\n")

    task_3()
    print("\n" + "=" * 60 + "\n")

    task_4()
    print("\n" + "=" * 60 + "\n")

    task_5()
    print("\n" + "=" * 60 + "\n")

    task_6()
    print("\n" + "=" * 60 + "\n")

    task_7()
    print("\n" + "=" * 60 + "\n")

    task_8()
    print("\n" + "=" * 60 + "\n")

    task_9()
    print("\n" + "=" * 60 + "\n")

    task_10()
    print("\n" + "=" * 60 + "\n")

    task_11()
    print("\n" + "=" * 60 + "\n")

    task_12()
    print("\n" + "=" * 60 + "\n")

    task_13()
    print("\n" + "=" * 60 + "\n")

    task_14()
    print("\n" + "=" * 60 + "\n")

    task_15()
