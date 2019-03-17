import re
import preparedata
import writeexcel

def __get_txt_lines(filepath):
    f = open(filepath, 'r')
    lines = []
    for line in f:
        lines.append(line.replace('\n',''))
    f.close()
    return lines

if __name__=="__main__":
    lines = __get_txt_lines(r'./grep-result.txt')
    tables = __get_txt_lines(r'./table-name-list.txt')
    output_data = []

    for line in lines:
        line_result = preparedata.Result(line, tables)
        line_result.append_to(output_data)

    writer = writeexcel.WriteExcel()
    writer.write_excel(output_data, tables)
