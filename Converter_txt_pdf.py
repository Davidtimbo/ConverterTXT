import os
import textwrap
from fpdf import FPDF
import subprocess


# Comando cd
#change_dir_command = "cd /mnt/dpessoal/CONVERTE-TXT"

# Comando lftp
#lftp_command = """lftp 1.0.0.1 <<EOF
#cd /usr/areaspo02/
#mget *.txt
#bye
#EOF"""


# Definição de uma função para converter texto em PDF
def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.33
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm


    # Inicialização de um objeto PDF
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)   # Configuração de quebras automáticas de página
    pdf.add_page()                                           # Adiciona uma nova página ao PDF
    pdf.set_font(family='Courier', size=fontsize_pt)         # Define a fonte e o tamanho do texto

    first_at_symbol_encountered = False
    # Iteração sobre cada linha do texto
    for line in text.split('\n'):
        if not line.strip():  # Ignora linhas vazias
            continue
        elif "@#" in line and not first_at_symbol_encountered:
            first_at_symbol_encountered = True
            continue
        elif line.strip() == "@#":                           # Adiciona uma nova página ao encontrar a marcação "@#"
            pdf.add_page()
            continue

        lines = textwrap.wrap(line, width_text)              # Quebra a linha de acordo com a largura especificada

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)             # Adiciona uma célula de texto ao PDF

    pdf.output(filename, 'F')                                # Salva o PDF no arquivo especificado

# Diretório onde os arquivos .txt estão localizados
input_directory = '/mnt/dpessoal/CONVERTE-TXT'

# Diretório onde os arquivos PDF serão salvos
output_directory = '/mnt/consultores/PDFS'

# Loop através de todos os arquivos .txt no diretório
for filename in os.listdir(input_directory):
    if filename.endswith(".txt"):                                                                # Verifica se o arquivo é um arquivo .txt
        input_filepath = os.path.join(input_directory, filename)                                 # Caminho completo para o arquivo de entrada
        output_filename = os.path.splitext(filename)[0] + ".pdf"                                 # Nome do arquivo de saída
        output_filepath = os.path.join(output_directory, output_filename)                        # Caminho completo para o arquivo de saída
        with open(input_filepath, 'r') as file:                                                  # Abre o arquivo .txt para leitura
            text = file.read()                                                                   # Lê o conteúdo do arquivo .txt
            text_to_pdf(text, output_filepath)                                                   # Chama a função para converter o texto em PDF

