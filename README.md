# docker-get-logs-to-discord-bot

## なにこれ

Dockerコンテナのログを取得してDiscordのwebhookに送信するbot

## つかいかた

### `.env`ファイルを作成

```
cp .env.sample .env
```

### `.env`ファイルを編集

いいかんじに

### 実行

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```
