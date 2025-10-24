# TransCredit - Complete Project Documentation

## 📋 Table of Contents

1. [Business Context](#business-context)
2. [Business Processes](#business-processes)
3. [System Analysis (As Is)](#system-analysis-as-is)
4. [To Be (Desired State)](#to-be-desired-state)

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

## 🚀 To Be (Desired State)

### Target System Overview
The new TransCredit system will be a modern web-based platform that addresses all current pain points through automation, enhanced communication, and comprehensive audit capabilities.

### Key Pain Points Addressed

#### 1. Manual Error Correction (95% → <20%)
**Current Problem**: Staff spend 95% of time manually correcting agent errors
**Solution**: Automated error detection and agent self-service portal
- **Automated Error Detection**: System automatically identifies all validation issues
- **Agent Self-Service**: DMZ portal allows agents to fix their own errors
- **Reduced Manual Work**: Staff focus on complex issues only

#### 2. Limited Search Capabilities
**Current Problem**: Basic search by certificate number, SSN, customer name
**Solution**: Enhanced search with multiple criteria
- **Wildcard Name Search**: First/Last name with partial matching
- **Multiple Search Fields**: Birthday, SSN, Claim Number, Certificate Number
- **Advanced Filtering**: Date ranges, status filters, agent-specific searches

#### 3. Inadequate Audit Trail
**Current Problem**: High-level logging without detailed change tracking
**Solution**: Comprehensive audit logging for all changes
- **Every Change Tracked**: Who, what, when, why for all modifications
- **Reason Required**: Mandatory reason for every change
- **Complete History**: Full audit trail for compliance and troubleshooting

#### 4. Communication Gaps
**Current Problem**: No integrated tracking of agent communications
**Solution**: Structured communication system with tracking
- **Email Integration**: Automated email generation and response parsing
- **Communication History**: Complete record of all agent interactions
- **Status Tracking**: Clear visibility into resolution progress

#### 5. System Limitations
**Current Problem**: Cannot handle non-monthly payments, birthday coverage, state regulations
**Solution**: Enhanced calculation engine with state rule automation
- **Multiple Payment Schedules**: Bi-weekly, annual, semi-annual support
- **Birthday Coverage**: Automated calculation up to 71st birthday
- **State Regulations**: Automated application of state-specific rules
- **Free Look Period**: Proper handling of 30-day cancellation periods

### New System Architecture

#### Process Diagram - Target Workflow
![TransCredit Target Process](./TransCredit%20-%20To%20Be.svg)

#### Architecture Diagram - Target System
![TransCredit Target Architecture](./TransCredit%20-%20Architecture%20-%20To%20Be.svg)

### Technology Stack Transformation

#### Current vs Target Technology

| Component | Current (As Is) | Target (To Be) |
|-----------|-----------------|----------------|
| **Frontend** | Excel-based interface | Blazor web application |
| **Backend** | MS Access with VBA | C# services with SQL Server |
| **Search** | Basic certificate/SSN search | Enhanced multi-criteria search |
| **Communication** | Email-based, no tracking | Integrated email system with DMZ portal |
| **Audit** | High-level logging | Comprehensive change tracking |
| **Error Handling** | 95% manual correction | Automated detection + agent self-service |
| **State Rules** | Manual handling | Automated application |
| **Payment Schedules** | Monthly only | Multiple schedules supported |

### New Business Process Flow

#### 1. Receive Agent Report
- **Enhanced**: Automated report processing and validation
- **Technology**: Web-based report upload with validation
- **Improvement**: Immediate error detection and feedback

#### 2. Enhanced Certificate Search
- **New Capability**: Search by name (wildcards), birthday, SSN, claim number
- **Technology**: Advanced search algorithms with multiple criteria
- **Improvement**: Faster certificate location and management

#### 3. Automated Error Detection
- **Current**: Manual "Run Snapshot" button click
- **Target**: Automated error checking with comprehensive validation
- **Technology**: Integrated error checking service
- **Improvement**: Proactive error identification

#### 4. Agent Self-Service Portal (DMZ)
- **New Feature**: Agents can fix their own errors
- **Technology**: DMZ website with Auth0 MFA authentication
- **Process**: 
  - Agent receives email with specific errors
  - Logs into DMZ portal
  - Views and edits certificates
  - Submits corrections
  - System validates changes automatically

#### 5. Automated Communication
- **Current**: Manual email communication
- **Target**: Structured email system with tracking
- **Features**:
  - Automated email generation
  - Response parsing and linking
  - Communication history tracking
  - Status monitoring

#### 6. Comprehensive Audit Logging
- **Current**: Basic logging
- **Target**: Complete change tracking
- **Features**:
  - Every change logged with reason
  - User and timestamp tracking
  - Old/New value comparison
  - Compliance reporting

#### 7. Enhanced Balancing
- **Current**: Manual reconciliation
- **Target**: Automated balancing with validation
- **Technology**: Report balancing service
- **Improvement**: Faster and more accurate financial reconciliation

### Key Benefits

#### Operational Efficiency
- **Manual Correction Time**: Reduced from 95% to <20%
- **Processing Speed**: Faster report processing and error resolution
- **Agent Satisfaction**: Self-service capabilities reduce friction
- **Staff Productivity**: Focus on complex issues, not routine corrections

#### Data Accuracy
- **Automated Validation**: Comprehensive error checking
- **State Compliance**: Automated rule application
- **Calculation Accuracy**: Enhanced payment schedule support
- **Audit Trail**: Complete change tracking for compliance

#### Communication
- **Structured Emails**: Automated generation and tracking
- **Agent Portal**: Self-service error correction
- **Status Visibility**: Clear progress tracking
- **Response Management**: Automated parsing and linking

#### Technology Modernization
- **Web-Based Platform**: Modern user interface
- **Scalable Architecture**: SQL Server backend
- **Integration Capabilities**: DMZ portal and email systems
- **Future-Proof**: Extensible platform for growth

### Implementation Impact

#### For Staff
- **Reduced Manual Work**: Focus on complex issues only
- **Better Tools**: Modern web interface with enhanced search
- **Clear Communication**: Structured agent communication
- **Complete Audit**: Full change tracking and compliance

#### For Agents
- **Self-Service Portal**: Fix errors independently
- **Clear Communication**: Structured email system
- **Faster Resolution**: Automated error detection
- **Better Support**: Enhanced communication tracking

#### For Business
- **Operational Efficiency**: Significant time savings
- **Compliance**: Automated state rule application
- **Scalability**: Modern platform for growth
- **Audit Readiness**: Complete change tracking

---

*This comprehensive documentation provides a complete overview of the TransCredit project, from high-level business context to detailed system analysis and target state, ensuring all stakeholders understand the current state, challenges, and future vision.*