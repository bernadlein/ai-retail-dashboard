# 🛍️ Retail Sales Dashboard - AI Engineer Portfolio

A professional Streamlit dashboard designed to analyze and visualize retail sales data, intended for showcasing data and AI engineering skills in real-time.

🔗 **Live Demo**: [Hugging Face Space](https://huggingface.co/spaces/bernadlein/ai-retail-dashboard)

---

## 📊 Features

* 📈 **Key Metrics:** Total Revenue, Average Order Value
* 📦 **Sales by Category:** Interactive bar chart by product type
* 🧃 **Sales by Product:** Top-selling products
* 📅 **Custom date range filtering** *(planned)*
* 🤖 **AI Forecasting Model** *(coming soon)*

---

## 🧱 Project Structure

```
├── app.py                  # Main Streamlit app
├── retail_sales.csv        # Retail sales dataset
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
```

---

## ⚙️ How to Run Locally

1. **Clone the Repository**

```bash
git clone https://github.com/bernadlein/ai-retail-dashboard.git
cd ai-retail-dashboard
```

2. **Install Requirements**

```bash
pip install -r requirements.txt
```

3. **Run Streamlit App**

```bash
streamlit run app.py
```

---

## 📈 Sample Data

Data used in this project simulates retail transactions with:

* Product Category
* Product Name
* Order Quantity & Revenue

---

## 🚀 Upcoming Enhancements

* [ ] Add Prophet/XGBoost model for forecasting sales per category
* [ ] Add `upload CSV` feature for custom data
* [ ] Export data/visuals to PDF or Excel
* [ ] Role-based view (admin vs. public)

---

## 🧑‍💻 Author

**Bernadus Boli**
AI & Data Engineer | Portfolio Project

---

## 🤝 License

MIT License — free for use, reuse, and remix.
