import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image, ImageTk

# Step 1: Create the main application class
class ImageClassifierApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Classifier App")
        self.geometry("600x400")
        
        # Step 2: Add UI components
        self.label = Label(self, text="Upload an image to classify", font=("Arial", 16))
        self.label.pack(pady=20)
        
        self.upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)
        
        self.result_label = Label(self, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)
        
        self.image_label = Label(self)
        self.image_label.pack(pady=10)

    # Encapsulation: upload_image method to handle file selection and display
    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
        if file_path:
            img = Image.open(file_path)
            img = img.resize((250, 250))  # Resize image
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img  # Keep reference to avoid garbage collection
            
            # Call AI model for classification (defined later)
            prediction = self.classify_image(file_path)
            self.result_label.config(text=f"Prediction: {prediction}")
