from locust import HttpUser, task, between
import os


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def hello_world(self):
        self.client.get('api/1/')
        self.client.post()


if __name__ == '__main__':
    os.system('locust -f loc.py --host=http://127.0.0.1:5000')
