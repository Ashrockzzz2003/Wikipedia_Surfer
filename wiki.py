import wikipedia
import requests
from bs4 import BeautifulSoup
import webbrowser
import time


def print_list(l):
    for i in range(len(l)):
        print(f'{i+1}. {l[i]}')


flag = 1

while (flag == 1):
    user_choice = int(input(
        "\n\nWelcome to Wikipedi Explorer!\n\nDo you want to\n1. Read about a particular Topic\n2. Pick me a Random Topic\n\nEnter your choice number: "))
    if (user_choice == 1):
        key = str(input("\nEnter the topic you wish to read about today: "))
        print("\n\nRelated Topics:\n")

        topics = list(wikipedia.search(key, results=5))

        print_list(topics)

        topic_flag = False
        while (topic_flag == False):
            topic_state = int(
                input("\nIs your Topic in the above list?\n[Yes -> 1, No -> 0]: "))
            if (topic_state != 1 and topic_state != 0):
                print("\nInvalid Choice! Press either 0 or 1!!\n")
                topic_flag == False
            else:
                topic_flag = True
        if (topic_state == 1):
            index_flag = False
            while (index_flag == False):
                key_index = int(
                    input("\nEnter the Topic number from the list: "))
                if (key_index < 1 and key_index > len(topics)):
                    print(
                        f"\nInvalid Topic Number! It should be in the range [1, {len(topics)}]!")
                    print_list("\nTOPICS\n", topics)
                    key_index = int(
                        input("\nEnter the Topic number from the list: "))
                else:
                    index_flag = True
            key = topics[key_index - 1]
            #print(f"\n\n{wikipedia.page(key).title}")
            b_flag = False
            while (b_flag == False):
                browser_choice = int(input(
                    "\n\nDo you want to see in browser or here?\n1. Browser\n2. Here\n\nEnter your choice: "))
                if (browser_choice != 1 and browser_choice != 2):
                    print("\nInvalid Choice! Press either 1 or 2!!\n")
                    b_flag == False
                else:
                    b_flag = True
            if(browser_choice == 1):
                url = requests.get(f"https://en.wikipedia.org/wiki/{key}")
                soup = BeautifulSoup(url.content, "html.parser")
                title = soup.find(class_="firstHeading").text
                url = "https://en.wikipedia.org/wiki/%s" % title
                webbrowser.open(url)
                flag = int(
                    input("\n\nIn a mood to read more?\n[Yes -> 1, No -> 0]: "))
            elif(browser_choice == 2):
                url = requests.get(f"https://en.wikipedia.org/wiki/{key}")
                soup = BeautifulSoup(url.content, "html.parser")
                content = soup.find(class_="mw-body-content mw-content-ltr").text
                title = soup.find(class_="firstHeading").text
                print(
                    f"\n\nTITLE: {title}\n\n{content}")
                flag = int(
                    input("\n\nIn a mood to read more?\n[Yes -> 1, No -> 0]: "))
        else:
            print(f"\nSorry {key} doesn't exist! Try Again!")
            flag = int(
                    input("\n\nWant to try another one?\n[Yes -> 1, No -> 0]: "))

    elif (user_choice == 2):
        satisfaction = False
        while satisfaction == False:
            url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
            soup = BeautifulSoup(url.content, "html.parser")
            title = soup.find(class_="firstHeading").text
            topic_flag = False
            while (topic_flag == False):
                print(f"\nTITLE: {title}\n")
                topic_state = int(
                    input("\nDoes this interest you?\n[Yes -> 1, No -> 0]: "))
                if (topic_state != 1 and topic_state != 0):
                    print("\nInvalid Choice! Press either 0 or 1!!\n")
                    topic_flag == False
                elif(topic_state == 1):
                    satisfaction = True
                    topic_flag = True
                elif(topic_state == 0):
                    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
                    soup = BeautifulSoup(url.content, "html.parser")
                    title = soup.find(class_="firstHeading").text
                    
            b_flag = False
            while (b_flag == False):
                browser_choice = int(input(
                    "\n\nDo you want to see in browser or here?\n1. Browser\n2. Here\n\nEnter your choice: "))
                if (browser_choice != 1 and browser_choice != 2):
                    print("\nInvalid Choice! Press either 1 or 2!!\n")
                    b_flag == False
                else:
                    b_flag = True
            if(browser_choice == 1):
                url = "https://en.wikipedia.org/wiki/%s" % title
                webbrowser.open(url)
                flag = int(
                    input("\n\nIn a mood to read more?\n[Yes -> 1, No -> 0]: "))
            elif(browser_choice == 2):
                url = requests.get(f"https://en.wikipedia.org/wiki/{title}")
                soup = BeautifulSoup(url.content, "html.parser")
                content = soup.find(class_="mw-body-content mw-content-ltr").text
                print(
                    f"\n\nTITLE: {title}\n\n{content}")
                flag = int(
                    input("\n\nIn a mood to read more?\n[Yes -> 1, No -> 0]: "))


print("\n\nThank you for using my Wikipedia Explorer!\nDeveloped by\nASHWIN NARAYANAN S")
time.sleep(5)