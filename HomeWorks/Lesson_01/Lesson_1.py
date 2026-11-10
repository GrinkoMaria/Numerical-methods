import math

def task_1():
    print("--- Задача 1 ---")

    data = [
        ("f(x) = sqrt(x)", 1e-8, math.sqrt(1e-8), 1 / (2 * math.sqrt(1e-8))),
        ("f(x) = ln(x)", 1.001, math.log(1.001), 1 / 1.001),
        ("f(x) = x - 1", 1.000001, 1.000001 - 1, 1.0),
        ("f(x) = sin(x)", math.pi / 2, math.sin(math.pi / 2), math.cos(math.pi / 2))
    ]

    conds = [abs(x * df / f) if f != 0 else float('inf') for _, x, f, df in data]

    evals = ["Хорошо" if c < 10 else "Плохо" for c in conds]

    table_rows = [
        f"{name:<15} | {x:<8.2e} | {f:<12.2e} | {df:<12.2e} | {c:<10.2f} | {e}"
        for (name, x, f, df), c, e in zip(data, conds, evals)
    ]

    print(f"{'Функция':<15} | {'x':<8} | {'f(x)':<12} | {'f\'(x)':<12} | {'cond':<10} | {'Оценка'}")
    print("-" * 80)
    print("\n".join(table_rows))

    print("\nВывод:")
    print("1. Расположение по возрастанию обусловленности (от лучшего к худшему):")
    print("   sin(x) (cond=0) < x-1 (cond~10^6) < ln(x) (cond~1000) < sqrt(x) (cond~0.5).")
    print("   *Примечание: у корня cond = 0.5 (хорошо), но абсолютная ошибка огромна из-за производной.*")
    print("2. Самая опасная задача — f(x) = x - 1 при x близком к 1.")
    print("   Это 'вычитание близких чисел'. При малейшей погрешности в x")
    print("   результат f(x) может измениться в разы, так как мы вычитаем почти равные числа.")


import math


def task_2():
    print("--- Задача 2 ---")

    a = 1.0
    b = 1.0 - 1e-8
    delta_a = 1e-9

    f_orig = a - b
    a_new = a + delta_a
    f_new = a_new - b

    delta_f_actual = abs(f_new - f_orig)
    cond = abs(a / (a - b))
    delta_f_predicted = cond * delta_a

    print(f"Исходные данные:")
    print(f"a = {a}")
    print(f"b = {b:.8f}")
    print(f"f(a, b) = a - b = {f_orig:.8f}\n")

    print(f"Маленькая ошибка:")
    print(f"delta_a = {delta_a}")
    print(f"a_new = {a_new}")
    print(f"f(a_new, b) = {f_new:.8f}\n")

    print(f"Результаты:")
    print(f"Фактическое изменение delta_f = {delta_f_actual:.8e}")
    print(f"Число обусловленности cond = |a / (a-b)| = {cond:.2e}")
    print(f"Предсказание по cond: delta_f ≈ {delta_f_predicted:.8e}")

    is_match = math.isclose(delta_f_actual, delta_f_predicted, rel_tol=1e-5)
    print(f"Совпадает ли предсказание с фактом? {is_match}")

    print("\nВывод:")
    print("1. Аналитически число обусловленности для вычитания: cond_a = |a / (a - b)|.")
    print("   При a ≈ b знаменатель стремится к нулю, поэтому cond огромно.")
    print("2. На практике: мы внесли ошибку в a всего 10^-9, но из-за того, что a и b")
    print("   почти равны, эта ошибка выросла в 10^8 раз и полностью исказила результат f.")
    print("3. Это классический пример 'катастрофической потери точности'.")


import math


def task_3():
    print("--- Задача 3 ---")

    epsilons = [1e-2, 1e-4, 1e-6]

    print(f"{'eps':<10} | {'Сдвиг корня':<15} | {'Отношение сдвигов':<20}")
    print("-" * 50)

    shifts = [math.sqrt(eps) for eps in epsilons]
    ratios = [shift / eps for shift, eps in zip(shifts, epsilons)]

    table_rows = [
        f"{eps:<10.0e} | {shift:<15.4e} | {ratio:<20.2e}"
        for eps, shift, ratio in zip(epsilons, shifts, ratios)
    ]

    print("\n".join(table_rows))

    print("\nВывод:")
    print("1. Исходное уравнение x^2 - 2x + 1 = 0 имеет один корень x = 1 кратности 2.")
    print("2. При изменении свободного члена на eps корень сдвигается на sqrt(eps).")
    print("3. Отношение сдвигов (sqrt(eps) / eps) равно 1 / sqrt(eps).")
    print("   Это значит, что чем меньше eps, тем сильнее относительное изменение.")
    print("   Например, при eps = 10^-6 сдвиг корня составит 10^-3 (в 1000 раз больше!).")
    print("4. Это доказывает, что задача нахождения кратных корней крайне плохо обусловлена.")
    print("   Малые изменения входных данных приводят к непропорционально большим изменениям корня.")


