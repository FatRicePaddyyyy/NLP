# NLP
NLPを用いた実用的なコードを載せていきます。現在、web上にあるコードはモデルの学習方法などが多いですが、その学習を自前の端末で行うと非常に負荷がかかります。なので、できる限り学習済みモデルを用いてNLPを行っていきます。

### 「MemGPTをもちいておしゃべり」
MemGPTと呼ばれる長期間記憶が可能な大規模言語モデルを用いて、ユーザーのテキスト入力に対して音声で返答を返すプログラムです。

VOICEBOXAPIの導入は https://haon-code.com/simple_zundamon/ こちらを参照してください。

MemGPTの導入はhttps://github.com/cpacker/MemGPT はこちらを参照してください。

### 「ツイートデータで感情分析」
twikitはX(旧ツイッター)での様々な操作を行うライブラリです。APIなしでツイートを取得することができるので、このツイートデータの感情分析します。

### SimSCEで文分類
SimSCEは文を固定長のベクトルに変換するモデルです。この固定長のベクトルの類似度を計算することで、近しい意味の文を検索することができます。このSimSCEにより、あいまい検索が可能となり、検索システムとして一歩優位に立てます。

