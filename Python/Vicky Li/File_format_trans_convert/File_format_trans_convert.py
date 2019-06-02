#! python3
# -*- coding: utf-8 -*-

import xlwt, xlrd, sqlite3

def to_excel(path):
    excel = xlwt.Workbook()
    sheet = excel.add_sheet('student')
    with open(path, 'r') as f:
        for index, line in enumerate(f.readlines()):
            x = line.split()
            for i in range(len(x)):
                sheet.write(index,i,x[i])
    excel.save('student.xls')

def to_xml(path):
    file = xlrd.open_workbook(path, encoding_override = 'utf-8')
    sheet = file.sheets()[0]
    xml = open(path.split('.')[0] + '.xml', 'w')
    xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xml.write('<root>\n')
    xml.write('<students>\n')
    xml.write('<!--\n')
    xml.write('    学生信息表\n')
    xml.write('    "id" : [名字, 数学, 语文, 英文]\n')
    xml.write('-->\n')

    for i in range(0, sheet.nrows):
        s = u''
        for j in range(sheet.ncols):
            tmp = [u'%s' % str(sheet.cell_value(i, j))]
            s += u''.join(tmp)
        s += u'\n'
        xml.write(s)

    xml.write(u'</students>\n')
    xml.write(u'</root>\n')

def to_SQLite(path):
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()
    cursor.close()
    conn.commit()
    comm.close()

to_excel('student.txt')
to_xml('student.xls')
