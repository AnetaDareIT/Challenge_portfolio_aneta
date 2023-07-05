# Task 1: SOFTWARE CONFIGURATION
## Subtask 1: Why did I decide to participate in the Dare IT Challenge?
### I am a pharmacist aware that the world of medicines and medicine is closely related to IT. I am fascinated by the opportunity to work on projects related to this topic. My goal is to take advantage of this opportunity. I expect the course to help me do so 😊
#### My test result: 12/14

# Task 2: SELECTORS

<li> scouts_panel_title_xpath</li>


//*[@id="__next"]/form/div/div[1]/h5<br>
//*[contains(@class, "MuiTypography-root MuiTypography")]<br>
//h5


<li> login_field_xpath</li>

//*[@id="login"]<br>
//input[@type="text"]<br>
//input[@name="login"]

<li> password_field_xpath</li>

//*[@id="password"]<br>
//input[@type="password"]<br>
//input[@type="password"]

<li> remaind_password_hyperlink_xpath</li>

//*[@id="__next"]/form/div/div[1]/a<br>
//*[contains(@class, "MuiTypography-root MuiLink")]<br>
//a [text()="Remind password"]


<li> listbox_language_xpath</li>

//*[@id="__next"]/form/div/div[2]/div/div<br>
//div[@aria-haspopup="listbox"]<br>
//div[@role="button"]

<li>sign_in_button_xpath</li>

//*[@id="__next"]/form/div/div[2]/button/span[1]<br>
//button[@type="submit"]<br>
//span[@class="MuiButton-label"]/parent::button