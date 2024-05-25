import difflib

def compare_files(file1_path, file2_path):
    """
    2つのテキストファイルの差分を比較する関数
    :param file1_path: 1つ目のファイルのパス
    :param file2_path: 2つ目のファイルのパス
    :return: 差分のリスト
    """
    with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()
    
    differ = difflib.Differ()
    diff = list(differ.compare(file1_lines, file2_lines))
    return diff
