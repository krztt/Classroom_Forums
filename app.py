from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Function to connect to your XAMPP database
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',          
        password='',         
        database='class_forumdb'  
    )
    return connection

# The main route that loads when you visit the site
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Fetch all questions and join with the users table to get the author's name
    query = """
        SELECT questions.id, questions.title, questions.body, users.username 
        FROM questions 
        JOIN users ON questions.user_id = users.id 
        ORDER BY questions.created_at DESC
    """
    cursor.execute(query)
    questions = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    # This line connects app.py to index.html and passes the 'questions' data to it
    return render_template('index.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)