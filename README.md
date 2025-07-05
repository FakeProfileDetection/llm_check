# llm_check

This script uses an Ollama model to analyze and determine the relevance of text files from a specified folder to three key topics:

- **Coach Carter (2005 movie)**
- **The Oscars Slap (Will Smith and Chris Rock, 2022)**
- **The Trump–Zelenskyy White House Meeting (2022)**

The script reads `.txt` files, analyzes their content, and provides a relevance percentage for each of the three topics. It uses a small, performant Ollama model (like `mistral` or `llama2:7b-chat`) to evaluate the content.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Arguments](#arguments)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

Before you can use the script, you will need to install the necessary dependencies and set up Ollama.

### Prerequisites

1. **Ollama** - An AI model serving platform. You can download and install it [here](https://ollama.com).
2. **Python 3.8+** - Make sure Python is installed and available in your PATH.

### Install Dependencies

Clone this repository and install the required Python packages:

```bash
git clone https://github.com/FakeProfileDetection/llm_check.git
cd llm_check
ollama pull mistral
pip install -r requirements.txt
```

## Usage

The script requires a folder containing `.txt` files. It will analyze each file and output the relevance percentage for each topic.

### Command-line Usage

```bash
python llm_check.py <folder_path> [--model <model_name>]
```

- `<folder_path>`: Path to the folder containing .txt files you want to analyze.
- `[--model <model_name>]`: Optional argument specifying the Ollama model to use. Default is `mistral`

## Example Output

Here’s an example of what the output might look like:

```json
{
  "Coach Carter": 12,
  "Oscars Slap": 88,
  "Trump-Ukraine Meeting": 5
}
```

This means that the file has:

- 12% relevance to Coach Carter.
- 88% relevance to The Oscars slap.
- 5% relevance to the Trump–Zelenskyy White House meeting.
