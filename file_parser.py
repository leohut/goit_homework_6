import sys
from pathlib import Path

# визначаємо списки, які будуть використовуватись для зберігання файлів з певними розширеннями
JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP4_VIDEO = []
AVI_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_AUDIO = []
OGG_AUDIO = []
VAV_AUDIO = []
AMR_AUDIO = []
MY_OTHER = []
ARCHIVES = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'VAV': VAV_AUDIO,
    'AMR': AMR_AUDIO,
    'DOC': DOC_DOCUMENTS,
    'DOCS': DOCX_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP4' : MP4_VIDEO,
    'AVI' : AVI_VIDEO,
    'MOV' : MOV_VIDEO,
    'MKV' : MKV_VIDEO,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES,
}

# оголошуємо змінні, які будуть використовуватись для зберігання папок
FOLDERS = []
EXTENSION = set()
UNKNOWN = set()

# приймаємо назву файлу і повертаємо його розширення в верхньому регістрі без крапки
def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

# рекурсивно скануємо всі файли та папки в цій папці
def scan(folder: Path) -> None:
    for item in folder.iterdir():

        if item.is_dir():

            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)  # рекурсія
            continue
          
        #  Робота з файлом. Якщо елемент є файлом, отримуємо його розширення
        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSION[ext]
                EXTENSION.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)


if __name__ == "__main__":
    folder_to_scan = sys.argv[1]
    print(f'Start in folder {folder_to_scan}')
    scan(Path(folder_to_scan))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    print(f'Audio mp3: {MP3_AUDIO}')   
    print(f'Audio ogg: {OGG_AUDIO}')
    print(f'Audio vav: {VAV_AUDIO}')
    print(f'Audio amr: {AMR_AUDIO}')
    print(f'Documents doc: {DOC_DOCUMENTS}')
    print(f'Documents docx: {DOCX_DOCUMENTS}')
    print(f'Documents pdf: {PDF_DOCUMENTS}')
    print(f'Documents txt: {TXT_DOCUMENTS}')
    print(f'Documents xlsx: {XLSX_DOCUMENTS}')
    print(f'Documents pptx: {PPTX_DOCUMENTS}')    
    print(f'Video mp4: {MP4_VIDEO}')  
    print(f'Video avi: {AVI_VIDEO}')
    print(f'Video mov: {MOV_VIDEO}')
    print(f'Video mkv: {MKV_VIDEO}')   
    print(f'Archives zip: {ARCHIVES}')
    print(f'Archives gz: {ARCHIVES}')
    print(f'Archives tar: {ARCHIVES}')
    print(f'Types of files in folder: {EXTENSION}')
    print(f'Unknown files of types: {UNKNOWN}')
    print(f'MY_OTHER: {MY_OTHER}')

    print(FOLDERS)
    