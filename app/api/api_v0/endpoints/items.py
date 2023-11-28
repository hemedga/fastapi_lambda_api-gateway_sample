from fastapi import APIRouter

router = APIRouter(prefix='/items', tags=["Items"])
d = [
	{
        "id": 0,
        "inInventory": "false",
        "product": "Car",
    },
	{
        "id": 1,
        "inInventory": "false",
        "product": "Coat",
    },
	{
        "id": 2,
        "inInventory": "true",
        "product": "Cereal",
    },
	{
        "id": 3,
        "inInventory": "false",
        "product": "Cerberos",
    },
	{
        "id": 4,
        "inInventory": "false",
        "product": "Cumin",
    },
	{
        "id": 5,
        "inInventory": "true",
        "product": "Can",
    }
            
] 

d5 = {
        "id": 5,
        "inInventory": "true",
        "product": "Can",
    }

@router.get("")
async def root():
    return d

@router.get("/5")
def results():
    return d5