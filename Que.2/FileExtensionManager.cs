// Samuel Ogunlusi
// Manages file extensions using Dictionary collection
// Similar to the DictionaryDemo we did in class

using System;
using System.Collections.Generic;

public class FileExtensionManager
{
    private Dictionary<string, FileExtension> db;

    public FileExtensionManager()
    {
        db = new Dictionary<string, FileExtension>(StringComparer.OrdinalIgnoreCase);
        Load();
    }

    private void Load()
    {
        Add(".mp4", "MPEG-4 Video", "Video", "VLC, WMP");
        Add(".mov", "QuickTime Movie", "Video", "QuickTime, VLC");
        Add(".avi", "AVI Video", "Video", "VLC, WMP");
        Add(".mkv", "Matroska Video", "Video", "VLC, MPC-HC");
        Add(".webm", "WebM Video", "Video", "VLC, Chrome");
        Add(".mp3", "MP3 Audio", "Audio", "WMP, VLC, iTunes");
        Add(".wav", "WAV Audio", "Audio", "WMP, Audacity");
        Add(".flac", "FLAC Audio", "Audio", "VLC, foobar2000");
        Add(".pdf", "PDF Document", "Document", "Adobe Reader");
        Add(".docx", "Word Document", "Document", "MS Word");
        Add(".xlsx", "Excel Spreadsheet", "Document", "MS Excel");
        Add(".pptx", "PowerPoint", "Document", "MS PowerPoint");
        Add(".txt", "Text File", "Document", "Notepad");
        Add(".jpg", "JPEG Image", "Image", "Photo Viewer");
        Add(".png", "PNG Image", "Image", "Photo Viewer");
        Add(".gif", "GIF Image", "Image", "Browser");
        Add(".svg", "SVG Vector", "Image", "Browser");
        Add(".py", "Python File", "Programming", "Python, VS Code");
        Add(".cs", "C# File", "Programming", "Visual Studio");
        Add(".java", "Java File", "Programming", "Eclipse, IntelliJ");
        Add(".zip", "ZIP Archive", "Archive", "WinZip, 7-Zip");
        Add(".rar", "RAR Archive", "Archive", "WinRAR, 7-Zip");
    }

    private void Add(string e, string d, string c, string p)
    {
        db[e] = new FileExtension(e, d, c, p);
    }

    // Search - basic version
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

    // Search with option to show related extensions
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
