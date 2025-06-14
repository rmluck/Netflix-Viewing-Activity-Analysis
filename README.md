# Netflix Viewing Activity Analysis

*By Rohan Mistry - Last updated June 13, 2025*

---

## 📖 Overview

This project is a web-based application that analyzes a user's Netflix viewing history by conducting statistical analysis using chosen filters and producing visualizations. This program provides meaningful long-term insights and trends to inform the user about their personal Netflix viewing habits which Netflix does not specifically provide themselves.

**Target Users** are anyone with access to their Netflix "ViewingActivity.csv" file who is curious about thier own watch patterns or wants to visualizes their habits.

🔗 **Try it live**: [netflix-viewing-activity-analysis.streamlit.app](https://netflix-viewing-activity-analysis.streamlit.app)

<br>

![](/static/img/streamlit_demo_application1.png)

![](/static/img/streamlit_demo_application2.png)

---

## 📁 Contents

```bash
├── .streamlit/          # Custom Streamlit theme configuration
├── data/                # Contains the time_zones.txt file and a sample viewing_activity.csv file
├── src/
│   └── viewing_activity_analysis.py   # Core data processing and visualization logic
├── web/
│   └── app.py           # Streamlit frontend app
├── LICENSE                # MIT License
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```

---

## 🌟 Features

* **File Upload**: Upload your __ViewingActivity.csv__ file exported from Netflix.
* **Time Zone Support**: Convert all timestamps to your selected time zone.
* **Profile Filter**: Choose between different user profiles on your account or All Profiles.
* **Content Type Filter**: Limit analysis to Movies, TV Shows, or All Content.
* **Title Filter**: Focus analysis on a specific title or All Titles.
* **Multiple Analyses**:
    * Countries
    * Device Types
    * Viewing Frequency
    * Viewing Activity Timeline
    * Viewing Heat Map
    * Most Watched Movies
    * Most Watched Shows
    * Most Watched Days
    * Most Watched Episodes
    * Duration
* **PNG Download**: Export any chart as an image.
* **Multi-Analysis Workflow**: Run multiple analyses and view them together.

---

## 🛠️ Installation Instructions

To run the app locally:
1. Clone the repository:
```bash
git clone https://github.com/rmluck/Netflix-Viewing-Activity-Analysis.git
cd Netflix-Viewing-Activity-Analysis
```
2. Set up a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Launch the app:
```bash
streamlit run web/app.py
```

To retrieve the .csv file containing the viewing activity data of your Netflix account, log into your Netflix account on your browser and go to the "[Get My Info](https://www.netflix.com/account/getmyinfo)" page and this page will appear:

![](/static/img/netflix_get_my_info_page.png)

Click the "Submit Request" button which will send a request to Netflix for your data. They will provide a downloadable report folder which contains various files, including one called __ViewingActivity.csv__. This is the file that contains the viewing activity data necessary for this program's input.

---

## 💡 Usage

### Sample Input File

### Upload File

### Analysis Output

---

## 🚧 Future Improvements

* Add the following analysis options: Most Watched Months, Start Times, Total Time Watched
* Dark mode support and advanced theme customization
* Session history saving
* Export filtered dataset (__st.download_button__ with __df.to_csv()__)
* Export all results in a zipped report format or as PDF (__matplotlib__ + __fpdf__ or __ReportLab__)
* Test with multiple real Netflix files (different formats, languages, profiles, etc.)
* Handle missing or malformed data more gracefully
* Add logging for errors or corner cases
* Unit test functions with __pytest__
* Combine multiple profiles or titles into a merged view
* Persistent dashboard layout
* Filter by date range (__st.date_input__ or __st.slider__) or time of day
* Search titles (__st.text_input__ and fuzzy matching)

---

## 🧰 Tech Stack

* Python
* **Frontend**: [Streamlit](https://streamlit.io/)
* **Data Analysis**: __pandas__, __numpy__
* **Visualization**: __matplotlib__, __seaborn__
* **Deployment**: Streamlit Community Cloud

## 🙏 Contributions / Acknowledgements

This project was built independently as a portfolio project. Inspired by the growing need to visualize personal data in an engaging and intellectually stimulating way.

## 🪪 License

This project is licensed under the [MIT License](/LICENSE)