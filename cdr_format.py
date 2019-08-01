from datetime import datetime, timedelta


cdr_first_part = "icdr.5_9_0A.0.1."
date_input = str(input("Type date in YYYYMMDD Format:\n"))


def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

dts = [dt.strftime('%Y-%m-%d %H:%M') for dt in 
       datetime_range(datetime(2019, 7, 25, 0), datetime(2019, 07, 26, 0), 
       timedelta(minutes=5))]
cdr_last_part = 864206 
for i in range(len(dts)):
    time_split = dts[i].split()
    time_split2 = time_split[1].split(":")

    cdr_format_time = cdr_first_part + date_input + time_split2[0] + time_split2[1] + "." + str(cdr_last_part + i) + "." + str(0)

    print(cdr_format_time)
