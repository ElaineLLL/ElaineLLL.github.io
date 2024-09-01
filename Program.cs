var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Serve static files from the "public" directory
app.UseDefaultFiles();
app.UseStaticFiles(new StaticFileOptions
{
    FileProvider = new Microsoft.Extensions.FileProviders.PhysicalFileProvider(
        Path.Combine(Directory.GetCurrentDirectory(), "Web")),
    RequestPath = ""
});

// API endpoint
app.MapGet("/api/message", () => new { message = "Hello from the backend!" });

// Fallback to index.html for any route (for client-side routing like React Router)
app.MapFallbackToFile("index.html", new StaticFileOptions
{
    FileProvider = new Microsoft.Extensions.FileProviders.PhysicalFileProvider(
        Path.Combine(Directory.GetCurrentDirectory(), "Web")),
});

// Run the application
app.Run();