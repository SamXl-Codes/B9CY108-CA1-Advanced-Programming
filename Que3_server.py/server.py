# Samuel Ogunlusi - B9CY108
# DBS Admission Server
# TCP server for handling student applications

import socket
import sqlite3
import json
import datetime
import random

def setup_database():
    """Set up the database"""
    conn = None
    try:
        conn = sqlite3.connect('dbs_admissions.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS applicants (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                registration_number TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                educational_qualifications TEXT NOT NULL,
                course TEXT NOT NULL,
                start_year INTEGER NOT NULL,
                start_month TEXT NOT NULL,
                application_date TEXT NOT NULL
            )
        ''')
        conn.commit()
        
        cursor.execute('SELECT COUNT(*) FROM applicants')
        count = cursor.fetchone()[0]
        print("Database initialized: " + str(count) + " records")
        return conn
        
    except Exception as e:
        print("Database error: " + str(e))
        if conn:
            conn.close()
        return None

def save_application(conn, data):
    """Save application to database - uses parameterized queries for security"""
    cursor = None
    try:
        cursor = conn.cursor()
        
        # Create random registration number
        reg_num = "20" + str(random.randint(100000, 999999))
        
        # Using ? placeholders to prevent SQL injection
        cursor.execute('''INSERT INTO applicants (registration_number, name, address, 
                         educational_qualifications, course, start_year, start_month, application_date) 
                         VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                      (reg_num, data['name'], data['address'], data['educational_qualifications'],
                       data['course'], data['start_year'], data['start_month'], 
                       datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        conn.commit()
        print("Saved: " + data['name'] + " - Reg: " + reg_num)
        return reg_num
        
    except Exception as e:
        print("Save error: " + str(e))
        if conn:
            conn.rollback()
        return None

def handle_client(client_sock, addr, db):
    """Handle each client connection"""
    try:
        client_sock.settimeout(300)  # 5 minute timeout
        
        # Send handshake
        handshake = json.dumps({'status': 'connected', 
                               'message': 'Connected to DBS Server'})
        client_sock.send(handshake.encode('utf-8'))
        print("Client connected: " + str(addr))
        
        # Receive data
        data = client_sock.recv(4096).decode('utf-8')
        if not data:
            print("No data received")
            return
            
        # Parse JSON
        try:
            app_data = json.loads(data)
        except:
            error = json.dumps({'status': 'error', 'message': 'Invalid format'})
            client_sock.send(error.encode('utf-8'))
            return
        
        # Validate required fields
        required = ['name', 'address', 'educational_qualifications', 
                   'course', 'start_year', 'start_month']
        for field in required:
            if field not in app_data or not app_data[field]:
                error = json.dumps({'status': 'error', 
                                  'message': 'Missing field: ' + field})
                client_sock.send(error.encode('utf-8'))
                return
        
        # Save to database
        reg_num = save_application(db, app_data)
        
        if reg_num:
            response = json.dumps({'status': 'success', 
                                  'registration_number': reg_num,
                                  'message': 'Application submitted'})
        else:
            response = json.dumps({'status': 'error', 
                                  'registration_number': '',
                                  'message': 'Failed to save'})
        
        client_sock.send(response.encode('utf-8'))
        print("Response sent")
        
    except socket.timeout:
        print("Connection timeout")
    except Exception as e:
        print("Error: " + str(e))
    finally:
        client_sock.close()

def main():
    """Main server function - TCP socket like we learned in lectures"""
    HOST = '127.0.0.1'
    PORT = 5555
    
    print("="*60)
    print("DBS ADMISSION SERVER")
    print("TCP Connection-Oriented Protocol")
    print("SQL Injection Prevention: Parameterized Queries")
    print("="*60)
    
    # Setup database
    db = setup_database()
    if not db:
        print("Failed to initialize database")
        return
    
    # Create TCP socket
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_sock.bind((HOST, PORT))
        server_sock.listen(5)
        print("Server listening on " + HOST + ":" + str(PORT))
        print("="*60 + "\n")
        
        while True:
            print("Waiting for connection...")
            client_sock, addr = server_sock.accept()
            print("*" * 60)
            print("Connected: " + str(addr))
            print("*" * 60)
            handle_client(client_sock, addr, db)
            
    except KeyboardInterrupt:
        print("\nServer stopped")
    except Exception as e:
        print("Server error: " + str(e))
    finally:
        server_sock.close()
        db.close()
        print("Server shutdown complete")

if __name__ == "__main__":
    main()
