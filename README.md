# 🎬 Film Concierge

**Your taste. Your next favourite movie.**

Film Concierge is a content-based movie recommendation system built with Python and Streamlit. Pick three movies you enjoy and get five personalised recommendations.

The app uses TF-IDF vectorisation and cosine similarity to analyse movie genres and find movies with similar characteristics.

## ✨ Features

- **Personalised Recommendations:** Select three movies to discover five similar ones.
- **Equal Movie Weighting:** All three selected movies contribute equally to the recommendation process.
- **Content-Based Filtering:** Uses movie genres to measure similarity between movies.
- **Cinematic UI:** Dark, Netflix-inspired theme with red accents, hover effects, and staggered card reveal animations.
- **Duplicate Selection Validation:** Makes sure you select three different movies.

## 🧠 How It Works

Film Concierge uses a content-based filtering approach.

1. **Dataset Processing:** Movie information is loaded and cleaned.
2. **Text Processing:** Movie genres are prepared for vectorisation.
3. **TF-IDF Vectorisation:** Genre information is converted into numerical feature vectors using Term Frequency-Inverse Document Frequency.
4. **Similarity Calculation:** Cosine similarity measures how closely movies match each other.
5. **Recommendation Generation:** The preferences represented by the three selected movies are combined, and the five most relevant movies are returned.

### Recommendation Pipeline

```text
User selects 3 movies
        ↓
Movie genres are extracted
        ↓
TF-IDF feature representation
        ↓
Cosine similarity calculation
        ↓
Combined preference scoring
        ↓
Top 5 movie recommendations
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Dataset handling and preprocessing |
| Scikit-learn | TF-IDF vectorisation and cosine similarity |
| Streamlit | Interactive web application |
| HTML / CSS | Custom interface elements, styling, and animations |

## 📂 Project Structure

```text
movie-recommender/
│
├── app.py              # Streamlit application and user interface
├── train.py            # Data processing and recommendation logic
├── movies.csv          # Movie dataset
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/abhinavspillai7-web/movie-recommender.git
```

### 2. Navigate to the project directory

```bash
cd movie-recommender
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

## 🎯 How to Use

1. Open Film Concierge.
2. Select your first movie.
3. Select your second movie.
4. Select your third movie.
5. Click **Get Recommendation**.
6. Explore your five recommended movies.

**Note:** All three selected movies must be different.

## 📊 Dataset

The project uses a movie dataset containing movie IDs, titles, and genres.

The dataset is preprocessed to remove entries without meaningful genre information before the recommendation process.

## 🔮 Future Improvements

- Incorporate movie descriptions and keywords.
- Add ratings and popularity information.
- Improve recommendation diversity.
- Integrate movie posters and additional movie details.
- Let users save their favourite recommendations.
- Deploy the application for public access.

## 👨‍💻 Author

**Abhinav**

GitHub: [abhinavspillai7-web](https://github.com/abhinavspillai7-web)

Built as an AI/ML portfolio project to explore content-based recommendation systems, natural language processing techniques, and interactive machine learning applications.

---

*Discover movies that match your taste with Film Concierge.*
