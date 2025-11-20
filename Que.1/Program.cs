using System;

class Program
{
    static void Main(string[] args)
    {
        ContactBook book = new ContactBook();
        Console.WriteLine("CONTACT BOOK\n");

        while (true)
        {
            Console.WriteLine("\n1: Add | 2: Show All | 3: Details | 4: Update | 5: Delete | 0: Exit");
            Console.Write("Choice: ");
            string choice = Console.ReadLine();

            try
            {
                if (choice == "1")
                {
                    Console.Write("First Name: ");
                    string fn = Console.ReadLine();
                    Console.Write("Last Name: ");
                    string ln = Console.ReadLine();
                    Console.Write("Company: ");
                    string co = Console.ReadLine();
                    Console.Write("Mobile: ");
                    string mb = Console.ReadLine();
                    Console.Write("Email: ");
                    string em = Console.ReadLine();
                    Console.Write("Birthdate (dd/MM/yyyy): ");
                    DateTime bd;
                    if (DateTime.TryParseExact(Console.ReadLine(), "dd/MM/yyyy", null, 
                        System.Globalization.DateTimeStyles.None, out bd))
                    {
                        book.Add(fn, ln, co, mb, em, bd);
                        Console.WriteLine("Added");
                    }
                    else
                        Console.WriteLine("Bad date");
                }
                else if (choice == "2")
                    book.ShowAll();
                else if (choice == "3")
                {
                    book.ShowAll();
                    Console.Write("\nContact #: ");
                    int vn;
                    if (int.TryParse(Console.ReadLine(), out vn))
                        book.ShowDetails(vn - 1);
                }
                else if (choice == "4")
                {
                    book.ShowAll();
                    Console.Write("\nUpdate #: ");
                    int un;
                    if (int.TryParse(Console.ReadLine(), out un))
                    {
                        Console.Write("First Name: ");
                        string fn = Console.ReadLine();
                        Console.Write("Last Name: ");
                        string ln = Console.ReadLine();
                        Console.Write("Company: ");
                        string co = Console.ReadLine();
                        Console.Write("Mobile: ");
                        string mb = Console.ReadLine();
                        Console.Write("Email: ");
                        string em = Console.ReadLine();
                        Console.Write("Birthdate (dd/MM/yyyy): ");
                        DateTime bd;
                        if (DateTime.TryParseExact(Console.ReadLine(), "dd/MM/yyyy", null,
                            System.Globalization.DateTimeStyles.None, out bd))
                            book.Update(un - 1, fn, ln, co, mb, em, bd);
                    }
                }
                else if (choice == "5")
                {
                    book.ShowAll();
                    Console.Write("\nDelete #: ");
                    int dn;
                    if (int.TryParse(Console.ReadLine(), out dn))
                    {
                        Console.Write("Confirm (y/n): ");
                        if (Console.ReadLine().ToLower() == "y")
                            book.Delete(dn - 1);
                    }
                }
                else if (choice == "0")
                {
                    Console.WriteLine("Goodbye");
                    return;
                }
                else
                    Console.WriteLine("Invalid");
            }
            catch (Exception e)
            {
                Console.WriteLine("Error: " + e.Message);
            }
            Console.WriteLine("\nPress any key...");
            Console.ReadKey();
        }
    }
}
