import time
import os
import fileinput
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


def save_credentials(username, password):
    with open("credentials.txt", "w") as file:
        file.write(f"{username}\n{password}")


def load_credentials():
    if not os.path.exists("credentials.txt"):
        return None

    with open("credentials.txt", "r") as file:
        lines = file.readlines()
        if len(lines) >= 2:
            return lines[0].strip(), lines[1].strip()

    return None


def prompt_credentials():
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    save_credentials(username, password)
    return username, password


def read_usernames_from_file(file_path):
    with open(file_path, "r") as file:
        usernames = [line.strip() for line in file]
    return usernames

def remove_username_from_file(username, file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip() != username:
                file.write(line)


def like_stories(username, password, usernames):
    # Set up ChromeDriver options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Set up ChromeDriver service
    service = Service(ChromeDriverManager().install())

    # Set up ChromeDriver instance
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Log in to Instagram
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Curtir story de cada seguidor
    for follower in usernames:
        story_url = f"https://www.instagram.com/stories/{follower}"
        driver.get(story_url)
        time.sleep(2)

        # Verifica se existe o botão de curtir story
        view_story_xpath = "//div/div/div[2]/div/div/div[1]/div[1]/section/div[1]/div/div/div/div[2]/div/div[3]/div"
        like_button_xpath = "//div/div/div[2]/div/div/div[1]/div[1]/section/div[1]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/span/div"
        like_button_xpath1 = "//div/div/div[2]/div/div/div[1]/div[1]/section/div[1]/div/div/div[1]/div[2]/div[3]/div[1]/div[2]/span/div"
        try:
            view_story_button = driver.find_element(By.XPATH, view_story_xpath)
            print("[TRUE] User -> " + follower + " tem um story disponível.")
            view_story_button.click()
            time.sleep(4)

            try:
                like_button = driver.find_element(By.XPATH, like_button_xpath)
                like_button.click()
                print("Story curtido com sucesso!")
                time.sleep(2)
            except NoSuchElementException:
                try:
                    # Tenta denovo caso a primeira tentativa falhe.
                    like_button = driver.find_element(By.XPATH, like_button_xpath1)
                    like_button.click()
                    print("Story curtido com sucesso na segunda tentativa!")
                    time.sleep(2)
                except NoSuchElementException:
                    print("Botão de curtir não encontrado.")

            
        except NoSuchElementException:
            print("[FALSE] User -> " + follower + " não tem story disponível.")
        except Exception as e:
            print("Um erro inexperado aconteceu:", str(e))


            remove_username_from_file(follower, followers_file)



if __name__ == "__main__":
    credentials = load_credentials()

    if credentials is None:
        username, password = prompt_credentials()
    else:
        username, password = credentials

    followers_file = "followers.txt"
    usernames = read_usernames_from_file(followers_file)

    like_stories(username, password, usernames)
