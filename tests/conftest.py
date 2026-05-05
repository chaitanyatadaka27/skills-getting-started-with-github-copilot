"""Pytest configuration and shared fixtures for FastAPI tests."""
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Provide a TestClient for API testing."""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to a known state before each test."""
    # Save original state
    original_activities = {
        k: {
            "participants": v["participants"].copy(),
            "description": v["description"],
            "schedule": v["schedule"],
            "max_participants": v["max_participants"],
        }
        for k, v in activities.items()
    }
    
    yield
    
    # Restore original state after test
    for activity_name, activity_data in original_activities.items():
        activities[activity_name]["participants"] = activity_data["participants"].copy()
