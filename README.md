# B9CY108 Advanced Programming Techniques - CA 1 (30%)

**Student:** Samuel Ogunlusi  
**Course:** B9CY108 Advanced Programming Techniques  
**Assignment:** CA 1 - Object-Oriented Programming with Collections  
**Institution:** Dublin Business School  
**Due Date:** December 13, 2025  

## Assignment Overview

This repository contains 4 programming questions demonstrating:
- Object-Oriented Programming concepts (encapsulation, method overloading)
- Collections (List, Dictionary)
- TCP client-server networking
- Database operations with SQLite
- Web scraping with BeautifulSoup

## Questions

### Question 1: Contact Book (C#)
- **Files:** Que.1/Contact.cs, ContactBook.cs, Program.cs
- **Features:** OOP principles, List collection, CRUD operations
- **Demonstrates:** Encapsulation, method overloading, properties

### Question 2: File Extension Info (C#)
- **Files:** Que.2/FileExtension.cs, FileExtensionManager.cs, Program.cs
- **Features:** Dictionary collection, case-insensitive search
- **Demonstrates:** Key-value pairs, method overloading

### Question 3: DBS Admission System (Python)
- **Files:** Que3_server.py/server.py, Que3_client.py/client.py
- **Features:** TCP socket programming, SQLite database
- **Security:** Parameterized queries, input validation, connection timeout
- **Demonstrates:** Client-server architecture, SQL injection prevention

### Question 4: Hotel Price Scraper (Python)
- **Files:** Que4.py/scraper.py
- **Features:** Web scraping, CSV export, data analysis
- **Source:** https://www.scrapethissite.com/pages/simple/ (educational use permitted)
- **Demonstrates:** BeautifulSoup, data processing

## Running the Programs

### C# Programs (Que.1 & Que.2)
```bash
cd Que.1
dotnet run

cd Que.2
dotnet run
```

### Python Programs (Que.3 & Que.4)
```bash
# Start server first (terminal 1)
cd Que3_server.py
python server.py

# Then run client (terminal 2)
cd Que3_client.py
python client.py

# Run scraper
cd Que4.py
python scraper.py
```

## Security Features

- **TCP Protocol:** Connection-oriented SOCK_STREAM sockets
- **SQL Injection Prevention:** Parameterized queries with ? placeholders
- **Input Validation:** Field checking before database insertion
- **Timeout Handling:** 300-second (5-minute) connection timeout
- **Error Handling:** Try-except blocks throughout

## Database Schema

**Table:** applicants
- id (INTEGER PRIMARY KEY AUTOINCREMENT)
- registration_number (TEXT UNIQUE NOT NULL)
- name (TEXT NOT NULL)
- address (TEXT NOT NULL)
- educational_qualifications (TEXT NOT NULL)
- course (TEXT NOT NULL)
- start_year (INTEGER NOT NULL)
- start_month (TEXT NOT NULL)
- application_date (TEXT NOT NULL)

## External Resources Used

- **Python Documentation:** https://docs.python.org/3/library/socket.html (TCP sockets)
- **Python Documentation:** https://docs.python.org/3/library/sqlite3.html (SQLite)
- **Beautiful Soup Documentation:** https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- **Microsoft C# Documentation:** https://learn.microsoft.com/en-us/dotnet/csharp/ (Collections)
- **SQLite Tutorial:** https://www.sqlitetutorial.net/ (Database design)
- **ScrapThisSite:** https://www.scrapethissite.com/ (Educational scraping sandbox)

## Project Structure

```
CA 1/
├── Que.1/           # ContactBook C# project
├── Que.2/           # File Extension C# project
├── Que3_server.py/  # Admission server
├── Que3_client.py/  # Admission client
├── Que4.py/         # Hotel scraper
├── README.md
└── .gitignore
```

## Academic Integrity Declaration

This work represents my own efforts. External resources and documentation used for learning purposes are cited above. All code was written by me for educational purposes as part of the B9CY108 course assessment.

---
*Repository created: November 2025*
