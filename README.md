QA Exercise - ioet by Daniel Mora

----Project Description:
This project is intended for automated testing the 3 user stories ioet provided for the exercise which are:
User Story 1
As a user 
I want to log in
So that I can access the online shop

User Story 2
As a standard user
I can review all the items
So that I can choose the ones I want

User Story 3
As a standard user
I can add items to the shopping car
So that I can review the cost of all of them

The project has 3 python scripts: 
1. user_login.py
2. standard_user_testing.py
3. security_test.py

The user_login.py script will test the login function by iterating through every user the webpage (https://www.saucedemo.com) has as well as testing for other user input. The script will provide a message if the login it's successful or not.
The standard_user_testing.py will test the whole process of login with a standard user, reviewing the access to every item through its image and title (so it will access the same item twice), and adding every item to the shopping car so it can procede to the checkout.
The security_test.py will test if the site has a Cross-Site Scripting (XSS) vulnerability inside its login.

----Technologies used:
*Python 3.12.2
*Selenium 4.18.1
*VsCode 1.87.0

----Installation process:
1. Make sure you have Python installed on your device. For this, you can download Python from here: https://www.python.org/. In my case I used the 3.12.2 version. 
Once you downloaded the installation wizard you just have to follow the wizard steps. I highly suggest you check the option for adding the PATH to the windows environment variables.
To check if it is installed correctly just open a cmd and type: python --version or py --version. It will show the version if the installation was done correctly.

2. Then you need to install Selenium by typing in the cmd: pip install selenium. In case that does not work try: py -m pip install selenium

3. You need to install the chrome webdriver. In my case I used the 122.0.6261.111 and I downloaded from here: https://googlechromelabs.github.io/chrome-for-testing/ . Be sure to match the platform and the version of your Chrome driver; you can check it at by clicking the 3 dots in the top right corner of your Chrome browser, the Help - About Google Chrome.

4. In my case I used VsCode as my text editor to run and test my python scripts. If using VsCode I suggest you add the Python(2024.2.1) and Code Runner(v0.12.1) inside the Extensions tab (I used the latest versions for both of them). 
Then you can open the QAExercise_ioet folder which will contain it's 3 python scripts. You can test every script independently and easily with the help of Code Runner by using the top right play button and if you use the dropdown you will see the option "Run Python File".
![image](https://github.com/T0KK3N/QAExercise_ioet/assets/43867402/6afc0798-de3a-4e6b-aba7-699d182b86a2)

----Contact Information:
If you have any questions feel free to contact me at danielmora414@gmail.com

 



