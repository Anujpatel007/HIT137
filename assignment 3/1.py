# Import necessary modules
import tkinter as tk  # tkinter for creating the GUI
from tkinter import filedialog, Label  # For file dialogs and labels in the GUI
from PIL import Image, ImageTk  # Image, ImageTK from PIL For image processing and display
import tensorflow as tf # Import TensorFlow for AI model processing
import time # Import time module for timing function execution


# Step 1: Create the main application class
class ImageClassifierApp(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the Tkinter parent class
        self.title("Image Classifier App")  # Set window title
        self.geometry("600x400")  # Set window size
        
        # Step 2: Add UI components
        self.label = Label(self, text="Upload an image to classify", font=("Arial", 16))  # Labeling for instructions that what should we need to do
        self.label.pack(pady=20)  # Add padding and display label 
        
        self.upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)  # it's a Button to upload an image
        self.upload_button.pack(pady=10)  # Add padding and display button
        
        self.result_label = Label(self, text="", font=("Arial", 12))  # it is a Label which is used for displaying the classification result
        self.result_label.pack(pady=20)  # Add padding and display result label
        
        self.image_label = Label(self)  # Label to display to uploaded the image
        self.image_label.pack(pady=10)  # Add padding and display image label

    # Encapsulation: it's a method to handle image file selection and display the image
    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])  # Open file dialog for image selection
        if file_path:  # If a file is selected
            img = Image.open(file_path)  # Open the selected image
            img = img.resize((250, 250))  # Resize the image for display
            img = ImageTk.PhotoImage(img)  # Converting image for Tkinter display
            self.image_label.config(image=img)  # Display the image in the GUI
            self.image_label.image = img  # Keep a reference to avoid garbage collection
            
            # Call AI model for classification (defined later)
            prediction = self.classify_image(file_path)  # Classify the image
            self.result_label.config(text=f"Prediction: {prediction}")  # Display the classification result

# Step 3: Define the model class for image classification
class ImageModel:
    def __init__(self):
        self.model = self.load_model()  # Load the AI model when class is initialized

    # Encapsulation: method to load the pre-trained AI model
    def load_model(self):
        # Load the pre-trained MobileNetV2 model for image classification with ImageNet weights
        model = tf.keras.applications.mobilenet_v2.MobileNetV2(weights='imagenet')
        return model  # Return the loaded model

    # Polymorphism: Generic method to classify an image file
    def classify_image(self, image_path):
        img = Image.open(image_path)  # the pathway to Open the image
        img = img.resize((224, 224))  # Resize the image to 224x224 (which is required by the model)
        img_array = tf.keras.preprocessing.image.img_to_array(img)  # Converting the image to array
        img_array = tf.expand_dims(img_array, axis=0)  # Add a batch dimension (which is also required by the model)
        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)  # and now Preprocessing the image array

        # Predict using the pre-trained model
        predictions = self.model.predict(img_array)  # Get the model's predictions
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0]  # Decode predictions
        return decoded_predictions[0][1]  # Return the predicted label (class name)

# Step 4: Multiple inheritance in the main class
class ImageClassifierApp(tk.Tk, ImageModel):
    def __init__(self):
        # Initialize both Tkinter (for GUI) and ImageModel (for AI)
        tk.Tk.__init__(self)
        ImageModel.__init__(self)

# Step 5: Define a decorator to time the classification process
def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the function being timed
        end_time = time.time()  # Record the end time
        print(f"Function {func.__name__} took {end_time - start_time} seconds")  # Print the time taken
        return result  # Return the function's result
    return wrapper  # Return the wrapper function

# Modify the classify_image method to include the decorator
class ImageModel:
    ...
    
    @log_time  # Decorator added to time the execution of the classify_image method
    def classify_image(self, image_path):
        ...

# Main application loop
if __name__ == "__main__":
    app = ImageClassifierApp()  # Instantiate the app
    app.mainloop()  # Start the Tkinter event loop to keep the app running
