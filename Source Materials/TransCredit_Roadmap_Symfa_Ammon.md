# TransCredit Roadmap Summary — Symfa & Ammon Alignment

| **Feature** | **Description (short summary)** | **Current Status / What Ammon Said** | **Phase** |
|--------------|----------------------------------|--------------------------------------|------------|
| **DMZ Certificates Portal** | External portal for agents to upload and review pending reports. | *"So, yes, the DMZ certificate portal, so they already have that there where they can put their certificates in. That piece is already done, so there's nothing that needs to be done with that."* | ✅ Done |
| **DMZ Certificate Update Forms** | External forms for agents to correct certificates. | *"We, after talking with Erin, she said that is not going to be very feasible because they need to be, when they need to make a correction, if something was input wrong, if the file was wrong, they need to go back and product the agent, and then they need to get the actual paper copy to compare to see what the differences are... So it's not as simple as, you know, letting an agent log in, make their changes, and letting that flow through. So that is going to be a manual process for now."* | ⏸️ Out of scope |
| **OCR Ingestion Integration** | Integration of OCR pipeline and UI. | *"The OCR ingestion, that is, we already have all of the pages and everything set up for that... So you don't need to, you're not going to be working on the OCR piece or doing anything here, you're going to be working on this one, but when you fix this one working, it's also going to work on the OCR piece, we just need to do some testing with it to make sure it works properly, but it's the same components calling the same DI and services."* | 🟢 MVP Phase 1 (Automatic byproduct) |
| **Certificate Creation Page Completion** | Add Certificate page: saving to DB and validation on save. | *"As far as the UI goes, I'm pretty sure that the UI... Is pretty much complete. The only thing it'll need to have done to it, as we mentioned, is when there are errors or something fails validation, that those need to be saved off into the cert error table. But everything else on here does work and is ready. The only thing that doesn't work yet is when you click add certificate, it doesn't actually call the DI service to actually insert it into the database because we hadn't finished those other pieces yet."* | 🟢 MVP Phase 1 |
| **Certificate Validation** | Data validation logic via DI Certificate Service. | *"We probably have, I'd say, at least 80% of the air checks, if I had to get that are already done and completed on this page. So there's a lot of things that are being done, but there are also some checks that are being done in the access code that we don't know about... So that's where a lot of that time will be spent on this specific part, is diving into the access pieces to pull out any additional air checks need to be done and immigrating those air checks into this new page."* | 🟢 MVP Phase 1 |
| **Certificate Versioning** | Snapshot of certificate data on each change. | Partially implemented in DI Service; full versioning to come later. | 🟢 MVP Phase 1 |
| **Error Summary UI** | Screen for grouped certificate errors (by type, severity) with drill-down. | *"I guess that would probably be a good spot to start with... that would just simply be loading up from that news error, cert error table... So that cert error table. So, like I the business logic, calculating, determining most of those errors, that's But when it actually comes to reading and writing that from the database, there is no table for that and nothing to do any of the credit operations needed for that."* | 🟡 MVP Phase 2 (Priority: Start here) |
| **Certificate Error Checking Service** | Validation logic and rules migrated from Access; error persistence. | *"That number seven is where probably you'll want to do a – probably start with things because that's where you need to go through the error logic from Access to determine everything that's... It's really going to be focusing on taking the current validation error logic we have, expanding that to include anything we're missing, and then taking that information and storing it off into a new certificate error table... There's a lot of the logic that's needed for that error checking is done here in this value certificate, but the actual storing and reading and writing and updating to the database table for the errors, yes, that's not there yet at all."* | 🟡 MVP Phase 2 (High priority) |
| **Error Storage and Management** | Store and manage validation errors (open/resolved). | *"The only database tables you should need are for the certificate errors. Everything else is already there and hooked up and working... There'll be a new certificate errors table, and then we'll need the DI service to be able to interact with that, you know, input and clear out."* | 🟡 MVP Phase 2 (Part of Error Checking Service) |
| **Certificate Editing** | Enable full editing of certificate details. | Part of MVP Phase 1 (816h). Base editing functionality. | 🟢 MVP Phase 1 |
| **Certificate Editing (Error Correction Flow)** | Using edit page from Error Summary UI to correct errors and mark them as resolved. | *"Once they have know what they need to do, and this part doesn't hear yet, they'll click on this, and it takes them to, it will need to be a certificate edit page. I haven't done anything with editing yet, but we'll the same controls to be adding, they would edit it, then once... They correct it, they fix it, they come back into it, save it, and then hopefully that error should be then clear while it'll be marked as cleared so it will no longer show up in the grid."* | 🟡 MVP Phase 2 (After Error Summary UI - uses Phase 1 editing) |
| **Email Communication UI** | UI for reading/sending emails and linking to certificates. | *"Because then after that we can dive into the agent notifications and communication... The agent communications where they're going to need to go to send emails off to the agents. And when they do, yeah, they'll need to include different things like the certificate errors and which certificates they want to show in that spreadsheet that they want to attach to it... 14, that's the one that we only have just that demo that I threw together, but it's not reading or writing anything. There's no tables there. There's nothing behind it. So that's going to take a bit of time as well to do all of that."* | 🟡 MVP Phase 2 (After Editing) |
| **Cert QA Review UI** | QA review of OCR data (Pass/Fail) and promotion to APS Plateau. | *"4 and 5 are kind of the same thing... The UI for that is pretty much done. Oh, okay. So when I say done, it needs to be tested with the changes that will be made in... So right now, this is we have. This is just a sample demo we did with the previous OCR piece, but it had lots of problems, so we stopped with it."* | 🟡 MVP Phase 2 (UI ready; needs testing) |
| **Certificate Import & Idempotency** | Controlled import/update of certificates after QA Pass. | Handled as part of QA Review flow, not a separate story. | 🟡 MVP Phase 2 (Part of QA Review) |
| **Correction & Approval Workflow** | Side-by-side comparison (DMZ vs APS), approve/reject flow. | *"Number nine, because of how that one works, we won't be doing anything with that on the DMZ side right now, so that one will be postponed until much later, if ever."* | ⏸️ Future phase |
| **Balancing Module** | Transaction and totals reconciliation logic. | *"This is actually fully functioning and working, this part of this transaction summary. What's not working yet, and we haven't done anything with, but they need to be able to go in the hut that balance it... What I'm still not. Entirely clear on, I have not spent time with Tanya going through, is what she does when these numbers here don't add up to what they were expecting from the agent or what they were getting back from the payment... It needs to be expanded, but yes, I'll add the... Review it. We need to review it, at least."* | ⏸️ Future phase |
| **Change Reason Tracking** | Mandatory reason/comment when editing certificate data. | Will be part of future Correction Workflow. Not in current scope. | ⏸️ Future phase |
| **Enhanced Certificate Search** | Advanced search filters (DOB, SSN, agent, etc.). | Not discussed; not in focus. | ⏸️ Future phase |
| **Email Integration** | Implement backend tables for inbound/outbound emails and attachments; integrate with the client's email service via DB. | *"But yeah, we have the piece that will grab the emails from the table. Oh, yeah, so there are a couple other tables we need for this... So yeah, that piece as far as interaction with the Exchange server, yeah, you won't need to do anything. It's just the UI and reading and writing to that one database table... 13, I'm doing that. We already have everything in place. I just need to finish with network services."*<br><br>**Symfa work (Phase 1, 16h)**: Create DB tables for emails and attachments. **Ammon work**: Backend service that interacts with Exchange server (reads/writes to Symfa's tables). | 🟢 MVP Phase 1 (Symfa: DB tables) |
| **Error Export and Attachment** | Export errors to Excel/CSV and attach to outgoing emails. | Planned later, together with Email UI. | ⏸️ Future phase |
| **Agent Notification** | Automatic notifications to agents. | Working and complete. | ✅ Done |
| **OpsLog Unification & Events** | System event tracking (creation, QA, corrections, etc.). | *"Everything for ops log, that's all. We're completely there with the traceability database certificate, PDFs. Oh, yeah, so we OpsLog is already there, so that can be called whenever is needed to send notifications to whoever internally... Operations logging is the way that we use to, yeah, notify and send alerts to anyone internally for whatever happens when phases change or stages change or something that's updated or whatever. That's fully done, so that's ready to be called and implemented and used at any time."* | ✅ Done |
| **Email Server** | Microsoft 365 SMTP backend service. | Configured by Ammon; no actions required. | ✅ Done |

