# Movie Genre Classification System

This project implements a comprehensive Movie Genre Classification system using Natural Language Processing (NLP) techniques. The system classifies movie descriptions into multiple genres such as Action, Drama, Comedy, Horror, Sci-Fi, Romance, and Thriller.

## 🎬 Movie Recommendations with Posters

The system includes a visual movie recommendation feature that displays similar movies with their posters loaded directly from the IMDB dataset.

## Academic NLP Concepts Implemented

### Unit 1: Introduction to NLP
- Text representation and preprocessing fundamentals
- Corpus linguistics concepts
- NLP pipeline architecture

### Unit 2: Text Preprocessing
- Tokenization using NLTK
- Stemming (Porter Stemmer)
- Lemmatization
- Stop word removal
- Text normalization

### Unit 3: Statistical Language Models
- N-gram features (Unigrams, Bigrams, Trigrams)
- Frequency distributions
- TF-IDF vectorization
- Bag-of-words vs N-gram performance comparison

### Unit 4: POS Tagging
- Part-of-speech tagging with NLTK
- POS pattern extraction as features
- Linguistic feature engineering

### Unit 5: Semantic Analysis
- Word sense disambiguation
- WordNet for semantic similarity
- Synonym/hypernym extraction as features

## Project Structure

```
movie-genre-classifier/
├── data/
│   ├── movies_dataset.csv
│   └── preprocessed_data.pkl
├── models/
│   ├── __init__.py
│   ├── preprocessor.py
│   ├── feature_extractor.py
│   ├── classifier.py
│   └── evaluator.py
├── notebooks/
│   └── analysis.ipynb
├── app/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── script.js
├── utils/
│   ├── data_loader.py
│   └── nlp_utils.py
├── requirements.txt
├── train.py
├── predict.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd movie-genre-classifier
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Download NLTK data:
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('averaged_perceptron_tagger'); nltk.download('vader_lexicon')"
   ```

## Usage

### Training the Models
```bash
python train.py
```

### Making Predictions
```bash
python predict.py "A group of astronauts travel through a wormhole in search of a new habitable planet."
```

### Running the Web Application
```bash
python app/app.py
```
Then open your browser to http://localhost:5000

## Model Performance

The system implements multiple classifiers for comparison:
- Multinomial Naive Bayes
- Bernoulli Naive Bayes
- Logistic Regression
- Random Forest

Evaluation metrics include:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion matrices
- Cross-validation scores

## Features

- Multi-label classification (movies can belong to multiple genres)
- Comprehensive text preprocessing pipeline
- Multiple feature extraction techniques (TF-IDF, N-grams, POS tags)
- Interactive web interface for real-time predictions
- **Movie recommendation system** with visual poster display from dataset
- Content-based recommendations using cosine similarity
- Hybrid recommendations combining genre and description similarity
- Movie posters and ratings loaded directly from IMDB dataset
- Detailed model evaluation and visualization
- Data preprocessing visualization