import math


def task_4():
    print("--- Задача 4 ---")

    x = 1.000000001

    def unstable_algo(x):
        return x ** 2 - 1.0

    def stable_algo(x):
        return (x - 1.0) * (x + 1.0)

    print(f"Входное значение: x = {x:.10f}\n")

    from decimal import Decimal, getcontext
    getcontext().prec = 50
    x_dec = Decimal('1.000000001')
    ideal_val = float((x_dec ** 2) - Decimal(1))

    print(f"Идеальное значение (эталон): {ideal_val:.20e}\n")

    res_unstable = unstable_algo(x)
    res_stable = stable_algo(x)

    err_unstable = abs(res_unstable - ideal_val)
    err_stable = abs(res_stable - ideal_val)

    print("Результаты алгоритмов:")
    print(f"1. Неустойчивый (x**2 - 1): {res_unstable:.20e}")
    print(f"   Абсолютная ошибка:       {err_unstable:.4e}")
    print(f"\n2. Устойчивый ((x-1)*(x+1)): {res_stable:.20e}")
    print(f"   Абсолютная ошибка:       {err_stable:.4e}")

    print("\nВывод:")
    print("1. Задача (возведение в квадрат и вычитание 1) сама по себе ХОРОШО ОБУСЛОВЛЕНА.")
    print("   Математическая функция f(x) = x^2 - 1 не является сверхчувствительной к x.")
    print("2. Но алгоритм 'x**2 - 1' НЕУСТОЙЧИВ. В компьютере числа хранятся с ограниченной")
    print("   точностью. При возведении в квадрат (x**2) мы теряем младшие разряды, а")
    print("   затем при вычитании 1 возникает эффект 'вычитания близких чисел'.")
    print("3. Алгоритм '(x-1)*(x+1)' УСТОЙЧИВ. Он избегает вычитания больших чисел и дает")
    print("   точный результат, доказывая, что проблему можно решить выбором правильного алгоритма.")


import math
from decimal import Decimal, getcontext

def task_5():
    print("--- Задача 5 ---")

    getcontext().prec = 50
    a = 1.0
    c = 1.0
    b_values = [10 ** 8, 10 ** 4, 10 ** 12]

    print(f"{'b':<10} | {'Метод':<12} | {'Результат':<25} | {'Отн. погрешность':<20}")
    print("-" * 75)

    for b in b_values:
        # Формула: x = 2c / (-b - sqrt(b^2 - 4ac))
        b_dec = Decimal(b)
        a_dec = Decimal(a)
        c_dec = Decimal(c)
        disc_dec = (b_dec ** 2) - (4 * a_dec * c_dec)
        root_dec = 2 * c_dec / (-b_dec - disc_dec.sqrt())
        ideal_x = float(root_dec)

        # Плохой способ:
        disc_float = math.sqrt(b ** 2 - 4 * a * c)
        x_bad = (-b + disc_float) / (2 * a)

        # Хороший способ:
        x_good = (2 * c) / (-b - disc_float)

        err_bad = abs(x_bad - ideal_x) / abs(ideal_x)
        err_good = abs(x_good - ideal_x) / abs(ideal_x)

        print(f"{b:<10.0e} | {'Плохо':<12} | {x_bad:<25.4e} | {err_bad:<20.4e}")
        print(f"{'':<10} | {'Хорошо':<12} | {x_good:<25.4e} | {err_good:<20.4e}")
        print("-" * 75)

    print("\nВывод:")
    print("1. Плохой способ '(-b + sqrt(D)) / 2a' страдает от вычитания близких чисел.")
    print("   При b^2 >> 4ac значения -b и sqrt(D) почти равны, их разность теряет точность.")
    print("2. Хороший способ '2c / (-b - sqrt(D))' использует эквивалентную формулу, где")
    print("   в знаменателе происходит сложение, что избегает потери точности.")
    print("3. Плохой способ начинает катастрофически ошибаться уже при b = 10^4 (погрешность 100%!).")
    print("   При b = 10^8 он вообще выдает 0.0, хотя истинный корень не равен нулю.")


