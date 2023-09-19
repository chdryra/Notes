from fastapi import APIRouter, HTTPException

from sql.sqlutils import PostgresDb

PREFIX = "/notes"

router = APIRouter(
    prefix=PREFIX,
    tags=["notes"],
    responses={404: {"description": "Not found"}},
)

executer = PostgresDb("postgresql://postgres:kulgasimsim@127.0.0.1:5432/notes")

@router.get("/")
async def read_notes():
    api = f"{PREFIX} GET"
    executer.insert(f"""
    INSERT into api_calls(api) values("{api}") 
    """)


@router.get("/{note_id}")
async def read_note(note_id: str):
    api = f"{PREFIX}/{note_id} GET"
    executer.insert(f"""
    INSERT into api_calls(api) values("{api}") 
    """)


@router.put("/{note_id}",
            tags=["custom"],
            responses={403: {"description": "Operation forbidden"}},
)
async def update_note(note_id: str):
    api = f"{PREFIX}/{note_id} POST"
    executer.insert(f"""
    INSERT into api_calls(api) values("{api}") 
    """)
