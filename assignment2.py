import datetime
import argparse
import urllib.request


def downloadData(url):
    """
    Reads data from a URL and returns the data as a string

    :param url:
    :return:
    """
    # read the URL
    # pip install requests
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response


def processData(data):
    """
    Parses data and return a dictionary with id: (name, birthday)

    :param data:
    :return:
    """
    result = {}
    # processing here ...
    lines = data.split("\n")
    header = True
    for line in lines:
        # process each line
        # Skip the header
        if header:
            header = False
            continue

        # Skip blank lines
        if len(line) == 0:
            continue

        elements = line.split(",")
        id = int(elements[0])
        name = elements[1]
        date_str = elements[2]

        try:
            birthday = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            result[id] = (name, birthday)
        except ValueError as e:
            # add this error line to the logger....
            print(f"Error parsing {line}")

    return result


def displayPerson(id, personData):
    # search for id in persondData and print it nicely
    print(personData[id])


def main(url):
    """
    Main function

    :param url:
    :return:
    """
    # Do something
    data = downloadData(url)
    personData = processData(data)

    # ask user for ID
    id = 33
    displayPerson(id, personData)


if __name__ == "__main__":
    # https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv
    # Create the parser
    my_parser = argparse.ArgumentParser(description='Assignment2 Parser')
    # Add the arguments
    my_parser.add_argument('--url', type=str, required=True, help='The URL we want to download')
    # Execute the parse_args() method
    args = my_parser.parse_args()

    url = args.url
    main(url)
