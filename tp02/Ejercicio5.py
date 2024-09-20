def ordenada(lista: list[int]) -> bool:
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True


assert ordenada([1, 2, 3]) == True
assert ordenada(['b', 'a']) == False
