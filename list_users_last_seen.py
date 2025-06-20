"""
Display user names, roles, and last login times ordered by last login.
"""

import logging
from airfocus.client import AirfocusClient
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def format_time(time_str):
    """Format ISO timestamp into a readable format."""
    if not time_str:
        return "Never logged in"
    
    try:
        dt = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        logger.warning(f"Could not parse timestamp '{time_str}': {e}")
        return time_str

def list_users_by_last_login():
    """List all users by last login time."""
    try:
        client = AirfocusClient()
        
        # Get all users
        users = client.team.get_users()
        
        if not users:
            logger.info("No users found")
            return
        
        # Sort users by last login time (most recent first)
        users.sort(key=lambda u: u.lastSeenAt if u.lastSeenAt else "", reverse=True)
        
        print("\n{:<40} {:<15} {:<30}".format("User Name", "Role", "Last Seen"))
        print("-" * 85)
        
        for user in users:
            print("{:<40} {:<15} {:<30}".format(
                user.fullName[:39], 
                user.role[:14],
                format_time(user.lastSeenAt)[:29]
            ))
            
        logger.info(f"Displayed {len(users)} users")
        
    except Exception as e:
        logger.error(f"Error listing users: {e}")
        raise

if __name__ == "__main__":
    list_users_by_last_login()