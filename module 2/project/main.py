import pandas as pd
import matplotlib.pyplot as plt
from random import randint


class Project:
    def __init__(self, path):
        self.df = pd.read_csv(path)
        self.markers = ['^', '*', 'o', 'x']

    def task1(self):
        min_bedrooms = self.df[self.df['price']
                               == self.df['price'].min()]['bedrooms'].min()
        bedrooms_less_equal_bathrooms = (
            self.df['bedrooms'] <= self.df['bathrooms']).sum()
        min_price_guestroom = self.df[self.df['guestroom']
                                      == 'yes']['price'].min()
        ac_proportion = round(
            (self.df[(self.df['price'] >= 2000000) & (
                self.df['price'] <= 5000000)]['airconditioning'] == 'yes').mean()*100, 2)
        print(f"""
            Количество спален в самом дешёвом доме: {min_bedrooms}
            Количество домов, в которых количество спален не больше количества ванных: {bedrooms_less_equal_bathrooms}
            Цена самого дешёвого дома с гостевой комнатой: {min_price_guestroom}
            Доля домов с кондиционированием среди домов ценой от 2.000.000 до 5.000.000: {ac_proportion}%
            """)

    def task2(self):
        plt.figure(figsize=(10, 6))

        colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown']
        for i in range(self.df['parking'].nunique()):
            subset = self.df[self.df['parking'] == i]
            plt.scatter(subset['price'], subset['area'], alpha=0.6, marker=self.markers[randint(0, 3)],
                        c=colors[i], label=f'Парковочных мест: {i}')

        plt.xlabel('Цена')
        plt.ylabel('Площадь')
        plt.title(
            'Отношение цены и площади для различного количества парковочных мест')

        plt.legend()
        plt.grid(True)
        plt.show()

    def task3(self):
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))

        features = ['guestroom', 'basement', 'hotwaterheating', 'prefarea']
        titles = ['Наличие гостевой комнаты', 'Наличие подвала',
                  'Наличие обогрева с помощью горячей воды', 'Наличие предбанника']
        colors = ['red', 'blue']

        for i, ax in enumerate(axes.flatten()):
            feature = features[i]
            for j, value in enumerate(self.df[feature].unique()):
                subset = self.df[self.df[feature] == value]
                ax.scatter(subset['price'], subset['area'], marker=self.markers[randint(0, 3)], alpha=0.5, c=colors[j],
                           label=f'{titles[i].capitalize()}: {value}')

            ax.set_xlabel('Цена')
            ax.set_ylabel('Площадь')
            ax.set_title(titles[i])
            ax.legend()
            ax.grid(True)

        plt.tight_layout()
        plt.show()

    def task4(self):
        plt.figure(figsize=(10, 6))

        ac_houses = self.df[self.df['airconditioning']
                            == 'yes']['price']
        plt.hist(ac_houses, bins=20, alpha=0.5,
                 color='blue', label='Наличие кондиционирования')
        non_ac_houses = self.df[self.df['airconditioning']
                                == 'no']['price']

        plt.hist(non_ac_houses, bins=20, alpha=0.5,
                 color='green', label='Отстутсвие кондиционирования')
        plt.xlabel('Цена')
        plt.ylabel('количество домов')
        plt.title('Распределение цены')

        plt.legend()
        plt.grid(True)
        plt.show()

    def task_switch(self, num):
        if num == 1:
            self.task1()
        elif num == 2:
            self.task2()
        elif num == 3:
            self.task3()
        elif num == 4:
            self.task4()
        else:
            print('Ошибка! Неверный номер')
        print('Задание номер:', end=' ')


if __name__ == '__main__':
    prj = Project('./Housing.csv')
    print('Введите номер задания (1-4) или `q` для выхода\nЗадание номер:', end=' ')
    while True:
        task_num = input()
        if task_num.lower() == 'q':
            break
        elif task_num.isdigit() and int(task_num) in range(1, 5):
            prj.task_switch(int(task_num))
        else:
            print('Некорректный ввод, попробуйте снова')
