import requests
import json

URL = "http://127.0.0.1:5000/students"
results_log = []

def log_and_print(step_name, response):
    status = response.status_code
    try:
        content = response.json()
    except:
        content = response.text
    log_line = f"=== STEP: {step_name} ===\nStatus Code: {status}\nResponse:\n{json.dumps(content, indent=4, ensure_ascii=False)}\n\n"
    print(log_line)
    results_log.append(log_line)

def run_tests():
    print("Запуск тестів...\n")
    r = requests.get(URL)
    log_and_print("1. Get all students (Initial)", r)
    
    s1, s2, s3 = {"first_name": "Олег", "last_name": "Петренко", "age": 20}, {"first_name": "Анна", "last_name": "Сидоренко", "age": 22}, {"first_name": "Ігор", "last_name": "Коваленко", "age": 19}
    r1 = requests.post(URL, json=s1); log_and_print("2a. Створено студент 1", r1)
    r2 = requests.post(URL, json=s2); log_and_print("2b. Створено студент 2", r2)
    r3 = requests.post(URL, json=s3); log_and_print("2c. Створено студент 3", r3)
    
    id1 = r1.json().get('id', 1) if r1.status_code == 201 else 1
    id2 = r2.json().get('id', 2) if r2.status_code == 201 else 2
    id3 = r3.json().get('id', 3) if r3.status_code == 201 else 3

    r = requests.get(URL); log_and_print("3. Отримати всіх студентів після створення", r)
    r = requests.patch(f"{URL}/{id2}", json={"age": 23}); log_and_print("4. Оновити вік Студента 2 на 23", r)
    r = requests.get(f"{URL}/{id2}"); log_and_print("5. Отримати дані студент 2", r)
    
    updated_s3 = {"first_name": "Василь", "last_name": "Шевченко", "age": 25}
    r = requests.put(f"{URL}/{id3}", json=updated_s3); log_and_print("6. Повне оновлення Студента 3 через PUT", r)
    r = requests.get(f"{URL}/{id3}"); log_and_print("7. Отримання даних Студента 3", r)
    r = requests.get(URL); log_and_print("8. Отримання всіх студентів перед видаленням", r)
    r = requests.delete(f"{URL}/{id1}"); log_and_print("9. Видалення Студента 1", r)
    r = requests.get(URL); log_and_print("10. Отримання всіх студентів (Фінал)", r)

    with open("results.txt", "w", encoding="utf-8") as f:
        f.writelines(results_log)
    print("Готово! Результати збережено в results.txt")

if __name__ == '__main__':
    run_tests()
