from zione.domain.repository_interface import RepositoryInterface

def fetch_agenda_usecase(repo: RepositoryInterface):
    return repo.select({"isFinished": "= false"}, "agenda")
