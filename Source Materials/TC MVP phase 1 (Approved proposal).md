# TransCredit MVP

## 1\. Technology Stack:

### Frontend:

- **Blazor (C\#)** \- Сore frontend framework across all projects. Must align with existing portal modules and component library.  
- **Razor Components / Shared UI Kit** \- Reuse Plateau Group’s internal component library and DMZ Bootstrap-based Blazor controls.  
- **Styling Consistency** – Follow existing internal web portal (PlateauGroup.Web) standards, compiled via Web Compiler SCSS.

### Backend:

- **C\# / .NET 8 API layer** \- Business logic, data validation, workflow, audit, and integrations.  
- **Microsoft SQL Server** \- Centralised relational DB for Certificates  
- **Entity Framework Core** \- ORM for database communication.  
- **Plateau Services Layer** – Shared API for report and remittance processing.

### Deployment and Environments:

- Daily commits → feature branches → review → merge to main (repo shared with Plateau team).  
- Plateau executes the final merge and deployment via the existing internal pipeline.  
- Standard four-tier model (Dev/Test/UAT/Prod).

### Authentication / Authorisation:

- **Azure Active Directory (SSO \+ MFA)** – Confirmed as the primary auth provider for internal users.  
- **RBAC** – Role-based access controlled by Active Directory groups (APS Admin, Operators, etc.).  
- No new roles required for MVP; existing groups cover all permissions.

## 2\. Feature List:

| Feature | Description | Est., H |
| :---- | :---- | :---- |
| Certificate Creation Page Completion | Finalise the existing “Add Certificate” page: ensure all required fields are functional, enable saving new certificates to the database, and run validation on save. | 2412h |
| Certificate Editing | Enable full editing of certificate details. | 816h |
| Change Reason Tracking | Require users to provide a reason for any certificate change; allow selecting predefined reasons or entering a custom one. Record all certificate modifications (old/new values, reasons, user, date) | 1016h |
| Certificate Versioning | Maintain version history for each certificate record. Each agent enhancement round should create a new version entry capturing the full snapshot of certificate data at the time of change. Versions can be compared to highlight differences between any two states (e.g., “before vs after” view). | 1632h |
| Certificate Validation | Extend the existing validation logic (already migrated from Access) by adding remaining missing checks and enabling persistent storage of validation results in the database. Validation should run on save/update. | 816h |
| Error Storage and Management | Store validation errors in the database, track their status (open/resolved), and display them in the interface (issues tab). | 616h |
| Enhanced Certificate Search | Add extended search criteria (name, date of birth, SSN, claim number, agent) and an advanced search mode. | 8h |
| Email Integration | Implement backend tables for inbound/outbound emails and attachments; integrate with the client’s email service via DB. | 1632h |
| Email Communication UI | Improve the communications interface, add logic (Get Emails/Create an Email) | 8h |
| Error Export and Attachment | Allow users to export validation errors to Excel/CSV and attach them to outgoing emails. | 8h |

## 3\. Team Composition:

| Role | Responsibility | Allocation |
| :---- | :---- | :---- |
| Project Manager | Client communication, scope control, prioritisation, and sprint planning. | Cross |
| Business Analyst | Process mapping, requirement detailing, backlog management, user stories, and acceptance criteria. | Cross |
| Tech Lead | Defines system architecture, integration approach, API contracts, and data flow. Coordinates with Client SMEs | As needed |
| Developer FS | Builds Blazor UI, forms, and approval screens using the existing component kit. Implements APIs, workflow logic, and data access | 1 FTE |
| QA Engineer | End-to-end testing, regression, and UAT support. | As needed |

## 4\. Assumptions:

- The Certificates module will be developed inside the existing Plateau Web portal.  
- The public agent-facing portal is not in scope for this phase.  
- No new standalone web app or DB server required.  
- An OCR system is assumed to exist and provide structured data output.  
- Outbound and inbound email processing will be handled by Plateau’s internal Microsoft 365 infrastructure. The Symfa team will only manage database records.  
- All existing Access-based logic (snapshot checks, rule validations, and audit placeholders) can be accessed or exported for migration.  
- Authentication and role management will rely on existing infrastructure: Azure AD; no new identity provider is introduced.  
- Document generation and storage will leverage existing ShareFile; no new PDF/letter builder will be introduced unless Plateau explicitly requests it.  
- System non-functional goals (load, concurrency, RPO/RTO) are assumed to match existing Plateau web standards until defined otherwise.  
- All outgoing agent communications will use Plateau’s Microsoft 365 SMTP relay, routed internally for compliance.

## 5\. Risks:

- Legacy data mapping between old Access structures and the new SQL schema may require additional adjustments during migration.  
- Ownership of financial totals (which layer is authoritative) must be confirmed to prevent balancing discrepancies.  
- Legally required customer letters and notifications must follow approved templates and compliance workflows; missing templates could delay production rollout.  
- If dynamic template-based document generation is later requested, new infrastructure or integration effort may be required beyond the current MVP scope.

