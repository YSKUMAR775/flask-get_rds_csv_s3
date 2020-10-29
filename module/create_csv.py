import pandas as pd


def fun_csv(id, file_name, info_1):

    df = pd.read_sql_query("select * from sql_flask_excel_table where id = '" + str(id) + "'", con=info_1)
    df.to_csv(file_name, index=False)

    print(df)

    return file_name
