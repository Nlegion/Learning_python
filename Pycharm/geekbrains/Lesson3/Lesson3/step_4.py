PI = 3.1415


def show_circle_area(r):  # procedure bcs no return
    area = PI * r ** 2
    print(f'площадь окружности радиуса {radius} равна {area:.2f}')
    # return None


radius = 5
show_circle_area(radius)
# print(show_circle_area(radius))

radius = 15
show_circle_area(radius)

radius = 25
show_circle_area(radius)
