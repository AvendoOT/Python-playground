import urllib.request
import re
import sys


def main():

    address = sys.argv[1]
    page = urllib.request.urlopen(address)
    page = page.read()
    page = page.decode("utf8")

    #links = re.findall(r'href="h.*?"', page) # parsing just href (all, with duplicates)
    hosts = {}

    print("Links to other pages:")

    for match in re.findall(r'href="h.*?"', page) :

    	matchy = re.search(r'"https?://((www.)?(.*?)(/.*)?)"', match)

    	url = matchy.group(1)
    	host = matchy.group(3)

    	print(url)

    	if host in hosts:
        	hosts[host] = hosts[host] + 1
    	else:
        	hosts[host] = 1

    print("\nHosts:")

    for host in hosts.keys():
        print(host, "is repeating", hosts[host], "times")

    print("\nE-Mails:")

    mails = []
    for match in re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", page):
        if not match in mails: # unique mails
            mails.append(match)
        print(match)
    
    print("\nNumber of picture links:")
    pics = re.findall(r'img.*src="([^"]+)"', page)
    print(len(pics), "pictures")


if __name__ == "__main__":
    main()
