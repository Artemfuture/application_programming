import re
import requests
import dns.resolver


def validate_email(email: str) -> bool:
    check = re.compile(r"(?:[a-zA-Z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,})")
    return bool(re.fullmatch(check, email))


def domain_check(domain: str, retries=3, timeout=2) -> bool:
    resolver = dns.resolver.Resolver()
    resolver.timeout = timeout
    resolver.lifetime = timeout

    for i in range(retries):
        try:
            answers = resolver.resolve(domain, "MX")
            return len(answers) > 0
        except Exception:
            continue
    return False


def find_emails_in_text(text: str) -> list[str]:
    check = re.compile(r"(?:[a-zA-Z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,})")
    emails = re.findall(check, text)
    result = []
    for email in emails:
        domain = email.split("@")[1]
        if domain_check(domain):
            result.append(email)
    return result


def find_emails_from_url(url: str) -> list[str]:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.text)
        return find_emails_in_text(response.text)
    except requests.RequestException:
        return None


def find_emails_in_file(filename: str) -> list[str]:
    try:
        with open(filename, encoding="utf-8") as file:
            return find_emails_in_text(file.read())
    except Exception:
        return None


if __name__ == "__main__":
    print("1 — Проверка email")
    print("2 — Поиск email на странице по URL")
    print("3 — Поиск email в файле")

    choice = input("Выберите действие: ")
    match choice:
        case "1":
            email = input("Введите email: ")
            print(
                "Корректный"
                if validate_email(email) and domain_check(email.split("@")[1])
                else "Некорректный"
            )
        case "2":
            url = input("Введите URL: ")
            emails = find_emails_from_url(url)
            print("Найденные email:", emails or "Не найдено")
        case "3":
            filename = input("Введите имя файла: ")
            emails = find_emails_in_file(filename)
            print("Найденные email:", emails or "Не найдено")
        case _:
            pass
