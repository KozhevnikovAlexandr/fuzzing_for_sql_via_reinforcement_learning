import os

print("URL:")
url = input()  # Target URL.
batch = True  # Never ask for user input, use the default behaviour. Valid: True or False
forms = True  # Parse and test forms on target URL. Valid: True or False
crawlDepth = 2  # Crawl the website starting from the target URL. Valid: integer
answers = (
    "sitemap=y",  # do you want to check for the existence of site's sitemap(.xml) [y/N]
    "follow=y",  # got a 302 redirect to '...'. Do you want to follow? [Y/n]
    "normalize crawling results=y",  # do you want to normalize crawling results [Y/n]
    "store crawling result=y",  #  do you want to store crawling results to a temporary file for eventual further processing with other tools [y/N]
    "reduce=y",  # it is recommended to perform only basic UNION tests if there is not at least one other (potential) technique found. Do you want to reduce the number of requests? [Y/n]
    "other DBMSes=y",  # it looks like the back-end DBMS is '...'. Do you want to skip test payloads specific for other DBMSes? [Y/n]
    "remaining tests=y",  # for the remaining tests, do you want to include all tests for 'MySQL' extending provided level (1) and risk (1) values? [Y/n]
    "keep testing=y",  # POST parameter '...' is vulnerable. Do you want to keep testing the others (if any)? [y/N]
    "exploit=n",  # do you want to exploit this SQL injection? [Y/n]
    "skip further tests=n",  # SQL injection vulnerability has already been detected against '...'. Do you want to skip further tests involving it? [Y/n]
    "threads=1"  # please enter number of threads? [Enter for 1 (current)]
)
options = {
    "--batch": batch,
    "--forms": forms,
    "--crawl=": crawlDepth > 0,
    "--answers=": len(answers) > 0
}
command = "python sqlmap.py -u \"{}\"".format(url)
for option in options:
    if options[option]:
        command = command + " {}".format(option)
        if option == "--crawl=":
            command += str(crawlDepth)
        if option == "--answers=":
            command += "\"{}\"".format(','.join(answers))
os.system(command)