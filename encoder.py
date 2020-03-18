import pandas as pd

# Target encoding
def cat_encoder(df, i):
    Y=str(df.columns[2])
    X=str(df.columns[i])

    if pd.api.types.is_object_dtype(df.iloc[:, i]) or (pd.api.types.is_categorical_dtype(df.iloc[:, i])):
        encoding = df.groupby([X]).agg({Y: ['std']}).reset_index()
        dt = df.copy()
        dt = dt.merge(encoding, on=X, how='left')
        dt.columns = [*dt.columns[:-1], 'Encoded']

        return dt[dt.columns[-1]]

    else:
        return


data = pd.read_csv('filepath')
col_index=1
c = cat_encoder(data, col_index)
