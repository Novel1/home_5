from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "article" ADD "author_id" UUID NOT NULL;
        ALTER TABLE "article" ADD CONSTRAINT "fk_article_user_8c489e15" FOREIGN KEY ("author_id") REFERENCES "user" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "article" DROP CONSTRAINT "fk_article_user_8c489e15";
        ALTER TABLE "article" DROP COLUMN "author_id";"""
