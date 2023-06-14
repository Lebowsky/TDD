from selenium import webdriver


options = webdriver.FirefoxOptions()
options.add_argument("--width=300")
options.add_argument("--height=500")

browser = webdriver.Firefox(options=options)
browser.get('http://localhost:8000')

assert 'Django' in browser.title

if __name__ == '__main__':
    pass
