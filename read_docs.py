#!/usr/bin/env python3
import os
from docx import Document

def read_docx(file_path):
    """Читает содержимое .docx файла и возвращает текст"""
    try:
        doc = Document(file_path)
        text = []
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                text.append(paragraph.text.strip())
        return '\n'.join(text)
    except Exception as e:
        return f"Ошибка при чтении файла {file_path}: {str(e)}"

def main():
    source_materials_path = "/Users/jacobvardanyan/PycharmProjects/Trans-credit/Source Materials"
    
    # Список файлов для анализа
    files_to_read = [
        "TransCredit - 2025_09_26 17_14 CEST - Notes by Gemini.docx",
        "[Tech Spec.] TransCredit - Certificates.docx"
    ]
    
    for filename in files_to_read:
        file_path = os.path.join(source_materials_path, filename)
        if os.path.exists(file_path):
            print(f"\n{'='*80}")
            print(f"ФАЙЛ: {filename}")
            print(f"{'='*80}")
            content = read_docx(file_path)
            print(content)
            print(f"\n{'='*80}\n")
        else:
            print(f"Файл не найден: {file_path}")

if __name__ == "__main__":
    main()
