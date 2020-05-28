# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here

j = 0


for header in headlines:
    len_news_ticker = len(news_ticker)
    print("Current length of news ticker is {} ".format(len(news_ticker)))
    if len_news_ticker > 140:
        print("breaking loop now!")
        break
    elif len_news_ticker + len(header) > 140:
        while(len(news_ticker)) < 140:
            print("Length of news ticker is in While loop {} ".format(len(news_ticker)))
            print("Current character being added {} ".format(header[j]))
            news_ticker += header[j]
            j += 1
        continue
    else:
        print("  adding {}".format(header))
        news_ticker += header + " "


print("\nNews Ticker is: {}".format(news_ticker))
