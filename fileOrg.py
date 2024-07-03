import os, shutil, time, asyncio, sys
from pathlib import Path
import aiofiles
import aiofiles.os
import argparse

# Define the file formats
image_formats = ['.jpg', '.png', '.jpeg', '.gif', '.bmp', '.tiff', '.dng']
document_formats = ['.pdf', '.docx', '.doc', '.txt', '.csv', '.xlsx', '.xls']
video_formats = ['.mp4', '.avi', '.mov', '.mkv', '.mpg', '.mpeg']
audio_formats = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
program_formats = ['.exe', '.dmg', '.app']
archive_formats = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.zst']
source_files = ['.py', '.java', '.cpp', '.c', '.js', '.ts', '.json', '.md', '.mdx', '.html', '.css', '.scss', '.sass', '.xml', '.yaml', '.yml', '.sh', '.bash', '.zsh', '.ps1', '.bat', '.cmd']

async def move_file(file_path, destination):
    """A asynchronous function to move files from the downloads folder to the appropriate folder.

    Args:
        file_path (Path): The path to the file to move.
        destination (Path): The destination folder to move the file to.
    """
    await aiofiles.os.rename(file_path, destination / file_path.name)

async def organize_files(directory):
    """A asynchronous function to organize files in the specified directory."""
    home = Path.home()
    downloads = Path(directory)
    documents = home / "Documents"
    music = home / "Music"
    pictures = home / "Pictures"
    videos = home / "Videos"

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

async def main(directory):
    print(f"Organizing files in {directory}...")
    while True:
        if Path(directory).exists() and Path(directory).is_dir():
            await organize_files(directory)
        await asyncio.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a specified directory.")
    parser.add_argument("directory", nargs="?", default=".", help="The directory to organize files in. Defaults to the current directory.")
    args = parser.parse_args()

    asyncio.run(main(args.directory))
