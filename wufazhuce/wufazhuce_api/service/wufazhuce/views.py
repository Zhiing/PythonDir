from flask_restful import Resource, reqparse
from .model import (PhotoModel, ArticleModel, QuestionModel)
from service import db


class PhotoView(Resource):
    def get(self):
        '''
        http://127.0.0.1:5008/photo?photo_id=123
        '''
        parser = reqparse.RequestParser()
        parser.add_argument('photo_id', type=str, location='args')

        args = parser.parse_args()
        photo_info = db.session.query(PhotoModel).filter_by(
            photo_id=args.get('photo_id')).first()

        if photo_info is None:
            return {'code': 404, 'message': 'not found', 'data': {}}

        return {
            'code': 200,
            'message': 'success',
            'data': {
                'photo_id': photo_info.photo_id,
                'photo_url': photo_info.photo_url,
                'photo_date': photo_info.photo_date,
                'photo_text': photo_info.photo_text,
                'wufazhuce_url': photo_info.wufazhuce_url
            }
        }

    def post(self):
        pass

    def put(self):
        pass


class ArticleView(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('article_id', type=str, location='args')

        args = parser.parse_args()
        article_info = db.session.query(ArticleModel).filter_by(
            article_id=args.get('article_id')).first()

        if article_info is None:
            return {'code': 404, 'message': 'not found', 'data': {}}

        return {
            'code': 200,
            'message': 'success',
            'data': {
                'article_id': article_info.article_id,
                'article_title': article_info.article_title,
                'article_author': article_info.article_author,
                'article_text': article_info.article_text,
                'article_body': article_info.article_body
            }
        }

    def post(self):
        pass

    def put(self):
        pass


class QuestionView(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('question_id', type=str, location='args')

        args = parser.parse_args()
        question_info = db.session.query(QuestionModel).filter_by(
            question_id=args.get('question_id')).first()

        if question_info is None:
            return {'code': 404, 'message': 'not found', 'data': {}}

        return {
            'code': 200,
            'message': 'success',
            'data': {
                'question_id': question_info.question_id,
                'question_title': question_info.question_title,
                'question_text': question_info.question_text,
                'question_body': question_info.question_body
            }
        }

    def post(self):
        pass

    def put(self):
        pass
