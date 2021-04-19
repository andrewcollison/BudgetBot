import matplotlib.pyplot as plt
import numpy as np


class budget_expenses():

    def __init__(self, range):       
        self.range = range

    def cat_expenses(self, act_data, bud_data):
        # print(self.range)
        # print(act_data)
        # print(bud_data)
        if self.range == 'weekly':
            bud_data = bud_data/52
        elif self.range == 'monthly':
            bud_data = bud_data/12

        else:
            print('do nothing')

        
        

        # x_bud = np.arange(len(bud_data.index))
        # x_act = np.arange(len(act_data.index)) 
        width = 0.4
        fig, ax = plt.subplots(1, sharex=False)

        rect1 = ax.bar(bud_data.index, bud_data, label = 'budget data', width = width+0.4)
        # ax.set_xticks(bud_data.index)

        rect2 = ax.bar(act_data.index, act_data, label = 'Expenses', width = width) 
        plt.legend()
        plt.show()


def main():
    dispData = budget_expenses("weekly")
    # dispData.cat_expenses


if __name__ == "__main__":
    main()