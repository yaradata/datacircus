import os

# from pathlib import Path
# file = Path() / 'doc.txt'  # or Path('./doc.txt')
# size = file.stat().st_size

async def convert_file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)

        fsize = file_info.st_size
        ext = ""
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if fsize < 1024.0:
                ext = x
                return f"{fsize:.3f} {x}"
                # return "%3.1f %s" % (fsize, x)
            fsize /= 1024.0

        return f"{fsize:.2f} {ext}"

