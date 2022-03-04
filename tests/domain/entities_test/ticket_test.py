import pytest

from zione.domain.entities.ticket import Ticket

class TestTicketInstance:
    tk_dict = {
        "id": 1,
        "clientName": "Roberto Barao",
        "clientAddress": "Rua David Campista, 211",
        "clientPhone": 41999000888,
        "serviceType": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False
    }

    tk = Ticket(
        id = 1,
        clientName = "Roberto Barao",
        clientAddress = "Rua David Campista, 211",
        clientPhone = 41999000888,
        serviceType = "Manutencao",
        description = "Alarme nao arma",
        isFinished = False
    )

    def test_tkpointment_entity_init(self):
        assert self.tk.id == 1
        assert self.tk.clientName == "Roberto Barao"
        assert self.tk.clientAddress == "Rua David Campista, 211"
        assert self.tk.clientPhone == 41999000888
        assert self.tk.serviceType == "Manutencao"
        assert self.tk.description == "Alarme nao arma"
        assert self.tk.isFinished == False

    def test_ticket_entity_to_dict(self):
        assert self.tk.to_dict() == self.tk_dict

    def test_ticket_entity_from_dict(self):
        tk = Ticket.from_dict(self.tk_dict)
        
        assert self.tk.id == 1
        assert self.tk.clientName == "Roberto Barao"
        assert self.tk.clientAddress == "Rua David Campista, 211"
        assert self.tk.clientPhone == 41999000888
        assert self.tk.serviceType == "Manutencao"
        assert self.tk.description == "Alarme nao arma"
        assert self.tk.isFinished == False

    def test_ticket_entity_comparison(self):
        tk1 = self.tk
        tk2 = Ticket.from_dict(self.tk_dict)

        assert tk1 == tk2

    def test_ticket_entity_to_dict_with_additional_fields(self):
        additonal_field = {
        "id": 1,
        "time": "10:00",
        "date": "12-12-2021",
        "duration": "1:00",
        "ticketId": 1,
        "clientName": "Roberto Barao",
        "clientAddress": "Rua David Campista, 211",
        "clientPhone": 41999000888,
        "serviceType": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False
        }
        tk = Ticket.from_dict(additonal_field)

        assert tk == self.tk

    def test_ticket_entity_to_dict_with_missing_fields(self):
        missing_field = {"id": 1, "ticketId": 1, "isFinished": False}

        with pytest.raises(TypeError):
            _ = Ticket.from_dict(missing_field)

    def test_user_entity_from_dict_default_id_value(self):
        tk_dict = {
        "time": "10:00",
        "date": "12-12-2021",
        "duration": "1:00",
        "ticketId": 1,
        "clientName": "Roberto Barao",
        "clientAddress": "Rua David Campista, 211",
        "clientPhone": 41999000888,
        "serviceType": "Manutencao",
        "description": "Alarme nao arma",
        "isFinished": False
        }
        tk = Ticket.from_dict(tk_dict)

        assert tk.id == -1

    def test_user_entity_endpoint_value(self):
        endpoint = Ticket.endpoint

        assert endpoint == "tickets"