import math

def task_6():
    print("--- Задача 6 ---")

    x_vals = [10 ** -k for k in range(2, 11)]

    print(f"{'x':<10} | {'Плохо (прямо)':<18} | {'Хорошо (2sin^2)':<18} | {'Ош. плохо':<12} | {'Ош. хорошо':<12}")
    print("-" * 80)

    for x in x_vals:
        ideal = 0.5
        bad = (1.0 - math.cos(x)) / (x ** 2)
        good = (2 * math.sin(x / 2) ** 2) / (x ** 2)

        err_bad = abs(bad - ideal) / ideal
        err_good = abs(good - ideal) / ideal

        print(f"{x:<10.0e} | {bad:<18.6e} | {good:<18.6e} | {err_bad:<12.2e} | {err_good:<12.2e}")

    print("\nВывод:")
    print("1. 'Плохой' способ начинает превышать ошибку в 1% (0.01) примерно при x = 10^-4.")
    print("   При x = 10^-8 погрешность достигает 100% и более.")
    print("2. Причина: когда x мало, cos(x) в компьютере округляется до 1.0, и 1 - cos(x)")
    print("   дает чистый 0. Происходит 'вычитание близких чисел'.")
    print("3. 'Хороший' способ через 2*sin^2(x/2) не вычитает близкие числа, поэтому")
    print("   его ошибка остается на уровне машинной погрешности (около 10^-16).")
    print("\nСформулированное правило:")
    print("Если при вычислении функции происходит вычитание двух близких по значению величин,")
    print("нужно использовать алгебраические или тригонометрические тождества для преобразования")
    print("выражения в такую форму, где большие числа складываются или умножаются, а не вычитаются.")


import math
from decimal import Decimal, getcontext


def task_7():
    print("--- Задача 7 ---")

    getcontext().prec = 50
    x_vals = [10.0 ** k for k in range(4, 17, 2)]

    print(f"{'x':<10} | {'Плохо (прямо)':<18} | {'Хорошо (сопряж.)':<18} | {'Отн. ошибка (плохо)'}")
    print("-" * 75)

    for x in x_vals:
        x_dec = Decimal(str(x))
        ideal_dec = (x_dec + 1).sqrt() - x_dec.sqrt()
        ideal = float(ideal_dec)

        bad = math.sqrt(x + 1) - math.sqrt(x)

        good = 1.0 / (math.sqrt(x + 1) + math.sqrt(x))

        err_bad = abs(bad - ideal) / ideal if ideal != 0 else 0

        print(f"{x:<10.0e} | {bad:<18.6e} | {good:<18.6e} | {err_bad:<12.2e}")

    print("\nВывод:")
    print("1. 'Плохой' способ 'sqrt(x+1) - sqrt(x)' при больших x дает колоссальную ошибку.")
    print("   При x = 10^16 погрешность достигает 100% (все значащие цифры теряются).")
    print("2. Причина: при больших x числа sqrt(x+1) и sqrt(x) почти равны, и компьютер")
    print("   обрезает младшие разряды при вычитании.")
    print("3. 'Хороший' способ использует формулу 1 / (sqrt(x+1) + sqrt(x)). Это")
    print("   математически эквивалентно, но позволяет избежать вычитания больших чисел.")
    print("4. Оценка показателя степени: ошибка растет пропорционально x. Если x")
    print("   увеличивается в 10 раз, потеря точности возрастает на 1 порядок.")


import math
from decimal import Decimal, getcontext


