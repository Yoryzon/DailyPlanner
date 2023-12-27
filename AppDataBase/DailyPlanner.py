from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from DataBase.DataBaseClassesMethods.EventsMethods import EventManager
from DataBase.DataBaseClassesMethods.TasksMethods import TaskManager
from DataBase.DataBaseClassesMethods.NotesMethods import NoteManager
from DataBase.DataBaseClassesMethods.ContactsMethods import ContactManager

from AppDataBase import Ui_DailyPlanner
from AppDataBaseFunctions.EventsWindowsFunctions.EventsWindowFunctions import EventsWindowDialog
from AppDataBaseFunctions.TasksWindowsFunctions.TasksWindowFunctions import TasksWindowDialog
from AppDataBaseFunctions.ContactsWindowsFunctions.ContactsWindowFunctions import ContactsWindowDialog
from AppDataBaseFunctions.NotesWindowsFunctions.NotesWindowFunctions import NotesWindowDialog


class DailyPlannerFunctions(QMainWindow, Ui_DailyPlanner):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_connections()
        self.load_events()

        self.EventsTableView.clicked.connect(self.load_tasks)
        self.EventsTableView.clicked.connect(self.load_contacts)
        self.TasksForTheEventsTableView.clicked.connect(self.load_notes)

    def setup_connections(self):
        self.EventsButton.clicked.connect(self.open_events_dialog)
        self.TasksButton.clicked.connect(self.open_tasks_dialog)
        self.ContactsButton.clicked.connect(self.open_contacts_dialog)
        self.NotesButton.clicked.connect(self.open_notes_dialog)

    def load_events(self):
        try:
            events = EventManager.get_all_events()

            model = QStandardItemModel(len(events), 6)
            model.setHorizontalHeaderLabels(
                ["Event ID", "Title", "Description", "Event Date", "Start Time", "End Time"])

            for row, event in enumerate(events):
                event_id_item = QStandardItem(str(event.EventID))
                event_id_item.setEditable(False)
                model.setItem(row, 0, event_id_item)

                title_item = QStandardItem(event.Title)
                model.setItem(row, 1, title_item)

                description_item = QStandardItem(event.Description)
                model.setItem(row, 2, description_item)

                event_date_item = QStandardItem(str(event.EventDate))
                model.setItem(row, 3, event_date_item)

                start_time_item = QStandardItem(str(event.StartTime))
                model.setItem(row, 4, start_time_item)

                end_time_item = QStandardItem(str(event.EndTime))
                model.setItem(row, 5, end_time_item)

            self.EventsTableView.setModel(model)
            self.EventsTableView.setSelectionBehavior(QTableView.SelectRows)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error loading events: {str(e)}')

    def load_tasks(self):
        try:
            selected_row = self.EventsTableView.currentIndex().row()
            if selected_row >= 0:
                event_id = self.EventsTableView.model().index(selected_row, 0).data()
                tasks = TaskManager.search_tasks_by_event_id(event_id) if event_id else []

                model = QStandardItemModel(len(tasks), 6)
                model.setHorizontalHeaderLabels(
                    ["Task ID", "Task Name", "Description", "Due Date", "Priority", "Status"])

                for row, task in enumerate(tasks):
                    task_id_item = QStandardItem(str(task.TaskID))
                    task_id_item.setEditable(False)
                    model.setItem(row, 0, task_id_item)

                    task_name_item = QStandardItem(task.TaskName)
                    model.setItem(row, 1, task_name_item)

                    description_item = QStandardItem(task.Description)
                    model.setItem(row, 2, description_item)

                    due_date_item = QStandardItem(str(task.DueDate))
                    model.setItem(row, 3, due_date_item)

                    priority_item = QStandardItem(str(task.Priority))
                    model.setItem(row, 4, priority_item)

                    status_item = QStandardItem(task.Status)
                    model.setItem(row, 5, status_item)

                self.TasksForTheEventsTableView.setModel(model)
                self.TasksForTheEventsTableView.setSelectionBehavior(QTableView.SelectRows)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error loading tasks: {str(e)}')

    def load_contacts(self):
        try:
            selected_row = self.EventsTableView.currentIndex().row()
            if selected_row >= 0:
                event_id = self.EventsTableView.model().index(selected_row, 0).data()
                contacts = ContactManager.search_contacts_by_event_id(event_id) if event_id else []

                model = QStandardItemModel(len(contacts), 5)
                model.setHorizontalHeaderLabels(["Contact ID", "Full Name", "Phone", "Email", "Address"])

                for row, contact in enumerate(contacts):
                    contact_id_item = QStandardItem(str(contact.ContactID))
                    contact_id_item.setEditable(False)
                    model.setItem(row, 0, contact_id_item)

                    full_name_item = QStandardItem(contact.FullName)
                    model.setItem(row, 1, full_name_item)

                    phone_item = QStandardItem(contact.Phone)
                    model.setItem(row, 2, phone_item)

                    email_item = QStandardItem(contact.Email)
                    model.setItem(row, 3, email_item)

                    address_item = QStandardItem(contact.Address)
                    model.setItem(row, 4, address_item)

                self.ContactForTheEventTableView.setModel(model)
                self.ContactForTheEventTableView.setSelectionBehavior(QTableView.SelectRows)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error loading contacts: {str(e)}')

    def load_notes(self):
        try:
            selected_row = self.TasksForTheEventsTableView.currentIndex().row()
            if selected_row >= 0:
                task_id = self.TasksForTheEventsTableView.model().index(selected_row, 0).data()
                notes = NoteManager.search_notes_by_task_id(task_id) if task_id else []

                model = QStandardItemModel(len(notes), 4)
                model.setHorizontalHeaderLabels(["Note ID", "Title", "Content", "Created Date"])

                for row, note in enumerate(notes):
                    note_id_item = QStandardItem(str(note.NoteID))
                    note_id_item.setEditable(False)
                    model.setItem(row, 0, note_id_item)

                    title_item = QStandardItem(note.Title)
                    model.setItem(row, 1, title_item)

                    content_item = QStandardItem(note.Content)
                    model.setItem(row, 2, content_item)

                    created_date_item = QStandardItem(str(note.CreatedDate))
                    model.setItem(row, 3, created_date_item)

                self.NotesForTheTaskTableView.setModel(model)
                self.NotesForTheTaskTableView.setSelectionBehavior(QTableView.SelectRows)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error loading notes: {str(e)}')

    @staticmethod
    def open_events_dialog():
        events_window = EventsWindowDialog()
        events_window.show()

    @staticmethod
    def open_tasks_dialog():
        tasks_window = TasksWindowDialog()
        tasks_window.show()

    @staticmethod
    def open_contacts_dialog():
        contacts_window = ContactsWindowDialog()
        contacts_window.show()

    @staticmethod
    def open_notes_dialog():
        notes_window = NotesWindowDialog()
        notes_window.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = DailyPlannerFunctions()
    window.show()
    sys.exit(app.exec_())
