import numpy as np
from PIL import Image

DIRECTIONS = {'top': 0, 'right': 1, 'bottom': 2, 'left': 3}

def ant_path(
    board_size: tuple[int, int] = (1024, 1024),
    init_ant_pos: tuple[int, int] = (512, 512),
    init_direction: str = 'top'
) -> tuple[list[list[int]], int]:
    """
    Функция нахождения пути муровья и количества: шагов, черных клеток.
    
    Аргументы:
    board_size -- размер поля
    init_ant_pos -- начальная позиция муравья
    init_direction  -- начальное направление муравья
    """
    # Ширина и высота поля, по которому движется муравей
    width, height = board_size

    # Ячейка, в которой находится муравей
    h_ant_pos, v_ant_pos = init_ant_pos

    # Направление муравья
    direction = DIRECTIONS[init_direction]

    # Создаем 2D-матрицу (поле) белого цвета (число 255 в RGB-системе)
    # размером width х height, по которому буде двигаться муравей
    matrix = [[255] * width for _ in range(height)]

    # Инициализируем число черных клеток
    black_cells = 0

    # Выполняем цикл, пока муравей не дойдет до любой границы поля
    while 0 <= h_ant_pos < width and 0 <= v_ant_pos < height:
        # если клетка белая...
        if matrix[h_ant_pos][v_ant_pos] == 255:
            # ... муравей поворачивает вправо
            direction = (direction + 1) % 4
            # инвертируем цвет текущей клетки на противоположный
            # и увеличиваем счетчик количества черных клеток
            matrix[h_ant_pos][v_ant_pos] = 0
            black_cells += 1
        # иначе, клетка черная...
        else:
            # ... и муравей поворачивает влево
            direction = (direction - 1) % 4
            # инвертируем цвет текущей клетки на противоположный
            # и уменьшаем счетчик количества черных клеток
            matrix[h_ant_pos][v_ant_pos] = 255
            black_cells -= 1
        
        # Муравей переходит в соседнюю клетку, в зависимости от стороны,
        # в которую направлен
        match direction:
            case 0: v_ant_pos -= 1
            case 1: h_ant_pos += 1
            case 2: v_ant_pos += 1
            case 3: h_ant_pos -= 1

    return matrix, black_cells

def main():
    """
    Основная функция. Вызывает функцию подсчета с заданными значениями.
    Выводит на печать результат. Формирует и сохраняет изображение.
    """
    # Размеры поля, положение и направление по условиям задачи
    board_size = (1024, 1024)
    init_ant_pos = (512, 512)
    init_direction = 'top'

    ant_path_matrix, black_cells = ant_path(
        board_size, init_ant_pos, init_direction
    )

    result_ant_path_array = np.asarray([*ant_path_matrix], np.dtype('uint8'))

    print(f'Количество черных клеток поля, когда муравей дошел до границы: '
          f'{black_cells}')
    print(f'Результирующая матрица:\n{result_ant_path_array}')

    img = Image.fromarray(result_ant_path_array, mode='L').convert('1')
    img.save(f'antpath_black_cells={black_cells}.png')


if __name__ == '__main__':
    main()
