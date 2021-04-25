from docxtpl import DocxTemplate
from datetime import date
import logging
import db


def consent_personal_data(first_name, last_name, passport, pass_other_info, reg_address, aim, name_of_company):
    doc = DocxTemplate("consent_personal_data.docx")
    logging.info("Opened consent_personal_data.docx template")
    current_date = date.today()
    day = current_date.day
    temp_month = current_date.month
    month = "temp"
    if temp_month == 1:
        month = "января"
    elif temp_month == 2:
        month = "февраля"
    elif temp_month == 3:
        month = "марта"
    elif temp_month == 4:
        month = "апреля"
    elif temp_month == 5:
        month = "мая"
    elif temp_month == 6:
        month = "июня"
    elif temp_month == 7:
        month = "июля"
    elif temp_month == 8:
        month = "августа"
    elif temp_month == 9:
        month = "сентября"
    elif temp_month == 10:
        month = "октября"
    elif temp_month == 11:
        month = "ноября"
    elif temp_month == 12:
        month = "декабря"
    year = current_date.year
    context = {'first_name': first_name, 'last_name': last_name, 'passport': passport, 'pass_other_info': pass_other_info,
               'registration_address': reg_address, 'aim': aim, 'name_of_company': name_of_company,
               'day': day, 'month': month, 'year': year, 'place_to_sign': "{{ place_to_sign }}"}
    doc.render(context)
    name_of_file = "consent_personal_data_" + first_name + last_name + ".docx"
    doc.save(name_of_file)
    logging.info('Doc consent_personal_data_' + first_name + last_name + '.docx filled in and saved successfully')
    return name_of_file


def filling_and_uploading():
    # print("Имя:")
    # f_name = str(input())
    # print("Фамилия:")
    # l_name = str(input())
    print("Телефон:")
    tel_number = str(input())
    aim = "test"

    con = db.sql_connection()
    data = db.sql_find_person(con, tel_number)

    id = data[0][0]
    first_name = data[0][1]
    last_name = data[0][2]
    pass_number = data[0][3]
    pass_info = data[0][4]
    reg_address = data[0][5]

    name = first_name + " " + last_name

    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('Send request to FILL IN docx template for ' + name)

    return [consent_personal_data(first_name, last_name, pass_number, pass_info, reg_address, aim, "Шереметьево"), name, id]



# if __name__ == '__main__':
#     main()
