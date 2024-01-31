import stripe


def days_later(jour):
  if jour == 1:
    return "(next day)"
  elif jour > 1:
    return f"({jour} days later)"
  return ""


def add_time(start, duration, day=False):
  days_of_week = [
      "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
      "Sunday"
  ]
  hours, minutes = start.split(":")
  minutes, AM_PM = minutes.split(" ")
  end_h, end_min = duration.split(":")

  next_day = 0
  hours_in_a_day = 24
  hours_half_day = 12

  hours = int(hours)
  minutes = int(minutes)
  end_h = int(end_h)
  end_min = int(end_min)

  total_min = minutes + end_min
  total_h = hours + end_min

  if (total_min >= 60):
    total_h += int(total_min / 60)
    total_h = int(total_min % 60)

  if end_h or end_min:
    if AM_PM == "PM" and total_h > hours_half_day:
      if int(total_h % hours_half_day) >= 1:
        next_day += 1
      if total_h >= hours_half_day:
        h_restant = total_h / hours_in_a_day
        next_day += int(h_restant)

      temp_hours = total_h
      while True:
        if temp_hours < hours_half_day:
          break
        if AM_PM == "AM":
          AM_PM = "PM"
        else:
          AM_PM = "AM"
        temp_hours -= hours_half_day
  remaining_hours = int(total_h % hours_half_day) or hours + 1
  remaining_mins = int(total_min % 60)
  results = f"{remaining_hours}:{remaining_mins:02} {AM_PM.upper()}"
  if day:
    day = day.strip().lower()
    selected_day = int((days_of_week.index(day) + next_day) % 7)
    current_day = days_of_week[selected_day]
    results += f", {current_day.title()} {days_later(next_day)}"

  else:
    new_time = " ".join((results, days_later(next_day)))

  return new_time.strip()

#---------------------------------------------------------------


#Test
# This entrypoint file to be used in development. Start by reading README.md
# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))


# Run unit tests automatically
main(module='test_module', exit=False)