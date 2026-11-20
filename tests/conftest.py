from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture(autouse=True)
def restore_activities():
    """Keep mutations to the in-memory activity store isolated per test."""
    original_activities = deepcopy(activities)

    yield

    activities.clear()
    activities.update(original_activities)


@pytest.fixture
def client():
    return TestClient(app)
