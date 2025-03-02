def add_time(start, duration, weekday=None):
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


    g = start.split()
    a = [int(x) for x in g[0].split(":")]
    period = g[1]

    h = [int(x) for x in duration.split(":")]


    is_pm = period == "PM"
    start_minutes = (a[0] % 12) * 60 + a[1]
    if is_pm:
        start_minutes += 12 * 60


    duration_minutes = h[0] * 60 + h[1]


    new_total_minutes = start_minutes + duration_minutes


    total_days = new_total_minutes // (24 * 60)


    new_minutes = new_total_minutes % (24 * 60)
    new_period = "AM" if new_minutes < 12 * 60 else "PM"


    new_hour = (new_minutes // 60) % 12
    new_hour = 12 if new_hour == 0 else new_hour  # Convert 0 to 12
    new_minute = new_minutes % 60


    if weekday:
        weekday = weekday.capitalize()
        new_weekday = week[(week.index(weekday) + total_days) % 7]
    else:
        new_weekday = None


    result = f"{new_hour}:{new_minute:02d} {new_period}"

    if new_weekday:
        result += f", {new_weekday}"

    if total_days == 1:
        result += " (next day)"
    elif total_days > 1:
        result += f" ({total_days} days later)"

    print(result)



add_time('11:59 PM', '24:05')