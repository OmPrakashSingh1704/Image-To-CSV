# OCR Table Detection with PaddleOCR and Gradio

This project demonstrates the use of the PaddleOCR's PPStructure engine to detect and extract tables from images. The extracted table is converted to an HTML format and saved as a CSV file.

## Features
- Uses PaddleOCR's PPStructure engine for table detection and extraction.
- Converts the detected table into HTML format.
- Saves the extracted table data into a CSV file.
- Simple and user-friendly Gradio interface for uploading images and displaying HTML output.

## Dependencies
To run this project, you need the following Python libraries installed:
- `opencv-python`
- `paddleocr`
- `gradio`
- `pandas`

You can install the dependencies using the following command:
```bash
pip install opencv-python paddlepaddle paddleocr gradio pandas
```

## How It Works
1. The image containing a table is uploaded through a Gradio interface.
2. PaddleOCR's PPStructure engine processes the image to detect tables.
3. The detected table is converted to an HTML format.
4. The HTML result is displayed in the Gradio interface.
5. The extracted table data is saved as a CSV file.

## File Structure
- `main.py`: The main script containing the OCR pipeline and Gradio interface.
- `README.md`: This file providing project information.
- `output.csv`: The CSV file where the table data is saved.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/OmPrakashSingh1704/Image-To-CSV/
   ```
2. Navigate to the project directory:
   ```bash
   cd Image-to-CSV
   ```
3. Run the script:
   ```bash
   python main.py
   ```
4. Open the Gradio interface in your browser, upload an image, and view the extracted table data.

## Example
Upload an image of a table through the Gradio interface, and the table data will be displayed as HTML and saved in `output.csv`.

## Acknowledgements
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) for the OCR engine.
- [Gradio](https://www.gradio.app/) for the web interface.
