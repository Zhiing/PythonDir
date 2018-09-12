from service import db


class PhotoModel(db.Model):
    '''
    图片表
    '''
    __tablename__ = 'photo'

    photo_id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.Text)
    photo_date = db.Column(db.Text)
    photo_text = db.Column(db.Text)
    wufazhuce_url = db.Column(db.Text)


class ArticleModel(db.Model):
    '''
    文章表
    '''
    __tablename__ = 'article'

    article_id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.Text)
    article_author = db.Column(db.Text)
    article_text = db.Column(db.Text)
    article_body = db.Column(db.Text)


class QuestionModel(db.Model):
    '''
    问答表
    '''
    __tablename__ = 'question'

    question_id = db.Column(db.Integer, primary_key=True)
    question_title = db.Column(db.Text)
    question_text = db.Column(db.Text)
    question_body = db.Column(db.Text)
