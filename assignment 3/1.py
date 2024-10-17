import tkinter as tk  # Import Tkinter for GUI
from tkinter import filedialog, Label  # Import filedialog to allow file selection, Label for UI text
from PIL import Image, ImageTk  # Import Pillow to handle image processing and display
import tensorflow as tf  # Import TensorFlow for using pre-trained AI models
import time  # Import time to measure execution time

# Step 1: Define a decorator to log the time taken for classification
def log_time(func):
    """
    This decorator measures and logs the time taken by the classify_image method.
    It's applied to the classify_image method to keep track of how long the model takes to make a prediction.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start timer
        result = func(*args, **kwargs)  # Call the wrapped function
        end_time = time.time()  # End timer
        print(f"Function {func.__name__} took {end_time - start_time:.2f} seconds")  # Log time taken
        return result  # Return the result of the function
    return wrapper

# Step 2: Define the AI model class (for Image Classification)
class ImageModel:
    """
    This class handles the loading and running of the AI model (MobileNetV2).
    Encapsulation is used to hide the details of loading the model and classifying images.
    """
    def __init__(self):
        # Initialize the model by calling the load_model method
        self.model = self.load_model()

    # Encapsulation: Method to load the AI model
    def load_model(self):
        """
        Load the pre-trained MobileNetV2 model from TensorFlow with ImageNet weights.
        This model will be used to classify images.
        """
        print("Loading MobileNetV2 model...")  # Inform user that model is being loaded
        model = tf.keras.applications.mobilenet_v2.MobileNetV2(weights='imagenet')  # Load model with ImageNet weights
        print("Model loaded successfully.")  # Confirmation message
        return model  # Return the loaded model

    # Polymorphism: Method to classify any image file
    @log_time  # Decorator to log time for classification process
    def classify_image(self, image_path):
        """
        Preprocess the image and classify it using the MobileNetV2 model.
        The method works polymorphically for any image input, classifying them the same way.
        """
        # Load and preprocess the image to match the input format required by MobileNetV2
        img = Image.open(image_path)  # Open the image from the provided path
        img = img.resize((224, 224))  # Resize the image to 224x224 pixels (MobileNetV2 input size)
        img_array = tf.keras.preprocessing.image.img_to_array(img)  # Convert the image to a numpy array
        img_array = tf.expand_dims(img_array, axis=0)  # Add batch dimension (expected input format)
        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)  # Preprocess input for the model

        # Predict using the MobileNetV2 model
        predictions = self.model.predict(img_array)  # Perform prediction on the preprocessed image
        # Decode predictions to get human-readable labels (top 1 prediction)
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0]
        return decoded_predictions[0][1]  # Return the predicted label (e.g., "Golden Retriever")

# Step 3: Define the main Tkinter application class
class ImageClassifierApp(tk.Tk, ImageModel):
    """
    This class combines the functionality of the Tkinter GUI and the ImageModel for image classification.
    It uses multiple inheritance to combine Tkinter (for the GUI) and ImageModel (for the AI).
    """
    def __init__(self):
        # Initialize both Tkinter's root window and the AI model
        tk.Tk.__init__(self)  # Initialize the Tkinter window
        ImageModel.__init__(self)  # Initialize the AI model (MobileNetV2)

        # Set up the window title and size
        self.title("Image Classifier App")  # Set the window title
        self.geometry("600x500")  # Set window dimensions

        # Step 4: Add UI components
        # Label to instruct the user
        self.label = Label(self, text="Upload an image to classify", font=("Arial", 16))
        self.label.pack(pady=20)  # Add padding for spacing

        # Button to upload image
        self.upload_button = tk.Button(self, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)  # Add padding for spacing

        # Label to display the classification result
        self.result_label = Label(self, text="", font=("Arial", 12))  # Initially empty
        self.result_label.pack(pady=20)  # Add padding for spacing

        # Label to display the uploaded image
        self.image_label = Label(self)  # Initially empty
        self.image_label.pack(pady=10)  # Add padding for spacing

    # Encapsulation: Method to handle image upload and display
    def upload_image(self):
        """
        This method allows the user to select an image file from the system.
        It then displays the image in the GUI and passes it to the AI model for classification.
        """
        # Open file dialog to select image file
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])  # Open dialog to select image
        if file_path:
            # Display the selected image
            img = Image.open(file_path)  # Open the image
            img = img.resize((250, 250))  # Resize the image for display
            img = ImageTk.PhotoImage(img)  # Convert the image to a format usable by Tkinter
            self.image_label.config(image=img)  # Set the image in the label
            self.image_label.image = img  # Keep reference to avoid garbage collection

            # Call AI model to classify the image and update the result label
            prediction = self.classify_image(file_path)  # Get the predicted label
            self.result_label.config(text=f"Prediction: {prediction}")  # Display the result

    # Method overriding: Custom quit method to print a message before exiting
    def quit(self):
        """
        This method overrides the default Tkinter quit method.
        It adds a custom message before calling the original quit method.
        """
        print("Exiting the application...")  # Print message when the user closes the app
        super().quit()  # Call the original Tkinter quit method to close the application

# Step 5: Run the application
if __name__ == "__main__":
    """
    This block runs the Tkinter event loop to start the application.
    """
    app = ImageClassifierApp()  # Instantiate the app
    app.mainloop()  # Start the main loop to keep the app running