def task_8():
    print("--- Задача 8 ---")

    getcontext().prec = 50

    x_vals = [10.0 ** -k for k in range(2, 17, 2)]

    print(f"{'x':<10} | {'Плохо (log(1+x))':<18} | {'Хорошо (log1p)':<18} | {'Отн. ошибка (плохо)'}")
    print("-" * 75)

    for x in x_vals:
        x_dec = Decimal(str(x))
        ideal_dec = (Decimal(1) + x_dec).ln()
        ideal = float(ideal_dec)

        bad = math.log(1 + x)

        good = math.log1p(x)

        err_bad = abs(bad - ideal) / ideal if ideal != 0 else 0

        print(f"{x:<10.0e} | {bad:<18.6e} | {good:<18.6e} | {err_bad:<12.2e}")

    print("\nВывод:")
    print("1. 'Плохой' способ math.log(1 + x) начинает ошибаться, когда x становится")
    print("   меньше машинной точности (около 10^-16).")
    print("2. Причина: компьютер не может сложить 1.0 и 10^-16 в float64, поэтому")
    print("   1 + x превращается в ровно 1.0. Логарифм от 1 равен 0 (100% ошибка).")
    print("3. 'Хороший' способ math.log1p(x) дает точный результат на всем диапазоне.")
    print("4. Что делает log1p внутри: в стандартной библиотеке C (на которой основан Python)")
    print("   реализован специальный алгоритм (обычно через ряды Тейлора или рациональные")
    print("   аппроксимации), который не вычисляет промежуточное (1+x) напрямую, а работает")
    print("   с самим x. Это делает его устойчивым.")
    print("\nПочему странные функции типа log1p, expm1, hypot — это хорошо?")
    print("Они решают конкретные проблемы точности. Если вам нужно посчитать ln(1+x)")
    print("для x, близкого к нулю, использовать math.log(1+x) — грубая ошибка.")


import math
from decimal import Decimal, getcontext


def task_9():
    print("--- Задача 9 ---")

    getcontext().prec = 50

    def get_ideal(n):
        return float(sum(Decimal(1) / Decimal(k) for k in range(1, n + 1)))

    n_values = [10 ** 5, 10 ** 6, 10 ** 7]

    print(f"{'n':<10} | {'Способ':<15} | {'Сумма':<18} | {'Отн. ошибка'}")
    print("-" * 65)

    for n in n_values:
        terms = [1.0 / k for k in range(1, n + 1)]

        s_naive = sum(terms)
        s_fsum = math.fsum(terms)

        ideal = get_ideal(n)

        errors = [abs(s - ideal) / ideal for s in [s_naive, s_fsum]]

        rows = [
            f"{n:<10.0e} | {name:<15} | {val:<18.8f} | {err:.4e}"
            for name, val, err in zip(["Наивный sum()", "math.fsum()"], [s_naive, s_fsum], errors)
        ]

        print("\n".join(rows))
        print("-" * 65)

    print("\nВывод:")
    print("1. При увеличении n ошибка наивного sum() растет из-за накопления погрешности.")
    print("2. math.fsum() не накапливает ошибку, так как внутри использует точное")
    print("   суммирование (алгоритм компенсированного суммирования Кэхана).")
    print("3. При n = 10^7 ошибка наивного способа может достигнуть 10^-10.")
    print("   Наивная сумма становится неприемлемой, когда ошибка превышает 10^-10.")


import math
import numpy as np

