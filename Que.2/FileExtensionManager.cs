using System;
using System.Collections.Generic;

// manages file extensions using Dictionary
public class FileExtensionManager
{
    private Dictionary<string, FileExtension> db;

    public FileExtensionManager()
    {
        db = new Dictionary<string, FileExtension>(StringComparer.OrdinalIgnoreCase);
        Load();
    }

    // load default extensions
    private void Load()
    {
        Add(".mp4", "MPEG-4 Video", "Video", "VLC, WMP");
        Add(".avi", "AVI Video", "Video", "VLC, WMP");
        Add(".mp3", "MP3 Audio", "Audio", "WMP, VLC");
        Add(".wav", "WAV Audio", "Audio", "WMP, Audacity");
        Add(".pdf", "PDF Document", "Document", "Adobe Reader");
        Add(".docx", "Word Document", "Document", "MS Word");
        Add(".txt", "Text File", "Document", "Notepad");
        Add(".jpg", "JPEG Image", "Image", "Photo Viewer");
        Add(".png", "PNG Image", "Image", "Photo Viewer");
        Add(".py", "Python File", "Programming", "Python");
        Add(".cs", "C# File", "Programming", "Visual Studio");
        Add(".zip", "ZIP Archive", "Archive", "7-Zip");
        Add(".mov", "QuickTime Movie", "Video", "QuickTime, VLC");
        Add(".mkv", "Matroska Video", "Video", "VLC, MPC-HC");
        Add(".webm", "WebM Video", "Video", "VLC, Chrome");
        Add(".flac", "FLAC Audio", "Audio", "VLC, foobar2000");
        Add(".xlsx", "Excel Spreadsheet", "Document", "MS Excel");
        Add(".gif", "GIF Image", "Image", "Browser");
        Add(".svg", "SVG Vector", "Image", "Browser");
        Add(".rar", "RAR Archive", "Archive", "WinRAR, 7-Zip");
    }

    private void Add(string e, string d, string c, string p)
    {
        db[e] = new FileExtension(e, d, c, p);
    }

    // search for extension
    public void Search(string ext)
    {
        if (!ext.StartsWith(".")) ext = "." + ext;
        
        if (db.ContainsKey(ext))
        {
            Console.WriteLine("\nINFO:");
            db[ext].Show();
        }
        else
        {
            Console.WriteLine("\nNot found");
        }
    }

    // search with option to show related files
    public void Search(string ext, bool showRelated)
    {
        if (!ext.StartsWith(".")) ext = "." + ext;
        
        if (db.ContainsKey(ext))
        {
            db[ext].Show();
            if (showRelated)
            {
                Console.WriteLine("\nRelated:");
                foreach (FileExtension f in db.Values)
                {
                    if (f.Category == db[ext].Category && f.Extension != ext)
                        Console.Write(f.Extension + " ");
                }
                Console.WriteLine();
            }
        }
        else
        {
            Console.WriteLine("\nNot found");
        }
    }

    public void ShowAll()
    {
        Console.WriteLine("\nExtensions (" + db.Count + "):");
        foreach (string cat in new string[] {"Video", "Audio", "Document", "Image", "Programming", "Archive"})
        {
            Console.Write("\n" + cat + ": ");
            foreach (FileExtension f in db.Values)
            {
                if (f.Category == cat)
                    Console.Write(f.Extension + " ");
            }
        }
        Console.WriteLine();
    }
}
