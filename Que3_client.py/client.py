# client for submitting applications
import socket
import json

def get_input(prompt, max_len):
    while True:
        val = input(prompt).strip()
        if not val:
            print("Cannot be empty")
            continue
        if len(val) > max_len:
            print(f"Max {max_len} chars")
            continue
        return val

def get_application_data():
    print("\nAPPLICATION FORM")
    
    name = get_input("Full Name: ", 100)
    address = get_input("Address: ", 200)
    quals = get_input("Qualifications: ", 500)
    
    # show available courses
    print("\nCourses:")
    print("1. MSc in Cyber Security")
    print("2. MSc Information Systems & computing")
    print("3. MSc Data Analytics")
    
    courses = {'1': 'MSc in Cyber Security', '2': 'MSc Information Systems & computing', '3': 'MSc Data Analytics'}
    choice = input("Course (1-3): ").strip()
    course = courses.get(choice, courses['1'])
    
    year = int(input("Start Year: ").strip())
    
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    m = int(input("Month (1-12): ").strip())
    month = months[m - 1] if 1 <= m <= 12 else months[0]
    
    return {'name': name, 'address': address, 'educational_qualifications': quals,
            'course': course, 'start_year': year, 'start_month': month}

# let user review before submitting
def confirm_data(data):
    print("\nREVIEW:")
    print("Name: " + data['name'])
    print("Address: " + data['address'])
    print("Quals: " + data['educational_qualifications'])
    print("Course: " + data['course'])
    print("Start: " + data['start_month'] + " " + str(data['start_year']))
    confirm = input("\nSubmit? (y/n): ").strip().lower()
    return confirm == 'y'

def main():
    HOST = '127.0.0.1'
    PORT = 5555
    
    print("ADMISSION APPLICATION")
    
    # create socket and connect to server
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        print("Connecting...")
        client_sock.connect((HOST, PORT))
        print("Connected")
        
        handshake = client_sock.recv(1024).decode('utf-8')
        msg = json.loads(handshake)
        print(msg['message'])
        
        data = get_application_data()
        
        if not confirm_data(data):
            print("Cancelled")
            return
        
        # send application data
        print("\nSending...")
        data_json = json.dumps(data)
        client_sock.send(data_json.encode('utf-8'))
        
        response = client_sock.recv(4096).decode('utf-8')
        result = json.loads(response)
        
        if result['status'] == 'success':
            print("\nSUCCESS")
            print("Registration: " + result['registration_number'])
        else:
            print("\nFAILED: " + result['message'])
        
    except ConnectionRefusedError:
        print("Connection refused")
    except Exception as e:
        print("Error: " + str(e))
    finally:
        client_sock.close()

if __name__ == "__main__":
    main()
