"""empty message

Revision ID: b3571c20fc47
Revises: 
Create Date: 2021-10-04 17:14:31.037105

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b3571c20fc47'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subscribers', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('email_subscribers', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('total_revenue', sa.Integer(), nullable=True),
    sa.Column('monthly_fee', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('original_post', sa.Text(), nullable=True),
    sa.Column('post_edits', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('free', sa.Boolean(), nullable=True),
    sa.Column('revenue', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('subscribed_ids', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('newsfeed_filters', postgresql.ARRAY(postgresql.ENUM('football', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'esports', 'fighting', name='filtersenum')), nullable=True),
    sa.Column('light_mode', sa.Boolean(), nullable=True),
    sa.Column('odds_format', sa.Boolean(), nullable=True),
    sa.Column('stripe_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('stripe_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('user_bets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event', sa.String(), nullable=True),
    sa.Column('american_odds', sa.Integer(), nullable=True),
    sa.Column('decimal_odds', sa.Integer(), nullable=True),
    sa.Column('stake', sa.Integer(), nullable=True),
    sa.Column('sportsbook', sa.String(length=50), nullable=True),
    sa.Column('handicap', sa.Integer(), nullable=True),
    sa.Column('notification_handicap', sa.Numeric(precision=3, scale=1), nullable=True),
    sa.Column('notification_price', sa.Integer(), nullable=True),
    sa.Column('closing_line_value', sa.Numeric(precision=4, scale=4), nullable=True),
    sa.Column('roi', sa.Numeric(precision=4, scale=4), nullable=True),
    sa.Column('results', postgresql.ARRAY(postgresql.ENUM('win', 'loss', 'push', 'cancelled', name='resultsenum')), nullable=True),
    sa.Column('payout', sa.Numeric(precision=4, scale=4), nullable=True),
    sa.Column('game_date', sa.DateTime(), nullable=True),
    sa.Column('bet_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_bets')
    op.drop_table('users')
    op.drop_table('posts')
    op.drop_table('authors')
    # ### end Alembic commands ###
