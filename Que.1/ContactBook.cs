using System;
using System.Collections.Generic;

// manages the contact book using List
public class ContactBook
{
    private List<Contact> contacts;

    public ContactBook()
    {
        contacts = new List<Contact>();
        LoadDefault();
    }

    // load some default contacts
    private void LoadDefault()
    {
        try
        {
            Add("Emily", "Blackwell", "DBS", "087111111", "emily@dbs.ie", new DateTime(1990, 1, 1));
            Add("John", "Smith", "Tech Ltd", "087222222", "john@tech.ie", new DateTime(1985, 3, 15));
            Add("Sarah", "Connor", "Cyber Inc", "087333333", "sarah@cyber.com", new DateTime(1992, 7, 22));
            Add("Michael", "OBrien", "Data Co", "087444444", "michael@data.ie", new DateTime(1988, 11, 30));
            Add("Lisa", "Murphy", "Cloud Sys", "087555555", "lisa@cloud.com", new DateTime(1995, 4, 18));
            Add("David", "Walsh", "AI Lab", "087666666", "david@ailab.ie", new DateTime(1987, 9, 5));
            Add("Emma", "Kelly", "Software", "087777777", "emma@soft.ie", new DateTime(1993, 12, 10));
            Add("James", "Ryan", "Networks", "087888888", "james@net.com", new DateTime(1990, 6, 25));
            Add("Sophie", "Brennan", "DBS", "087999999", "sophie@dbs.ie", new DateTime(1991, 2, 14));
            Add("Patrick", "Doyle", "IT Consult", "086111111", "patrick@it.ie", new DateTime(1986, 8, 8));
            Add("Rachel", "McCarthy", "Web Design", "086222222", "rachel@web.ie", new DateTime(1994, 5, 20));
            Add("Tom", "Fitzgerald", "Mobile Apps", "086333333", "tom@mobile.com", new DateTime(1989, 10, 12));
            Add("Amy", "Collins", "Database", "086444444", "amy@db.ie", new DateTime(1992, 1, 28));
            Add("Daniel", "OSullivan", "Security", "086555555", "daniel@sec.com", new DateTime(1988, 4, 7));
            Add("Kate", "Byrne", "DBS", "086666666", "kate@dbs.ie", new DateTime(1996, 11, 15));
            Add("Sean", "Dunne", "Innovation", "086777777", "sean@innov.ie", new DateTime(1987, 3, 3));
            Add("Olivia", "Quinn", "Startup", "086888888", "olivia@startup.com", new DateTime(1993, 7, 19));
            Add("Brian", "Kennedy", "Systems", "086999999", "brian@sys.ie", new DateTime(1990, 9, 21));
            Add("Grace", "Nolan", "Marketing", "085111111", "grace@mark.ie", new DateTime(1991, 12, 5));
            Add("Liam", "Power", "Cloud", "085222222", "liam@cloud.com", new DateTime(1989, 6, 17));
        }
        catch (Exception e)
        {
            Console.WriteLine("Error: " + e.Message);
        }
    }

    // add contact with individual parameters
    public void Add(string fn, string ln, string co, string mb, string em, DateTime bd)
    {
        contacts.Add(new Contact(fn, ln, co, mb, em, bd));
    }

    // add contact using Contact object
    public void Add(Contact c)
    {
        contacts.Add(c);
    }

    public void ShowAll()
    {
        Console.WriteLine("\nContacts (" + contacts.Count + "):");
        for (int i = 0; i < contacts.Count; i++)
        {
            Console.WriteLine((i + 1) + ". " + contacts[i].GetFullName() + " - " + contacts[i].Company);
        }
    }

    public void ShowDetails(int index)
    {
        if (index >= 0 && index < contacts.Count)
        {
            Console.WriteLine("\nDetails:");
            contacts[index].Show();
        }
        else
        {
            Console.WriteLine("Invalid");
        }
    }

    public void Update(int index, string fn, string ln, string co, string mb, string em, DateTime bd)
    {
        if (index >= 0 && index < contacts.Count)
        {
            // create new Contact triggers validation in property setters
            Contact updated = new Contact(fn, ln, co, mb, em, bd);
            contacts[index] = updated;
            Console.WriteLine("Updated");
        }
        else
        {
            Console.WriteLine("Invalid");
        }
    }

    public void Delete(int index)
    {
        if (index >= 0 && index < contacts.Count)
        {
            string name = contacts[index].GetFullName();
            contacts.RemoveAt(index);
            Console.WriteLine("Deleted: " + name);
        }
        else
        {
            Console.WriteLine("Invalid");
        }
    }
}
