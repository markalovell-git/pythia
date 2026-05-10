# Astrology App Requirements Clarification

- **Backend Services**: FastAPI will be used for backend services to ensure separation between backend and frontend.
- **Database Choice**: SQLite will be used initially, with SQLAlchemy as the ORM, allowing future migration to PostgreSQL.
- **UI Design**: Qt Designer will be used for UI design to ensure easy replacement of graphics.
- **Graphics**: Placeholder graphics ('programmer art') will be used initially, which can be easily replaced later.
- **Chart Display**: The application should support both sidereal and tropical chart displays.
- **Authentication**: Authentication will not be implemented initially.
- **Installers**: Cross-platform installers will be considered later, but the application will be structured to allow for this easily.
- **Loose Coupling**: The application will be designed with loose coupling between components for flexibility and ease of modification.