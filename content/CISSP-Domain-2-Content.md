<a id="domain-2"></a>

# Domain 2: Asset Security

Exam weight: 10%. Study edition: September 2026.

## Start here

Asset security follows information from collection through disposal. You will learn to identify value, assign ownership, classify information, establish handling rules, and choose protections for its lifecycle. Start with what the information means to the organization before considering the device on which it happens to be stored.

This chapter follows the published Domain 2 objectives. Read the opening explanation of each objective first, then the detailed lessons, and finish with its application check. Three-part numbers identify subtopics retained from the source guide. The examples use Harbor Services, a small organization launching a customer portal and an AI support assistant.

Artificial intelligence (AI) is the broad field of systems performing tasks associated with intelligence. Machine learning (ML) builds models from examples during training; inference uses a trained model to produce an output. A large language model (LLM) produces language using learned numerical parameters called model weights. These terms identify components and processes to protect, rather than establish that a system is correct or trustworthy.

The AI additions apply [ISC2's domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline) to existing objectives. Detailed placement and Harbor scenarios are editorial teaching choices. Named historical technologies remain useful for comparison; their inclusion is not a recommendation to deploy them.

## Chapter navigation

- [2.1 Identify and classify information and assets](#objective-2-1)
- [2.2 Establish information and asset handling requirements](#objective-2-2)
- [2.3 Provision information and assets securely](#objective-2-3)
- [2.4 Manage data lifecycle](#objective-2-4)
- [2.5 Ensure appropriate asset retention (e.g. End-of-Life (EOL), End-of-Support)](#objective-2-5)
- [2.6 Determine data security controls and compliance requirements](#objective-2-6)

<a id="objective-2-1"></a>

## 2.1 Identify and classify information and assets

You cannot protect information appropriately until you know what it is and why it matters. An asset can be data, a device, software, a contractual right, or something less tangible such as reputation. Classification assigns protection requirements based on sensitivity, criticality, and obligations rather than treating every asset identically.

At Harbor, a public help article and a customer identity document may occupy the same storage service but need different access rules. The owner evaluates the consequences of disclosure, alteration, and unavailability, then assigns a classification that the organization can translate into handling rules.

<a id="subtopic-2-1-1"></a>

### 2.1.1 Data classification

Asset security includes the concepts, principles, and standards of monitoring and securing any asset important to the organization. Domain 2 of the CISSP exam covers asset security making up ~10% of the test. Managing the data lifecycle refers to protecting it from cradle to grave -- steps need to be taken to protect data when it's first created until it's destroyed. One of the first steps in the lifecycle is identifying and classifying information and assets, often within a security policy. In this context, assets include sensitive data, the hardware used to process that data, and the media used to store/hold it.

**Data categorization** is a process of grouping sets of data, information or knowledge that have comparable sensitivities (e.g. impact or loss rating), and have similar law/contract/compliance security needs; the act of assigning a classification level to an asset. **Sensitive data** requires protection because of harm that could result from disclosure, alteration, loss, or misuse, or because of applicable obligations. Unclassified information can still be sensitive.

**Personally Identifiable Information (PII)** is any information that can identify an individual.

More specifically, information about an individual including (1) any information that can be used to distinguish or trace an individual‘s identity, such as name, social security number, date and place of birth, mother‘s maiden name, or biometric records; and (2) any other information that is linked or linkable to an individual, such as medical, educational, financial, and employment information ([NIST SP 800-122](https://csrc.nist.gov/publications/detail/sp/800-122/final)).

**Protected Health Information (PHI)** is individually identifiable health information within HIPAA's scope. HIPAA applies to covered entities and relevant business associates, not every organization holding health-related data. [HHS](https://www.hhs.gov/hipaa/for-professionals/covered-entities/index.html). **Proprietary data** is any data that helps an organization maintain a competitive edge.

#### Organizations classify data using labels

#### Government classification labels include

**Top Secret** applies to information whose unauthorized disclosure could reasonably cause exceptionally grave damage to US national security. [National Archives](https://www.archives.gov/isoo/faqs/e-o-13526-and-32-cfr-part-2001). **Confidential**: applied to information that if disclosed would likely cause damage to the national security. **Secret** applies to information whose unauthorized disclosure could reasonably cause serious damage to US national security. [National Archives](https://www.archives.gov/isoo/faqs/e-o-13526-and-32-cfr-part-2001). **Unclassified** means not classified national security information; it can still be sensitive or subject to handling requirements, such as Controlled Unclassified Information (CUI).

#### Non-government organizations use labels such as

**Confidential/Proprietary**: only used within the organization and, in the case of unauthorized disclosure, it could suffer serious consequences. **Private**: may include personal information, such as credit card data and bank accounts; unauthorized disclosure can be disastrous. **Sensitive**: needs extraordinary precautions to ensure confidentiality and integrity. **Public** can be viewed by the general public and, therefore, the disclosure of this data would not cause damage.

Labels can be as granular and custom as required by the organization.

It is important to protect data in all states: at rest, in transit, or in use. Protect confidentiality with appropriate access control, encryption, key management, and handling practices. The suitable combination depends on the threat and data use.

<a id="subtopic-2-1-2"></a>

### 2.1.2 Asset classification

**Asset**: anything of value owned by the organization. It's important to identify and classify assets, such as systems, mobile devices etc. Owners are accountable for an asset and protecting its value.

**Asset Classification**: assigning assets the level of protection required based on their value to the organization; assets require an identified owner to be classified and protected adequately.

Derived from compliance mandates, the process of recognizing organizational impacts if information suffers any security compromise (whether to confidentiality, integrity, availability, non-repudiation, authenticity, privacy, or safety).

Asset classifications should match data classification, i.e. if a computer is processing top secret data, the computer should be classified as a top secret asset. **Clearance**: relates to access of certain classification of data or equipment, and who has access to that level or classification.

A **formal access approval process** should be used to change user access; the process should involve approval from the data/asset owner, and the user should be informed about rules and limits.

Before a user is granted access they should be educated on working with that level of classification.

Classification levels can be used by businesses during acquisitions, ensuring only personnel who need to know are involved in the assessment or transition. In general, classification labels help users use data and assets properly, for instance by restricting dissemination or use of assets by their classification. Asset classification should include confidentiality (sensitivity), integrity (accuracy), and availability (criticality).

### AI in this objective

**AI assets.** Classify training datasets, pretrained models, and model weights. A model's weights are learned numerical parameters, and the resulting model may be valuable intellectual property. Its classification should reflect its value and the information it may expose. [ISC2 AI guidance, Domain 2](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

### Apply this objective

**Question.** A public price list is not confidential. Does that mean it needs no protection?

**Reasoning.** No. Customers must still receive accurate prices, and the list may need to remain available. Public classification removes a confidentiality restriction; it does not eliminate integrity and availability requirements.

<a id="objective-2-2"></a>

## 2.2 Establish information and asset handling requirements

Handling requirements turn a classification into everyday actions. They describe how to label, store, copy, transmit, share, and dispose of an asset. A label helps a person or system recognize the requirement, but the controls and procedures must enforce it.

Follow one Harbor customer record through a support session. Ask who may read it, whether it can be exported, how an export is protected, and what happens to temporary copies. Information does not lose its sensitivity when it moves into an email, printout, or spreadsheet.

**Asset handling**: procedures that mitigate risks associated with who and how assets are moved, stored, and retrieved ensuring proper tools and technologies used; handling requirements are based on the classification of the asset (not the media type); handling can refer to secure transport of media through its lifetime.

The data and asset handling key goal is to prevent data breaches, by using:

**Data Maintenance**: on-going efforts to organize and care for data through its life cycle. **Data collection limitations**: only store data that has a clear business purpose. DLP: see section 2.6.4 below.

**Labeling** is the association of security attributes with subjects and objects represented by internal data structures; *labels are system-readable* and enable system-based enforcement of security policies; labeling often uses things like: metadata, barcodes, QR codes, RFID or GPS tags. **Marking**: association of security attributes in a *human-readable form*, enabling process-based enforcement of security policies; sensitive information/assets ensures proper handling (both physically and electronically). **Data Collection Limitation**: prevent loss by not collecting unnecessary sensitive data; a best practice when collecting customer data, for instance, is to limit the amount of data collected to only what is needed.

**Data Location**: keep duplicate copies of backups, on- and off-site. **Storage**: data storage and associated media are based on the classification of the data; define storage locations and procedures by storage type; use physical locks for paper-based media, and encrypt electronic data. Data destruction: see 2.4.7 below.

### Apply this objective

**Question.** A confidential database export is copied onto a removable drive. Which classification governs its handling?

**Reasoning.** The information's classification still governs. The medium introduces additional risks and determines suitable controls, but copying the information does not make it less sensitive.

<a id="objective-2-3"></a>

## 2.3 Provision information and assets securely

Provisioning makes an asset available for approved use. Before deployment, establish an owner, record the asset in an inventory, and configure its protection. Ownership means accountability for decisions; custody and administration are day-to-day responsibilities that can be delegated.

An inventory is useful when it supports action. Harbor needs to know which team owns a server, what information it processes, where it is deployed, and how it is maintained. Tracking software and other intangible assets is also necessary for license compliance, dependency management, and retirement planning.

The primary purpose of security operations practices is to safeguard assets such as information, systems, devices, facilities, and applications; these practices help to identify threats, vulnerabilities, and implement controls to reduce the risk to these assets. Implementing common security operations concepts, along with performing periodic security audits and reviews demonstrates a level of due care. **Need-to-know** is a principle that imposes the requirement to grant users access only to data or resources they need to perform assigned work tasks; another way of saying this is that need to know means that someone is only given access to an asset if there is an absolute need based on role, function, or specific authorization.

**Least privilege** is a principle stating that subjects are granted only the privileges necessary to perform assigned work tasks and no more; a person is given only absolutely needed access, and nothing more.

<a id="subtopic-2-3-1"></a>

### 2.3.1 Information and asset ownership

**Information and Asset owner**: assigning ownership is a key requirement for protection accountability; the owner is the person or role who has ultimate organizational accountability for protection of the asset; usually a Sr. Manager (CEO,president, dept. head); owners typically delegate data protection tasks to others in the organization; the asset owner needs to make sure that appropriate security controls are in place.

<a id="subtopic-2-3-2"></a>

### 2.3.2 Asset inventory (e.g., tangible, intangible)

**Inventory**: complete list of items. **Tangible assets**: include hardware, devices, physical documents etc, owned by the company.

**Intangible assets**: things like software, patents, copyrights, a company’s reputation, etc.

An organization should keep track of intangible assets, like intellectual property, patents, trademarks, the company’s reputation, and copyrights to protect them. US utility patents generally have a term measured from filing, commonly 20 years; design patents use different rules. Determine the patent type and applicable dates. [USPTO](https://www.uspto.gov/patents/basics).

<a id="subtopic-2-3-3"></a>

### 2.3.3 Asset management

Asset management refers to managing both tangible and intangible assets; this starts with asset inventory, and includes tracking the assets, and taking additional steps to protect them throughout their lifetime. The primary goal of asset management is to prevent losses (by tracking and protecting assets).

**Hardware assets**: IT resources such as computers, servers, routers, switches, and peripherals.

Use an automated configuration management system (CMS) to help with hardware asset management. Use barcodes, RFID tags to track hardware assets.

#### Software assets: operating systems and applications

Important to monitor license compliance to avoid legal issues. Software licensing also refers to ensuring that systems do not have unauthorized software installed.

To protect intangible inventories (like intellectual property, patents, trademarks, and company’s reputation, and copyrights), they need to be tracked.

### Apply this objective

**Question.** A cloud database exists but nobody accepts ownership. What should happen before production use?

**Reasoning.** Assign accountable ownership and document the database's purpose, information, access rules, and maintenance responsibilities. A technically working service is not securely provisioned if its protection decisions have no owner.

<a id="objective-2-4"></a>

## 2.4 Manage data lifecycle

The data lifecycle begins when information is collected or created and ends when its authorized retention period and disposal process are complete. Copies, backups, archives, derived datasets, and exports belong in that lifecycle too. The easiest data to protect is information that was never unnecessarily collected.

Roles answer different questions. The controller determines purposes and means of personal-data processing; a processor acts on the controller's behalf. A data owner makes organizational decisions about the information, and a custodian carries out protection tasks. These roles can overlap in practice, but their responsibilities should be explicit.

Data Lifecycle: the comprehensive process that data undergoes, from its creation to its eventual disposal; as a reference, take a look at this version of the data lifecycle from [the CSA](https://cloudsecurityalliance.organization/artifacts/cybersecurity-and-the-data-lifecycle) as a baseline.

#### Here is a slightly modified version

Creation: generate or alter data. Classify & Store: ensure the data is classified and stored according to classification, and with appropriate data at rest security controls. Use: data is protected during transmission/motion, and against improper exfiltration or sharing during use. Archived: data is placed in long-term storage with appropriate data-at-rest protection. Destroyed: data is permanently destroyed based on its classification, using the method (see above) required to ensure it can't be recovered.

<a id="subtopic-2-4-1"></a>

### 2.4.1 Data roles (i.e., owners, controllers, custodians, processors, users/subjects)

The Asset Security domain focuses on collecting, handling, and protecting information throughout its lifecycle; the first step is classifying information based on its value to the organization.

**System owner** controls the computer storing the data; usually includes software and hardware configurations and support services (e.g. cloud implementation).

System owners are responsible for the systems that process the data. System owner is responsible for system operation and maintenance, and associated updating/patching as well as related procurement activities.

Per [NIST SP 800-18](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-18r1.pdf), information **system owner** has the following responsibilities:

Responsible for the security of the system that stores or processes the data. Develops the system security plan. Maintains the system security plan and ensures that the system is deployed/operated according to security requirements. Ensures that system users and support personnel receive the requisite security training. Updates the system security plan as required. Assists in the identification, implementation, and assessment of the common security controls.

**Data owner** is the person responsible for classifying, categorizing, and permitting access to the data; the data owner is the person who is best familiar with the importance of the data to the business; typically the CEO, president, or department head.

**Data controller**: decides what data to process and how to process it.

The data controller is the person or entity that controls the processing of the data - deciding what data to process, why this data should be processed, and how it is processed. E.g. a company that collects personal information on employees for payroll is a data controller (but, if they pass this information to a third-party to process payroll, the payroll company is the data processor, see below).

**Data processor** means an entity processing personal data on a controller's behalf, with duties to protect it and follow authorized purposes. In privacy law, a computer used to process data is not itself necessarily the legal processor. [GDPR Article 4](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

Processing data on behalf of the Data Controller while ensuring quality, validation, and compliance, safe custody, transport, storage of the data and implementation of business rules. A controller can hire a third party to process data, and in this context, the third party is the data processor; data processors are often third-party entities that process data for an organization at the direction of the data controller.

Note GDPR definition: "a natural or legal person, public authority, agency, or other body, which processes personal data solely on behalf of the data controller".

GDPR also restricts data transfers to countries outside EU, with fines for violations. Many organizations have created dedicated roles to oversee GDPR data laws are followed.

**Data Protection Officer (DPO)** is an independent security leadership role responsible for overseeing an organization's data privacy strategy and ensuring compliance with legal requirements, such as the GDPR. **Data custodian** is a custodian is delegated, from the system owner, day-to-day responsibilities for properly storing and protecting data; responsible for the protection of data through maintenance activities, backing up and archiving, and preventing the loss or corruption and recovering data. **Data steward** is a data steward has business responsibility for data (e.g. data quality, governance, compliance, metadata definition etc).

**Security administrator**: responsible for ensuring the overall security of entire infrastructure; they perform tasks that lead to the discovery of vulnerabilities, monitor network traffic and configure tools to protect the network (like firewalls and antivirus software).

Security admins also devise security policies, plans for business continuity and disaster recovery and train staff.

**Supervisors**: responsible for overseeing the activities of all the above entities and all support personnel; they ensure team activities are conducted smoothly and that personnel is properly skilled for the tasks assigned.

**Users** is any person who accesses data from a computer device or system to accomplish work (think of users as employees or end users).

Users should have access to the data they need to perform tasks; users should have access to data according to their roles and their need to access info. Must comply with rules, mandatory policies, standards and procedures.

Users fall into the category of subjects, and a subject is any entity that accesses an object such as a file or folder.

Subjects can be users, programs, processes, services, computers, or anything else that can access a resource.

<a id="subtopic-2-4-2"></a>

### 2.4.2 Data Collection

One of the easiest ways of preventing the loss of data is to simply not collect it. The **data collection guideline**: if the data doesn't have a clear purpose for use, don't collect it, and don't store it; this is why many privacy regulations mention limiting data collection.

<a id="subtopic-2-4-3"></a>

### 2.4.3 Data location

**Data location**: in this context, refers to the location of data backups or data copies. If a company's system is on-prem, keeps data on-site, but regularly backs up data, best practice is to keep a backup copy on-site and off-site. Consider distance between data/storage locations to mitigate potential mutual (primary and backup) damage risk.

<a id="subtopic-2-4-4"></a>

### 2.4.4 Data maintenance

**Data maintenance**: managing data through the data lifecycle (see above); data maintenance is the process (often automated) of making sure the data is available (or not available) based on where it is in the lifecycle. Ensuring appropriate asset protection requires that sensitive data be preserved for a period of not less than what is business-required, but for no longer than necessary. Encrypt sensitive data. Safeguard assets via basic security controls to enforce appropriate levels of confidentiality, integrity and availability and act per security policies, standards, procedures and guidelines.

<a id="subtopic-2-4-5"></a>

### 2.4.5 Data retention

Retention requirements apply to data or records, media holding sensitive data, systems that process sensitive data, and personnel who have access to sensitive data.

**record retention**: retaining and maintaining information as long as it is needed, and destroying it when it's no longer needed.

A current trend in many organizations is to reduce legal liabilities by implementing short retention policies with email.

#### Three fundamental retention policy questions

**how to retain**: data should be kept in a manner that makes it accessible whenever required; take taxonomy (or the scheme for data classification) into account. **How long to retain data** depends on record type, legal and contractual duties, business need, and applicable holds. Seven years is an example for some records, not a universal retention period. **what data**: retain per organization requirements.

<a id="subtopic-2-4-6"></a>

### 2.4.6 Data remanence

**TEMPEST** is a classification of technology designed to minimize the electromagnetic emanations generated by computing devices; TEMPEST technology makes it difficult, if not impossible, to compromise confidentiality by capturing emanated information; TEMPEST countermeasures to Van Eck phreaking (i.e. eavesdropping), include Faraday cages, white noise, control zones, and shielding. **ROM**: nonvolatile memory that can't be written to by end users. **RAM**: Random Access Memory - volatile memory that loses contents when the computer is powered off. **PROM**: programmable read-only memory, a form of digital memory where the contents can be changed once after manufacture of the device.

**EEPROM**: Electrically Erasable Programmable Read-Only Memory; chips may be erased with electrical current. **EPROM / UVEPROM**: erasable programmable read-only memory, is a type of programmable read-only memory (PROM) chip that retains its data when its power supply is switched off; chips may be erased with ultraviolet light. **Asset lifecycle**: phases an asset goes through, from creation (or collection) to destruction.

**Data remanence** is the data remaining on media after the data is supposedly erased.

Typically refers to data on a hard drive as residual magnetic flux or **slack space** (unused space within a disk cluster).

Many OSs store files in **clusters**, which are groups of **sectors** (the smallest storage unit on a hard disk drive).

If media includes any type of private and sensitive data, it is important to eliminate data remanence. Some OSs fill slack space with data from memory, which is why personnel should never process classified data on unclassified systems.

<a id="subtopic-2-4-7"></a>

### 2.4.7 Data destruction

**Destruction**: retention and destruction of data should be based on data classification and archiving policies; destroy data no longer needed by the organization; policy should define acceptable destruction methods by type and classification ([see NIST SP-800-88 for details](https://csrc.nist.gov/pubs/sp/800/88/r2/final)). **Erasing**: usually refers to a delete operation on media, leaving data remanence. **Clearing**: removal of sensitive data from a storage device such that there is assurance data may not be reconstructed using *normal functions* of software recovery or software recovery utilities; over-writing existing data with a pattern; note that with this method, there's a chance that the data could be brought back by using advanced techniques.

**Purging**: removal of sensitive data from a system or device with *the intent* that data cannot be reconstructed by any known technique; purging aims to make data unrecoverable even with laboratory techniques, while clearing only protects against standard software recovery.

Select clearing, purging, or destruction using the media, sensitivity, reuse plan, and applicable authority. Classified information may require separate approved procedures. [NIST sanitization guidance](https://csrc.nist.gov/pubs/sp/800/88/r2/final).

**Destruction** physically renders media unusable through a suitable method such as shredding, pulverizing, disintegration, or incineration. Cryptographic erase is a distinct sanitization technique, not physical destruction. [NIST](https://csrc.nist.gov/pubs/sp/800/88/r2/final).

**Data Remanence**: data remaining on media after typical erasure; to ensure all remanence is removed, the following tools can help:

**Degaussing**: used on magnetic media, removes data from tapes and magnetic hard drives; no effect on optical media or SSDs. **Cryptographic Erasure**, also called **crypto shredding**, destroys the keys needed to recover encrypted data. Its effectiveness depends on adequate encryption, complete key sanitization, and control of all recoverable copies; it is not automatically the best method in every cloud environment. [NIST](https://csrc.nist.gov/pubs/sp/800/88/r2/final).

**File carving** reconstructs files from recognizable content and structure when file-system metadata is missing or damaged. It can recover some deleted or formatted content; it does not by itself decrypt strongly encrypted information.

#### Destroy sensitive data when it is no longer needed

An organization's security or data policy should define the acceptable methods of destroying data based on the data's classification. **Defensible destruction**: eliminating data using a controlled, legally defensible and regulatory-compliant way.

### AI in this objective

**Training-data integrity.** Poisoning changes training material or its handling to influence learned behavior. Harbor should record dataset provenance, control changes, and retain a trustworthy version for investigation. Follow derived datasets and model artifacts through the lifecycle as well as the original conversations. [NIST adversarial ML taxonomy](https://csrc.nist.gov/News/2025/nist-ai-100-2-adversarial-machine-learning-taxonom).

### Apply this objective

**Question.** Harbor deletes a record from the live database, but it remains in backups. Has the disposal process finished?

**Reasoning.** Not necessarily. The retention and disposal plan must account for recoverable copies, legal holds, backup expiration, and restoration behavior. Document how the information will leave each location without compromising required recovery capability.

<a id="objective-2-5"></a>

## 2.5 Ensure appropriate asset retention (e.g. End-of-Life (EOL), End-of-Support)

Retention has a purpose and a limit. Business, legal, and contractual requirements may require keeping information, while privacy and risk considerations discourage keeping it indefinitely. A legal hold can suspend routine disposal for relevant material.

End of life and end of support concern the asset's usable or maintainable lifetime. Keeping a readable archive may require migration to supported software or media. Harbor must therefore plan both how long information is needed and whether the systems needed to read and protect it will remain dependable.

Hardware: even if you maintain data for the appropriate retention period, it won’t do you any good if you don’t have hardware that can read the data. Personnel: beyond retaining data for required time periods and maintaining hardware to read the data, you need personnel who know how to operate the hardware to execute restoration processes. **End-Of-Life (EOL)**: often identified by vendors as the time when they stop offering a product for sale. **End-Of-Support (EOS)/End-Of-Service-Life (EOSL)**: often used to identify when support ends for a product.

EOL, EOS/EOSL can apply to either software or hardware.

### Apply this objective

**Question.** Records must be retained for seven years, but the archive software loses support next year. Should Harbor simply keep the unsupported server running?

**Reasoning.** Plan a controlled migration or another justified protection strategy. Verify that records remain complete, readable, accessible to authorized users, and subject to the retention schedule. Retention does not remove the need for supported protection.

<a id="objective-2-6"></a>

## 2.6 Determine data security controls and compliance requirements

Choose controls for the information's state and the way it is used. At-rest protection concerns stored data, in-transit protection concerns communication, and in-use protection concerns active processing. Encryption is valuable, but an application that is allowed to decrypt data can still disclose it through excessive permissions or unsafe behavior.

Scoping identifies the systems and data covered by a requirement; tailoring adapts applicable controls to the environment with justified decisions. Tools such as data loss prevention, digital rights management, and cloud access security brokers enforce different parts of the handling rules. Their usefulness depends on deployment and visibility.

You need security controls that protect data in each possible state: at rest, in transit or in use.

Each state requires a different approach to security; note that there aren’t as many security options for data in use as there are for data at rest or data in transit.

Keeping the systems patched, maintaining a standard computer build process, and running anti-virus/malware are typically the real-world primary protections for data in use.

<a id="subtopic-2-6-1"></a>

### 2.6.1 Data states (e.g., in use, in transit, at rest)

#### The three data states are at rest, in transit, and in use

**Data at rest** is any data stored on media such as hard drives or external media.

**Data in transit**: AKA data in motion; any data transmitted over a network.

Encryption methods protect data at rest and in transit.

#### Data in use: data in memory and used by an application

Applications should flush memory buffers to remove data after it is no longer needed.

<a id="subtopic-2-6-2"></a>

### 2.6.2 Scoping and tailoring

**Baseline**: documented, lowest level of security config allowed by a standard or organization. After selecting a control baseline, organizations fine-tune with tailoring and scoping processes; a big part of the tailoring process is aligning controls with an organization's specific security requirements.

**Tailoring** refers to modifying the list of security controls within a baseline to align with the organization's mission.

#### Includes the following activities

Identifying and designating common controls; specification of organization-defined parameters in the security controls via explicit assignment and selection statements. Applying scoping guidance/considerations. Selecting/specifying compensating controls. Assigning control values.

**Scoping**: setting the boundaries of security control implementation; limiting the general baseline recommendations by removing those that do not apply; part of the tailoring process and refers to reviewing a list of baseline security controls and selecting only those controls that apply to the systems you're trying to protect.

Scoping processes eliminate controls that are recommended in a baseline.

<a id="subtopic-2-6-3"></a>

### 2.6.3 Standards selection

Organizations need to identify the standards (e.g. PCI DSS, GDPR etc) that apply and ensure that the security controls they select fully comply with these standards. Even if the organization doesn't have to comply with a specific standard, using a well-designed community standard can be helpful (e.g. NIST SP 800 documents).

**Standards selection** is the process by which organizations plan, choose and document technologies or architectures for implementation.

E.g. you evaluate three vendors for a security control; you could use a standards selection process to help determine which solution best fits the organization.

Vendor selection is closely related to standards selection but focuses on the vendors, not the technologies or solutions.

The overall goal is to have an objective and measurable selection process.

If you repeat the process with a totally different team, the alternate team should come up with the same selection.

<a id="subtopic-2-6-4"></a>

### 2.6.4 Data protection methods (e.g., Digital Rights Management (DRM), Data Loss Prevention (DLP), Cloud Access Security Broker (CASB))

**Randomized masking** replaces values with randomized substitutes. Whether the result is anonymous depends on remaining information and re-identification risk; masking alone is not a guarantee. **Anonymization** aims to make individuals no longer identifiable, considering available means of re-identification. Replacing names with inaccurate values does not by itself achieve anonymization. [GDPR Recital 26](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

#### Data protection methods include

**digital rights management (DRM)**: methods used in attempt to protect copyrighted materials; purpose is to prevent the unauthorized use, modification, and distribution of copyrighted works.

**Data Loss Prevention (DLP)**: systems that detect and block data exfiltration attempts by monitoring data in motion, at rest, and in use; three primary types:

**network-based DLP**: placed on the edge of a network, scans all outgoing network data. **endpoint-based DLP**: scans stored files and can be used to prevent printing or copying sensitive data to removable storage. **cloud-based DLP**: similar to network DLP but designed specifically for cloud-native environments.

**Cloud Access Security Brokers (CASBs)**: software placed logically between users and cloud-based resources ensuring that cloud resources have the same protections as resources within a network.

CASB is a solution for security policy enforcement, ensuring security policies and compliance are met when accessing cloud applications and data; it can be used on-premise or in the cloud. The four cornerstones of CASBs are visibility, data security, threat detection, and compliance.

Entities must comply with the EU GDPR, and use additional data protection methods/controls such as anonymization and randomized masking (which, when done correctly, can't be reversed), or quasi-anonymization which can be reversed (pseudonymization, tokenization, encryption).

One of the primary methods of protecting the confidentiality of data is encryption.

#### Options for protecting your data vary depending on its state

Data at rest: consider encryption for operating system volumes and data volumes, and backups as well.

Be sure to consider all locations for data at rest, such as tapes, USB drives, external drives, RAID arrays, SAN, NAS, and optical media.

DRM is useful for data at rest because DRM "travels with the data" regardless of the data state.

DRM is especially useful when you can’t encrypt data volumes.

Data in transit: think of data in transit wholistically -- moving data from anywhere to anywhere; use encryption for data in transit.

E.g. a web server uses a certificate to encrypt data being viewed by a user, or IPsec encrypting a communication session. Most important point is to use encryption whenever possible, including for internal-only web applications. DLP solutions are useful for data in transit, scanning data on the wire, and stopping the transmission/transfer, based on the DLP rules set (e.g. outbound data that contains numbers matching a social security number pattern, a DLP rule can be used to block that traffic).

#### Data in use

A **Cloud Access Security Broker (CASB)** applies visibility and policy controls to cloud service use. Capabilities may include data protection, access policy, and threat detection; deployment determines which traffic and activities it can inspect. It does not universally protect arbitrary data in process memory.

**Pseudonymization** refers to the process of using pseudonyms to represent other data; process of replacing data elements with pseudonyms or aliases.

A pseudonym is an alias, and pseudonymization can prevent data from directly identifying an entity (i.e. person). An external dataset holds the original data along with the pseudonym such that the original data can be recreated. Therefore, unlike full anonymization, pseudonymized data can be reversed if the key is available.

**Tokenization**: use of a token, typically a random string of characters, to replace other data.

Tokenization is similar to pseudonymization in that they are both used to represent other data, and the token or pseudonym have no meaning or value outside the process that creates and links them to that data.

#### Example of tokenization used in CC transactions

Registration: application on user's smart phone securely sends CC information to the credit card processor (CCP).

The CCP sends the CC information to a tokenization vault, creating a token and associating it with the user's phone.

Usage: when the user makes a purchase, the POS system sends the token to the CCP for authorization. Validation: the CCP sends the token to the tokenization vault; the vault replies with the CC info, the charge is processed. Completing the sale: the CCP sends a reply to the POS indicating the charge is approved. Tokenization reduces exposure of the original card number at the point of sale. Protect tokens, mappings, and transaction authorization as well; the design does not eliminate every form of payment fraud.

Also see [Understanding CISSP Domain 2: Asset Security](https://blog.balancedsec.com/p/understanding-cissp-domain-2-asset) on the source author's blog, [The Cyber Leader](https://blog.balancedsec.com/) for additional information.

### AI in this objective

**Privacy protection for AI.** Data masking obscures selected values. Differential privacy introduces controlled randomness to limit what can be learned about an individual's contribution under a defined privacy model. Neither term alone proves that a dataset is safe to share: evaluate the method, remaining linkability, and intended use. [NIST AI privacy characteristics](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/).

### Apply this objective

**Question.** A support tool decrypts records correctly but lets staff export every customer's information. What additional protection is needed?

**Reasoning.** Restrict authorized access and exports, enforce handling policy, and monitor or block inappropriate transfers where possible. Encryption alone cannot distinguish an appropriate business use from an excessive authorized export.

## Chapter review

Return to the Harbor examples and explain each decision without looking at the answer. Identify the asset or business activity, the relevant requirement, the possible harm, the responsible owner, and the evidence that would support the decision. If two controls appear interchangeable, explain the different failure each addresses.

### Connections and common distinctions

Ownership is accountability; custody is execution. Classification drives handling. Retention is not permission to keep unsupported systems indefinitely. Pseudonymization and tokenization do not necessarily anonymize information. Connect data controls to the identity decisions in Domain 5.

### Review questions and explained answers

**1. How would you explain this domain to Harbor's service owner?** Describe the decisions it governs using the examples in this chapter. A useful answer connects technical measures to customer service, accountability, and evidence rather than listing product names.

**2. Which assumption in the chapter's examples would most change your recommendation if it were false?** Choose a concrete assumption, such as data sensitivity, allowed downtime, or an identity's authority. Explain how a different assumption changes the relevant control or test. More than one answer can be sound when justified.

**3. How does adding the AI assistant change the work?** Follow the AI lessons in this chapter. Identify an additional asset, failure, or decision and describe its owner and verification method. The assistant still operates within ordinary governance, access, data, and recovery requirements.

### AI application review

**Question.** Can Harbor remove customer names from old support conversations and call the training dataset anonymous?

**Reasoning.** Not automatically. Other details may identify people. Classify and inventory the dataset and model artifacts, assess remaining linkability, and select appropriate privacy measures. Track provenance and changes to detect poisoning, and apply retention and disposal rules to copies and derived data. Differential privacy has a defined mathematical model; masking is not the same claim.

## Term index

This index points to explanations in the chapter. Terms retain the source guide's spelling where useful for recognition; corrected concepts are explained in context.

- [AI assets](#objective-2-1)
- [Anonymization](#subtopic-2-6-4)
- [Asset](#subtopic-2-1-2)
- [Asset Classification](#subtopic-2-1-2)
- [Asset handling](#objective-2-2)
- [Asset lifecycle](#subtopic-2-4-6)
- [Baseline](#subtopic-2-6-2)
- [Clearance](#subtopic-2-1-2)
- [Clearing](#subtopic-2-4-7)
- [Cloud Access Security Brokers (CASBs)](#subtopic-2-6-4)
- [cloud-based DLP](#subtopic-2-6-4)
- [clusters](#subtopic-2-4-6)
- [Confidential](#subtopic-2-1-1)
- [Confidential/Proprietary](#subtopic-2-1-1)
- [crypto shredding](#subtopic-2-4-7)
- [Cryptographic Erasure](#subtopic-2-4-7)
- [Data at rest](#subtopic-2-6-1)
- [Data categorization](#subtopic-2-1-1)
- [data collection guideline](#subtopic-2-4-2)
- [Data Collection Limitation](#objective-2-2)
- [Data collection limitations](#objective-2-2)
- [Data controller](#subtopic-2-4-1)
- [Data custodian](#subtopic-2-4-1)
- [Data in transit](#subtopic-2-6-1)
- [Data in use](#subtopic-2-6-1)
- [Data Location](#objective-2-2)
- [Data location](#subtopic-2-4-3)
- [Data Loss Prevention (DLP)](#subtopic-2-6-4)
- [Data Maintenance](#objective-2-2)
- [Data maintenance](#subtopic-2-4-4)
- [Data owner](#subtopic-2-4-1)
- [Data processor](#subtopic-2-4-1)
- [Data protection methods](#subtopic-2-6-4)
- [Data Protection Officer (DPO)](#subtopic-2-4-1)
- [Data remanence](#subtopic-2-4-6)
- [Data Remanence](#subtopic-2-4-7)
- [Data steward](#subtopic-2-4-1)
- [Defensible destruction](#subtopic-2-4-7)
- [Degaussing](#subtopic-2-4-7)
- [Destruction](#subtopic-2-4-7)
- [digital rights management (DRM)](#subtopic-2-6-4)
- [EEPROM](#subtopic-2-4-6)
- [End-Of-Life (EOL)](#objective-2-5)
- [End-Of-Support (EOS)/End-Of-Service-Life (EOSL)](#objective-2-5)
- [endpoint-based DLP](#subtopic-2-6-4)
- [EPROM / UVEPROM](#subtopic-2-4-6)
- [Erasing](#subtopic-2-4-7)
- [File carving](#subtopic-2-4-7)
- [formal access approval process](#subtopic-2-1-2)
- [Hardware assets](#subtopic-2-3-3)
- [how long to retain data](#subtopic-2-4-5)
- [how to retain](#subtopic-2-4-5)
- [Information and Asset owner](#subtopic-2-3-1)
- [Intangible assets](#subtopic-2-3-2)
- [Inventory](#subtopic-2-3-2)
- [Labeling](#objective-2-2)
- [Least privilege](#objective-2-3)
- [Marking](#objective-2-2)
- [Need-to-know](#objective-2-3)
- [network-based DLP](#subtopic-2-6-4)
- [Personally Identifiable Information (PII)](#subtopic-2-1-1)
- [Privacy protection for AI](#objective-2-6)
- [Private](#subtopic-2-1-1)
- [PROM](#subtopic-2-4-6)
- [Proprietary data](#subtopic-2-1-1)
- [Protected Health Information (PHI)](#subtopic-2-1-1)
- [Pseudonymization](#subtopic-2-6-4)
- [Public](#subtopic-2-1-1)
- [Purging](#subtopic-2-4-7)
- [RAM](#subtopic-2-4-6)
- [Randomized masking](#subtopic-2-6-4)
- [record retention](#subtopic-2-4-5)
- [ROM](#subtopic-2-4-6)
- [Scoping](#subtopic-2-6-2)
- [Secret](#subtopic-2-1-1)
- [sectors](#subtopic-2-4-6)
- [Security administrator](#subtopic-2-4-1)
- [Sensitive](#subtopic-2-1-1)
- [Sensitive data](#subtopic-2-1-1)
- [slack space](#subtopic-2-4-6)
- [Software assets](#subtopic-2-3-3)
- [Standards selection](#subtopic-2-6-3)
- [Storage](#objective-2-2)
- [Supervisors](#subtopic-2-4-1)
- [System owner](#subtopic-2-4-1)
- [system owner](#subtopic-2-4-1)
- [Tailoring](#subtopic-2-6-2)
- [Tangible assets](#subtopic-2-3-2)
- [TEMPEST](#subtopic-2-4-6)
- [Tokenization](#subtopic-2-6-4)
- [Top Secret](#subtopic-2-1-1)
- [Training-data integrity](#objective-2-4)
- [Unclassified](#subtopic-2-1-1)
- [Users](#subtopic-2-4-1)
- [what data](#subtopic-2-4-5)

## Sources and further reading

- [Original Domain 2 objectives and notes](../CISSP-Domain-2-2024+Objectives.md) by the repository's contributors; adapted under the repository license.
- [ISC2 CISSP exam outline and AI domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).
- [ISC2 AI guidance announcement](https://www.isc2.org/Insights/2026/04/ISC2-Publishes-Exam-Guidance-AI).
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

Additional references appear alongside the relevant concepts. Official Study Guide chapter references in the original objective files remain available for comparison.
