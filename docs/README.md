# SSHepherd Docs

## Description

This folder contains the source documentation for the SSHepherd utility.

## Howto: Use this repository

1. Build and serve the module source material:

```
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 -m mkdocs build
python3 -m mkdocs serve
```

2. Use the module material:

[http://127.0.0.1:8080](http://127.0.0.1:8080)

3. Gracefully exit when complete:

```
ctl+c
deactivate
```
