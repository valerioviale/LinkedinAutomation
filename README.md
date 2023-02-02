# LinkedinAutomation
A collection of linkedin automation files
It's a collection of scripts and bots to automate activity on linkedin.
You need Python, Selenium and an editor. I tested both Visual Studio Code and Jupyter. The bots work on both MacOs and Windows.

To install Selenium

Using pip:
pip install selenium

On Windows if you need to install Python you should go there:
https://www.python.org/downloads/

It's not necessary to install webdriver since to make it more portable we use in both files:
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #starts the webdriver

That should be used only to testing since Linkedin does not allow scraping on the website.
That's why is so complex to do it and it's also why it needs so much maintenance.
Read carefully my comments and use a dummy account to avoid your official account being banned by Linkedin.
