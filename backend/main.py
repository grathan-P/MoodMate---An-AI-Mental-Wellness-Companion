from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chatbotapi import router as chatbot_router
from loginauth import router as auth_router
from signupauth import router as signup_router
from analyzetweets import router as analyze_router
from googlefit import router as googlefit_router
from habit import router as habit_router

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 👈 match your frontend port!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chatbot_router)
app.include_router(auth_router)
app.include_router(signup_router)
app.include_router(analyze_router)
app.include_router(googlefit_router)
app.include_router(habit_router)