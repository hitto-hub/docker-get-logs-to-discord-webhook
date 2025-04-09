# ベースイメージとして軽量な Python イメージを利用
FROM python:3.13-slim

# 必要なパッケージのインストール
RUN pip install docker requests

# プログラムファイルをコンテナ内にコピー
COPY log_to_webhook.py /app/log_to_webhook.py

# 作業ディレクトリの設定
WORKDIR /app

# コンテナ起動時にプログラムを実行
CMD ["python", "log_to_webhook.py"]
