** Settings ***
Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot
Library        unicon.robot.UniconRobot

*** Variables ***
# Defining variables that can be used elsewhere in the test data.
# Can also be driven as dash argument at runtime
${testbed}     testbed.yaml
${verification_datafile}    /usr/local/lib/python3.8/dist-packages/genie/libs/sdk/genie_yamls/verification_datafile.yaml

*** Test Cases ***
# Creating test cases from available keywords.

Connect
    use genie testbed "${testbed}"
    connect to devices "R1"

verify Interfaces
    run verification "Verify" on device "R1"
