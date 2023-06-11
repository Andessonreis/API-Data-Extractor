# API Data Extractor

Este é um simples script em Python que extrai dados de uma API e os salva em um arquivo CSV.

## Pré-requisitos

Antes de executar o script, certifique-se de ter os seguintes requisitos:

- Python 3 instalado
- Pacotes `requests` e `csv` instalados. Você pode instalá-los executando o seguinte comando:
  ```
  pip install requests csv
  ```

## Como usar

Siga as etapas abaixo para usar o script:

1. Clone o repositório do GitHub:
   ```
   git clone https://github.com/Andessonreis/API-Data-Extractor.git
   ```

2. Navegue até o diretório do projeto:
   ```
   cd API-Data-Extractor
   ```

3. Execute o script fornecendo a URL da API quando solicitado:
   ```
   python extractor.py
   ```

4. O script solicitará que você insira a URL da API. Digite a URL e pressione Enter.

   Exemplo de URL: `https://api.spacexdata.com/v3/missions`

5. Aguarde enquanto o script faz a chamada para a API, extrai os dados e os salva em um arquivo CSV chamado `data.csv`.

6. Após a conclusão, você verá uma mensagem indicando se a extração dos dados foi bem-sucedida ou não.

## Licença

Este projeto está licenciado nos termos da Licença MIT. Consulte o arquivo [LICENSE](https://github.com/Andessonreis/API-Data-Extractor/blob/main/LICENSE) para obter mais informações.

## Contribuições

Contribuições são bem-vindas! Se você deseja contribuir para este projeto, siga as etapas abaixo:

1. Faça um fork deste repositório.

2. Crie um branch para sua nova funcionalidade ou correção de bug:
   ```
   git checkout -b minha-nova-funcionalidade
   ```

3. Faça suas alterações e adicione commits descrevendo as mudanças realizadas:
   ```
   git commit -m "Adiciona nova funcionalidade: minha nova funcionalidade"
   ```

4. Envie seu branch para o repositório remoto:
   ```
   git push origin minha-nova-funcionalidade
   ```

5. Abra um Pull Request no repositório original.

Agradecemos antecipadamente suas contribuições!

## Observação

Este script é fornecido como uma solução simples para extrair dados de uma API e salvá-los em um arquivo CSV. Você pode personalizá-lo e adicionar recursos adicionais de acordo com suas necessidades específicas.