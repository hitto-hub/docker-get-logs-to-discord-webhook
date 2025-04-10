# ベースイメージとして軽量な Python イメージを利用
FROM python:3.13-slim

# 必要なパッケージのインストール
RUN pip install docker requests

# プログラムファイルをコンテナ内にコピー
COPY docker_log_sender.py /app/docker_log_sender.py

# 作業ディレクトリの設定
WORKDIR /app

# コンテナ起動時にプログラムを実行
CMD ["python", "docker_log_sender.py"]
