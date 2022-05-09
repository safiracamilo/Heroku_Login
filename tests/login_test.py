import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


@pytest.fixture  # como se fosse configucao
def login(request):
    # variavel local para armazenar o caminho do chromedriver
    print('>>> CWD == ' + os.getcwd())
    #_chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver.exe')
    _chromedriver = 'vendor/chromedriver.exe'

    if os.path.isfile(_chromedriver):
        # se existe um chromedriver dentro do projeto, instancie com ele
        driver_ = webdriver.Chrome(_chromedriver)  # ligando o selenium
    else:
        # se não existe, tente usar um chormedriver publico no ambiente
        driver_ = webdriver.Chrome()
    loginPage = LoginPage(driver_)  # instanciando a clase LoginPage e passando o Selenium

    def quit():
        driver_.quit()

    # sinalizando o fim da execução para o ambiente
    request.addfinalizer(quit)
    return loginPage


'''
# como eram os passos do jeito simples
def testar_login_valido(driver_):
    driver_.get('https://the-internet.herokuapp.com/login')
    driver_.find_element(By.ID, 'username').send_keys('tomsmith')
    driver_.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    driver_.find_element(By.CSS_SELECTOR, 'button.radius').click()
    assert driver_.find_element(By.CSS_SELECTOR, 'div.flash.success').is_displayed()
'''


# passos do jeito Page Objects
def testar_login_com_sucesso(login):
    # preencher o usuário, a senha e clicar no botão
    login.com_('tomsmith', 'SuperSecretPassword!')
    # validar a mensagem
    assert login.vejo_mensagem_de_sucesso()


def testar_login_com_invalidado(login):
    # preencher o usuário, a senha e clicar no botão
    login.com_('fada', 'SuperSecretPassword!')
    # validar a mensagem
    assert login.vejo_mensagem_de_falha()


def testar_login_com_senha_invalida(login):
    # preencher o usuário, a senha e clicar no botão
    login.com_('tomsmith', '12345')
    # validar a mensagem
    assert login.vejo_mensagem_de_falha()