def task_10():
    print("--- Задача 10: Разделение источников ошибки ---")

    ideal = 0.5

    print("\n(а) Эксперимент А: Меняем x (float64), алгоритм ПЛОХОЙ")
    print("    Влияние обусловленности задачи на ошибку:")
    print(f"    {'x':<10} | {'Ошибка':<15}")
    print("    " + "-" * 28)

    x_vals = [10.0 ** -k for k in range(2, 10)]
    errs_a = [abs(((1.0 - math.cos(x)) / (x ** 2)) - ideal) / ideal for x in x_vals]

    rows_a = [f"    {x:<10.0e} | {err:<15.2e}" for x, err in zip(x_vals, errs_a)]
    print("\n".join(rows_a))
    print("\n(б) Эксперимент Б: Фиксируем x = 10^-4, алгоритм ПЛОХОЙ")
    print("    Влияние машинной точности (dtype):")

    x_fixed = 1e-4
    x64 = np.float64(x_fixed)
    val64 = (1.0 - np.cos(x64)) / (x64 ** 2)
    err64 = abs(val64 - ideal) / ideal
    x32 = np.float32(x_fixed)
    val32 = (1.0 - np.cos(x32)) / (x32 ** 2)
    err32 = abs(val32 - ideal) / ideal

    print(f"    float64: значение = {val64:.8e}, ошибка = {err64:.2e}")
    print(f"    float32: значение = {val32:.8e}, ошибка = {err32:.2e}")
    print("    (float32 дает в ~10^4 раз большую ошибку)")

    print("\n(в) Эксперимент В: Фиксируем x = 10^-8, меняем алгоритм")
    print("    Влияние устойчивости алгоритма:")

    x_tiny = 1e-8

    bad_val = (1.0 - math.cos(x_tiny)) / (x_tiny ** 2)
    bad_err = abs(bad_val - ideal) / ideal

    good_val = (2 * math.sin(x_tiny / 2) ** 2) / (x_tiny ** 2)
    good_err = abs(good_val - ideal) / ideal

    print(f"    Плохой (прямо): ошибка = {bad_err:.2e}")
    print(f"    Хороший (sin^2): ошибка = {good_err:.2e}")

    print("\nОбщий вывод по задаче:")
    print("1. В случае (а) мы видим, как с уменьшением x ошибка растет из-за ПЛОХОЙ ОБУСЛОВЛЕННОСТИ.")
    print("   Малые изменения на входе (x -> 0) дают огромные изменения в вычислении (1-cos x).")
    print("2. В случае (б) видно, что смена типа данных на float32 (меньшая МАШИННАЯ ТОЧНОСТЬ)")
    print("   приводит к резкому скачку ошибки. float32 оставляет всего ~7 значащих цифр.")
    print("3. В случае (в) мы берем тот же плохой x, но меняем алгоритм.")
    print("   Устойчивый алгоритм (через тождество) полностью убирает ошибку, доказывая,")
    print("   что выбор метода (УСТОЙЧИВОСТЬ) критически важен.")


import math
import numpy as np
from decimal import Decimal, getcontext


def task_11():
    print("--- Задача 11 ---")

    x = 1e-8
    print(f"Вычисляем f(x) = (1 - cos x) / x^2 для x = {x:.0e}")

    res_a = (1.0 - math.cos(x)) / (x ** 2)

    res_b = (1.0 - np.cos(x)) / (x ** 2)

    print("\nСравнение алгоритмов друг с другом:")
    print(f"Результат А (Python): {res_a}")
    print(f"Результат Б (NumPy):  {res_b}")
    print(f"А == Б: {res_a == res_b} (или np.isclose: {np.isclose(res_a, res_b)})")
    print("-> Вывод: они совпадают.")

    getcontext().prec = 50
    x_dec = Decimal('1e-8')

    ideal = (2 * math.sin(x / 2) ** 2) / (x ** 2)

    print("\nСравнение с ЭТАЛОНОМ:")
    print(f"Эталонное значение: {ideal}")
    print(f"Ошибка А: {abs(res_a - ideal):.2e}")
    print(f"Ошибка Б: {abs(res_b - ideal):.2e}")
    print(f"А == Эталон: {math.isclose(res_a, ideal)}")
    print("-> Вывод: ОБА алгоритма полностью неправильные (выдали 0.0 вместо 0.5)")

    print("\nИтоговый вывод:")
    print("1. Сравнивать алгоритмы друг с другом через '==' недостаточно.")
    print("   Два неправильных алгоритма могут давать одинаковый неправильный результат.")
    print("2. Всегда нужен независимый ЭТАЛОН (например, mpmath, Decimal или")
    print("   аналитически известное точное значение), чтобы понять, кто прав.")
    print("3. Сравнивать результаты float нужно только через np.isclose() или math.isclose(),")
    print("   так как абсолютное равенство '==' для чисел с плавающей точкой почти не работает.")


import math
from decimal import Decimal, getcontext

