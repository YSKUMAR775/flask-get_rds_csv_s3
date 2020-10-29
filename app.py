from flask import Flask, jsonify
from module import upload_s3, database_connection, create_csv

app = Flask(__name__)


@app.route('/get/<id>', methods=['Get'])
def fn_1(id):

    file_name = 'student_data.csv'
    info_1 = database_connection.fun_connect()
    info_2 = create_csv.fun_csv(id, file_name, info_1)
    info_3 = upload_s3.fun_upload(info_2)

    return jsonify(info_3)


if __name__ == '__main__':
    app.run(debug=True)
