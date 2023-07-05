from pages.base_page import BasePage


class Dashboard(BasePage):
    player_button_xpath = "//ul[2]/div[1]"
    submit_button_xpath = "//button[@type="submit"]"
    clear_button_xpath = "//span[text()='Clear']//parent::button"
    my_team_field_xpath = "//input[@name='myTeam']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    my_team_score_field_xpath = "//input[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//input[@name='enemyTeamScore']"
    rating_field_xpath = "//input[@name="rating"]"
    date_field_xpath = "//input[@name='date']"
    sign_out_button_xpath = "//*[text()="Sign out"]"
pass