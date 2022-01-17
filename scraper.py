import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class ForcastHour:
    time=""
    temperature=""
    chancePrecipication=""
    windSpeedAndDirection=""

    def __init__(self, time, temperature, chancePrecipication, windSpeedAndDirection):
        self.time = time
        self.temperature = temperature
        self.chancePrecipication = chancePrecipication
        self.windSpeedAndDirection = windSpeedAndDirection


    def returnString(self):
        return self.time + " " + self.temperature + " " + self.chancePrecipication + " " + self.windSpeedAndDirection


url = 'https://tempestwx.com/station/27024/'
driver = webdriver.Firefox()
try:
    driver.get(url)
    time.sleep(2)
    listOfForcast = []
    #grab items here, kind of like:
    #timeValue = driver.find_element(By.XPATH, "//div[@id='titleIndex0']/h2[@data-testid='daypartName']")
    #this is for a different webpage, so it won't match directly.