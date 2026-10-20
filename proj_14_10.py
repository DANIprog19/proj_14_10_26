#Nome: Daniel Cesar Silva RA:05223-035 Eng.Computação
#Nome: Jeferson Augusto Manoel RA:05223-084 Eng.Computação
#Nome: Maria Eduarda Veríssimo Rodrigues RA:05223-061 Eng.Computação
#Nome: Patrick Valerio NUnes Braga RA:05223-054 Eng.Computação

import threading
import time

# Anomalia de Belady
def testar_anomalia_belady(paginas):
    resultados = {}

    print("\n" + "-" * 15 + " ANOMALIA DE BELADY " + "-" * 15)

    for frames in range(1, 11):
        memoria, fila = [], []
        faults = 0

        for pagina in paginas:
            if fifo(pagina, memoria, fila, frames) == "PAGE FAULT":
                faults += 1

        resultados[frames] = faults
        print(f"{frames} frames: {faults} faltas")

    for frames in range(1, 10):
        if resultados[frames + 1] > resultados[frames]:
            print("\n" + "-" * 15 + " ANOMALIA DETECTADA " + "-" * 15)
            print(f"Anomalia detectada: {frames} para {frames + 1} frames!")


# FIFO
def fifo(pagina, memoria, fila, qtd_frames):
    if pagina in memoria:
        return "HIT"

    if len(memoria) < qtd_frames:
        memoria.append(pagina)
        fila.append(pagina)
    else:
        antiga = fila.pop(0)
        memoria.remove(antiga)
        memoria.append(pagina)
        fila.append(pagina)
        print(f"Página substituída: {antiga} -> {pagina}")

    return "PAGE FAULT"


# LRU
def lru(pagina, memoria, fila, qtd_frames):
    if pagina in memoria:
        fila.remove(pagina)
        fila.append(pagina)
        return "HIT"

    if len(memoria) < qtd_frames:
        memoria.append(pagina)
        fila.append(pagina)
    else:
        antiga = fila.pop(0)
        memoria.remove(antiga)
        memoria.append(pagina)
        fila.append(pagina)
        print(f"Página substituída: {antiga} -> {pagina}")

    return "PAGE FAULT"


# Deadlock
recurso_1 = threading.Lock()
recurso_2 = threading.Lock()

def processo_a():
    print("[Processo A] Executando...")
    with recurso_1:
        print("[Processo A] Adquiriu o Recurso 1.")
        time.sleep(1)
        print("[Processo A] Aguardando o Recurso 2...")
        with recurso_2:
            print("[Processo A] Adquiriu o Recurso 2.")

def processo_b():
    print("[Processo B] Executando...")
    with recurso_2:
        print("[Processo B] Adquiriu o Recurso 2.")
        time.sleep(1)
        print("[Processo B] Aguardando o Recurso 1...")
        with recurso_1:
            print("[Processo B] Adquiriu o Recurso 1.")


print("\n" + "-" * 20 + " SIMULAÇÃO DE DEADLOCK " + "-" * 20)

a = threading.Thread(target=processo_a, daemon=True)
b = threading.Thread(target=processo_b, daemon=True)

a.start()
b.start()

a.join(timeout=3)
b.join(timeout=3)

if a.is_alive() or b.is_alive():
    print("\n[!] DEADLOCK DETECTADO!")
    print("Processos envolvidos: Processo A e Processo B.")
    print("Processo A aguarda o Recurso 2.")
    print("Processo B aguarda o Recurso 1.")
else:
    print("\nProcessos finalizados sem deadlock.")

print("-" * 60)


# Paginação
paginas = [7, 0, 1, 2, 0, 3, 0, 4]

print("\n" + "-" * 20 + " SIMULAÇÃO DE PAGINAÇÃO " + "-" * 20)

qtd_frames = int(input("\nDigite a quantidade de frames: "))

print("-" * 55)

memoria = []
fila = []
faults = 0
hits = 0

print("\n" + "-" * 25 + " FIFO " + "-" * 25)

for pagina in paginas:
    resultado = fifo(pagina, memoria, fila, qtd_frames)

    if resultado == "HIT":
        hits += 1
    else:
        faults += 1

    print(f"Página: {pagina} - Resultado: {resultado} - Memória: {memoria} - Fila: {fila}")

print(f"\nHits: {hits}")
print(f"Page Faults: {faults}")


print("\n" + "-" * 25 + " LRU " + "-" * 25)

memoria = []
fila = []
hits = 0
faults = 0

for pagina in paginas:
    resultado = lru(pagina, memoria, fila, qtd_frames)

    if resultado == "HIT":
        hits += 1
    else:
        faults += 1

    print(f"Página: {pagina} - Resultado: {resultado} - Memória: {memoria} - Fila: {fila}")

print(f"\nHits: {hits}")
print(f"Page Faults: {faults}")


print("\n" + "-" * 20 + " RESULTADO FINAL " + "-" * 20)
print(f"Hits: {hits}")
print(f"Page Faults: {faults}")

testar_anomalia_belady(paginas)

print("\n" + "-" * 20 + " FIM DA SIMULAÇÃO " + "-" * 20)