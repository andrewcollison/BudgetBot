import seaborn as sns
import matplotlib.pyplot as plt

class displayData():        

    def catData(df):
        parent_cats = df.parentCategory.unique()
        print(parent_cats)
        sum_expense_parent = []
        for i in range(len(parent_cats)):
            total = 0
            for idx in range(len(df['value'])):
                if df['parentCategory'][idx] == parent_cats[i]:
                    total = total + float(df['value'][idx]) 
            # print(total)

            sum_expense_parent.append(abs(total))
        print(sum_expense_parent)


        sub_cats = df.subCategory.unique()
        print(sub_cats)
        sum_expense_sub = []
        for i in range(len(sub_cats)):
            total = 0
            for idx in range(len(df['value'])):
                if df['subCategory'][idx] == sub_cats[i]:
                    total = total + float(df['value'][idx]) 
            # print(total)

            sum_expense_sub.append(abs(total))
        print(sum_expense_sub)

        # Filter cat
        res_parent = dict(zip(parent_cats, sum_expense_parent))
        if 'None' in res_parent: del res_parent['None']

        res_sub = dict(zip(sub_cats, sum_expense_sub))
        if 'None' in res_sub: del res_sub['None']


        plt.bar(res_sub.keys(), res_sub.values())
        plt.title('Expenses by Category')
        plt.show()