import numpy as np
import matplotlib.pyplot as plt
import os


def task_1():
    print("--- Задача 1 ---")

    k = np.arange(6)
    x = np.cos(2 * np.pi * k / 6)
    y = np.sin(2 * np.pi * k / 6)

    hexagon = np.column_stack((x, y))
    hexagon = np.vstack((hexagon, hexagon[0]))

    theta = np.deg2rad(45)
    rot_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

    reflect_matrix = np.array([
        [0, 1],
        [1, 0]
    ])

    hex_rotated = hexagon @ rot_matrix.T
    hex_reflected = hexagon @ reflect_matrix.T

    fig, ax = plt.subplots(figsize=(7, 7))

    ax.plot(hexagon[:, 0], hexagon[:, 1], '-o', color='gray', label='Исходный', linewidth=2)
    ax.plot(hex_rotated[:, 0], hex_rotated[:, 1], '-s', color='steelblue', label='Поворот на 45°', linewidth=2)
    ax.plot(hex_reflected[:, 0], hex_reflected[:, 1], '-^', color='crimson', label='Отражение y=x', linewidth=2)

    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(0, color='black', lw=0.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title("Поворот и отражение шестиугольника")
    ax.legend()

    plt.savefig("task_1_hexagon.png", dpi=150, bbox_inches='tight')
    plt.show()

    print("\nОтвет на вопрос:")
    print("Отраженный шестиугольник выглядит 'повернутым', потому что матрица отражения")
    print("относительно прямой y=x ([[0, 1], [1, 0]]) математически идентична матрице")
    print("поворота на 90 градусов. То есть отражение y=x визуально неотличимо от поворота")
    print("на 90° в двумерном пространстве.")


def task_2():
    print("\n--- Задача 2 ---")

    rng = np.random.default_rng(42)
    points = rng.uniform(-2, 2, size=(200, 2))

    S = np.array([
        [1.5, 0.0, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.0, 1.0]
    ])

    theta = np.deg2rad(60)
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0.0],
        [np.sin(theta), np.cos(theta), 0.0],
        [0.0, 0.0, 1.0]
    ])

    T = np.array([
        [1.0, 0.0, 1.0],
        [0.0, 1.0, -1.0],
        [0.0, 0.0, 1.0]
    ])

    M = T @ R @ S

    points_h = np.hstack((points, np.ones((200, 1))))

    transformed_h = points_h @ M.T
    transformed = transformed_h[:, :2]

    T_inv = np.array([
        [1.0, 0.0, -1.0],
        [0.0, 1.0, 1.0],
        [0.0, 0.0, 1.0]
    ])

    theta_inv = np.deg2rad(-60)
    R_inv = np.array([
        [np.cos(theta_inv), -np.sin(theta_inv), 0.0],
        [np.sin(theta_inv), np.cos(theta_inv), 0.0],
        [0.0, 0.0, 1.0]
    ])

    S_inv = np.array([
        [1 / 1.5, 0.0, 0.0],
        [0.0, 1 / 0.5, 0.0],
        [0.0, 0.0, 1.0]
    ])

    M_inv = S_inv @ R_inv @ T_inv

    restored_h = transformed_h @ M_inv.T
    restored = restored_h[:, :2]

    is_equal = np.allclose(points, restored, atol=1e-12)
    print(f"Проверка восстановления (np.allclose): {is_equal}")

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.scatter(points[:, 0], points[:, 1], color='gray', alpha=0.4, label='Исходные', s=20)
    ax.scatter(transformed[:, 0], transformed[:, 1], color='crimson', alpha=0.7, label='Преобразованные', s=20)
    ax.scatter(restored[:, 0], restored[:, 1], color='green', marker='x', alpha=0.8, label='Восстановленные', s=20)

    ax.axhline(0, color='black', lw=0.5)
    ax.axvline(0, color='black', lw=0.5)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title("Исходные, преобразованные и восстановленные точки")
    ax.legend()

    plt.savefig("task_2_composition.png", dpi=150, bbox_inches='tight')
    plt.show()

    print("\nОтвет на вопрос:")
    print("Обратные преобразования нужно применять строго в обратном порядке.")
    print("Матрица композиции имеет вид M = T * R * S. Обратная матрица — это")
    print("M_inv = S_inv * R_inv * T_inv. Если применить их в прямом порядке,")
    print("результат будет неверным, так как сначала нужно отменить последнее действие (T),")
    print("затем среднее (R) и только потом первое (S).")


if __name__ == "__main__":
    task_1()
    task_2()