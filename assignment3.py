import datetime
import argparse
import urllib.request
import csv
import io
import re


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


def process_url(data):
    """
    Magic happens here

    :return:
    """
    image_hits = 0
    broser_dict = {
        'IE': 0,
        'Safari': 0,
        'Chrome': 0,
        'Firefox': 0
    }
    # you need a file - Convert a string into a file by using io.StringIO(...)
    csv_data = csv.reader(io.StringIO(data))
    for i, row in enumerate(csv_data):
        path_to_file = row[0]
        datetime_accessed = row[1] # parse this using datetime.datetime.strptim(...)
        browser = row[2]

        # check if the path_to_file has an image and count it
        if re.search("gif|jpg", path_to_file.lower()):
            image_hits += 1

        # check browser and update browser dict

        # if i == 5:
        #     break

    avg_hits = image_hits / (i + 1) * 100
    print(f"Image requests account for {avg_hits}% of all requests")
    # Find most popular browser


def main(url):
    data = downloadData(url)
    process_url(data)


if __name__ == "__main__":
    # http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv
    # Create the parser
    my_parser = argparse.ArgumentParser(description='Assignment2 Parser')
    # Add the arguments
    my_parser.add_argument('--url', type=str, required=True, help='The URL we want to download')
    # Execute the parse_args() method
    args = my_parser.parse_args()

    url = args.url
    main(url)
