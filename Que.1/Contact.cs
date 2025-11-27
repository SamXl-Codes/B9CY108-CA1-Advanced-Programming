using System;

// Contact class for storing person details
public class Contact
{
    // private fields
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
            // remove spaces and dashes then check length
            string clean = value.Replace(" ", "").Replace("-", "");
            if (clean.Length != 9)
                throw new Exception("Mobile needs 9 digits");
            if (clean[0] == '0')
                throw new Exception("Mobile cannot start with zero");
            if (!clean.All(char.IsDigit))
                throw new Exception("Mobile must be digits only");
            mobile = value;
        }
    }

    public string Email
    {
        get { return email; }
        set
        {
            if (!value.Contains("@"))
                throw new Exception("Email not valid");
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

    // display contact info
    public void Show()
    {
        Console.WriteLine("Name: " + FirstName + " " + LastName);
        Console.WriteLine("Company: " + Company);
        Console.WriteLine("Mobile: " + Mobile);
        Console.WriteLine("Email: " + Email);
        Console.WriteLine("Birthdate: " + Birthdate.ToString("dd/MM/yyyy"));
    }

    // overloaded Show method with date format option
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
