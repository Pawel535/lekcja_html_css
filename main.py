from flask import Flask
import random

app = Flask(__name__)

facts_list = [
    "Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń.",
    "Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów.",
    "Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych.",
    "Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy.",
    "Jednym ze sposobów walki z uzależnieniem od technologii jest poszukiwanie zajęć, które sprawiają przyjemność i poprawiają nastrój.",
    "Elon Musk twierdzi, że sieci społecznościowe są zaprojektowane tak, aby trzymać nas na platformie, abyśmy spędzali jak najwięcej czasu na przeglądaniu treści.",
    "Elon Musk opowiada się także za regulacją sieci społecznościowych i ochroną danych osobowych użytkowników.",
    "Twierdzi, że sieci społecznościowe gromadzą o nas ogromną ilość informacji, które następnie można wykorzystać do manipulowania naszymi myślami i zachowaniami.",
    "Sieci społecznościowe mają swoje zalety i wady, a korzystając z tych platform, powinniśmy być ich świadomi."
]

@app.route("/")
def hello_world():
    return (
        "<p>Witaj w aplikacji! Kliknij napis poniżej, aby zobaczyć losowy fakt.</p>"
        "<a href='/random_fact'>Kliknij tutaj!</a><br>"
        "<a href='/coin_flip'>Rzut monetą</a>"
    )

@app.route("/random_fact")
def random_fact():
    fact = random.choice(facts_list)
    return (
        f'<p>{fact}</p>'
        '<a href="/">Wróć do strony głównej</a>'
        '<br>'
        '<a href="/random_fact">Kolejny fakt</a>'
    )

@app.route("/coin_flip")
def coin_flip():
    result = random.choice(["Orzeł", "Reszka"])
    return (
        f'<p>Wynik rzutu monetą: {result}</p>'
        '<a href="/">Wróć do strony głównej</a>'
    )

if __name__ == "__main__":
    app.run(debug=True)
