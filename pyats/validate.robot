** Settings ***
Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot
Library        unicon.robot.UniconRobot

*** Variables ***
# Defining variables that can be used elsewhere in the test data.
# Can also be driven as dash argument at runtime
${testbed}     testbed.yaml

*** Test Cases ***
# Creating test cases from available keywords.

Connect
    use genie testbed "${testbed}"
    connect to all devices

Verify Interfaces
    run verification "Verify_IpInterfaceBrief" on device "R1"