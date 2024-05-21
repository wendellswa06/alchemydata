import json
def merge(inputfile: str):
    # Read the contents of the A.txt file
    with open(inputfile, 'r') as f:
        lines = f.readlines()

    # Create a dictionary to store the merged texts
    merged_texts = {}

    # Iterate through the lines and merge the texts
    for line in lines:
        data = json.loads(line.strip())
        file_name = data['file_name']
        text = data['text']
        
        if file_name in merged_texts:
            merged_texts[file_name] += ' ' + text
        else:
            merged_texts[file_name] = text

    # Write the merged texts to a new file
    with open("merged"+inputfile, 'w') as f:
        for file_name, text in merged_texts.items():
            f.write(f'{{"file_name": "{file_name}", "text": "{text}"}}\n')
if __name__ == '__main__':
    merge("metadata.jsonl")