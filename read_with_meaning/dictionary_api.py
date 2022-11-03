import requests

def get_meaning(word):
    from read_with_meaning import dict_api
    meanings = []
    error = None
    if len(word) == 0:
        error = "Invalid input word"
        return meanings, error

    response = requests.get(f"{dict_api}/{word}")
    if response is None or len(response.text) == 0:
        error = "Invalid resposne"
        return meanings, error

    response = response.json()
    if isinstance(response, dict):
        return meanings, response['title']
    
    for word in response:
        word_meanings = word['meanings']
        meanings = [
            {
            'POS': row['partOfSpeech'], 'meaning': row['definitions'][0]['definition']
            } for row in word_meanings
        ]

    return meanings, error