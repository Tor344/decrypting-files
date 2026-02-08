from pathlib import Path


count = 0

def main(folder:Path) -> int:
    global count
    try:
        for element in folder.iterdir():
            if element.is_dir():
                main(element)
            else:
                count += 1
        return count
    except BaseException as e:
        print(f"Ошибка: {e}")
        return 0
    
    
if __name__ == "__main__":
    dir = input("Введите директорию (Enter для пути по умолчанию): ") or "/home/tor344/Documents/MyNode"
    print(main(folder=Path(dir)))