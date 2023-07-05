from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@type='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    listbox_language_xpath = "//div[@role='button']"
    scouts_panel_title_xpath = "//h5"
    remaind_password_hyperlink_xpath = "//[@id="__next"]/form/div/div[1]/a"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
#