from locust import HttpUser, task, between
import os


class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def hello_world(self):
        self.client.get("/api/1/")


if __name__=='__main__':
    os.system("locust -f loc.py --host=http://172.18.2.132:5000")