import time

from behave import given, when, then

from pages.login_page import LoginPage
from pages.video_page import VideoPage


@given("I am logged in to the platform")
def step_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()
    context.login_page.login()


@when("I navigate to the Test Automation Project")
def step_navigate_project(context):
    context.video_page = VideoPage(context.driver)
    context.video_page.navigate_to_project()


@when("I switch to the Details tab")
def step_switch_details(context):
    context.video_page.switch_to_details_tab()


@when("I wait for 5 seconds")
def step_wait_details(context):
    time.sleep(5)


@when("I switch back to the Videos tab")
def step_switch_videos(context):
    context.video_page.switch_to_videos_tab()


@when("I play the video")
def step_play_video(context):
    context.video_page.play_video()


@when("I wait for 10 seconds")
def step_wait_play(context):
    time.sleep(5)


@when("I pause the video")
def step_pause_video(context):
    context.video_page.pause_video()


@when("I continue watching the video")
def step_continue_video(context):
    context.video_page.continue_watching()


@when("I adjust the volume to 50%")
def step_adjust_volume(context):
    context.video_page.adjust_volume(50)


@when("I change the resolution to 480p and then 720p")
def step_change_resolution(context):
    context.video_page.change_resolution()


@when("I exit the project")
def step_exit_project(context):
    context.video_page.exit_project()


@then("I logout")
def step_logout(context):
    context.video_page.logout()
