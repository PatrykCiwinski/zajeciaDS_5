lista_skladana=[i for i in range(1, 101) if i % 5 == 0]
s = 0
print([s:=s+i for i in range(1, 101) if i%5 == 0][-1]) #printuje wszystkie sumy , dlatego [-1], żby ostatni wynik
print(sum(lista_skladana))