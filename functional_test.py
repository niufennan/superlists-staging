from selenium import webdriver
executable_path="C:\\Program Files (x86)\\Mozilla Firefox"
browser=webdriver.Firefox()

browser.get("http://localhost:8000")

assert "Django" in browser.title