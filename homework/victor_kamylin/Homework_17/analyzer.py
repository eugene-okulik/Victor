import os
import argparse


def analyze_logs():
    # 1. Настройка аргументов
    parser = argparse.ArgumentParser(description="Поиск в логах")
    parser.add_argument("path", help="Путь к папке с логами")
    parser.add_argument("--text", required=True, help="Текст для поиска")
    args = parser.parse_args()

    if os.path.isdir(args.path):
        files = [os.path.join(args.path, f) for f in os.listdir(
            args.path) if os.path.isfile(os.path.join(args.path, f))]
    else:
        print("Указанный путь не является папкой")
        return

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

            lines = content.splitlines()

            current_block = ""
            timestamp = ""

            for line in lines:
                if line and line[0].isdigit():
                    if args.text in current_block:
                        print_result(file_path, timestamp,
                                     current_block, args.text)

                    # Берем первые два "слова" (дата и время)
                    timestamp = " ".join(line.split()[:2])
                    current_block = line
                else:
                    current_block += " " + line

            if args.text in current_block:
                print_result(file_path, timestamp, current_block, args.text)


def print_result(file_name, time, block, target):
    words = block.split()
    if target in words:
        idx = words.index(target)
        # Берем 5 слов до и 5 после
        start = max(0, idx - 5)
        end = idx + 6
        context = " ".join(words[start:end])

        print(f"Файл: {os.path.basename(file_name)}")
        print(f"Время: {time}")
        print(f"Контекст: ...{context}...")
        print("-" * 40)


if __name__ == "__main__":
    analyze_logs()
