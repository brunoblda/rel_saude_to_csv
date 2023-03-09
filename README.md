# 1. Relatório de saúde suplementar to csv

Transforma os arquivos gerados no extrator (.REF e .TXT) em arquivo .csv com o cabeçalho embutido.

Transforma o relatório de documento texto gerado em um arquivo .csv com o cabeçalho embutido

As configurações de como ler o relatorio de servidores e de pensionistas se encontram nos arquivos serv_config.REF e pens_config_REF respectivamente.

Os valores em das percapitas sao convertidos de inteiro para float com as devidas casas decimais

## 1.1 Forma de utilização

Salvar o arquivo executavel na pasta que contem 1 relatório e os 2 arquivos de configuração e posteriormente clicar 2 vezes no arquivo para executa-lo.

O programa só realiza uma conversão por vez e precisa estar somente o programa, um arquivo do relatório na pasta e os dois arquivos de configuração.

Dessa forma, para o correto funcionamento do programa, apagar o relatório e o documento gerado da pasta, e somente colocar um documento quando for realizar a execucao do programa.

## 1.2 Requerimentos 

Os modulos utilizados se encontram no arquivo requirements.txt. (Realmente, no momento, o arquivo requirements esta vázio)

Foi utilizado o python 3.10.8.

## 1.3 Executável

Para gerar o executável foi utilizado o modulo pyinstaller versão 5.0.

Foi executado o commando no powershell como administrador:

``` Bash
pyinstaller --onefile --paths .\venv\Lib\site-packages main.py
```