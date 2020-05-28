# HINT: modify the headlines list to verify your loop works with different inputs
headlines_list = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
j = 0

for headline in headlines_list:
    len_news_ticker = len(news_ticker)
    if len_news_ticker > 140:
        break
    elif len_news_ticker + len(headline) > 140:
        while(len(news_ticker)) < 140:
            news_ticker += headline[j]
            j += 1
        continue
    else:
        news_ticker += headline + " "


print("\nNews Ticker is: {}".format(news_ticker))
