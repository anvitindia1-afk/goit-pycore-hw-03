# Завдання 4: кого з колег вітати з днем народження в найближчі 7 днів.

from datetime import datetime, timedelta


def get_birthday_in_year(birthday, year):
    """
    Повертає день народження в заданому році.
    Якщо людина народилася 29 лютого, а рік не високосний
    (такого дня немає), святкуємо 1 березня.
    """
    try:
        return birthday.replace(year=year)
    except ValueError:
        return birthday.replace(year=year, month=3, day=1)


def get_upcoming_birthdays(users):
    """
    users — список словників виду {"name": "...", "birthday": "РРРР.ММ.ДД"}.
    Повертає список словників {"name": "...", "congratulation_date": "РРРР.ММ.ДД"}
    для тих, у кого день народження від сьогодні до +7 днів.
    Якщо день народження в суботу чи неділю, вітаємо в понеділок.
    """
    today = datetime.today().date()
    upcoming = []

    for user in users:
        # Перетворюємо рядок на дату
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # День народження в цьому році: той самий місяць і день, але поточний рік
        birthday_this_year = get_birthday_in_year(birthday, today.year)

        # Якщо в цьому році вже минув — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = get_birthday_in_year(birthday, today.year + 1)

        # Скільки днів лишилося до дня народження
        days_left = (birthday_this_year - today).days

        # Беремо лише тих, у кого від 0 до 7 днів
        if 0 <= days_left <= 7:
            congratulation_date = birthday_this_year

            # weekday(): 0 = понеділок ... 5 = субота, 6 = неділя
            if congratulation_date.weekday() == 5:      # субота
                congratulation_date = congratulation_date + timedelta(days=2)
            elif congratulation_date.weekday() == 6:    # неділя
                congratulation_date = congratulation_date + timedelta(days=1)

            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Leap Person", "birthday": "2000.02.29"},  # 29 лютого
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
