"""Add AI interaction tables

Revision ID: 002
Revises: 001_initial_database_schema
Create Date: 2023-07-01 14:15:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSON


# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001_initial_database_schema'
branch_labels = None
depends_on = None


def upgrade():
    # Create AI interactions table
    op.create_table(
        'ai_interactions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('session_id', sa.String(64), nullable=False),
        sa.Column('client_ip', sa.String(45), nullable=True),
        sa.Column('user_agent', sa.String(512), nullable=True),
        sa.Column('interaction_type', sa.String(50), nullable=False),
        sa.Column('request_text', sa.Text(), nullable=True),
        sa.Column('response_text', sa.Text(), nullable=True),
        sa.Column('started_at', sa.DateTime(), nullable=False),
        sa.Column('completed_at', sa.DateTime(), nullable=True),
        sa.Column('duration_ms', sa.Float(), nullable=True),
        sa.Column('tokens_input', sa.Integer(), nullable=True),
        sa.Column('tokens_output', sa.Integer(), nullable=True),
        sa.Column('context', JSON, nullable=True),
        sa.Column('metadata', JSON, nullable=True),
        sa.Column('success', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('error_type', sa.String(100), nullable=True),
        sa.Column('error_message', sa.Text(), nullable=True),
        sa.Column('user_rating', sa.Integer(), nullable=True),
        sa.Column('user_feedback', sa.Text(), nullable=True),
        sa.Column('model_name', sa.String(100), nullable=True),
        sa.Column('model_version', sa.String(50), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create indexes
    op.create_index(op.f('ix_ai_interactions_id'), 'ai_interactions', ['id'], unique=False)
    op.create_index(op.f('ix_ai_interactions_session_id'), 'ai_interactions', ['session_id'], unique=False)
    op.create_index(op.f('ix_ai_interactions_interaction_type'), 'ai_interactions', ['interaction_type'], unique=False)
    op.create_index(op.f('ix_ai_interactions_created_at'), 'ai_interactions', ['created_at'], unique=False)
    
    # Create AI feedback table
    op.create_table(
        'ai_feedback',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('interaction_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('rating', sa.Integer(), nullable=False),
        sa.Column('comment', sa.Text(), nullable=True),
        sa.Column('category', sa.String(100), nullable=True),
        sa.Column('sentiment_score', sa.Float(), nullable=True),
        sa.Column('tags', JSON, nullable=True),
        sa.Column('reviewed', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('reviewer_notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['interaction_id'], ['ai_interactions.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create indexes
    op.create_index(op.f('ix_ai_feedback_id'), 'ai_feedback', ['id'], unique=False)
    op.create_index(op.f('ix_ai_feedback_interaction_id'), 'ai_feedback', ['interaction_id'], unique=False)
    op.create_index(op.f('ix_ai_feedback_rating'), 'ai_feedback', ['rating'], unique=False)
    op.create_index(op.f('ix_ai_feedback_created_at'), 'ai_feedback', ['created_at'], unique=False)


def downgrade():
    # Drop tables
    op.drop_table('ai_feedback')
    op.drop_table('ai_interactions')
