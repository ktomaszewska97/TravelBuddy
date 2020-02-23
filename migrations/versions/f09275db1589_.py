"""empty message

Revision ID: f09275db1589
Revises: 
Create Date: 2019-10-11 11:31:29.333280

"""
import sqlalchemy as sa
import sqlalchemy_utils
from alembic import op

GENDER = [('man', 'Man'),
              ('woman', 'Woman')]

BUDGET = [('small', '<250$'),
          ('medium', '250$-750$'),
          ('regular', '750$-1500$'),
          ('big', '1500$+')]

TYPE_OF_TRIP = [
    ("city_break", "City break"),
    ("work_and_travel", "Work&travel"),
    ("roadtrip", "Roadtrip"),
    ("backpacking", "Backpacking"),
    ("vacations", "Vacations"),
    ("other", "Other"),
]

HOUSING = [
    ("camping", "Camping"),
    ("airbnb", "AirBnB"),
    ("couchsurfing", "Couchsurfing"),
    ("hotels", "Hotels"),
    ("hostels", "Hostels"),
    ("other", "Other"),
]

FOOD = [
    ("self", "Self-cooking"),
    ("fastfoods", "Fast foods"),
    ("bistros", "Bistros"),
    ("restaurants", "Restaurants"),
]

# revision identifiers, used by Alembic.
revision = 'f09275db1589'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('mobile', sa.String(length=50), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('country', sa.String(length=200), nullable=True),
    sa.Column('if_english', sa.Boolean(), nullable=True),
    sa.Column('about', sa.String(length=255), nullable=True),
    sa.Column('gender', sqlalchemy_utils.types.choice.ChoiceType(choices=GENDER), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=True),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['profile_id'], ['profile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('trip_title', sa.String(length=100), nullable=True),
    sa.Column('gender', sqlalchemy_utils.types.choice.ChoiceType(choices=GENDER), nullable=True),
    sa.Column('type_of_trip', sqlalchemy_utils.types.choice.ChoiceType(choices=TYPE_OF_TRIP), nullable=True),
    sa.Column('housing', sqlalchemy_utils.types.choice.ChoiceType(choices=HOUSING), nullable=True),
    sa.Column('food', sqlalchemy_utils.types.choice.ChoiceType(choices=FOOD), nullable=True),
    sa.Column('budget', sqlalchemy_utils.types.choice.ChoiceType(choices=BUDGET), nullable=True),
    sa.Column('must_do', sa.String(length=255), nullable=True),
    sa.Column('must_see', sa.String(length=255), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('activity_name', sa.String(length=255), nullable=True),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favourite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('place',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('place_name', sa.String(length=255), nullable=True),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('place')
    op.drop_table('favourite')
    op.drop_table('activity')
    op.drop_table('trip')
    op.drop_table('user')
    op.drop_table('profile')
    # ### end Alembic commands ###