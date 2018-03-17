import pathlib
class DbDefine:
    def __init__(self):
        self.__dbs = {}
        self.Load()
    @property
    def Define(self): return self.__dbs
    def Load(self):
        path = pathlib.Path('./src/db/create/sqlite.names')
        if not path.is_file(): raise Exception('DB名前定義ファイルがない。: {}'.format(str(path)))
        with path.open() as f:
            for i, line in enumerate(f.read().split('\n')):
                if 0 == len(line.strip()): continue
                columns = line.split()
                if len(columns) < 3: raise Exception('SyntaxError:{}: 1行あたりName,Out,Inの3つ必要です。'.format(i))
                if 'NAME' == columns[0].upper() and 'OUT' == columns[1].upper() and 'IN' == columns[2].upper(): continue
                if columns[0] in self.__dbs: raise Exception('SyntaxError:{}: Nameが重複しています。: {}'.format(i, columns[0]))
                self.__dbs[columns[0]] = {'out': columns[1], 'in': columns[2]}
        print(self.__dbs)


if __name__ == '__main__':
    DbDefine()
