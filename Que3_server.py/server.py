import socket
import sqlite3
import json
import datetime
import random

def setup_database():
    conn = sqlite3.connect('dbs_admissions.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS applicants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        registration_number TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        educational_qualifications TEXT NOT NULL,
        course TEXT NOT NULL,
        start_year INTEGER NOT NULL,
        start_month TEXT NOT NULL,
        application_date TEXT NOT NULL
    )''')
    conn.commit()
    print("Database ready")
    return conn

def save_application(conn, data):
    cursor = conn.cursor()
    reg_num = "20" + str(random.randint(100000, 999999))
    
    cursor.execute('''INSERT INTO applicants (registration_number, name, address, 
                     educational_qualifications, course, start_year, start_month, application_date) 
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (reg_num, data['name'], data['address'], data['educational_qualifications'],
                   data['course'], data['start_year'], data['start_month'], 
                   datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    conn.commit()
    print("Saved: " + data['name'])
    return reg_num

def handle_client(client_sock, addr, db):
    try:
        handshake = json.dumps({'status': 'connected', 'message': 'Connected'})
        client_sock.send(handshake.encode('utf-8'))
        
        data = client_sock.recv(4096).decode('utf-8')
        if not data:
            return
            
        try:
            app_data = json.loads(data)
        except:
            error = json.dumps({'status': 'error', 'message': 'Bad format'})
            client_sock.send(error.encode('utf-8'))
            return
        
        required = ['name', 'address', 'educational_qualifications', 
                   'course', 'start_year', 'start_month']
        for field in required:
            if field not in app_data or not app_data[field]:
                error = json.dumps({'status': 'error', 'message': 'Missing: ' + field})
                client_sock.send(error.encode('utf-8'))
                return
        
        reg_num = save_application(db, app_data)
        
        if reg_num:
            response = json.dumps({'status': 'success', 'registration_number': reg_num,
                                  'message': 'Application saved'})
        else:
            response = json.dumps({'status': 'error', 'registration_number': '',
                                  'message': 'Save failed'})
        
        client_sock.send(response.encode('utf-8'))
        
    except Exception as e:
        print("Error: " + str(e))
    finally:
        client_sock.close()

def main():
    HOST = '127.0.0.1'
    PORT = 5555
    
    print("DBS ADMISSION SERVER - TCP Connection")
    
    db = setup_database()
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_sock.bind((HOST, PORT))
        server_sock.listen(5)
        print("Listening on " + HOST + ":" + str(PORT))
        while True:
            client_sock, addr = server_sock.accept()
            print("Client: " + str(addr))
            handle_client(client_sock, addr, db)
    except KeyboardInterrupt:
        print("\nStopped")
    finally:
        server_sock.close()
        db.close()

if __name__ == "__main__":
    main()
