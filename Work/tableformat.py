class TableFormatter:
    def headings(self, headers):
        pass

    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        ''' Emit the table headings'''
        for each in headers:
            print(f'{each:>10s}', end=' ')

        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        ''' Emit a single row of table data '''
        for each in rowdata:
            print(f'{each:>10}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    ''' Output portfolio in CSV format '''

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(map(str, rowdata)))


class HTMLTableFormatter(TableFormatter):
    ''' Output portfolio in HTML format '''

    def headings(self, headers):
        print('<tr>', end='')
        for head in headers:
            print(f'<th>{head}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for data in rowdata:
            print(f'<td>{data}</td>', end='')
        print('</tr>')


class FormatError(Exception):
    pass


def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown/Incompatible format {fmt}.')

def print_table(portfolio, columns, formatter):

    formatter.headings(columns)
    for obj in portfolio:
        rowdata = [str(getattr(obj, name)) for name in columns]
        formatter.row(rowdata)
