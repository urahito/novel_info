# coding: utf-8

import scr_util as utl

# ライブラリ
import csv # ファイル出力用
import bs4, requests # スクレイピング(html取得・処理)
import re #正規表現
from pathlib import Path
import pandas as pd
    
# ファイルの読み込み
def read_for(files, out_writer):    
    # 入力ファイルでfor文を回す
    for file_path in files:
        with Path(file_path).open('r', encoding=utl.get_enc('r')) as read_file_obj:
            # 全行取り込む
            url_list = read_file_obj.readlines()

            # urlの読み込み
            read_url(url_list, out_writer)

# urlからタイトルを取得し、csvファイルに出力する
def read_url(url_list, out_writer):
        # urlリストを1行ごとに処理する
        for url in url_list:
            # urlでなければ次へ
            if not utl.ask_is_url(url):
                print('{} do not matched url pattern'.format(url))
                continue

            # ページの取得
            soup = utl.get_soup(url)

            # タイトルの取得とMarkdown用フォーマット
            title = utl.ignore_str(soup.title.string, utl.get_enc('w'))
            markup = '[{}]({})'.format(title, url)

            # csvファイルへ書き出し
            out_writer.writerow([url, title, markup])

def main():
    # 各ディレクトリの取得
    org_dir = utl.get_new_dir(Path(__file__).parent, 'org')
    out_dir = utl.get_new_dir(Path(__file__).parent, 'out')

    # 出力ファイルの決定
    out_file = out_dir / 'result.csv'

    # 入力、出力ファイル・ディレクトリの取得
    files = list(org_dir.glob('*.txt'))
    with out_file.open('w', encoding=utl.get_enc('w'), newline='') as out_file_obj:
        # csvファイルのwriterを取得
        out_writer = csv.writer(out_file_obj, dialect="excel")

        # ファイルの読み込み
        read_for(files, out_writer)

if __name__ == '__main__':
    main()
    print('finish')