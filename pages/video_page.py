import logging
import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class VideoPage(BasePage):
    TEST_AUTOMATION_PROJECT = (By.XPATH, "//div[@title='Test automation project']")
    DETAILS_TAB = (By.XPATH, "//a[text()='Details ']")
    VIDEOS_TAB = (By.XPATH, "//a[text()='Videos ']")
    # PLAY_BUTTON = (By.CSS_SELECTOR, "button.play")
    PLAY_BUTTON = (By.XPATH, "//button[@aria-label='Play Video']")
    # PAUSE_BUTTON = (By.XPATH, "//div[@aria-label='Pause']")
    PAUSE_BUTTON = (By.CSS_SELECTOR, "div.jw-icon.jw-icon-display")
    CONTINUE_WATCHING = (By.XPATH, "//button[@aria-label='Continue Watching']")
    VOLUME_BUTTON = (By.XPATH, "//div[@aria-label='Mute button']")
    VOLUME_SLIDER = (By.XPATH, "//div[@aria-label='Volume' and @class= 'jw-overlay jw-reset']")
    SETTINGS_BUTTON = (By.CSS_SELECTOR, "div.jw-settings-submenu-button.jw-icon-settings")
    RES_480P = (By.XPATH, "//button[text()='480p']")
    RES_720P = (By.XPATH, "//button[text()='720p']")
    BACK_BUTTON = (By.XPATH, "//button[@aria-label='Go Back and continue playing video']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button#signOutSideBar")

    def navigate_to_project(self):
        logging.info("clicking project..")
        self.click(self.TEST_AUTOMATION_PROJECT)

    def switch_to_details_tab(self):
        self.click(self.DETAILS_TAB)

    def switch_to_videos_tab(self):
        self.click(self.VIDEOS_TAB)

    def play_video(self):
        self.click(self.PLAY_BUTTON)

    def pause_video(self):
        # Switch to iframe if the video is embedded
        iframe = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        self.driver.switch_to.frame(iframe)

        # Click on the video to make controls visible
        video_player = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='jw-media jw-reset']/video")))
        # self.driver.execute_script("arguments[0].click();", video_player)

        video_player.send_keys(Keys.SPACE)  # Press space key to pause
        # Switch back to the default content after interacting
        self.driver.switch_to.default_content()

    def continue_watching(self):
        self.click(self.CONTINUE_WATCHING)

    def adjust_volume(self, level=50):
        # Switch to iframe if the video is embedded
        iframe = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        self.driver.switch_to.frame(iframe)
        volume_button = self.wait.until(EC.element_to_be_clickable(self.VOLUME_BUTTON))

        # Use ActionChains to hover over the settings button to avoid click interception
        ActionChains(self.driver).move_to_element(volume_button).perform()

        volume_element = self.wait.until(EC.presence_of_element_located(self.VOLUME_SLIDER))
        self.driver.execute_script("arguments[0].value = arguments[1]", volume_element, level)
        # Switch back to the default content after interacting
        self.driver.switch_to.default_content()

    def change_resolution(self):
        iframe = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        self.driver.switch_to.frame(iframe)

        settings_button = self.wait.until(EC.element_to_be_clickable(self.SETTINGS_BUTTON))

        # Use ActionChains to hover over the settings button to avoid click interception
        ActionChains(self.driver).move_to_element(settings_button).click().perform()

        # Select 480p resolution
        res_480p = self.wait.until(EC.element_to_be_clickable(self.RES_480P))
        # self.driver.execute_script("arguments[0].click();", res_480p)
        self.click(res_480p)
        # Wait and click settings again to reopen menu
        self.click(self.SETTINGS_BUTTON)

        time.sleep(3)
        print("clicked on setting btn")
        # Select 720p resolution
        res_720p = self.wait.until(EC.element_to_be_clickable(self.RES_720P))
        self.click(res_720p)
        self.driver.switch_to.default_content()

    def exit_project(self):
        self.click(self.BACK_BUTTON)

    def logout(self):
        self.click(self.LOGOUT_BUTTON)
