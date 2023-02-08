# Creators: Edwin and Joshua
# Date: February 7, 2023,
# Description:
#       This is a simple Python program designed to allow users calculate the distance between two planets

# Github: https://github.com/JMorenoAI/Planet_Calculator_Group_Assignment/blob/main/PlanetCalculatorCode.py


DASH_LENGTH = 60  # Just codes to make the program look more appealing

# Hard coded tuple to store data of planets' distance from the Sun

planets = (
    ('Mercury', 57),
    ('Venus', 108),
    ('Earth', 150),
    ('Mars', 228),
    ('Jupiter', 779),
    ('Saturn', 1430),
    ('Uranus', 2880),
    ('Neptune', 4500)

)


def get_integer_input(message, min_num=0, max_num=0):
    while True:
        try:
            user_input = int(input(message))

            if min == 0 and max == 0:
                return user_input
            elif min_num <= user_input <= max_num:
                return user_input
            else:
                print(f"\t Invalid Input: Please enter a number between {min_num} and {max_num}.")
                continue

        except ValueError:
            print("\tInvalid Input: Please enter a number.")
            continue


def display_abs_distance(planet1_num=0, planet2_num=0):
    planet1_info = planets[planet1_num - 1]
    planet1_name, planet1_dist = planet1_info

    planet2_info = planets[planet2_num - 1]
    planet2_name, planet2_dist = planet2_info

    planet_dist = abs(planet2_dist - planet1_dist)
    print(f"\n{planet1_name} and {planet2_name} are on average {planet_dist} million miles apart\n")


# The menu that users see on screen that they can enter planets to calculate the distance between them.
def display_planets_menu():
    numbers = 0

    print("=" * DASH_LENGTH)
    print("Planet's Average Distance From Sun")
    print("=" * DASH_LENGTH)

    # displays the planets and the distance from each plant to the sun
    for planet, distance in planets:
        numbers += 1
        print(f"#{numbers} {planet:<9} ={distance:>6} million miles")

    print("=" * DASH_LENGTH)
    print("To calculate the distance between two planets")
    print("Enter two planet numbers or 0 to quit: ")
    print("-" * DASH_LENGTH)


# start of the running program
def main():
    display_planets_menu()

    while True:
        # This gets what planets the user want to calculate
        planet1 = get_integer_input(message="Please enter the first planet number #", min_num=0, max_num=len(planets))
        if planet1 == 0:
            break

        while True:
            planet2 = get_integer_input(message="Please enter the second planet number #",
                                        min_num=0, max_num=len(planets))
            if planet2 == planet1:
                print("      Invalid Input: The same planet was entered twice")  # prompt the users to enter a valid #
                continue
            else:
                break

        if planet2 == 0:
            break

        # Displays the and sees if the tuple unpacker would work
        display_abs_distance(planet1, planet2)

        input("Please press enter to continue...")  # pause to display the next prompt

        print("-" * DASH_LENGTH)
        print("Enter two planet numbers or 0 to quit: ")
        print("-" * DASH_LENGTH)


if __name__ == "__main__":
    main()

    # Final goodbye message before the end
    print("=" * DASH_LENGTH)
    print("Live Long and Prosper")
    print("=" * DASH_LENGTH)
