# 1 - Biblioteca
import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage  # recebeer as funções da base_page


#   2 - Classe
class LoginPage(BasePage):
    # 2.1 - Mapeamento Elementos da página
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _login_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _success_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.success'}
    _failure_message = {'by': By.CSS_SELECTOR, 'value': 'div.flash.error'}
    #_login_form = {'by': By.ID, 'value': 'login'}

    # 2.2 Inicializador / Construtor (Java)
    def __int__(self, driver):
         # instanciando o Selenium
        self.driver = driver
        # abrindo a página

        #self._entrar('https://the-internet.herokuapp.com/login')
        # validando se o formulario de login
        #assert self._aparecer(self._login_form)

    def com_(self, username, password):#
        '''
        Programação Comum - Sem Page Object
        self.driver.find_elemente(self._username_input['by'],
                                  self._username_input['value']).send_keys(username)
        self.driver.find_elemente(self._password_input['by'],
                                  self._password_input['value']).send_keys(password)
        self.driver.find_elemente(self._login_button['by'],
                                  self._login_button['value']).click()
        '''

        self._entrar('https://the-internet.herokuapp.com/login')
        self._escrever(self._username_input, username)
        self._escrever(self._password_input, password)
        self._clicar(self._login_button)

    # 2.2.3 - Ações Realizaveis
    def vejo_mensagem_de_sucesso(self):
        '''
         Programação Comum - Sem Page Object
        return self.driver.find_elemente(self._success_message['by'],
                                  self._success_message['value']).is_displayed()


        '''
        return self._aparecer(self._success_message, 10)

    def vejo_mensagem_de_falha(self):
        '''
        Programação Comum - Sem Page Object
        return self.driver.find_elemente(self._failure_message['by'],
                                         self._failure_message['value']).is_displayed()
        '''
        return self._aparecer(self._failure_message, 10)
