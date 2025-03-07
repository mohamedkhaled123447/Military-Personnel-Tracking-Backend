import openpyxl


def read_from_excel():
    data_list = []
    workbook = openpyxl.load_workbook("data\data.xlsx")
    sheet = workbook["Sheet1"]
    for row in sheet.iter_rows(values_only=True):
        data_list.append(row)
    workbook.close()
    return data_list
