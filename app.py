from flask import Flask, render_template,request,url_for,flash,redirect
from db.conDB import ConDB
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = '234FDasf#fada#@$r'


@app.route('/')
def index():
    with ConDB() as connect:
        results = connect.getAllData()
        print(results)
        return render_template('index.html', results = results)

@app.route('/<int:post_id>')
def getPost(post_id):
    with ConDB() as connect:
        result = connect.getPost(post_id)
        return render_template('post.html', result = result[0])

@app.route('/create', methods=('GET','POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash("Tytuł jest wymagany!")
        else:
            with ConDB() as add:
                add.inserttodb(title,content)
                return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit',methods=('GET','POST'))
def edit(id):
    with ConDB() as connect:
        result = connect.getPost(id)
    if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            if not title:
                flash("Tytuł jest wymagany!")
            else:
                with ConDB() as connect:
                    connect.updatedb(title,content,id)
                return redirect(url_for('index'))
    return render_template('edit.html',post = result)

@app.route('/<int:id>/delete',methods=('POST',))
def delete(id):
    with ConDB() as connect:
        result = connect.getPost(id)
        connect.delete(id)
        flash('Wpis został usuniety zostal usuniety!')
        return redirect(url_for('index'))

@app.route('/aboutme')
def aboutme():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
