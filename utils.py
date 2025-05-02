# Цей файл містить функції, які можна протестувати (функція matrix_multiplication буде тестуватися, але з файлу matrix.py)
import colorsys


def hsv_to_rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


# Функція для розрахунку координат Лоренца
def lorenz_step(x, y, z, sigma, rho, beta, dt):
    dx = (sigma * (y - x)) * dt
    dy = (x * (rho - z) - y) * dt
    dz = (x * y - beta * z) * dt
    return x + dx, y + dy, z + dz
