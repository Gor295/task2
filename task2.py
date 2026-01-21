import sys
import math

def point_position_relative_to_ellipse(x_center, y_center, rx, ry, x, y):
    """
    Определяет положение точки относительно эллипса
    Возвращает:
    0 - на эллипсе
    1 - внутри
    2 - снаружи
    """
    # Вычисляем значение уравнения эллипса
    if rx == 0 or ry == 0:
        return 2  # вырожденный эллипс
    
    # Смещаем координаты относительно центра
    dx = x - x_center
    dy = y - y_center
    
    # Уравнение эллипса: (x^2 / rx^2) + (y^2 / ry^2) = 1
    value = (dx * dx) / (rx * rx) + (dy * dy) / (ry * ry)
    
    # Определяем положение с учетом погрешности вычислений
    epsilon = 1e-10
    
    if abs(value - 1.0) < epsilon:
        return 0  # на эллипсе
    elif value < 1.0:
        return 1  # внутри
    else:
        return 2  # снаружи

def main():
    if len(sys.argv) != 3:
        print("Использование: python task2.py <файл_эллипса> <файл_точек>")
        sys.exit(1)
    
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]
    
    try:
        # Чтение параметров эллипса
        with open(ellipse_file, 'r') as f:
            lines = f.readlines()
            center_line = lines[0].strip().split()
            radius_line = lines[1].strip().split()
            
            x_center = float(center_line[0])
            y_center = float(center_line[1])
            rx = float(radius_line[0])
            ry = float(radius_line[1])
        
        # Чтение координат точек
        with open(points_file, 'r') as f:
            points = []
            for line in f:
                coords = line.strip().split()
                if len(coords) >= 2:
                    x = float(coords[0])
                    y = float(coords[1])
                    points.append((x, y))
        
        # Определение положения каждой точки
        for point in points:
            position = point_position_relative_to_ellipse(
                x_center, y_center, rx, ry, point[0], point[1]
            )
            print(position)
            
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка: некорректные данные в файле - {e}")
        sys.exit(1)
    except IndexError as e:
        print(f"Ошибка: недостаточно данных в файле - {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()