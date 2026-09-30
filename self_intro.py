from flask import Flask
app=Flask(__name__)
@app.route("/")
def selfintro():
	return{"Result": "Hi, I’m Dhanu. I am currently pursuing my B.Tech in Artificial Intelligence and Data Science. I’m interested in Machine Learning, Data Analytics, and Generative AI. I have basic knowledge of Python, SQL, and Power BI. My goal is to improve my technical skills and build useful AI-based projects."}
