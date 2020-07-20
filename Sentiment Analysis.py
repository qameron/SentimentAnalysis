

def get_neg(x):
    x = strip_punctuation(x)
    x = x.lower()
    negative = 0
    split = x.split()

    for word in split:
        if word in negative_words:
            negative += 1
    return negative


def strip_punctuation(string):
    for ch in string:
        if ch in punctuation_chars:
            string = string.replace(ch, "")
    return string


def get_pos(x):
    x = strip_punctuation(x)
    x = x.lower()
    positive = 0
    split = x.split()

    for word in split:
        if word in positive_words:
            positive += 1
    return positive


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("C:\\Users\\User\\PycharmProjects\\SentimentAnalysis\\positive-words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("C:\\Users\\User\\PycharmProjects\\SentimentAnalysis\\negative-words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
# -----------------------------------------------------------------

twitterdata = open('project_twitter_data.csv', 'r')
twitterdatalines = twitterdata.readlines()

twitter_sentiment = open("resulting_data.csv", "w")
twitter_sentiment.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
twitter_sentiment.write('\n')
for line in twitterdatalines[1:]:
    split = line.split(",")
    Number_of_Retweets = split[-2]
    Number_of_Retweets = Number_of_Retweets.replace("'", "")
    Number_of_Replies = split[-1].strip()
    Number_of_Replies = Number_of_Replies.replace("\n", "")
    Number_of_Replies = Number_of_Replies.replace("'", "")
    Number_of_Replies = Number_of_Replies[:-2]
    Positive_score = get_pos(line)
    Negative_score = get_neg(line)
    Net_score = get_pos(line) - get_neg(line)
    row_string = '{}, {}, {}, {}, {}'.format(Number_of_Retweets, Number_of_Replies, Positive_score, Negative_score,
                                             Net_score)
    twitter_sentiment.write(row_string)
    twitter_sentiment.write('\n')
twitter_sentiment.close()
twitterdata.close()







