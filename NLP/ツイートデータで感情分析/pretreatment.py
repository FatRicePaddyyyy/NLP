# encoding: utf8
from __future__ import unicode_literals
import re
import unicodedata

def pretreatment(text):
    # 不要なユーザー名、ハッシュタグ、URLを削除
    text = re.sub(r'[@＠]\w+|#\w+|https?://\S+', '', text)
    
    # 全角文字を半角に変換、特定の全角記号を半角に、不要なスペースの削除
    text = unicodedata.normalize('NFKC', text)
    
    # ハイフンやダッシュ、長音符の統一
    text = re.sub('[˗֊‐‑‒–⁃⁻₋−]+', '-', text)
    text = re.sub('[﹣－ｰ—―─━ー]+', 'ー', text)
    
    # 特定の記号を一括で置換
    translation_table = str.maketrans(
        '!"#$%&\'()*+,-./:;<=>?@[¥]^_`{|}~｡､･｢｣',
        '！”＃＄％＆’（）＊＋，－．／：；＜＝＞？＠［￥］＾＿｀｛｜｝〜。、・「」')
    text = text.translate(translation_table)
    
    # 不要な空白を削除
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

