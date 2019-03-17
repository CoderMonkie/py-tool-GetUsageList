import re

# 出力対象定義クラス
class Result(object):

    path = ''
    filename = ''
    tablename = ''
    use_flag_dic = {}

    # コンストラクタ
    def __init__(self, line, tables):
        self.path = self.__get_sub_path(line)
        self.filename = self.__get_filename(line)
        self.tablename = self.__get_table_name(line)
        self.use_flag_dic = {}
        for table in tables:
            self.use_flag_dic[table] = False
        pass

    # 出力対象に追加
    def append_to(self, lst):
        filter_result = list(filter(lambda x: x.path == self.path and x.filename == self.filename, lst))
        if any(filter_result) == False:
            self.__set_use_flag(self.tablename)
            lst.append(self)
        else:
            filter_result[0].__set_use_flag(self.tablename)

    # private methods -->

    # Table利用有無フラグ更新
    def __set_use_flag(self, table_name):
        if table_name in self.use_flag_dic.keys():
            self.use_flag_dic[table_name] = True
        pass

    # サブ フォルダ パスを取得
    def __get_sub_path(self, line):
        ma = re.match(r'.*moodle+[\\]+?(?P<folder>([\w]+[\\]+)*)', line)
        if ma is None:
            return ''
        else:
            # return ma.groupdict()['folder']
            return ma.group(1)

    # PHPファイル名を取得
    def __get_filename(self, line):
        ma = re.match(r'.*moodle+[\\]+?([\w]+[\\]+)*(?P<filename>[^(]+)', line)
        if ma is None:
            return ''
        else:
            return ma.groupdict()['filename']

    # テーブル名を取得
    def __get_table_name(self, line):
        ma = re.match(r'.*DB->[\w]+?\(\'(?P<table_name>[^\'\,]+)', line)
        if ma is None:
            return ''
        else:
            # return ma.group(1)
            return ma.groupdict()['table_name']
