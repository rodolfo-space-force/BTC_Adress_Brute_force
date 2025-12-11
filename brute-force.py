#Rodolfo Milhomem
#https://github.com/rodolfo-space-force/

import base58
from itertools import combinations, product
import time

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def is_valid_base58_address(address):
    try:
        base58.b58decode_check(address)
        return True
    except Exception:
        return False

def brute_force_base58_verbose(address, max_results=5, max_attempts=None):
    length = len(address)
    total_attempts = 0
    results = []

    print(f" Iniciando brute-force sobre o endereço: {address}")
    print(f" Testando variações com até 2 caracteres trocados...")

    positions = list(combinations(range(length), 2))
    total_combinations = len(positions) * (len(BASE58_ALPHABET) ** 2)
    print(f" Total estimado de combinações: {total_combinations:,}")

    start_time = time.time()

    for count, (i, j) in enumerate(positions, 1):
        for repl_i in BASE58_ALPHABET:
            for repl_j in BASE58_ALPHABET:
                if repl_i == address[i] and repl_j == address[j]:
                    continue
                candidate = (
                    address[:i] + repl_i + address[i+1:j] + repl_j + address[j+1:]
                )
                total_attempts += 1
                if total_attempts % 10000 == 0:
                    elapsed = time.time() - start_time
                    print(f" {total_attempts:,} tentativas... tempo decorrido: {elapsed:.1f}s")

                if is_valid_base58_address(candidate):
                    print(f" Válido encontrado: {candidate}")
                    print(f"   ↳ Posição {i}: '{address[i]}' → '{repl_i}', Posição {j}: '{address[j]}' → '{repl_j}'")
                    results.append((candidate, i, repl_i, j, repl_j))
                    if len(results) >= max_results:
                        print(" Limite de resultados atingido.")
                        return results

                if max_attempts and total_attempts >= max_attempts:
                    print(" Limite de tentativas atingido.")
                    return results

    print("Busca concluída.")
    return results

# Executar
# endereco correto 1BoatSLRHtKNngkdXEeobR76b53LETtpyT

endereco = '1BoutSLRHtKNngkdXEeobR76b53LETtpyX'
brute_force_base58_verbose(endereco, max_results=1, max_attempts=5000000) #parar após 5 resultado, apenas use max_results=5

# Licença
#Este projeto está licenciado sob a **Licença MIT**.  
#Você pode usar, modificar e redistribuir este código livremente, **desde que mencione o autor original**.

