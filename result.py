"""
This code gets result of NIT Raipur students from command line
Author: @appi147
"""
from io import BytesIO
from PIL import Image
from selenium import webdriver


def load_first(rollNo, sem):
    """
    This function has to be run only once at beginning.
    """
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
    """
    This function fetches and returns SPI of student
    """
    roll = driver.find_element_by_id('txtRegno')
    roll.clear()
    roll.send_keys(rollNo)
    showResult = driver.find_element_by_id('btnimgShowResult')
    showResult.click()
    SPI = driver.find_element_by_id('lblSPI')
    return SPI.text


def get_cpi(rollNo):
    """
    This function fetches and returns SPI of student
    """
    roll = driver.find_element_by_id('txtRegno')
    roll.clear()
    roll.send_keys(rollNo)
    showResult = driver.find_element_by_id('btnimgShowResult')
    showResult.click()
    CPI = driver.find_element_by_id('lblCPI')
    return CPI.text


def screenshot_full_screen(fileName):
    """
    This function takes full screen screenshot.
    Useful in debugging
    """
    driver.save_screenshot('img/' + fileName + '.png')


def get_screenshot_of_result(rollNo):
    """
    This function takes scrrenshot of result
    """
    roll = driver.find_element_by_id('txtRegno')
    roll.clear()
    roll.send_keys(rollNo)
    showResult = driver.find_element_by_id('btnimgShowResult')
    showResult.click()
    # Credits for following lines : https://gist.github.com/jsok/9502024
    screen = driver.get_screenshot_as_png()
    image = Image.open(BytesIO(screen))
    box = (40, 666, 631, 1390)  # Just some hardcoded cropping box
    requiredRegion = image.crop(box)
    requiredRegion.save('img/' + rollNo + '.png', 'PNG', optimize=False, quality=100)


if __name__ == '__main__':
    # Loading of driver
    driver = webdriver.PhantomJS()
    # Opening results page
    driver.get('http://results.nitrr.ac.in/Default.aspx')
    # load first has to be executed only once
    load_first('15116015', 'V')
    # remaining code goes here
    get_screenshot_of_result('15116015')
    print(get_cpi('15116015'))
    print(get_spi('15116015'))
