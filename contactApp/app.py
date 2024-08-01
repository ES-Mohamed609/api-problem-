from flask import url_for, redirect, render_template

from endpoints import create_app


app = create_app()


@app.route('/')
def root():
    return redirect(url_for('home'))


@app.route("/base")
def base():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
