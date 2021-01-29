from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class Driver:

    def __init__(self, see):
        chromeOptions = Options()
        if see:
            chromeOptions.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        self.driver.get('https://unifix.repairdesk.co/')
        self.username = 'Davidcastillo07@yahoo.com'
        self.password = 'starwars'
        self.login()
        return

    def login(self):
        # Wait for the Page to load
        loginButton = '/html/body/div[2]/div/div[1]/div[1]/div/div[1]/div/div/form/div[5]/button'
        self.waitLoad(loginButton)

        # Input user login information
        usernamePath = '/html/body/div[2]/div/div[1]/div[1]/div/div[1]/div/div/form/div[3]/input'
        passwordPath = '/html/body/div[2]/div/div[1]/div[1]/div/div[1]/div/div/form/div[4]/input'

        self.driver.find_element_by_xpath(usernamePath).send_keys(self.username)
        self.driver.find_element_by_xpath(passwordPath).send_keys(self.password)
        self.driver.find_element_by_xpath(loginButton).click()

        # Check to make sure we were not rejected by the website
        try:
            noDiv = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div/div[1]/div[1]/div/div[1]/div/div/form/div[3]')
            # Failure Div exists
            print("Login Failed as " + self.username + "\nReason:\n'" + noDiv.text + "'")
        except NoSuchElementException:
            # Logged in
            print("Logged In Successfully as " + self.username)

    def waitLoad(self, pathToDiv, textOfDiv=None):
        stopBool = False
        while not stopBool:
            try:
                div = self.driver.find_element_by_xpath(pathToDiv)
                if textOfDiv == div.text or textOfDiv is None:
                    stopBool = True
            except NoSuchElementException:
                continue
        return
