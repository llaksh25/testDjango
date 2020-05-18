from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
#class ConstructHeader():


def construct_excel(params):
    header = construct_excel_header(params.data[0])
    body = construct_excel_body(params)

    wb = Workbook()
    ws = wb.active

    ws.append(header)
    # del params[0]
    for rows in body:
        ws.append(rows)

    return wb


def construct_excel_header(params):
    header = [];
    for iter_data in params:
        header.append(iter_data)

    return header;


def construct_excel_body(params):
    body = []
    for iter_data in params.data:
        each_record = []
        for key, val in iter_data.items():
            each_record.append(val)
        body.append(each_record)
    return body
