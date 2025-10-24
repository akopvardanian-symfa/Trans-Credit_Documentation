# TransCredit - Complete Project Documentation

## 📋 Table of Contents

1. [Business Context](#business-context)
2. [Business Processes](#business-processes)
3. [System Analysis (As Is)](#system-analysis-as-is)

---

## 🏢 Business Context

### Industry Background
**Plateau Group** operates within the **credit insurance industry**, specifically managing **credit life and disability insurance** sold through banking channels. This type of insurance protects borrowers and their families in case of death or disability, ensuring loan repayment.

**TransCredit** is the internal system used by Plateau Group to process monthly reports from financial institution agents and manage certificate data.

### Business Model: How Insurance Works with Agents

#### Who are Agents in Plateau Group Context
**Agents** in this context are **financial institutions** (including banks, credit unions, and other lending organizations) that sell credit insurance to their customers when they take out loans. These are not individual insurance agents, but rather **institutions** that have agreements with Plateau Group to offer credit insurance products to their loan customers.

#### How the Insurance Business Works
1. **Customer takes a loan** from a financial institution (agent)
2. **Institution offers credit insurance** to protect the loan in case of death or disability
3. **Customer purchases insurance** as part of their loan package
4. **Institution collects premium** from customer along with loan payments
5. **Institution submits monthly reports** to Plateau Group with all insurance sales
6. **Plateau Group processes** the insurance certificates and manages the policies

#### Where TransCredit Fits In
**TransCredit** is the **internal processing system** used by Plateau Group to handle the monthly reports from financial institution agents. It's the system that Plateau Group uses to:
- **Receive monthly sales reports** from financial institutions showing all insurance sold
- **Process certificate data** for each insurance policy
- **Validate and correct errors** in the data submitted by institutions
- **Manage financial reconciliation** between what institutions sold and what they owe
- **Handle agent communication** when errors need to be corrected

### Current System Scope
The **TransCredit system** (used by Plateau Group) handles:
- **Monthly Sales Reports** from financial institution agents containing certificate data
- **Certificate Processing** including data entry, validation, and error correction
- **Financial Balancing** between agent reports and premium remittances
- **Agent Communication** for error resolution and billing adjustments
- **Compliance Management** ensuring adherence to state regulations and audit requirements

---

## 📊 Business Processes

### Current Business Process (As Is)

#### Process Diagram
![TransCredit Current Process](./TransCredit%20-%20As%20Is.svg)

#### Monthly Report Processing Workflow

Here is the detailed step-by-step process:

##### 1. Receive Monthly Sales Report
Banks and credit unions send monthly reports showing how many insurance policies they sold. The report contains: who bought insurance, how much they paid, what health information they provided. It also shows how much money the bank owes Plateau Group for the sold insurance policies.

##### 2. Assign Report Number and Description
Staff member logs into TransCredit system, creates a new report record and assigns it a number. The staff member gives the report an internal name based on how it was received:

- **Manual processing**: "August Bath" (month + city where bank is located)
- **Electronic payment**: "August ER" (month + "ER" for e-remit system)
- **Website upload**: "August Upload" (month + "Upload" for website submission)

This internal naming helps staff immediately identify how each report was received and processed.

##### 3. Enter Certificate Information into TransCredit System
Staff member enters data for each insurance certificate into the system. If a certificate has no number (bank's printing problem), they use the last 4 digits of SSN. They notify agent services about the printing issue so they can contact the bank and fix the printing problem.

**Important**: Data is entered exactly as printed, even if they know it's wrong.

##### 4. Check Health Questions Status
Staff member checks if the customer answered health questions and sets a system code in TransCredit:
- **Code "1"**: Health questions answered
- **Code "3"**: Health questions NOT answered (triggers system error)

For disability insurance, ALL health questions must be answered before the policy can be processed.

##### 5. Run Snapshot Validation
Staff member clicks "Run Snapshot" button and system checks all certificates for errors:
- Is customer too old for insurance
- Is premium calculated correctly
- Is coverage amount correct
- Is refund method correct (pro-rata or Rule 78)
- Bank platform errors
- Printing errors (extra premiums)
- Limit violations

##### 6. Error Processing (95% of work time)
If errors are found, the most time-consuming part begins. Staff spend 95% of time fixing errors that banks make. Errors happen because:
- Bank employee entered data incorrectly in their system
- Bank's system works incorrectly
- Bank's platform cannot help

When fixing errors:
1. **View error list**
2. **Enter data exactly as bank submitted** (even if they know it's wrong)
3. **Balance to original amounts** (critically important - before corrections)
4. **Create exception report** (what they changed)
5. **Update system with correct amounts**
6. **Print updated error list**
7. **Generate billing for bank** (how much they owe or get back)
8. **Notify bank of changes** (billing + explanations + customer letters)

##### 7. Run Over Limits Check
Staff member clicks "Run OLIST" button and system checks if customer exceeds coverage limits. For example, if customer already has $50,000 insurance and bank sold another $60,000, then the $100,000 limit is exceeded.

If limit exceeded:
- **Contact bank** - is old insurance still active
- **Reduce new coverage** if both are active
- **Notify customer of reduction** (legal requirement)
- **Bank can keep new insurance** if they cancel old one

##### 8. Print Report
Print main report with financial balance.

##### 9. Print Customer List
Print list of all customers in the report.

##### 10. Scan All Documents Together
Scan all documents together for archive:
- Report
- Customer list
- All supporting documents

##### 11. Complete Monthly Report Processing
Monthly report processing is completed.

### Error Correction Process (Detailed)

#### Common Error Types
1. **Age Limit Violations**: Customers too old for insurance
2. **Premium Calculation Errors**: Wrong amounts calculated by agents
3. **Coverage Amount Mistakes**: Incorrect coverage amounts
4. **Refund Method Errors**: Wrong refund calculations (pro-rata vs Rule 78)
5. **Platform Provider Errors**: System issues with agent platforms
6. **Printing Errors**: Extra premiums or incorrect data
7. **Multiple Policy Violations**: Exceeding agent coverage limits

#### Error Correction Workflow
1. **Identify Errors**: Through snapshot validation
2. **Input Original Data**: Enter exactly as agent submitted
3. **Balance to Original**: Must balance to original report numbers
4. **Make Corrections**: Apply correct calculations
5. **Document Changes**: Create exception report
6. **Notify Agent**: Send billing statement and explanations
7. **Notify Customer**: If life/disability/AD&D changed (legal requirement)

---

## 🏗️ System Analysis (As Is)

### Technology Stack Overview
- **Frontend**: Excel-based interface for data input and search
- **Backend**: MS Access database with VBA code and stored procedures
- **Communication**: Email-based with no integrated tracking
- **Manual Processes**: 95% of operations require manual intervention

### Technology Used for Each Business Process Step

#### 1. Receive Monthly Sales Report
- **Technology**: Email system, physical mail, website uploads
- **Process**: Manual receipt and sorting of reports
- **Tools**: Email clients, physical mail handling, website interface

#### 2. Assign Report Number and Description
- **Technology**: MS Access database
- **Process**: Staff logs into TransCredit system, creates new report record
- **Tools**: Access forms for data entry, internal naming system

#### 3. Enter Certificate Information into TransCredit System
- **Technology**: MS Access database with Excel interface
- **Process**: Manual data entry from certificates
- **Tools**: Excel-based forms, Access database tables
- **Data Sources**: Certificate numbers, SSN (last 4 digits), customer information

#### 4. Check Health Questions Status
- **Technology**: MS Access database with VBA code
- **Process**: Staff sets system codes (1 = answered, 3 = not answered)
- **Tools**: Access forms with dropdown codes, VBA validation logic

#### 5. Run Snapshot Validation
- **Technology**: MS Access with VBA stored procedures
- **Process**: Staff clicks "Run Snapshot" button, system scans for errors
- **Tools**: Access VBA code, database queries, error checking algorithms
- **Validations**: Age limits, premium calculations, coverage amounts, refund methods

#### 6. Error Processing (95% of work time)
- **Technology**: MS Access database, Excel for calculations, Email system
- **Process**: Manual error correction and agent communication
- **Tools**: 
  - Access forms for error list viewing
  - Excel for manual calculations
  - Email clients for agent communication
  - Manual balancing and reconciliation

#### 7. Run Over Limits Check
- **Technology**: MS Access with VBA code
- **Process**: Staff clicks "Run OLIST" button, system checks coverage limits
- **Tools**: Access VBA procedures, Form ME-SPNLD-HQA (8/12)
- **Database**: Coverage limit tables, agent agreement data

#### 8. Print Report
- **Technology**: MS Access reporting, printer system
- **Process**: Generate and print financial balance report
- **Tools**: Access report generator, printer drivers

#### 9. Print Customer List
- **Technology**: MS Access reporting
- **Process**: Generate and print customer list
- **Tools**: Access report generator

#### 10. Scan All Documents Together
- **Technology**: Scanner hardware and software
- **Process**: Physical document scanning and archiving
- **Tools**: Scanner drivers, file management system

#### 11. Complete Monthly Report Processing
- **Technology**: MS Access database
- **Process**: Mark report as completed in system
- **Tools**: Access forms for status updates

### Current System Limitations
- **Payment Schedules**: System only calculates monthly payments (not bi-weekly/annual)
- **Birthday Coverage**: System assumes max 12 months, but customers can have coverage up to 71st birthday (15+ months)
- **30-Day Free Look**: System incorrectly flags full refunds within 30 days as errors
- **State Regulations**: Manual handling required for North Carolina ("net plus three") and Kentucky (county taxes)
- **Agent Platform Issues**: Wrong refund methods, printing errors, platform provider problems

### Operational Challenges
- **Manual Error Correction**: 95% of time spent on corrections
- **Limited Search Capabilities**: Basic search by certificate number, SSN, customer name
- **Inadequate Audit Trail**: High-level logging without detailed change tracking
- **Email Communication**: No integrated tracking of agent communications
- **State-Specific Rules**: Manual notes required for different state regulations

---

## 🔧 Technical Requirements

### Current System Technology

#### Existing Technology Stack
When inputting certificate information, if there's no certificate number available, it's usually due to a printing problem with the platform provider.

- **MS Access Database**: Current backend system
- **Excel-based Interface**: Frontend for data input and search
- **VBA Code**: Business logic implementation
- **Manual Processing**: 95% of operations are manual

#### Current System Limitations

1. **Payment Schedule Limitations**:
   - System only calculates monthly payments
   - Bi-weekly payments require manual calculation
   - Annual payments require manual calculation
   - Semi-annual payments require manual calculation

2. **Birthday Coverage Limitations**:
   - System assumes maximum 12 months coverage
   - Cannot calculate birthday-based coverage (up to 71st birthday)
   - Manual calculation required for extended coverage periods

3. **Free Look Period Issues**:
   - System incorrectly flags 30-day free look refunds as errors
   - Manual override required for valid free look cancellations

4. **State Regulation Complexity**:
   - North Carolina: "net plus three" rule requires manual handling
   - Kentucky: County-specific tax rules require manual notes
   - No automated state rule application

#### Current Error Checking Process
When health questions are answered, the system runs the snapshot. If there are any errors, they are identified. If no errors, the system runs the over limits check to see if the customer has multiple policies at the institution that exceed the age limits.

- **Run Snapshot**: Manual button click to scan for errors
- **Run Over Limits Check**: Manual button click to check coverage limits
- **Manual Error Processing**: 95% of time spent on corrections
- **Manual Balancing**: Manual reconciliation of reports and remittances

### Target System Requirements

#### Technology Stack
- **Frontend**: Blazor application (`PlateauGroup.Web Project`)
- **Backend Services**: C# services (`ApsPlateau.Services project`)
- **Database**: MS SQL Server (for `apsPlateau` and `DMZ-webdata`)
- **DMZ Website**: Public portal for agents with Auth0 MFA credentials

#### Key Components (From Technical Specifications)

##### Frontend Components
- **CertificateSearch.razor**: Enhanced search capabilities
- **CertificateDetails.razor**: Certificate details with audit component
- **AgentReportPage.razor**: Agent report management with communication tab
- **CertAudit.razor**: Collapsible audit log component

##### Backend Services
- **CertificateService.cs**: Core certificate operations and search logic
- **AgentCommunicationService.cs**: Email generation and response parsing
- **ReportBalancingService.cs**: Report vs Remittance balancing
- **ErrorCheckingService.cs**: Error validation and checking

##### Database Tables (From Technical Specifications)
- **CertMaster**: Main certificate data
- **CertAudit**: Audit logging (Id, CertId, ChangedValue, RecordId, OldValue, NewValue, Reason, ChangeDate, ChangedBy)
- **AgentReportEmail**: Communication tracking (Id, AgentReportId, AgentEmail, AddedDate, IsInbound, Subject, Body, ResolvedDate, ResolvedBy)
- **AgentReportEmailAttachment**: Email attachments
- **CertError**: Error tracking
- **CompanyMaster**: Company data with RYM constraints

#### DMZ Integration (From Technical Specifications)
- **Public Portal**: For agents with Auth0 MFA authentication
- **Certificate Editing**: Agents can edit certificates directly
- **Change Tracking**: Monitor agent modifications
- **Approval Workflow**: User approval of agent changes
- **Data Cleanup**: Delete DMZ data after completion

### Functional Requirements (From Business Process Analysis)

#### Enhanced Search Capabilities
**Current Limitation**: Basic search by certificate number, SSN, customer name
**Target Requirement**: Search by first/last name (wildcards), birthday, SSN, claim number

#### Audit Logging Requirements
**Current Limitation**: High-level logging without detailed change tracking
**Target Requirement**: Detailed change tracking with reasons for all modifications

#### Error Correction Automation
**Current Limitation**: 95% manual error correction
**Target Requirement**: Automated error detection and correction

#### State Regulation Automation
**Current Limitation**: Manual handling of state-specific rules
**Target Requirement**: Automated application of state regulations

#### Payment Schedule Support
**Current Limitation**: Only monthly payment calculations
**Target Requirement**: Support for bi-weekly, annual, and other payment schedules

#### Birthday Coverage Calculation
**Current Limitation**: Cannot calculate birthday-based coverage
**Target Requirement**: Automated birthday-based coverage calculations

#### Free Look Period Handling
**Current Limitation**: System incorrectly flags 30-day free look refunds
**Target Requirement**: Proper handling of 30-day free look period

### Integration Requirements

#### Email System Integration
- **Outbound Emails**: Send emails to agents with attachments
- **Inbound Email Processing**: Parse agent responses
- **Email Tracking**: Complete audit trail of communications

#### DMZ Website Integration
- **Agent Authentication**: Auth0 MFA integration
- **Certificate Data Copying**: Copy data to DMZ for agent editing
- **Change Synchronization**: Sync changes back to main system

#### Database Integration
- **SQL Server**: Main database for apsPlateau
- **DMZ Database**: Temporary storage for agent editing
- **Data Synchronization**: Between main system and DMZ


---

*This comprehensive documentation provides a complete overview of the TransCredit project, from high-level business context to detailed technical requirements, ensuring all stakeholders understand the current state, challenges, and opportunities for improvement.*
