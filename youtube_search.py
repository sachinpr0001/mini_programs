from selenium import webdriver

r = input()

if r:
	
	driver = webdriver.Chrome()
	driver.get('https://youtube.com')

	# here we need the 'full XPath' for the search box
	searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
	searchbox.send_keys(r)

	searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
	searchButton.click()