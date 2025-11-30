from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import students, courses
from app.db.database import connect_to_mongo, close_mongo_connection

app = FastAPI(
    title="EduVerse AI Backend",
    description="Multi-tenant e-learning platform API",
    version="1.0.0"
)

# CORS middleware for Angular frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection events
@app.on_event("startup")
async def startup_db():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db():
    await close_mongo_connection()

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "EduVerse AI Backend API",
        "version": "1.0.0",
        "status": "operational"
    }

# Health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Include routers
app.include_router(students.router)
app.include_router(courses.router)