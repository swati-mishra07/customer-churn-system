def create_features(df):
    df['BalanceSalaryRatio'] = df['Balance'] / (df['EstimatedSalary'] + 1)
    df['TenureByAge'] = df['Tenure'] / (df['Age'] + 1)
    df['ProductsPerTenure'] = df['NumOfProducts'] / (df['Tenure'] + 1)
    
    return df