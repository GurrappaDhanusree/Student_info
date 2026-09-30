from flask import Flask
app=Flask(__name__)
@app.route("/")
def internship():
	return{"Result": "I recently completed an internship in Data Analytics using Power BI at Innovation Tech Tree. During my internship, I worked on a Travel and Tourism Preferences Survey project. I collected and analyzed survey data, cleaned and transformed the data using Power Query, and created interactive dashboards and visualizations using Power BI. This internship helped me gain practical knowledge of data analysis and data visualization."}
