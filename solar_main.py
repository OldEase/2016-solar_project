import pygame
from solar_vis import *
from solar_model import *
from solar_input import *

pygame.init()

FPS = 144
x_screen_size = 800
y_screen_size = 800
screen = pygame.display.set_mode((x_screen_size, y_screen_size))

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

physical_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

displayed_time = None
"""Отображаемое на экране время.
Тип: переменная tkinter"""

input_text = ''

time_step = 1000
"""Шаг по времени при моделировании.
Тип: float"""

space_objects = []
"""Список космических объектов."""


def text(
        screen,
        font_coord,
        font_size,
        font_color,
        text
):
    '''
    function to draw text
    :param screen: screen to draw on
    :param font_coord: (x, y) - position of text
    :param font_size: size of text
    :param font_color: color of text
    :param text: text to render
    :return: None
    '''
    score_font = pygame.font.Font(None, font_size)
    score_result = score_font.render(str(text), True, font_color)
    screen.blit(score_result, font_coord)


def choose_max_distance(func_objects):
    func_max_distance = 0
    for obj in func_objects:
        if func_max_distance ** 2 < obj.x ** 2 + obj.y ** 2:
            func_max_distance = (obj.x ** 2 + obj.y ** 2) ** 0.5
    return func_max_distance


def execution(perform_execution):
    """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    screen.fill((0, 0, 0))
    if perform_execution:
        recalculate_space_objects_positions(space_objects, time_step)
    for obj in space_objects:
        create_planet_image(screen, obj, scale_factor, y_screen_size, x_screen_size)
    pygame.display.update()
    '''global physical_time
    global displayed_time
    recalculate_space_objects_positions(space_objects, time_step.get())
    for body in space_objects:
        update_object_position(space, body)
    physical_time += time_step.get()
    displayed_time.set("%.1f" % physical_time + " seconds gone")'''

    '''if perform_execution:
        space.after(101 - int(time_speed.get()), execution)'''


def start_execution():
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """
    pass
    '''global perform_execution
    perform_execution = True
    start_button['text'] = "Pause"
    start_button['command'] = stop_execution

    execution()
    print('Started execution...')'''


def stop_execution():
    """Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.
    """
    pass
    '''
    global perform_execution
    perform_execution = False
    start_button['text'] = "Start"
    start_button['command'] = start_execution
    print('Paused execution.')'''


def open_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (150, 400, 500, 50), 0)
    text(screen, (160, 410), 50, (0, 0, 0), input_text)
    text(screen, (50, 350), 50, (255, 255, 255), 'Введите название файла для считывания')



    '''global space_objects
    global perform_execution
    perform_execution = False
    for obj in space_objects:
        space.delete(obj.image)  # удаление старых изображений планет
    in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
    space_objects = read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    calculate_scale_factor(max_distance)

    for obj in space_objects:
        if obj.type == 'star':
            create_star_image(space, obj)
        elif obj.type == 'planet':
            create_planet_image(space, obj)
        else:
            raise AssertionError()'''


def save_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    pass
    '''out_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
    write_space_objects_data_to_file(out_filename, space_objects)'''


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    '''
    global physical_time
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button

    print('Modelling started!')
    physical_time = 0

    root = tkinter.Tk()
    # космическое пространство отображается на холсте типа Canvas
    space = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
    space.pack(side=tkinter.TOP)
    # нижняя панель с кнопками
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)

    start_button = tkinter.Button(frame, text="Start", command=start_execution, width=6)
    start_button.pack(side=tkinter.LEFT)

    time_step = tkinter.DoubleVar()
    time_step.set(1)
    time_step_entry = tkinter.Entry(frame, textvariable=time_step)
    time_step_entry.pack(side=tkinter.LEFT)

    time_speed = tkinter.DoubleVar()
    scale = tkinter.Scale(frame, variable=time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)

    load_file_button = tkinter.Button(frame, text="Open file...", command=open_file_dialog)
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Save to file...", command=save_file_dialog)
    save_file_button.pack(side=tkinter.LEFT)

    displayed_time = tkinter.StringVar()
    displayed_time.set(str(physical_time) + " seconds gone")
    time_label = tkinter.Label(frame, textvariable=displayed_time, width=30)
    time_label.pack(side=tkinter.RIGHT)

    root.mainloop()
    print('Modelling finished!')

if __name__ == "__main__":
    main()'''



pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    fps = clock.get_fps()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                finished = True
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
    open_file_dialog()
    pygame.display.update()
finished = False

space_objects = read_space_objects_data_from_file(input_text)

max_distance = choose_max_distance(space_objects)

scale_factor = calculate_scale_factor(max_distance, y_screen_size, x_screen_size)

while not finished:
    clock.tick(FPS)
    fps = clock.get_fps()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    perform_execution = True
    execution(perform_execution)

