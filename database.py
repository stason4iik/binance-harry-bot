import aiosqlite


DB_NAME = "posts.db"


async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS posts (
                id TEXT PRIMARY KEY
            )
            """
        )
        await db.commit()


async def is_new_post(post_id):

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            "SELECT id FROM posts WHERE id=?",
            (post_id,)
        )

        result = await cursor.fetchone()

        return result is None


async def save_post(post_id):

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            "INSERT OR IGNORE INTO posts(id) VALUES(?)",
            (post_id,)
        )

        await db.commit()