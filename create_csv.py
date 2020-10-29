import pandas as pd


def fun_csv(id, file_name, info_1):

    df = pd.read_sql_query("select * from sql_flask_excel_table where id = '" + str(id) + "'", con=info_1)
    df.to_csv(file_name, index=False)

    print(df)

    return file_name

                    ############(method-2)#####################

"""

    cur = mydb.cursor()

    query = "select * from sql_flask_excel_table where id = '" + str(a) + "'"

    cur.execute(query)

    s = cur.fetchall()

    total_list = []
    for i in s:

        all_dict = {'id': i[0], 'name_info': i[1], 'mail': i[2], 'contact': i[3], 'address': i[4]}
        total_list.append(all_dict)

    list_columns = ['id', 'name_info', 'mail', 'contact', 'address']
    csv_path = 'C:/Users/Hemanth Y/Desktop/csv_file'

    try:
        with open(csv_path, 'w') as csv_data:
            writer = csv.DictWriter(csv_data, fieldnames=list_columns)
            writer.writeheader()

            for data in total_list:
                writer.writerow(data)
    except IOError:
        print("I/O error")

    return jsonify({'file_name': csv_path})
    
    """
