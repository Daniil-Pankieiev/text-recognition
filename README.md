# Email Extractor from Images
This Python script utilizes the EasyOCR library to extract email addresses from images. It offers two modes of operation: one where the user provides the input and output file paths interactively in the terminal, and another where these paths are provided as command-line arguments. In both modes, the script extracts email addresses from the specified image and writes them to the specified output file. If no email addresses are found, it notifies the user accordingly.
## Getting Started

### Prerequisites
- Python 3.10 or higher

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Daniil-Pankieiev/text-recognition.git
```
2. Create and activate the virtual environment:

On macOS and Linux:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
On Windows:
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
3. Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

4. Copy .env.sample to .env and populate it with all required data.

5. Run the bot:

On macOS and Linux:
```bash
python3 recognition.py
```
OR
```bash
python3 recognition_arguments.py -i input_image.jpg -o output_file.txt
```

On Windows:
```bash
python recognition.py
```
OR
```bash
python recognition_arguments.py -i input_image.jpg -o output_file.txt
```
## Contributing
Feel free to contribute to these enhancements, and let's make our Telegram Bot even better!
## Conclusion

Thank you for using the Text Recognition! 