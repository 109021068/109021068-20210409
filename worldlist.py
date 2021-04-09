import requests
import time
from bs4  import BeautifulSoup


URL = "https://www.majortests.com/word-lists/word-list-0{0}.html"

def generate_urls(url, start_page, end_page):
    urls = []
    for page in range(start_page, end_page):
        urls.append(url.format(page))
    return urls


def get_resource(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    return requests.get(url, headers=headers)

def parse_html(html_str):
    return BeautifulSoup(html_str, "lxml")


def get_word(soup, file):
    words = []
    count = 0
    for wordlist_table in soup.find_all(class_="wordlist"):
        count += 1
        for word_entry in wordlist_table.find_all("tr"):
            new_word = []
            new_word.append(file)
            new_word.append(str(count))
            new_word.append(word_entry.th.text)
            new_word.append(word_entry.td.text)
            words.append(new_word)
    return words      

def web_scraping_bot(urls):
    eng_words = []
    for url in urls:
        file = url.split("/")[-1]
        print("catching: ", file, "web data...")
        r = get_resource(url)
        if r.status_code == requests.codes.ok:
            soup = parse_html(r.text)
            words = get_word(soup, file)
            eng_words = eng_words + words
            print("waiting 5 seconds...")
            time.sleep(5)
        else:
            print("HTTP request error!!")
    return eng_words

def save_to_csv(word, file):
    with open(file, "w+", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        for word in words:
            writer.writerow(word)

if __name__ == "__main__":
    urlx = generate_urls(URL, 1, 3)
    eng_words = web_scraping_bot(urlx)
    for item in eng_words:
        print(item)
    save_to_csv(eng_words, "engWordList 1.csv") 


#if __name__ == "__main__":
    #urlx = generate_urls(URL, 1, 3)
    #eng_words = web_scraping_bot(urlx)
    #print(eng_words)
    #for url in urls:
        #file = url.split("/")[-1]
        #print("catching: ", file, "web data...")
        #r = get_resource(url)
        #if r.status_code == requests.codes.ok:
            #soup = parse_html(r.text)
            #words = []
            #count = 0
            #for wordlist_table in soup.find_all(class_="wordlist"):
                #count += 1
                #for word_entry in wordlist_table.find_all("tr"):
                    #new_word = []
                    #new_word.append(file)
                    #new_word.append(str(count))
                    #new_word.append(word_entry.th.text)
                    #new_word.append(word_entry.td.text)
                    #words.append(new_word)
            #print(words)
            #print("------------\n\n")
        #else:
            #print("HTTP request error!!")
        #print("sleep 5 second")
        #time.sleep(5)