
# Whatsapp Chat Analysis




![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/whatsapp-group-chat.jpg)


##  Description

This project provides a comprehensive analysis of WhatsApp chat data, utilizing a dataset from my hostel group's chat. By employing various data processing and visualization techniques, this tool offers insights into chat dynamics, participant behavior, and textual patterns.
## Table of contents:
1. [Overview](#overview)
1. [Features](#features)
2. [Data preprocessing](#Data-preprocessing)
3. [Statistical Analysis](#Statistical-Analysis)
4. [Visualization](#Visualization)
5. [Interactive Dashboard](#Interactive-Dashboard)
6. [Installation](#Installation)
7. [Usage](#Usage)
8. [Project Structure](#Project-Structure)
9. [Dependencies](#Dependencies)
10. [Contributing](#contributing)
11. [License](#license)
## Overview

The WhatsApp Chat Analyzer is an end-to-end project designed to analyze WhatsApp chat data, providing insights into participant behavior, chat activity trends, and textual patterns. It includes features like data preprocessing, statistical analysis, visualization, and sentiment analysis. The project utilizes Python libraries such as Pandas, Matplotlib, Seaborn, WordCloud, NLTK, and TextBlob, and offers an interactive dashboard built with Streamlit for easy exploration of the chat data. This tool is particularly useful for gaining a deeper understanding of communication dynamics within a WhatsApp group.


# Features
## Data preprocessing
* Cleaning: Remove unnecessary characters and structure the data for analysis.
* Formatting: Convert the raw chat data into a structured DataFrame. 
## Statistical Analysis

* Message Count: Calculate the total number of messages sent by each participant.
* Daily Activity: Analyze message activity on a daily basis.
* Weekly and Monthly Trends: Identify patterns in message frequency over weeks and months.
## Visualization

* Word Clouds: Generate visual representations of the most frequently used words.
* Emoji Analysis: Visualize emoji usage patterns.
* Sentiment Analysis: Classify messages into positive, negative, and neutral sentiments using NLP techniques
## Interactive Dashboard

* Streamlit App: An interactive web app for exploring chat data, built with Streamlit.

1. Main Dashboard:

![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/Interactive%20Dashboard/Picture1.png)

2. Sidebar: Browse whatsappchat.txt file and upload;

![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/Interactive%20Dashboard/Picture2.png)

3. Top Statistics graph:

![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/Interactive%20Dashboard/Picture3.png)

4. Number of total messages monthwise graph:

![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/Interactive%20Dashboard/Picture4.png)

5. Number of total messages daywise graph:

![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/Interactive%20Dashboard/Picture5.png)

6. Most busy day, month graph:

![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/Interactive%20Dashboard/Picture6.png)

7. Heatmap showing weekly activity WRT time:

![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/Interactive%20Dashboard/Picture7.png)

8. Most busy users graph with that dataframe:

![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/Interactive%20Dashboard/Picture8.png)

9. Wordcloud - most common words:

![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/Interactive%20Dashboard/Picture9.png)

10. Most common words ranking graph:

![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/Interactive%20Dashboard/Picture10.png)

11. Emoji analysis
![Logo](https://github.com/negativenagesh/Whatsapp_Chat_Analyzer/blob/main/Interactive%20Dashboard/Picture11.png)
## Installation (bash)

To set up and run this project locally, follow these steps:

1. Clone the Repository:
git clone https://github.com/negativenagesh/Whatsapp_Chat_Analyzer.git

2. Create a Conda Environment:
conda env create -f environment.yml

3. Activate the Environment:
conda activate whatsapp_chat_analyzer

4. Run the Streamlit App:
streamlit run app.py
## Usage

1. Upload Chat Data:
Export your WhatsApp chat as a text file and upload it through the app interface.

2. Explore Visualizations:
Navigate through different sections to explore message statistics, activity trends, word clouds, emoji usage, and sentiment analysis.
## project structure

* app.py: The main script to run the Streamlit app.

* preprocessor.py: Contains functions for data cleaning and preprocessing.

* helper.py: Utility functions for analysis, such as generating statistics and visualizations.
* environment.yml: Defines the Conda environment and dependencies.
* requirements.txt: Lists Python packages required for the project.
* data/: Directory to store sample chat data.
* output/: Directory to save generated visualizations.
* setup.sh: makes the setup process more user-friendly, reproducible, and reliable. for deployment (heroku)
* procfile: it is used to define the process that should be executed by the server to run the Streamlit application. Deployment--->The Procfile is crucial for deploying the app to platforms like Heroku, as it instructs the server on how to run the Streamlit app. Simplicity---> It simplifies the deployment process by providing a single file that specifies the startup command.
## Dependencies

* Streamlit: For building interactive web applications.

* Pandas: For data manipulation and analysis.
* Matplotlib and Seaborn: For data visualization.
* WordCloud: For generating word clouds.
* NLTK and TextBlob: For natural language processing and sentiment analysis.

many more.....
## Potential Implications

1. Personal and Group Insights

* Behavior Analysis: Understand individual and group behavior through message frequency and patterns.
* Sentiment Tracking: Gauge overall sentiment and mood changes over time, which can be useful for group dynamics and personal reflection.
* Activity Patterns: Identify peak activity times, helping in better coordination and communication planning.

2. Social Media Research

* Trend Analysis: Researchers can use the tool to study communication trends and social behaviors in digital interactions.
* Emoji Usage: Provides insights into emoji usage patterns, adding to research in digital communication and linguistics.
3. Educational Purposes

* Learning Tool: Acts as a practical example for students learning about data science, natural language processing, and visualization techniques.
* Project Blueprint: Serves as a template for similar projects involving text analysis and interactive dashboards.
4. Business Applications

* Customer Insights: Businesses can adapt the tool to analyze customer communication, improving customer service and product feedback.
* Team Communication: Helps businesses understand internal communication patterns, aiding in team management and improving productivity.
5. Privacy and Ethical Considerations
* Data Sensitivity: Highlights the importance of handling personal data responsibly, ensuring privacy and consent in data analysis.
* Ethical Use: Encourages discussions on ethical implications of analyzing personal and group communication data.
## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to fork the repository and submit a pull request.
## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) See the LICENSE file above for more details.
## Acknowledgments

Special thanks to my hostel friends for providing the chat data used in this analysis.
## Authors

- [Subrahmanya Gaonkar](https://www.linkedin.com/in/subrahmanya-gaonkar)
