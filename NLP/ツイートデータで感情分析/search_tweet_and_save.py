from twikit import Client
import os
import pickle
from typing import List

def search_tweets_and_save(*,query : str, 
                           user_name : str, 
                           mail : str, 
                           password : str, 
                           pickle_name : str,
                           max_tweets : int=100, 
                           save_flag : bool=True) -> None:
    # クライアントの初期化
    client = Client('ja')
    client.login(
        auth_info_1=user_name,
        auth_info_2=mail,
        password=password,
    )

    # 検索結果の取得
    texts = []
    results = client.search_tweet(query, count=20, product='Latest')

    # 指定された最大ツイート数に達するまでツイートを取得
    while len(texts) < max_tweets:
        for result in results:
            texts.append(result.text)
            #print(result.text)
        if not hasattr(results, 'next'):
            break
        results = results.next()

    #結果をファイルに保存（オプション）
    if save_flag :
        with open(f'{pickle_name}.pkl', 'wb') as file:
            pickle.dump(texts, file)



# 例として、100件のツイートを検索語 "しぐれうい" で検索
# texts = search_tweets_and_save("しぐれうい", 100)
# print(len(texts))
