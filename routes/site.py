from fastapi import APIRouter
from controllers.site_controller import get_site_health

router = APIRouter(prefix="/sites",tags=["sites"])

@router.get("/health")
def site_health():
    return get_site_health()
    