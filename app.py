from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer
from flask import Flask, jsonify
import concurrent.futures as cf
import waitress
import logging
import yaml
import time
import sys


app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    """Index

    Returns:
        str: Hello, World!
    """
    return "Hello, World!"


@app.route("/api/<x>/", methods=["GET", "POST"])
def api(x: str, path: str = 'config.yaml') -> jsonify:
    """Interface of the project

    Args:
        x (str): Request parameter
        path (str): Path of configuration file. Default to `config.yaml`

    Returns:
        jsonify: Format the data to JSON and return
    """
    # Params
    params = None
    while params == None:
        # When the yaml configuration file is being modified, it will return `None`
        params = yaml.load(open(path), Loader=yaml.FullLoader)
    a = params["params"]["a"]
    b = params["params"]["b"]
    # Params

    # Algorithm
    def func(x):
        time.sleep(1)
        y = a*float(x)+b
        return y
    # Algorithm

    # Data
    r = {"r": []}
    x = x.split(",")
    for i in x:
        if i != "":
            r["r"].append({"x": float(i), "y": func(i)})
        else:
            pass
    # Data
    return jsonify(r)


def main():
    """Start web service and monitor file system events
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            waitress.serve(app, host="127.0.0.1", port=5000)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    main()
