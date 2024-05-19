# import sys
import requests
from bs4 import BeautifulSoup
from LatestDeals import LatestDeals


def get_store(listing):
    """

    :param listing:
    :return:
    """
    store_element_retailer = listing.select_one('.topictitle_retailer')
    store_element = listing.select_one('.topictitle')

    if store_element_retailer:
        return store_element_retailer.text.strip()
    elif store_element:
        # Extract store from the square brackets, if available
        store_text = store_element.text.strip()
        return store_text.split(']')[0][1:].strip() if ']' in store_text else store_text
    else:
        return "N/A"


url = "https://forums.redflagdeals.com/"
response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
response.raise_for_status()
soup = BeautifulSoup(response.content, "html.parser")
# I create arrays with which I will create my objects for use later
base_url = "https://forums.redflagdeals.com/"
store_list = []
url_list = []
item_list = []
votes_list = []
username_list = []
timestamp_list = []
category_list = []
replies_list = []
views_list = []
for listing1 in soup.find_all("li", class_="row topic"):
    store = get_store(listing1)
    store_list.append(store)

    item_element = listing1.select_one('.topic_title_link')
    item = item_element.text.strip() if item_element else "N/A"
    item_list.append(item)

    votes_element = listing1.select_one('.total_count_selector')
    votes = votes_element.text.strip() if votes_element else "N/A"
    votes_list.append(votes)

    username_element = listing1.select_one('.thread_meta_author')
    username = username_element.text.strip() if username_element else "N/A"
    username_list.append(username)

    timestamp_element = listing1.select_one('.first-post-time')
    timestamp = timestamp_element.text.strip() if timestamp_element else "N/A"
    timestamp_list.append(timestamp)

    category_element = listing1.select_one('.thread_category a')
    category = category_element.text.strip() if category_element else "N/A"
    category_list.append(category)

    replies_element = listing1.select_one('.posts')
    replies = replies_element.text.strip() if replies_element else "N/A"
    replies_list.append(replies)

    views_element = listing1.select_one('.views')
    views = views_element.text.strip() if views_element else "N/A"
    views_list.append(views)

    url_element = item_element['href'] if item_element else "N/A"
    url = base_url + url_element
    url_list.append(url)

Hot_deals = []
for x in (range(len(url_list))):
    Hot_deals.append(
        LatestDeals(store_list[x], item_list[x], votes_list[x], username_list[x], timestamp_list[x], category_list[x],
                    replies_list[x], views_list[x], url_list[x]))
condition = 1
while condition == 1:
    print("***** Web Scraping Adventure *****\n1.Display Latest Deals\n2.Analyze Deals by Category\n3.Find Top "
          "Stores\n4.Log Deal Information\n5.Exit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        print("Total deals found: \n", len(Hot_deals))
        for x in (range(len(Hot_deals))):
            Hot_deals[x].print_info()
    elif choice == 2:
        print("Deals by Category: \n")
        counter = 0
        category_dict = {}
        for j in (range(len(category_list))):
            for i in (range(len(category_list))):
                if category_list[i] == category_list[j]:
                    counter += 1
            category_dict[category_list[j]] = counter
        sorted_category_list = sorted(category_dict.items(), key=lambda y: y[1], reverse=True)
        sorted_category_dict = dict(sorted_category_list)
        for key in sorted_category_dict:
            print(key, ": ", sorted_category_dict[key], "deals")
    elif choice == 3:
        choice2 = int(input("Enter the number of top stores to display: "))
        top_stores_dict = {}
        counter1 = 0
        for j in (range(len(store_list))):
            for i in (range(len(store_list))):
                if store_list[j] == store_list[i]:
                    counter1 += 1
            top_stores_dict[store_list[j]] = counter1
        sorted_stores_list = sorted(top_stores_dict.items(), key=lambda y: y[1], reverse=True)
        sorted_stores_dict = dict(sorted_stores_list)
        counter2 = 1
        for key in sorted_stores_dict:
            if counter2 <= choice2:
                print(key, ": ", sorted_stores_dict[key], "deals")
            counter2 += 1
    elif choice == 4:
        category_set = set(category_list)
        category_list_unrepeated = list(category_set)
        for x in (range(len(category_list_unrepeated))):
            print((x + 1), category_list_unrepeated[x])
        print("******************************************")
        choice1 = int(input("Enter your choice : "))

        log_txt_file = open("log.txt", "w")
        log_deals_list = []
        for x in (range(len(Hot_deals))):
            if category_list_unrepeated[choice1 - 1] == Hot_deals[x].getcategory():
                log_deals_list.append(Hot_deals[x])

        log_txt_file.close()
        log_txt_file = open("log.txt", "a")
        for x in (range(len(log_deals_list))):
            if log_deals_list[x].print_info_file() is not None:
                log_txt_file.write(log_deals_list[x].print_info_file())
        log_txt_file.close()
    elif choice == 5:
        condition = 0
