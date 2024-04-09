#!/bin/bash

#Ativação do modo de depuração (descomente para ativar)
#set -x

# Definição de um sinal de armadilha para o evento DEBUG (descomente para ativar)
#trap read DEBUG

# Entrando no diretorio para baixar do lftp para o converte-txt
cd /mnt/dpessoal/CONVERTE-TXT

#Downloads de arquivos 'TXT' para o diretorio "/opt/transmissao/dpessoal/CONVERTE-TXT/"
lftp 1.0.0.1 <<EOF
cd /usr/areaspo02/consultores/
mget *.txt
mrm *.txt
bye
EOF

# Permissao no diretorio '/opt/transmissao/dpessoal/CONVERTE-TXT/'.
chmod 777 /mnt/dpessoal/CONVERTE-TXT/*.txt

# Navega para o diretório onde os arquivos estão localizados
#cd /home/crase/converterTeste
cd /mnt/dpessoal/CONVERTE-TXT


python3 /home/crase/converte/Converter_txt_pdf.py


#Define as permissões do arquivo PDF para 777
chmod 777 /mnt/consultores/PDFS/*.pdf


#Remove todos os arquivos .txt no diretório após a conversão (descomente para ativar)
rm /mnt/dpessoal/CONVERTE-TXT/*.txt



trap "" DEBUG

