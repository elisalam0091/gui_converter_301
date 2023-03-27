from datetime import date
import re

# if filename is blank, returns default name
# otherwise checks filename and either returns
# an error or returns the filename (with .txt extention)


def filename_maker(filename):

    # creates default filename
    # (YYYY_MM_DD_temperature_calculations)
    if filename == "":

        # set filename_ok to " so we can see the default name for testing purposes
        filename_ok = ""
        date_part = get_date()
        filename = "{}_temperature_calculations".format(date_part)

    # checks filename has only a-z / A-Z / underscores
    else:
        filename_ok = check_filename(filename)

    if filename_ok == "":
        filename += ".txt"

    else:
        filename = filename_ok

    return filename


def get_date():
    today = date.today()

    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%Y")

    return "{}_{}_{}".format(year, month, day)


def check_filename(filename):
    problem = ""

    # regular expression to check filename is valid
    valid_char = "[A-Za-z0-9_]"

    # iterates through filename and checks each letter.
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "Sorry, no spaces allowed"

        else:
            problem = ("Sorry, no {}'s allowed".format(letter))

        break

    if problem != "":
        problem = "{}. Use letters / numbers /" \
                      "underscores only.".format(problem)

    return problem

# **** main routine ****


test_filenames = ["", "Text.txt", "Test It", "test"]

for item in test_filenames:
    checked = filename_maker(item)
    print(checked)
    print()