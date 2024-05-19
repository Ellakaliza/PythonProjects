import requests
from bs4 import BeautifulSoup



def get_store(listing):
    store_element_retailer = listing.select_one('.topictitle_retailer')
    store_element = listing.select_one('.topictitle')

    if store_element_retailer:
        return store_element_retailer.text.strip()
    elif store_element:
        store_text = store_element.text.strip()
        return store_text.split(']')[0][1:].strip() if ']' in store_text else store_text
    else:
        return "N/A"


def latestdeals():
    url = "https://forums.redflagdeals.com/"
    response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    counter = 0
    base_url = "https://forums.redflagdeals.com/"
    for count in soup.find_all("li", class_="row topic"):
        counter += 1
    print(f"Total deals found: {counter}\n")
    for listing in soup.find_all("li", class_="row topic"):
        count1 = 0
        store = get_store(listing)

        item_element = listing.select_one('.topic_title_link')
        item = item_element.text.strip() if item_element else "N/A"

        votes_element = listing.select_one('.total_count_selector')
        votes = votes_element.text.strip() if votes_element else "N/A"

        username_element = listing.select_one('.thread_meta_author')
        username = username_element.text.strip() if username_element else "N/A"

        timestamp_element = listing.select_one('.first-post-time')
        timestamp = timestamp_element.text.strip() if timestamp_element else "N/A"

        category_element = listing.select_one('.thread_category a')
        category = category_element.text.strip() if category_element else "N/A"

        replies_element = listing.select_one('.posts')
        replies = replies_element.text.strip() if replies_element else "N/A"

        views_element = listing.select_one('.views')
        views = views_element.text.strip() if views_element else "N/A"

        url_element = item_element['href'] if item_element else "N/A"
        url = base_url + url_element

        print(f"    Store: {store}")
        print(f"    Title: {item}")
        print(f"    Votes:{votes}")
        print(f"    Username:{username}")
        print(f"    Timestamp:{timestamp}")
        print(f"    Category:{category}")
        print(f"    Replies:{replies}")
        print(f"    Views:{views}")
        print(f"    Url: {url}")
        print("-------------------------")


if __name__ == "__main__":
    latestdeals()
print("THIS IS ELLA'S CLASS")
Lat1 = LatestDeals()
