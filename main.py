# Libraries
import tkinter as tk
from tkinter import filedialog, messagebox
import pyttsx3
import PyPDF2

# Function to upload PDF file
def upload_pdf():
    print("upload pdf function")
    global pdf_path
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]) 
    if pdf_path:
        read_pdf() 
    else:
        return

# Function to read the PDF file
def read_pdf():
    print("read pdf function")
    if not pdf_path:
        return
    
    try:
        with open(pdf_path, 'rb') as book:  # --> Read mode binary <--
            reader = PyPDF2.PdfReader(book)
            audio_reader = pyttsx3.init()  # --> Init pyttsx3 as the reader <--
            audio_reader.setProperty("rate", 150)  # --> Speed <--
            audio_reader.setProperty("volume", 1)  # --> Volume <--

            for page_number in range(len(reader.pages)):  # --> Loop through PDF pages <--
                next_page = reader.pages[page_number]
                content = next_page.extract_text()  # --> Extract text from PDF page <--

                if content:
                    audio_reader.say(content)  # --> Read content aloud <--
                    audio_reader.runAndWait()  # --> Wait until it finishes speaking <--
                else:
                    print("No content found")  # --> Print if no content found <--
    except Exception as e:
        print(f"Error: {e}")  # --> Print any exception encountered <--

# Create main window
window = tk.Tk()
window.title("PDF Reader")
window.geometry("400x300") 

# Create text/button
label = tk.Label(window, text="Upload a PDF file:")
label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)  

upload_button = tk.Button(window, text="Upload PDF", command=upload_pdf)
upload_button.grid(row=1, column=0, columnspan=2, padx=20, pady=10) 

# Configure grid to allow widgets to expand evenly
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Start the loop
window.mainloop()