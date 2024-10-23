from datetime import datetime

data = "30/09/2024"

def check_date(data):
    date_format = "%d/%m/%Y"
    try:
        new_date = datetime.strptime(data, date_format)
        return True
    except ValueError:
        return False