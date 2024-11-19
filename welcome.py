
import csv
from speak import speak



def print_csv_text(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            speak(row)


print_csv_text('welcome.csv')



