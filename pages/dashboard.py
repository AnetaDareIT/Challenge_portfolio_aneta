from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_title_xpath = "//*[@id="__next"]/div[1]/header/div/h6"
    main_page_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//*[text()="Players"]"
    change_language_button_xpath = "//*/ul[2]/div[1][@role="button"]"
    sign_out_button_xpath = "//span[text()='Sign out']"
    players_count_section_xpath = "//*[@id="__next"]/div[1]/main/div[2]/div[1]/div"
    matches_count_section_xpath"//div[text() = 'Matches count']"
    logo_scouts_panel_xpath = "// div[ @ title = "Logo Scouts Panel"]"
    dev_team_contact_button_xpath = "//a[@target='_blank']"
    report_panel_xpath = "//div[@class="MuiCardContent-root"]/p"

pass