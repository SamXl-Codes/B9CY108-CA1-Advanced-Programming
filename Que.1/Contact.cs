// Samuel Ogunlusi
// Contact class - stores individual contact details
// Using properties for encapsulation like we learned in class

using System;

public class Contact
{
    private string firstName;
    private string lastName;
    private string company;
    private string mobile;
    private string email;
    private DateTime birthdate;

    public string FirstName
    {
        get { return firstName; }
        set
        {
            if (string.IsNullOrWhiteSpace(value))
                throw new Exception("Name required");
            firstName = value;
        }
    }

    public string LastName
    {
        get { return lastName; }
        set
        {
            if (string.IsNullOrWhiteSpace(value))
                throw new Exception("Name required");
            lastName = value;
        }
    }

    public string Company
    {
        get { return company; }
        set { company = value; }
    }

    public string Mobile
    {
        get { return mobile; }
        set
        {
            string clean = value.Replace(" ", "").Replace("-", "");
            if (clean.Length != 9)
                throw new Exception("Mobile must be 9 digits");
            mobile = value;
        }
    }

    public string Email
    {
        get { return email; }
        set
        {
            if (!value.Contains("@"))
                throw new Exception("Invalid email");
            email = value;
        }
    }

    public DateTime Birthdate
    {
        get { return birthdate; }
        set { birthdate = value; }
    }

    public Contact(string fn, string ln, string co, string mb, string em, DateTime bd)
    {
        FirstName = fn;
        LastName = ln;
        Company = co;
        Mobile = mb;
        Email = em;
        Birthdate = bd;
    }

    // basic Show method
    public void Show()
    {
        Console.WriteLine("Name: " + FirstName + " " + LastName);
        Console.WriteLine("Company: " + Company);
        Console.WriteLine("Mobile: " + Mobile);
        Console.WriteLine("Email: " + Email);
        Console.WriteLine("Birthdate: " + Birthdate.ToString("dd/MM/yyyy"));
    }

    // Show method with extra parameter for date format
    public void Show(bool fullDate)
    {
        Console.WriteLine("Name: " + FirstName + " " + LastName);
        Console.WriteLine("Company: " + Company);
        Console.WriteLine("Mobile: " + Mobile);
        Console.WriteLine("Email: " + Email);
        if (fullDate)
            Console.WriteLine("Birthdate: " + Birthdate.ToString("dddd, dd MMMM yyyy"));
        else
            Console.WriteLine("Birthdate: " + Birthdate.ToString("dd/MM/yyyy"));
    }

    public string GetFullName()
    {
        return FirstName + " " + LastName;
    }
}
