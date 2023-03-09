""" Main module """
from os import listdir
from os.path import isfile, join
import csv
import os

def insert_in_a_string(source_str, insert_str, pos):
    """ Insere uma string em uma outra string pelo index"""
    return source_str[:pos] + insert_str + source_str[pos:]

def heading_list_to_text(list_heading):
    """ Tranforma uma lista de strings em uma grande string"""
    text = "".join(list_heading)
    return text

def dict_rows(list_heading, list_data):
    """ Cria o dicionario para inclusão dos dados e do header do arquivo csv"""
    list_rows = []
    float_data = []
    for heading_element in list_heading:
        if "VALOR-PERCAPITA" in heading_element:
            float_data.append(heading_element)
    for data_row in list_data:
        data_row_list = data_row[0].split(",")
        dict_row = {}
        for iteration, data_row in enumerate(data_row_list):
            if list_heading[iteration] in float_data:
                float_number = float(data_row)/100
                dict_row[list_heading[iteration]] = f"{float_number:.2f}"
            elif list_heading[iteration] == "FAIXA-ETARIA":
                listed_string = list(data_row)
                listed_string[3] = "0" if listed_string[3] == "9" else listed_string[3]
                listed_string[3:3]= ["-"]
                data_row = "".join(listed_string)
                dict_row[list_heading[iteration]] = data_row
            else:
                dict_row[list_heading[iteration]] = data_row
        list_rows.append(dict_row)
    return list_rows

if __name__ == '__main__':

    directory = os.getcwd()

    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]

    for file_name in onlyfiles:
        if file_name not in ["serv_config.REF", "pens_config.REF"]:
            file_TXT = directory+"\\"+file_name
            file_REF_serv = directory+"\\serv_config.REF"
            file_REF_pens = directory+"\\pens_config.REF"
            chars_count = []
            headings = []
            lines = []

            with open(file_TXT, encoding="utf8") as f:
                for line in f:
                    lines.append(line.strip())
            
            FILE_REF = ""

            if len(lines[0]) == 107:
                FILE_REF = file_REF_serv
            else:
                FILE_REF = file_REF_pens

            with open(FILE_REF, encoding="utf8") as f:
                for line in f:
                    char_count = line[-4:]
                    chars_count.append(char_count.strip())
                    heading = line[:40]
                    headings.append(heading.strip())

            lines_csv = []
            for line in lines:
                PLUS = 0
                CHAR_INDEX = 0
                for i in range(len(chars_count)-1):
                    char_count = chars_count[i]
                    # Verifica a um indicativo de float 09,2
                    if char_count.isdigit():
                        CHAR_INDEX += int(char_count) + PLUS
                    else:
                        list_char_count = char_count.split(",")
                        char_count_intern = int(list_char_count[0]) + int(list_char_count[1])
                        CHAR_INDEX += int(char_count_intern) + PLUS

                    line = insert_in_a_string(line, ",", CHAR_INDEX)
                    PLUS = 1
                line = [line]
                lines_csv.append(line)

            with open(file_name + ".csv", "w", encoding="utf8", newline="") as result_file:
                rows = dict_rows(headings, lines_csv)
                fieldnames = headings
                writer = csv.DictWriter(result_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in rows:
                    writer.writerow(row)
