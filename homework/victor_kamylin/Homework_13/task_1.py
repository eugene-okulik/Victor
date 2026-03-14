import os
import datetime

now = datetime.datetime.now()
base_path = os.path.dirname(__file__)
file_path = os.path.join(
    os.path.dirname(os.path.dirname(base_path)), "eugene_okulik", "hw_13", "data.txt"
)


def read_fale(file):
    with open(file_path, "r", encoding="utf-8") as data:
        for i in data:
            date = i.split(". ", 1)
            date, text = date[1].split(" - ")
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")

            yield date, text


for date, text in read_fale(file_path):
    if (
        "распечатать эту дату, но на неделю позже. "
        "Должно получиться 2023-12-04 20:34:13.212967"
    ) in text:
        print(date + datetime.timedelta(weeks=1))
    elif "распечатать какой это будет день недели" in text:
        print(date.strftime("%A"))
    elif "распечатать сколько дней назад была эта дата" in text:
        different = now - date
        print(f"{different.days} дней назад была эта дата")
