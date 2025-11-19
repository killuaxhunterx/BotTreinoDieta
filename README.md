🤖 Diet & Workout Generator Bot - Telegram

Este projeto é um bot de Telegram construído em Python, utilizando a biblioteca python-telegram-bot (PTB), projetado para coletar informações detalhadas do usuário (sobre dieta e treino) e, em seguida, gerar um plano personalizado. O resultado final é entregue como um documento PDF formatado, gerado pela biblioteca FPDF.

✨ Funcionalidades Principais

    Coleta de Dados Interativa: O bot guia o usuário através de uma série de perguntas essenciais (idade, peso, objetivo, restrições alimentares, experiência de treino, etc.) usando o recurso de Conversations do PTB.

    Processamento e Geração: Com base nas respostas, o bot processa as informações para criar uma sugestão de plano alimentar de 5 dias e um cronograma de treino.

    Geração de PDF: Utiliza a biblioteca FPDF para formatar e gerar um documento profissional e limpo contendo a dieta e o treino sugeridos.

    Entrega Automática: O PDF gerado é enviado diretamente ao usuário no chat do Telegram.

🛠️ Tecnologias Utilizadas

O projeto foi desenvolvido majoritariamente em Python, utilizando as seguintes bibliotecas principais:

    Python: Linguagem de programação.

    python-telegram-bot (PTB): Para a interface e lógica do bot, gerenciamento de comandos e estados de conversação.

    FPDF: Para a criação e formatação do arquivo PDF final.

🚀 Como Executar o Projeto

1. Pré-requisitos

    Python 3.13 instalado.

    Conta no Telegram e um Token de Bot (obtido via BotFather).

2. Instalação de Dependências

    Clone o repositório e instale as bibliotecas necessárias:

        git clone https://github.com/killuaxhunterx/BotTreinoDieta/tree/master
        
        cd botTreinoDieta
        
        pip install python-telegram-bot
        
        pip install fpdf
        
        pip install google-genai
        
        pip install dotenv

3. Configuração

    Substitua SEU_TOKEN_AQUI pelo seu token real do Telegram no seu arquivo principal (ex: bot.py):
    Python

        TOKEN = 'SEU_TOKEN_AQUI' 

4. Inicialização

    Execute o script principal do bot:

        python main.py

👨‍💻 Como Usar o Bot

    Inicie a Conversa: Procure o bot no Telegram e envie o comando de início:

        /start

    Inicie a Geração: Use o comando para começar a coleta de dados:

        /gerarPdf

    Responda às Perguntas: Siga as instruções e responda as perguntas sobre seus objetivos, saúde, dieta e rotina de treino.

    Receba o PDF: Após a coleta, o bot enviará o documento PDF personalizado com seu plano de 5 dias.

Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.
