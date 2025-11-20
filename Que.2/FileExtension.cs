// stores info about file extensions

using System;

public class FileExtension
{
    private string ext;
    private string desc;
    private string cat;
    private string progs;

    public string Extension { get { return ext; } set { ext = value; } }
    public string Description { get { return desc; } set { desc = value; } }
    public string Category { get { return cat; } set { cat = value; } }
    public string Programs { get { return progs; } set { progs = value; } }

    public FileExtension(string e, string d, string c, string p)
    {
        ext = e;
        desc = d;
        cat = c;
        progs = p;
    }

    // display extension details
    public void Show()
    {
        Console.WriteLine("\nExtension: " + Extension);
        Console.WriteLine("Description: " + Description);
        Console.WriteLine("Category: " + Category);
        Console.WriteLine("Programs: " + Programs);
    }
}
