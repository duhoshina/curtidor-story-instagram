# Curtidor de Stories do Instagram

Um script para curtir automaticamente os stories de usuários do Instagram usando Selenium e ChromeDriver.

## Pré-requisitos
- Python (versão 3.6 ou superior)
- Selenium (`pip install selenium`)
- ChromeDriver

## Configuração
1. Clone ou baixe este repositório para sua máquina local.
2. No mesmo diretório do script, crie um arquivo chamado `seguidores.txt`. Este arquivo deve conter os nomes de usuário dos usuários do Instagram cujos stories você deseja curtir, com cada nome de usuário em uma nova linha.
3. Instale os requisitos com este comando:
```pip install -r requirements.txt```

## Uso
1. Abra um terminal ou prompt de comando e navegue até o diretório onde o script está localizado.
2. Execute o script usando o seguinte comando:
```python run.py```
3. O script solicitará que você insira seu nome de usuário e senha do Instagram. Digite as informações necessárias e pressione Enter.

O script começará a curtir os stories de cada usuário no arquivo `seguidores.txt`. Ele abrirá uma janela do Chrome e navegará automaticamente até o story de cada usuário. Se o usuário tiver um story, o script clicará no botão "Curtir". Se o usuário não tiver um story, o script passará para o próximo usuário.

O script removerá cada nome de usuário do arquivo `seguidores.txt` após curtir seu story.

Depois que o script terminar de ser executado, você pode verificar o terminal ou prompt de comando para mensagens de saída que indicam o status de cada ação (curtir um story ou falhar ao curtir um story).

## Personalização
Você pode personalizar o script conforme necessário. Por exemplo, você pode:
- Descomentar a linha `chrome_options.add_argument("--headless")` para executar o Chrome em modo headless (sem abrir uma janela do navegador visível).
- Modificar o código para curtir outros tipos de interações, como comentários ou curtidas de publicações.

## Aviso
Por favor, use este script com responsabilidade e respeite os termos de serviço do Instagram. A automação de interações no Instagram pode violar as políticas de uso da plataforma, portanto, use este script por sua própria conta e risco.
