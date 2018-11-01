from selenium import webdriver
import time

driver = webdriver.Chrome()

# gets elem by id, assert its text equals the passed in value
def check_by_id(id, value):
    elem = driver.find_element_by_id(id)
    assert(elem.text == value)

def test_home():
    driver.get("http://199.116.235.226:8000/")

    # wait until all the objects zoom up
    time.sleep(5)

    check_by_id("name", "Ben Hart")
    check_by_id("about", "Just a small town boy...")
    check_by_id("education", "B.Sc. University of Alberta")
    check_by_id("skills", "I'm very skilled.")
    check_by_id("work", "I've worked for 16 months.")
    check_by_id("contact", "hreherch@ualberta.ca")

    driver.quit()