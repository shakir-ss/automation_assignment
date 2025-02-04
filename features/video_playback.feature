Feature: Automate video playback and control

    Scenario: Automate video playback functionality
        Given I am logged in to the platform
        When I navigate to the Test Automation Project
        And I switch to the Details tab
        And I wait for 5 seconds
        And I switch back to the Videos tab
        And I play the video
        And I wait for 10 seconds
        And I pause the video
        And I continue watching the video
        And I adjust the volume to 50%
        And I change the resolution to 480p and then 720p
        And I pause the video
        And I exit the project
        Then I logout