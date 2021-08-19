import random


def get_jokes(quality, repeat_words):
    '''
    This function generates the specified number of jokes
    :param quality: Number of jokes
    :param repeat_words: Type: Boolean. If TRUE words in jokes can repeat, else they can not repeat
    :return:List with jokes
    '''

    jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    while quality != 0:
        noun_number = random.randint(0, len(nouns) - 1)
        adverb_number = random.randint(0, len(adverbs) - 1)
        adjective_number = random.randint(0, len(adjectives) - 1)
        if repeat_words:
            joke = f'{nouns[noun_number]} {adverbs[adverb_number]} {adjectives[adjective_number]}'
            jokes.append(joke)
        else:
            joke = f'{nouns[noun_number]} {adverbs[adverb_number]} {adjectives[adjective_number]}'
            nouns.pop(noun_number)
            adverbs.pop(adverb_number)
            adjectives.pop(adjective_number)
            jokes.append(joke)
        quality -= 1
    return jokes


x = get_jokes(3, False)
print(x)

get_jokes(2, True)
