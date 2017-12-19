import time
from selenium import webdriver

def load_first(rollNo, sem):
    roll = driver.find_element_by_id('txtRegno')
    roll.send_keys(rollNo)
    showButton = driver.find_element_by_id('btnimgShow')
    showButton.click()
    semester = driver.find_element_by_id('ddlSemester')
    for option in semester.find_elements_by_tag_name('option'):
        if option.text == sem:
            option.click()
    showResult = driver.find_element_by_id('btnimgShowResult')
    showResult.click()

def get_spi(rollNo):
    roll = driver.find_element_by_id('txtRegno')
    roll.clear()
    roll.send_keys(rollNo)
    showResult = driver.find_element_by_id('btnimgShowResult')
    showResult.click()
    SPI = driver.find_element_by_id('lblSPI')
    return SPI.text

def screenshot(fileName):
    driver.save_screenshot(fileName + '.png')

if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    driver.get('http://results.nitrr.ac.in/Default.aspx')
    load_first('15116015', 'V')
    print get_spi('15116015')
