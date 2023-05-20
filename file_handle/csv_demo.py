import csv
import xlrd
import xlwt
import pandas as pd

def csv_to_xlsx_pd():
    csv = pd.read_csv('./source/example.csv', encoding='utf-8')
    csv.to_excel('./source/example_pd.xlsx', sheet_name='data')


def xlsx_to_csv_pd():
    data_xls = pd.read_excel('./source/example.xlsx', index_col=0)
    data_xls.to_csv('./source/example_pd.csv', encoding='utf-8')


def csv_to_xlsx():
    with open('./source/example.csv', 'r', encoding='utf-8') as f:
        read = csv.reader(f)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data')  # 创建一个sheet表格
        l = 0
        for line in read:
            print(line)
            r = 0
            for i in line:
                print(i)
                sheet.write(l, r, i)  # 一个一个将单元格数据写入
                r = r + 1
            l = l + 1

        workbook.save('./source/example.xlsx')  # 保存Excel


def xlsx_to_csv():
    workbook = xlrd.open_workbook('./source/example.xlsx')
    table = workbook.sheet_by_index(0)
    with open('./source/r_example.csv', 'w', encoding='utf-8') as f:
        write = csv.writer(f)
        for row_num in range(table.nrows):
            row_value = table.row_values(row_num)
            write.writerow(row_value)

if __name__ == '__main__':
    csv_to_xlsx()
    xlsx_to_csv()
    xlsx_to_csv_pd()
    csv_to_xlsx_pd()
