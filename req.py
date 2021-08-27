import requests
import json


def main(x: list) -> str:
    """Interface request test

    Args:
        x (list): Request parameter

    Returns:
        str: Elapsed seconds and contents of response
    """
    url = f'http://127.0.0.1:5000/api/{",".join([str(i) for i in x])}/'
    res = requests.get(url)
    return f'elapsed seconds: {res.elapsed.seconds}\n{json.dumps(res.json(), indent=2)}'


if __name__ == '__main__':
    print(main([1, 2]))
