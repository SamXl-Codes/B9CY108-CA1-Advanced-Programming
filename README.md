# B9CY108 Advanced Programming Techniques - CA 1

**Course:** MSc Cyber Security  
**Module:** B9CY108 Advanced Programming Techniques  
**Assignment:** CA_ONE_(30%)  
**Institution:** Dublin Business School  
**Submission Deadline:** December 13, 2025  

---

## Overview

This repository contains solutions to 4 programming problems demonstrating Object-Oriented Programming, data structures, networking, and web scraping techniques.

**Part I (C#):** Contact management and file extension information systems  
**Part II (Python):** Client-server admission system and hotel price scraper

---

## Question 1: Contact Book System (30 marks)

**Language:** C#  
**Files:** `Que.1/Contact.cs`, `ContactBook.cs`, `Program.cs`

### Features
- 20 pre-loaded contacts with complete information
- Add new contacts with validation
- View all contacts or search specific contacts
- Update existing contact details
- Delete contacts
- 9-digit mobile number validation
- Email format validation

### OOP Concepts Demonstrated
- **Encapsulation:** Private fields with public properties
- **Properties:** Get/set accessors with validation logic
- **Method Overloading:** Multiple `Show()` and `Add()` methods
- **Collections:** `List<Contact>` for dynamic storage
- **Object Relationships:** ContactBook contains List of Contact objects

### How to Run
```bash
cd Que.1
dotnet run
```

---

## Question 2: File Extension Information System (20 marks)

**Language:** C#  
**Files:** `Que.2/FileExtension.cs`, `FileExtensionManager.cs`, `Program.cs`

### Features
- 20+ file extensions with detailed information
- Dictionary-based fast lookup
- Case-insensitive search
- Category grouping (Video, Audio, Document, Image, Programming, Archive)
- Graceful handling of unknown extensions

### Data Structure
- **Dictionary<string, FileExtension>** with StringComparer.OrdinalIgnoreCase
- **Method Overloading:** Two `Search()` methods with different parameters

### How to Run
```bash
cd Que.2
dotnet run
```

---

## Question 3: DBS Admission System (30 marks)

**Language:** Python  
**Files:** `Que3_server.py/server.py`, `Que3_client.py/client.py`

### System Architecture
**Client Application:**
- Console-based user interface
- Accepts applicant information (name, address, qualifications, course, start date)
- Connects to server via TCP
- Displays assigned registration number

**Server Application:**
- TCP socket server (connection-oriented protocol)
- SQLite database for persistent storage
- Generates unique 8-digit registration numbers
- JSON data format for client-server communication

### Available Courses
1. MSc in Cyber Security
2. MSc Information Systems & computing
3. MSc Data Analytics

### Security Features
- **TCP Protocol:** SOCK_STREAM connection-oriented sockets
- **SQL Injection Prevention:** Parameterized queries using `?` placeholders
- **Input Validation:** Required field checking
- **Timeout Handling:** 300-second connection timeout
- **Error Handling:** Try-except blocks throughout

### Database Schema
```sql
CREATE TABLE applicants (
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
```

### How to Run
```bash
# Terminal 1 - Start server
cd Que3_server.py
python server.py

# Terminal 2 - Run client
cd Que3_client.py
python client.py
```

---

## Question 4: Hotel Room Price Scraper (20 marks)

**Language:** Python  
**File:** `Que4.py/scraper.py`  
**Output:** `hotel_prices.csv`

### Features
- Scrapes real hotel room pricing data from API
- Two establishments: Shady Meadows B&B and Restful Lodge
- Seasonal period: December 20-30, 2025
- Multiple room types (Single, Double, Suite)
- Christmas premium pricing (Dec 22-25)
- CSV export with structured format
- Reads and displays CSV data in terminal
- Price analysis (cheapest, most expensive, average)

### Data Source
- **URL:** https://automationintesting.online/api/room/
- **Website:** https://automationintesting.online/
- **Authorization:** Educational testing site that permits scraping
- **Created by:** Ministry of Testing (automation practice platform)

### Python Modules Used
- `requests` - HTTP requests to API
- `csv` - CSV file operations
- `datetime` - Date handling
- `random` - Price variation simulation

### How to Run
```bash
cd Que4.py
python scraper.py
# Creates hotel_prices.csv with 33 pricing records
```

---

## Technical Implementation

### C# Collections
- **List<T>:** Dynamic contact storage (Question 1)
- **Dictionary<TKey, TValue>:** Fast file extension lookup (Question 2)

### Python Networking
- **socket module:** TCP/IP communication
- **JSON serialization:** Data exchange format
- **SQLite3:** Relational database operations

### Web Scraping
- **requests library:** HTTP API calls
- **CSV module:** Structured data storage
- **Data processing:** Price calculations and comparisons

---

## Project Structure

```
CA 1/
├── Que.1/
│   ├── Contact.cs
│   ├── ContactBook.cs
│   ├── Program.cs
│   └── Que.1.csproj
├── Que.2/
│   ├── FileExtension.cs
│   ├── FileExtensionManager.cs
│   ├── Program.cs
│   └── Que.2.csproj
├── Que3_server.py/
│   ├── server.py
│   └── dbs_admissions.db
├── Que3_client.py/
│   └── client.py
├── Que4.py/
│   ├── scraper.py
│   └── hotel_prices.csv
├── README.md
└── .gitignore
```

---

## External Resources

**Python Official Documentation**
- Socket Programming: https://docs.python.org/3/library/socket.html
- SQLite Database: https://docs.python.org/3/library/sqlite3.html
- CSV File Operations: https://docs.python.org/3/library/csv.html

**Microsoft C# Documentation**
- Collections: https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/collections
- Properties: https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/properties

**Third-Party Resources**
- Requests Library: https://requests.readthedocs.io/
- Automation Testing Site: https://automationintesting.online/ (Ministry of Testing)
- SQLite Tutorial: https://www.sqlitetutorial.net/

---

**GitHub Repository:** https://github.com/SamXl-Codes/B9CY108-CA1-Advanced-Programming

*Repository Created: 5th November 2025*
