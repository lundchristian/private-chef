# README

Repository for Private Fridge

Use the docker image if you want to try it out.

```bash
# pull the image
docker pull lundchristian/uit-repo:chef
# run the image
docker run -e UIT_KEY="sk-..." -p <host_port>:4000 lundchristian/uit-repo:chef
```

Or, if you want to build it yourself.

```bash
# clone the repo
git clone git@github.com:lundchristian/private-chef.git
# switch directories
cd private-chef
# create virtual environment
python3 -m venv .venv
# activate virtual environment
source .venv/bin/activate
# install dependencies
pip install -r requirements.txt
# switch directories
cd src
# download models, will take some time
python3 download_models.py
# run app
python3 app.py
```