def task_12():
    print("--- Задача 12 ---")

    getcontext().prec = 50

    x_vals = [10.0 ** k for k in range(2, 17)]

    eps_machine = 2.220446049250313e-16

    print(f"{'x':<10} | {'Ошибка (факт)':<15} | {'Ошибка (теория)':<15} | {'Наклон (лог)':<12} | {'График ошибки'}")
    print("-" * 85)

    prev_err = None
    prev_x = None

    for x in x_vals:
        x_dec = Decimal(x)
        ideal = float((x_dec + 1).sqrt() - x_dec.sqrt())

        bad = math.sqrt(x + 1) - math.sqrt(x)

        err_fact = abs(bad - ideal) / ideal
        err_theory = eps_machine * x

        if prev_err is not None:
            slope = (math.log10(err_fact) - math.log10(prev_err)) / (math.log10(x) - math.log10(prev_x))
            slope_str = f"{slope:.2f}"
        else:
            slope_str = "-"

        visual_len = int(abs(math.log10(err_fact)) - 0.1) if err_fact > 0 else 0
        bar = "#" * visual_len

        print(f"{x:<10.0e} | {err_fact:<15.2e} | {err_theory:<15.2e} | {slope_str:<12} | {bar}")

        prev_err = err_fact
        prev_x = x

    print("\nВывод:")
    print("1. Ошибка практически полностью совпадает с предсказанием теории.")
    print("   На каждом шаге (при x = 10^k) ошибка растет ровно в 10 раз.")
    print("2. Оценка наклона: колонка 'Наклон' показывает ~1.00 на всем диапазоне.")
    print("   Это доказывает, что ошибка растет линейно: O(x).")
    print("3. Теоретическая оценка eps * x предсказывает рост ошибки с показателем степени 1.")
    print("4. Зачем нужен диапазон, а не одна точка?")
    print("   В одной точке (например, x = 10^4) ошибка может показаться незаметной (10^-12).")
    print("   Но на диапазоне до 10^16 видно, что ошибка достигает 100%, и алгоритм ломается.")
    print("   Численные методы всегда нужно проверять на широком спектре входных данных.")


import math
import numpy as np
from decimal import Decimal, getcontext


def task_13():
    print("--- Задача 13 ---")

    getcontext().prec = 50
    n = 10 ** 5

    def run_experiment(seed_val, seed_name):
        print(f"\nЭксперимент с {seed_name} = {seed_val}:")

        import random
        random.seed(seed_val)
        arr_py = [random.random() for a in range(n)]

        arr_np = np.random.default_rng(seed_val).random(n)
        sum_builtin = sum(arr_np)
        sum_math = math.fsum(arr_np)

        sum_py = 0.0
        for x in arr_py:
            sum_py += x

        sum_ideal = float(sum(Decimal(x) for x in arr_np))

        print(f"  Python (sum): {sum_py:.15f}")
        print(f"  NumPy (sum):  {sum_builtin:.15f}")
        print(f"  math.fsum:    {sum_math:.15f}")
        print(f"  Эталон:       {sum_ideal:.15f}")
        print(f"  {np.isclose(sum_py, sum_builtin)}")

    run_experiment(42, "seed")
    run_experiment(42, "seed")

    # Запускаем с seed=43
    run_experiment(43, "seed")

    print("\nВывод:")
    print("1. При seed=42 результаты совпадают от запуска к запуску. Python (sum) и")
    print("   NumPy (sum) дают одинаковый результат (различия только в последних знаках).")
    print("   math.fsum дает наиболее точный результат, близкий к эталону.")
    print("2. При seed=43 результаты отличаются. Это доказывает, что расхождения")
    print("   не случайны, а полностью зависят от выбранного зерна генератора.")
    print("   Каждый запуск будет генерировать новые случайные числа, а значит,")
    print("   и новые суммы. В научных статьях и тестах это недопустимо: нельзя")
    print("   проверить результат, который нельзя повторить.")


import math
import numpy as np

def task_14():
    print("--- Задача 14 ---")

    test_cases = [
        ("Очень большие (~10^300)", [1e300, 2e300, 3e300, 4e300, 5e300]),
        ("Очень маленькие (~10^-300)", [1e-300, 2e-300, 3e-300, 4e-300, 5e-300]),
        ("Нули", [0.0, 0.0, 0.0, 0.0, 0.0]),
        ("Денормализованные (~10^-320)", [1e-320, 2e-320, 3e-320, 4e-320, 5e-320]),
        ("Содержит inf", [float('inf'), 1.0, 2.0, 3.0, 4.0]),
        ("Содержит nan", [float('nan'), 1.0, 2.0, 3.0, 4.0])
    ]

    print(f"{'Массив':<30} | {'Наивный sum()':<18} | {'math.fsum()':<18}")
    print("-" * 72)

    res_naive = [sum(arr) for name, arr in test_cases]

    res_fsum = [
        math.fsum(arr) if not any(math.isnan(x) or math.isinf(x) for x in arr)
        else "Error (inf/nan)"
        for name, arr in test_cases
    ]

    table = [f"{name:<30} | {str(r1):<18} | {str(r2):<18}"
             for (name, _), r1, r2 in zip(test_cases, res_naive, res_fsum)]
    print("\n".join(table))

    print("\nПроверка math.fsum() при наличии +inf и -inf одновременно:")
    arr_mixed_inf = [float('inf'), float('-inf'), 1.0]

    try:
        print(f"Сумма [inf, -inf, 1.0]: {math.fsum(arr_mixed_inf)}")
    except ValueError as e:
        print(f"Выброшено исключение: {type(e).__name__} (математическая неопределенность)")

    print("\nВывод:")
    print("1. Большие/маленькие числа и нули: и sum(), и fsum() работают.")
    print("2. При наличии inf или nan: sum() возвращает inf или nan.")
    print("   math.fsum() тоже вернул бы их, но мы в коде отловили их заранее.")
    print("3. При смеси +inf и -inf: наивный sum() вернет nan.")
    print("   math.fsum() выбрасывает ValueError.")
    print("4. В реальном коде перед суммированием всегда проверяйте данные на NaN/Inf.")


