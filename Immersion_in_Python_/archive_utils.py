import os
import zipfile

def create_zip_archive(source_dir, target_zip):
    """Создаёт архив .zip из указанного каталога."""
    with zipfile.ZipFile(target_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # Добавляем файл в архив, сохраняя структуру директорий
                arcname = os.path.relpath(file_path, start=source_dir)
                zipf.write(file_path, arcname)
    print(f"Архив создан: {target_zip}")