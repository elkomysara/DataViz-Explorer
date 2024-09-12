from flask import Blueprint, render_template, request, jsonify
import pandas as pd
import plotly.express as px

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_data():
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    df = pd.read_csv(file)
    df.to_csv('data/uploaded_data.csv', index=False)
    
    return jsonify({"message": "File uploaded successfully"})

@main.route('/visualize', methods=['GET'])
def visualize_data():
    df = pd.read_csv('data/uploaded_data.csv')
    fig = px.line(df, x='Date', y='Value')  # Replace with actual columns from your dataset
    graph_html = fig.to_html(full_html=False)
    
    return render_template('visualize.html', graph_html=graph_html)
