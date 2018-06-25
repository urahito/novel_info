import bs4, requests # スクレイピング(html取得・処理)
from pathlib import Path
import re #正規表現

# 指定エンコードのgetメソッド
def get_enc(mode):
    enc_dic = dict(r='utf-8', w='sjis', p='cp932')
    return enc_dic[mode]

# インラインのfor文リストで除外文字以外を繋ぐ
def remove_str(target, str_list):    
    return ''.join([c for c in target if c not in str_list])

# 指定エンコードでエラー文字以外を再取得する
def ignore_str(target, enc):    
    return target.encode(enc, 'ignore').decode(enc)

# ページをパースする
def get_soup(url):
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text)
    return soup

# parent,subのフォルダ作成
def get_new_dir(parent_dir, sub_dir):
    # フォルダが無ければ作成（あってもエラーなし）
    parent_dir.mkdir(exist_ok=True)
    sub_dir_path = parent_dir / sub_dir
    sub_dir_path.mkdir(exist_ok=True)
    return Path(sub_dir_path)

# URLか判定する
def ask_is_url(url):
    url = remove_str(url, ['\r', '\n'])

    # 正規表現処理
    rep = r'^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+$'
    return re.match(rep, url) != None