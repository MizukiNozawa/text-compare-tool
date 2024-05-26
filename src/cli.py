import argparse
from compare import compare_files
from highlight import highlight_diff

def main():
    parser = argparse.ArgumentParser(description='2つのテキストファイルを比較し、差分を表示するツール')
    parser.add_argument('--file1', required=True, help='1つ目のテキストファイルのパス')
    parser.add_argument('--file2', required=True, help='2つ目のテキストファイルのパス')

    args = parser.parse_args()
    
    diff = compare_files(args.file1, args.file2)
    highlighted_diff = highlight_diff(diff)
    
    print(highlighted_diff)

if __name__ == "__main__":
    main()

