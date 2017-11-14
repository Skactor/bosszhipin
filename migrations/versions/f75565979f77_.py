"""empty message

Revision ID: f75565979f77
Revises: 
Create Date: 2017-09-27 14:17:04.718080

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f75565979f77'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('companies', sa.Column('bosszhipin_companyid', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_companies_bosszhipin_companyid'), 'companies', ['bosszhipin_companyid'], unique=False)
    op.drop_column('companies', 'city_id')
    op.add_column('jobs', sa.Column('bosszhipin_jobid', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_jobs_bosszhipin_jobid'), 'jobs', ['bosszhipin_jobid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_jobs_bosszhipin_jobid'), table_name='jobs')
    op.drop_column('jobs', 'bosszhipin_jobid')
    op.add_column('companies', sa.Column('city_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_companies_bosszhipin_companyid'), table_name='companies')
    op.drop_column('companies', 'bosszhipin_companyid')
    # ### end Alembic commands ###
