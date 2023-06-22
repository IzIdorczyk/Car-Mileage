import os
import yaml
import win32com.client
from pywintypes import com_error


from sheet import sheet, get_month_name
from generator import generate_distances, rows_needed, dates


with open('../backend/config.yml', 'r', encoding='utf8') as file:
    cfg = yaml.safe_load(file)

filename = f"{get_month_name(cfg['month'])} {cfg['year']} {cfg['car_name']} {cfg['car_register_numbers']}"
filepath = f'../backend/created_files/{filename}.xls'
filepath_xls = os.path.abspath(filepath)
filepath_pdf = f'{filepath_xls[:-3]}pdf'
filepath_xlsx = f'{filepath_xls}x'


sheet(  filepath = filepath, page=cfg['page'],
        pages_needed= cfg['pages_needed'],
        first_day_date= cfg['first_day_date'],
        last_day_date= cfg['last_day_date'],
        car_register_numbers = cfg['car_register_numbers'],
        first_day_value = cfg['first_day_value'],
        month= cfg['month'], year = cfg['year'],
        rows_amount= rows_needed, dates = dates,
        distances = generate_distances(),
    )




def excel_to_pdf(excel_path, pdf_path):
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = 0
    try:
        print('Start conversion to PDF')
        # Open
        wb = excel.Workbooks.Open(excel_path)
        wb.WorkSheets[0]
        # Save
        wb.ExportAsFixedFormat(0, pdf_path)
    except com_error as e:
        print('Failed.', e)
    else:
        print('Succeeded.')
    finally:
        wb.Close()
        excel.Quit()


def xls_to_xlsx(xls_path, xlsx_path):
    os.rename(xls_path, xlsx_path)


excel_to_pdf(filepath_xls, filepath_pdf)
xls_to_xlsx(filepath_xls, filepath_xlsx)
