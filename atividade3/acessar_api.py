import requests

def acessar():
    # Definindo os parâmetros
    sport = "soccer_brazil_campeonato"
    apiKey = "ffa99eb14dmsh9a3955f41042537p1cbe63jsn3a64581bcd8d"
    daysFrom = "3"

    # Construindo a URL
    url = f"https://odds.p.rapidapi.com/v4/sports/{sport}/scores/?apiKey={apiKey}&daysFrom={daysFrom}"

    headers = {
        "X-RapidAPI-Key": apiKey,
        "X-RapidAPI-Host": "odds.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return response.json()

