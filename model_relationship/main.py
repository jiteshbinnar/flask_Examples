from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
# from marshmallow import fields, Schema, ValidationError
from flask_bootstrap import Bootstrap

from forms import CommentForm
app=Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///profile.db'
app.config['SECRET_KEY']='\xc4\xe3\xd9*\xd3X\xdeM)\xd5Cu'
db=SQLAlchemy(app)
app.app_context().push()


post_tag = db.Table('post_tag',
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                    )


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return f'<Tag "{self.name}">' 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    comments = db.relationship('Comment', backref='post')
    tags=db.relationship("Tag",secondary=post_tag,backref='posts')

    def __repr__(self):
        return f'<Post "{self.title}">'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __repr__(self):
        return f'<Comment "{self.content[:20]}...">'








# class CommentSchema(Schema):
#     id=fields.Int()
#     content=fields.Str(required=True)
   

# class PostSchema(Schema):
#     id=fields.Int()
#     title=fields.Str(required=True)
#     content=fields.Str(required=True)
#     comments=fields.Nested(CommentSchema)


# post_schemas=PostSchema(many=True)
# post_schema=PostSchema()
# comment_schema=CommentSchema()
# comment_schemas=CommentSchema(many=True)





@app.route("/",methods=["GET","POST"])
def index():

    posts=Post.query.all()
    return render_template("index.html",posts=posts)
        


@app.route("/<int:post_id>/",methods=["GET","POST"])
def post(post_id):
    form=CommentForm()
    post =Post.query.get_or_404(post_id)
    if request.method=="POST":
        comment=Comment(content=form.content.data,post=post)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('post', post_id=post.id))

        
    return render_template("post.html",post=post,form=form)




@app.route("/comments/",methods=["GET","POST"])
def comments():
    comments = Comment.query.order_by(Comment.id.desc()).all()
    return render_template("comments.html",comments=comments)
        


@app.route('/comments/<int:comment_id>/delete')
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    post_id = comment.post.id
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('post', post_id=post_id))


@app. route('/tags/<tag_name>',methods=["POST","GET"])
def all_tags(tag_name):
    tags=Tag.query.filter_by(name=tag_name).first_or_404()
    return render_template("tags.html",tags=tags)



    
   









if __name__=='__main__':
   
    app.run(debug=True)










