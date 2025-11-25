# TransCredit - Complete Project Documentation

## 📋 Table of Contents

1. [Glossary](#glossary)
2. [Business Context](#business-context)
3. [Business Processes](#business-processes)
4. [System Analysis (As Is)](#system-analysis-as-is)
5. [To Be (Desired State)](#to-be-desired-state)

---

## 📖 Glossary

### Key Terms and Definitions

**TransCredit System**: The primary operational application used by Plateau Group for processing credit insurance. Built on Microsoft Access frontends and SQL Server backends, it handles the business after insurance policies are sold by partner banks, finance companies, or credit unions.

**E-remits (Electronic Remit)**: Data files received from finance companies that are directly loaded into the system via import. These are text data files containing transaction information (issue and cancellation transactions) that can be imported to create a batch of certificates automatically, rather than requiring manual data entry.

**Issue Transaction**: The process of recording a new insurance policy. Represented as Trans Type = 10 in the system. Includes entering certificate number, customer information, loan details, plan codes, and premium amounts.

**Cancellation Transaction**: The process of recording the termination of an insurance policy, often due to early loan payoff, charge-off, or refinancing. Represented as Trans Type = 20 in the system. System automatically calculates premium refund based on cancellation date.

**Premium**: The amount of money the end-user pays for insurance coverage, which is financed with the loan. The end-user pays the bank, and the bank pays Plateau Group.

**Commission**: A percentage of the premium that the bank retains. Commission rates vary by plan type (commonly 60%, 53%, or other rates per agent agreement). Banks typically retain commission upfront before remitting net premium to Plateau Group.

**Claim**: A request made by an insured person (or their beneficiary) for payment of benefits under an insurance policy. Claims can be for life insurance (death) or disability insurance. All claim information is manually entered into the system; there are no automated integrations for claim verification with external medical databases.

**Agent Summary Report**: A financial report that tallies all issue and cancellation transactions for an agent report. Shows the total issued, total canceled, net difference, retained commission by the bank, and the net amount remitted to Plateau Group. Used for balancing reports and understanding financial transactions with agent partners.

**Error List**: A report generated for any discrepancies or out-of-tolerance amounts found during validation. Assists users in correcting errors and ensuring data accuracy. Generated after running snapshot validation.

**Customer Letters**: Legal notifications sent to customers about policy-related information after corrections and balancing. Required by law when life/disability/AD&D coverage or premium amounts are changed. Created outside the system and sent via mail.

**C-List (Customer List)**: A comprehensive table containing all issued policies for a report. Includes transaction information (trans type, dates, premiums), customer information, and coverage details. Provides complete audit trail of all transactions processed for a report.

**DMZ (Demilitarized Zone) Portal**: An external, agent-facing web portal separated from the internal system. Uses Auth0 authentication (MFA) and provides secure access for agents to upload certificates and review pending reports. Currently used for certificate uploads; self-correction functionality is postponed.

**RBAC (Role-Based Access Control)**: Access control system managed through Azure Active Directory groups. Roles include APS Admin (full administrative access including admin screen), Operators (main operational access for processing certificates), and Reviewers (approval workflow when implemented).

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
5. **Commission Retention**: Bank typically retains commission upfront before remitting to Plateau Group
6. **Institution submits monthly reports** to Plateau Group with all insurance sales
7. **Plateau Group processes** the insurance certificates and manages the policies

#### Financial Flow and Commission Structure
- **Premium Payment**: End user pays premium to bank → bank pays Plateau Group
- **Commission Rates**: Vary by plan type (commonly 60%, 53%, or other rates per agent agreement)
- **Commission Retention**: Banks usually retain commission upfront, then remit net premium to Plateau
- **Adjustment Handling**: When adjustments are needed (e.g., refunds), both Plateau and bank share the cost proportionally based on commission rate
- **Remittance**: Banks send "agent remit" amount (total premium minus retained commission) to Plateau Group

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
- **Cancellation Processing** handling policy cancellations and refund calculations
- **Claims Processing** managing insurance claims (life and disability) from insured customers
- **Financial Balancing** between agent reports and premium remittances
- **Agent Communication** for error resolution and billing adjustments
- **Compliance Management** ensuring adherence to state regulations and audit requirements

---

## 📊 Business Processes

### Current Business Process (As Is)

#### Process Diagram
![TransCredit Current Process](./TransCredit_As_Is.svg)

#### Monthly Report Processing Workflow

Here is the detailed step-by-step process:

#### 1. **Receive Monthly Sales Report**

**Current Process: Fully Manual**

Banks and credit unions send monthly reports showing how many insurance policies they sold. The report contains: who bought insurance, how much they paid, what health information they provided. It also shows how much money the bank owes Plateau Group for the sold insurance policies.

**How Reports Are Received:**
- **Primary Method**: Reports are received via **email** (completely manual process)
- **Operational Staff**: Staff member manually checks email inbox
- **Report Formats**: 
  - Excel files attached to emails
  - Text data files (e-remits) attached to emails
  - Paper documents (still common - no digital version)
- **No Automation**: There are **no API integrations** with external systems
- **No Automatic Processing**: Staff must manually open email, download attachments, and review contents

**Report Types:**
- **Manual Reports**: Paper documents or Excel files requiring manual data entry
- **E-remits (Electronic Remits)**: Text data files that can be imported into the system (but import is still done manually by staff)
- **Website Uploads**: Some agents upload reports via website (still requires manual processing)

**Current Limitations:**
- All report receipt is **100% manual** - no automated email processing
- Staff must manually open each email and download attachments
- No automatic routing or categorization of incoming reports
- No integration with email systems for automatic extraction

#### 2. **Assign Report Number and Description**
Staff member logs into TransCredit system, creates a new report record and assigns it a number. The staff member gives the report an internal name based on how it was received:

- **Manual processing**: "August Bath" (month + city where bank is located)
- **Electronic payment**: "August ER" (month + "ER" for e-remit system)
- **Website upload**: "August Upload" (month + "Upload" for website submission)

This internal naming helps staff immediately identify how each report was received and processed.

#### 3. **Enter Certificate Information into TransCredit System**

Staff member enters data for each insurance certificate into the system. If a certificate has no number (bank's printing problem), they use the last 4 digits of SSN. They notify agent services about the printing issue so they can contact the bank and fix the printing problem.

**Data Entry Methods:**

**Method A: Manual Entry (Manual Reports)**
- Staff member manually opens email attachment (Excel file) or paper document
- Staff reviews data in the file/document
- Staff manually enters each certificate through Access forms
- Staff builds up a batch of certificates manually
- Process includes fact-checking during manual input (e.g., maximum term, number of customers for single plan type)

**Method B: E-remit Import (Electronic Remits)**
- Staff member receives email with text data file attachment
- Staff manually downloads the e-remit file
- Staff manually imports the file into the system via import function
- System automatically creates a batch from the imported file
- Batch is then processed (but import itself is still done manually by staff)

**Note**: Even for e-remits, the import process is **manual** - staff must manually trigger the import. There is no automatic processing of incoming emails or automatic file import.

**Certificate Data Entry Fields:**
- **Certificate Number**: From agent (or last 4 digits of SSN if missing)
- **Branch**: Bank/credit union branch (optional)
- **Officer Initials**: Loan officer initials (optional)
- **Issue Date**: Date when certificate was issued
- **Maturity**: Either maturity date OR term (number of payments) - mutually exclusive
- **Loan Type**: Usually pulled in from e-remits, not manually entered
- **Amount Financed**: Loan amount
- **Interest Rate**: Loan interest rate
- **Balloon Loan Indicator**: If final payment is greater than normal payment amount
- **Form Information**: State-specific form identifier (e.g., Alabama form)
- **Customer Information**: First name, last name, SSN, date of birth (auto-calculates age)
- **Secondary Borrower**: If applicable, secondary borrower information
- **Plan Codes**: Different insurance products (single/joint life, disability, property, auto)
  - Single level life, Joint level life
  - Single net pay life, Joint net pay life
  - Single seven-day disability, Single 30-day disability
  - Dual interest personal property
  - Single interest auto
  - Regular vehicle physical damage
  - Forced place vehicle physical damage
- **Multiple Plans**: Can add multiple plans (plan 1, plan 2, plan 3) to same certificate

**Important**: Data is entered exactly as printed, even if they know it's wrong.

#### 4. **Check Health Questions Status**
Staff member checks if the customer answered health questions and sets a system code in TransCredit:
- **Code "1"**: Health questions answered
- **Code "3"**: Health questions NOT answered (triggers system error)

For disability insurance, ALL health questions must be answered before the policy can be processed.

#### 5. **Run Snapshot Validation**
Staff member clicks "Run Snapshot" button and system checks all certificates for errors:
- Is customer too old for insurance
- Is premium calculated correctly
- Is coverage amount correct
- Is refund method correct (pro-rata or Rule 78)
- Bank platform errors
- Printing errors (extra premiums)
- Limit violations

#### 6. **Error Processing (95% of work time)**
If errors are found, the most time-consuming part begins. Staff spend 95% of time fixing errors that banks make. Errors happen because:
- Bank employee entered data incorrectly in their system
- Bank's system works incorrectly
- Bank's platform cannot help

When fixing errors:
##### 6.1 **View error list**
##### 6.2 **Enter data exactly as bank submitted (even if they know it's wrong)**
##### 6.3 **Balance to original amounts (critically important - before corrections)**
##### 6.4 **Create exception report (what they changed)**
##### 6.5 **Update system with correct amounts**
##### 6.6 **Print updated error list**
##### 6.7 **Generate billing for bank (how much they owe or get back)**
##### 6.8 **Notify bank of changes (billing + explanations + customer letters)**

#### 7. **Run Over Limits Check**
Staff member clicks "Run OLIST" button and system checks if customer exceeds coverage limits. For example, if customer already has $50,000 insurance and bank sold another $60,000, then the $100,000 limit is exceeded.

**Business Context - Multiple Policies Active:**
This process addresses the situation where a customer has multiple active insurance policies that may exceed the agent's coverage limits. Each agent (bank/credit union) has a maximum coverage limit per customer (e.g., $100,000). When a customer takes a new loan and the bank offers insurance, the system must check if the total coverage would exceed the agent's limits.

**Business Logic:**
- **Agent Coverage Limits**: Each agent has maximum coverage limits per customer
- **Multiple Policies Problem**: Customer may have existing policies from other banks
- **Exceeded Limits**: New policy + existing policies > agent's maximum limit
- **Resolution Required**: Agent must either reduce new coverage or confirm old policies are cancelled

If limit exceeded:
- **Contact bank** - is old insurance still active
- **If Multiple Policies Active = YES**: Reduce new coverage to stay within limits
- **If Multiple Policies Active = NO**: Bank can proceed with new policy
- **Notify customer of reduction** (legal requirement if coverage is reduced)
- **Bank can keep new insurance** if they cancel old one

**Practical Example:**
##### 1. **Customer John has $50,000 insurance through Bank A**
##### 2. **Takes new loan at Bank B for $80,000**
##### 3. **Bank B offers $80,000 insurance**
##### 4. **System checks: $50,000 + $80,000 = $130,000 > Bank B's $100,000 limit**
##### 5. **Bank B must either reduce insurance to $50,000 or confirm Bank A's policy is cancelled**

#### 8. **Print Report**
Print main report with financial balance.

#### 9. **Print Customer List**
Print list of all customers in the report.

#### 10. **Scan All Documents Together**
Scan all documents together for archive:
- Report
- Customer list
- All supporting documents

#### 11. **Complete Monthly Report Processing**
Monthly report processing is completed.

### Data Output

The TransCredit system generates several key outputs during and after report processing:

#### 1. **Agent Summary Report**

**Purpose**: Financial summary that tallies all issue and cancellation transactions for an agent report.

**Contents**:
- **Total Issued**: Sum of all issue transactions (new policies)
- **Total Canceled**: Sum of all cancellation transactions
- **Net Difference**: Difference between issued and canceled amounts
- **Retained Commission**: Commission amount kept by the bank
- **Net Amount Remitted**: Final amount sent to Plateau Group (total premium minus retained commission)
- **Level 2 Commission**: Rare commission type, if applicable

**Usage**:
- Helps in balancing reports
- Understanding financial transactions with agent partners
- Verifying that calculations match agent's reported amounts
- Determining final remittance amount

**When Generated**: After all transactions (issues and cancellations) are entered and processed.

#### 2. **Error List**

**Purpose**: Report generated for any discrepancies or out-of-tolerance amounts found during validation.

**Contents**:
- List of all validation errors found during snapshot validation
- Error types (age limits, premium calculations, coverage amounts, refund methods, etc.)
- Certificate numbers with errors
- Specific error descriptions
- Calculated vs. reported amounts (for tolerance violations)

**Usage**:
- Assists users in correcting errors
- Ensures data accuracy
- Guides staff in identifying which certificates need correction
- Used for communication with agents about discrepancies

**When Generated**: After running "Run Snapshot" validation process. Can be regenerated after corrections are made.

**Error Types Include**:
- Age limit violations
- Premium calculation errors
- Coverage amount mistakes
- Refund method errors (pro-rata vs Rule 78)
- Platform provider errors
- Printing errors
- Multiple policy violations

#### 3. **Customer Letters**

**Purpose**: Legal notifications sent to customers about policy-related information after corrections and balancing.

**When Required**:
- **Legal Requirement**: Must be sent when life/disability/AD&D coverage or premium amounts are changed
- After corrections are made that affect customer's policy
- When coverage is reduced due to limit exceedances
- When premium adjustments are made

**Contents**:
- Notification of changes to policy
- Explanation of corrections made
- Updated coverage or premium information
- Legal compliance language

**Process**:
- Letters are created **outside the system** (not generated by TransCredit)
- Manually composed and formatted
- Printed and mailed to customers
- Required for legal compliance

**Note**: Customer letters are a crucial output for notifying customers about policy-related information after corrections and balancing, ensuring legal compliance with insurance regulations.

### Cancellation Processing

#### Process Diagram
![TransCredit Cancellation Process](./TransCredit_Cancellation_Process.svg)

#### When Policies Are Cancelled
Cancellations occur for various reasons:
- **Loan paid off early**: Customer pays loan before maturity
- **Loan charged off**: Bank writes off the loan as uncollectible
- **Refinanced**: Loan refinanced into new loan
- **Life claim paid**: When life claim is paid, disability plan is cancelled

#### Cancellation Workflow
1. **Find Certificate**: System automatically finds last certificate by agent number and pre-fills certificate information
2. **Enter Cancel Date**: Staff enters cancellation date
3. **Automatic Refund Calculation**: System calculates premium refund based on cancellation date
4. **Enter Bank Amount**: Staff enters refund amount provided by bank
5. **Tolerance Check**: System checks if bank amount is within tolerance:
   - **Within tolerance**: System accepts the amount
   - **Out of tolerance**: System flags as error (will show in error list)
6. **Error Handling**: If refund amount exceeds original premium or is significantly different, error appears in error list with calculated amount

**Note**: Cancellations are processed as transactions (trans type = 20) and appear in the C-List (Customer List) report.

### Transaction Processing and C-List

#### C-List (Customer List) Report
The C-List is a comprehensive table containing all issued policies for a report. It includes:

**Transaction Information:**
- **Agent Information**: Agent number and details
- **Certificate**: Certificate number
- **Cert ID**: Internal certificate identifier
- **Plan Code**: Insurance plan type
- **Trans Type**: 
  - 10 = Issue (new policy)
  - 20 = Cancellation
- **Trans Date**: Effective date of transaction
- **Trans Premium**: Amount collected (for issues) or refunded (for cancellations)
- **Trans RYM**: Reporting Year Month (when transaction was reported)

**Customer Information:**
- **Primary/Secondary Indicators**: P = Primary, S = Secondary
- **Customer Name**: First and last name
- **SSN**: Social Security Number
- **Date of Birth**: Customer birth date
- **Age**: Auto-calculated from DOB

**Coverage Details:**
- **Risk Codes**: Risk classification
- **State**: State where policy is issued
- **Risk Forms**: Form identifiers
- **Benefit Amount**: Insurance coverage amount
- **Premium Amount**: Premium charged
- **Commission Rates**: Varies by plan (e.g., 60%, 53%)
- **Issue Date**: When policy was issued
- **Maturity Date**: When policy matures

**Purpose**: The C-List provides complete audit trail of all transactions processed for a report, used for balancing, reporting, and compliance.

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

### Claims Processing Workflow

Claims processing is a separate module within the TransCredit Access frontend. This process handles insurance claims from insured customers when death or disability occurs.

#### 1. **Receive Claim Information**
Claims are received from agents (banks) through various channels:
- **Claim Form**: Completed claim form submitted by customer/agent
- **Email**: Claim information sent via email
- **Fax**: Claim documents faxed to Plateau Group
- **ShareFile**: Documents uploaded to ShareFile system
- **Physical Mail**: Paper documents sent by mail

**Note**: There are no API integrations for claims. All claim information is manually entered into the system.

#### 2. **Search for Customer Coverage**
Staff must first locate the customer's active insurance certificate in the system. Search options include:
- **Social Security Number (SSN)**: Search by full or partial SSN
- **Name**: Search by customer first and last name
- **Existing Claim**: Search if customer already has a claim
- **Certificate Number**: Search by certificate number

**Verification Steps:**
- Verify certificate status = 1 (active)
- Check issue date matches
- Confirm customer information matches claim form
- View certificate details to ensure correct person

#### 3. **Create Claim Record**
Once correct certificate is identified:
- **Select Plan Type**: Choose Life or Disability plan (certificate may have multiple plans)
- **Automatic Claim Number**: System automatically assigns unique claim number
- **Claim Date**: 
  - For Life claims: Date of death
  - For Disability claims: Date disability began
- **File Date**: Automatically set to today's date (date claim was filed)

#### 4. **Enter Claim Details**
Staff enters comprehensive claim information:

**Basic Information:**
- **Reason for Death/Disability**: Select from predefined codes
- **Occupation**: Customer's occupation
- **Lien Holder**: 
  - Search for existing lien holder in system
  - If not found, add new lien holder
- **Cause**: Specific cause of death or disability
- **Loan Number**: Loan number associated with the certificate

**Customer Information:**
- **Primary/Secondary Indicator**: P = Primary, S = Secondary (must match certificate)
- **Address**: Customer address
- **Phone Number**: Contact information (if available)

**Additional Fields:**
- Some fields are rarely used but available if needed

#### 5. **Claim Verification Process**

**Life Claims:**
- **Required Documentation**: Death certificate must be provided
- **Manual Verification**: Staff manually reviews death certificate
- **Fraud Detection**: If claim looks suspicious, staff contacts relevant parties to verify
- **Verification Methods**: 
  - Review death certificate authenticity
  - Check for stamps, official seals
  - Verify information matches claim form

**Disability Claims:**
- **Required Documentation**: Doctor's section must be completed
- **Manual Verification**: Staff reviews doctor's completion
- **Verification Indicators**:
  - Doctor's office stamp
  - Professional formatting
  - Medical records (if provided)
- **Fraud Detection**: If suspicious, staff contacts doctor's office to verify
- **Verification Methods**:
  - Review doctor's handwriting and stamps
  - Verify physician information
  - Contact doctor's office if needed

**Note**: There is no automated integration with federal medical databases or death registries. All verification is manual.

#### 6. **Save and Process Claim**
- **Save Claim**: Click save button to store claim in database
- **Print Privacy Statement**: System can print privacy statement to mail to customer (legal requirement)
- **Claim Appears on Certificate**: Once saved, claim is visible on certificate record

#### 7. **Claim Payment Process**
- **Payment Method**: Claims are paid through the bank (agent), not directly to customer
- **Bank Receives Payment**: Plateau Group pays bank, bank then pays customer
- **Payment Tracking**: Payment information tracked in system

#### 8. **Claim Management**
- **Update Claims**: Staff can update claim information if additional details are received
- **Correct Errors**: If wrong claim date or codes entered, staff can correct and save
- **Delete Claims**: Claims can be deleted if entered incorrectly (within same month)
- **View Claim History**: All claims associated with certificate are visible

**Business Rules:**
- Each certificate can have multiple claims (e.g., life claim and disability claim)
- Claims are permanently associated with certificate
- Claim number is unique and automatically generated
- All claim data is stored in claim master table

---

## 🏗️ System Analysis (As Is)

### Technology Stack Overview
- **Frontend**: Microsoft Access frontends (separate applications for TransCredit, Term Life, Group Mortgage)
- **Backend**: SQL Server databases with shared tables (cert master, cert names, cert)
- **Modules**: TransCredit includes Certificate Processing and Claims Processing modules within same Access frontend
- **Communication**: Email-based with no integrated tracking
- **Manual Processes**: 95% of operations require manual intervention

**System Architecture Notes:**
- **Separate Frontends**: TransCredit, Term Life, and Group Mortgage are separate Access frontend applications
- **Shared Database Tables**: All three systems use common tables (cert master, cert names, cert) for consistency
- **Historical Context**: Term Life and Group Mortgage were created in 2014-2015 as copies of APS TransCredit, customized for their specific workflows
- **Consolidation Plans**: Term Life and Group Mortgage will be combined back into TransCredit as modules within a unified frontend
- **Database Structure**: Main tables are consistent across all four databases (TransCredit, Term Life, Group Mortgage, Extend Plus, PTS)

### Technology Used for Each Business Process Step

#### 1. Receive Monthly Sales Report
- **Technology**: Email system, physical mail, website uploads
- **Process**: **Fully manual** receipt and sorting of reports
  - Staff manually checks email inbox
  - Staff manually opens each email
  - Staff manually downloads attachments (Excel files, text files)
  - Staff manually reviews file contents
  - **No automated email processing**
  - **No API integrations** with external systems
- **Tools**: Email clients, physical mail handling, website interface
- **Current Limitations**: 
  - 100% manual process - no automation
  - No automatic email routing or categorization
  - No integration with email systems for automatic extraction

#### 2. Assign Report Number and Description
- **Technology**: MS Access database
- **Process**: Staff logs into TransCredit system, creates new report record
- **Tools**: Access forms for data entry, internal naming system

#### 3. Enter Certificate Information into TransCredit System
- **Technology**: MS Access database with Access forms
- **Process**: Manual data entry from certificates or imported data files
- **Tools**: Access forms for data entry, Access database tables
- **Data Sources**: 
  - **Manual entry**: Certificate numbers, SSN (last 4 digits), customer information
    - Staff manually opens email attachment (Excel file) or paper document
    - Staff reviews data and manually enters through Access forms
    - Staff builds batch manually
  - **E-remit import**: Text data files imported into system
    - Staff manually downloads e-remit file from email
    - Staff manually triggers import function
    - System automatically creates batch from imported file
    - **Note**: Even e-remit import is manual - staff must manually trigger it
- **Import Capability**: Can import data files which create batch automatically, but import process itself is manual
- **Fact-Checking**: System performs fact-checking during manual input (e.g., maximum term, number of customers for single plan type)

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

### Database Behavior

#### Data Persistence
- **Save Mechanism**: Data is saved to SQL Server database only when user clicks "Save" button
- **No Auto-Save**: There is no automatic saving while form is open
- **Data Loss Risk**: If user exits without saving, data must be re-entered
- **Recovery**: If system crashes before save, user must restart from beginning of that step

#### Data Versioning
- **No Transaction History**: System does not maintain version history of changes
- **Direct Updates**: Changes update the original record directly (no separate version records)
- **Exception**: Additional payments create new transaction records, but claim master and certificate data update original records
- **Audit Limitation**: Cannot see what data was before a change was made (no before/after comparison)

#### Data Protection
- **Delete Restrictions**: Claims can only be deleted within the same month they were created
- **Update Capability**: Staff can update claim information if additional details are received
- **Error Correction**: If wrong information entered, staff can correct and save

### External Integrations

#### Data Input Methods
- **No API Integrations**: System does not have API connections with banks or external systems
- **Fully Manual Report Receipt**: 
  - Reports received via **email** (100% manual - staff manually checks inbox, opens emails, downloads attachments)
  - Staff manually reviews Excel files or text files
  - **No automated email processing** - no automatic extraction or routing
  - **No automatic file import** - even e-remits require manual trigger by staff
- **Manual Entry**: Primary method for certificate data entry
  - Staff manually opens email attachments or paper documents
  - Staff manually enters data through Access forms
  - Staff manually builds batches
- **File Import (E-remits)**: 
  - E-remit text files can be imported (creates batch automatically)
  - **But import is still manual** - staff must manually download file and trigger import
  - No automatic processing of incoming e-remit files
- **Email**: Claims and corrections received via email (manually processed)
- **Fax**: Claim documents received via fax (manually entered)
- **ShareFile**: Documents uploaded to ShareFile (manually processed)
- **Physical Mail**: Paper documents received by mail (manually entered)

#### Verification Systems
- **No Automated Verification**: No integration with federal medical databases or death registries
- **Manual Verification Only**: All claim verification is done manually by staff
- **Document Review**: Staff reviews physical documents (death certificates, doctor forms)
- **Phone Verification**: Staff may call doctor's offices or other parties to verify claims

### Commission and Premium Flow

#### Financial Flow Structure
1. **End User → Bank**: Customer pays premium to bank along with loan payment
2. **Bank → Plateau Group**: Bank pays Plateau Group (usually retains commission upfront)
3. **Commission Retention**: Bank typically keeps commission portion upfront before remitting to Plateau

#### Adjustment Calculations
When adjustments are made (e.g., $50 due back to customer):
- **Total Adjustment**: $50
- **Commission Split**: If commission rate is 50%:
  - **Plateau Provides**: $25 (50% of adjustment)
  - **Bank Provides**: $25 (50% of adjustment)
- **Customer Receives**: Full $50 adjustment applied to loan

#### Commission Rates
- **Variable Rates**: Different commission rates apply to different plan types
- **Common Rates**: 60%, 53% (varies by plan and agent agreement)
- **Level 2 Commission**: Rare commission type, but exists in system
- **Retained Commission**: Bank retains commission upfront, remits net premium to Plateau

#### Remittance Process
- **Agent Remit**: Amount bank sends to Plateau after retaining commission
- **Net Calculation**: Total premium minus retained commission equals agent remit
- **Balancing**: System balances report totals against remittance amounts

### Operational Challenges
- **Fully Manual Report Receipt**: 100% manual process - staff must manually check email, download attachments, and review files. No automated email processing or API integrations.
- **Manual Error Correction**: 95% of time spent on corrections
- **Manual Data Entry**: Even e-remit imports require manual trigger by staff - no automatic processing
- **Limited Search Capabilities**: Basic search by certificate number, SSN, customer name
- **Inadequate Audit Trail**: High-level logging without detailed change tracking (no version history)
- **Email Communication**: No integrated tracking of agent communications
- **State-Specific Rules**: Manual notes required for different state regulations
- **No Data Versioning**: Cannot track changes over time or see historical data states
- **Manual Claims Verification**: No automated verification systems for claims
- **No Automated Report Processing**: Reports must be manually opened, reviewed, and processed by staff

---

## 🚀 To Be (Desired State)

### Process Diagram

![TransCredit To Be Process](./TransCredit%20-%20To%20Be.svg)

### MVP Phases Overview

The TransCredit MVP is structured in multiple phases to enable incremental delivery:

* **MVP Phase 1 (In Progress)**: Focuses on core certificate input, validation, and editing functionality. This phase establishes the foundation for certificate management with validation logic, versioning, and basic editing capabilities. OCR integration works automatically as a byproduct of this work.

* **MVP Phase 2 (Next Focus)**: Builds upon Phase 1 to add error visualization and correction workflows. Priority order: Error Summary UI → Certificate Editing (Error Correction Flow) → Cert QA Review UI. Note: Error Storage and Management, Email Communication UI, and Certificate Error Checking Service are already included in Phase 1.

* **Future Phases**: Additional features such as Correction & Approval Workflow, Balancing Module enhancements, and other advanced capabilities will be addressed after core components are complete.

This phased approach allows development to proceed on Phase 1 while business requirements are being gathered for subsequent phases.

### Technology Stack (MVP)

Frontend:
* Blazor (C#) - Сore frontend framework across all projects. Must align with existing portal modules and component library.
* Razor Components / Shared UI Kit - Reuse Plateau Group’s internal component library and DMZ Bootstrap-based Blazor controls.
* Styling Consistency – Follow existing internal web portal (PlateauGroup.Web) standards, compiled via Web Compiler SCSS.

Backend:
* C# / .NET 8 API layer - Business logic, data validation, workflow, audit, and integrations.
* Microsoft SQL Server - Centralised relational DB for Certificates
* Entity Framework Core - ORM for database communication.
* Plateau Services Layer – Shared API for report and remittance processing.

Deployment and Environments:
* The main repo contains both the Internal and DMZ projects.
* Daily commits → feature branches → review → merge to main (repo shared with Plateau team).
* Plateau executes the final merge and deployment via the existing internal pipeline.
* Standard four-tier model (Dev/Test/UAT/Prod).

Authentication / Authorisation:
* Azure Active Directory (SSO + MFA) – Confirmed as the primary auth provider for internal users.
* RBAC – Role-based access controlled by Active Directory groups (APS Admin, Operators, etc.).
* No new roles required for MVP; existing groups cover all permissions.
* Note: DMZ portal already exists and uses Auth0; not part of Phase 1 scope.

Integrations:
* DocMgmt & OCR - Existing document ingestion system with PSI scanners and AI OCR. OCR works automatically via shared components with manual certificate UI (no separate integration work needed).
* Email Service – Microsoft 365 SMTP; outbound queued in Plateau DB and processed internally. Backend code ready (Ammon finishing network services setup).
* Note: DMZ → Internal Sync not in Phase 1 scope (DMZ portal already exists).

### Feature List (MVP)

The MVP is divided into multiple phases. Phase 1 focuses on core certificate input and validation functionality, while Phase 2 adds error management and correction workflows.

#### 🟢 MVP Phase 1 (In Progress)

| Feature | Description | Est., H |
|---|---|---|
| Certificate Creation Page Completion | Finalise the existing "Add Certificate" page: ensure all required fields are functional, enable saving new certificates to the database, and run validation on save. UI is mostly complete; needs connection to DI Certificate Service and data persistence. | 12h |
| Certificate Editing | Enable full editing of certificate details. Base functionality for editing certificates. | 8h |
| Change Reason Tracking | Require users to provide a reason for any certificate change; allow selecting predefined reasons or entering a custom one. Record all certificate modifications (old/new values, reasons, user, date). | 10h |
| Certificate Versioning | Maintain version history for each certificate record. Each agent enhancement round should create a new version entry capturing the full snapshot of certificate data at the time of change. Versions can be compared to highlight differences between any two states (e.g., "before vs after" view). | 16h |
| Certificate Validation | Extend the existing validation logic (already migrated from Access) by adding remaining missing checks and enabling persistent storage of validation results in the database. Approximately 80% of checks are implemented in DI; remaining ones need to be ported from Access. Validation should run on save/update. | 8h |
| Error Storage and Management | Store validation errors in the database, track their status (open/resolved), and display them in the interface (issues tab). | 6h |
| Enhanced Certificate Search | Add extended search criteria (name, date of birth, SSN, claim number, agent) and an advanced search mode. | 8h |
| Email Integration | Implement backend tables for inbound/outbound emails and attachments; integrate with the client's email service via DB. **Symfa work (16h)**: Create DB tables for emails and attachments. **Ammon work**: Backend service that interacts with Exchange server (reads/writes to Symfa's tables) - Ammon finishing network services setup. | 16h |
| Email Communication UI | Improve the communications interface, add logic (Get Emails/Create an Email). | 8h |
| Error Export and Attachment | Allow users to export validation errors to Excel/CSV and attach them to outgoing emails. | 8h |
| OCR Ingestion Integration | OCR system already exists and works automatically via shared components with manual certificate UI. No separate work needed - will work as a byproduct of Phase 1 validation work. | Automatic byproduct |

**Note:** OCR integration works automatically because it uses the same components as the manual certificate creation page. As Phase 1 validation and controls are built, OCR will automatically benefit from the same error checks and validations.

#### 🟡 MVP Phase 2 (Next Focus - Priority Order)

| Task | Feature | Description | Status |
|---|---|---|---|
| 1 | Error Summary UI | Screen for grouped certificate errors (by type, severity) with drill-down. Loads from cert error table. This is the recommended starting point for Phase 2. | UI ready; needs cert error table |
| 2 | Certificate Editing (Error Correction Flow) | Integration with Error Summary UI to correct errors. When operators see errors, they click to open certificate edit page, make corrections, save, and errors are marked as cleared. Uses Phase 1 editing functionality. | Uses Phase 1 editing |
| 3 | Cert QA Review UI | QA review of OCR data (Pass/Fail) and promotion to APS Plateau. UI is ready; needs testing with new validation logic. | UI ready; needs testing |
| 3 | Certificate Import & Idempotency | Controlled import/update of certificates after QA Pass. Handled as part of QA Review flow. | Part of QA Review flow |




#### ⏸️ Future Phases / Later

| Feature | Description | Status |
|---|---|---|
| Correction & Approval Workflow | Side-by-side comparison (DMZ vs APS), approve/reject flow. Postponed until much later, if ever. | Postponed |
| Balancing Module | Transaction and totals reconciliation logic. Happy path works, but mismatched cases need business review with Tanya. Needs expansion. | Needs business alignment |
| Change Reason Tracking | Mandatory reason/comment when editing certificate data. Will be part of future Correction Workflow. | Future phase |
| Enhanced Certificate Search | Advanced search filters (DOB, SSN, agent, etc.). Not in current focus. | Future phase |
| Error Export and Attachment | Export errors to Excel/CSV and attach to outgoing emails. Planned later. | Future phase |

#### ✅ Already Complete / No Action Required

| Feature | Description | Status |
|---|---|---|
| DMZ Certificates Portal | External portal for agents to upload and review pending reports. | Already exists and working |
| Agent Notification | Automatic notifications to agents. | Working and complete |
| OpsLog Unification & Events | System event tracking (creation, QA, corrections, etc.). Fully implemented and reusable. | Fully implemented |
| Email Server | Microsoft 365 SMTP backend service. | Configured by Ammon |
| Email Integration (Backend Service) | Backend service code ready; Ammon finishing network services setup. This service reads/writes to DB tables that Symfa creates in Phase 1. | Ammon completing setup |

#### ⏸️ Out of Scope

| Feature | Description | Status |
|---|---|---|
| DMZ Certificate Update Forms | External forms for agents to correct certificates. Dropped - agents won't edit through DMZ. Manual handling only. | Out of scope |

### Team Composition (MVP)

| Role | Responsibility | Allocation |
|---|---|---|
| Project Manager | Client communication, scope control, prioritisation, and sprint planning. | Cross |
| Business Analyst | Process mapping, requirement detailing, backlog management, user stories, and acceptance criteria. | Cross |
| Tech Lead | Defines system architecture, integration approach, API contracts, data flow. Coordinates with Client SMEs | As needed |
| Developer FS | Builds Blazor UI, forms, dashboards, and approval screens using the existing component kit.<br>Implements APIs, workflow logic, and data access | 1 FTE |
| QA Engineer | End-to-end testing, regression, and UAT support. | As needed |

### Assumptions (MVP)

* The Certificates module will be developed inside the existing Plateau Web portal.
* The public agent-facing portal (DMZ) is not in scope for Phase 1; DMZ Certificates Portal already exists and is working.
* No new standalone web app or DB server required.
* An OCR system exists and provides structured data output. OCR integration works automatically via shared components with manual certificate UI - no separate work needed for Phase 1.
* Outbound and inbound email processing will be handled by Plateau's internal Microsoft 365 infrastructure. The Symfa team will only manage database records for email UI.
* All existing Access-based logic (snapshot checks, rule validations, and audit placeholders) can be accessed or exported for migration.
* Authentication and role management will rely on existing infrastructure: Azure AD (internal); no new identity provider is introduced.
* Document generation and storage will leverage existing ShareFile; no new PDF/letter builder will be introduced unless Plateau explicitly requests it.
* System non-functional goals (load, concurrency, RPO/RTO) are assumed to match existing Plateau web standards until defined otherwise.
* All outgoing agent communications will use Plateau's Microsoft 365 SMTP relay, routed internally for compliance.

### Risks (MVP)

* Legacy data mapping between old Access structures and the new SQL schema may require additional adjustments during migration.
* Access snapshot and validation rules are extensive and poorly documented; extracting and replicating remaining logic (approximately 20% not yet ported) may take longer than planned.
* Ownership of financial totals (which layer is authoritative) must be confirmed to prevent balancing discrepancies.
* Legally required customer letters and notifications must follow approved templates and compliance workflows; missing templates could delay production rollout.
* If dynamic template-based document generation is later requested, new infrastructure or integration effort may be required beyond the current MVP scope.
* Balancing Module happy path works, but mismatched cases need business review with Tanya to understand how to handle situations when numbers don't add up as expected.

---

*This comprehensive documentation provides a complete overview of the TransCredit project, from high-level business context to detailed system analysis and target state, ensuring all stakeholders understand the current state, challenges, and future vision.*

---

# Appendix: Prototype Overview – Complete Interface Documentation

<!-- The following content is inserted verbatim from Prototype Overview/Complete-Interface-Documentation.md -->

## 📋 Overview
This document contains detailed descriptions of all TransCredit prototype interfaces, demonstrating the transition from the outdated MS Access/Excel system to a modern web application with automated error processing and improved agent communication.

---

# 1. Agent Reports Overview - Detailed Interface Description

## 📋 General Information
**Mockup File**: `01-Agent-Reports-Overview.svg`  
**Functionality**: Main page for managing agent reports  
**Target Audience**: TransCredit operational staff  
**Business Process**: Processing monthly reports from financial institutions

## 🖼️ Interface Preview
![Agent Reports Overview](01-Agent-Reports-Overview.svg)  

## 🎯 Interface Purpose
This interface serves as the central management point for agent reports, replacing the current MS Access system. It allows operational staff to view, analyze, and manage financial reports from banks and credit unions.

## 🧭 Navigation Structure

### Main Navigation (Top Panel)
- **Overview** - Report overview (current page)
- **Actions** - Report actions
- **Cert** - Certificate management
- **Transactions** - Financial transactions
- **Errors** - Error management
- **Communication** - Agent communication

## 📊 Report Information Section

### Report Header
- **Report Number**: Rpt #1593742
- **Description**: "August- Clarksdale"
  - Format: [Month] - [Agent City/Location]
  - Examples: "August Bath", "August ER", "August Upload"

### Main Report Fields
| Field | Value | Description | Business Logic |
|-------|-------|-------------|----------------|
| **Report Type** | Report Received (1) C List Report | Report type | Determines report source |
| **Created Date** | 9/5/25 | Creation date | Date when staff processed the report |
| **User** | jennifer.shannon | Responsible user | Who is processing the report |
| **Rpt Amount** | $2,286.69 | Report amount | Total amount agent owes |

### Financial Metrics
| Field | Value | Description | Calculation |
|-------|-------|-------------|-------------|
| **Certs Premium** | $5,210.72 | Total certificate premiums | Sum of all insurance premiums |
| **Certs Comm** | $2,924.04 | Agent commission | Percentage of premium agent receives |
| **Difference** | $0.01 | Calculation difference | Difference between expected and actual |

## 💰 Agent Transactions Section

### Section Header
- **Title**: "Agent Report Transactions"
- **Description**: "keep track of money posted to an Agent Report. Transactions can be added across RYMs as the data and funds are received and processed."

### Balancing Status
- **Status**: "Not Balanced, ($6.00)"
- **Indicator**: Red color (presumably)
- **Value**: Negative difference of $6.00

### Action Buttons
- **Add Transaction** - Add new transaction
- **E List Report** - Export transaction list

### Transactions Table
| Column | Description | Example Value |
|--------|-------------|---------------|
| **RYM** | Reporting Year Month | 202509 |
| **TYPE** | Transaction type | Report Received |
| **DESC** | Description | dev.user |
| **DATE** | Transaction date | 9/18/25, 12:43 PM |
| **AMOUNT** | Amount | $2,286.69 |

### Financial Summary
| Metric | Value | Description |
|--------|-------|-------------|
| **Trans Total** | $2,292.69 | Total of all transactions |
| **Report** | $2,286.69 | Report amount |
| **Difference** | ($6.00) | Difference (negative) |

## 🔧 Functional Capabilities

### Main Actions
1. **View Report** - Detailed financial status information
2. **Add Transactions** - Record agent payments
3. **Balancing** - Verify amount matching
4. **Navigation** - Transition to other report sections

### Business Rules
- **Mandatory Balancing**: Report cannot be completed without balance
- **Transaction Tracking**: All monetary receipts must be recorded
- **Time Frames**: Transactions can be added throughout the month (RYM)

## 🎨 Design and UX

### Visual Elements
- **Color Scheme**: Modern web palette
- **Typography**: Clear headers and readable text
- **Spacing**: Well-structured layout

### Interactivity
- **Clickable Elements**: Navigation tabs
- **Action Buttons**: Add Transaction, E List Report
- **Status Indicators**: Visual balance display

## 🔄 Integration with Other Modules

### Related Interfaces
- **Certificates** - Transition to certificate management
- **Errors** - View report errors
- **Communication** - Contact agent regarding balance issues

### Data
- **Source**: MS Access database (current system)
- **Target**: SQL Server (new system)
- **Format**: Structured report data

## 📈 Advantages of New Interface

### Compared to Current System (MS Access)
1. **Modern Interface** - Web application instead of Access forms
2. **Improved Navigation** - Intuitive tab structure
3. **Real-time** - Instant data updates
4. **Scalability** - Multiple user support

### Business Benefits
- **Processing Speed** - Quick access to information
- **Accuracy** - Automatic calculations and validation
- **Tracking** - Complete change history
- **Collaboration** - Multiple users

## 🚀 Technical Requirements

### Frontend
- **Technology**: Blazor WebAssembly
- **Responsive**: Adaptive design
- **Accessibility**: Compliance with accessibility standards

### Backend
- **API**: RESTful services
- **Database**: SQL Server
- **Authentication**: Integrated user system

### Integrations
- **Email System** - Status notifications
- **Financial Systems** - Transaction synchronization
- **Audit** - All action logging

---

# 2. Add Certificate Interface - Detailed Interface Description

## 📋 General Information
**Mockup File**: `02-Add-Certificate-Interface.svg`  
**Functionality**: Form for adding new insurance certificates  
**Target Audience**: TransCredit operational staff  
**Business Process**: Certificate data entry into the system

## 🖼️ Interface Preview
![Add Certificate Interface](02-Add-Certificate-Interface.svg)  

## 🎯 Interface Purpose
This interface replaces manual certificate data entry in MS Access. It allows staff to efficiently add new insurance certificates with built-in validation and structured data entry.

## 🧭 Navigation and Context

### Page Header
- **Back** - Return to previous page button
- **Rpt #1593742** - Report number (context)
- **Add Certificate** - Current operation name

### Contextual Information
- **Report**: #1593742 (August- Clarksdale)
- **User**: jennifer.shannon
- **Status**: Adding new certificate

## 📝 Form Structure

### 1. General Section
| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| **Certificate #** | Text | ✅ Required | Certificate number from agent | 67053 |

**Business Rules:**
- If certificate number is missing, use last 4 digits of SSN
- Uniqueness within report scope
- Format: numeric or alphanumeric

### 2. Lender Info Section
| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| **Branch** | Text | ❌ Optional | Bank/credit union branch | Main Branch |
| **Officer** | Text | ❌ Optional | Loan officer | John Smith |

**Business Rules:**
- Connection to agent (bank/credit union)
- Used for reporting and communication

### 3. Loan Info Section
| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| **Maturity** | Date/Number | ✅ Required | Maturity date or number of payments | 12/25/2026 |

**Business Rules:**
- Mutually exclusive fields: date OR number of payments
- Date cannot be in the past
- Maximum term: until customer's 71st birthday

### 4. Terms Section
| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| **Mature Date** | Date | ❌ Optional | Loan maturity date | 12/25/2026 |
| **# Payments** | Number | ❌ Optional | Number of payments | 36 |
| **First Payment** | Date | ❌ Optional | First payment date | 10/25/2023 |

**Business Rules:**
- Either maturity date or number of payments
- First payment cannot be in the past
- Relationship between payment count and maturity date

## 👥 Borrower Section

### Add Borrower Buttons
| Button | Function | Description |
|--------|----------|-------------|
| **Add Primary** | Add primary borrower | Primary borrower on the loan |
| **Add Joint** | Add joint borrower | Joint borrower (spouse) |

**Business Rules:**
- Minimum one borrower (Primary)
- Maximum two borrowers (Primary + Joint)
- Joint borrower only for family loans

## 📋 Insurance Plans Section

### Current State
- **Message**: "(no plans have been added to this certificate)"
- **Button**: **Add Plan** - Add insurance plan

### Insurance Plan Types
| Plan Type | Description | Required |
|-----------|-------------|----------|
| **Life Insurance** | Life insurance | ❌ Optional |
| **Disability Insurance** | Disability insurance | ❌ Optional |
| **AD&D Insurance** | Accidental death & dismemberment | ❌ Optional |

**Business Rules:**
- At least one plan must be added
- For Disability Insurance, health questions are mandatory
- Coverage limits depend on plan type and agent

## 🔧 Functional Capabilities

### Main Actions
1. **Data Entry** - Structured certificate information entry
2. **Validation** - Real-time data correctness checking
3. **Save** - Save certificate to system
4. **Navigation** - Return to report or proceed to next certificate

### Data Validation
- **Required Fields** - Check for mandatory field completion
- **Data Format** - Verify correct formats (dates, numbers)
- **Business Rules** - Check compliance with business logic
- **Duplication** - Verify certificate number uniqueness

## 🎨 Design and UX

### Visual Elements
- **Required Fields** - Marked with asterisk (*)
- **Sections** - Clear separation into logical groups
- **Buttons** - Intuitive action buttons
- **States** - Visual feedback during validation

### Interactivity
- **Dynamic Fields** - Show/hide fields based on selection
- **Real-time Validation** - Instant data checking
- **Auto-completion** - Suggestions based on previous entries

## 🔄 Integration with Other Modules

### Related Interfaces
- **Agent Reports Overview** - Return to report
- **Error Management** - Display validation errors
- **Certificate Search** - Search existing certificates

### Data
- **Source**: OCR-processed documents or manual entry
- **Target**: Certificate database
- **Format**: Structured certificate data

## 📈 Advantages of New Interface

### Compared to Current System (MS Access)
1. **Structured Entry** - Clear sections and fields
2. **Real-time Validation** - Instant data checking
3. **Improved UX** - Modern web interface
4. **Fewer Errors** - Built-in checks and constraints

### Business Benefits
- **Entry Speed** - Fast form completion
- **Data Accuracy** - Validation prevents errors
- **Standardization** - Uniform entry process
- **Tracking** - Change history and audit trail

## 🚀 Technical Requirements

### Frontend
- **Technology**: Blazor WebAssembly
- **Validation**: Client and server-side
- **Responsive**: Adaptive design for different devices

### Backend
- **API**: RESTful services for data saving
- **Database**: SQL Server with certificate tables
- **Validation**: Server-side business rules

### Integrations
- **OCR System** - Auto-fill from scanned documents
- **Error System** - Automatic validation error creation
- **Audit** - Logging all changes

## 🔍 Usage Examples

### Scenario 1: Adding Life Insurance Certificate
1. Enter certificate number: 67053
2. Select branch: Main Branch
3. Specify maturity date: 12/25/2026
4. Add primary borrower
5. Add Life Insurance plan
6. Save certificate

### Scenario 2: Certificate with Data Errors
1. Enter incorrect data
2. System shows validation errors
3. Correct errors
4. Re-validate
5. Save corrected certificate

---

# 3. Error Management System - Detailed Interface Description

## 📋 General Information
**Mockup File**: `03-Error-Management-System.svg`  
**Functionality**: System for managing and tracking certificate errors  
**Target Audience**: TransCredit operational staff  
**Business Process**: Automatic detection and correction of certificate data errors

## 🖼️ Interface Preview
![Error Management System](03-Error-Management-System.svg)  

## 🎯 Interface Purpose
This interface is a key automation component that replaces the manual "Run Snapshot" process from the current MS Access system. It allows staff to efficiently manage validation errors, track their status, and coordinate corrections with agents.

## 🧭 Navigation and Context

### Page Header
- **Navigation**: Agent Reports → Errors
- **Context**: Rpt #1593742 Details
- **Agent**: Dalton Furniture, Inc. (145990)

### Contextual Information
- **Report**: #1593742 (August- Clarksdale)
- **Agent**: Dalton Furniture, Inc. (ID: 145990)
- **Status**: Processing errors

## 🚨 Error Types in System

### 1. Premium Errors
| Error | Description | Business Logic |
|-------|-------------|----------------|
| **Premium Too High** | "Premium value of $540.34 is too high for a loan amount of $5,000" | Premium exceeds allowable percentage of loan amount |
| **Premium Mismatch** | "Premium total of $3,241.23 does not match the expected value of $3,000" | Mismatch between calculated and actual premium |

**Business Rules:**
- Premium cannot exceed established percentage of loan amount
- Calculations must match rate tables
- Verification of mathematical calculation correctness

### 2. Missing Information Errors
| Error | Description | Business Logic |
|-------|-------------|----------------|
| **Agent Report Missing Info** | "Agent Report is missing information" | Incomplete data in agent report |

**Business Rules:**
- All mandatory fields must be completed
- Data completeness check before processing
- Agent notification of missing information

### 3. Over Limit Errors
| Error | Description | Business Logic |
|-------|-------------|----------------|
| **Risk Face Over Limit** | "Over limit - Risk face amount for this certificate of $5,345 is over the Agent's max risk face amount of $4,000" | Exceeds agent's maximum coverage limit |

**Business Rules:**
- Each agent has maximum coverage limit per customer
- Check cumulative coverage across all active policies
- Agent confirmation or coverage adjustment required

## 🔧 Functional Capabilities

### Main Actions
1. **View Errors** - Detailed list of all certificate errors
2. **Filtering** - Show only unresolved errors
3. **Sorting** - Order by type, certificate, or priority
4. **Search** - Quick search by certificate number or error type

### Error Management
- **Error Status** - Track state (new, in progress, resolved)
- **Priority** - Determine error importance
- **Assignee** - Assign user for correction
- **Comments** - Add notes to errors

### Communication Integration
- **Agent Emails** - Automatic error list sending
- **Response Tracking** - Monitor agent corrections
- **Communication Status** - Track correction process

## 📈 Process Automation

### Automatic Error Detection
| Process | Current System | New System |
|---------|----------------|------------|
| **Start Check** | Manual "Run Snapshot" click | Automatic validation |
| **Check Frequency** | On demand | Real-time |
| **Error Types** | Limited set | Extended validation |

### Automatic Check Types
1. **Age Limits** - Check customer age compliance
2. **Premium Calculations** - Validate mathematical calculations
3. **Coverage Amounts** - Verify insurance amount correctness
4. **Refund Methods** - Validate pro-rata vs Rule 78
5. **Platform Errors** - Check agent system errors
6. **Printing Errors** - Detect extra premiums
7. **Limit Violations** - Check agent limit exceedances

## 🎨 Design and UX

### Visual Elements
- **Color Coding** - Different colors for different error types
- **Status Icons** - Visual error state indicators
- **Grouping** - Logical grouping by certificates
- **Progress Bars** - Display correction progress

### Interactivity
- **Clickable Rows** - Navigate to error details
- **Context Menus** - Quick error actions
- **Drag & Drop** - Move errors between statuses
- **Bulk Operations** - Select and process multiple errors

## 🔄 Integration with Other Modules

### Related Interfaces
- **Agent Reports Overview** - Report context
- **Add Certificate Interface** - Source of validation errors
- **Communication History** - Send agent notifications
- **Email Composition** - Create error emails

### Data
- **Source**: Automatic certificate validation
- **Target**: Error database and statuses
- **Format**: Structured error data

## 📈 Advantages of New System

### Compared to Current System (MS Access)
1. **Automation** - Eliminates manual "Run Snapshot" trigger
2. **Real-time** - Instant error detection
3. **Extended Validation** - More check types
4. **Improved Tracking** - Detailed error history

### Business Benefits
- **Time Reduction** - From 95% manual work to automation
- **Increased Accuracy** - Fewer missed errors
- **Improved Communication** - Structured agent notifications
- **Complete Audit** - Track all changes

## 🚀 Technical Requirements

### Frontend
- **Technology**: Blazor WebAssembly
- **Updates**: Real-time updates via SignalR
- **Filtering**: Client-side filtering for performance

### Backend
- **API**: RESTful services for error management
- **Database**: SQL Server with error tables
- **Validation**: Server-side business rules

### Integrations
- **Validation System** - Automatic error creation
- **Email System** - New error notifications
- **Audit** - Log all error actions

## 🔍 Usage Examples

### Scenario 1: Premium Error Detection
1. System automatically detects premium calculation error
2. Error appears in list with "Premium" type
3. Staff reviews error details
4. Email sent to agent with problem description
5. Agent corrects error and sends correction
6. Error marked as resolved

### Scenario 2: Agent Limit Exceedance
1. System checks customer's cumulative coverage
2. Agent limit exceedance detected
3. "Over Limit" error created
4. Staff contacts agent
5. Agent confirms or adjusts coverage
6. Error resolved after adjustment

---

# 4. Communication History - Detailed Interface Description

## 📋 General Information
**Mockup File**: `04-Communication-History.svg`  
**Functionality**: History of correspondence with agents regarding reports  
**Target Audience**: TransCredit operational staff  
**Business Process**: Tracking and managing agent communication

## 🖼️ Interface Preview
![Communication History](04-Communication-History.svg)  

## 🎯 Interface Purpose
This interface solves a critical problem of the current system - lack of integrated communication tracking with agents. It replaces scattered email correspondence in email clients with a centralized communication management system.

## 🧭 Navigation and Context

### Page Header
- **Navigation**: Agent Reports → Communication
- **Context**: Rpt #1593742 Details
- **Section**: EMAILS

### Contextual Information
- **Report**: #1593742 (August- Clarksdale)
- **Agent**: Dalton Furniture, Inc. (ID: 145990)
- **Status**: Viewing communication history

## 📧 Email List

### Email List Structure
| Column | Description | Example Value |
|--------|-------------|---------------|
| **Sender** | Agent email address | agent@email.com |
| **Date** | Email send date | 10/27/25 |
| **Subject** | Email subject | My Subject 12, 14, 16 |

### Examples of Emails in History
| Date | Sender | Subject | Status |
|------|--------|---------|--------|
| 10/27/25 | agent@email.com | My Subject 12 | Read |
| 10/27/25 | agent@email.com | My Subject 14 | Read |
| 10/27/25 | agent@email.com | My Subject 16 | Read |

## 📄 Pagination and Navigation

### Pagination Information
- **Current Page**: Page 1 of 2
- **Total Items**: 10 items
- **Items per Page**: 5 emails

### Navigation Elements
| Element | Function | Description |
|---------|----------|-------------|
| **<** | Previous page | Go to previous page |
| **>** | Next page | Go to next page |
| **K** | Quick navigation | Go to specific page |

## 📖 Email Details

### Selected Email
| Field | Value | Description |
|-------|-------|-------------|
| **Sender** | agent@email.com | Agent email address |
| **Subject** | My Subject 10 | Email subject |
| **Date** | 10/27/25 | Send date |
| **Time** | 4 | Send time (presumably 4:00) |

### Email Content
- **Text**: "This is a test email message."
- **Type**: Test message
- **Status**: Read

### Action Buttons
| Button | Function | Description |
|--------|----------|-------------|
| **Reply** | Reply | Send response to agent |
| **Forward** | Forward | Forward email to another recipient |
| **Archive** | Archive | Move to archive |

## 🔧 Functional Capabilities

### Main Actions
1. **View History** - Complete correspondence history with agent
2. **Search Emails** - Search by subject, date, content
3. **Filter** - Filter by status, date, email type
4. **Sort** - Order by date, subject, status

### Email Management
- **Email Status** - Read/unread, important, archived
- **Tags** - Categorize emails by type (errors, confirmations, questions)
- **Attachments** - View and download attached files
- **Related Certificates** - Link emails to specific certificates

### Error Integration
- **Automatic Linking** - Emails automatically linked to errors
- **Contextual Information** - Display related errors in email
- **Correction Status** - Track error correction progress

## 📈 Process Automation

### Automatic Functions
| Function | Description | Benefit |
|----------|-------------|---------|
| **Automatic Categorization** | System determines email type | Quick sorting |
| **Error Linking** | Emails automatically linked to errors | Contextual information |
| **Notifications** | Notifications for new emails | Timely response |
| **Archiving** | Automatic archiving of old emails | Data organization |

### Email System Integration
- **Incoming Emails** - Automatic receipt from agents
- **Outgoing Emails** - Send emails through system
- **Synchronization** - Sync with mail servers
- **Backup** - Save all emails in database

## 🎨 Design and UX

### Visual Elements
- **Email List** - Clear structure with main information
- **Active Email Highlighting** - Visual highlighting of selected email
- **Status Indicators** - Icons for email status
- **Color Coding** - Different colors for different email types

### Interactivity
- **Clickable Rows** - Select email for viewing
- **Context Menus** - Quick email actions
- **Drag & Drop** - Move emails between folders
- **Keyboard Shortcuts** - Quick navigation

## 🔄 Integration with Other Modules

### Related Interfaces
- **Agent Reports Overview** - Report context
- **Error Management System** - Link to errors
- **Email Composition Interface** - Create new emails
- **Certificate Management** - Link to certificates

### Data
- **Source**: Email servers and manual entry
- **Target**: Communication database
- **Format**: Structured email data

## 📈 Advantages of New System

### Compared to Current System (Email Clients)
1. **Centralization** - All communication in one place
2. **Context** - Link emails to reports and errors
3. **Search** - Quick search through entire history
4. **Tracking** - Complete interaction history

### Business Benefits
- **Improved Communication** - Structured correspondence
- **Time Reduction** - Quick access to history
- **Quality Improvement** - Contextual information
- **Complete Audit** - Track all interactions

## 🚀 Technical Requirements

### Frontend
- **Technology**: Blazor WebAssembly
- **Updates**: Real-time updates via SignalR
- **Search**: Client-side search for quick access

### Backend
- **API**: RESTful services for email management
- **Database**: SQL Server with communication tables
- **Email Integration**: SMTP/POP3/IMAP protocols

### Integrations
- **Email Servers** - Sync with corporate email
- **Error System** - Automatic error linking
- **Audit** - Log all email actions

## 🔍 Usage Examples

### Scenario 1: View Error Correction History
1. Staff opens report with errors
2. Goes to Communication section
3. Views email history with agent
4. Finds email with error description
5. Checks agent response with corrections
6. Confirms receipt of corrections

### Scenario 2: Track Correction Progress
1. System sends email to agent with errors
2. Email appears in communication history
3. Agent responds with corrections
4. Response automatically linked to original email
5. Staff sees complete correspondence chain
6. Updates error status after receiving corrections

## 📊 Metrics and Analytics

### Key Metrics
- **Agent Response Time** - Average response time to emails
- **Email Count** - Statistics by agents and reports
- **Communication Status** - Percentage of resolved issues
- **Response Quality** - Completeness and accuracy of agent responses

### Reporting
- **Agent Reports** - Communication statistics by agents
- **Period Reports** - Communication analysis over time
- **Type Reports** - Email categorization and responses
- **Efficiency Reports** - Communication effectiveness analysis

---

# 5. Email Composition Interface - Detailed Interface Description

## 📋 General Information
**Mockup File**: `05-Email-Composition-Interface.svg`  
**Functionality**: Interface for creating and sending emails to agents  
**Target Audience**: TransCredit operational staff  
**Business Process**: Structured communication with agents regarding errors and questions

## 🖼️ Interface Preview
![Email Composition Interface](05-Email-Composition-Interface.svg)  

## 🎯 Interface Purpose
This interface replaces manual email creation in email clients with a structured communication system. It allows creating standardized emails with automatic inclusion of contextual information about errors and reports.

## 🧭 Navigation and Context

### Page Header
- **Navigation**: Agent Reports → Communication → Send Email
- **Context**: Rpt #1593742 Details
- **Section**: Communication

### Contextual Information
- **Report**: #1593742 (August- Clarksdale)
- **Agent**: Dalton Furniture, Inc. (ID: 145990)
- **Status**: Creating email to agent

## 📧 Email Creation Form

### Main Email Fields
| Field | Value | Description | Required |
|-------|-------|-------------|----------|
| **To** | test@email.com | Primary recipient (agent) | ✅ Required |
| **Cc** | "Add any additional email addresses here" | Additional recipients | ❌ Optional |
| **Subject** | "RPT#1593742 - Report Correction Request" | Email subject | ✅ Required |

### Auto-fill Features
- **Report Number** - Automatically included in email subject
- **Request Type** - Standardized subjects (Correction Request, Information Request, etc.)
- **Agent Email** - Auto-fill from agent database

## 📎 Document Inclusion Options

### Checkboxes for Including Files
| Option | Status | Description | Content |
|--------|--------|-------------|---------|
| **Include Cert Errors spreadsheet?** | ☑ Checked | Include certificate errors table | Excel file with detailed error list |
| **Include R-List?** | ☑ Checked | Include R-List report | Report with financial data |

### Automatically Generated Documents
- **Cert Errors Spreadsheet** - Detailed table of all certificate errors
- **R-List Report** - Financial report with amounts and calculations
- **Certificate Details** - Detailed information on problematic certificates

## 📎 Attachment Management

### Attachments Section
| Element | Description | Function |
|---------|-------------|----------|
| **Attachments** | "(none)" | Current attachments |
| **+ Attachment** | Add button | Add file manually |

### Attachment Types
- **Automatic** - System-generated documents
- **Manual** - User-uploaded files
- **Templates** - Standard documents for different request types

## 🔧 Functional Capabilities

### Main Actions
1. **Create Email** - Structured message creation
2. **Auto-fill** - Pre-fill fields from context
3. **Include Documents** - Automatically add reports
4. **Send** - Send email to agent

### Email Templates
| Email Type | Description | Auto Content |
|------------|-------------|--------------|
| **Correction Request** | Request for error corrections | Error list, instructions |
| **Information Request** | Request for additional information | Missing data list |
| **Confirmation** | Confirmation of data receipt | Processing confirmation |
| **Follow-up** | Reminder about unresolved issues | Open questions list |

### Validation and Checks
- **Required Fields** - Check completion of main fields
- **Email Validation** - Verify email address correctness
- **Attachment Size** - Check attached file sizes
- **Content** - Verify presence of necessary information

## 📈 Process Automation

### Automatic Functions
| Function | Description | Benefit |
|----------|-------------|---------|
| **Subject Generation** | Automatic email subject creation | Communication standardization |
| **Error Inclusion** | Automatic error list addition | Information completeness |
| **Templates** | Pre-set email templates | Consistency |
| **Tracking** | Automatic sent email tracking | Complete audit |

### Error System Integration
- **Automatic Inclusion** - Errors automatically included in email
- **Contextual Information** - Error details with certificate numbers
- **Instructions** - Automatic correction instructions
- **Deadlines** - Specify correction timeframes

## 🎨 Design and UX

### Visual Elements
- **Clear Structure** - Logical section separation
- **Intuitive Elements** - Understandable buttons and fields
- **Status Indicators** - Visual feedback
- **Preview** - Pre-send preview capability

### Interactivity
- **Dynamic Fields** - Show/hide fields based on selection
- **Auto-completion** - Suggestions based on previous emails
- **Drag & Drop** - Drag files for attachments
- **Keyboard Shortcuts** - Quick actions

## 🔄 Integration with Other Modules

### Related Interfaces
- **Agent Reports Overview** - Report context
- **Error Management System** - Source of errors to include
- **Communication History** - Save sent emails
- **Certificate Management** - Link to certificates

### Data
- **Source**: Report and error data
- **Target**: Email servers and communication database
- **Format**: Structured email data

## 📈 Advantages of New System

### Compared to Current System (Email Clients)
1. **Standardization** - Uniform emails with templates
2. **Automation** - Automatic contextual information inclusion
3. **Integration** - Link to error and report systems
4. **Tracking** - Complete sent email history

### Business Benefits
- **Consistency** - Standardized communication
- **Completeness** - Automatic inclusion of all necessary information
- **Efficiency** - Quick professional email creation
- **Audit** - Complete communication tracking

## 🚀 Technical Requirements

### Frontend
- **Technology**: Blazor WebAssembly
- **Editor** - Rich text editor for formatting
- **Validation** - Client-side form validation
- **Preview** - WYSIWYG editor

### Backend
- **API**: RESTful services for email sending
- **Email Server** - SMTP server for sending
- **Document Generation** - Create Excel/PDF reports
- **Templates** - Email template system

### Integrations
- **Email Servers** - Corporate SMTP servers
- **Error System** - Automatic error inclusion
- **Database** - Save email history
- **File System** - Attachment management

## 🔍 Usage Examples

### Scenario 1: Send Error Correction Request
1. Staff opens report with errors
2. Goes to Communication section
3. Clicks "Send Email"
4. System auto-fills subject: "RPT#1593742 - Report Correction Request"
5. Checks "Include Cert Errors spreadsheet?"
6. Adds additional instructions
7. Sends email to agent

### Scenario 2: Request Additional Information
1. Staff discovers missing information
2. Creates new email with subject "Information Request"
3. System automatically includes missing data list
4. Adds completion instructions
5. Sends email to agent

## 📊 Email Templates

### Standard Templates
| Template | Subject | Content | Attachments |
|----------|---------|---------|-------------|
| **Correction Request** | RPT#[number] - Report Correction Request | Error list, correction instructions | Cert Errors spreadsheet |
| **Information Request** | RPT#[number] - Missing Information Request | Missing data list | R-List report |
| **Confirmation** | RPT#[number] - Report Received Confirmation | Receipt confirmation | None |
| **Follow-up** | RPT#[number] - Follow-up Required | Reminder about unresolved issues | Previous correspondence |

### Template Customization
- **Personalization** - Add agent name
- **Contextual Information** - Include specific details
- **Instructions** - Detailed correction instructions
- **Deadlines** - Specify timeframes

---

# System Workflow Overview

## 🔄 Interface Integration Flow

```
Agent Reports Overview
         ↓
Add Certificate Interface
         ↓
Error Management System
         ↓
Communication History ← → Email Composition Interface
```

## 🎯 Key System Benefits

### Operational Efficiency
- **Error Automation**: 95% manual work → automation
- **Processing Speed**: Quick access to information
- **Data Accuracy**: Built-in validation
- **Standardization**: Uniform processes

### Agent Communication
- **Centralization**: All correspondence in one place
- **Structure**: Standardized emails
- **Tracking**: Complete interaction history
- **Context**: Linking emails to reports and errors

### Technology Modernization
- **Modern Platform**: Blazor WebAssembly
- **Scalability**: SQL Server backend
- **Integrations**: Email, OCR, file systems
- **Future Development**: Growth foundation

---

*This comprehensive document is intended for analysts, project managers, and developers to understand the complete functionality of all TransCredit prototype interfaces.*