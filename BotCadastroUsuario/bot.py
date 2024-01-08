# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.CHROME
    bot.driver_path = r"C:\Users\lohan\Desktop\Projetos\Python\bots\webbot\webbot_cadastro_usuario\BotCadastroUsuario\resources\chromedriver.exe"

    # Opens the BotCity website.
    bot.browse("https://forms.gle/xHTTbRvvohSR1JyUA")

    
    INPUT_NAME = bot.find_element(
        selector='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input', 
        by=By.XPATH,
        ensure_clickable=True
    )

    INPUT_IDADE = bot.find_element(
        selector='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
        by=By.XPATH
    )

    SELECT_MASCULINO = bot.find_element(
        selector='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[2]/div/span',
        by=By.XPATH
    )

    SELECT_FEMININO = bot.find_element(
        selector='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[2]/div/span',
        by=By.XPATH
    )

    INPUT_NAME.send_keys('Lohan')
    INPUT_IDADE.send_keys('25')
    SELECT_FEMININO.click()

    # Implement here your logic...
    ...

    # Wait 3 seconds before closing
    bot.wait(3000)


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
