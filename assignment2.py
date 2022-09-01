import datetime
import requests


def downloadData(url):
    """
    Reads data from a URL and returns the data as a string

    :param url:
    :return:
    """
    # read the URL
    response = requests.get(url)
    # return the data
    return response.text


def processData(data):
    """
    Parses data and return a dictionary with id: (name, birthday)

    :param data:
    :return:
    """
    result = {}
    # processing here ...
    lines = data.split("\n")
    for line in lines:
        # process each line
        elements = line.split(",")
        # id =
        # name =
        # date_str =

        # result[id] = (name, birthday)
    return result


def displayPerson(id, personData):
    # search for id in persondData and do something about it
    pass


if __name__ == "__main__":
    url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'
    # Do something
    data = downloadData(url)
    personData = processData(data)
    # ask use for ID
    id = 33
    displayPerson(id, personData)



