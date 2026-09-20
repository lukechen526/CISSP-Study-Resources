<a id="domain-1"></a>

# Domain 1: Security and Risk Management

Exam weight: 16%. Study edition: September 2026.

## Start here

Security and risk management explains why the organization protects information and who is accountable for the decisions. You will learn to connect ethics, governance, obligations, people, continuity, and risk treatment. The result is a defensible security program that supports the business, rather than a collection of unrelated controls.

This chapter follows the published Domain 1 objectives. Read the opening explanation of each objective first, then the detailed lessons, and finish with its application check. Three-part numbers identify subtopics retained from the source guide. The examples use Harbor Services, a small organization launching a customer portal and an AI support assistant.

Artificial intelligence (AI) is the broad field of systems performing tasks associated with intelligence. Machine learning (ML) builds models from examples during training; inference uses a trained model to produce an output. A large language model (LLM) produces language using learned numerical parameters called model weights. These terms identify components and processes to protect, rather than establish that a system is correct or trustworthy.

The AI additions apply [ISC2's domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline) to existing objectives. Detailed placement and Harbor scenarios are editorial teaching choices. Named historical technologies remain useful for comparison; their inclusion is not a recommendation to deploy them.

## Chapter navigation

- [1.1 Understand, adhere to, and promote professional ethics](#objective-1-1)
- [1.2 Understand and apply security concepts](#objective-1-2)
- [1.3 Evaluate, apply, and sustain security governance principles](#objective-1-3)
- [1.4 Understand legal, regulatory, and compliance issues that pertain to information security in a holistic context](#objective-1-4)
- [1.5 Understand requirements for investigation types (i.e., administrative, criminal, civil, regulatory, industry standards)](#objective-1-5)
- [1.6 Develop, document, and implement security policy, standards, procedures and guidelines](#objective-1-6)
- [1.7 Identify, analyze, assess, prioritize, and implement Business Continuity (BC) requirements](#objective-1-7)
- [1.8 Contribute to and enforce personnel security policies and procedures](#objective-1-8)
- [1.9 Understand and apply risk management concepts](#objective-1-9)
- [1.10 Understand and apply threat modeling concepts and methodologies](#objective-1-10)
- [1.11 Apply Supply Chain Risk Management (SCRM) concepts](#objective-1-11)
- [1.12 Establish and maintain a security awareness, education, and training program](#objective-1-12)

<a id="objective-1-1"></a>

## 1.1 Understand, adhere to, and promote professional ethics

Security work gives you access to information and systems that other people must trust you to handle responsibly. Professional ethics supplies a standard for decisions even when a policy does not describe the exact situation. An employer's request is therefore one consideration, alongside duties to the public, the law, and the profession.

In this guide, Harbor Services is a small organization launching an online customer portal and considering an AI support assistant. A security analyst at Harbor should be honest about the limits of a test and seek qualified help when needed. Concealing a weakness to meet a launch date undermines the trust that the service depends on.

As a CISSP, you must understand and follow the (ISC)² code of ethics, as well as your organization’s own code.

<a id="subtopic-1-1-1"></a>

### 1.1.1 (ISC)² Code of Professional Ethics

#### RFC 1087: activity that is unethical and unacceptable

(a) seeks to gain unauthorized access to the resources of the Internet. (b) disrupts the intended use of the Internet. (c) wastes resources (people, capacity, computer) through such actions. (d) destroys the integrity of computer-based information, and/or. (e) compromises the privacy of users.

This domain is one of the largest with a weighting of 16%; it is also very much foundational for most of the other domains, so give it the associated time in preparation. (ISC)² Code of Professional Ethics -- take the time to read the [code of ethics](https://www.isc2.organization/Ethics).

#### At a minimum, know and understand the ethics canons

**Protect society, the common good, necessary public trust and confidence, and the infrastructure**.

This is “do the right thing”; put the common good ahead of yourself; ensure that the public can have faith in your infrastructure and security; any member of the public can file a claim under canon I.

#### Act honorably, honestly, justly, responsibly, and legally

Always follow the laws. When laws appear to conflict, identify the applicable jurisdictions and obtain qualified legal advice; location alone does not resolve the conflict. Any member of the public can file a claim under canon II.

#### Provide diligent and competent service to principals

Avoid passing yourself as an expert or as qualified in areas that you aren’t. Maintain and expand your skills to provide competent services. Only an employer or someone with a contractual relationship can file a complaint under canon III.

#### Advance and protect the profession

Don’t bring negative publicity to the profession. Provide competent services, get training and act honorably. Each ethics canon remains a distinct obligation; conduct that supports one canon does not automatically establish compliance with all others. Anyone who subscribes to a code of ethics as part of their licensure or certification is eligible to file a complaint under canon IV.

<a id="subtopic-1-1-2"></a>

### 1.1.2 Organizational code of ethics

You must also support ethics at your organization; this can be interpreted to mean evangelizing ethics throughout the organization, providing documentation and training around ethics, or looking for ways to enhance the existing organizational ethics.

Some organizations might have slightly different ethics than others, so be sure to familiarize yourself with your organization’s ethics and guidelines.

### AI in this objective

**AI ethics and bias.** An AI system can make harmful errors even when nobody intended discrimination. Harbor should ask whose outcomes may be affected, whether the evidence represents those people, and who can challenge a decision. Assign human accountability rather than treating a model's output as an independent authority. [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework).

### Apply this objective

**Question.** Harbor asks you to describe an untested system as secure in a customer report. How should you respond?

**Reasoning.** Explain what was actually tested, identify the remaining uncertainty, and propose the work needed to support the claim. Honesty and competent service require an accurate report even when the schedule is uncomfortable.

<a id="objective-1-2"></a>

## 1.2 Understand and apply security concepts

Before choosing a control, name the outcome that needs protection. Confidentiality protects against unauthorized disclosure; integrity protects against improper change; availability makes information and services usable when needed. Authenticity helps establish that a message or identity is genuine, while nonrepudiation provides evidence that makes a denial of an action difficult to sustain.

For Harbor, exposing a customer's address is a confidentiality failure, changing a payment destination is an integrity failure, and losing the portal during business hours is an availability failure. A single incident can affect several properties. Encryption, access controls, backups, and audit trails solve different parts of this problem; none is a universal replacement for the others.

<a id="subtopic-1-2-1"></a>

### 1.2.1 Confidentiality, integrity, and availability, authenticity and nonrepudiation (5 Pillars of Information Security)

#### Confidentiality

Principle that objects are not disclosed to unauthorized subjects. Concept of measures used to ensure the protection of the secrecy of data, objects, and resources. Confidentiality protections prevent disclosure while protecting authorized access. Preserving authorized restrictions on information access and disclosure, including the means for protecting personal privacy and proprietary information. Sensitive data, including personally identifiable information (PII) must be kept confidential; confidentiality is different from secrecy. Preserving confidentiality means protecting an asset or data, even if it's not a secret.

#### Integrity

Principle that objects retain their veracity and are intentionally modified only by authorized subjects. Concept of protecting the reliability and correctness of data; guarding against improper information modification/destruction; includes ensuring non-repudiation and authenticity. Integrity protection prevents unauthorized alterations of data. Preventing authorized subjects from making unauthorized modifications, such as mistakes. Maintaining the internal and external consistency of objects.

#### Availability

Principle that authorized subjects are granted timely and uninterrupted access to objects. To ensure high availability of services and data, use techniques like failover clustering, site resiliency, automatic failover, load balancing, redundancy of hardware and software components, and fault tolerance.

**Authenticity**: ensuring a transmission, message or sender is legitimate.

See the NIST glossary for examples: <https://csrc.nist.gov/glossary/term/authenticity>.

#### Nonrepudiation

Ensures that the subject of activity or who caused an event cannot deny that the event occurred. Nonrepudiation is made possible through identification, authentication, authorization, accountability, and auditing.

#### AAA Services

Identification: assertion of a user's identity; claiming to be an identity when attempting to access a secured area or system. Authentication: proving that you are that claimed identity via one or more factors of knowledge, ownership, or characteristic (something you know, something you have, something you are). Authorization: defining the needed resources, permissions (i.e. allow/grant and/or deny) to a resource, and object access for a specific identity or subject. Auditing: recording a log of the events and activities related to the system and subjects. Accountability (aka accounting, aka principle of access control): proper identification, authentication, and authorization that is logged and monitored; access control process which records information about attempts by all entities to access resources; reviewing log files to check for compliance and violations in order to hold subjects accountable for their actions, especially violations of organizational security policy.

### Apply this objective

**Question.** A database is encrypted, but an authorized employee accidentally changes customer balances. Which property failed, and why did encryption not prevent it?

**Reasoning.** Integrity failed. Storage encryption protects data against particular forms of disclosure; it does not determine whether an authorized change is correct. Validation, restricted update rights, review, and recoverable records address that risk.

<a id="objective-1-3"></a>

## 1.3 Evaluate, apply, and sustain security governance principles

Governance establishes direction, accountability, and oversight. Management turns that direction into plans and action. The board or senior leadership determines what the organization is trying to achieve and the risk it will accept; security professionals provide advice and operate a program that supports those decisions.

A framework organizes the work so important activities are not forgotten. It does not decide Harbor's priorities automatically. Start with business goals and obligations, assign owners, select applicable controls, and measure whether they work. Due diligence is the investigation and continuing attention needed to understand a risk; due care is taking reasonable action in light of what is known.

**Security governance** is the collection of policies, roles, processes/practices used to make security decisions in an organization; related to supporting, evaluating, defining, and directing the security efforts of an organization; it involves making sure that security strategies align with business goals, and that they are comprehensive and consistent across the organization.

Security governance is the implementation of a security solution and a management method that are tightly interconnected.

**The security function** is the aspect of operating a business that focuses on the task of evaluating and improving security over time.

To manage security, an organization must implement proper and sufficient security governance. The act of performing a risk assessment to drive the security policy is the clearest and most direct example of management of the security function.

**Third-party governance**: external entity oversight that may be mandated by law, regulation, industry standards, contractual obligation, or licensing requirement; outside investigator or auditors are often involved.

<a id="subtopic-1-3-1"></a>

### 1.3.1 Alignment of security function to business strategy, goals, mission, and objectives

**Security Management Planning** ensures proper creation/implementation/enforcement of a security policy, and alignment with organization strategy, goals, mission, and objectives; security management is based on three types of plans: strategic, tactical, and operational.

**Strategic Plan** is a strategic plan is a long-term plan (useful for 5 years); it defines the organization's security purpose.

A strategic plan should include a risk assessment.

**Tactical Plan**: mid-term plan (1 year or less) developed to provide more details on accomplishing the goals set forth in the strategic plan.

**Operational Plan** is a short-term, highly detailed plan based on strategic or tactical plans.

Mission, strategy, goals, and objectives — support each other in a hierarchy. **Objectives** are closest to the ground-level and represent small efforts to help you achieve a mission. **Missions**: represent a collection of objectives, and one or more missions lead to goals; when you reach your goals, you are achieving the strategy.

A security framework must closely tie to mission and objectives, enabling the business to complete its objectives and advance the mission while securing the environment based on risk tolerance.

<a id="subtopic-1-3-2"></a>

### 1.3.2 Organizational processes (e.g., acquisitions, divestitures, governance committees)

Security governance should address every aspect of an organization, including organizational processes of acquisitions, divestitures, and governance. Be aware of the risks in acquisitions (since the state of the IT environment to be integrated is unknown, due diligence is key) and divestitures (how to split the IT infrastructure and what to do with identities and credentials). Understand the value of governance committees (vendor governance, project governance, architecture governance, etc.).

Executives, managers and appointed individuals meet to review architecture, projects and incidents (security or otherwise), and provide approvals for new strategies or directions.

The goal is a fresh set of eyes, often eyes that are not purely focused on information security.

When evaluating a third-party for your security integration, consider the following: on-site assessment; document exchange and review; process/policy review; third-party audit.

<a id="subtopic-1-3-3"></a>

### 1.3.3 Organizational Roles and Responsibilities

Primary security roles are senior manager, security professional, asset owner, custodian, user, and auditor. Senior Manager: has a responsibility for organizational security and to maximize profits and shareholder value. Security Professional: has the functional responsibility for security, including writing the security policy and implementing it. Asset Owner: responsible for classifying information for placement or protection within the security solution. Custodian: responsible for the task of implementing the prescribed protection defined by the security policy and senior management. Auditor: responsible for reviewing and verifying that the security policy is properly implemented.

<a id="subtopic-1-3-4"></a>

### 1.3.4 Security control frameworks (e.g. International Organization for Standardization (ISO), National Institute of Standards and Technology (NIST), Control Objectives for Information and Related Technology (COBIT), Sherwood Applied Business Security Architecture (SABSA), Payment Card Industry (PCI), Federal Risk and Authorization Management Program (FedRAMP))

A **security control framework**: (AKA security frameworks) outlines the organization's approach to security, including guidelines, standards and controls; a security framework is important in planning the structure of an organization's security solution; frameworks include:

**[International Organization for Standardization (ISO)](https://www.iso.organization/about)** is a non-governmental organization comprised of standards bodies from over 160 countries that bring global experts together to agree on best practices across a range of industries with six main products: International Standards, Technical Reports, Technical Specifications, Publicly Available Specifications, Technical Corrigenda, and Guides; ISO standards are widely used.

**[ISO/IEC 27001](https://www.iso.organization/standard/27001)** is a widely recognized international standard for information security management systems (ISMS); it provides a risk-based approach, and emphasizes continual improvement of the ISMS.

ISO 27000 series (27000, 27001, 27002, etc.) is the international security standard for implementing organizational security and includes:

**ISO 27000:2018** provides an overview of the information security management system (ISMS). **ISO 27001:2022** provides best practice recommendations for an Information Security Management System (ISMS). **ISO 27002:2022** provides detailed implementation guidance for controls in ISO 27001. **ISO 27017:2015** provides guidelines for information security controls applicable to the provision and use of cloud services. **ISO 27018:2019**: commonly accepted controls and guidelines for protecting PII in the cloud (consent, control, transparency, communication, independent, yearly audit).

**[NIST Cybersecurity Framework (CSF)](https://www.nist.gov/cyberframework)**: built around six core functions providing guidance to industry, government agencies, and other organizations to improve their ability to prevent, detect, and respond to cyber attacks, and manage cybersecurity risks.

CSF was designed for commercial organizations and critical infrastructure and CSF 2.0 consists of these six functions: govern; identify; protect; detect; respond; recover.

**SP 800-53** is a catalog of security and privacy controls. **SP 800-171**, Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations, addresses protection of CUI in nonfederal environments. [NIST](https://csrc.nist.gov/pubs/sp/800/171/r3/final). **[SP 800-100](https://csrc.nist.gov/pubs/sp/800/100/r1/iprd)**: titled Information Security Handbook: a guide for managers, NIST hasn't released an update since 2006, although they appear to have an update in progress.

**[COBIT (Control Objectives for Information and Related Technologies)](https://www.isaca.organization/resources/cobit)**: COBIT is a framework created by ISACA that focuses on enterprise IT, aligning IT and business strategies, and providing a comprehensive framework for managing risks.

COBIT is commonly used as an *audit/compliance* framework for organizations.

**Six key principles**

Provide stakeholder value. Holistic approach. Dynamic governance system. Governance distinct from management. Tailored to enterprise needs. End-to-end governance system.

**[Sherwood Applied Business Security Architecture (SABSA)](https://sabsa.organization/sabsa-executive-summary/)** is a framework and methodology for developing business-driven, risk and opportunity-focused architectures for security and risk management.

SABSA is comprised of a series of integrated frameworks, models, methods and processes, used independently or as a holistic integrated enterprise solution, including: Business Requirements Engineering Framework (known as Attributes Profiling); Risk and Opportunity Management Framework; Policy Architecture Framework; Security Services-Oriented Architecture Framework; Governance Framework; Security Domain Framework; Through-life Security Service Management & Performance Management Framework.

**[Payment Card Industry Data Security Standard PCI DSS](https://www.pcisecuritystandards.organization/standards/pci-dss/)** is a set of standards and requirements that endeavors to protect credit & debit card info.

**Key elements include**

Building and maintaining network security: including firewalls, at rest and in-transit encryption, and secure network configurations. Protecting cardholder data: including stored payment data, encrypting data transmissions, and ensuring data security measures are in place. Maintaining vulnerability management: developing secure systems and applications, and identification and remediation of vulnerabilities. Implementing strong access control: restricting physical and logical access to cardholder data to only required business functions, and assigning unique IDs to users. Regular monitoring and testing: testing security systems and process, and maintaining an incident response plan.

Maintaining Information Security policies: establishing policies that address information security for all personnel and outline proper cardholder data handling, and maintaining compliance audits.

**[Federal Risk and Authorization Management Program (FedRAMP)](https://www.fedramp.gov/)** is a government-wide program that standardizes the security assessment, authorization, and monitoring of cloud services and products; the program was established in 2011 to help the federal government use cloud technologies while protecting federal information.

**Key elements include**

Standardized security framework: FedRAMP provides a common set of security controls, requirements, and baselines that cloud service providers (CSPs) must meet to provide federal agency solutions. Security assessment and authorization: requires CSPs to undergo third-party assessment by an authorized assessment organization (3PAO) to demonstrate compliance; this process leads to Authorization to Operate (ATO) or rejection. Continuous monitoring: FedRAMP emphasizes the importance of continuous monitoring to ensure security controls remain effective over time. Impact levels: categorizes services into three impact levels (low, moderate, and high) based on sensitivity of handled data; each level has specific controls.

Agency benefits: FedRAMP provides benefits such as reduced costs and time by eliminating redundant assessments since other federal agencies can reuse an authentication once a CSP obtains FedRAMP authorization, improved visibility and risk management and accelerated cloud adoption.

**[CIS Critical Security Controls](https://www.cisecurity.organization/controls)** is the CIS (Center for Internet Security) Critical Security Controls provides a prioritize set of actions to defend against threats; it focuses on practical steps to reduce the attack surface, like implementing secure configurations, managing admin privileges, and monitoring logs. **[Information Technology Infrastructure Library (ITIL)](https://www.axelos.com/certifications/itil-service-management/)**: ITIL is a set of practices for IT service management (ITSM) that focuses on aligning IT services with business needs; it includes elements of security governance, particularly in managing security incidents, changes, and service continuity, and is often integrated with other frameworks like ISO 27001.

**Committee of Sponsoring Organizations of the Treadway Commission (COSO)** is a framework that helps organizations reduce financial fraud by establishing, assessing, and enhancing their internal controls.

COSO's five components: Control Environment, Risk Assessment, Control Activities, Information & Communication, and Monitoring Activities.

<a id="subtopic-1-3-5"></a>

### 1.3.5 Due care/due diligence

**Due diligence**: establishing a plan, policy, and process to protect the interests of the organization; due diligence is knowing what should be done and planning for it; understanding your security governance principles (policies and procedures) and the risks to your organization; actions taken by a vendor to demonstrate or provide due care.

#### Due diligence often involves

Gathering information through discovery, risk assessments and review of existing documentation. Developing a formalized security structure containing a security policy, standards, baselines guidelines, and procedures. Documentation to establish written policies. Disseminating the information to the organization.

**Due care**: practicing the individual activities that maintain the due diligence effort; due care is about your legal responsibility within the law or within organization policies to implement your organization’s controls, follow security policies, do the right thing and make reasonable choices. Security documentation is the security policy. After establishing a framework for governance, security awareness training should be implemented, making sure that all new hires receive the training as then on-board, and all existing employees re-certify regularly (typically yearly). Due care is the responsible protection of assets.

Due diligence is the ability to prove due care.

### AI in this objective

**Governing the assistant.** Name an owner, define permitted uses, and establish a process for approving and reviewing the assistant. A useful governance decision says what the system may recommend, what it may execute, and what evidence is required before expanding its role. Keep the decision connected to Harbor's business goals and obligations. [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).

### Apply this objective

**Question.** Harbor acquires a company with an unfamiliar customer database. Is installing the standard firewall enough to demonstrate good governance?

**Reasoning.** No. Leadership needs an assessment of the acquired data, systems, obligations, and dependencies, with ownership and an integration plan. The firewall may be one control in that plan, but it does not establish whether the acquisition's risks are understood.

<a id="objective-1-4"></a>

## 1.4 Understand legal, regulatory, and compliance issues that pertain to information security in a holistic context

Legal and contractual obligations establish constraints on security decisions. Determine which organization, people, data, activity, and jurisdictions are involved before choosing a rule. A law may apply because of where the organization operates, whom it serves, or what kind of information it handles. Moving a server does not necessarily remove the obligation.

Treat the named laws below as a map of issues to investigate. Distinguish privacy rights, breach reporting, evidence access, intellectual property, and sector-specific requirements. Their scope and exceptions matter as much as a deadline. Harbor should involve legal and privacy specialists when obligations overlap, documenting the applicable rule and the decision rather than assuming that the strictest-sounding summary resolves every conflict.

<a id="subtopic-1-4-1"></a>

### 1.4.1 Cybercrimes and data breaches

The Gramm-Leach-Bliley Act eliminated the Glass-Steagall Act's restrictions against affiliations between commercial and investment banks in 1999. Understand the notification requirements placed on organizations that experience a data breach.

**Computer Fraud and Abuse Act (CFAA)** is a US federal cybersecurity bill enacted in 1986 as an amendment to existing law; amended multiple times (notably in 1996, 2001, 2008), the CFAA is designed to protect computers used by the government or in interstate commerce from a variety of abuses.

#### The CFAA covers a range of offenses including

Accessing a computer without authorization, or exceeding authorized access. Obtaining information illegally (e.g. from gov or financial institutions). Committing fraud via computer/system. Causing damage associated with DoS. Trafficking in passwords or access creds. Threatening to damage a computer, or to extort money/value.

**National Information Infrastructure Protection Act**: passed in 1996 as an additional set of CFAA amendments including coverage of computer systems used in international commerce, protections for additional national infrastructure, and treating as a felony any act that causes damage to critical national infrastructure. FISMA (see below). California's SB 1386 implemented the first statewide requirement to notify individuals of a breach of their personnel information; all other states eventually followed suit with similar laws. Federal breach notification requirements are not governed by a single, comprehensive law but are instead determined by a patchwork of laws covering specific industries; organizations must also comply with state laws, many of which are stricter than federal regulations.

The **HIPAA Breach Notification Rule** covers breaches of unsecured PHI. Notice to individuals is generally due without unreasonable delay and within 60 days. HHS reporting and media notification have distinct thresholds and procedures. [HHS](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html). Before an organization expands to other countries, perform due diligence to understand legal systems and what changes might be required to the way that data is handled and secured.

#### In particular, be familiar with

**Council of Europe Convention on Cybercrime** is a treaty signed by many countries that establishes standards for cybercrime policy. Laws about data breaches, including notification requirements.

In the US, the **Health Information Technology for Economic and Clinical Health (HITECH)** Act expanded HIPAA's breach reporting requiring notification of a data breach in some cases, such as when the personal health information was not protected as required by HIPAA.

For HIPAA breaches, notify affected individuals without unreasonable delay and within 60 days. HHS notification is due on that schedule for 500 or more affected individuals; smaller breaches have annual reporting. Media notice applies when more than 500 residents of a state or jurisdiction are affected. [HHS](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html).

**Glass-Steagall Act**: passed in 1933 and separated investment and commercial banking activities and created the Federal Deposit Insurance Corporation (FDIC). **GLBA (Gramm-Leach-Bliley Act)** imposes privacy and safeguards obligations on covered financial institutions. Breach reporting depends on the applicable regulator and rule; do not assume one deadline or recipient list for all institutions. [FTC Safeguards Rule](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know). Certain states also impose their own requirements concerning data breaches. Under GDPR Article 33, controllers notify the supervisory authority without undue delay and, where feasible, within 72 hours of awareness, unless the breach is unlikely to risk individuals' rights and freedoms. Individual notification has a different threshold. [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

**Communications Assistance to Law Enforcement Act (CALEA)** requires all communication carriers make wiretaps possible for law enforcement officials who have an appropriate court order. Some countries do not have any reporting requirements.

<a id="subtopic-1-4-2"></a>

### 1.4.2 Licensing and Intellectual Property requirements

**Intellectual property**: intangible assets (e.g. software, data). **Trademarks**: words, slogans, and logos used to identify a company and its products or services.

**Patents**: provide protection to the creators of new inventions; a temporary monopoly for producing a specific item such as a toy, which must be novel and unique to qualify for a patent.

**Utility**: protect the intellectual property rights of inventors. **Design**: cover the appearance of an invention and last for 15 years; note design patents don't protect the idea of an invention only its form, and are generally seen as weaker. Software: area of on-going controversy; e.g. Google vs Oracle and giving to a rise of "patent trolls".

**Copyright** protects original works of authorship, such as books, articles, poems, and songs; exclusive use of artistic, musical or literary works which prevents unauthorized duplication, distribution or modification. **Licensing** is a contract between the software producer and the consumer which limits the use and/or distribution of the software. **Trade Secrets**: trade secret laws protect the operating secrets of a firm; trade secrets are intellectual property that is critical to a business, and significant damage would result if it were disclosed to competitors or the public; the Economic Espionage Act imposes fines and jail sentences on someone found guilty of stealing trade secrets from a US corp.

<a id="subtopic-1-4-3"></a>

### 1.4.3 Import/export controls

Every country has laws around the import and export of hardware and software; e.g. the US has restrictions around the export of cryptographic technology, and Russia requires a license to import encryption technologies manufactured outside the country. **International Traffic in Arms Regulations (ITAR)** is a US regulation controlling the manufacture, export, and import of military or defense items (e.g. missiles, rockets, bombs, or anything else existing in the United States Munitions List (USML)). The Export Administration Regulations (EAR): EAR predominantly focuses on commercial use-related items like computers, lasers, marine items, and more; however, it can also include items that may have been designed for commercial use but actually have military applications.

<a id="subtopic-1-4-4"></a>

### 1.4.4 Transborder data flow

Organizations should adhere to origin country-specific laws and regulations, regardless of where data resides; also be aware of applicable laws where data is stored and systems are used. **Wassenaar Arrangement**: multinational agreement, voluntary export control.

<a id="subtopic-1-4-5"></a>

### 1.4.5 Issues related to privacy (e.g., General Data Protection Regulation (GDPR), California Consumer Privacy Act, Personal Information Protection Law, Protection of Personal Information Act)

Be familiar with the requirements around healthcare data, credit card data and other PII data as it relates to various countries and their laws and regulations. **California SB 1386 (2002)** introduced breach-notification requirements. Apply the current California statute and its scope, timing, and exceptions rather than assuming every incident requires immediate notice. [California Attorney General](https://oag.ca.gov/privacy/databreach/reporting).

#### California Consumer Privacy Act (CCPA): The CCPA applies to

For-profit businesses that collect consumers’ personal information (or have others collect personal information for them). Determine why and how the information will be processed.

#### Do business in California and meet any of the following

The original $25 million CCPA revenue threshold was adjusted to $26,625,000 effective January 1, 2025; check current applicability and adjustment rules. [CPPA](https://cppa.ca.gov/regulations/cpi_adjustment.html). Buy, sell, or share the personal information of 100k or more California residents or households; or. Get 50% or more of their annual revenue from selling or sharing California residents’ personal information.

The CCPA imposes separate obligations on service providers and contractors (who contract with businesses to process personal info) and other recipients of personal information from businesses. The CCPA does not generally apply to nonprofit organizations or government agencies.

#### California residents have the right to

(L)imit use and disclosure of personal info. (O)pt-out of sale or cross-context advertising. (C)orrect inaccurate info. (K)now what personal information business have and share. (E)qual treatment / nondiscrimination. (D)elete information business have on them.

See the National Conference of State Legislatures (NCSL) [list of state-based data breach notifications](https://www.ncsl.organization/technology-and-communication/security-breach-notification-laws).

#### Children's Online Privacy Protection Act (COPPA) of 1998

COPPA makes a series of demands on websites that cater to children or knowingly collect information from children:

Websites must have a privacy notice that clearly states the types of information they collect and what it's used for (including whether information is disclosed to third parties); must also include contact information for site operators. Parents must be able to review any information collected from children and permanently delete it from the site's records. Parents must give verifiable consent to the collection of information about children younger than the age of 13 prior to any such collection.

**Clarifying Lawful Overseas Use of Data (CLOUD)**: act allowing law enforcement to gather digital evidence from US companies regardless of where the data is stored.

US government can make bilateral agreements with other countries to provide reciprocal rights. US-based companies must comply with lawful orders for data disclosure from foreign governments. Companies are provided a mechanism to challenge data requests.

**Electronic Communication Privacy Act (ECPA)**: as amended, protects wire, oral, and electronic communications while those communications are being made, are in transit, and when they are stored on computers; makes it a crime to invade electronic privacy of an individual, and it broadened the Federal Wiretap Act. **Economic Espionage Act of 1996** is the EEA was enacted to address the threat of trade secret theft, misappropriations, or economic espionage by foreign entities changing the definition of theft so it was no longer restricted by physical constraints.

**Family Educational Rights and Privacy Act (FERPA)**: Grants privacy rights to students over 18, and the parents of minor students. **Fourth Amendment to the US Constitution** is the right of the people to be secure in their persons, houses, papers, effects against unreasonable search and seizure.

**General Data Protection Regulation (GDPR)**: replaced Data Protection Directive (DPD), purpose is to provide a single, harmonized law that covers data throughout the EU.

#### Key aspects

Lawfulness, fairness, and transparency. Purpose Limitation. Data Minimization. Accuracy. Storage Limitation. Security. Accountability.

GDPR territorial scope depends on establishment in the EU or relevant offering of goods or services to, or monitoring of, people in the Union. Rights and lawful bases depend on the processing context; consent and an unrestricted opt-out are not universal requirements. [GDPR Articles 3 and 6](https://eur-lex.europa.eu/eli/reg/2016/679/oj). Be familiar with the EU Data Protection Directive (Directive 95/46/EC, which was superseded by GDPR).

GLBA: see above. HIPAA: (see above) note that HITECH updated many of HIPAA's privacy and security requirements, including requiring a written contract between a HIPAA-covered entity and their business associates (e.g. organizations that handle PHI on their behalf). **HITECH** strengthened HIPAA breach notification. Individuals generally receive notice without unreasonable delay and within 60 days; HHS reporting differs for breaches affecting fewer than 500 versus 500 or more people. [HHS](https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html). **Organization for Economic Co-operation and Development (OECD)**: 8 best practices privacy principles: collection limitation, data quality, purpose specification, use limitation, security safeguards, openness, individual participation, and accountability; require organizations to avoid unjustified obstacles to trans-border data flow, set limits to personal data collection, protect personal data with reasonable security and more.

**Privacy Act of 1974** is a US federal law designed to protect individuals' personal information help by federal government agencies, mandating that agencies only keep records necessary for conducting their business, and procedures for people to get access to the government maintained records. **Personal Information Protection and Electronic Documents Act (PIPEDA)**: Canadian law that governs the use of personal information.

**Personal Information Protection Law (PIPL)**: comprehensive Chinese data privacy law, with similarities to GDPR.

#### Key aspects of PIPL

PIPL provides consent and other specified grounds for processing. Assess necessity, purpose, and any separate-consent requirements; individuals may withdraw consent where processing relies on it. [PIPL](https://en.npc.gov.cn.cdurl.cn/2021-12/29/c_694559.htm). Minimum Data Collection: PIPL requires organizations to collect only relevant and necessary personal data. Data Subject Rights: provides people with rights to access, correction, deletion, and to be informed of data breaches. Cross-Border Data Transfer: imposes restrictions on transferring personal data outside of China.

**Privacy Shield** and its predecessor Safe Harbor are historical transfer arrangements, not the only possible transfer mechanisms. Assess the applicable current transfer basis; the source notes also identify the later EU-US Data Privacy Framework. [European Commission](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/eu-us-data-transfers_en).

The EU-US Privacy Shield was invalidated by the Court of Justice of the European Union (CJEU) in the "Schrems II" ruling (July 2020) and has been replaced by the EU-US Data Privacy Framework (DPF) adopted in July 2023.

**Protection of Personal Information Act (POPIA)**: South Africa's comprehensive data protection law designed to protect personal information processed by public and private entities, and promote the right to privacy.

#### Key provisions of POPIA

Applies to any organization processing PII of natural or juristic persons in SA.

**Eight conditions for lawful processing**

Accountability. Processing limitation (minimality and consent). Purpose specification. Information quality. Openness. Security safeguards. Data subject participation. Limitation on further processing.

Consent is one possible basis for processing under POPIA; assess the applicable lawful justification and additional conditions for children or special personal information. [Information Regulator](https://inforegulator.organization.za/popia/). Strict conditions on special personal information (race, religion, trade union membership, political affiliation etc). Restricts cross-border information transfers unless recipient country has similar privacy protections. Penalties for POPIA violation can be severe, enforced by the Information Regulator.

**US Patriot Act of 2001**: enacted following the September 11 attacks with the stated goal of tightening U.S. national security, particularly as it related to foreign terrorism.

#### The act included three main provisions

Expanded surveillance abilities of law enforcement, including by tapping domestic and international phones. Easier interagency communication to allow federal agencies to more effectively use all available resources in counter-terrorism efforts, allowing government to obtain detailed information on user activity through a subpoena, and ISPs can voluntarily provide a large range of information to the government. Increased penalties for terrorism crimes and an expanded list of activities which would qualify for terrorism charges.

<a id="subtopic-1-4-6"></a>

### 1.4.6 Contractual, legal, industry standards, and regulatory requirements

Understand the difference between criminal, civil, and administrative law.

**Criminal law** protects society against acts that violate the basic principles we believe in; violations of criminal law are prosecuted by federal and state governments. **Civil law** provides the framework for the transaction of business between people and organizations; violations of civil law are brought to the court and argued by the two affected parties. **Administrative law**: used by government agencies to effectively carry out their day-to-day business.

**Compliance**: Organizations may find themselves subject to a wide variety of laws, and regulations imposed by regulatory agencies or contractual obligation.

**Payment Card Industry Data Security Standard (PCI DSS)**: governs the security of credit card information and is enforced through the terms of a merchant agreement between a business that accepts CC payments, and the bank that processes the business' transactions.

**Sarbanes-Oxley (SOX)**: governs publicly traded corps; financial systems may be audited to ensure security controls are sufficient to ensure compliance with SOX; requires top management to individually certify the accuracy of financial info.

Violations include criminal penalties.

**Gramm-Leach-Bliley Act (GLBA)**: affects banks, insurance companies, and credit providers; included a number of limitations on the types of information that could be exchanged even among subsidiaries of the same corp, and required financial institutions to provide written privacy policies to all their customers.

**Health Insurance Portability and Accountability Act (HIPAA)** establishes privacy and security requirements for covered entities and relevant business associates, with individual rights and notice obligations. Scope depends on the entity and activity, not simply possession of medical information. [HHS covered entities](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html).

Includes criminal penalties for violations.

**Federal Information Security Management Act (FISMA)** requires federal agencies to implement an information security program that covers the agency's operations and contractors; the Federal Information Security Modernization Act of 2014 amended the 2002 version of FISMA by centralizing federal cybersecurity responsibility within the Department of Homeland Security (DHS) except for defense-related cybersecurity and scope of the DNI (Director of National Intelligence); the Cybersecurity Enhancement Act of 2014 charged NIST with coordination of voluntary nation-wide cybersecurity standards. **Electronic Communications Privacy Act (ECPA)**: in short, makes it a crime to invade the electronic privacy of an individual; passed in 1986 to expand and revise federal wiretapping and electronic eavesdropping provisions, making it a crime to intercept or procure electronic communications, and includes important provisions that protect a person’s wire and electronic communications from being intercepted by another private individual.

**Digital Millennium Copyright Act (DMCA)**: prohibits the circumvention of copyright protection mechanisms placed in digital media and limits the liability of internet service providers for the activities of their users.

### AI in this objective

**AI privacy obligations.** Putting personal information into a prompt or a training dataset is still processing information. For Harbor's proposed assistant, determine the purpose, applicable authority, recipients, retention, and supplier use before uploading support conversations. A convenient interface does not establish that a new use is permitted. [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).

### Apply this objective

**Question.** Harbor stores European customer data with a US supplier. Can it decide its privacy obligations solely from the server's location?

**Reasoning.** No. It must assess applicable territorial scope, processing roles, transfer conditions, contracts, and data-subject rights. Location is one factor; it does not by itself determine which obligations apply.

<a id="objective-1-5"></a>

## 1.5 Understand requirements for investigation types (i.e., administrative, criminal, civil, regulatory, industry standards)

An investigation begins with a question and an authority to pursue it. A policy violation, suspected crime, commercial dispute, and regulatory inquiry may concern the same event but involve different investigators, procedures, and standards of proof. Identify those differences before collecting information.

Internal work still needs reliable records. Evidence collected casually may later be needed in litigation or a regulatory response. Harbor should preserve relevant material, document actions, restrict access, and coordinate with counsel or law enforcement as appropriate. Domain 7 explains the handling and forensic techniques in more detail.

An investigation will vary based on incident type, e.g. for a financial services company, a financial system compromise might cause a regulatory investigation; a system breach or website compromise might cause a criminal investigation; each type of investigation has special considerations:

**Administrative**: internal investigations usually review operational issues or violations of an organization's policies; often tied to HR scenarios, an admin investigation could be part of technical troubleshooting; since these investigations are for internal purposes, they usually have the lowest formality and standards in terms of documentation or procedures compared to other types; admin investigations often focus on finding the root cause of operational issues.

**Criminal** is a criminal investigation occurs when a crime has been committed and you are working with a law enforcement agency to convict the alleged perpetrator; in such a case, it is common to gather evidence for a court of law, and to share the evidence with the defense.

You need to gather and handle the information using methods that ensure the evidence can be used in court. In a criminal case, a suspect must be proven guilty beyond a reasonable doubt; a higher bar compared to a civil case, which is showing a preponderance of evidence.

**Civil**: in a civil case, one person or entity sues another, e.g. one company could sue another for a trademark violation.

A civil case is typically about monetary damages, and doesn't involve criminality. In a civil case, a preponderance of evidence is required to secure a victory, differing from criminal cases, where a suspect is innocent until proven guilty beyond a reasonable doubt; evidence collection standards for civil investigations usually are lower than criminal cases.

**Industry Standards** is an industry standards investigation is intended to determine whether an organization is adhering to a specific industry standard or set of standards, such as those associated with PCI DSS; because standards are not laws, these investigations can be related to contractual compliance, and an organization may be required to participate in audits or assessments.

Because industry standards represent well-understood and widely implemented best practices, many organizations try to adhere to them even when they are not required to do so in order to improve security, and reduce operational and other risks.

**Regulatory** is a regulatory investigation is conducted by a regulatory body, such as the Securities and Exchange Commission (SEC) or Financial Industry Regulatory Authority (FINRA), against an organization suspected of an infraction.

Here the organization is required to comply with the investigation, e.g., by not hiding or destroying evidence.

### Apply this objective

**Question.** An internal misuse investigation uncovers suspected fraud. Should the team continue deleting irrelevant-looking files as part of routine cleanup?

**Reasoning.** It should preserve potentially relevant material and reassess its authority and procedures with the appropriate stakeholders. A change in investigative purpose can change preservation and disclosure requirements; routine cleanup must not destroy evidence.

<a id="objective-1-6"></a>

## 1.6 Develop, document, and implement security policy, standards, procedures and guidelines

Security documentation connects a business intention to repeatable work. A policy states the required outcome and authority. A standard specifies mandatory requirements. A baseline describes a minimum configuration. A procedure tells someone how to perform a task, while a guideline offers recommended ways to handle situations that permit judgment.

Harbor might require protection of customer information in policy, approved encryption settings in a standard, a hardened server image as a baseline, and a key-rotation procedure for operators. Keeping these levels distinct makes it easier to update technical steps without rewriting the organization's overall intent.

To create a comprehensive security plan, you need the following items: security policy, standards, baselines, guidelines, and procedures.

The top tier of a formalized hierarchical organization security documentation is the security policy.

**Policy**: docs created by and published by senior management describing organizational strategic goals. A security policy is a document that defines the scope of security needed by the organization, discussing assets that require protection and the extent to which security solutions should go to provide the necessary protections. It defines the strategic security objectives, vision, and goals and outlines the security framework of the organization.

**Acceptable Use Policy (AUP)** is the AUP is a commonly produced document that exists as part of the overall security documentation infrastructure.

This policy defines a level of acceptable performance and expectation of behavior and activity; failure to comply with the policy may result in job action warnings, penalties, or termination.

Security Standards, Baselines and Guidelines: once the main security policies are set, the remaining security documentation can be crafted from these policies.

**Policies**: these are high-level documents, usually written by the management team; policies are mandatory, and a policy might provide requirements, but not the steps for implementation. **Standards**: specific mandates explicitly stating expectations of performance/conformance; more descriptive than policies, standards define compulsory requirements for the homogeneous use of hardware, software, technology, and security controls, uniformly implemented throughout the organization.

**Baselines** defines a minimum level of security that every system throughout the organization must meet; baselines are usually system specific and refer to industry / government standards.

E.g. a baseline for server builds would be a list of configuration areas that should be applied to every server that is built. A Group Policy Object (GPO) in a Windows network is sometimes used to comply with standards; configuration management solutions can also help you establish baselines and spot configurations that are not in alignment.

**Guidelines**: offers recommendations on how standards and baselines should be implemented & serves as an operational guide for security professionals and users.

Guidelines are flexible, and can be customized for unique systems or conditions; they state which security mechanism should be deployed instead of prescribing a specific product or control; they are not compulsory, but are suggested practices and expectations of activity to best accomplish tasks and goals.

**Procedures** (AKA Standard Operating Procedure or SOP): detailed, step-by-step how-to doc that describes the exact actions necessary to implement a specific security mechanism, control, or solution.

### Apply this objective

**Question.** A technician needs the exact steps for restoring a database. Which document should provide them?

**Reasoning.** A procedure should give the steps, checks, and escalation points. The policy establishes the recovery requirement, and standards may specify acceptable backup protections, but neither substitutes for an executable recovery procedure.

<a id="objective-1-7"></a>

## 1.7 Identify, analyze, assess, prioritize, and implement Business Continuity (BC) requirements

Business continuity starts with the activities the organization must keep performing. A business impact analysis asks what happens when an activity stops and how the harm grows over time. It identifies dependencies and recovery needs before the team buys backup products or chooses another location.

Recovery time objective (RTO) is the target limit for restoring service; recovery point objective (RPO) expresses tolerable data loss as a period of time. Maximum tolerable downtime is the business's outer limit for an interruption. Allow time for restoration and business validation inside that limit. Keeping a server available is useful only if the people, suppliers, networks, and procedures needed for the business activity also work.

<a id="subtopic-1-7-1"></a>

### 1.7.1 Business Impact Analysis (BIA)

**Business impact analysis (BIA)**: Identify the systems and services that the business relies on and assess the impacts that a disruption or outage would cause, including the impacts on business processes like accounts receivable and sales.

Step 1: Identification of priorities. Step 2: Risk identification. Step 3: Likelihood assessment.

#### Step 4: Resource prioritization

Deciding which systems and services you need to get things running again (think foundational IT services such as the network and directory, which many other systems rely on). And prioritize the order in which critical systems and services are recovered or brought back online.

#### As part of the BIA, establish

**recovery time objectives (RTO)**: how long it takes to recover; maximum tolerable time to recover systems to a defined service level. **recovery point objectives (RPO)** is the maximum tolerable data loss measured in time. **maximum tolerable downtime (MTD) or maximum allowable downtime (MAD)** is the length of time an organization can suffer the loss of its critical path or critical functions before ceasing to be a viable enterprise; how long an organization can survive an interruption of critical functions. **MTTR**: mean time to repair is the average length of time required to perform a repair on the device (also see Domain 7).

**MTBF**: mean time between failure is an estimation of time between the first and any subsequent failures (also see Domain 7). Along with the costs of downtime and recovery.

**Continuity planning** is the first two phases of the BCP process (project scope and planning and the business impact analysis) focus on determining how the BCP process will work and prioritizing the business assets that need to be protected against interruption.

The next phase of BCP development, continuity planning, focuses on the development and implementation of a continuity strategy to minimize the impact realized risks might have on protected assets.

There are two primary subtasks/phases involved in continuity planning:

**Strategy development**: in this phase, the BCP team determines which risks they will mitigate. **Provisions and processes**: in this phase, the team designs mechanisms and procedures that will mitigate identified risks.

The goal of this process is to create a **continuity of operations plan (COOP)**, which focuses on how an organization will carry out critical business functions starting shortly after a disruption occurs and extending up to one month of sustained operations.

#### Approval and implementation

BCP plan now needs sr. management buy-in (should be endorsed by the organization's top exec). BCP team should create an implementation schedule, and all personnel involved should receive training on the plan.

**Business Continuity Planning (BCP)** involves assessing the risk to organizational processes and creating policies, plans, and procedures to minimize the impact those risks might have on the organization if they were to occur.

BCP is used to maintain the continuous operation of a business in the event of an emergency, with a goal to implement a combination of policies, procedures, and processes. Business continuity requires a lot of planning and preparation; actual implementation of business continuity processes occur quite infrequently.

#### The primary facets of business continuity are

Resilience: (e.g. within a data center and between sites or data centers). Recovery: if a service becomes unavailable, you need to recover it as soon as possible. Contingency: a last resort in case resilience and recovery prove ineffective.

#### The BCP process has four main steps

Project scope and planning. Business Impact Analysis. Continuity planning. Approval and Implementation.

**Project scope and planning**: Developing the project scope and plan starts with gaining support of the management team, making a business case (cost/benefit analysis, regulatory or compliance reasons etc.) and gaining approval to move forward.

Next, you need to form a team with representatives from the business as well as IT.

Next, start with a business continuity policy statement, conduct a business impact analysis (see next item), and then develop the remaining components: preventive controls; relocation; the actual continuity plan; testing; training and maintenance.

#### BCP vs DR

BCP activities are typically strategically focused at a high level and center themselves on business processes and operations. DR plans tend to be more tactical and describe technical activities such as recovery sites, backups, and fault tolerance.

The overall goal of BCP is to provide a quick, calm, and efficient response in the event of an emergency and to enhance a company's ability to quickly recover from a disruptive event.

<a id="subtopic-1-7-2"></a>

### 1.7.2 External dependencies

It's important to explore external party and vendor roles and responsibilities as part of the BCP process to understand and plan for how these organizations/services will impact your organization's contingency plans.

External party contingency review includes (but is not limited to) vendors supplying critical hardware and software, cloud services, legal/regulatory concerns etc.

The top priority of BCP and DRP is people: **Always prioritize people's safety**; get people out of harm's way, and then address IT recovery and restoration issues.

### Apply this objective

**Question.** Harbor can tolerate losing 15 minutes of transactions and needs service restored within four hours. What do these requirements mean?

**Reasoning.** The RPO is 15 minutes and the RTO is four hours. The first drives how current the recoverable data must be; the second drives how quickly the complete service must return. Both must be tested against business needs.

<a id="objective-1-8"></a>

## 1.8 Contribute to and enforce personnel security policies and procedures

Personnel security follows a person's relationship with the organization. Screening helps establish suitability for a role; agreements and training establish expectations; access provisioning enables approved work; transfers and departures change what should remain accessible. These are coordinated business processes involving human resources, managers, legal staff, and security.

People also detect and report problems. Harbor should make safe behavior practical, give staff clear reporting routes, and avoid relying on awareness alone to compensate for excessive privileges or confusing systems. Background checks and employment restrictions must be appropriate to the role and applicable law.

People are often considered the weakest element in any security solution; no matter what physical or logical controls are deployed, humans can discover ways to avoid, circumvent/subvert, or disable them.

Malicious actors are routinely targeting users with phishing and spear phishing campaigns, social engineering, and other types of attacks, and everybody is a target. Once attackers compromise an account, they can use that entry point to move around the network and elevate their privileges. People can also become a key security asset when they are properly trained and are motivated to protect not only themselves but the security of the organization as well. Part of planning for security includes having standards in place for job descriptions, job classifications, work tasks, job responsibilities, prevention of collusion, candidate screening, background checks, security clearances, employment and nondisclosure agreements.

<a id="subtopic-1-8-1"></a>

### 1.8.1 Candidate screening and hiring

#### The following strategies can reduce your risk

#### Candidate screening and hiring

Screening employment candidates thoroughly is a key part of the hiring process. Be sure to conduct a full background check that includes a criminal records check, job history verification, education verification, certification validation and confirmation of other accolades when possible. All references should be contacted.

<a id="subtopic-1-8-2"></a>

### 1.8.2 Employment agreements and policies driven requirements

**Employment agreement** specifies job duties, expectations, rate of pay, benefits and information about termination; sometimes, such agreements are for a set period (for example, in a contract or short-term job).

Employment agreements facilitate termination when needed for an underperforming employee. Clear, lawful employment terms help establish expectations, but additional wording alone does not guarantee less litigation risk. E.g. a terminated employee might take a copy of their email with them without thinking of it as stealing, but they are less likely to do so if an employment agreement or another policy document clearly prohibits it.

#### Example employee agreements

Non-compete. Codes of conduct such as an acceptable use policy (AUP), which defines what is and isn’t acceptable activity, practice, or use for company equipment and resources. Nondisclosure agreement (NDA), which is a doc used to protect confidential information from being disclosed by a current or former employee.

**Compliance** is the act of confirming or adhering to rules, policies, regulations, standards, or requirements. On a personnel level, compliance is related to individual employees following company policies and procedures. Employees need to be trained on company standards as defined in the security policy and remain in compliance with any contractual obligations (e.g. with PCI DSS).

Compliance is a form of administrative or managerial security control. **Compliance enforcement** is the application of sanctions or consequences for failing to follow policy, training, best practices, or regulations. Personally identifiable information (PII) about employees, partners, contractors, customers and others should be stored in a secure way, accessible only to those who require the information to perform their jobs. Organizations should maintain a documented privacy policy outlining the type of data covered by the policy and who the policy applies to. Employees and contractors should be required to read and agree to the privacy policy upon hire and on a regular basis thereafter (such as annually).

<a id="subtopic-1-8-3"></a>

### 1.8.3 Onboarding, transfers and termination processes

**Onboarding** is a process of bringing a new employee into the organization.

Creating documented processes allowing the new employee to be integrated quickly and consistently.

**Transfer** is an employee moves from one job to another, likely requiring adjusted account access to maintain appropriate least privilege.

**Termination or offboarding**: offboarding is the removal of an employee's identity from the IAM system, once that person has left the organization; can also be an element used when an employee transfers into a new role.

Coordinate departure access revocation, equipment return, and any escort with human resources and the assessed risk; do not assume every departure requires the same physical response.

<a id="subtopic-1-8-4"></a>

### 1.8.4 Vendor, consultant, and contractor agreements and controls

Organizations commonly outsource many IT functions, particularly data center hosting, contact-center support, and application development.

Info security policies and procedures must address outsourcing security and the use of service providers, vendors and consultants.

E.g. access control, document exchange and review, maintenance, on-site assessment, process and policy review, and Service Level Agreements (SLAs) are examples of outsourcing security considerations.

### Apply this objective

**Question.** A support employee moves into sales. Is adding sales access sufficient?

**Reasoning.** No. Review and remove support privileges that the new role no longer requires, then approve the new access. Otherwise privileges accumulate across transfers and undermine least privilege.

<a id="objective-1-9"></a>

## 1.9 Understand and apply risk management concepts

Risk describes potential harm to something valuable, considering both likelihood and impact. A threat is a possible cause of harm; a vulnerability is a weakness that contributes to it. An exposed administration interface is a vulnerability, an attacker attempting unauthorized access is a threat, and loss of customer records is a possible consequence.

For a quantitative example, suppose an asset is valued at $100,000 and a particular event would destroy 20% of its value. Single loss expectancy is $100,000 x 0.20 = $20,000. If the event is expected once every four years, annualized rate of occurrence is 0.25 and annualized loss expectancy is $5,000. A $2,000 annual control that reduces the annualized loss to $1,000 has an estimated net annual benefit of $2,000. These estimates support judgment; they do not make uncertain inputs exact.

Treatment can reduce, avoid, share or transfer, or accept a risk. The authorized owner must consider obligations and business effects as well as cost. Risk remaining after treatment is residual risk and still needs review.

<a id="subtopic-1-9-1"></a>

### 1.9.1 Threat and vulnerability identification

**Risk Management** is a process of identifying factors that could damage or disclose data, evaluating those factors in light of data value and countermeasure cost, and implementing cost-effective solutions for mitigating or reducing risk. **Threat** is any potential occurrence that may cause an undesirable or unwanted outcome for a specific asset; they can be intentional or accidental; loosely think of a threat as a weapon that could cause harm to a target. **Vulnerability** is the weakness in an asset, or weakness (or absence) of a safeguard or countermeasure; a flaw, limitation, error, frailty, or susceptibility to harm.

Threats and vulnerabilities are related: a threat is possible when a vulnerability is present.

Threats exploit vulnerabilities, which results in exposure. Exposure is risk, and risk is mitigated by safeguards. Safeguards protect assets that are endangered by threats. **Threat Agent/Actor**: intentionally exploit vulnerabilities. **Threat Event**: accidental occurrences and intentional exploitations of vulnerabilities. **Threat Vector**: (AKA attack vector) is the path or means by which an attack or attacker can gain access to a target in order to cause harm. **Exposure**: being susceptible to asset loss because of a threat; the potential for harm to occur. **Exposure Factor (EF)**: derived from this concept; an element of quantitative risk analysis that represents the percentage of loss that an organization would experience if a specific asset were violated by a realized risk.

**Single Loss Expectancy (SLE)** is an element of quantitative risk analysis that represents the cost associated with a single realized risk against a specific asset;.

SLE = asset value (AV) * exposure factor (EF). Where EF is a metric that represents the loss a realized threat would have on a specific asset, quantified as a percentage: e.g. an EF of 0.2 (or 20%) for a specific threat would indicate that a realization of that threat would result in a loss of 20% of the asset’s value. EF is not a fixed number for an asset, but is a unique value determined by a specific threat affecting a specific asset.

**Annualized rate of occurrence (ARO)** is an element of quantitative risk analysis that represents the expected frequency with which a specific threat or risk will occur within a single year.

**Annualized loss expectancy (ALE)** is an element of quantitative risk analysis that represents the possible yearly cost of all instances of a specific realized threat against a specific asset.

ALE = SLE * ARO.

**Safeguard evaluation**: ALE for an asset if a safeguard is implemented.

ALE before safeguard - ALE with safeguard - annual cost of safeguard; or (ALE1 - ALE2) - ACS.

**Risk** is the possibility or likelihood that a threat will exploit a vulnerability to cause harm to an asset and the severity of damage that could result; the the greater the potential harm, the greater the risk. **risk appetite** vs. **risk tolerance** vs. **risk capacity** are commonly tested concepts: **Risk appetite** is the total amount of risk an organization is willing to accept. **Risk tolerance** is the acceptable level of variation in outcomes relative to a specific objective. **Risk capacity** is the maximum amount of risk an organization can support or absorb.

<a id="subtopic-1-9-2"></a>

### 1.9.2 Risk analysis, assessment, and scope

**Risk Assessment**: used to identify the risks and set criticality priorities, and then risk response is used to determine the best defense for each identified risk. Risk assessment relates potential events, vulnerabilities, likelihood, and impact; a vulnerability alone is not a complete statement of risk. Risk = threat x vulnerability is a conceptual mnemonic, not a universal numeric formula. A quantitative estimate needs defined likelihood and impact inputs. Addressing the threat, threat agent or vulnerability directly results in a reduction of risk (known as threat mitigation).

All IT systems have risk; all organizations have risk; there is no way to eliminate 100% of all risks.

Instead upper management must decide which risks are acceptable, and which are not; there are two primary risk-assessment methodologies:

**Quantitative Risk Analysis**: assigns real dollar figures to the loss of an asset and is based on mathematical calculations. **Qualitative Risk Analysis**: assigns subjective and intangible values to the loss of an asset and takes into account perspectives, feelings, intuition, preferences, ideas, and gut reactions; qualitative risk analysis is based more on scenarios than calculations, and threats are ranked to evaluate risks, costs, and effects.

Most organizations employ a hybrid of both risk assessment methodologies. The goal of risk assessment is to identify risks (based on asset-threat parings) and rank them in order of criticality.

<a id="subtopic-1-9-3"></a>

### 1.9.3 Risk response and treatment (e.g. cybersecurity insurance)

**Risk response** is the formulation of a plan for each identified risk; for a given risk, you have a choice for a possible risk response:

**Risk Mitigation**: reducing risk, or risk mitigation, is the implementation of safeguards, security controls, and countermeasures to reduce and/or eliminate vulnerabilities or block threats. **Risk Assignment**: assigning or transferring risk is the placement of the responsibility of loss due to a risk onto another entity or organization; AKA assignment of risk and transference of risk.

**Risk Deterrence**: deterrence is the process of implementing deterrents for would-be violators of security and policy.

The goal is to convince a threat agent not to attack. E.g. implementing auditing, security cameras, and warning banners; using security guards.

**Risk Avoidance**: determining that the impact or likelihood of a specific risk is too great to be offset by potential benefits, and not performing a particular business function due to that determination; the process of selecting alternate options or activities that have less associated risk than the default, common, expedient, or cheap option.

**Risk Acceptance** is the result after a cost/benefit analysis determines that countermeasure costs would outweigh the possible cost of loss due to a risk.

Also means that management has agreed to accept the consequences/loss if the risk is realized.

**Risk Rejection** is an unacceptable possible response is to reject risk or ignore risk; denying that risk exists and hoping that it will never be realized are not valid prudent due care/due diligence responses to risk. **Risk Transference**: paying an external party (i.e. an insurance company) to accept the financial impact of a given risk.

**Inherent Risk** is the level of natural, native, or default risk that exists in an environment, system, or product prior to any risk management efforts being performed (AKA initial or starting risk); this is the risk identified by the risk assessment process. **Residual Risk** is the risk remaining after controls or other treatment. It may require additional treatment or explicit acceptance; it is not automatically accepted simply because controls exist. **Total Risk** is the amount of risk an organization would face if no safeguards were implemented.

**Conceptual Total Risk Formula**: threats x vulnerabilities x asset value = total risk. **Controls Gap**: amount of risk that is reduced by implementing safeguards, or the difference between total risk and residual risk. **Conceptual Residual Risk Formula**: total risk - controls gap = residual risk. Risk should be reassessed on a periodic basis to maintain reasonable security because security changes over time.

**Countermeasure**: AKA a "control" or "safeguard" can help reduce risk.

For exam prep, understand how the concepts are integrated into your environment; this is not a step-by-step technical configuration, but the process of the implementation — where you start, in which order it occurs and how you finish.

Bear in mind that security should be designed to support and enable business tasks and functions.

Security controls, countermeasures, and safeguards can be implemented administratively, logically / technically, or physically. These 3 categories should be implemented in a conceptual layered defense-in-depth manner to provide maximum benefit. Based on the concept that policies (part of administrative controls) drive all aspects of security and thus form the initial protection layer around assets. Then, logical and technical controls provide protection against logical attacks and exploits. Then, physical controls provide protection against real-world physical attacks against facilities and devices.

<a id="subtopic-1-9-4"></a>

### 1.9.4 Applicable types of controls (e.g., preventive, detection, corrective)

#### Three ways to implement mitigating controls

**Administrative** is the policies and procedures defined by an organization's security policy and other regulations or requirements. **Technical / Logical**: examples include firewalls, automated backups, encryption. **Physical**: security mechanisms focused on providing protection to the facility and real world objects.

#### Safeguards

**Preventive** is a preventive or preventative control is deployed to thwart or stop unwanted or unauthorized activity from occurring. **Deterrent** is a deterrent control is deployed to discourage security policy violations; deterrent and preventative controls are similar, but deterrent controls often depend on individuals being convinced not to take an unwanted action. **Directive** is a directive control is deployed to direct, confine, or control the actions of subjects to force or encourage compliance with security policies.

#### Countermeasures

**Detective** is a detective control is deployed to discover or detect unwanted or unauthorized activity; detective controls operate after the fact. **Corrective** is a corrective control modifies the environment to return systems to normal after an unwanted or unauthorized activity has occurred; it attempts to correct any problems resulting from a security incident. **Recovery** is an extension of corrective controls but have more advanced or complex abilities; a recovery control attempts to repair or restore resources, functions, and capabilities after a security policy violation. Recovery controls typically address more significant damaging events compared to corrective controls, especially when security violations may have occurred.

**Compensating** is a compensating control is deployed to provide various options to other existing controls, to aid in enforcement and support of security policies.

They can be any controls used in addition to, or in place of, another control. They can be a means to improve the effectiveness of a primary control or as the alternative or failover option in the event of a primary control failure.

<a id="subtopic-1-9-5"></a>

### 1.9.5 Control assessments (e.g. security and privacy)

**Security Control Assessment (SCA)**: formal evaluation and review of individual controls against a baseline; tests if an organization's security controls (technical, administrative, and physical) are implemented correctly, functioning as intended and meeting security requirements. Basically a formal evaluation of a defined set of controls against a baseline or reliability expectation; may be conducted with the Security Test and Evaluation (ST&E); [NIST Special Publication 800-53A Security and Privacy Controls for Federal Information Systems and Organizations](https://www.nist.gov/privacy-framework/nist-sp-800-53a) ensure the security requirements and enforcement of appropriate security controls.

#### Goals of SCA

Ensure the effectiveness of the security mechanisms. Evaluate the quality and thoroughness of the risk management processes. Produce a report of the relative strengths and weaknesses of the deployed security infrastructure.

An SCA goal is to ensure security mechanism effectiveness; periodically assess security and privacy controls to determine what’s working, what isn’t.

As part of this assessment, the existing documents should be thoroughly reviewed, and some of the controls tested randomly. A report is typically produced to show the outcomes and enable the organization to remediate deficiencies. Often, security and privacy control assessments are performed and/or validated by different teams, with the privacy team handling the privacy aspects.

For federal agencies, an SCA process generally is based on SP 800-53.

<a id="subtopic-1-9-6"></a>

### 1.9.6 Continuous monitoring and measurement

Monitoring and measurement are closely aligned with identifying risks. While monitoring is used for more than security purposes, monitoring should be tuned to ensure the organization is notified about potential security incidents as soon as possible. If a security breach occurs, monitored systems and data become valuable from a forensics perspective; from the ability to derive root cause of an incident to making adjustments to minimize the chances of reoccurrence.

<a id="subtopic-1-9-7"></a>

### 1.9.7 Reporting (e.g., internal, external)

Risk Reporting is a key task to perform at the conclusion of risk analysis (i.e. production and presentation of a summarizing report).

A Risk Register or Risk Log is a document that inventories all identified risks to an organization or system or within an individual project.

A risk register is used to record and track the activities of risk management, including: identifying risks; evaluating the severity of, and prioritizing those risks; prescribing responses to reduce or eliminate the risks; track the progress of risk mitigation.

<a id="subtopic-1-9-8"></a>

### 1.9.8 Continuous improvement (e.g., risk maturity modeling)

Risk analysis is performed to provide upper management with the details necessary to decide which risks should be mitigated, which should be transferred, which should be deterred, which should be avoided, and which should be accepted; to fully evaluate risks and subsequently take proper precautions, the following must be analyzed: assets; asset valuation; threats; vulnerabilities; exposure; risk; realized risk; safeguards; countermeasures; attacks; breaches.

An **Enterprise Risk Management** (ERM) program can be evaluated using an RMM.

**Risk Maturity Model (RMM)**: assesses the key indicators and activities of a mature, sustainable, and repeatable risk management process, typically relating the assessment of risk maturity against a five-level model such as:

**Ad hoc** is a chaotic starting point from which all organizations initiate risk management. **Preliminary**: loose attempts are made to follow risk management processes, but each department may perform risk assessment uniquely. **Defined** is a common or standardized risk framework is adopted organization-wide. **Integrated**: risk management operations are integrated into business processes, metrics are used to gather effectiveness data, and risk is considered an element in business strategy decisions. **Optimized**: risk management focuses on achieving objectives rather than just reacting to external threats; increased strategic planning is geared toward business success rather than just avoiding incidents; and lessons learned are re-integrated into the risk management process.

<a id="subtopic-1-9-9"></a>

### 1.9.9 Risk frameworks (e.g., International Organization for Standardization (ISO), National Institute of Standards and Technology (NIST), Control Objectives for Information and Related Technology (COBIT), Sherwood Applied Business Security Architecture (SABSA), Payment Card Industry (PCI))

See section 1.3.4 above for definitions of these frameworks. A risk framework is a guide or recipe for how risk is to be assessed, resolved, and monitored. NIST established the **Risk Management Framework** (RMF) and the **Cybersecurity Framework** (CSF): the CSF is a set of guidelines for mitigating organizational cybersecurity risks, based on existing standards, guidelines, and practices.

The RMF is intended as a risk management process to identify and respond to threats, and is defined in three core, interrelated Special Publications:

SP 800-37 Rev 2, Risk Management Framework for Information Systems and Organizations. SP 800-39, Managing Information Security Risk.

[SP 800-30 Rev 1, Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final) outlines four primary steps to conduct a risk assessment.

Prepare for the assessment.

**Conduct assessment**

Identify threat sources and events. Identify vulnerabilities and predisposing conditions. Determine likelihood of occurrence. Determine magnitude of impact. Determine risk.

Communicate results. Maintain assessment.

#### The RMF has 7 steps, and six cyclical phases

**Prepare** to execute the RMF from an organization and system-level perspective by establishing a context and priorities for managing security and privacy risk. **Categorize** the system and the information processed, stored, and transmitted by the system based on an analysis of the impact of loss. **Select** an initial set of controls for the system and tailor the controls as needed to reduce risk to an acceptable level based on an assessment of risk. **Implement** the controls and describe how the controls are employed within the system and its environment of operation.

**Assess** the controls to determine if the controls are implemented correctly, operating as intended, and producing the desired outcomes with respect to satisfying the security and privacy requirements. **Authorize** the system or common controls based on a determination that the risk to organizational operations and assets, individuals, and other organizations, and the nation is acceptable. **Monitor** the system and associated controls on an on-going basis to include assessing control effectiveness, documenting changes to the system and environment of operation, conducting risk assessments and impact analysis, and reporting the security and privacy posture of the system.

See the source author's overview article, [The NIST Risk Management Framework](https://blog.balancedsec.com/p/the-nist-risk-management-framework).

There are other risk frameworks, such as the ISO/IEC 31000, ISO/IEC 31004, COSO's ERM, ISACA's Risk IT, OCTAVE, FAIR, and TARA (transfer, avoid, reduce, and accept); be familiar with frameworks and their goals.

### AI in this objective

**Model risk.** Evaluate the harm of an incorrect answer as well as the probability of a technical compromise. Harbor's assistant might confidently invent a refund policy. Compare limited recommendations with autonomous transactions, record assumptions, and measure performance on the intended task before accepting the residual risk. [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).

### Apply this objective

**Question.** Insurance covers a breach's financial costs. Has Harbor transferred every consequence of the breach?

**Reasoning.** No. Insurance can transfer specified financial losses under its terms, but customer harm, operational disruption, reputational damage, exclusions, and organizational accountability may remain. Record and manage those residual risks.

<a id="objective-1-10"></a>

## 1.10 Understand and apply threat modeling concepts and methodologies

Threat modeling is a structured way to ask what could go wrong with a system and what to do about it. Begin with a simple representation of data flows, entry points, privileged actions, and trust boundaries. Then examine how an attacker, mistake, or failure could undermine the intended behavior.

The methods below offer different perspectives. A category-based method helps avoid overlooking classes of threat; an attack-oriented method explores an adversary's path; a business-oriented method connects technical weaknesses to consequences. The output should guide design and testing, not merely produce an attractive diagram.

**Threat Modeling**: security process where potential threats are identified, categorized, and analyzed; can be performed as a **proactive** measure during design and development (aka **defensive approach**) or as a **reactive** measure once a product has been deployed (aka **adversarial approach**).

Threat modeling identifies the potential harm, the probability of occurrence, the priority of concern, and the means to eradicate or reduce the threat.

[**MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge)**](https://attack.mitre.organization/): a comprehensive framework with a globally accessible knowledge base that documents real-world tactics, techniques, and procedures (TTPs) used by cyber adversaries; it is widely used by organizations to improve threat detection, incident response, and cybersecurity defenses; ATT&CK is used as a default model in many software packages.

Microsoft uses the **Security Development Lifecycle** (SDL) with the motto: "Secure by design, secure by default, secure in deployment and communication".

#### It has two objectives

Reduce the number of security-related design and coding defects. Reduce the severity of any remaining defects.

A defensive approach to threat modeling takes place during the early stages of development; the method is based on predicting threats and designing in specific defenses during the coding and crafting process.

Security solutions are more cost effective in this phase than later; this concept should be considered a proactive approach to threat management.

#### Microsoft developed the STRIDE threat model

Spoofing: an attack with the goal of gaining access to a target system through the use of falsified identity. Tampering: any action resulting in unauthorized changes or manipulation of data, whether in transit or in storage. Repudiation: the ability of a user or attacker to deny having performed an action or activity by maintaining plausible deniability. Information Disclosure: the revelation or distribution of private, confidential, or controlled information to external or unauthorized entities. **Denial of Service (DoS)** is an attack that attempts to prevent authorized use of a resource; this can be done through flaw exploitation, connection overloading, or traffic flooding; for example, a SYN flood is a DoS attack that disrupts the TCP three-way handshake.

Elevation of privilege: an attack where a limited user account is transformed into an account with greater privileges, powers, and access. STRIDE is threat categorization model; threat categorization is an important part of application threat modeling.

**Process for Attack Simulation and Threat Analysis (PASTA)** is a seven-stage threat modeling methodology: Stage I: Definition of the Objectives (DO) for the Analysis of Risk; Stage II: Definition of the Technical Scope (DTS); Stage III: Application Decomposition and Analysis (ADA); Stage IV: Threat Analysis (TA); Stage V: Weakness and Vulnerability Analysis (WVA); Stage VI: Attack Modeling and Simulation (AMS); Stage VII: Risk Analysis and Management (RAM).

Each stage of PASTA has a specific list of objectives to achieve and deliverables to produce in order to complete the stage. **Visual, Agile, and Simple Threat (VAST)** is a threat modeling concept that integrates threat and risk management into an Agile programming environment on a scalable basis.

Part of the job of the security team is to identify threats, using different methods:

Focus on attackers: this is a useful method in specific situations.

E.g. suppose that a developer’s employment is terminated, and that post-offboarding and review of developer’s computer, a determination is made that the person was disgruntled and angry. Understanding this situation as a possible threat, allows mitigation steps to be taken.

Focus on assets: an organization’s most valuable assets are likely to be targeted by attackers. Focus on software: organizations that develop applications in house, and can be viewed as part of the threat landscape; the goal isn’t to identify every possible attack, but to focus on the big picture, identifying risks and attack vectors.

Understanding threats to the organization allow the documentation of potential attack vectors; diagramming can be used to list various technologies under threat. **Reduction analysis**: with a purpose of gaining a greater understanding of the logic of a product and interactions with external elements includes breaking down a system into five core elements: trust boundaries, data flow paths, input points, privileged operations, and security control details; AKA decomposing the application, system, or environment.

**DREAD**: Microsoft developed the DREAD threat modeling approach to detect and prioritize threats so that serious threats can be mitigated first.

D: Damage potential; R: Reproducibility; E: Exploitability; A: Affected users; D: Discoverability.

STRIDE and DREAD are used together: STRIDE to identify the threats, DREAD to prioritize them. **Trike** is an open source risk-based threat modeling methodology; provides a method of performing a reliable and repeatable security audit, and a framework for collaboration and communication. Also see Cyber Kill Chain in Domain 7.

#### Threat intelligence feed standards include

**CAPEC (Common Attack Pattern Enumeration and Classification)** is a dictionary of known attack patterns. **STIX (Structured Threat Information eXpression language)**: used to describe threats in a standardized way. **TAXII (Trusted Automated eXchange of Indicator Information)** defines how threat information can be shared and exchanged.

### Apply this objective

**Question.** Harbor's portal trusts an incoming request to specify the customer account to read. What should a threat model investigate?

**Reasoning.** Investigate whether a user can change that identifier and read another customer's record. Document the trust boundary, the authorization decision, the potential disclosure, the proposed server-side check, and a test proving that the check works.

<a id="objective-1-11"></a>

## 1.11 Apply Supply Chain Risk Management (SCRM) concepts

A supplier can introduce risk through hardware, software, data, or a service on which the organization depends. Purchasing from a recognizable company does not reveal every component or subcontractor behind the product. Supply chain risk management follows those dependencies through selection, contracting, delivery, operation, and exit.

Ask what evidence supports the supplier's claims, what changes must be disclosed, how incidents will be handled, and how service or data can be recovered if the relationship ends. Technical provenance, contractual rights, and continuing monitoring complement one another.

<a id="subtopic-1-11-1"></a>

### 1.11.1 Risks associated with the acquisition of products and services from suppliers and providers (e.g., product tampering, counterfeits, implants)

**Supply Chain Risk Management (SCRM)** is the means to ensure that all of the vendors or links in the supply chain are:

Reliable,. Trustworthy,. Reputable organizations that disclose their practices and security requirements to their business partners (not necessarily to the public).

Each link in the chain should be responsible and accountable to the next link in the chain; each handoff is properly organized, documented, managed, and audited.

The goal of a secure supply chain is that the finished product is of sufficient quality, meets performance and operational goals, provides stated security mechanisms, and that at no point in the process was any element counterfeited or subject to unauthorized or malicious manipulation or sabotage.

The supply chain can be a threat vector, where materials, software, hardware, or data are obtained from a supposedly trusted source but the supply chain behind the source could have been compromised and asset poisoned or modified.

Supply chain attacks include things like product tampering, counterfeits, or implants; these attacks can be difficult to detect, and changes or manipulations can be made via hardware (even miniaturized chips), or via software.

Choosing trusted and reputable vendors, and doing security monitoring, management and assessments are important to lower these risks.

<a id="subtopic-1-11-2"></a>

### 1.11.2 Risk mitigations (e.g., third-party assessment and monitoring, minimum security requirements, service level requirements, silicon root of trust, physically unclonable function, software bill of materials)

Before doing business with another company, an organization needs to perform due-diligence, and third-party assessments can help gather information and perform the assessment.

An on-site assessment is useful to gain information about physical security and operations.

During document review, your goal is to thoroughly review all the architecture, designs, implementations, policies, procedures, etc. A good understanding of the current state of the environment, especially to understand any shortcomings or compliance issues prior to integrating the IT infrastructures. The level of access and depth of information obtained is usually proportional to how closely the companies will work together.

Creating security requirements that dovetail with SLAs and contracts is important, as are including things like a **silicon root of trust (RoT)** (AKA hardware root of trust) to ensure the integrity, authenticity, and confidentiality as a foundation of system startup security. **Physically unclonable function (PUF)**: physical component that creates a unique digital identifier that can create an electronic fingerprint for integrated circuits or devices. **Software Bill of Materials (SBOM)** is a detailed list of all components, libraries, and dependencies (including open-source and proprietary code) included in a software application; the purpose is to provide better software transparency, security and compliance helping teams address risks and track vulnerabilities.

### AI in this objective

**AI supplier transparency.** Ask how the provider obtains data, manages model changes, protects customer inputs, and responds to failures. An undisclosed upstream dependency can affect Harbor even when its direct supplier appears reliable. Record evidence and gaps in the same supplier review used for other critical services. [ISC2 AI guidance, Domain 1](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

### Apply this objective

**Question.** A vendor supplies a software bill of materials. Is that evidence that the product contains no exploitable vulnerabilities?

**Reasoning.** No. The inventory helps identify components and assess exposure, but it is not a security guarantee. Harbor must evaluate relevant vulnerabilities, deployment context, update practices, and the vendor's response process.

<a id="objective-1-12"></a>

## 1.12 Establish and maintain a security awareness, education, and training program

Awareness helps people recognize an issue, training builds skill in a particular task, and education develops broader understanding. A useful program selects the right approach for the audience. Developers, executives, support staff, and administrators face different decisions and therefore need different examples and practice.

Measure outcomes rather than attendance alone. Harbor can examine whether staff report suspicious requests promptly, whether developers apply required checks, and whether incidents reveal a recurring misunderstanding. Review the material when tools, threats, or business processes change.

<a id="subtopic-1-12-1"></a>

### 1.12.1 Methods and techniques to increase awareness and training (e.g., social engineering, phishing, security champions, gamification)

Before actual training takes place, user security awareness needs to take place; from there, training, or teaching employees to perform their work tasks and to comply with the security policy can begin.

All new employees require some level of training so that they will be able to comply with all standards, guidelines, and procedures mandated by the security policy. Education is a more detailed endeavor in which students/users learn much more than they actually need to know to perform their work tasks. Education is most often associated with users pursuing certification or seeking job promotion.

Employees need to understand what to be aware of (e.g. types of threats, such as phishing and free USB sticks), how to perform their jobs securely (e.g. encrypt sensitive data, physically protect valuable assets) and how security plays a role in the big picture (company reputation, profits,and losses).

Training should be mandatory and provided both to new employees and yearly (at a minimum) for ongoing training. Routine tests of operational security should be performed (such as phishing test campaigns, tailgating at company doors and social engineering tests).

**Social engineering** is a form of attack that exploits human nature and behavior; the common social engineering principles are authority, intimidation, consensus, scarcity, familiarity, trust, and urgency.

**familiarity**: as a social engineering principle, an attempt to exploit someone's native trust in things that are familiar; might include claiming to know a coworker (existing or not), and designed to put the target in a mindset that promotes willingness to provide info. Social engineering attacks include phishing, spear phishing, business email compromise (BEC), whaling, smishing, vishing, spam, shoulder surfing, invoice scams, hoaxes, impersonation, masquerading, tailgating, piggybacking, dumpster diving, identity fraud, typo squatting, and influence campaigns. While many organizations don’t perform social engineering campaigns (testing employees using benign social engineering attempts) as part of security awareness, it is likely to gain traction.

Outside of campaigns, presenting social engineering scenarios and information is a common way to educate.

Phishing: phishing campaigns are popular, and many organizations use third-party services to routinely test their employees with fake phishing emails.

Such campaigns produce valuable data, such as the percentage of employees who open the phishing email, the percentage who open attachments or click links, and the percentage who report the fake phishing email as malicious.

Security champions: the term "champion" has been gaining ground; organizations often use it to designate a person on a team who is a subject matter expert in a particular area or responsible for a specific area.

E.g. somebody on the team could be a monitoring champion — they have deep knowledge around monitoring and evangelize the benefits of monitoring to the team or other teams. A security champion is a person responsible for evangelizing security, helping bring security to areas that require attention, and helping the team enhance their skills.

Gamification: legacy training and education are typically based on reading and then answering multiple-choice questions to prove knowledge; gamification aims to make training and education more fun and engaging by packing educational material into a game.

Gamification has enabled organizations to get more out of the typical employee training.

**Security champions**: team member who acts as the liaison between their team and the security team, promoting secure development practices and helping integrate security into daily workflows.

<a id="subtopic-1-12-2"></a>

### 1.12.2 Periodic content reviews to include emerging technologies and trends (e.g., cryptocurrency, artificial intelligence (AI), blockchain)

On-going training (or teaching people how to perform their tasks and comply with policies) and education (teaching students/users more than they need to know to perform specific tasks) is important as is developing security champions.

It's also important to periodically review training material content, especially in regard to the fast pace of change of newer technologies such as AI, blockchain and even cryptocurrencies.

Emerging tech trends should be incorporated into training materials. Not only material updates, but methods should also be updated to keep content and approach relevant and from getting stale.

Threats are complex, so training needs to be relevant and interesting to be effective; this means updating training materials and changing out the ways which security is tested and measured.

If you always use the same phishing test campaign or send it from the same account on the same day, it isn’t effective, and the same applies to other materials. Instead of relying on long/detailed security documentation for training and awareness, consider using internal social media tools, videos and interactive campaigns.

<a id="subtopic-1-12-3"></a>

### 1.12.3 Program effectiveness evaluation

Time and money must be allocated for evaluating the company’s security awareness and training; the company should track key metrics, such as the percentage of employees who click on a fake phishing campaign email links.

Also see [Understanding CISSP Domain 1: Security and Risk Management](https://blog.balancedsec.com/p/understanding-cissp-domain-1-security) on the source author's blog, [The Cyber Leader](https://blog.balancedsec.com/) for additional information. Articles on risk management: [Part 1](https://blog.balancedsec.com/p/risk-concepts-from-the-cissp-part-1) introduces risk and risk terminology from the lens of the (ISC)² Official Study Guide.

Since the primary goal of risk management is to identify potential threats against an organization's assets, and bring those risks into alignment with an organization's risk appetite, in [Part 2](https://blog.balancedsec.com/p/risk-concepts-from-the-cissp-part-2), we cover the threat assessment -- a process of examining and evaluating cyber threat sources with potential system vulnerabilities.

We look at how a risk assessment helps drive our understanding of risk by pairing assets and their associated potential threats, ranking them by criticality. We also discuss quantitative analytic tools to help provide specific numbers for various potential risks, losses, and costs.

In the [Part 3](https://blog.balancedsec.com/p/risk-concepts-from-the-cissp-part-3), we review the outcome of the risk assessment process, looking at total risk, allowing us to determine our response to each risk/threat pair and perform a cost/benefit review of a particular safeguard or control.

We look at the categories and types of controls and the idea of layering them to provide several different types of protection mechanisms. We also review the important step of reporting out our risk analysis and recommended responses, noting differences in requirements for messaging by group.

### Apply this objective

**Question.** Everyone completed a phishing course, but suspicious messages are rarely reported. What should Harbor change?

**Reasoning.** Investigate whether staff can recognize the messages, know the reporting route, and feel safe using it. Practice the reporting task and measure the result. Completion records show participation, not necessarily effective behavior.

## Chapter review

Return to the Harbor examples and explain each decision without looking at the answer. Identify the asset or business activity, the relevant requirement, the possible harm, the responsible owner, and the evidence that would support the decision. If two controls appear interchangeable, explain the different failure each addresses.

### Connections and common distinctions

Governance sets direction; management executes it. Due diligence develops understanding; due care acts reasonably on it. Risk appetite, tolerance, and capacity describe different limits. Business continuity requirements in this domain guide the recovery work in Domain 7.

### Review questions and explained answers

**1. How would you explain this domain to Harbor's service owner?** Describe the decisions it governs using the examples in this chapter. A useful answer connects technical measures to customer service, accountability, and evidence rather than listing product names.

**2. Which assumption in the chapter's examples would most change your recommendation if it were false?** Choose a concrete assumption, such as data sensitivity, allowed downtime, or an identity's authority. Explain how a different assumption changes the relevant control or test. More than one answer can be sound when justified.

**3. How does adding the AI assistant change the work?** Follow the AI lessons in this chapter. Identify an additional asset, failure, or decision and describe its owner and verification method. The assistant still operates within ordinary governance, access, data, and recovery requirements.

### AI application review

**Question.** Harbor wants to approve an AI assistant on the strength of a supplier demonstration. What should the review cover?

**Reasoning.** Define the permitted task and accountable owner, assess bias and harmful errors, determine privacy obligations, and examine supplier data sourcing and change practices. Compare evidence with the proposed use and record who accepts remaining risk. A demonstration does not establish performance for Harbor's customers.

## Term index

This index points to explanations in the chapter. Terms retain the source guide's spelling where useful for recognition; corrected concepts are explained in context.

- [AAA Services](#subtopic-1-2-1)
- [Acceptable Use Policy (AUP)](#objective-1-6)
- [Act honorably, honestly, justly, responsibly, and legally](#subtopic-1-1-1)
- [Ad hoc](#subtopic-1-9-8)
- [Administrative](#objective-1-5)
- [Administrative law](#subtopic-1-4-6)
- [Advance and protect the profession](#subtopic-1-1-1)
- [adversarial approach](#objective-1-10)
- [AI ethics and bias](#objective-1-1)
- [AI privacy obligations](#objective-1-4)
- [AI supplier transparency](#objective-1-11)
- [Always prioritize people's safety](#subtopic-1-7-2)
- [Annualized loss expectancy (ALE)](#subtopic-1-9-1)
- [Annualized rate of occurrence (ARO)](#subtopic-1-9-1)
- [Approval and implementation](#subtopic-1-7-1)
- [Assess](#subtopic-1-9-9)
- [Authenticity](#subtopic-1-2-1)
- [Authorize](#subtopic-1-9-9)
- [Availability](#subtopic-1-2-1)
- [Baselines](#objective-1-6)
- [Business Continuity Planning (BCP)](#subtopic-1-7-1)
- [Business impact analysis (BIA)](#subtopic-1-7-1)
- [California Consumer Privacy Act (CCPA)](#subtopic-1-4-5)
- [Candidate screening and hiring](#subtopic-1-8-1)
- [CAPEC (Common Attack Pattern Enumeration and Classification)](#objective-1-10)
- [Categorize](#subtopic-1-9-9)
- [Children's Online Privacy Protection Act (COPPA)](#subtopic-1-4-5)
- [CIS Critical Security Controls](#subtopic-1-3-4)
- [Civil](#objective-1-5)
- [Civil law](#subtopic-1-4-6)
- [Clarifying Lawful Overseas Use of Data (CLOUD)](#subtopic-1-4-5)
- [COBIT (Control Objectives for Information and Related Technologies)](#subtopic-1-3-4)
- [Committee of Sponsoring Organizations of the Treadway Commission (COSO)](#subtopic-1-3-4)
- [Communications Assistance to Law Enforcement Act (CALEA)](#subtopic-1-4-1)
- [Compensating](#subtopic-1-9-4)
- [Compliance](#subtopic-1-4-6)
- [Compliance enforcement](#subtopic-1-8-2)
- [Computer Fraud and Abuse Act (CFAA)](#subtopic-1-4-1)
- [Conceptual Residual Risk Formula](#subtopic-1-9-3)
- [Conceptual Total Risk Formula](#subtopic-1-9-3)
- [Confidentiality](#subtopic-1-2-1)
- [continuity of operations plan (COOP)](#subtopic-1-7-1)
- [Continuity planning](#subtopic-1-7-1)
- [Controls Gap](#subtopic-1-9-3)
- [Copyright](#subtopic-1-4-2)
- [Corrective](#subtopic-1-9-4)
- [Council of Europe Convention on Cybercrime](#subtopic-1-4-1)
- [Countermeasure](#subtopic-1-9-3)
- [Criminal](#objective-1-5)
- [Criminal law](#subtopic-1-4-6)
- [Cybersecurity Framework](#subtopic-1-9-9)
- [defensive approach](#objective-1-10)
- [Defined](#subtopic-1-9-8)
- [Denial of Service (DoS)](#objective-1-10)
- [Design](#subtopic-1-4-2)
- [Detective](#subtopic-1-9-4)
- [Deterrent](#subtopic-1-9-4)
- [Digital Millennium Copyright Act (DMCA)](#subtopic-1-4-6)
- [Directive](#subtopic-1-9-4)
- [DREAD](#objective-1-10)
- [Due care](#subtopic-1-3-5)
- [Due diligence](#subtopic-1-3-5)
- [Electronic Communication Privacy Act (ECPA)](#subtopic-1-4-5)
- [Electronic Communications Privacy Act (ECPA)](#subtopic-1-4-6)
- [Electronic Espionage Act of 1996](#subtopic-1-4-5)
- [Employment agreement](#subtopic-1-8-2)
- [Enterprise Risk Management](#subtopic-1-9-8)
- [Exposure](#subtopic-1-9-1)
- [Exposure Factor (EF)](#subtopic-1-9-1)
- [familiarity](#subtopic-1-12-1)
- [Family Education Rights and Privacy Act (FERPA)](#subtopic-1-4-5)
- [Federal Information Security Management Act (FISMA)](#subtopic-1-4-6)
- [Federal Risk and Authorization Management Program (FedRAMP)](#subtopic-1-3-4)
- [Fourth Amendment to the US Constitution](#subtopic-1-4-5)
- [General Data Protection Regulation (GDPR)](#subtopic-1-4-5)
- [Glass-Steagall Act](#subtopic-1-4-1)
- [Governing the assistant](#objective-1-3)
- [Gramm-Leach-Bliley Act (GLBA)](#subtopic-1-4-6)
- [Guidelines](#objective-1-6)
- [Health Information Technology for Economic and Clinical Health (HITECH)](#subtopic-1-4-1)
- [Health Insurance Portability and Accountability Act (HIPAA)](#subtopic-1-4-6)
- [Implement](#subtopic-1-9-9)
- [Industry Standards](#objective-1-5)
- [Information Technology Infrastructure Library (ITIL)](#subtopic-1-3-4)
- [Inherent Risk](#subtopic-1-9-3)
- [Integrated](#subtopic-1-9-8)
- [Integrity](#subtopic-1-2-1)
- [Intellectual property](#subtopic-1-4-2)
- [International Organization for Standardization (ISO)](#subtopic-1-3-4)
- [International Traffic in Arms Regulations (ITAR)](#subtopic-1-4-3)
- [ISO 27000:2018](#subtopic-1-3-4)
- [ISO 27001:2022](#subtopic-1-3-4)
- [ISO 27002:2022](#subtopic-1-3-4)
- [ISO 27017:2015](#subtopic-1-3-4)
- [ISO 27018:2019](#subtopic-1-3-4)
- [ISO/IEC 27001](#subtopic-1-3-4)
- [Licensing](#subtopic-1-4-2)
- [maximum tolerable downtime (MTD) or maximum allowable downtime (MAD)](#subtopic-1-7-1)
- [Missions](#subtopic-1-3-1)
- [MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge)](#objective-1-10)
- [Model risk](#objective-1-9)
- [Monitor](#subtopic-1-9-9)
- [MTBF](#subtopic-1-7-1)
- [MTTR](#subtopic-1-7-1)
- [National Information Infrastructure Protection Act](#subtopic-1-4-1)
- [NIST Cybersecurity Framework (CSF)](#subtopic-1-3-4)
- [Nonrepudiation](#subtopic-1-2-1)
- [Objectives](#subtopic-1-3-1)
- [Onboarding](#subtopic-1-8-3)
- [Operational Plan](#subtopic-1-3-1)
- [Optimized](#subtopic-1-9-8)
- [Organization for Economic Co-operation and Development (OECD)](#subtopic-1-4-5)
- [Patents](#subtopic-1-4-2)
- [Payment Card Industry Data Security Standard (PCI DSS)](#subtopic-1-4-6)
- [Payment Card Industry Data Security Standard PCI DSS](#subtopic-1-3-4)
- [Personal Information Protection and Electronic Documents Act (PIPEDA)](#subtopic-1-4-5)
- [Personal Information Protection Law (PIPL)](#subtopic-1-4-5)
- [Physical](#subtopic-1-9-4)
- [Physically unclonable function (PUF)](#subtopic-1-11-2)
- [Policies](#objective-1-6)
- [Policy](#objective-1-6)
- [Preliminary](#subtopic-1-9-8)
- [Prepare](#subtopic-1-9-9)
- [Preventive](#subtopic-1-9-4)
- [Privacy Act of 1974](#subtopic-1-4-5)
- [Privacy Shield](#subtopic-1-4-5)
- [proactive](#objective-1-10)
- [Procedures](#objective-1-6)
- [Process for Attack Simulation and Threat Analysis (PASTA)](#objective-1-10)
- [Project scope and planning](#subtopic-1-7-1)
- [Protection of Personal Information Act (POPIA)](#subtopic-1-4-5)
- [Provide diligent and competent service to principals](#subtopic-1-1-1)
- [Provisions and processes](#subtopic-1-7-1)
- [Qualitative Risk Analysis](#subtopic-1-9-2)
- [Quantitative Risk Analysis](#subtopic-1-9-2)
- [reactive](#objective-1-10)
- [Recovery](#subtopic-1-9-4)
- [recovery point objectives (RPO)](#subtopic-1-7-1)
- [recovery time objectives (RTO)](#subtopic-1-7-1)
- [Reduction analysis](#objective-1-10)
- [Regulatory](#objective-1-5)
- [Residual Risk](#subtopic-1-9-3)
- [Risk](#subtopic-1-9-1)
- [Risk Acceptance](#subtopic-1-9-3)
- [risk appetite](#subtopic-1-9-1)
- [Risk appetite](#subtopic-1-9-1)
- [Risk Assessment](#subtopic-1-9-2)
- [Risk Assignment](#subtopic-1-9-3)
- [Risk Avoidance](#subtopic-1-9-3)
- [risk capacity](#subtopic-1-9-1)
- [Risk capacity](#subtopic-1-9-1)
- [Risk Deterrence](#subtopic-1-9-3)
- [Risk Management](#subtopic-1-9-1)
- [Risk Management Framework](#subtopic-1-9-9)
- [Risk Maturity Model (RMM)](#subtopic-1-9-8)
- [Risk Mitigation](#subtopic-1-9-3)
- [Risk Rejection](#subtopic-1-9-3)
- [Risk response](#subtopic-1-9-3)
- [risk tolerance](#subtopic-1-9-1)
- [Risk tolerance](#subtopic-1-9-1)
- [Risk Transference](#subtopic-1-9-3)
- [RMF has 7 steps](#subtopic-1-9-9)
- [Safeguard evaluation](#subtopic-1-9-1)
- [Sarbanes-Oxley (SOX)](#subtopic-1-4-6)
- [Security champions](#subtopic-1-12-1)
- [Security Control Assessment (SCA)](#subtopic-1-9-5)
- [security control framework](#subtopic-1-3-4)
- [Security Development Lifecycle](#objective-1-10)
- [Security governance](#objective-1-3)
- [Security Management Planning](#subtopic-1-3-1)
- [Select](#subtopic-1-9-9)
- [Sherwood Applied Business Security Architecture (SABSA)](#subtopic-1-3-4)
- [silicon root of trust (RoT)](#subtopic-1-11-2)
- [Single Loss Expectancy (SLE)](#subtopic-1-9-1)
- [six cyclical phases](#subtopic-1-9-9)
- [Social engineering](#subtopic-1-12-1)
- [Software Bill of Materials (SBOM)](#subtopic-1-11-2)
- [SP 800-100](#subtopic-1-3-4)
- [SP 800-53](#subtopic-1-3-4)
- [Standards](#objective-1-6)
- [STIX (Structured Threat Information eXpression language)](#objective-1-10)
- [Strategic Plan](#subtopic-1-3-1)
- [Strategy development](#subtopic-1-7-1)
- [STRIDE threat model](#objective-1-10)
- [Supply Chain Risk Management (SCRM)](#subtopic-1-11-1)
- [Tactical Plan](#subtopic-1-3-1)
- [TAXII (Trusted Automated eXchange of Indicator Information)](#objective-1-10)
- [Technical / Logical](#subtopic-1-9-4)
- [Termination or offboarding](#subtopic-1-8-3)
- [The security function](#objective-1-3)
- [Third-party governance](#objective-1-3)
- [Threat](#subtopic-1-9-1)
- [Threat Agent/Actor](#subtopic-1-9-1)
- [Threat Event](#subtopic-1-9-1)
- [Threat Modeling](#objective-1-10)
- [Threat Vector](#subtopic-1-9-1)
- [Total Risk](#subtopic-1-9-3)
- [Trade Secrets](#subtopic-1-4-2)
- [Trademarks](#subtopic-1-4-2)
- [Transfer](#subtopic-1-8-3)
- [Trike](#objective-1-10)
- [US Patriot Act of 2001](#subtopic-1-4-5)
- [Utility](#subtopic-1-4-2)
- [Visual, Agile, and Simple Threat (VAST)](#objective-1-10)
- [Vulnerability](#subtopic-1-9-1)
- [Wassenaar Arrangement](#subtopic-1-4-4)

## Sources and further reading

- [Original Domain 1 objectives and notes](../CISSP-Domain-1-2024+Objectives.md) by the repository's contributors; adapted under the repository license.
- [ISC2 CISSP exam outline and AI domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).
- [ISC2 AI guidance announcement](https://www.isc2.org/Insights/2026/04/ISC2-Publishes-Exam-Guidance-AI).
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

Additional references appear alongside the relevant concepts. Official Study Guide chapter references in the original objective files remain available for comparison.
