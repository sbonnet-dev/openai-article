# AI Book Writer

This script is meant to assist in writing a book or article on a specific topic. It uses the OpenAI API to generate an outline for the book based on a given thematic and language. The user is then prompted to write an article using this outline, and the script generates the article using AI-generated paragraphs.

## Prerequisites

- Python 3.6 or above
- OpenAI API key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/your_repository
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the script, you need to set your OpenAI API key. Replace `ENTER_YOUR_OPENAI_KEY` in the script with your API key.

## Usage

Run the script using the following command:

```bash
python main.py
```

The script will ask for the language (French/English) and the article thematic. It will then generate an outline for the book based on the thematic and language, and prompt the user if they want to write an article using this outline.

If the user chooses to write the article, the script will generate paragraphs for each chapter in the outline and create a book/article using AI-generated content. The generated content will be written in the specified language and will include transitions between paragraphs.

Once the article is written, the script will use the `md2pdf` library to convert the markdown file into a PDF file named `article.pdf`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
