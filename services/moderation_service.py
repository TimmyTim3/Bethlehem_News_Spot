BAD_WORDS = {

"word1",

"word2",

"word3",

}


def contains_profanity(text):

    text=text.lower()

    for word in BAD_WORDS:

        if word in text:

            return True

    return False

SPAM_PHRASES = [

"buy now",

"free money",

"click here",

"http://",

"https://",

]


def is_spam(text):

    text=text.lower()

    for phrase in SPAM_PHRASES:

        if phrase in text:

            return True

    return False
