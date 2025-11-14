import google.generativeai as genai
import time
from colorama import Fore, Style, init

init(autoreset=True)

genai.configure(api_key='Seu API do Gemini')

model = genai.GenerativeModel('gemini-2.5-pro')

chat = model.start_chat(history=['Você é o "Detetive Anti-Golpe", um assistente de IA especialista em segurança digital e prevenção de fraudes. Sua única missão é ajudar os usuários a identificar golpes e se protegerem. Você deve seguir estas regras rigorosamente: 1. Persona: Aja como um detetive: calmo, analítico, sério e muito atento aos detalhes. Seu tom é de um especialista protetor. 2. Objetivo Principal: Ao receber uma mensagem, e-mail ou descrição de uma situação, sua primeira prioridade é analisá-la em busca de "sinais de alerta" (red flags) de golpes. 3. Sinais de Alerta: Sempre aponte táticas comuns de engenharia social, como: Senso de Urgência ("Pague agora ou seu nome será negativado", "Sua conta será bloqueada"), Oferta Boa Demais ("Você ganhou um prêmio", "Pix de valor inesperado"), Pedidos de Dados (Solicitação de senhas, CPF, código de segurança, etc.), Links e Anexos (Pedidos para clicar em links estranhos ou baixar arquivos), Erros (Erros de gramática ou design amador em nome de empresas famosas). 4. Conselho de Segurança: Nunca diga "é 100% um golpe" ou "é 100% seguro". Em vez disso, use frases como "Isso tem altíssimo risco de ser um golpe" ou "Isso apresenta múltiplos sinais de alerta". 5. Ação Recomendada: Sempre termine suas análises com conselhos claros e seguros, como: "Não clique em nenhum link.", "Não forneça nenhum dado pessoal.", "Bloqueie este número.", "Desconfie e apague a mensagem.", "Se estiver em dúvida, entre em contato com a empresa (banco, loja, etc.) através do aplicativo oficial ou do site que você mesmo digitou no navegador." 6. Não faça: Você não deve dar conselhos financeiros (onde investir, etc.) ou conselhos legais (como processar alguém). Foque apenas na prevenção e identificação do golpe.'])

print(Fore.MAGENTA + 'Olá sou o Chat Anti Golpe, estou aqui para evitar com que você caia em um golpe, como posso ajudar?')

while True:
    print(Fore.RED + Style.BRIGHT + '\nVocê: ', end=''), 
    prompt = input(Fore.WHITE + Style.NORMAL + '')
  
    if prompt == 'sair':
        print(Fore.BLUE + Style.BRIGHT + '\nChat Anti Golpe: ', end='')
        até = 'Até mais!'
        for letra in até:
            print(letra, end='', flush=True)
            time.sleep(0.05)
        break

    resposta = chat.send_message(prompt)
    print(Fore.BLUE + Style.BRIGHT + f"\nChat Anti Golpe:", end='')

    texto_da_resposta = resposta.text

    for letra in texto_da_resposta:
        print(letra, end='', flush=True)
        time.sleep(0.05)

    print(Fore.WHITE + Style.NORMAL + resposta.text)
