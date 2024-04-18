import uvicorn
from app import llm_prediction

if __name__ == "__main__":
    uvicorn.run(llm_prediction, host="0.0.0.0", port=7000)
