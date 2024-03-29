from selenium import webdriver


class Browser:
    def __init__(self, chromedriver_path: str) -> None:
        self._chromedriver_path = chromedriver_path

    def __enter__(self):
        # Первый этап обхода CloudFlare.
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')

        # Создать браузер с опциями.
        self.browser = webdriver.Chrome(executable_path=self._chromedriver_path, options=options)

        # Второй этап обхода CloudFlare. Удалить маркеры роботизированного ПО из браузера.
        self.browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': """
                        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
                        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
                        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
                    """
        })

        # Задать неявную задержку.
        self.browser.implicitly_wait(2)

        return self.browser

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.quit()
