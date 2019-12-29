import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'goodreads'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@cluster0-y00j5.mongodb.net/goodreads?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("get_books.html", books=mongo.db.books.find())
    

# @app.route('/get_tasks')
# def get_tasks():
#     return render_template("tasks.html", tasks=mongo.db.tasks.find())

# @app.route('/add_task')
# def add_task():
#     return render_template('addtask.html',
#                           categories=mongo.db.categories.find())


# @app.route('/insert_task', methods=['POST'])
# def insert_task():
#     tasks = mongo.db.tasks
#     tasks.insert_one(request.form.to_dict())
#     return redirect(url_for('get_tasks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