---

## Focus Areas for Symfa Team

### 🟢 MVP Phase 1 (in progress)
- Certificate Creation Page Completion  
- Certificate Validation (DI Service integration)  
- Certificate Versioning (partial)  
- Certificate Editing (base functionality - 8h)  
- Email Integration (DB tables for emails and attachments - 16h)  
- OCR Integration (automatic byproduct - no separate work needed)  
- Foundation for DI Certificate Service  

### 🟡 MVP Phase 2 (next focus after current MVP - priority order)

**Priority 1: Start here**
- **Error Summary UI** — Display grouped errors with drill-down (loads from cert error table)

**Priority 2: High priority**
- **Certificate Error Checking Service** — Port remaining Access rules + create CertError table + CRUD operations
- **Error Storage and Management** — Part of Error Checking Service (cert error table implementation)

**Priority 3: After Error Summary UI**
- **Certificate Editing (Error Correction Flow)** — Integration with Error Summary UI to correct errors (uses Phase 1 editing functionality)

**Priority 4: After Editing**
- **Email Communication UI** — Reading/sending emails, linking to certificates, attaching error spreadsheets

**Priority 5: Testing & QA**
- **Cert QA Review UI** — UI ready; needs testing with new validation logic
- **Certificate Import & Idempotency** — Part of QA Review flow

### ⏸️ Future Phases / Later
- Correction & Approval Workflow (side-by-side diff)  
- Balancing Module (after business alignment with Tanya)  
- Change Reason Tracking  
- Enhanced Search  
- Error Export & Attachment  

---

### Suggested Intro for Ammon

> **Hi Ammon,**  
>  
> Following our discussion on November 10, we summarized the current TransCredit scope to clarify the focus areas for Symfa.  
>  
> - **MVP Phase 1** includes the ongoing development of certificate creation, validation, and DI integration. OCR will work automatically as a byproduct of this work.  
> - **MVP Phase 2** will follow this priority order (as you suggested):  
>   1. **Error Summary UI** — Start here (loads from cert error table)  
>   2. **Certificate Error Checking Service** — High priority (port Access rules + CertError table)  
>   3. **Certificate Editing (Error Correction Flow)** — After Error Summary UI (uses Phase 1 editing functionality)  
>   4. **Email Communication UI** — After Editing  
>   5. **Cert QA Review UI** — Testing with new validation logic  
> - **Future phases** (Correction Workflow, Balancing, and other features) are postponed until after these core components are complete.  
>  
> Please review and confirm the phase alignment and priority order below before we proceed with detailed planning for Phase 2.
