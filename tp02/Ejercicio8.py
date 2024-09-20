from typing import List

def num_impar() -> List[int]:
    return list(filter(lambda x: x % 2 != 0, range(100,201)))

def main() -> None:
    result = num_impar()
    print(f"los numeros impares entre 100 y 200 son: {result}")

if __name__ == "__main__":
    main()