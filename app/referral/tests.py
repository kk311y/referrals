import pytest
from .models import Participant


@pytest.mark.django_db
def test_create_participant():
    participant = Participant.objects.create(
        first_name = 'Jane',
        last_name = 'Austen',
        middle_name = '',
        date_of_birth = '1775-12-16'
    )
    assert participant.first_name == 'Jane'


