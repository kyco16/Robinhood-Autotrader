from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


def robinhoodBuyAutomation(stock):
    # specify web driver
    driver = webdriver.Firefox()

    # go to URL
    driver.get("https://robinhood.com")

    # sign in
    signIn = driver.find_element_by_xpath('//a[@href="https://robinhood.com/login"]')
    signIn.click()
    time.sleep(5)
    username = driver.find_element_by_name('username')
    username.send_keys(input('Enter your Robinhood email'))
    password = driver.find_element_by_name('password')
    password.send_keys(input('Enter your Robinhood password'))
    signInButton = driver.find_element_by_tag_name('button')
    signInButton.click()
    time.sleep(5)

    # get buying power
    accountLink = driver.find_element_by_xpath('//a[@href="/account"]')
    accountLink.click()
    buyingPower = driver.find_element_by_xpath(
        '/html/body/div[1]/div/main/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/header/div/div[2]/div/div[1]/h3').get_attribute(
        'innerHTML')
    buyingPower = float(buyingPower.replace('$', ''))
    accountLink.click()

    # search for stock
    search = driver.find_element_by_tag_name('input')
    search.send_keys(stock)
    time.sleep(3)
    search.send_keys(Keys.ENTER)
    time.sleep(5)

    # put in an order
    stockPrice = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div/div[1]/div/main/div[2]/div[2]/div/form/div[1]/div[1]/div[2]/span').get_attribute('innerHTML')
    stockPrice = float(stockPrice.replace('$', '').replace(' ', ''))
    orderType = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div/div[1]/div/main/div[2]/div[2]/div/form/header/div/div[2]')
    orderType.click()
    time.sleep(3)
    limitOrder = driver.find_elements_by_class_name('menu-option')
    limitOrder[1].click()
    maxShares = int(round(buyingPower/stockPrice, 0)-1)
    print(maxShares)
    numberOfShares = driver.find_element_by_xpath('//input[@data-testid="OrderFormRows-Shares"]')
    numberOfShares.send_keys(maxShares)
    reviewOrderButton = driver.find_element_by_xpath('//button[@data-testid="OrderFormControls-Review"]')
    reviewOrderButton.click()


def robinhoodSellAutomation(stock):
    # specify browser
    driver = webdriver.Firefox()

    # go to URL
    driver.get("https://robinhood.com")

    # sign in
    signIn = driver.find_element_by_xpath('//a[@href="https://robinhood.com/login"]')
    signIn.click()
    time.sleep(5)
    username = driver.find_element_by_name('username')
    username.send_keys(input('Enter your Robinhood email'))
    password = driver.find_element_by_name('password')
    password.send_keys(input('Enter your Robinhood password'))
    signInButton = driver.find_element_by_tag_name('button')
    signInButton.click()
    time.sleep(10)

    # sell the selected stock
    selectedStock = driver.find_element_by_xpath('//a[@href="/stocks/' + stock + '"]')
    selectedStock.click()
    time.sleep(5)
    sellStock = driver.find_element_by_xpath('/html/body/div[1]/div/main/div[2]/div/div[1]/div/main/div[2]/div[2]/div/form/header/div/div[1]/div/div[2]')
    sellStock.click()
    numberOfShares = driver.find_element_by_xpath('//input[@data-testid="OrderFormRows-Shares"]')
    numberOfShares.send_keys('10')
    reviewOrderButton = driver.find_element_by_xpath('//button[@data-testid="OrderFormControls-Review"]')
    reviewOrderButton.click()



robinhoodBuyAutomation('XXII')

