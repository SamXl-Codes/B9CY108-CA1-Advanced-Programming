// file extension lookup program

using System;

class Program
{
    static void Main(string[] args)
    {
        FileExtensionManager mgr = new FileExtensionManager();

        Console.WriteLine("FILE EXTENSION INFO");
        Console.WriteLine("===================\n");

        // main menu
        while (true)
        {
            Console.WriteLine("\n1: Search | 2: Search+Related | 3: Show All | 0: Exit");
            Console.Write("Choice: ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    Console.Write("\nExtension: ");
                    mgr.Search(Console.ReadLine());
                    break;

                case "2":
                    Console.Write("\nExtension: ");
                    mgr.Search(Console.ReadLine(), true);
                    break;

                case "3":
                    mgr.ShowAll();
                    break;

                case "0":
                    Console.WriteLine("Goodbye");
                    return;

                default:
                    Console.WriteLine("Invalid");
                    break;
            }

            Console.WriteLine("\nPress any key...");
            Console.ReadKey();
        }
    }
}
