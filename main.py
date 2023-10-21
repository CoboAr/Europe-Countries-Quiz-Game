import turtle
import pandas
# Screen setup
screen = turtle.Screen()
screen.setup(width=960, height=950)
screen.title("Europe Guess Countries Game")
image = "Europe_blank_map.gif"
screen.addshape(image)
turtle.shape(image)
# Read data from 49_European_Countries.csv file
data = pandas.read_csv("49_European_Countries.csv")
all_countries = data.country.to_list()
guessed_countries = []

while len(guessed_countries) < 49:
    answer_country = screen.textinput(title=f"{len(guessed_countries)}/49 Countries Correct",
                                    prompt="What's another country's name?").title()
    if answer_country == "Exit":
        missing_countries = []
        for country in all_countries:
            if country not in guessed_countries:
                missing_countries.append(country)
        # Create a new csv file containing all the countries that the player wasn't able to guess during the game
        new_data = pandas.DataFrame(missing_countries)
        new_data.to_csv("countries_to_learn.csv")
        break
    # draw countries names accordingly
    if answer_country in all_countries:
        guessed_countries.append(answer_country)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_data = data[data.country == answer_country]
        t.goto(int(country_data.x), int(country_data.y))
        t.write(answer_country)

