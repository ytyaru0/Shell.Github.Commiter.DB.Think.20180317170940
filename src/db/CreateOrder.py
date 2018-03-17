from DbDefine import DbDefine
class CreateOrder:
    def __init__(self):
        pass

    def CalcOrder(self):
        names = self.__GetNames()
        # TODO: namesのDB名から依存関係を導き出す
        print(names)
        
    def __GetNames(self):
        names = []
        d = DbDefine()
        for key in d.Define:
            if '${' in d.Define[key]['out']:
                start = d.Define[key]['out'].find('${') + len('${')
                end = d.Define[key]['out'][start:].find('}') + start
                name = d.Define[key]['out'][start:end].strip()
                # TODO: name の妥当性確認 import shlex
                #   DB.Table.Column の書式。"DB"."Table"."Column" のようにクォートされている可能性もある。
                names.append(name)
        return names


if __name__ == '__main__':
    CreateOrder().CalcOrder()

