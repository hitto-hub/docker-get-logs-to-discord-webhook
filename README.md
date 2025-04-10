# docker-get-logs-to-discord-bot

## example

```yaml
services:
  my_container:
    image: /path/to/your/image
    container_name: my_container
  log_to_webhook:
    image: h1tto/docker-get-logs-to-discord-webhook
    environment:
      WEBHOOK_URL: "https://discord.com/api/webhooks/1234567890/your_webhook_token"
      CONTAINER_NAME: "my_container"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```
