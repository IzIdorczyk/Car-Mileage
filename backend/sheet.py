import xlsxwriter


# convert month number to text
def get_month_name(number):
    names = ['Styczeń',
             'Luty',
             'Marzec',
             'Kwiecień',
             'Maj',
             'Czerwiec',
             'Lipiec',
             'Sierpień',
             'Wrzesień',
             'Październik',
             'Listopad',
             'Grudzień',
             ]
    return names[number - 1]


# convert inch to cm
def inch_to_cm(inch):
    return inch * 0.3937


def sheet(filepath: str = None, paper: int = 9, margin_left: float = 0.5, margin_right: float = 0.1,
          margin_top: float = 0.2, margin_bottom: float = 0, page: int = 1, pages_needed: int = 1,
          first_day_date: str = None, last_day_date: str = None, car_register_numbers: str = None,
          first_day_value: int = None, month: int = None, year: int = None, rows_amount: int = None, start_at: int = 23,
          dates: list = [], distances: list = []):
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet()

    # set the paper type ( 9 = A4)
    worksheet.set_paper(paper)

    # set margins in inches
    worksheet.set_margins(left=inch_to_cm(margin_left), right=inch_to_cm(margin_right), top=inch_to_cm(margin_top),
                          bottom=inch_to_cm(margin_bottom))

    # columns size
    worksheet.set_column_pixels('A:A', 39)
    worksheet.set_column_pixels('B:B', 28)
    worksheet.set_column_pixels('C:C', 42)
    worksheet.set_column_pixels('D:D', 16)
    worksheet.set_column_pixels('E:E', 53)
    worksheet.set_column_pixels('F:F', 7)
    worksheet.set_column_pixels('G:G', 23)
    worksheet.set_column_pixels('H:H', 7)
    worksheet.set_column_pixels('I:I', 19)
    worksheet.set_column_pixels('J:J', 48)
    worksheet.set_column_pixels('K:K', 16)
    worksheet.set_column_pixels('L:L', 16)
    worksheet.set_column_pixels('M:M', 16)
    worksheet.set_column_pixels('N:N', 33)
    worksheet.set_column_pixels('O:O', 29)
    worksheet.set_column_pixels('P:P', 49)
    worksheet.set_column_pixels('Q:Q', 28)
    worksheet.set_column_pixels('R:R', 11)
    worksheet.set_column_pixels('S:S', 17)
    worksheet.set_column_pixels('T:T', 54)
    worksheet.set_column_pixels('U:U', 27)
    worksheet.set_column_pixels('V:V', 29)
    worksheet.set_column_pixels('W:W', 30)
    worksheet.set_column_pixels('X:X', 65)

    # rows size
    row5 = (6, 11, 13, 15, 88, 90)
    row14 = (91, 92, 93)
    row15 = (0, 2, 3, 4, 5, 7, 8, 12, 14, 16, 17, 18, 19, 20, 21, 84, 85, 86, 87, 89)
    worksheet.set_row_pixels(1, 13)
    worksheet.set_row_pixels(9, 10)
    worksheet.set_row_pixels(10, 21)

    for x in range(22, 84):
        worksheet.set_row_pixels(x, 0)

    for x in row5:
        worksheet.set_row_pixels(x, 5)

    for x in row14:
        worksheet.set_row_pixels(x, 14)

    for x in row15:
        worksheet.set_row_pixels(x, 15)

    # formating sets
    arial6 = workbook.add_format({
        'font_name': "Arial",
        'font_size': 6,
    })

    arial6lt = workbook.add_format({
        'font_name': "Arial",
        'font_size': 6,
        'align': 'left',
        'valign': 'top',
    })

    arial6ltstr = workbook.add_format({
        'font_name': "Arial",
        'font_size': 6,
        'font_strikeout': 1,
    })

    arial6ltsup = workbook.add_format({
        'font_name': "Arial",
        'font_size': 6,
        'font_script': 1,
    })

    arial7 = workbook.add_format({
        'font_name': "Arial",
        'font_size': 7,
    })

    arial7t = workbook.add_format({
        'font_name': "Arial",
        'font_size': 7,
        'valign': 'top',
    })

    arial7sup = workbook.add_format({
        'font_name': "Arial",
        'font_size': 7,
        'font_script': 1
    })

    arial8 = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8
    })

    arial8t = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'valign': 'top'
    })

    arial8str = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'font_strikeout': 1
    })

    arial8sup = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'font_script': 1
    })

    arial8ct = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
    })

    arial8c = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'align': 'center'
    })

    arial8cn = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'align': 'center',
        'valign': 'top',
        'num_format': 3
    })

    arial8border = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'border': 1
    })

    arial8borderc = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'valign': 'vcenter',
        'align': 'center',
        'border': 1
    })

    arial8bordercw = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'valign': 'vcenter',
        'align': 'center',
        'border': 1,
        'text_wrap': True,
    })

    arial8bordercn = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'valign': 'vcenter',
        'align': 'center',
        'border': 1,
        'num_format': 3
    })

    arial8borderdiag = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'diag_type': 2,
        'border': 1
    })

    arial7bold = workbook.add_format({
        'font_name': "Arial",
        'font_size': 7,
        'bold': True
    })

    arial8bold = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'bold': True
    })

    arial8boldl = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'bold': True,
        'valign': 'top',
        'align': 'left'
    })

    arial8boldln = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'bold': True,
        'align': 'center',
        'valign': 'top',
        'num_format': 3
    })

    arial8boldcenter = workbook.add_format({
        'font_name': "Arial",
        'font_size': 8,
        'bold': True,
        'center_across': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'align': 'center'
    })

    arial12boldcenter = workbook.add_format({
        'font_name': "Arial",
        'font_size': 12,
        'bold': True,
        'center_across': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'align': 'center'
    })

    arialn8boldcenter = workbook.add_format({
        'font_name': "Arial Narrow",
        'font_size': 8,
        'bold': True,
        'center_across': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'align': 'center'
    })

    arialn8boldcenterb = workbook.add_format({
        'font_name': "Arial Narrow",
        'font_size': 8,
        'bold': True,
        'center_across': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'align': 'center',
        'border': 1
    })

    arialn8boldcentsup = workbook.add_format({
        'font_name': "Arial Narrow",
        'font_size': 8,
        'bold': True,
        'center_across': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'align': 'center',
        'font_script': 1
    })

    arialn8boldcentstr = workbook.add_format({
        'font_name': "Arial Narrow",
        'font_size': 8,
        'bold': True,
        'center_across': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'align': 'center',
        'font_strikeout': 1
    })

    border = workbook.add_format({
        'border': 1
    })

    bottomBorder = workbook.add_format({
        'bottom': 1
    })

    # top of the register

    worksheet.write('A1', 'Dane podatnika:', arial8)
    worksheet.write('X1', 'strona ' + f"{page}/{pages_needed}", arial8)
    worksheet.write_rich_string('A2',
                                arial6lt, '(',
                                arial6ltstr, 'nazwisko, imię',
                                arial6lt, '/ nazwa',
                                arial6ltsup, '1)',
                                arial6lt, 'adres',
                                arial6lt)
    worksheet.write('A3', 'prowadzonej działalności, NIP)', arial6lt)
    worksheet.write('O3', 'Dzień zakończenia prowadzenia ewidencji:', arial8)
    worksheet.merge_range('V3:X3', last_day_date, arial8boldl)
    worksheet.write('A4', 'Numer rejestracyjny pojazdu samochodowego:', arial8)
    worksheet.merge_range('J4:K4', car_register_numbers, arial8boldl)
    worksheet.write('O5', 'Stan licznika przebiegu pojazdu na dzień', arial8)
    worksheet.write('A6', 'Dzień rozpoczęcia prowadzenia ewidencji:', arial8)
    worksheet.merge_range('I6:J6', first_day_date, arial8boldl)
    worksheet.write('O6', 'zakończenia prowadzenia ewidencji:', arial8)
    worksheet.merge_range('U6:W6', '=C90', arial8boldln)
    worksheet.write('A8', 'Stan licznika przebiegu pojazdu na dzień', arial8)
    worksheet.write('O8', 'Liczba przejechanych kilometrów na dzień', arial8)
    worksheet.write('A9', 'rozpoczęcia prowadzenia ewidencji:', arial8)
    worksheet.merge_range('G9:I9', first_day_value, arial8boldln)
    worksheet.write('O9', 'zakończenia prowadzenia ewidencji:', arial8)
    worksheet.merge_range('U9:W9', '=Q87', arial8boldln)
    worksheet.merge_range('A11:X11', 'EWIDENCJA PRZEBIEGU POJAZDU DLA CELÓW VAT', arial12boldcenter)
    worksheet.merge_range('A13:X13', '', arial8boldcenter)
    worksheet.write_rich_string('A13',
                                arial8boldcenter, 'za miesiąc / ',
                                arialn8boldcentstr, 'kwartał',
                                arialn8boldcentsup, '1) ',
                                arial8boldcenter, f"{get_month_name(month)} {year}",
                                arial8boldcenter)
    worksheet.write('A15', 'Stan licznika', arial8t)
    worksheet.merge_range('C15:D15', '', arial8ct)
    worksheet.write('C15', '=G9', arial8cn)
    worksheet.write_rich_string('E15',
                                arial8, ' na początek miesiąca / ',
                                arial8str, 'kwartału',
                                arial8sup, '1) ',
                                arial8, f"{get_month_name(month)} {year}",
                                arial8t)

    # top of the table
    worksheet.merge_range('A17:A22', '', arialn8boldcenterb)
    worksheet.merge_range('B17:C22', '', arialn8boldcenterb)
    worksheet.merge_range('D17:I22', '', arialn8boldcenterb)
    worksheet.merge_range('J17:P22', '', arialn8boldcenterb)
    worksheet.merge_range('Q17:S22', '', arialn8boldcenterb)
    worksheet.merge_range('T17:V22', '', arialn8boldcenterb)
    worksheet.merge_range('W17:X19', '', arialn8boldcenterb)
    worksheet.merge_range('W20:X22', '', arialn8boldcenterb)

    worksheet.write('A17', 'Nr\nkolejny\nwpisu', arialn8boldcenterb)
    worksheet.write_rich_string('B17',
                                arialn8boldcenterb, 'Data wyjazdu/\nudostępnienia\npojazdu',
                                arialn8boldcentsup, '2)',
                                arialn8boldcenterb)
    worksheet.write_rich_string('D17',
                                arialn8boldcenterb, 'Opis trasy\n',
                                arialn8boldcenterb, 'wyjazdu\n',
                                arialn8boldcenterb, '(skąd-dokąd)',
                                arialn8boldcentsup, '3)',
                                arialn8boldcenterb)
    worksheet.write_rich_string('J17',
                                arialn8boldcenterb, 'Cel wyjazdu/\n',
                                arialn8boldcenterb, 'udostępnienia pojazdu',
                                arialn8boldcentsup, '2)',
                                arialn8boldcenterb)
    worksheet.write('Q17', 'Liczba\nfaktycznie\nprzejecha-\nnych\nkilometrów', arialn8boldcenterb)
    worksheet.write_rich_string('T17',
                                arialn8boldcenterb, 'Imię i nazwisko osoby\n',
                                arialn8boldcenterb, 'kierującej pojazdem/\n',
                                arialn8boldcenterb, 'osoby, której\n',
                                arialn8boldcenterb, 'udostępniony został\n',
                                arialn8boldcenterb, 'pojazd',
                                arialn8boldcentsup, '2)',
                                arialn8boldcenterb)
    worksheet.write_rich_string('W17',
                                arialn8boldcenterb, 'Stan licznika\n',
                                arialn8boldcenterb, 'na dzień udostęp-\n',
                                arialn8boldcenterb, 'nienia pojazdu',
                                arialn8boldcentsup, '2)',
                                arialn8boldcenterb)
    worksheet.write_rich_string('W20',
                                arialn8boldcenterb, 'Stan licznika\n',
                                arialn8boldcenterb, 'na dzień zwrotu\n',
                                arialn8boldcenterb, 'pojazdu',
                                arialn8boldcentsup, '2)',
                                arialn8boldcenterb)

    # rows
    for row_a in range(rows_amount):

        row = start_at + (row_a * 2)
        if row_a == 0:
            str_row7 = '=C15'
        else:
            str_row7 = '=W' + str(row - 1)
        str_row8 = '=W' + str(row) + '+Q' + str(row)

        # column creator

        col = [
            # col1 =
            'A' + str(row) + ':' + 'A' + str(row + 1),
            # col2 =
            'B' + str(row) + ':' + 'C' + str(row + 1),
            # col3 =
            'D' + str(row) + ':' + 'I' + str(row + 1),
            # col4 =
            'J' + str(row) + ':' + 'P' + str(row + 1),
            # col5 =
            'Q' + str(row) + ':' + 'S' + str(row + 1),
            # col6 =
            'T' + str(row) + ':' + 'V' + str(row + 1),
            # col7 =
            'W' + str(row) + ':' + 'X' + str(row),
            # col8 =
            'W' + str(row + 1) + ':' + 'X' + str(row + 1)]

        worksheet.set_row_pixels((row - 1), 13)
        worksheet.set_row_pixels(row, 13)

        for x in range(8):
            worksheet.merge_range(col[x], '', arial8border)

        worksheet.write(col[0], row_a + 1, arial8borderc)
        worksheet.write(col[1], f'{dates[row_a]}.{month}.{year}', arial8borderc)
        worksheet.write_rich_string(col[2],
                                    arial8bordercw, 'Gdańsk\n',
                                    arial7, '(jazda po mieście)',
                                    arial8bordercw)
        worksheet.write(col[3], 'dowóz zamówień do klientów', arial8borderc)
        worksheet.write(col[4], distances[row_a], arial8borderc)
        worksheet.write(col[5], '', arial8borderc)
        worksheet.write(col[6], str_row7, arial8bordercn)
        worksheet.write(col[7], str_row8, arial8bordercn)

    # end of the table
    worksheet.write('A85', 'UWAGA:', arial7bold)
    worksheet.write('B85', 'W przypadku, gdy pojazd samochodowy jest', arial7bold)
    worksheet.write('M85', 'Podsumowanie strony', arial8bold)
    worksheet.merge_range('Q85:S85', '=SUM(Q23:S84)', arial8borderc)
    worksheet.write('B86', 'udostępniany osobie niebędącej pracownikiem', arial7bold)
    worksheet.write('M86', 'Z przeniesienia', arial8bold)
    worksheet.merge_range('Q86:S86', '', arial8borderdiag)
    worksheet.write('B87', 'podatnika, ewidencję przebiegu pojazdu wypełnia', arial7bold)
    worksheet.write('B88', 'osoba, która udostępnia pojazd.', arial7bold)
    worksheet.write('M87', 'Razem', arial8bold)
    worksheet.merge_range('Q87:S87', '=SUM(Q85:S86)', arial8borderc)
    worksheet.merge_range('T85:X87', '', arial8borderdiag)

    # footer of register
    worksheet.write('A90', 'Stan licznika', arial8t)
    worksheet.merge_range('C90:D90', '', arial8ct)
    worksheet.write('C90', '=Q87+G9', arial8cn)
    worksheet.write_rich_string('E90',
                                arial8, ' na koniec miesiąca / ',
                                arial8str, 'kwartału',
                                arial8sup, '1) ',
                                arial8, f"{get_month_name(month)} {year}",
                                arial8t)
    worksheet.write('Q90', 'Podpis podatnika …………………………………….', arial8t)
    worksheet.merge_range('A91:P91', '', bottomBorder)
    worksheet.write_rich_string('A92',
                                arial7sup, '1)',
                                arial7, ' niepotrzebne skreślić,',
                                arial7t)
    worksheet.write_rich_string('A93',
                                arial7sup, '2)',
                                arial7,
                                ' dotyczy sytuacji, gdy pojazd samochodowy jest udostępniany osobie niebędącej pracownikiem podatnika,',
                                arial7t)
    worksheet.write_rich_string('A94',
                                arial7sup, '3)',
                                arial7,
                                ' nie wypełnia się, gdy pojazd samochodowy jest udostępniany osobie niebędącej pracownikiem podatnika.',
                                arial7t)

    workbook.close()
