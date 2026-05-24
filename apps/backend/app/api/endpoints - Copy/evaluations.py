from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_evaluations():
    return [{"id": 1, "name": "Eval 1"}]

@router.post("/")
def create_evaluation():
    return {"message": "Evaluation created successfully"}
