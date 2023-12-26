from sqlalchemy.exc import SQLAlchemyError

from DataBase.DataBaseConnection.DataBaseMeta import Base, Engine, SessionFactory
from DataBase.DataBaseClasses.Notes import Notes
from DataBase.DataBaseClasses.Tasks import Tasks

Base.metadata.create_all(Engine)
session = SessionFactory()


class NoteManager:
    @staticmethod
    def create_note(title, content, created_date, task_id=None):
        try:
            new_note = Notes(Title=title, Content=content, CreatedDate=created_date)
            if task_id:
                task = session.query(Tasks).filter_by(TaskID=task_id).first()
                if task:
                    new_note.task = task
            session.add(new_note)
            session.commit()
            return new_note
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error creating note: {e}")
            return None

    @staticmethod
    def get_all_notes():
        try:
            return session.query(Notes).all()
        except SQLAlchemyError as e:
            print(f"Error getting all notes: {e}")
            return []

    @staticmethod
    def update_note(note_id, new_title=None, new_content=None, new_created_date=None, new_task_id=None):
        try:
            note = session.query(Notes).filter_by(NoteID=note_id).first()
            if note:
                if new_title:
                    note.Title = new_title
                if new_content:
                    note.Content = new_content
                if new_created_date:
                    note.CreatedDate = new_created_date
                if new_task_id:
                    task = session.query(Tasks).filter_by(TaskID=new_task_id).first()
                    if task:
                        note.task = task
                session.commit()
                return note
            return None
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error updating note: {e}")
            return None

    @staticmethod
    def delete_note(note_id):
        try:
            note = session.query(Notes).filter_by(NoteID=note_id).first()
            if note:
                session.delete(note)
                session.commit()
                return True
            return False
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error deleting note: {e}")
            return False

    @staticmethod
    def get_note_by_id(note_id):
        try:
            return session.query(Notes).filter_by(NoteID=note_id).first()
        except SQLAlchemyError as e:
            print(f"Error getting note by ID: {e}")
            return None

    @staticmethod
    def search_notes_by_title(title):
        try:
            return session.query(Notes).filter(Notes.Title.ilike(f"%{title}%")).all()
        except SQLAlchemyError as e:
            print(f"Error searching notes by title: {e}")
            return []

    @staticmethod
    def search_notes_by_content(content):
        try:
            return session.query(Notes).filter(Notes.Content.ilike(f"%{content}%")).all()
        except SQLAlchemyError as e:
            print(f"Error searching notes by content: {e}")
            return []
