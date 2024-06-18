import cv2
from paddleocr import PPStructure
from paddleocr.ppstructure.recovery.recovery_to_doc import sorted_layout_boxes
import gradio as gr
import pandas
import csv

# Initialize the PPStructure engine
table_engine = PPStructure(recovery=True, lang='en')

def Download_CSV(file):
    df=pandas.read_html(file)
    filename="output.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(df[0].values)
def ocrwithpaddle(img):
    # Read the image using OpenCV
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert Gradio image to BGR format for OpenCV
    result = table_engine(img)

    # Remove image data from the result
    for line in result:
        if 'img' in line:
            line.pop('img')

    # Get image dimensions
    h, w, _ = img.shape

    # Sort layout boxes
    res = sorted_layout_boxes(result, w)

    # Extract HTML from the result
    html_result = res[1]['res']['html'] if len(res) > 1 else "No table detected"
    print(html_result)
    Download_CSV(html_result)
    return html_result


# Create and launch Gradio interface
gr.Interface(ocrwithpaddle, gr.Image(), gr.HTML()).launch()
