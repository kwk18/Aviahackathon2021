from docxtpl import DocxTemplate, InlineImage
import logging


def sign_doc(name):
    name_of_doc = "consent_personal_data_" + name + ".docx"
    doc = DocxTemplate(name_of_doc)
    logging.info(name_of_doc + " opened")
    sign_img = InlineImage('signature.png')
    context = {'place_to_sign': sign_img}
    doc.render(context)
    name_to_save = "consent_personal_data_" + name + "_signed" + ".docx"
    doc.save(name_to_save)
    logging.info(name_to_save + " signed and saved successfully")


if __name__ == "__main__":
    name = "Вася Пупкин"

    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
    logging.info('Send request to SIGN doc file for ' + name)

    sign_doc(name)
