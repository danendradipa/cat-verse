# CatVerse

CatVerse is a web application that identifies the breed of a cat from an uploaded image. Built using Flask and TensorFlow, this application leverages a pre-trained deep learning model to classify cat breeds with high accuracy.

## Features

- **Cat Breed Classification**: Upload an image of a cat, and the app will predict its breed.
- **Breed Details**: Provides detailed information about the predicted breed, including origin, personality, physical traits, and care tips.
- **Responsive Design**: User-friendly interface built with Tailwind CSS.

## Project Structure

```
cat-image-cnn/
├── app.py                # Main Flask application
├── detail_ras.py         # Contains detailed information about cat breeds
├── model/
│   └── cat_model.h5      # Pre-trained TensorFlow model for classification
├── static/
│   └── src/
│       └── input.css     # Tailwind CSS input file
├── templates/
│   ├── base.html         # Base HTML template
│   ├── classify.html     # Classification result page
│   └── index.html        # Home page
├── requirements.txt      # Python dependencies
├── tailwind.config.js    # Tailwind CSS configuration
├── vercel.json           # Vercel deployment configuration
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/danendradipa/cat-verse.git
   cd cat-image-cnn
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`.

## Dependencies

- Flask==3.1.0
- Jinja2==3.1.4
- Pillow==11.0.0
- TensorFlow==2.18.0

## Deployment

This project is configured for deployment on Vercel. The `vercel.json` file specifies the build and routing settings.

1. Install the Vercel CLI:

   ```bash
   npm install -g vercel
   ```

2. Deploy the application:
   ```bash
   vercel
   ```

## Usage

1. Navigate to the home page.
2. Upload an image of a cat.
3. View the predicted breed and detailed information.

## Technologies Used

- **Backend**: Flask, TensorFlow
- **Frontend**: Tailwind CSS, Jinja2 Templates
- **Deployment**: Vercel

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy identifying cat breeds with CatVerse!
