from selenium import webdriver
from time import sleep
import userPass


def scroolDown():
    jsCommand = """
    page = document.querySelector(".isgrP");
    page.scrollTo(0,page.scrollHeight);
    var endPage = page.scrollHeight;
    return endPage;
    """
    endPage = browser.execute_script(jsCommand)
    while True:
        last = endPage
        sleep(2)
        endPage = browser.execute_script(jsCommand)
        if last == endPage:
            break


instaPath = "https://www.instagram.com/"
browser = webdriver.Firefox(executable_path="C:/Users/berka/PycharmProjects/untitled1/geckodriver.exe")
browser.maximize_window()
browser.get(instaPath)
sleep(2)

# Login
browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(
    userPass.username)
browser.find_element_by_xpath(
    "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(
    userPass.password)
browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
sleep(5)
browser.get(instaPath + userPass.username)

# # Get the Followers
sleep(1)
browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
sleep(2)
scroolDown()
followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
followersText = []

for f in followers:
    followersText.append(f.text)

# Get who you follow
sleep(5)
browser.get(instaPath + userPass.username)
browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
sleep(3)
scroolDown()
youFollows = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
youFollowText = []

for f in youFollows:
    youFollowText.append(f.text)


def diff(li1, li2):
    return list(set(li1) - set(li2))


result = diff(youFollowText, followersText)

print("People who doesn't follow you\n")

for f in result:
    print(f)
