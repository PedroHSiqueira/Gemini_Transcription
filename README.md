# Ollama Chatbot

## Instruções

Este projeto é um Porgrama de transcrição de imagens em python usando a Gemini AI. Siga as instruções abaixo para configurar e executar o projeto em seu computador.

### Pré-requisitos

- Python 3.x
- Gemini Api Key
- Git

### Passos para Configuração

1. Clone o repositório para o seu computador:
    ```bash
    git clone https://github.com/PedroHSiqueira/Gemini_Transcription
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd Gemini_Transcription
    ```
3. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```
4. Adicione a foto no codígo fonte e altere genai.upload_file :
    ```bash
    "parts": [genai.upload_file("images.jpeg", mime_type="image/jpeg")],
    ```

### Executando o Chatbot

Para iniciar o programa, execute o seguinte comando:
```bash
python transcription.py
```

### Contribuições

Sinta-se à vontade para contribuir com o projeto. Para isso, faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

### Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
