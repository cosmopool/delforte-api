from zione.domain.entities.appointment import Appointment
from zione.domain.repository_interface import RepositoryInterface

def fetch_open_appointments_usecase(repo: RepositoryInterface):
    return repo.select({"isFinished": "= false"}, Appointment.endpoint)
