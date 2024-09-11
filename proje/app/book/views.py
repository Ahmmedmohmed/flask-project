from flask import request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

from app.book import  book_blueprint
from app.models import book, db 
import  os

@book_blueprint.route('', endpoint='index')
def index():
    books = book.query.all()
    return render_template("index.html", books=books)



@book_blueprint.route("/<int:id>", endpoint="show")
def show(id):
    bo = book.query.get_or_404(id)
    return render_template("book_details.html", book=bo)


@book_blueprint.route("/<int:id>/delete", endpoint="delete", methods=["POST"])
def delete(id):
    bo = book.query.get_or_404(id)
    db.session.delete(bo)
    db.session.commit()
    return redirect(url_for("book.index"))



from app.book.forms import bookform




@book_blueprint.route("/create", endpoint="create", methods=["POST", "GET"])
def create_book():
    form = bookform()
    if request.method == 'POST':
        if form.validate_on_submit():
            image_name = None
            if request.files.get('image'):
                image = form.image.data
                image_name = secure_filename(image.filename)
                image_dir = os.path.join('app','static', 'book', 'images')
                if not os.path.exists(image_dir):
                    os.makedirs(image_dir)
                image_path = os.path.join(image_dir, image_name)
                image.save(image_path)
            
            data = dict(request.form)
            del data['csrf_token']
            

            data["image"] = image_name
            
            bo = book(**data)
            db.session.add(bo)
            db.session.commit()
            return redirect(bo.show_url)



    return render_template("create.html", form=form)
 
@book_blueprint.route('/book/<int:id>/edit', endpoint="edit" , methods=['GET', 'POST'])
def edit_book(id):
    bo = book.query.get_or_404(id)
    form = bookform(obj=bo)
    if request.method=='POST':
        if form.validate_on_submit():
            image_name=None
            if request.files.get('image'):
                image= form.image.data
                image_name =secure_filename(image.filename)
                image.save(os.path.join('app/static/book/images/', image_name))
            data= dict(request.form)
            del data['csrf_token']
            data.pop('submit', None)
            data["image"]= image_name
            print(request.form)
            bo= book(**data)
            db.session.add(bo)
            db.session.commit()
            return redirect(bo.show_url)

    return  render_template("edit.html", form=form)



