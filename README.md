# Instagram-Story-viewing-Bot
Basic Instagram story-viewing bot, built using Selenium and used to automate story viewing.

When ran, the bot types in the user-provided username and password, closes notifications and efficiently loops through stories.

# How to Use
All the code is provided in the 'new.py' file.
You should be able to run the code after specifying the path to geckodriver and adding driverpath to the webdriver.Firefox() call, installing Firefox as well as the required libraries:

```
pip install selenium
pip install time
```

The code is initiated as a class called InstaBot. Create an instance of the class under a new name (already done, line 98) and call the functions from the class.
 
# Important note

Built for Croatian version of Instagram.
