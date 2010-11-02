"""The application's model objects"""
from cvwww.model.meta import Session, metadata

import sqlalchemy as sa
from sqlalchemy import orm

ability_cats_table = sa.Table(
    'ability_cats', metadata,
    sa.Column(
        'id', sa.types.Integer(), sa.schema.Sequence(
            'ability_cats_seq', optional = True
        ), primary_key = True
    ),
    sa.Column('name', sa.types.Unicode(128)),
    sa.Column('slug', sa.types.Unicode(128)),
)

abilities_table = sa.Table(
    'abilities', metadata,
    sa.Column(
        'id', sa.types.Integer(), sa.schema.Sequence(
            'projects_id_seq', optional= True
        ), primary_key = True
    ),
    sa.Column('ability_cat_id', sa.types.Integer(), sa.ForeignKey('ability_cats.id'), nullable = False),
    sa.Column('ability_group_id', sa.types.Integer(), sa.ForeignKey('ability_cats.id'), nullable = True),
    sa.Column('name', sa.types.Unicode(128)),
    sa.Column('skill', sa.types.Integer()),
)

abilities_projects_table = sa.Table(
    'abilities_projects', metadata,
    sa.Column('ability_id', sa.types.Integer(), sa.ForeignKey('abilities.id')),
    sa.Column('project_id', sa.types.Integer(), sa.ForeignKey('projects.id')),
)

pages_table = sa.Table(
    'pages', metadata,
    sa.Column(
        'id', sa.types.Integer(), sa.schema.Sequence(
            'pages_id_seq', optional= True
        ), primary_key = True
    ),
    sa.Column('title', sa.types.Unicode(128)),
    sa.Column('slug', sa.types.Unicode(128), index=True),
    sa.Column('content', sa.types.UnicodeText()),
)

projects_table = sa.Table(
    'projects', metadata,
    sa.Column(
        'id', sa.types.Integer(), sa.schema.Sequence(
            'projects_id_seq', optional = True
        ), primary_key = True
    ),
    sa.Column('name', sa.types.Unicode(128)),
    sa.Column('description', sa.types.UnicodeText()),
    sa.Column('url_source', sa.types.Unicode(64)),
    sa.Column('url_application', sa.types.Unicode(64)),
)

class Ability(object):
    pass

class AbilityCat(object):
    pass

class Page(object):
    pass

class Project(object):
    pass

orm.mapper(Ability, abilities_table, properties = {
    'ability_cat' = orm.relationship(AbilityCat, backref = 'abilities',
           primaryjoin = (
               abilities_table.c.ability_cat_id == ability_cats_table.c.id
           )),
    'ability_group' = orm.relationship(AbilityCat, backref = 'abilities',
           primaryjoin = (
               abilities_table.c.ability_group_id == ability_cats_table.c.id
           )),
}

orm.mapper(AbilityCat, ability_cats_table)

orm.mapper(Page, pages_table)

orm.mapper(Project, projects_table, properties = {
    'abilities' = orm.relationship(Ability, secondary = abilities_projects_table, backref = 'projects')
}

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
