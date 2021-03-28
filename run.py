#! /usr/bin/env python
from app import app
from os import getenv

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)