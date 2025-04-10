import os
import docker
import requests
import time

WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
if not WEBHOOK_URL:
    raise Exception("環境変数 WEBHOOK_URL が設定されていません")

CONTAINER_NAME = os.environ.get("CONTAINER_NAME")
if not CONTAINER_NAME:
    raise Exception("環境変数 CONTAINER_NAME が設定されていません")

def send_to_webhook(message):
    payload = {"content": message}
    max_retries = 5
    retry_count = 0
    while retry_count < max_retries:
        try:
            response = requests.post(WEBHOOK_URL, json=payload)
            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After")
                sleep_time = float(retry_after) if retry_after else 1.0
                print(f"Rate limit hit. Retrying after {sleep_time} seconds.")
                time.sleep(sleep_time)
                retry_count += 1
                continue
            response.raise_for_status()
        except Exception as e:
            print(f"Webhook 送信エラー: {e}")
            break
        else:
            print(f"送信成功: {message}")
            break

def main():
    client = docker.from_env()
    try:
        container = client.containers.get(CONTAINER_NAME)
    except Exception as e:
        print(f"対象コンテナの取得エラー: {e}")
        return

    logs_stream = container.logs(stream=True, follow=True)
    buffer = ""
    try:
        for chunk in logs_stream:
            buffer += chunk.decode("utf-8")
            if "\n" in buffer:
                lines = buffer.split("\n")
                for line in lines[:-1]:
                    message = line.strip()
                    if message:
                        send_to_webhook(message)
                        time.sleep(0.2)
                buffer = lines[-1]
    except Exception as e:
        print(f"ログ取得エラー: {e}")

if __name__ == "__main__":
    main()
