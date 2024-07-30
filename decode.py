from tqdm import tqdm
from colorama import Fore, Style
import warnings

def banner():
    print("\n")
    print(Fore.YELLOW + "         ::::::::  " + Style.RESET_ALL + """      :::::::::      ::::::::       ::::::::        ::::::::         ::::::::  """)
    print(Fore.YELLOW + "       :+:     :+: " + Style.RESET_ALL + """     :+:           :+:    :+:     :+:+   :+:      :+:    :+:       :+:         """)
    print(Fore.YELLOW + "      +:+      +:+ " + Style.RESET_ALL + """    +:+           +:+            +:+    +:+      +:+     +:+      +:+          """)
    print(Fore.YELLOW + "     +#+      +#+  " + Style.RESET_ALL + """   +#++:++#:     +#+            +#+    +:+      +#+     +:+     +#++:++#:      """)
    print(Fore.YELLOW + "    +#+      #+#   " + Style.RESET_ALL + """  +#+           +#+            +#+    +#+      +#+     +#+     +#+             """)
    print(Fore.YELLOW + "   #+#     #+#     " + Style.RESET_ALL + """ #+#           #+#    #+#     #+#    #+#      #+#    #+#      #+#              """)
    print(Fore.YELLOW + "   ########        " + Style.RESET_ALL + """##########     ########       ########        ########       ########       \n""") 

class Tqdm(tqdm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

banner()

#crypt foi depreciado, suprimir erro
with warnings.catch_warnings():
    warnings.filterwarnings('ignore', category=DeprecationWarning)
    import crypt

# Recebimento de informações
encryptedPass = input(f"   {Fore.YELLOW}↳[!] Informe o hash encontrado: {Style.RESET_ALL}")
print("\n")

#Identificação do $ para o identifier e salt
firsDollar = encryptedPass.find('$')
secondDollar = encryptedPass.find('$', firsDollar + 1)
saltWithoutIdentifier = encryptedPass.find('$', secondDollar + 5)

identifier = encryptedPass[firsDollar : secondDollar + 1]
salt = encryptedPass[secondDollar + 1 : saltWithoutIdentifier + 1]

#Possibilidades de Algoritimos encontrados
match identifier:
    case "$1$":
        algorithms = "MD5"
    case "$2a$":
        algorithms = "BLOWFISH"
    case "$5$":
        algorithms = "SHA-256"
    case "$6$":
        algorithms = "SHA-512"
    case "$7$" | "$y$":
        algorithms = "YESCRYPT"
    case _:
        print(f"   {Fore.RED}↳[X]{Style.RESET_ALL} Não foi possível encontrar o identificador do Hash")
        exit()

# Abrir Wordlist
with open('wl.txt', 'r') as file:
    passwords =  [line.strip() for line in file]
 
#Iniciando contador de vezes que passou pelo loop abaixo
total_tentativas = 0
#Loop para encriptar as palavras da wordlist, utilisando o salt da variável encryptedPass
for password in Tqdm(passwords, desc="   Realizando Brute Force", total=len(passwords), unit="itens", ncols=100):
    encrypted = crypt.crypt(password, f"{identifier}{salt}")
    total_tentativas += 1
    if encrypted == encryptedPass:
        print(f"\n\n   {Fore.GREEN}↳[+] SENHA ENCONTRADA!!{Style.RESET_ALL}\n")
        #Informação de quantidade de linhas analisadas e o Hash informado
        print(f"   {Fore.YELLOW}↳[!]{Style.RESET_ALL} Foram analisadas um total de: {total_tentativas} possíbilidades.")
        print(f"   {Fore.YELLOW}↳[+]{Style.RESET_ALL} Hash informado: {encrypted}{Style.RESET_ALL}\n")
        #senha encontrada
        print(f"   {Fore.GREEN}↳[+]{Style.RESET_ALL} Senha: {Fore.GREEN}{password}{Style.RESET_ALL}\n")
        #Criptografia e salt encontrado
        print(f"   {Fore.YELLOW}↳[!]{Style.RESET_ALL} Criptografia: {identifier} : {algorithms}")
        print(f"   {Fore.YELLOW}↳[!]{Style.RESET_ALL} Salt: ${salt}\n")
        exit()
#Mensagem de erro caso não seja encontrado nenhuma senha
if encrypted != encryptedPass:
    print(f"\n   {Fore.RED}↳[X]{Style.RESET_ALL} Foram analisadas um total de :{total_tentativas} possíbilidades e a senha não foi encontrada!")
