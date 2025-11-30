# from motor.motor_asyncio import AsyncIOMotorClient
# from pymongo.server_api import ServerApi
# import os
# from dotenv import load_dotenv

# load_dotenv()

# MONGO_URI = os.getenv("MONGO_URI")
# DATABASE_NAME = os.getenv("DATABASE_NAME", "LMS")

# client = None
# database = None

# async def connect_to_mongo():
#     """Connect to MongoDB"""
#     global client, database
#     try:
#         client = AsyncIOMotorClient(MONGO_URI, server_api=ServerApi('1'))
#         database = client[DATABASE_NAME]
#         await client.admin.command('ping')
#         print("✅ Connected to MongoDB successfully!")
#     except Exception as e:
#         print(f"❌ Error connecting to MongoDB: {e}")
#         raise

# async def close_mongo_connection():
#     """Close MongoDB connection"""
#     global client
#     if client:
#         client.close()
#         print("MongoDB connection closed")

# def get_database():
#     """Get database instance"""
#     return database

# # Collection helpers
# def get_collection(name: str):
#     """Get any collection by name"""
#     return database[name]

# # Specific collection getters
# def get_courses_collection():
#     return database.courses

# def get_students_collection():
#     return database.students

# def get_teachers_collection():
#     return database.teachers

# def get_assignments_collection():
#     return database.assignments

# def get_quizzes_collection():
#     return database.quizzes


from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME", "LMS")

# You requested this EXACT structure:
client = AsyncIOMotorClient(MONGO_URI)
db = client[DATABASE_NAME]   # db = client["LMS"]


async def connect_to_mongo():
    """Connect to MongoDB"""
    try:
        # Test connection
        await db.command("ping")
        print("✅ Connected to MongoDB successfully!")
    except Exception as e:
        print(f"❌ Error connecting to MongoDB: {e}")
        raise


async def close_mongo_connection():
    """Close MongoDB connection"""
    global client
    if client:
        client.close()
        print("MongoDB connection closed")


def get_database():
    """Return db instance"""
    return db


def get_collection(name: str):
    """Return any collection dynamically"""
    return db[name]


# === Specific Collection Helpers === #
def get_courses_collection():
    return db["courses"]

def get_students_collection():
    return db["students"]

def get_teachers_collection():
    return db["teachers"]


