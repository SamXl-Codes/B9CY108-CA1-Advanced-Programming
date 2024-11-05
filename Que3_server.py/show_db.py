import sqlite3

conn = sqlite3.connect('dbs_admissions.db')
cursor = conn.cursor()

cursor.execute('SELECT id, name, registration_number, course FROM applicants ORDER BY id')
rows = cursor.fetchall()

print('\nCurrent records in database:')
print('='*70)
for row in rows:
    print(f'ID: {row[0]} | Name: {row[1]} | Reg: {row[2]}')
    print(f'Course: {row[3]}')
    print('-'*70)

print(f'\nTotal: {len(rows)} records\n')
conn.close()
