from flask import Flask, jsonify, request

app = Flask(__name__)

# Data
tasks = [
    {"id": 1, "title": "Tugas 1", "description": "Membangun website Sistem Informasi"},
    {"id": 2, "title": "Tugas 2", "description": "Membangun aplikasi mobile untuk absesi karyawan"},
    {"id": 3, "title": "Tugas 3", "description": "Membangun model python untuk mendeteksi penyakit"},
    {"id": 4, "title": "Tugas 4", "description": "Melakukan testing terhadapat aplikasi yang dibangun"},
    {"id": 5, "title": "Tugas 5", "description": "Mengumpulkan dataset untuk kebutuhan sistem"}
]

# Endpoint untuk membuat tugas baru
@app.route('/baru', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data['title']
    description = data['description']
    new_task = {"id": len(tasks) + 1, "title": title, "description": description}
    tasks.append(new_task)
    return jsonify(new_task), 201

# Endpoint untuk mengambil daftar semua tugas
@app.route('/daftar', methods=['GET'])
def get_all_tasks():
    return jsonify(tasks)

# Endpoint untuk mengambil detail tugas berdasarkan ID
@app.route('/detail/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"message": "Tugas tidak ditemukan"}), 404

# Endpoint untuk mengubah tugas berdasarkan ID
@app.route('/ubah/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        data = request.get_json()
        task['title'] = data.get('title', task['title'])
        task['description'] = data.get('description', task['description'])
        return jsonify(task)
    return jsonify({"message": "Tugas tidak ditemukan"}), 404

# Endpoint untuk menghapus tugas berdasarkan ID
@app.route('/hapus/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        tasks.remove(task)
        return jsonify({"message": "Tugas berhasil dihapus"})
    return jsonify({"message": "Tugas tidak ditemukan"}), 404

if __name__ == '__main__':
    app.run()