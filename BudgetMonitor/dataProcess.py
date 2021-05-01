import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class processData(): 

    def __init__(self):       
        pass

    def acctual_expenses(self, df):
        df_sub = df.groupby(df.subCategory, as_index = True)['value'].sum()
        
        df_sub.drop(index='None' , inplace=True)
        df_sub = abs(df_sub)
        # print(df_sub)
        return df_sub
        

    def budget_expenses(self):
        # Load in data from budget spreadsheet        
        df = pd.read_excel('costs.xlsx', 'costs')
        df['YearlyCosts'] = None

        # Weekly 
        df['YearlyCosts'] = (df.Cost * 52).where(df['Period'] == 'weekly', other = df.YearlyCosts)
        # Monthly
        df['YearlyCosts'] = (df.Cost * 12).where(df['Period'] == 'monthly', other = df.YearlyCosts)
        # Quarterly
        df['YearlyCosts'] = (df.Cost * 4).where(df['Period'] == 'quarterly', other = df.YearlyCosts)
        # Yearly
        df['YearlyCosts'] = (df.Cost).where(df['Period'] == 'yearly', other = df.YearlyCosts)          

        # Return table that has budget by category on a weekly, monthly and yearly basis
        # df_parent = df.groupby(df.ParentCategory)['YearlyCosts'].sum()
        df_sub = df.groupby(df.SubCategory, as_index = True)['YearlyCosts'].sum()
        
        return df_sub
        
        


def main():
    df = processData()
    df.budget_expenses()

if __name__ == "__main__":
    main()