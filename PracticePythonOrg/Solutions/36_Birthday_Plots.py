from bokeh.plotting import figure, show, output_file
import json
from collections import Counter
import math

def main():
    output_file('/Users/amitshetty/Desktop/36_output.html')
    month_dictionary = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }

    month_categories = month_dictionary.values()

    with open('/Users/amitshetty/Desktop/scientist_birthdays.json') as read_file:
        cnt = Counter()
        birthday_dict_json = json.load(read_file)
        for k, v in birthday_dict_json.items():
            # Month is the first element here. US style
            cnt[month_dictionary.get(v.split('/')[0])]+=1
        print("Count Dictionary :{}".format(cnt))
        count_dict = dict(cnt)
        # Plotting Bar grahs
        birth_range = list(month_categories)
        birth_axis = list(count_dict.keys())
        count_axis = list(count_dict.values())
        # x_rnage is important otherwise it doesn't show the graph
        p = figure(x_range=birth_range)
        p.vbar(x=birth_axis, top=count_axis, width=1.0)
        p.xaxis.major_label_orientation = math.pi/2
        show(p)

if __name__ == "__main__":
    main()
