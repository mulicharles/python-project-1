# User Management Microservice
class UserManagementService:
    def _init_(self):
        self.users = {}

    def register_user(self, username, password, email):
        self.users[username] = {'password': password, 'email': email}

    def authenticate_user(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            return True
        return False

# Incident Reporting Microservice
class IncidentReportingService:
    def _init_(self):
        self.incidents = []

    def report_incident(self, username, location, incident_type, description):
        self.incidents.append({'username': username, 'location': location,
                               'type': incident_type, 'description': description})

# Main Application (Microservices Interaction)
class SecurityMonitoringSystem:
    def _init_(self):
        self.user_service = UserManagementService()
        self.incident_service = IncidentReportingService()

    def register_user(self, username, password, email):
        self.user_service.register_user(username, password, email)

    def report_incident(self, username, location, incident_type, description):
        if self.user_service.authenticate_user(username, password):
            self.incident_service.report_incident(username, location, incident_type, description)
            print("Incident reported successfully!")
        else:
            print("Authentication failed. Please check your credentials.")

# Example Usage
security_system = SecurityMonitoringSystem()

# Registering a user
security_system.register_user("user123", "password123", "user@example.com")

# Reporting an incident (assuming user logs in)
security_system.report_incident("user123", "Street A", "Break-in", "House was broken into.")

# Viewing incidents (this is a simplified example and might not be part of microservices)
print("Incidents:")
for incident in security_system.incident_service.incidents:
    print(incident)