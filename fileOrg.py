import os, shutil, time, asyncio
from pathlib import Path
import aiofiles
import aiofiles.os

home = Path.home()
# Define the paths to the different folders
downloads = home / "Downloads"
documents = home / "Documents"
music = home / "Music"
pictures = home / "Pictures"
videos = home / "Videos"

# Define the file formats
image_formats = ['.jpg', '.png', '.jpeg', '.gif', '.bmp', '.tiff']
document_formats = ['.pdf', '.docx', '.doc', '.txt', '.csv', '.xlsx', '.xls']
video_formats = ['.mp4', '.avi', '.mov', '.mkv', '.mp3', '.wav', '.mpg', '.mpeg']
audio_formats = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
program_formats = ['.exe', '.dmg', '.app']
archive_formats = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.zst']
source_files = ['.py', '.java', '.cpp', '.c', '.js', '.ts', '.json', '.md', '.mdx', '.html', '.css', '.scss', '.sass', '.xml', '.yaml', '.yml', '.sh', '.bash', '.zsh', '.ps1', '.bat', '.cmd', '.sh', '.bash', '.zsh', '.ps1', '.bat', '.cmd']

async def move_file(file_path, destination):
    """A asynchronous function to move files from the downloads folder to the appropriate folder.

    Args:
        file_path (Path): The path to the file to move.
        destination (Path): The destination folder to move the file to.
    """
    await aiofiles.os.rename(file_path, destination / file_path.name)

async def organize_files():
    """A asynchronous function to organize files in the downloads folder."""
    for file in await aiofiles.os.listdir(downloads):
        file_path = downloads / file
        if file_path.suffix.lower() in image_formats:
            await move_file(file_path, pictures)
        elif file_path.suffix.lower() in document_formats:
            await move_file(file_path, documents)
        elif file_path.suffix.lower() in video_formats:
            await move_file(file_path, videos)
        elif file_path.suffix.lower() in audio_formats:
            await move_file(file_path, music)
        elif file_path.suffix.lower() in program_formats:
            await move_file(file_path, documents)
        elif file_path.suffix.lower() in archive_formats:
            await move_file(file_path, documents)
        elif file_path.suffix.lower() in source_files:
            await move_file(file_path, documents)

async def main():
    print("Organizing files...")
    while True:
        if downloads.exists() and downloads.is_dir():
            await organize_files()
        await asyncio.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    asyncio.run(main())
