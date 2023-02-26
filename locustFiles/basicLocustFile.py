import logging
from locust import HttpUser, task, between

baseUrl = "https://api.punkapi.com/v2/"

endpoints = {
    "listBeers":"/beers",
    "randomBeer":"/beers/random"
}

log = logging.getLogger("Punk Brewery Stress Test")

class PunkUser(HttpUser):
    host = baseUrl
    wait_time = between(2,10)

    def __init__(self, environment):
        super().__init__(environment)

    def on_start(self):
        return super().on_start()
    
    def on_stop(self):
        pass

    @task
    def getBeers(self):
        try: 
            with self.client.get(endpoints["listBeers"], catch_response=True) as apiResponse:
                if apiResponse.status_code == 200:
                    responseBody = apiResponse.json()
                    log.info(f"Acquired beer list: {responseBody}")
                    apiResponse.success()
                
                else:
                    apiResponse.failure("Didn't manage to reach the endpoint, check logs for more info")
                    log.info(f"Error happened here, can't reach beers endpoint: {apiResponse.status_code}")
        
        except Exception as e:
            log.error(f"Exception @beer enpoint: {e}")

    @task
    def getRandomBeer(self):
        try: 
            with self.client.get(endpoints["randomBeer"], catch_response=True) as apiResponse:
                if apiResponse.status_code == 200:
                    responseBody = apiResponse.json()
                    log.info(f"Acquired random beer: {responseBody}")
                    apiResponse.success()
                
                else:
                    apiResponse.failure("Didn't manage to reach the endpoint, check logs for more info")
                    log.info(f"Error happened here, can't reach randomBeer endpoint: {apiResponse.status_code}")
        
        except Exception as e:
            log.error(f"Exception @randomBeer enpoint: {e}")