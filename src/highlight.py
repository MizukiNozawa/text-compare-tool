def highlight_diff(diff):
    """
    差分をハイライトする関数
    :param diff: 比較結果の差分リスト
    :return: ハイライトされた差分の文字列
    """
    highlighted_diff = []
    for line in diff:
        if line.startswith('+ '):
            highlighted_diff.append(f'\033[92m{line}\033[0m')  # 緑色で追加された行を表示
        elif line.startswith('- '):
            highlighted_diff.append(f'\033[91m{line}\033[0m')  # 赤色で削除された行を表示
        else:
            highlighted_diff.append(line)  # 変更のない行はそのまま
    return ''.join(highlighted_diff)
