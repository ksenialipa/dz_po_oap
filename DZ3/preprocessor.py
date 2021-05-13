from fem.fem_tools import Beam
from fem.fem_tools import save_model

def main():
    # Длина одного участка
    L = 1
    # Площадь поперечного сечения
    F = 1
    # Модуль Юнга
    E = 1
    # приложенные силы
    P1 = 2*E*F
    P2 = 3*E*F

    # Жёсткость пружинки
    C = 2*E*F/L

    # Заготовка для стержневой системы
    beam = Beam()

    # Собираем конструкцию
    rod1 = beam.add_rod(E, F, L=L)
    rod2 = beam.add_rod(E, F, n1=rod1.node2, L=L)
    rod3 = beam.add_rod(E, F, n1=rod2.node2, L=L)
    spring4 = beam.add_spring(C, n1=rod1.node2, L=L)

    # Нужно добавить заделки
    rod1.node1.add_pinning()
    beam.add_pinning(spring4.node2)

    # Добавляем усилия
    beam.add_point_force(rod2.node2, P1)
    rod3.node2.add_point_force(P2)

    # Сохраняем конструкцию в файл модели
    save_model(beam, 'model.txt', comment='Моё домашнее задание')


if __name__ =="__main__":
    main()
