from urllib.request import urlopen
page=urlopen("http://public.gr/")

#Fetches the code
#of the webpage
content = page.read()

print(content)
