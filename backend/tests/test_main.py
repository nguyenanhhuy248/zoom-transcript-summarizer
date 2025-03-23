"""Unit tests for the FastAPI application main module."""
from __future__ import annotations

import pytest
from app.config.config import settings
from app.main import create_application
from fastapi.testclient import TestClient


@pytest.fixture
def test_client():
    """Create a test client for the FastAPI application."""
    app = create_application()
    return TestClient(app)


def test_application_creation():
    """Test that the application is created with correct settings."""
    app = create_application()
    assert app.title == settings.project_name
    assert app.version == settings.version
    assert app.debug == settings.debug


def test_cors_middleware(test_client):
    """Test that CORS middleware is properly configured."""
    response = test_client.options(
        '/',
        headers={
            'Origin': 'http://localhost:3000',
            'Access-Control-Request-Method': 'GET',
        },
    )
    assert response.status_code == 200
    assert 'access-control-allow-origin' in response.headers
    assert response.headers['access-control-allow-origin'] == '*'


def test_api_prefix(test_client):
    """Test that the API prefix is correctly configured."""
    response = test_client.get(f"{settings.api_prefix}/health")
    # Should return 404 as health endpoint doesn't exist
    assert response.status_code == 404


def test_error_handlers(test_client):
    """Test that error handlers are properly configured."""
    # Test 404 error handler
    response = test_client.get('/non-existent-endpoint')
    assert response.status_code == 404

    # Test validation error handler
    response = test_client.post(f"{settings.api_prefix}/summarize", json={})
    assert response.status_code == 422


def test_application_lifespan():
    """Test that the application lifespan manager is properly configured."""
    app = create_application()
    assert hasattr(app, 'lifespan')
    assert app.lifespan is not None
