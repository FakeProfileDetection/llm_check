import os
import json
import argparse
import ollama
from typing import List


def get_txt_files(folder_path: str) -> List[str]:
    return [f for f in os.listdir(folder_path) if f.endswith(".txt")]


def read_file_content(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def build_prompt(text: str) -> str:
    return f"""
You are a helpful AI tasked with determining relevance.

Given the following text:

{text}

Rate on a scale from 0 to 100 how relevant this text is to each of the following topics:

1. Coach Carter (2005 movie)
2. The 2022 Oscars slap (Will Smith and Chris Rock)
3. The Trump–Zelenskyy White House meeting

Return your answer as JSON in the format:
{{
    "Coach Carter": <percentage>,
    "Oscars Slap": <percentage>,
    "Trump-Ukraine Meeting": <percentage>
}}
"""


def analyze_text(text: str, model: str = "mistral"):
    prompt = build_prompt(text[:1500])  # Truncate for speed
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    try:
        return json.loads(response["message"]["content"])
    except Exception as e:
        print("Error parsing response:", e)
        print("Raw response:", response["message"]["content"])
        return None


def main(folder_path: str, model: str = "mistral"):
    files = get_txt_files(folder_path)
    for filename in files:
        path = os.path.join(folder_path, filename)
        text = read_file_content(path)
        print(f"\nAnalyzing {filename}...")
        result = analyze_text(text, model=model)
        if result:
            print(json.dumps(result, indent=2))
        else:
            print("Could not determine relevance.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check text relevance to specific events."
    )
    parser.add_argument("folder", help="Folder containing .txt files")
    parser.add_argument(
        "--model", default="mistral", help="Ollama model to use (default: mistral)"
    )
    args = parser.parse_args()

    main(args.folder, model=args.model)
