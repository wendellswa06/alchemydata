import json
from openai import OpenAI

def converter(inputfile: str):
    text = "A very clean and well decorated empty bathroom A blue and white bathroom with butterfly themed wall tiles. A bathroom with a border of butterflies and blue paint on the walls above it. An angled view of a beautifully decorated bathroom. A clock that blends in with the wall hangs in a bathroom."
        
    openai_client = OpenAI(api_key="")
    model = "gpt-4"
    
    with open(inputfile, 'r') as f:
        lines = f.readlines()

    # Create a dictionary to store the merged texts
    converted_texts = {}

    # Iterate through the lines and merge the texts
    for i, line in enumerate(lines):
        print(f"NOTE: {i}")
        data = json.loads(line.strip())
        file_name = data['file_name']
        text = data['text']
        prompt = f"You are an image prompt generator. Your purpose is to convert {text} into a single one sentence prompt that can be fed into Dalle-3."
        response = openai_client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": prompt,
                },
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        response = response.choices[0].message.content    
        converted_texts[file_name] = response
    # Write the merged texts to a new file
    with open("converted"+inputfile, 'w') as f:
        for file_name, text in converted_texts.items():
            f.write(f'{{"file_name": "{file_name}", "text": "{text}"}}\n')
    
    
    
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
    # converter("test_merged.txt")