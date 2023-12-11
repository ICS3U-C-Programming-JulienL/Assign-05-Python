#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: December 6, 2023
# This program display an equation of a line or the volume of a square pyramid


def calc_slope(x1, x2, y1, y2):
    # return (y2-y1)/(x2-x1)
    return (y2 - y1) / (x2 - x1)


def calc_y_int(x1, y1, slope):
    # return y1-(slope*x1)
    return y1 - (slope * x1)


def main_equation_of_a_line():
    # get all the x and y points
    print("This programs shows the equation of a line given 2 points on a graph.")
    x_point1_str = input("Enter your first x point.")
    y_point1_str = input("Enter your first y point.")
    x_point2_str = input("Enter your second x point.")
    y_point2_str = input("Enter your second y point.")

    try:
        # convert x1 to a float
        x_point1_float = float(x_point1_str)

        try:
            # convert y1 to a float
            y_point1_float = float(y_point1_str)

            try:
                # convert x2 to a float
                x_point2_float = float(x_point2_str)

                try:
                    # convert y2 to a float
                    y_point2_float = float(y_point2_str)

                    # call the calc_slope function
                    slope = calc_slope(
                        x_point1_float, x_point2_float, y_point1_float, y_point2_float
                    )

                    # call the calc_y_int function
                    y_int = calc_y_int(x_point1_float, y_point1_float, slope)

                    # if the y-int is negative, display the equation of a line with it being subtracted
                    if y_int < 0:
                        print(
                            "The equation of your line is y = {}x-{}".format(
                                slope, y_int
                            )
                        )
                    elif y_int > 0:
                        # otherwise if the y-int is positive, display the equation of a line with it being added
                        print(
                            "The equation of your line is y = {}x+{}".format(
                                slope, y_int
                            )
                        )
                    elif y_int == 0:
                        # otherwise if the y-int is positive, display the equation of a line without the y-int
                        print(
                            "The equation of your line is y = {}x".format(slope, y_int)
                        )

                except:
                    # if y2 cannot become a float, tell the user to enter one
                    print(
                        "{} is not a valid floating decimal number, please enter one".format(
                            y_point2_str
                        )
                    )
            except:
                # if x2 cannot become a float, tell the user to enter one
                print(
                    "{} is not a valid floating decimal number, please enter one".format(
                        x_point2_str
                    )
                )
        except:
            # if y1 cannot become a float, tell the user to enter one
            print(
                "{} is not a valid floating decimal number, please enter one".format(
                    y_point1_str
                )
            )
    except:
        # if x1 cannot become a float, tell the user to enter one
        print(
            "{} is not a valid floating decimal number, please enter one".format(
                x_point1_str
            )
        )


def calc_volume_pyramid(base, height):
    # return (base**2)*(height/3)
    return (base**2) * (height / 3)


def main_volume_square_pyramid():
    # get the base and height
    print(
        "This program displays the volume of a square pyramid given the base edge and the height."
    )
    base_str = input("Enter the base edge: ")
    height_str = input("Enter the height :")

    try:
        # convert the base to a float
        base_float = float(base_str)

        try:
            # convert the height to a float
            height_float = float(height_str)

            # call the calc_volume_pyramid() function
            volume_pyramid = calc_volume_pyramid(base_float, height_float)

            # display the volume of the pyramid
            print("The volume of your square pyramid is {} cm^3".format(volume_pyramid))
        except:
            # if the height cannot become a float, tell the user to enter one
            print(
                "{} is not a valid floating decimal number, please enter one".format(
                    height_str
                )
            )
    except:
        # if the base cannot become a float, tell the user to enter one
        print(
            "{} is not a valid floating decimal number, please enter one".format(
                base_str
            )
        )


def main():
    # get user choice
    user_choice = input(
        "This program writes the equation of a line from two points on a graph (press 1 for this option), or displays the volume of a pyramid with a square base given the base and height (press 2 for this option). "
    )
    # if user choice is 1, then call the main_equation_of_a_line function
    if user_choice == "1":
        main_equation_of_a_line()
    elif user_choice == "2":
        # otherwise, if user choice is 2, then call the main_volume_square_pyramid()
        main_volume_square_pyramid()
    else:
        # otherwise, tell the user to enter 1 or 2
        print("Please enter 1 or 2 for your selection.")


if __name__ == "__main__":
    main()
