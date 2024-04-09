# Programas de Conversão de Arquivos TXT para PDF (atualizado para quebrar página)

### Resumo 
- Este repositório contém dois programas principais: um script ```Bash``` e um script ```Python```. Ambos trabalham em conjunto para baixar arquivos de texto de um servidor remoto, converter esses arquivos de texto em PDFs e, em seguida, remover os arquivos de texto originais.


### Observações 
- Este conjunto de scripts foi desenvolvido para substituir uma versão anterior que não atendia adequadamente à necessidade de quebra de página. Ao contrário do seu antecessor, este script permite a quebra 
de página a cada ocorrência do marcador ```" @# "``` nos arquivos .txt, conforme acordado entre mim e meu colega que trabalha com Cobol. A principal razão para a criação deste novo script foi garantir essa 
funcionalidade de quebra de página, uma vez que o anterior não a fornecia de maneira satisfatória. Caso contrário, continuaríamos a usar o script anterior (convert.sh) onde já tinha um programa em python
desenvolvido.


### Pré-requisitos
- Certifique-se de que os seguintes requisitos estejam atendidos antes de executar os scripts:

- Sistema operacional Linux.
- Ferramenta lftp instalada para manipulação de arquivos remotos.
- Python 3 instalado no sistema.
- Biblioteca Python fpdf instalada. Você pode instalar usando o seguinte comando:
- Copy code
- pip install fpdf
- Funcionamento

  
## Script Bash
O script Bash faz o seguinte:

- Navega para o diretório ```/mnt/dpessoal/CONVERTE-TXT.```
- Baixa todos os arquivos .txt do diretório ```/usr/areaspo02/consultores/``` no servidor ```1.0.0.1``` usando ```lftp``` e os salva no diretório ```/mnt/dpessoal/CONVERTE-TXT```.
- Remove os arquivos .txt do servidor após o download.
- Altera as permissões dos arquivos ```.txt``` baixados para 777.
- Executa o script Python ```Converter_txt_pdf.py``` localizado em ```/home/crase/converte/```.
- Altera as permissões dos arquivos ```.pdf``` convertidos para 777.
- Remove todos os arquivos .txt do diretório ```/mnt/dpessoal/CONVERTE-TXT``` após a conversão.  


## Script Python
O script Python ```Converter_txt_pdf.py``` faz o seguinte:

- Define uma função ```text_to_pdf``` que converte texto em um arquivo PDF. Esta função leva dois argumentos: o texto a ser convertido e o nome do arquivo PDF de saída.
- Define os diretórios de entrada e saída para os arquivos ```.txt``` e ```.pdf```, respectivamente.
- Itera sobre todos os arquivos ```.txt``` no diretório de entrada.
- Para cada arquivo ```.txt```, lê o conteúdo do arquivo, converte o texto em PDF usando a função ```text_to_pdf``` e salva o PDF no diretório de saída.



### Uso
- Para usar esses scripts, você precisará ter bash, lftp e python3 instalados em seu sistema. Além disso, o script Python requer o pacote fpdf para criar arquivos PDF.

- Para executar o script Bash, navegue até o diretório que contém o script e use o seguinte comando:
- ```./nome_do_script.sh```

- Substitua nome_do_script.sh pelo nome do seu script Bash.
- O script Python será chamado pelo script Bash, então não é necessário executá-lo separadamente.

Ou executar no crontab:
- ```30 22 * * 1-5 root /home/crase/converte/limparPDFS.sh```
- ```*/1 8-20 * * 1-5 root /home/crase/converte/converterTxt.sh```



### Notas
- Os scripts assumem que você tem permissões adequadas para ler e escrever nos diretórios especificados e para executar os comandos listados. Se você encontrar problemas de permissão, pode ser necessário alterar as permissões dos diretórios ou arquivos relevantes ou executar os scripts como superusuário.

- Além disso, o script Bash está configurado para remover os arquivos .txt originais após a conversão em PDF. Se você deseja manter os arquivos .txt originais, pode comentar ou remover a linha rm /mnt/dpessoal/CONVERTE-TXT/*.txt.

- Por fim, observe que o script Python está configurado para adicionar uma nova página ao PDF sempre que encontra a marcação “@#” no texto. Se você não deseja esse comportamento, pode comentar ou remover a linha relevante no script Python.
