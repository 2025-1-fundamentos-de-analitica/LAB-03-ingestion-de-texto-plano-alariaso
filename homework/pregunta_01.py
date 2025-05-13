"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import pandas as pd

# pylint: disable=import-outside-toplevel


def clean_header(header):
    return header.lower().replace(" ", "_")


def clean_word(word):
    return ' '.join(filter(lambda x: x != '', word.split(" ")))


def clean_words(words_str):
    return ', '.join(map(clean_word, words_str.split(",")))


def parse_percentage(percentage: str):
    s = percentage.removesuffix(" %")
    s = s.replace(",", ".")
    return float(s)


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    widths = [9, 16, 16]
    headers = [[], [], [], []]
    rows = []


    with open("files/input/clusters_report.txt") as f:
        lines = iter(f.readlines())

        # Obtener la cabecera
        for _ in range(2):
            line = next(lines).rstrip()
            i = 0
            j = 0
            for width in widths:
                headers[j].append(line[i:i+width].strip())
                j+=1
                i+=width
            headers[j].append(line[i:].strip())
        headers = list(map(lambda x: ' '.join(x).strip(), headers))

        # ignorar linea vacía
        next(lines)

        # ignorar separador
        next(lines)

        # Obtener las filas
        while (line := next(lines, None)) is not None:
            i = 0
            j = 0
            row = []
            for width in widths:
                row.append(line[i:i+width].strip())
                j += 1
                i+=width
            row.append(line[i:].strip())

            row[-1] = clean_words(row[-1]).strip()

            if row[0] == '':
                if row[-1] == '':
                    continue
                rows[-1][-1] += " " + row[-1]
            else:
                row[0] = int(row[0])
                row[1] = int(row[1])
                row[2] = parse_percentage(row[2])
                rows.append(row)

    headers = list(map(clean_header, headers))

    for row in rows:
        row[-1] = row[-1].removesuffix(".")

    return pd.DataFrame(rows, columns=headers)
