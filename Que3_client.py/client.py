# Samuel Ogunlusi - B9CY108
# DBS Admission Client
# Connects to the server to submit applications

import socket
import json

def get_application_data():
    """Get all the application info from user"""
    print("\n" + "-"*60)
    print("APPLICATION FORM")
    print("-"*60)
    
    # Get name
    while True:
        name = input("\nFull Name: ").strip()
        if name:
            break
        print("Name cannot be empty")
    
    # Get address
    while True:
        address = input("Address: ").strip()
        if address:
            break
        print("Address cannot be empty")
    
    # Get qualifications
    while True:
        quals = input("Educational Qualifications: ").strip()
        if quals:
            break
        print("Qualifications cannot be empty")
    
    # Select course
    print("\nAvailable Courses:")
    print("1. MSc in Cyber Security")
    print("2. MSc Information Systems & computing")
    print("3. MSc Data Analytics")
    
    courses = {'1': 'MSc in Cyber Security', 
               '2': 'MSc Information Systems & computing', 
               '3': 'MSc Data Analytics'}
    
    while True:
        choice = input("Select course (1-3): ").strip()
        if choice in courses:
            course = courses[choice]
            break
        print("Invalid selection")
    
    # Get year
    while True:
        try:
            year = int(input("Start Year (2024-2030): ").strip())
            if 2024 <= year <= 2030:
                break
            print("Year must be between 2024 and 2030")
        except:
            print("Invalid year")
    
    # Get month
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    
    print("\nMonths:")
    for i in range(len(months)):
        print(str(i + 1) + ". " + months[i])
    
    while True:
        try:
            m = int(input("Select month (1-12): ").strip())
            if 1 <= m <= 12:
                month = months[m - 1]
                break
            print("Invalid selection")
        except:
            print("Invalid input")
    
    return {'name': name, 'address': address, 'educational_qualifications': quals,
            'course': course, 'start_year': year, 'start_month': month}

def confirm_data(data):
    """Show the data and ask user to confirm"""
    print("\n" + "="*60)
    print("REVIEW YOUR APPLICATION")
    print("="*60)
    print("Name: " + data['name'])
    print("Address: " + data['address'])
    print("Qualifications: " + data['educational_qualifications'])
    print("Course: " + data['course'])
    print("Start: " + data['start_month'] + " " + str(data['start_year']))
    print("="*60)
    
    confirm = input("\nSubmit? (yes/no): ").strip().lower()
    return confirm in ['yes', 'y']

def main():
    """Main client function - TCP connection to server"""
    HOST = '127.0.0.1'
    PORT = 5555
    
    print("="*60)
    print("DUBLIN BUSINESS SCHOOL")
    print("ADMISSION APPLICATION SYSTEM")
    print("="*60)
    
    # Create TCP socket
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.settimeout(300)  # 5 minute timeout
    
    try:
        # Connect to server
        print("\nConnecting to server...")
        client_sock.connect((HOST, PORT))
        print("Connected successfully!")
        
        # Receive handshake
        handshake = client_sock.recv(1024).decode('utf-8')
        msg = json.loads(handshake)
        print(msg['message'])
        
        # Get application data
        data = get_application_data()
        
        # Confirm before sending
        if not confirm_data(data):
            print("\nApplication cancelled")
            return
        
        # Send data to server
        print("\nSending application...")
        data_json = json.dumps(data)
        client_sock.send(data_json.encode('utf-8'))
        print("Data sent: " + str(len(data_json)) + " bytes")
        
        # Wait for response
        print("Waiting for response...")
        response = client_sock.recv(4096).decode('utf-8')
        result = json.loads(response)
        
        # Display result
        print("\n" + "="*60)
        if result['status'] == 'success':
            print("APPLICATION SUBMITTED SUCCESSFULLY")
            print("="*60)
            print("\nRegistration Number: " + result['registration_number'])
            print("Please save this number for your records")
        else:
            print("APPLICATION FAILED")
            print("="*60)
            print("\nError: " + result['message'])
        print("="*60)
        
    except ConnectionRefusedError:
        print("\nError: Connection refused")
        print("Please ensure server is running")
    except socket.timeout:
        print("\nError: Connection timeout")
    except Exception as e:
        print("\nError: " + str(e))
    finally:
        client_sock.close()
        print("\nThank you for using DBS Admission System")

if __name__ == "__main__":
    main()
