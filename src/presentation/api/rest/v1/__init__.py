from .trip import router as trip_router
from .pass_in_trip import router as pass_in_trip_router
from .company import router as company_router
from .passenger import router as passenger_router
from fastapi import APIRouter

router = APIRouter(prefix='/v1')
router.include_router(trip_router)
router.include_router(pass_in_trip_router)
router.include_router(company_router)
router.include_router(passenger_router)