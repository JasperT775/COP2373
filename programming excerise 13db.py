import sqlite3
import turtle

# Create a database and table
def create_database():
    conn = sqlite3.connect('population_YI.db')  # Replace 'YI' with your initials
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Insert initial data for 10 cities in Florida for the year 2023
def insert_initial_data():
    cities = [
        ('Miami', 2023, 470000),
        ('Tampa', 2023, 400000),
        ('Orlando', 2023, 280000),
        ('Jacksonville', 2023, 950000),
        ('Tallahassee', 2023, 195000),
        ('Fort Lauderdale', 2023, 180000),
        ('St. Petersburg', 2023, 270000),
        ('Hialeah', 2023, 230000),
        ('Gainesville', 2023, 140000),
        ('Sarasota', 2023, 57000)
    ]

    conn = sqlite3.connect('population_YI.db')
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO population VALUES (?, ?, ?)', cities)
    conn.commit()
    conn.close()

# Simulate population growth for the next 20 years at a 2% growth rate
def simulate_population_growth():
    conn = sqlite3.connect('population_YI.db')
    cursor = conn.cursor()

    cursor.execute('SELECT city, population FROM population WHERE year = 2023')
    initial_data = cursor.fetchall()

    for city, population in initial_data:
        for year in range(2024, 2044):
            population = int(population * 1.02)  # 2% growth rate
            cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, year, population))

    conn.commit()
    conn.close()

# Visualize population growth for a chosen city using turtle
def visualize_population_growth():
    conn = sqlite3.connect('population_YI.db')
    cursor = conn.cursor()

    # List of cities for user to choose from
    cities = [
        'Miami', 'Tampa', 'Orlando', 'Jacksonville', 'Tallahassee',
        'Fort Lauderdale', 'St. Petersburg', 'Hialeah', 'Gainesville', 'Sarasota'
    ]
    print("Choose a city from the following list to visualize its population growth:")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

    choice = int(input("Enter the number corresponding to your choice: ")) - 1
    chosen_city = cities[choice]

    cursor.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (chosen_city,))
    data = cursor.fetchall()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    conn.close()

    # Setting up turtle graphics
    screen = turtle.Screen()
    screen.title(f"Population Growth of {chosen_city}")
    
    max_population = max(populations)
    max_year = max(years)
    
    screen.setworldcoordinates(2023, 0, max_year, max_population)

    pen = turtle.Turtle()
    pen.penup()
    pen.goto(years[0], populations[0])
    pen.pendown()

    for year, population in zip(years, populations):
        pen.goto(year, population)

    pen.hideturtle()
    screen.mainloop()

# Main function to execute the workflow
def main():
    create_database()
    insert_initial_data()
    simulate_population_growth()
    visualize_population_growth()

if __name__ == "__main__":
    main()
