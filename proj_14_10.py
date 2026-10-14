#Nome: Daniel Cesar Silva RA:05223-035 Eng.Computação
#Nome: Jeferson Augusto Manoel RA:05223-084 Eng.Computação
#Nome: Maria Eduarda Veríssimo Rodrigues RA:05223-061 Eng.Computação
#Nome: Patrick Valerio NUnes Braga RA:05223-054 Eng.Computação
def fifo(pagina, memoria, fila, qtd_frames):
    if pagina in memoria:
        return "HIT"
    else:
        if len(memoria) < qtd_frames:
            memoria.append(pagina)
            fila.append(pagina)
        else:
            antiga = fila.pop(0)
            memoria.remove(antiga)
            memoria.append(pagina)
            fila.append(pagina)
        return "PAGE FAULT"

def lru(pagina, memoria, fila, qtd_frames):
    if pagina in memoria:
        fila.remove(pagina)
        fila.append(pagina)
        return "HIT"
    else:
        if len(memoria) < qtd_frames:
            memoria.append(pagina)
            fila.append(pagina)
        else:
            antiga = fila.pop(0)
            memoria.remove(antiga)
            memoria.append(pagina)
            fila.append(pagina)
        return "PAGE FAULT"
            
paginas = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
qtd_frames =int(input("Dite a quantidade de frames:"))

memoria = []
fila = []
faults = 0
hits = 0

print("\n--- FIFO ---")
for pagina in paginas:
    resultado = fifo(pagina, memoria, fila, qtd_frames)

    if resultado == "HIT":
        hits += 1
    else:
        faults += 1

    print(f"Pagina: {pagina} - Resultado: {resultado} - Memoria: {memoria} - Fila: {fila}")

print("\n--- LRU ---")
for pagina in paginas:
    resultado = lru(pagina, memoria, fila, qtd_frames)

    if resultado == "HIT":
        hits += 1
    else:
        faults += 1

    print(f"Pagina: {pagina} - Resultado: {resultado} - Memoria: {memoria} - Fila: {fila}")

print("\n--- RESULTADO FINAL ---")
print(f"Hits: {hits}")
print(f"Page Faults: {faults}")

    

