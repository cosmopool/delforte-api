from zione.domain.entities.appointment import Appointment
from zione.domain.entities.response import Response
from zione.domain.repository_interface import RepositoryInterface


def fetch_appointment_usecase(repo: RepositoryInterface, id: int) -> Response:
    record = {"id": f"= {id}"}
    return repo.select(record, Appointment.endpoint)
