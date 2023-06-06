# theScore QA Challenge
This repo is a submission for theScore's QA Challenge, using Python, Behave, and Appium 2.0.

![leage_table_test](https://github.com/sohum/theScore-qa-challenge/assets/8813530/040c6573-5137-47af-ac54-faab3a46c680)

## Prerequisites
- [Python 3.9+](https://www.python.org/downloads/release/python-396/)
- Appium 2.0
  - Requires [Node](https://nodejs.org/en/download), npm
    ```bash
    # Install Appium 2.0
    $ npm install -g appium@next
  
    # Install the UiAutomator2 driver
    $ appium driver install uiautomator2
    ```
- A local Android emulator 
  - Install [Android Studio](https://developer.android.com/studio), [ Android SDK Platform Tools](https://developer.android.com/tools/releases/platform-tools)
  - Follow [this](https://developer.android.com/studio/run/managing-avds) guide on how to set up an Android Virtual Device
    - This test suite was developed with an Android 13.0 (API 33) emulator

## Installation
In the project's root directory, run
```bash
    # Install all Python dependencies
    $ pip3 install -r requirements.txt
```

## Usage
1. Set theScore account credentials in [secrets.js](secrets.js)
   - **This test suite requires a theScore account with the England, Germany, and Spain soccer leagues favorited!**
2. Launch an Android emulator
3. Start an Appium server
```bash
    # Start Appium server
    $ appium
```
4. In the project's root directory, run
```bash
    # To run all tests
    $ behave
```

## Documentation
The test specification for the scenarios implemented can be found [here](features/League.feature).

For a detailed explanation on some of the rationale behind the approach to this challenge, please refer to [this](https://docs.google.com/document/d/1BWQp8D1jqVWnu_AusRcwWBQy2Sd185nuhs15s_aZFYU/edit?usp=sharing) document.

### Project Structure
- _[pages/](pages)_: page objects for the various pages and components interacted with so far in the app
  - _[components/](pages/components)_: page objects for areas of the app that are visible across multiple screens, eg. the bottom nav bar, toolbar, etc.
- _[features/](features)_: Gherkin feature files that serve as the layout for scenarios and steps for the tests, and also as documentation for non-technical stakeholders 
  - _[steps/](features/steps)_: Actions from various pages are combined to become test steps. These step definitions link to steps in feature files
- _[helpers/](helpers)_: contains helper methods that are not directly related to the functionality of the app, but support the test suite during runtime
- _[secrets.js](secrets.js)_: a small JSON object that can be stored locally to house sensitive data like email addresses and passwords
- _[requirements.txt](requirements.txt)_: a list of Python dependencies for the project, installable via the `pip3` command
- _[thescore_23.6.0.apk](thescore_23.6.0.apk)_: a version of theScore's Android application for the purpose of this challenge
