from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/notes",
    tags=["notes"],
    responses={404: {"description": "Not found"}},
)


fake_notes_db = {
    "1": {
        "user": "Riz",
        "note": "This is note 1"
    },
    "2": {
        "user": "Riz",
        "note": "This is note 2"
    }
}


@router.get("/")
async def read_notes():
    return fake_notes_db


@router.get("/{note_id}")
async def read_note(note_id: str):
    if note_id not in fake_notes_db:
        raise HTTPException(status_code=404, detail="note not found")
    return fake_notes_db[note_id]


@router.put("/{note_id}",
            tags=["custom"],
            responses={403: {"description": "Operation forbidden"}},
)
async def update_note(note_id: str):
    raise HTTPException(
        status_code=403, detail="You cannot update yet"
    )
