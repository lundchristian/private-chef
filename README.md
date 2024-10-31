# README

Private Fridge repository.

Use the docker image if you want to try it out.

```bash
# pull the image
docker pull lundchristian/uit-repo:chef
# run the image
docker run -e UIT_KEY="sk-..." -p <host_port>:4000 lundchristian/uit-repo:chef
```

If you want to build it yourself.

```bash
# pull the image
docker pull lundchristian/uit-repo:chef
# run the image
docker run -e UIT_KEY="sk-..." -p <host_port>:4000 lundchristian/uit-repo:chef
```

### Direct Dependencies

- `flask`
- `flask-cors`
- `openai`
- `gpt4all`
