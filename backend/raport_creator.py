import os
import yaml
import random
from calendar import monthrange
import win32com.client
from pywintypes import com_error


from sheet import sheet, get_month_name


with open('../backend/config.yml', 'r', encoding='utf8') as file:
    cfg = yaml.safe_load(file)


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


def generate_distances(monthly_distance: int = (cfg['dayly_min'] * cfg['min_days']), days_quantity: int = cfg['min_days'],  min: int = cfg['dayly_min'], max: int = cfg['dayly_max']) -> list:

    distance_left = monthly_distance
    distances = []

    for _ in range(days_quantity):
        r = random.randint(min, max)
        distance_left -= r
        distances.append(r)

    if distance_left > 0:
        add_all = int(distance_left / days_quantity) 
        add_rest = distance_left - (add_all * days_quantity)
        for i in range(len(distances)):
            distances[i] += add_all
        
        for n in range(add_rest):
            distances[n] += 1
        return distances
    elif distance_left < 0:
        sub_all = int(distance_left / days_quantity) * -1
        sub_rest = (distance_left * -1) - (sub_all * days_quantity)
        for i in range(len(distances)):
            distances[i] -= sub_all
        
        for n in range(sub_rest):
            distances[n] -= 1
        return distances
    else:
        return distances

def create_raport(plate: str = 'XX XXXXX', model: str = 'Brand Model', first_day_value: int = 1, last_day_value: int = 1001, month: int = 1, year: int = 2000):

    filename = f"{get_month_name(month)} {year} {model} {plate}"
    filepath = f'../backend/created_files/{filename}.xls'
    filepath_xls = os.path.abspath(filepath)
    filepath_pdf = f'{filepath_xls[:-3]}pdf'
    filepath_xlsx = f'{filepath_xls}x'

    km_needed = last_day_value - first_day_value
    rows_needed = km_needed // random.randint(cfg['dayly_min'], cfg['dayly_max'])

    # check if it is out of range
    # if it is, sets extreme values
    if rows_needed < cfg['min_days']:
        rows_needed = cfg['min_days']
    if rows_needed > cfg['max_days']:
        rows_needed = cfg['max_days']

    while km_needed < (rows_needed * cfg['dayly_min']):
        print("subtracts a day ...")
        rows_needed -= 1

    if rows_needed <= 0:
        return 'err'

    num_days = monthrange(year, month,)[1]
    dates = sorted(random.sample(range(1, num_days + 1), rows_needed))

    first_day_date = f"1.{month}.{year}"
    last_day_date = f"{num_days}.{month}.{year}"

    sheet(  filepath = filepath, page=cfg['page'],
            pages_needed= cfg['pages_needed'],
            first_day_date= first_day_date,
            last_day_date= last_day_date,
            car_register_numbers = plate,
            first_day_value = first_day_value,
            month= month,
            year = year,
            rows_amount= rows_needed,
            dates = dates,
            distances = generate_distances(monthly_distance = km_needed, days_quantity = rows_needed),
        )

    excel_to_pdf(filepath_xls, filepath_pdf)
    xls_to_xlsx(filepath_xls, filepath_xlsx)

