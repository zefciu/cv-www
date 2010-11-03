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

ability_groups_table = sa.Table(
    'ability_groups', metadata,
    sa.Column(
        'id', sa.types.Integer(), sa.schema.Sequence(
            'ability_cats_seq', optional = True
        ), primary_key = True
    ),
    sa.Column('ability_cat_id', sa.ForeignKey('ability_cats.id')),
    sa.Column('name', sa.types.Unicode(128)),
)

abilities_table = sa.Table(
    'abilities', metadata,
    sa.Column(
        'id', sa.types.Integer(), sa.schema.Sequence(
            'projects_id_seq', optional= True
        ), primary_key = True
    ),
    sa.Column('ability_cat_id', sa.types.Integer(), sa.ForeignKey('ability_cats.id'), nullable = False),
    sa.Column('ability_group_id', sa.types.Integer(), sa.ForeignKey('ability_groups.id'), nullable = True),
    sa.Column('name', sa.types.Unicode(128), nullable = False),
    sa.Column('icon', sa.types.Unicode(128), nullable = True),
    sa.Column('skill', sa.types.Integer(), nullable = False),
)

abilities_projects_table = sa.Table(
    'abilities_projects', metadata,
    sa.Column('ability_id', sa.types.Integer(), sa.ForeignKey('abilities.id'), primary_key = True, nullable = False),
    sa.Column('project_id', sa.types.Integer(), sa.ForeignKey('projects.id'), primary_key = True, nullable = False),
)

pages_table = sa.Table(
    'pages', metadata,
    sa.Column(
        'id', sa.types.Integer(), sa.schema.Sequence(
            'pages_id_seq', optional= True
        ), primary_key = True
    ),
    sa.Column('title', sa.types.Unicode(128), nullable = False),
    sa.Column('slug', sa.types.Unicode(128), index=True, nullable = False),
    sa.Column('content', sa.types.UnicodeText(), nullable = False),
)

projects_table = sa.Table(
    'projects', metadata,
    sa.Column(
        'id', sa.types.Integer(), sa.schema.Sequence(
            'projects_id_seq', optional = True
        ), primary_key = True
    ),
    sa.Column('name', sa.types.Unicode(128), nullable = False),
    sa.Column('description', sa.types.UnicodeText(), nullable = False),
    sa.Column('url_source', sa.types.Unicode(64), nullable = True),
    sa.Column('url_application', sa.types.Unicode(64), nullable = True),
)

class Ability(object):
    pass

class AbilityCat(object):
    pass

class AbilityGroup(object):
    pass

class Page(object):
    pass

class Project(object):
    pass

orm.mapper(Ability, abilities_table, properties = {
    'ability_cat': orm.relationship(AbilityCat, backref = 'abilities'),
    'ability_group': orm.relationship(AbilityGroup, backref = 'abilities'),
})

orm.mapper(AbilityCat, ability_cats_table)

orm.mapper(AbilityGroup, ability_groups_table, properties = {
    'ability_cat': orm.relationship(AbilityCat, backref = 'ability_groups')
})

orm.mapper(Page, pages_table)

orm.mapper(Project, projects_table, properties = {
    'abilities': orm.relationship(Ability, secondary = abilities_projects_table, backref = 'projects')
})

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
