# Example using FastAPI
from fastapi import APIRouter, Request
from pydantic import BaseModel
import boto3
from datetime import datetime
from decimal import Decimal
from fastapi.middleware.cors import CORSMiddleware


router = APIRouter()



dynamodb = boto3.resource("dynamodb", region_name="ap-south-1")  # change region if needed
table = dynamodb.Table("UserHealthData")  # make sure this exists

class HealthData(BaseModel):
    user_id: str
    date: str  # e.g., "2025-07-20"
    sleep: float
    hrv: float

@router.post("/save-health-data")
async def save_health_data(data: HealthData):
    table.put_item(
        Item={
            "user_id": data.user_id,
            "date": data.date,
            "sleep": Decimal(str(data.sleep)),  # 👈 convert to Decimal
            "hrv": Decimal(str(data.hrv))       # 👈 convert to Decimal
        }
    )
    return {"message": "✅ Health data saved to DynamoDB!"}

