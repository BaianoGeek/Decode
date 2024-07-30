# Decode Hash Cracker

Este projeto é uma ferramenta de brute force para descobrir senhas a partir de hashes. Ele utiliza diferentes algoritmos de criptografia e uma wordlist para tentar encontrar a senha correspondente a um hash fornecido.

## Funcionalidades

- Identificação automática do algoritmo de hash a partir do identificador no hash fornecido.
- Suporte para vários algoritmos de hash: MD5, Blowfish, SHA-256, SHA-512 e Yescrypt.
- Uso de uma wordlist para tentar encontrar a senha correspondente ao hash fornecido.
- Progresso do brute force exibido com a biblioteca `tqdm`.
- Mensagens coloridas para melhor visualização dos resultados e erros.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `tqdm`
  - `colorama`

Você pode instalar as bibliotecas necessárias com o seguinte comando:

```
pip install tqdm colorama
```

## Uso

1. Clone o repositório para o seu ambiente local:
```
git clone https://github.com/BaianoGeek/Decode.git
```
2. Abra o diretório:
```
cd Decode
```
3. Execute o código python:
```
python3 decode.py
```

## Exemplo

```
↳[!] Informe o hash encontrado: $6$gfsjf7$kSjflkJS34lkjlkj34klj34lkjlkj23lksjdflk$

   Realizando Brute Force:  30%|█████████████████                           | 3000/10000 [00:30<01:10, 100.00itens/s]

↳[+] SENHA ENCONTRADA!!

↳[!] Foram analisadas um total de: 5000 possíbilidades.
↳[+] Hash informado: $6$gfsjf7$kSjflkJS34lkjlkj34klj34lkjlkj23lksjdflk$
↳[+] Senha: password123
↳[!] Criptografia: $6$ : SHA-512
↳[!] Salt: $gfsjf7$
```

## Contribuição

Contribuições são bem-vindas! Se você encontrar bugs ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.
