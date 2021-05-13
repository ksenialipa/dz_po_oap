from fem.fem_tools import load_model
from fem.fem_tools import FEMComput

def main():
    # Загружаем конструкцию из файла
    beam = load_model('model.txt')

    # Передаём конструкцию расчётчику
    comp = FEMComput(beam)

    # Выводим на экран расчёт
    comp.display_results()

    # Сохраняем расчёт в отдельном файле
    comp.save_results("results.txt", comment="Расчёт по моей домашке")


if __name__ =="__main__":
    main()
