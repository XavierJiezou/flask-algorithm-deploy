import requests
import json


def main(x: list) -> str:
    """Interface request test

    Args:
        x (list): Request parameter

    Returns:
        str: Elapsed seconds and contents of response
    """
    try:
        url = f'http://172.18.2.132:5000/api/{",".join([str(i) for i in x])}/'
        res = requests.get(url)
        if len(res.json()['r']) == len(x):
            return f'elapsed seconds: {res.elapsed.seconds}'
        else:
            return 'Unknown Error!'
    except:
        return f'Status Code: {res.status_code}'


if __name__ == '__main__':
    print(main([i for i in range(int(1e6))]))
