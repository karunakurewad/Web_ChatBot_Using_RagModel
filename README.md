# Brainlox Course Search AI

This project is a **Streamlit application** that allows users to search for **technical courses** available on Brainlox. It uses **Google Gemini AI** for processing queries and **Pinecone** as a vector database for storing and retrieving course information.

---

## 🚀 Features
- **Retrieve technical course details** from Brainlox.
- **Embeds and indexes data** using Google Generative AI Embeddings.
- **Stores and searches efficiently** in Pinecone.
- **Streamlit UI** for easy interaction.

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/brainlox-course-search-ai.git
cd brainlox-course-search-ai
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a **.env** file in the project directory and add your API keys:
```ini
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENV=your_pinecone_environment
```

---

## 🔄 How to Run the Application
```bash
streamlit run app.py
```

This will launch the Streamlit web app in your browser.

---

## 📜 File Structure
```
📂 brainlox-course-search-ai
│── app.py                 # Main Streamlit application
│── requirements.txt       # Required dependencies
│── .env                   # API keys (not included in repo)
│── README.md              # Project documentation
```

---

## 🧑‍💻 Usage Guide
1. Open the application in the browser.
2. Type your **query** in the input box (e.g., *"What Python courses are available?"*).
3. Click on **Search**, and the AI will retrieve relevant courses.
4. The app displays **retrieved course details** and an **AI-generated summary**.

---

## 🛠️ Troubleshooting
- If you see **Missing API Keys!** ❌, check your **.env file**.
- If **no results are returned**, verify your **Pinecone index** and dataset.
- To retrieve **more results**, increase `search_kwargs={"k": 20}`.

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 🤝 Contributing
Pull requests are welcome! If you find an issue, feel free to open an issue or contribute fixes.

---

## 💡 Future Improvements
- Support for **more data sources**.
- **Improved ranking of search results**.
- **Better UI enhancements**.

---

### ⭐ Enjoy using Brainlox Course Search AI!










