# Data Analysis on LinkedIn Profiles of ENSIAS Students
This project involves using web scraping techniques to collect LinkedIn profile information from 58 students of ENSIAS. The collected data is then stored in a JSON file and fed into a database. Using Python, the data is analyzed to uncover relevant trends and insights about the skills and experiences of ENSIAS students. The analysis aims to improve educational programs and career opportunities for students. The project includes a sample JSON data model, Python code for web scraping, a PDF analysis report, and a Jupyter notebook for data analysis.
# Introduction
This project involves using web scraping techniques to collect LinkedIn profile information from 58 students of ENSIAS. We will then create a JSON file to store this data and feed it into a MongoDB database. Using Python, we will then conduct a data analysis on the collected information in order to uncover relevant trends and insights. This analysis will help us to better understand the skills and experiences of ENSIAS students, and can be used to improve educational programs and career opportunities.

# Data Collection
The data collection process is done using web scraping techniques. We used the library Selenium and BeautifulSoup to extract the relevant information from the students' LinkedIn profiles. The information collected includes the students' work experience, education, skills, and endorsements.

# Data Storage
The data collected is stored in a JSON file, which is then imported into a MongoDB database. This allows for easy access and manipulation of the data for the analysis process.

# Data Analysis
**The data analysis is done using the Python programming language and the PyMongo library for interacting with the MongoDB database. The following are some of the questions that the data analysis aims to answer** :

- What are the most common skills among ENSIAS students?
- How many students have experience in data science?
- What are the most common technologies used by students with data science experience?
- What is the average and maximum number of years of experience in data science?
- How many students have a degree in data science?
- How many students have experience with both Python and R?
- Is there a correlation between the number of years of study and employability?
- Is there a correlation between academic background and job mobility?
- What are the top companies that have hired ENSIAS students?

### The files included in the GitHub repository are:

- **A sample JSON file of the data (as sharing actual data would be illegal)**
- **The Python code for web scraping using Selenium and BeautifulSoup (bs4)**
- **A PDF document detailing the data analysis and its results**
- **A Jupyter notebook file containing the data analysis code and its outputs**
# Conclusion
The data analysis performed on the LinkedIn profiles of ENSIAS students has provided valuable insights into the skills and experiences of these students. By using Python and MongoDB, we were able to uncover trends and patterns in the data, such as the most popular skills among students and the average number of years of experience.

The results of this analysis can be used to improve educational programs and career opportunities for ENSIAS students. For example, we can use the data to identify the skills that are in high demand in the job market, and incorporate them into the curriculum. Additionally, we can use the data to provide career guidance and support to students, by helping them to identify the skills and experiences that are most likely to lead to successful job placements.

Overall, this project has demonstrated the power of data analysis to uncover valuable insights from LinkedIn profile data. We hope that this project will serve as a useful resource for ENSIAS students, educators, and career counselors, and that it will inspire future research in this area
# References and Additional Resources

- "Web Scraping with Python and Selenium" by Michael Herman, available at https://www.michael Herman.com/web-scraping-with-python-and-selenium/
- "Beautiful Soup Documentation" available at https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- "MongoDB Python Driver" available at https://api.mongodb.com/python/current/
- "Pandas" available at https://pandas.pydata.org/
- "Matplotlib" available at https://matplotlib.org/
- "Seaborn" available at https://seaborn.pydata.org/
Note: Selenium, Beautiful Soup, Pandas, Matplotlib and Seaborn are all popular Python libraries used for web scraping, data analysis, and data visualization. MongoDB is a popular NoSQL database
