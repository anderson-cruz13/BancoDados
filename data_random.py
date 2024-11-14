from datetime import datetime, timedelta
from files import Files
import random


def random_date(start=1980, end=datetime.now().year):
    start = datetime(start, 1, 1)
    end = datetime(end, 12, 31)
    random_days = random.randint(0, (end - start).days)
    return (start + timedelta(days=random_days)).strftime("%d/%m/%Y")


if __name__ == "__main__":
    users = []

    for i in range(1, 101):
        user_name = f"Usuário {i}"
        birth_date = random_date()
        users.append([user_name, birth_date])

    f = Files()
    for user in users:
        f.write("users.txt", f"{user[0]},{user[1]}\n")
