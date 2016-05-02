from scrapy import cmdline

#script for easier PyCharm debugging

def main():
    cmdline.execute("scrapy crawl socareers".split())

if __name__ == "__main__":
    main()