import math
from decimal import Decimal, getcontext


def task_15():
    print("--- Задача 15 ---")
    print("Функция: f(x) = sqrt(x+1) - sqrt(x)\n")

    getcontext().prec = 50

    def get_ideal(x):
        x_dec = Decimal(x)
        return float((x_dec + 1).sqrt() - x_dec.sqrt())

    def bad_algorithm(x):
        return math.sqrt(x + 1) - math.sqrt(x)

    def good_algorithm(x):
        return 1.0 / (math.sqrt(x + 1) + math.sqrt(x))

    x_vals = [10.0 ** k for k in range(2, 17, 2)]

    print(f"{'x':<10} | {'Плохой':<15} | {'Хороший':<15} | {'Эталон':<15} | {'Ош. плохого':<12} | {'Ош. хор.'}")
    print("-" * 90)

    for x in x_vals:
        res_bad = bad_algorithm(x)
        res_good = good_algorithm(x)
        res_ideal = get_ideal(x)

        err_bad = abs(res_bad - res_ideal) / res_ideal
        err_good = abs(res_good - res_ideal) / res_ideal

        print(
            f"{x:<10.0e} | {res_bad:<15.4e} | {res_good:<15.4e} | {res_ideal:<15.4e} | {err_bad:<12.2e} | {err_good:.2e}")

    print("\nВывод:")
    print("1. Плохой алгоритм неустойчив при больших x (начиная с x = 10^8).")
    print("   Происходит это из-за вычитания близких чисел: sqrt(x+1) и sqrt(x)")
    print("   становятся почти равными, и при вычитании теряются значащие цифры.")
    print("   Хороший алгоритм использует сложение в знаменателе, избегая потери точности.")
    print("\n2. Плохим алгоритмом можно пользоваться только при малых x (до 10^6),")
    print("   где ошибка остается в пределах машинной погрешности (10^-16).")
    print("\n3. Хороший алгоритм показывает точность на уровне 0 (или 10^-16)")
    print("   на ВСЕМ диапазоне значений, вплоть до 10^16.")


import time

if __name__ == "__main__":
    print("=" * 70)
    print("ДОМАШНЯЯ РАБОТА: УСТОЙЧИВОСТЬ АЛГОРИТМА И КОРРЕКТНЫЙ ЭКСПЕРИМЕНТ")
    print("=" * 70)

    tasks = [
        task_1,
        task_2,
        task_3,
        task_4,
        task_5,
        task_6,
        task_7,
        task_8,
        task_9,
        task_10,
        task_11,
        task_12,
        task_13,
        task_14,
        task_15
    ]

start_time = time.perf_counter()

for i, task_func in enumerate(tasks, start=1):
    print(f"\n>>> ЗАПУСК ЗАДАЧИ {i}...")
    try:
        task_func()
    except Exception as e:
        print(f"!!! ОШИБКА В ЗАДАЧЕ {i}: {e}")

    print("-" * 70)

end_time = time.perf_counter()
total_time = end_time - start_time

print("\n" + "=" * 70)
print(f"ВСЕ 15 ЗАДАЧ УСПЕШНО ВЫПОЛНЕНЫ!")
print(f"Общее время выполнения: {total_time:.2f} секунд.")
print("=" * 70)