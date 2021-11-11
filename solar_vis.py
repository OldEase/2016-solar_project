
import pygame
"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие графические объекты и перемещающие их на экране, принимают физические координаты
"""

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 800
"""Ширина окна"""

window_height = 800
"""Высота окна"""

scale_factor = None
"""Масштабирование экранных координат по отношению к физическим.
Тип: float
Мера: количество пикселей на один метр."""



def calculate_scale_factor(func_max_distance, func_window_height, func_window_width):
    """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
    func_scale_factor = 0.4*min(func_window_height, func_window_width)/func_max_distance
    print('Scale factor:', func_scale_factor)
    return func_scale_factor


def scale_x(x, func_scale_factor, func_window_width):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    Параметры:

    **x** — x-координата модели.
    """

    return int(round(x*func_scale_factor)) + func_window_width//2


def scale_y(y, func_scale_factor, func_window_height):
    """Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

    Параметры:

    **y** — y-координата модели.
    """

    return -int(round(y*func_scale_factor)) + func_window_height//2


def create_star_image(func_space, func_star, func_scale_factor, func_window_height, func_window_width):
    """Создаёт отображаемый объект звезды.

    Параметры:

    **space** — холст для рисования.
    **star** — объект звезды.
    """

    x = scale_x(func_star.x, func_scale_factor, func_window_width)
    y = scale_y(func_star.y, func_scale_factor, func_window_height)
    r = func_star.R
    pygame.draw.circle(func_space, func_star.color, (x, y), r, 0)


def create_planet_image(func_space, func_planet, func_scale_factor, func_window_height, func_window_width):
    """Создаёт отображаемый объект планеты.

    Параметры:

    **space** — холст для рисования.
    **planet** — объект планеты.
    """
    x = scale_x(func_planet.x, func_scale_factor, func_window_width)
    y = scale_y(func_planet.y, func_scale_factor, func_window_height)
    r = func_planet.R
    pygame.draw.circle(func_space, func_planet.color, (x, y), r, 0)


def update_system_name(space, system_name):
    """Создаёт на холсте текст с названием системы небесных тел.
    Если текст уже был, обновляет его содержание.

    Параметры:

    **space** — холст для рисования.
    **system_name** — название системы тел.
    """
    pass
    '''space.create_text(30, 80, tag="header", text=system_name, font=header_font)'''


def update_object_position(space, body):
    """Перемещает отображаемый объект на холсте.

    Параметры:

    **space** — холст для рисования.
    **body** — тело, которое нужно переместить.
    """
    pass
    x = scale_x(body.x)
    y = scale_y(body.y)
    r = body.R
    '''if x + r < 0 or x - r > window_width or y + r < 0 or y - r > window_height:
        space.coords(body.image, window_width + r, window_height + r,
                     window_width + 2*r, window_height + 2*r)  # положить за пределы окна
    space.coords(body.image, x - r, y - r, x + r, y + r)'''


if __name__ == "__main__":
    print("This module is not for direct call!")
