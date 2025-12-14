## BTC_Adress_Brute_force

##  Tecnologias

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/topics/python)



Brute-force sobre o BTC adress e que testa até 2 caracteres trocados.
Endereço P2PKH (Pay-to-PubKey-Hash)

## Base58 Address Brute-Force Validator

Este repositório fornece um script em Python para recuperação de endereços **Base58Check** corrompidos (como endereços Bitcoin), realizando uma busca exaustiva por variantes com até **duas substituições de caracteres**. 

O objetivo é identificar possíveis correções que resultem em um endereço válido segundo a verificação de checksum da codificação Base58Check.

---

##  Objetivo

Corrigir erros tipográficos em endereços codificados em Base58 (por exemplo, endereços de carteira Bitcoin), quando há suspeita de até dois caracteres incorretos. 

O script tenta todas as combinações possíveis em duas posições e verifica se o endereço resultante é válido.

---

##  Funcionamento

- O código utiliza a função `base58.b58decode_check()` para validar o checksum.
- É feita uma busca por todas as combinações de **duas posições** em que os caracteres podem ter sido alterados.
- Para cada par de posições, todas as substituições possíveis do alfabeto Base58 são testadas.
- Caso um endereço válido seja encontrado, ele é impresso juntamente com a descrição da modificação.
- O processo é interrompido quando:
  - O número máximo de resultados (`max_results`) for atingido, ou
  - O número máximo de tentativas (`max_attempts`) for excedido.

---

##  Estrutura do Código

- `is_valid_base58_address(address)`  
  Valida um endereço Base58 com checksum, retornando `True` se for válido.

- `brute_force_base58_verbose(address, max_results=5, max_attempts=None)`  
  Função principal que realiza a busca exaustiva. Parâmetros:
  - `address`: endereço Base58 suspeito
  - `max_results`: número máximo de endereços válidos a retornar
  - `max_attempts`: (opcional) número máximo de tentativas

---

##  Exemplo de Execução

```python
# Endereço corrompido:
endereco = '1BoutSLRHtKNngkdXEeobR76b53LETtpyX'

# Executa brute-force buscando apenas 1 resultado válido:
brute_force_base58_verbose(endereco, max_results=1, max_attempts=5_000_000)

 Iniciando brute-force sobre o endereço: 1BoutSLRHtKNngkdXEeobR76b53LETtpyX
 Testando variações com até 2 caracteres trocados...
 Total estimado de combinações: 244,944

 10.000 tentativas... tempo decorrido: 1.2s
 ...
Válido encontrado: 1BoatSLRHtKNngkdXEeobR76b53LETtpyT
   ↳ Posição 3: 'u' → 'a', Posição 33: 'X' → 'T'
 Limite de resultados atingido.
```

You can reach me at rmilhomem[at]gmail[dot]com or connect on [LinkedIn](https://www.linkedin.com/in/rodolfo-space-force/) for collaborations.


## Licença

Este projeto está licenciado sob a Licença MIT. Você pode usar, modificar e redistribuir este código livremente, desde que mencione o autor original.

[![MIT License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)



