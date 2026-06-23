import os
import csv
from flask import Flask, jsonify, request

app = Flask(__name__)
CSV_FILE = 'students.csv'
FIELDS = ['id', 'first_name', 'last_name', 'age']

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()

def read_students():
    students = []
    if not os.path.exists(CSV_FILE):
        return students
    with open(CSV_FILE, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['age'] = int(row['age'])
            students.append(row)
    return students

def write_students(students):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for s in students:
            writer.writerow(s)

@app.route('/students', methods=['GET'])
def get_students():
    students = read_students()
    last_name_query = request.args.get('last_name')
    if last_name_query:
        filtered = [s for s in students if s['last_name'].lower() == last_name_query.lower()]
        if not filtered:
            return jsonify({"error": f"Студент з ім'ям '{last_name_query}' не знайдений"}), 404
        return jsonify(filtered), 200
    return jsonify(students), 200

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    students = read_students()
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"error": f"Студент з ID {student_id} не знайдений"}), 404
    return jsonify(student), 200

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json() or {}
    if not data:
        return jsonify({"error": "Тіло запиту не може бути порожнім"}), 400
    if any(k not in FIELDS for k in data.keys()):
        return jsonify({"error": "Запит містить невалідні поля"}), 400
    required = ['first_name', 'last_name', 'age']
    if not all(k in data for k in required):
        return jsonify({"error": "Відсутні обов'язкові поля"}), 400

    students = read_students()
    next_id = max([s['id'] for s in students], default=0) + 1
    new_student = {'id': next_id, 'first_name': data['first_name'], 'last_name': data['last_name'], 'age': int(data['age'])}
    students.append(new_student)
    write_students(students)
    return jsonify(new_student), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student_put(student_id):
    data = request.get_json() or {}
    if not data:
        return jsonify({"error": "Тіло запиту не може бути порожнім"}), 400
    if any(k not in FIELDS or k == 'id' for k in data.keys()):
        return jsonify({"error": "Invalid fields"}), 400
    required = ['first_name', 'last_name', 'age']
    if not all(k in data for k in required):
        return jsonify({"error": "Метод PUT вимагає наявності всіх полів"}), 400

    students = read_students()
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"error": "Not found"}), 404

    student['first_name'] = data['first_name']
    student['last_name'] = data['last_name']
    student['age'] = int(data['age'])
    write_students(students)
    return jsonify(student), 200

@app.route('/students/<int:student_id>', methods=['PATCH'])
def update_student_patch(student_id):
    data = request.get_json() or {}
    if not data:
        return jsonify({"error": "Empty body"}), 400
    if any(k != 'age' for k in data.keys()):
        return jsonify({"error": "PATCH приймає лише поле 'age'"}), 400

    students = read_students()
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"error": "Not found"}), 404

    student['age'] = int(data['age'])
    write_students(students)
    return jsonify(student), 200

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    students = read_students()
    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({"error": "Not found"}), 404

    students = [s for s in students if s['id'] != student_id]
    write_students(students)
    return jsonify({"message": "Видалення успішне"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
