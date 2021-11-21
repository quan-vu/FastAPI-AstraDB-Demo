# FastAPI AstraDB

Pre-requites:

- Python 3.9+


Features

- [x] Working with AstraDB (a cloud cassandra database)
- [x] Restful API with FastAPI

## Development

Install python3.9 on Ubuntu

```shell
# Once you added the PPA on your Ubuntu system
sudo add-apt-repository ppa:deadsnakes/ppa 

# Update the apt cache and install Python 3.9
sudo apt update 
sudo apt install python3.9 

# Check the Python version
python3.9 -V 
```

Download your AstraDB connecttion zip file

```shell
# Save it to this path
app/ignored/connection.zip
```

Create virtualenv

```shell
virtualenv -p python3.9 venv3.9
source venv3.9/bin/activate

pip install -r requirements.txt
```

Create .env file

```shell
make env
```

Start app in develoment 

```shell
make start
```
