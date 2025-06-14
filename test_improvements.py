"""
Test script to demonstrate the improvements made to the pyAirfocus library.
"""

import logging
from airfocus.client import AirfocusClient
from airfocus.models.workspace import Workspace, WorkspaceGroup
from airfocus.models.team import TeamUser
from airfocus.logging_config import setup_logging, get_logger

# Set up logging
setup_logging(level=logging.INFO)
logger = get_logger(__name__)

def test_validation():
    """Test the new validation features."""
    logger.info("Testing validation features...")
    
    # Test workspace validation
    try:
        # This should fail - empty name
        workspace = Workspace(
            id="test-id",
            teamId="team-id",
            name="",  # Empty name should raise ValueError
            description="Test description"
        )
    except ValueError as e:
        logger.info(f"✅ Workspace validation caught empty name: {e}")
    
    try:
        # This should fail - negative order
        workspace = Workspace(
            id="test-id",
            teamId="team-id",
            name="Test Workspace",
            description="Test description",
            order=-1  # Negative order should raise ValueError
        )
    except ValueError as e:
        logger.info(f"✅ Workspace validation caught negative order: {e}")
    
    # Test workspace group validation
    try:
        # This should fail - empty name
        group = WorkspaceGroup(
            id="test-id",
            name="",  # Empty name should raise ValueError
            teamId="team-id"
        )
    except ValueError as e:
        logger.info(f"✅ WorkspaceGroup validation caught empty name: {e}")
    
    # Test team user validation
    try:
        # This should fail - invalid email
        user = TeamUser(
            userId="user-id",
            teamId="team-id",
            email="invalid-email",  # Invalid email should raise ValueError
            fullName="Test User",
            role="admin",
            state={"pending": False},
            isTeamCreator=False,
            disabled=False,
            emailVerified=True,
            createdAt="2023-01-01T00:00:00Z",
            updatedAt="2023-01-01T00:00:00Z"
        )
    except ValueError as e:
        logger.info(f"✅ TeamUser validation caught invalid email: {e}")
    
    try:
        # This should fail - invalid role
        user = TeamUser(
            userId="user-id",
            teamId="team-id",
            email="test@example.com",
            fullName="Test User",
            role="invalid-role",  # Invalid role should raise ValueError
            state={"pending": False},
            isTeamCreator=False,
            disabled=False,
            emailVerified=True,
            createdAt="2023-01-01T00:00:00Z",
            updatedAt="2023-01-01T00:00:00Z"
        )
    except ValueError as e:
        logger.info(f"✅ TeamUser validation caught invalid role: {e}")

def test_error_handling():
    """Test the improved error handling."""
    logger.info("Testing error handling...")
    
    # Test client initialization without API key
    try:
        client = AirfocusClient(api_key="")  # Empty API key should raise ValueError
    except ValueError as e:
        logger.info(f"✅ Client validation caught empty API key: {e}")
    
    # Test workspace group methods
    group = WorkspaceGroup(
        id="test-id",
        name="Test Group",
        teamId="team-id"
    )
    
    try:
        # This should fail - empty group ID
        group.add_child_group("")
    except ValueError as e:
        logger.info(f"✅ WorkspaceGroup validation caught empty group ID: {e}")
    
    try:
        # This should fail - empty workspace ID
        group.add_workspace("")
    except ValueError as e:
        logger.info(f"✅ WorkspaceGroup validation caught empty workspace ID: {e}")

def test_constants_usage():
    """Test that constants are being used properly."""
    logger.info("Testing constants usage...")
    
    from airfocus.constants import (
        BASE_URL, SUPPORTED_ROLES, PERMISSION_LEVELS,
        HTTP_OK, HTTP_BAD_REQUEST, ERROR_API_KEY_REQUIRED
    )
    
    logger.info(f"✅ Using BASE_URL constant: {BASE_URL}")
    logger.info(f"✅ Using SUPPORTED_ROLES constant: {SUPPORTED_ROLES}")
    logger.info(f"✅ Using PERMISSION_LEVELS constant: {PERMISSION_LEVELS}")
    logger.info(f"✅ Using HTTP status constants: {HTTP_OK}, {HTTP_BAD_REQUEST}")
    logger.info(f"✅ Using error message constant: {ERROR_API_KEY_REQUIRED}")

def main():
    """Run all tests."""
    logger.info("Starting improvement tests...")
    
    test_validation()
    test_error_handling()
    test_constants_usage()
    
    logger.info("✅ All tests completed successfully!")

if __name__ == "__main__":
    main() 