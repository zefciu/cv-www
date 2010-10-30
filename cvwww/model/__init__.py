"""The application's model objects"""
from cvwww.model.meta import Session, metadata

import sqlalchemy as sa
from sqlalchemy import orm

pages_table = sa.Table(
    'pages', metadata,
    sa.Column(
        'id', sa.types.Integer, sa.schema.Sequence(
            'pages_id_seq', optional= True
        ), primary_key = True
    ),
    sa.Column('slug', sa.types.Unicode(64), index=True),
    sa.Column('text', sa.types.UnicodeText()),
)

class Page(object):
    pass

orm.mapper(pages, Page)

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
