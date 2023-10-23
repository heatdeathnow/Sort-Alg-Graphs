from abc import ABC

DATA_DIR = 'data'
GRAPH_DIR = 'graphs'
WORKING_DIRECTORY = '__data_gathering_and_graphing'

def format_name(text: str, extension: str | None = None) -> str:
    if extension is None:
        return text.lower().strip().replace(' ', '_')
    
    else:
        return text.lower().strip().replace(' ', '_') + f'.{extension.replace('.', '')}'

# Funny function
# rows: list[list[int | float]] = list(map(lambda line: [row := line.split(';'), [0.0 if val in ' \n' else float(val) for val in row]][0], lines[1 :]))
