<a id="domain-7"></a>

# Domain 7: Security Operations

Exam weight: 13%. Study edition: September 2026.

## Start here

Security operations keeps protection working from day to day and coordinates action when something fails. You will learn how investigation, monitoring, configuration, incident response, recovery, physical security, and personnel safety fit together. The chapter links technical activities to the continuity priorities established in Domain 1.

This chapter follows the published Domain 7 objectives. Read the opening explanation of each objective first, then the detailed lessons, and finish with its application check. Three-part numbers identify subtopics retained from the source guide. The examples use Harbor Services, a small organization launching a customer portal and an AI support assistant.

Artificial intelligence (AI) is the broad field of systems performing tasks associated with intelligence. Machine learning (ML) builds models from examples during training; inference uses a trained model to produce an output. A large language model (LLM) produces language using learned numerical parameters called model weights. These terms identify components and processes to protect, rather than establish that a system is correct or trustworthy.

The AI additions apply [ISC2's domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline) to existing objectives. Detailed placement and Harbor scenarios are editorial teaching choices. Named historical technologies remain useful for comparison; their inclusion is not a recommendation to deploy them.

## Chapter navigation

- [7.1 Understand and comply with investigations](#objective-7-1)
- [7.2 Conduct logging and monitoring activities](#objective-7-2)
- [7.3 Perform Configuration Management (CM) (e.g. provisioning, baselining, automation)](#objective-7-3)
- [7.4 Apply foundational security operations concepts](#objective-7-4)
- [7.5 Apply resource protection](#objective-7-5)
- [7.6 Conduct incident management](#objective-7-6)
- [7.7 Operate and maintain detection and preventative measures](#objective-7-7)
- [7.8 Implement and support patch and vulnerability management](#objective-7-8)
- [7.9 Understand and participate in change management processes](#objective-7-9)
- [7.10 Implement recovery strategies](#objective-7-10)
- [7.11 Implement Disaster Recovery (DR) processes](#objective-7-11)
- [7.12 Test Disaster Recovery Plans (DRP)](#objective-7-12)
- [7.13 Participate in Business Continuity (BC) planning and exercises](#objective-7-13)
- [7.14 Implement and manage physical security](#objective-7-14)
- [7.15 Address personnel safety and security concerns](#objective-7-15)

<a id="objective-7-1"></a>

## 7.1 Understand and comply with investigations

Investigations depend on evidence that can be explained and trusted. Identify what needs to be preserved, who is authorized to collect it, and how collection may change the system. Volatile data can disappear when power or processes change, while stored data can be altered by ordinary use.

Chain of custody records possession and handling. Hashes can help demonstrate that a copy has not changed since collection, but they do not prove the original information was true. Preserve originals where appropriate, analyze controlled copies, and document tools, times, and actions.

**Investigation**: a formal inquiry and systematic process that involves gathering information to determine the cause of a security incident or violation.

Investigators must be able to conduct reliable investigations that will hold up in court; securing the scene is an essential and critical part of every investigation.

#### Securing the scene might include any/all of the following

Sealing off access to the area or crime scene. Taking images of the scene. Documenting evidence. Ensuring evidence (e.g. computers, mobile devices, portable drives etc) is not contacted, tampered with, or destroyed.

#### General steps

Identify and secure the scene. Protect evidence to preserve its integrity and the chain of custody. Identification and examination of the evidence. Complete additional analysis of the most compelling evidence. Produce a final reporting of findings.

**Locard exchange principle**: whenever a crime is committed something is taken, and something is left behind.

#### The purpose of an investigation is to

Identify the root cause of the incident. Prevent future occurrences. Mitigate the impact of the incident on the organization.

#### Types of investigations

**administrative** is an investigation that is focused on policy violations.

**criminal**: conducted by law enforcement, this type of investigation tries to determine if there is cause to believe (beyond a reasonable doubt) that someone committed a crime.

The goal is to gather evidence that can be used to convict in court. The job of a security professional is to preserve evidence, ensure law enforcement has been contacted, and assist as necessary.

**civil**: non-criminal investigation for matters such as contract disputes.

The goal of a civil investigation is to gather evidence that can be used to support a legal claim in court, and is typically triggered from an imminent or on-going lawsuit. The level of proof is much lower for a civil compared to a criminal investigation.

**regulatory**: investigation initiated by a government regulator when there is reason to believe an organization is not in compliance.

This type of investigation varies significantly in scope and could look like any of the other three types of investigation depending on the severity of the allegations. As with criminal investigations, it is key to preserve evidence, and assist the regulator’s investigators.

<a id="subtopic-7-1-1"></a>

### 7.1.1 Evidence collection and handling

**Sampling** is one of two main methods of choosing records from a large pool for further analysis, sampling uses statistical techniques to choose a sample that is representative of the entire pool; sampling is a data extraction process, where elements are selected from a large body of data to construct a meaningful representation or summary of the whole; statistical sampling uses precise math functions to extract meaningful information from a large volume of data (also see clipping). **Cyber forensics**: gathering, retaining, analyzing data for investigative purposes, while maintaining the integrity of that data.

**Clipping** is one of two main methods of choosing records from a large pool for further analysis, clipping selects records exceeding a predefined threshold; clipping is a form of non-statistical sampling that records only events that exceed the threshold (also see sampling). Evidence collection is complex, should be done by professionals, and can be thrown out of court if incorrectly handled. It’s important to preserve original evidence; as soon as an incident is discovered, evidence collection should begin, and as much information about the incident as possible should be collected; the evidence can be used in a subsequent legal action or in finding the identity of the attacker; evidence can also assist in determining the extent of damage; because discovery may happen after an incident has occurred, it's critical that log files are retained for a reasonable period of time; log files and system status information can be retained either in place or in archives.

**International Organization on Computer Evidence (IOCE) six principles for media, network and software analysis**:

All general forensic and procedural principles must be applied to digital evidence collection. Seizing digital evidence shouldn't change the evidence. Accessing original digital evidence should only be done by trained professionals. All activity relating to seizure, access, storage, or transfer of digital evidence must be fully documented, preserved, and available for review. A person in possession of digital evidence is responsible for all actions taken with respect to that evidence. Any agency that is responsible for seizing, accessing, storing, or transferring digital evidence is responsible for compliance with these principles.

**Scientific Working Group on Digital Evidence (SWGDE) developed principles for standardized recovery of computer-based evidence**: legal system consistency; use of a common language; durability; ability to cross international and state boundaries; instill confidence in evidence integrity; forensic evidence applicability at the individual, agency, and country levels.

**ISO/IEC 27037: Guidelines for Identification, Collection, Acquisition, and Preservation of Digital Evidence** is the international standard on digital evidence handling, with four phases: identification; collection; acquisition; preservation.

#### Types of evidence

#### Primary evidence

Most reliable and used at trial. Original documents (e.g. legal contracts), no copies or duplicates.

#### Secondary evidence

Less powerful and reliable than primary evidence (e.g. copies of originals, witness oral evidence etc). If primary evidence is available secondary of the same content is not valid.

**best evidence rule**: states that the original evidence should be presented in court, rather than a copy or other secondary evidence. **circumstantial evidence**: this type of evidence is based on inference and can be used to support a conclusion, but not prove it. **corroborative evidence**: this type of evidence is used to support other evidence and can be used to strengthen a case. **demonstrated evidence** can be objects, pictures, models, displays used in a trial to support facts the party is trying to prove. **direct evidence**: this type of evidence is based on the observations of a witness or expert opinion and can be used to prove a fact at hand (with backup evidence support).

**hearsay evidence** is a type of evidence that is based on statements made by someone outside of court and is generally not admissible; rule says that a witness cannot testify about what someone else told them; courts have applied it such that attorneys may not introduce system logs into evidence unless they are authenticated by a system admin. **parol evidence rule**: determines whether extra/additional evidence can be used to alter or explain a written contract, stating that a written contract takes precedence over any oral negotiations or stipulations that relate to it; the rule generally prohibits the introduction of parol (extra) evidence that contradicts or varies the contract's terms.

**real evidence**: this type of evidence includes physical objects such as computers, hard drives, and other storage devices, that can be brought into a court of law; real evidence must be either uniquely identified by a witness or authenticated through a documented chain of custody.

It is important to note that evidence should be collected and handled in a forensically sound manner to ensure that it is admissible in court and to avoid any legal issues.

The **chain of custody**: focuses on having control of the evidence -- who collected and handled what evidence, when, and where.

#### Think about establishing the chain of custody as

Tag. Bag and. Carry the evidence.

#### Basic alternatives for confiscating evidence

Person who owns the evidence voluntarily surrenders it. A subpoena is used to compel the subject to surrender the evidence. A law enforcement officer while performing a legally permissible duty, and with probable cause to believe is associated with criminal activity seizes visible evidence. A search warrant is used to confiscate evidence without giving the subject an opportunity to alter it. A law enforcement officer collects evidence when exigent circumstances exist.

Five rules of evidence: five evidence characteristics providing the best chance of surviving legal and other scrutiny:

**authentic**: evidence is not fabricated or planted, and can be proven through crime scene photos, or bit-for-bit copies of storage. **accurate**: evidence that has integrity (not been modified). **complete**: evidence must be complete, and all parts available and shared, whether they support the case or not. **convincing**: evidence must be easy to understand, and convey integrity. **admissible**: evidence must be accepted as part of a case; admissible evidence must be relevant to a fact at issue in the case, the fact must be material to the case, and the evidence must be competent or legally collected.

<a id="subtopic-7-1-2"></a>

### 7.1.2 Reporting and documentation

Each investigation should result in a final report that documents the goals of the investigation, the procedures followed, the evidence collected, and the final results. Preparing formal documentation prepares for potential legal action, and even internal investigations can become part of employment disputes. Identify in advance a single point of contact who will act as your liaison with law enforcement, providing a go-to person with a single perspective, potentially improving the working relationship. Participate in the FBI’s InfraGard program.

<a id="subtopic-7-1-3"></a>

### 7.1.3 Investigative techniques

Whether in response to a crime or incident, an organizational policy breach, troubleshooting a system or network issue etc, digital forensic methodologies can assist in finding answers, solving problems, and in some cases, help in successfully prosecuting crimes.

#### The forensic investigation process should include the following

Identification and securing of a crime scene. Proper collection of evidence that preserves its integrity and the chain of custody. Examination of all evidence. Further analysis of the most compelling evidence. Final reporting.

#### Sources of information and evidence

Oral/written statements: given to police, investigators, or as testimony in court by people who witness a crime or who may have pertinent information. Written documents: checks, printed contracts, handwritten letters/notes. Computer systems: components, local/portable storage, memory etc. Visual/audio: visual and audio evidence pertinent to a security investigation could include photographs, video, taped recordings, and surveillance footage from security cameras.

Several investigative techniques can be used when conducting analysis:

Media analysis: examining the bits on a hard drive that are intact despite not having an index. Software analysis: focuses on an application and malware, determining how it works and what it's trying to do, with a goal of attribution.

<a id="subtopic-7-1-4"></a>

### 7.1.4 Digital forensics tools, tactics, and procedures

Digital forensics: the scientific examination and analysis of data from storage media so that the information can be used as part of an investigation to identify the culprit or the root cause of an incident. **Live evidence**: data stored in a running system e.g. random access memory (RAM), cache, and buffers.

#### Examining a live system can change the state of the evidence

Small changes like interacting with the keyboard, mouse, loading/unloading programs, or of course powering off the system, can change or eliminate live evidence.

Whenever a forensic investigation of a storage drive is conducted, two identical bit-for-bit copies of the original drive should be created first.

**eDiscovery(E-Discovery)** is the process of identifying, collecting, and producing electronically stored information for legal proceedings; the E-Discovery reference model (EDRM) has 9 steps:

Information Governance - ensuring information is well-organized, and balancing value, risk and cost. Identification - locating potential sources of electronically stored information covered by a discovery request, and determining its scope, breadth, and depth. Preservation - ensuring data is protected against alteration or destruction. Collection - gathering data for further use in the process. Processing - screening and reducing the volume of data, and converting as appropriate to forms suitable for review and analysis. Review - evaluating data for relevance; what information needs to be provided, and what may need to be protected.

Analysis - evaluating data for content and context. Production - delivering electronically stored information in a sharable form. Presentation - displaying before appropriate audiences (e.g. depositions, hearings, trials etc). Organizations that believe they will be the target of a lawsuit have a duty to preserve digital evidence.

<a id="subtopic-7-1-5"></a>

### 7.1.5 Artifacts (e.g., data, computer, network, mobile device)

Forensic artifacts: remnants of a system or network breach/attempted breach, which may or may not be relevant to an investigation or response.

#### Artifacts can be found in numerous places, including

Computer systems. Web browsers. Mobile devices. Hard drives, flash drives.

### Apply this objective

**Question.** An analyst copies a suspicious file but does not record where it came from or how it was handled. What is missing?

**Reasoning.** Provenance and handling evidence are missing. A file's contents alone may not establish its relationship to the incident. Document collection, integrity checks, custody, and analysis so others can evaluate the conclusion.

<a id="objective-7-2"></a>

## 7.2 Conduct logging and monitoring activities

Logs describe events from particular viewpoints. Monitoring turns those records and other signals into questions worth investigating. Correlation can connect a suspicious login, an unusual process, and an outbound transfer, but the relationship still needs validation.

At Harbor, useful monitoring depends on reliable timestamps, sufficient detail, protected storage, retention, and a response process. Tune detection to reduce noise without hiding important events. An absence of alerts may reflect a blind spot rather than an absence of attacks.

<a id="subtopic-7-2-1"></a>

### 7.2.1 Intrusion detection and prevention system (IDPS)

**Intrusion** is a security event, or a combination of multiple security events that constitutes an incident; occurs when an attacker attempts to bypass or can bypass/thwart security mechanisms and access an organization’s resources without the authority to do so. **Intrusion detection** is a specific form of monitoring events, usually in real time, to detect abnormal activity indicating a potential incident or intrusion.

**Intrusion Detection System (IDS)**: (AKA burglar alarms) is a security service that monitors and analyzes network or system events for the purpose of finding/providing realtime/neartime warnings of unauthorized attempts to access system resources; automates the inspection of logs and real-time system events to detect intrusion attempts and system failures.

An IDS is intended as part of a defense-in-depth security plan.

**Intrusion Prevention Systems (IPS)** is an IPS is a security service that uses available information to determine if an attack is underway, alerting and also blocking attacks from reaching intended target; includes detection capabilities, you’ll also see them referred to as intrusion detection and prevention systems (IDPSs).

An IPS can be a signature-based detection system which matches traffic patterns against a database of known attack signatures; it can be anomaly or behavior-based detection, that starts with a baseline, comparing activity to the baseline to detect abnormal activity; IPS can also be policy-based, comparing activity to predefined security policies, or hybrid of these.

[NIST SP 800-94](https://csrc.nist.gov/pubs/sp/800/94/final) Guide to Intrusion Detection and Prevention Systems provides comprehensive (albeit outdated) coverage of both IDS and IPS.

<a id="subtopic-7-2-2"></a>

### 7.2.2 Security Information and Event Management (SIEM)

Security Information and Event Management (SIEM): systems that ingest logs from multiple sources, compile and analyze log entries, and report relevant information.

SIEM systems are complex and require expertise to install and tune. Require a properly trained team that understands how to read and interpret info, and escalation procedures to follow when a legitimate alert is raised. SIEM systems represent technology, process, and people, and each is important to overall effectiveness. A SIEM includes significant intelligence functionality, allowing large amounts of logged events and analysis and correlation of the same to occur very quickly.

SIEM solutions enhance threat detection and incident response, provide visibility and compliance management, and with AI and automation improve the security team's effectiveness.

#### Key capabilities include

Aggregation. Normalization. Correlation. Secure storage. Analysis. Reporting.

**Security Orchestration, Automation, and Response (SOAR)** refers to a group of technologies that allow organizations to respond to some incidents automatically; SOAR tech automates responses to incidents; a primary benefit is that this reduces the workload of admins, and it removes/reduces the possibility of human error by having a computer/system respond. **Playbook** is a document or checklist that defines how to respond to an incident. **Runbook**: implementation of the playbook's documented processes; implements the playbook's content, translating steps into automated actions. SOAR allows security admins to define these incidents and the response, typically using playbooks and runbooks.

Both SOAR and SIEM platforms can help detect and, in the case of SOAR, respond to threats against your software development efforts.

Devs can be resistant to anything that slows down the development process, and this is where DevSecOps can help build the right culture, and balance the needs of developers and security.

<a id="subtopic-7-2-3"></a>

### 7.2.3 Continuous monitoring and tuning

Effective continuous monitoring encompasses technology, processes, and people.

#### Continuous monitoring steps are

Define. Establish. Implement. Analyze/report. Respond. Review/update.

**Monitoring** is the process of reviewing information logs, looking for something specific.

Necessary to detect malicious actions by subjects as well as attempted intrusions and system failures. Can help reconstruct events, provide evidence for prosecution, and create reports for analysis. Continuous monitoring ensures that all events are recorded and can be investigated later if necessary. Monitoring is a form of auditing that focuses on active review of log file data; it's used to hold subjects accountable for their actions and to detect abnormal or malicious activities. It is also used to gauge system performance. Tools like IDSs and SIEMs automate continuous monitoring and provide real-time analysis of events, including monitoring both ingress and egress network traffic.

**Log analysis** is a detailed and systematic form of monitoring where logged information is analyzed for trends and patterns as well as abnormal, unauthorized, illegal, and policy-violating activities.

Log analysis isn’t necessarily in response to an incident, it’s a periodic task.

After a SIEM is set up, configured, tuned, and running, it must be routinely updated and continuously monitored to function effectively. **Tuning**: tuning a SIEM is inherently the process of reducing **false positives** (incorrectly classifying a benign activity, system state, or configuration as malicious or vulnerable), while not incurring **false negatives** (NOT alerting on a true malicious activity or vulnerability); false positives can result in analyst fatigue and reduced efficiency.

<a id="subtopic-7-2-4"></a>

### 7.2.4 Egress monitoring

**Egress monitoring**: monitoring the flow of information out of an organization's boundaries.

It’s important to monitor traffic exiting as well as entering a network, and **Egress monitoring** refers to monitoring outgoing traffic to detect unauthorized data transfer outside the organization (AKA data exfiltration).

Common methods used to detect or prevent data exfiltration are data loss prevention (DLP) techniques and monitoring for steganography.

<a id="subtopic-7-2-5"></a>

### 7.2.5 Log management

**Log**: record of actions/events that have taken place on a system. **Log management** refers to all the methods used to collect, process, analyze, and protect log entries (see SIEM definition above). **rollover logging** allows admins to set a maximum log size, when the log reaches that max, the system begins overwriting the oldest events in the log.

<a id="subtopic-7-2-6"></a>

### 7.2.6 Threat intelligence (e.g. threat feeds, threat hunting)

**Threat intelligence** is an umbrella term encompassing threat research and analysis and emerging threat trends; gathering data on potential threats, including various sources to get timely information on current threats; information that is aggregated, transformed, analyzed, interpreted, or enriched to provide the necessary context for the decision-making process. **Threat feed**: provide organizations with a steady stream of raw data providing security admins with threat feeds to understand current threats; by using this knowledge to search through the network they can engage in threat hunting looking for signs of these threats.

**Structured Threat Information eXpression (STIX)** is a standardized language that uses a JSON-based lexicon to express and share threat intelligence information in a readable and consistent format. **Trusted Automated eXchange of Intelligence Information (TAXII)** is the format through which threat intelligence data is transmitted; TAXII is a transport protocol that supports transferring STIX insights over Hyper Text Transfer Protocol Secure (HTTPS). **Threat hunting** is a proactive search across an organization’s network and endpoints to identify malicious activity that has evaded traditional automated security tools; threat hunting assumes an attacker may already be present in the environment.

#### Kill chain: military model (used for both offense and defense)

Find/identify a target through reconnaissance. Get the target’s location. Track the target’s movement. Select a weapon to use on the target. Engage the target with the selected weapon. Evaluate the effectiveness of the attack.

Organizations have adapted this model for cybersecurity: Lockheed Martin created the **Cyber Kill Chain** framework including seven ordered stages of an attack:

**reconnaissance**: attackers gather information on the target. **weaponization**: attackers identify an exploit that the target is vulnerable to, along with methods to send the exploit. **delivery**: attackers send the weapon to the target via phishing attacks, malicious email attachments, compromised websites, or other common social engineering methods. **exploitation** is the weapon exploits a vulnerability on the target system. **installation**: code that exploits the vulnerability then installs malware with a backdoor allowing attacker remote access. **command and control**: attackers maintain a command and control system, which controls the target and other compromised systems.

**actions on objectives**: attackers execute their original goals such as theft of money, or data, destruction of assets, or installing additional malicious code (eg. ransomware).

<a id="subtopic-7-2-7"></a>

### 7.2.7 User and Entity Behavior Analytics (UEBA)

**Heuristics** is a method of machine learning which identifies patterns of acceptable activity, so that deviations from the patterns will be identified. **Entity** is any form of a user including hardware device, software daemon, task, processing thread or human, which is attempting to use or access system resources; e.g. endpoint devices are entities that human (or non-human) users use to access a system; should be subject to access control and accounting. **UEBA (aka UBA)** focuses on the analysis of user and entity behavior as a way of detecting inappropriate or unauthorized activity (e.g. fraud, malware, insider attacks etc); analysis engines are typically included with SIEM solutions or may be added via subscription; UEBA tools develop profiles of individual behavior and monitor users for deviations from those profiles that may indicate malicious activity and/or compromised accounts.

**Behavior-based detection**: AKA statistical intrusion, anomaly, and heuristics-based detection, starts by creating a baseline of normal activities and events; once enough baseline data has been accumulated to determine normal activity, it can detect abnormal activity (that may indicate a malicious intrusion or event). Behavior-based IDSs use the baseline, activity statistics, and heuristic evaluation techniques to compare current activity against previous activity to detect potentially malicious events. **Static code scanning techniques** is the scanner scans code in files, similar to white box testing. **Dynamic techniques** is the scanner runs executable files in a sandbox to observe their behavior.

### AI in this objective

**Model drift.** Monitor whether a model's performance changes after deployment, as well as whether telemetry and controls remain healthy. Establish a task-specific baseline and review meaningful deviations. [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).

### Apply this objective

**Question.** Harbor receives no alerts from a newly deployed service. What should the team check before calling it quiet?

**Reasoning.** Confirm that telemetry is being generated, collected, parsed, and evaluated by relevant rules. Test a known event and verify the response path. No alerts are meaningful only when the monitoring works.

<a id="objective-7-3"></a>

## 7.3 Perform Configuration Management (CM) (e.g. provisioning, baselining, automation)

Configuration management establishes what a system should look like and controls changes to that state. Provisioning creates the system, a baseline describes approved settings, and drift is a deviation from those settings. Automation can make builds repeatable and differences easier to detect.

A baseline is not permanently correct. Harbor must update it when requirements or threats change, and manage justified exceptions. Keep the inventory, configuration records, and actual deployed state aligned.

### Concepts in context

**Baseline**: total inventory of all of a system's components (e.g. hardware, software, data, admin controls, documentation, user instruction); types of baselines include enumerated (which are inventory lists, generated by system cataloging, discovery or enumeration), build security (minimal set of security controls for each CI, see below), modification/update/patch baselines (subsets of total system baseline), or configuration baseline (which should include a revision/version identifier associated with each CI).

**Configuration Management (CM)** is the process of identifying, controlling, and verifying the configuration of organizational systems and settings; the focus is on establishing and maintaining the integrity of IT products and systems by controlling their initialization and changes, and by monitoring configuration throughout their lifecycle.

The three basic components of change management: request control, change control, and release control. CM is an integral part of secure provisioning and relates to the proper configuration of a device at the time of deployment. CM helps ensure that systems are deployed in a secure, consistent state and that they stay in a secure, consistent state throughout their lifecycle.

**Provisioning**: taking a particular config baseline, making additional or modified copies, and placing those copies into the environment in which they belong; refers to installing and configuring the operating system and needed applications on new systems.

New systems should be configured to reduce vulnerabilities introduced via default configurations; the key is to harden a system based on intended usage.

**Hardening a system** is a process of applying security configurations, and locking down various hardware, communications systems, software (e.g. OS, web/application server, applications etc); normally performed based on industry guidelines and benchmarks like the Center for Internet Security (CIS);.

Makes it more secure than the default configuration and includes the following: disable all unused services; close all unused logical ports; remove all unused applications; change default passwords.

**Baseline**: in the context of configuration management, a baseline is the starting point or starting config for a system.

An easy way to think of a baseline is as a list of services; an OS baseline identifies all the settings to harden specific systems. Many organizations use images to deploy baselines; baseline images improve the security of systems by ensuring that desired security settings are always configured correctly. Baseline images improve the security of systems by ensuring that desired security settings are always configured correctly; they also reduce the amount of time required to deploy and maintain systems, reducing overall maintenance costs.

Automation: it's typical to create a baseline, and then use automated methods to add additional applications, features, or settings for specific groups of computers.

Admins can use create/modify group policy settings to create domain-level standardization or to make security-related Windows registry changes.

### Apply this objective

**Question.** An emergency setting change fixes an outage but is absent from configuration records. What should happen next?

**Reasoning.** Review and document the change, determine whether it should remain, update the approved baseline if justified, and reconcile automation. Otherwise a rebuild may silently reintroduce the failure or preserve an insecure exception.

<a id="objective-7-4"></a>

## 7.4 Apply foundational security operations concepts

Operational controls reduce the opportunity for misuse and help detect it. Least privilege limits authority; need-to-know limits access to relevant information; separation of duties divides sensitive work so one person cannot complete every step unchecked. Rotation and oversight can reveal hidden practices.

Privileged accounts need stronger management because their actions have broader consequences. Service commitments should identify expected performance, responsibilities, and escalation. These controls support reliable work rather than merely making work slower.

Security operations encompasses the day-to-day tasks, practices, and processes involved in securing and maintaining the operational integrity of an organization's information systems and assets; it includes security monitoring, incident response, and security awareness and training. The primary purpose of security operations practices is to safeguard assets such as information, systems, devices, facilities, and applications, and helping organizations to detect, prevent, and respond to security threats. Implementing common security operations concepts, along with performing periodic security audits and reviews, demonstrates a level of due care and due diligence.

<a id="subtopic-7-4-1"></a>

### 7.4.1 Need-to-know/least privilege

Need-to-Know: principle restricts access to information or resources to only those individuals who require it to perform their specific tasks or duties.

Focus: protects sensitive information by limiting **what** someone can access.

Least Privilege: principle that limits the access rights of users, processes, or systems to the minimum level necessary to perform their job functions; states that subjects are granted only the privileges necessary to perform assigned work tasks and no more.

Focus: restricts **how much** access a user or system has (permissions). Privilege in this context includes both permissions to data and rights to perform systems tasks. Limiting and controlling privileges based on this concept protects confidentiality and data integrity. Principle relies on the assumption that all users have a well-defined job description that personnel understand. Least privilege is typically focused on ensuring that user privileges are restricted, but it also applies to applications or processes (e.g. if an application or service is compromised, the attacker can assume the service account’s privileges).

Need to know and least privilege principle are two standard IT security principles implemented in secure networks; they limit access to data and systems so users and other subjects can access only what they require; this limited access helps prevent security incidents and helps limit the scope of incidents when they occur; when not followed, security incidents result in far greater damage to an organization.

<a id="subtopic-7-4-2"></a>

### 7.4.2 Segregation of Duties (SoD) and responsibilities

**Segregation of Duties (SoD)** ensures that no single person has total control over a critical function or system.

SoD policies help reduce fraud by requiring collusion between two or more people to perform unauthorized activity. Example of how SoD can be enforced, is by dividing the security or admin capabilities and functions among multiple trusted individuals.

**Two-person control**: (AKA two-man rule) requires the approval of two individuals for critical tasks.

Using two-person controls within an organization ensures peer review and reduces the likelihood of collusion and fraud. Ex: privilege access management (PAM) solutions that create special admin accounts for emergency use only; perhaps a password is split in half so that two people need to enter the password to log on.

**Split knowledge** combines the concepts of separation of duties and two-person control into a single solution; the information or privilege required to perform an operation is divided among two or more users, ensuring that no single person has sufficient privileges to compromise the security of the environment; M of N control is an example of split knowledge.

Principles such as least privilege and separation of duties help prevent security policy violations, and monitoring helps to deter and detect any violations that occur despite the use of preventive controls.

**Collusion** is an agreement among multiple people to perform some unauthorized or illegal actions;.

Implementing SoD, two-person control, or split knowledge policies help prevent fraud by limiting actions individuals can do without colluding with others.

<a id="subtopic-7-4-3"></a>

### 7.4.3 Privileged account management

Privileged entities are trusted, but they can abuse privileges, and it's therefore essential to monitor all assignments of privileged operations. The goal is to ensure that trusted employees do not abuse the special privileges that are granted; monitoring these operations can also detect many attacks, because attackers commonly use special privileges during an attack. Advanced privileged account management practices can limit the time users have advanced privileges.

**Privileged Account Management (PAM)**: solutions that restrict access to privileged accounts or detect when accounts use any elevated privileges (e.g. admin accounts).

Microsoft domains, this includes local admin accounts, Domain and Enterprise Admins groups. Linux includes root or sudo accounts.

PAM solutions should monitor actions taken by privileged accounts, new user accounts, new routes to a router table, altering config of a firewall, accessing system log and audit files.

<a id="subtopic-7-4-4"></a>

### 7.4.4 Job rotation

**Job rotation**: (AKA rotation of duties) means that employees rotate through jobs or rotate job responsibilities with other employees.

Using job rotation as a security control provides peer review, reduces fraud, and enables cross-training. Job rotation policy can act as both a deterrent and a detection mechanism.

<a id="subtopic-7-4-5"></a>

### 7.4.5 Service Level Agreements (SLA)

**Service Level Agreement (SLA)** is an agreement between an organization and an outside entity, such as a vendor, where the SLA stipulates performance expectations and often includes penalties if the vendor doesn’t meet these expectations. **Memorandum of Understanding (MOU)**: documents the intention of two entities to work together toward a common goal.

### Apply this objective

**Question.** One administrator can request, approve, and execute payments. Which operational principle should Harbor apply?

**Reasoning.** Separate incompatible duties and require an independent approval or other justified control. Logging is useful, but reviewing an action after the fact does not provide the same prevention as separating authority.

<a id="objective-7-5"></a>

## 7.5 Apply resource protection

Resource protection maintains the confidentiality, integrity, and availability of the assets used in operations. Media handling includes inventory, storage, transport, access, reuse, and disposal. A backup copy or removable device can expose the same information as the primary system.

Connect operational handling to Domain 2's classification and retention decisions. Harbor's staff need a practical method for tracking a drive during maintenance and confirming its final destination, not just a general instruction to be careful.

Media management should consider all types of media as well as short- and long-term needs and evaluate: Confidentiality; Access speeds; Portability; Durability; Media format; Data format.

For the test, data storage media should include any of the following: Paper; Microforms (microfilm and microfiche); Magnetic (HD, disks, and tapes); Flash memory (SSD and memory cards); Optical (CD and DVD).

Mean Time Between Failure (MTBF) is an important criterion when evaluating storage media, especially where valuable or sensitive information is concerned. Media management includes the protection of the media itself, which typically involves policies and procedures, access control mechanisms, labeling and marking, storage, transport, sanitization, use, and end-of-life.

<a id="subtopic-7-5-1"></a>

### 7.5.1 Media management

**MTBF**: mean time between failure is an estimation of time between the first and any subsequent failures.

**Media management** refers to the steps taken to protect media (i.e. anything that can hold data) and the data stored on that media; includes most portable devices (e.g. smart phones, memory/flash cards etc).

Media is protected throughout its lifetime and destroyed when no longer needed.

As above, OSG-10 also refers to tape media, as well as “hard-copy data”.

<a id="subtopic-7-5-2"></a>

### 7.5.2 Media protection techniques

If media includes sensitive info, it should be stored in a secure location with strict access controls to prevent loss due to unauthorized access.

Any location used to store media should have temperature and humidity controls to prevent losses due to corruption.

Media management can also include technical controls to restrict device access from computer systems. When media is marked, handled, and stored properly, it helps prevent unauthorized disclosure (loss of confidentiality), unauthorized modification (loss of integrity), and unauthorized destruction (loss of availability).

<a id="subtopic-7-5-3"></a>

### 7.5.3 Data at rest/data in transit

This was previously covered in Domain 2 (see 2.6.4) - Data at rest and data in transit can be protected via encryption.

### Apply this objective

**Question.** A failed drive is being returned to a vendor. What must Harbor consider before shipment?

**Reasoning.** Assess the information it held, applicable handling rules, sanitization options, and the return arrangement. A failed device may still contain recoverable data; inability to boot does not establish successful disposal.

<a id="objective-7-6"></a>

## 7.6 Conduct incident management

Incident management turns a suspected event into coordinated action. Validate what is happening, limit harm, preserve necessary evidence, communicate with the right people, and restore a trustworthy service. The detailed order can overlap and change with urgency, safety, and the incident plan.

Containment limits spread; eradication or remediation addresses causes and persistence; recovery restores service with validation and monitoring. Lessons learned improve prevention and response. Harbor should identify authority and communication routes before a crisis.

**Analysis:** Gathering and analyzing information about the incident to determine its scope, impact, and root cause (e.g., by interviewing witnesses, collecting and analyzing evidence, and reviewing system logs). **Containment:** Limiting the impact of the incident and preventing further damage (e.g., by isolating affected systems, changing passwords, and implementing security controls). **Eradication:** Removing the cause of the incident from the environment (e.g., by removing malware, patching vulnerabilities, and disabling compromised accounts). **Incident response (IR)** is the mitigation of violations of security policies and recommended practices; the process to detect and respond to incidents and to reduce the impact when incidents occur; IR attempts to keep a business operating or restore operations as quickly as possible in the wake of an incident.

Incident management is usually conducted by an Incident Response Team (IRT), which comprises individuals with the required expertise and experience to manage security incidents; the IRT is accountable for implementing the incident response plan, which is a written record that defines the processes to be followed during each stage of the incident response cycle.

#### The main goals of incident response

Provide an effective and efficient response to reduce impact to the organization. Maintain or restore business continuity. Defend against future attacks.

An important distinction needs to be made to know when an incident response process should be initiated: events take place continually, and the vast majority are insignificant; however, events that lead to some type of adversity can be deemed incidents, and those incidents should trigger an organization's incident response process steps.

#### Incident Response Summary

| Step | Stage | Action/Goal |
|--------|---------------| -----------|
| Preparation|||
| (D)etection  | Triage | initial assessment |
| (R)esponse | Investigate | activate IR team |
| (M)itigation  | Reduce incident severity| containment|
| (R)eporting  | Documentation|communicate to stakeholders|
| (R)ecovery | Restoration | return to normal|
| (R)emediation  | Recovery| root cause; prevention|
| (L)essons Learned | Recovery| improve process|

The following steps (Detection, Response, Mitigation, Reporting, Recovery, Remediation, and Lessons Learned) are on the exam; you can use the mnemonic DRMRRRL (drumroll).

In summary: after detecting and verifying an incident, the first response is to limit or contain the scope of the incident while protecting evidence; based on governing laws, an organization may need to report an incident to official authorities, and if PII is affected, individuals need to be informed; the remediation and lessons learned stages include root cause analysis to determine the cause and recommend solutions to prevent reoccurrence.

**Preparation** includes developing the IR process, assigning IR team members, and everything related to what happens when an incident is identified; preparation is critical, and will anticipate the steps to follow.

<a id="subtopic-7-6-1"></a>

### 7.6.1 Detection

**Security Incident** is any attempt to undermine the security of an organization or violation of a security policy is a security incident. **Detection:** the identification of potential security incidents via monitoring and analyzing security logs, threat intelligence, or incident reports; as above, understanding the distinction between an event and an incident, the goal of detection is to identify an adverse event (an incident) and begin dealing with it.

#### Common methods to detect incidents

Intrusion detection and prevention systems. Antimalware. Automated tools that scan audit logs looking for predefined events. End users sometimes detect irregular activity and contact support.

Receiving an alert or complaint doesn’t always mean an incident has occurred.

<a id="subtopic-7-6-2"></a>

### 7.6.2 Response

**Incident** is an event which potentially or actually jeopardizes the CIA of an information system or the information the system processes, stores, transmits. After detecting and verifying an incident, the next step is activate an Incident Response (IR) or CSIRT team. An IR team is AKA computer incident response team (CIRT) or computer security incident response team (CSIRT). Among the first steps taken by the IR Team will be an impact assessment to determine the scale of the incident, how long the impact might be experienced, who else might need to be involved etc.

The IR team typical investigate the incident, assess the damage, collect evidence, report the incident, perform recovery procedures, and participate in the remediation and lessons learned stages, helping with root cause analysis.

It's important to protect all data as evidence during an investigation, and computers should not be turned off.

<a id="subtopic-7-6-3"></a>

### 7.6.3 Mitigation

**Mitigation**: attempt to contain an incident; in addition to conducting an impact assessment, the IR Team will attempt to minimize or contain the damage or impact from the incident. The IR Team's job at this point is not to fix the problem; it's simply to try and prevent further damage. Note this may involve disconnecting a computer from the network; sometimes responders take steps to mitigate the incident, but without letting the attacker know that the attack has been detected.

<a id="subtopic-7-6-4"></a>

### 7.6.4 Reporting

Reporting occurs throughout the incident response process. Once an incident is mitigated, formal reporting occurs because numerous stakeholders often need to understand what has happened. Jurisdictions may have specific laws governing the protection of personally identifiable information (PII), and must report if it's been exposed. Additionally, some third-party standards, such as the Payment Card Industry Data Security Standard (PCI DSS), require organizations to report certain security incidents to law enforcement.

<a id="subtopic-7-6-5"></a>

### 7.6.5 Recovery

Recovery is the next step, returning a system to a fully functioning state. **Recovery:** Restoring systems and data to their normal state (e.g., by restoring from backups, rebuilding systems, and re-enabling compromised accounts); at this point, the goal is to start returning to normal.

The most secure method of restoring a system after an incident is completely rebuilding the system from scratch, including restoring all data from the most recent backup.

Effective configuration and change management will provide the necessary documentation to ensure the rebuilt systems are configured properly.

According to the OSG, you should check these areas as part of recovery:

Access control lists (ACLs), including firewall or router rules. Services and protocols, ensuring the unneeded services and protocols are disabled or removed. Patches. User accounts, ensuring they have changed from default configs. Known compromises have been reversed.

<a id="subtopic-7-6-6"></a>

### 7.6.6 Remediation

**Root Cause Analysis**: principle-based systems approach for the identification of underlying causes associated with a particular risk set or incidents. **Remediation**: changes to a system's config to immediately limit or reduce the chance of reoccurrence of an incident. Remediation stage: personnel look at the incident, identify what allowed it to occur, and then implement methods to prevent it from happening again. Remediation includes performing a root cause analysis (which examines the incident to determine what allowed it to happen), and if the root cause analysis identifies a vulnerability that can be mitigated, this stage will recommend a change.

<a id="subtopic-7-6-7"></a>

### 7.6.7 Lessons Learned

**Lessons Learned:** documenting the incident and learning from it to improve future responses (e.g., by identifying areas where the incident response process can be improved and by sharing lessons learned with other organizations); lessons learned stage is an all-encompassing view of the situation related to an incident, where personnel, including the IR team and other key stakeholders, examine the incident and the response to see if there are any lessons to be learned.

The output of this stage can be fed back to the detection stage of incident management.

It's common for the IR team to create a report when they complete a lessons learned review.

Based on the findings, the team may recommend changes to procedures, the addition of security controls, or even changes to policies. Management will decide what recommendations to implement and is responsible for the remaining risk for any recommendations they reject.

Incident management DOES NOT include a counterattack against the attacker.

### AI in this objective

**Adversarial AI incidents.** Investigate suspicious model behavior alongside application, identity, and data evidence. A bad answer alone does not identify its cause. Preserve relevant versions and records while limiting ongoing harm. [NIST adversarial ML taxonomy](https://csrc.nist.gov/News/2025/nist-ai-100-2-adversarial-machine-learning-taxonom).

### Apply this objective

**Question.** A compromised server has been restored from backup. Can Harbor declare recovery complete immediately?

**Reasoning.** First verify that the restored system is trustworthy, the entry point and persistence are addressed, required data and service levels are restored, and monitoring is in place. A working service may still be vulnerable to the same compromise.

<a id="objective-7-7"></a>

## 7.7 Operate and maintain detection and preventative measures

Defensive products provide different kinds of evidence and intervention. A firewall controls traffic, an intrusion detection system alerts on suspicious activity, and an intrusion prevention system can block selected activity. Sandboxes and deception systems expose behavior under controlled conditions, while anti-malware tools identify or restrict malicious code.

Their effectiveness depends on placement, visibility, configuration, updates, and response. Harbor should understand what each tool cannot see, how false positives are handled, and what happens when the tool fails. Multiple products with the same blind spot do not necessarily create useful defense in depth.

As noted in [Domain 1](CISSP-Domain-1-Content.md#objective-1-9), a preventive or preventative control is deployed to thwart or stop unwanted or unauthorized activity from occurring.

#### Examples

Fences. Locks. Biometrics. Separation of duties policies. Job rotation policies. Data classification. Access control methods. Encryption. Smart cards. Callback procedures. Security policies. Security awareness training. Antivirus software. Firewalls. Intrusion prevention systems.

A detective control is deployed to discover or detect unwanted or unauthorized activity; detective controls operate after the fact.

#### Examples

Security guards, guard dogs. Motion detectors. Recording and reviewing of events captured by security cameras. Job rotation policies. Mandatory vacation policies. Audit trails. Honeypots or honeynets. Intrusion detection systems. Violation reports. Supervision and reviews of users. Incident investigations.

#### Some preventative measures

Keep systems and applications up to date. Remove or disable unneeded services and protocols. Use intrusion detection and prevention systems. Use up-to-date antimalware software. Use firewalls. Implement configuration and system management processes.

<a id="subtopic-7-7-1"></a>

### 7.7.1 Firewalls (e.g. next generation, web application, network)

**View-Based access controls**: access control that allows the database to be logically divided into components like records, fields, or groups allowing sensitive data to be hidden from non-authorized users; admins can set up views by user type, allowing only access to assigned views. **Vendor Management System (VMS)**: software that assists with the management and procurement of staffing services, hardware, software, and other products and services. **Tuple**: tuple usually refers to a collection of values that represent specific attributes of a network connection or packet; these values are used to uniquely identify and manage network flows, as part of a state table or rule set in a firewall; as an example, a 5-tuple is as a bundle of five values that identify a specific connection or network session, which might include the sourced IP address, source port numbers, destination IP address, destination port number, and the specific protocol in use (e.g. TCP UDP).

**Trusted Computing Base (TCB)** is the collection of all hardware, software, and firmware components within an architecture that is specifically responsible for security and the isolation of objects that forms a trusted base.

TCB is a term that is usually associated with security kernels and the reference monitor. A trusted base enforces the security policy. A security perimeter is the imaginary boundary that separates the TCB from the rest of the system; TCB components communicate with non-TCB components using trusted paths. **Reference Monitor Concept (RMC)** is the logical part of the TCB that confirms whether a subject has the right to use a resource prior to granting access; based on three principles: Complete Mediation (all access must be validated by the Reference Monitor), Verifiability (the correct operation of the Reference monitor can be analyzed and verified), and Isolation (the Reference Monitor must be protected from unauthorized modification or tampering).

The security kernel is the collection of the TCB components that implement the functionality of the reference monitor.

**TCP Wrappers** is a host-based network access control system used in Unix-like operating systems to filter incoming connections to network services; allows administrators to define which IP addresses or hostnames are allowed or denied access to certain network services, such as SSH, FTP, or SMTP, by controlling access based on incoming TCP connections; TCP Wrappers relies on two config files: /etc/hosts.allow, and /etc/hosts.deny. **SWG (Secure Web Gateway)** is a security solution that filters and monitors internet traffic for organizations, ensuring that users can securely access the web while blocking malicious sites, preventing data leaks, and enforcing web browsing policies; while it is not a traditional firewall, it complements firewall functionality by focusing specifically on web traffic security.

**SCCM** is a system Center Configuration Manager is a Microsoft systems management software product that provides the capability to manage large groups of computers providing remote control, patch management, software distribution, operating system deployment, and hardware and software inventory. **RTBH (Remote Triggered Black Hole)** is a network security technique used in conjunction with firewalls and routers to mitigate Distributed Denial of Service (DDoS) attacks or unwanted traffic by dropping malicious or unwanted traffic before it reaches the target network; RTBH works by creating a "black hole route", where packets destined for a specific IP address are discarded or "dropped" by the network equipment, effectively isolating malicious traffic.

**Request For Change (RFC)**: documentation of a proposed change in support of change management activities. **Regression testing**: testing of a system to ascertain whether recently approved modifications have changed its performance, or if other approved functions have introduced unauthorized behaviors. **Netflow**: data that contains information on the source, destination, and size of all network communications and is routinely saved as a matter of normal activity; captures information about the parties involved in a communication and the amount of data exchanged. **MTTR**: mean time to repair is the average length of time required to perform a repair on the device.

**MTTF**: mean time to failure is the expected typical functional lifetime of the device given a specific operating environment. **Motion detector types**: wave pattern motion detectors transmit ultrasonic or microwave signals into the monitored area watching for changes in the returned signals bouncing off objects; infrared heat-based detectors watch for unusual heat patterns; capacitance detectors work based on electromagnetic fields. **Information Sharing and Analysis Center (ISAC)**: entity or collab created for the purposes of analyzing critical cyber and related information to better understand security problems and interdependencies to ensure CIA.

**Information Security Continuous Monitoring (ICSM)**: maintaining ongoing awareness of information security, vulnerabilities and threats to support organizational risk management decisions; ongoing monitoring sufficient to ensure and assure effectiveness of security controls. **Indicators of Compromise (IoC)** is a signal that an intrusion, malware, or other predefined hostile or hazardous set of events has or is occurring. **Hackback**: actions taken by a victim of hacking to compromise the systems of the alleged attacker. **Entitlement** refers to the privilege granted to users when an account is first provisioned. **DPI (Deep Packet Inspection)** is a method used by firewalls and other network security devices to examine the data portion (or payload) of packets as they pass through the firewall; DPI goes beyond traditional packet filtering by not only inspecting the header information (such as source/destination IP addresses and port numbers) but also analyzing the content within the packet to identify and respond to security threats.

**Configuration Item (CI)**: aggregation of information system components designated for configuration management and treated as a single entity in the config management process. **Computer crime**: law or regulation violation that is directed against, or directly involves a computer, grouped into six categories: military and intelligence attack, business attack, financial attack, terrorist attack, grudge attack, and thrill attack.

**Bastion host** is a special-purpose computer on a network specifically designed and configured to withstand attacks; it is typically placed in a demilitarized zone (DMZ) or exposed network segment, and its primary function is to act as a gateway between an internal network and external, potentially untrusted networks (like the internet); key characteristics of a Bastion host include:

Hardened security: minimizing the number of running services and applications which reduces potential attack surfaces. Publicly accessible: exposed to the internet or untrusted network, acting as the first point of contact for external users. Logging and monitoring: include extensive logging and monitoring to detect suspicious activity. Limited network access: typically has limited access to the internal network.

**Audit trail** is the records created by recording information about events and occurrences into one or more database or log files; they are used to reconstruct an event, extract information about an incident, and prove or disprove culpability; using audit trails is a passive form of detective security control and audit trails are essentially evidence in a criminal prosecution. **Alternate site**: contingency or Continuity of Operations (COOP) site used to assume system or organization operations, if the primary site is not available. **Allowed/Blocked listing**: allowed or blocked entities, register of entities that are being provided (or blocked) for a particular privilege, service, mobility, access or recognition including web, IP, geo, hardware address, files/programs; entities on the allowed list will be accepted, approved and/or recognized; deprecated AKA whitelist/blacklist; systems also alert IT security personnel an access attempt involves a resource not on a pre-approved list; can also incorporate anti-malware.

**Alarm types**: deterrent, repellent, and notification. Security operations is about safeguarding assets and includes core concepts like logging & monitoring, secure configuration and change management; keep due care and due diligence in mind as you traverse these topics; domain 7 has an exam weighting of ~13%. Firewalls are preventive and technical controls.

#### Types of firewalls

**Static Packet Filtering**: inspects individual packets based on predefined rules (such as IP address, port number, and protocol) without considering the connection state or the content of the data; simple and fast, but lacks context awareness. **Application-Level**: functions at the application layer (OSI:Layer 7), acts as an intermediary or proxy, inspecting traffic between the user and the service; can perform deep packet inspection, meaning it can analyze the contents of data packets to identify malicious content or enforce rules for specific applications (e.g., web, email); example: a web application firewall (WAF) inspects traffic going to a web server and can block malicious traffic such as SQL injection attacks and cross-site scripting (XSS) attacks.

**Circuit-Level Gateway Firewall**: works at the session layer (OSI:Layer 5), and monitors TCP handshakes (i.e., the connection establishment process) to ensure the validity of the session; once the session is validated, it allows the traffic to pass without further inspection of the content; circuit-level gateway firewalls have lower processing overhead, but lacks deep packet inspection. **Stateful Inspection Firewall** operates at the network and transport layers (Layers 3 and 4) but maintains a record of active connections (i.e., it tracks the state of traffic streams across the network); checks whether a packet belongs to an active, legitimate connection before allowing it through; offers better security than static packet filtering; lacks the ability to inspect data at the application layer.

**Next-Generation Firewall (NGFW)**: functions as a unified threat management (UTM) device and combines the features of traditional firewalls (like stateful inspection) with additional features such as deep packet inspection, intrusion prevention systems (IPS), and the ability to detect and block threats at the application layer; often incorporates advanced threat detection using techniques such as sandboxing and behavioral analysis; an NGFW inspects traffic at both the application and network layers, providing comprehensive security, including the ability to identify and block sophisticated threats, but is more expensive and resource-intensive.

**Internal Segmentation Firewall (ISFW)**: used within a network to segment internal traffic and control access between different parts of an organization; an ISFW monitors and filters traffic between network segments (such as between the finance department and HR), preventing lateral movement of threats within the network; provides internal protection by monitoring east-west traffic, reduces the risk of an insider threat or lateral movement, can enforce micro-segmentation, but can be complex to configure and manage.

| **Firewall Type**         | **OSI Layers**           | **Key Features**                                       | **Strengths**                                        | **Weaknesses**                                      |
|---------------------------|--------------------------|-------------------------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| **Static Packet Filtering**| Layer 3 (Network)        | Basic filtering on source/destination IPs and ports    | Fast, low overhead                                   | No context awareness, can't inspect data payload    |
| **Application-Level**      | Layer 7 (Application)    | Inspects application-level data                       | Deep inspection, blocks specific applications        | High processing overhead, slower performance        |
| **Circuit-Level**          | Layer 5 (Session)        | Validates session establishment                       | Low overhead, monitors session validity              | No payload inspection, can't detect deeper threats   |
| **Stateful Inspection**    | Layers 3-4 (Network, Transport) | Tracks connection states across sessions              | Better security than static filtering                | Doesn't inspect data at the application layer        |
| **NGFW**                   | Layers 3-7               | Combines stateful inspection with deep packet inspection, IPS, and application control | Comprehensive threat detection, application-aware   | Expensive, high resource usage                       |
| **ISFW**                   | Internal Segmentation    | Filters traffic between internal network segments     | Prevents lateral movement, enforces micro-segmentation | Complex configuration, typically for internal use   |

<a id="subtopic-7-7-2"></a>

### 7.7.2 Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS)

**Event**: observable occurrence in a network or system. Intrusion Detection Systems (IDSs) and Intrusion Prevention Systems (IPSs) are two methods organizations typically implement to detect and prevent attacks.

**Intrusion detection** is a specific form of monitoring events, usually in real time, to detect abnormal activity indicating a potential incident or intrusion.

Intrusion Detection System (IDS) automates the inspection of logs and real-time system events to detect intrusion attempts and system failures. IDSs are an effective method of detecting many DoS and DDoS attacks. An IDS actively watches for suspicious activity by monitoring network traffic and inspecting logs. An IDS is intended as part of a defense-in-depth security plan. **knowledge-based detection**: AKA signature-based or pattern-matching detection, the most common method used by an IDS. **behavior-based detection**: AKA statistical intrusion, anomaly, and heuristics-based detection; behavior-based IDSs use baseline, activity stats, and heuristic eval techniques to compare current activity against previous activity to detect potentially malicious events.

An IPS includes detection capabilities, you’ll see them referred to as intrusion detection and prevention systems (IDPSs).

An IPS includes all the capabilities of an IDS but can also take additional steps to stop or prevent intrusions.

IDS/IPS should be deployed at strategic network locations to monitor traffic, such as at the perimeters, or between network segments, and should be configured to alert for specific types of scans and traffic patterns.

See NIST SP 800-94.

<a id="subtopic-7-7-3"></a>

### 7.7.3 Whitelisting/blacklisting

Method used to control which applications run and which applications can’t is via allow list, and deny list (AKA whitelists and blacklists). Application whitelisting or allow listing is a security option prohibiting unauthorized software from executing; AKA deny by default or implicit deny. **Allow list** identifies a list of applications authorized to run on a system and blocks all other applications. **Deny list** identifies a list of applications that are not authorized to run on a system. Allow and deny lists are used for applications to help prevent malware infections.

A system can combine allow and block rules. Define precedence, default behavior, and exceptions explicitly to avoid unintended access. Apple iOS illustrates a controlled application-distribution environment, but available distribution routes depend on region, device management, and platform policy; do not assume a universal single-store rule.

<a id="subtopic-7-7-4"></a>

### 7.7.4 Third-party provided security services

Some organizations outsource security services such as auditing and penetration testing to third party security services. Some outside compliance entities (e.g. PCI DSS) require organizations to ensure that service providers comply. OSG also mentions that some SaaS vendors provide security services via the cloud (e.g. next-gen firewalls, UTM devices, and email gateways for spam and malware filtering).

<a id="subtopic-7-7-5"></a>

### 7.7.5 Sandboxing

**Sandboxing** refers to a security technique where a separate, secure environment is created to run and analyze untested or untrusted programs or code without risking harm to the host device or network; this isolated environment, known as a **sandbox**, effectively contains the execution of the code, allowing it to run and behave as if it were in a normal computing environment, but without the ability to affect the host system or access critical resources and data. **Confinement**: restriction of a process to certain resources, or reading from and writing to certain memory locations; bounds are the limits of memory a process cannot exceed when reading or writing;isolation is using bounds to create/enforce confinement.

Sandboxing provides a security boundary for applications and prevents the application from interacting with other applications; can be used as part of development, integration, or acceptance testing, as part of malware screening, or as part of a honeynet.

<a id="subtopic-7-7-6"></a>

### 7.7.6 Honeypots/honeynets

**Honeypots**: individual computers created as a trap or a decoy for intruders or insider threats; a honeypot typically has pseudo flaws and fake data to lure attackers. **Honeynet**: two or more networked honeypots used together to simulate a network; admins can observe attacker's activity while they are in a honeypot, keeping them occupied, instead of attacking the production network. They look and act like legit systems, but they do not host data of any real value for an attacker; admins often configure honeypots with vulnerabilities to tempt intruders into attacking them.

In addition to keeping the attacker away from a production environment, the honeypot allows administrators to observe an attacker’s activity without compromising the live environment.

<a id="subtopic-7-7-7"></a>

### 7.7.7 Anti-malware

**adware**: software that displays unwanted advertisements, sometimes bundled with spyware. **bot** is a compromised computer that is remotely controlled by an attacker via a command-and-control (C2) channel; also called a zombie. **bot herder**: someone who controls a botnet, using a command-and-control server to remotely control the zombies to launch attacks on other systems or send spam/phishing emails; bot herders can also rent botnet access out to other criminals. **botnet** is a collection of compromised computing devices (called bots or zombies), organized in a network controlled by a criminal known as a bot herder;  these many infected systems that have been harnessed together and act in unison.

**boot sector infectors**: pieces of malware that can install themselves in the boot sector of a drive. **companion**: helper software that is not malicious on its own; it could be something like a wrapper that accompanies the actual malware. **fileless malware**: leaves no trace of its presence nor saves itself to a storage device, but is still able to stay resident and active on a computer. **hoaxes/pranks**: not actually software, they're usually part of social engineering—via email or other means—that intends harm (hoaxes) or a joke (pranks).

**logic bomb**: malware inserted into a program which will activate and perform functions suiting the attacker when some later date/conditions are met; code that will execute based on some triggering event. **macro**: associated with Microsoft Office products, and is created using a straightforward programming language to automate tasks; macros can be programmed to be malicious and harmful. **Malware**: program inserted into a system with the intent of compromising the CIA of the victim's data, applications, or OS; malicious software that negatively impacts a system.

The most important protection against malicious code is the use of antimalware software with up-to-date signature files and heuristic capabilities.

Multi-pronged approach with antimalware software on each system in addition to filtering internet content helps protect systems from infections. Following the principle of least privilege, ensuring users do not have admin permissions on systems so they won't be able to install applications that may be malicious.

#### These are the characteristics of each malware type

**virus**: software written with the intent/capability to copy and disperse itself without direct owner knowledge/cooperation; the *defining characteristic is that it's a piece of malware that has to be triggered in some way by the user*; program that modifies other programs to contain a possibly altered version of itself.

**Viruses use four main propagation techniques**

File infection. Service injection. Boot sector infection. Macro infection.

**multipartite** means the malware spreads in different ways (e.g. Stuxnet). **polymorphic**: malware that can change aspects of itself as it replicates to evade detection (e.g. file name, file size, code structure etc). **ransom attack** is any form of attack which threatens the destruction, denial or unauthorized public release/remarketing of private information assets; usually involves encrypting assets and withholding the decryption key until a ransom is paid. **ransomware** is a type of malware that typically encrypts a system or a network of systems, effectively locking users out, and then demands a ransom payment (usually in the form of a digital currency) to gain access to the decryption key.

**rootkit**: Similar to stealth malware, a rootkit attempts to mask its presence on a system; malware that embeds itself deeply in an OS; term is derived from the concept of rooting and a utility kit of hacking tools; rooting is gaining total or full control over a system; typically includes a collection of malware tools that an attacker can utilize according to specific goals. **spyware**: software that secretly monitors and collects user information. **stealth**: malware that uses various active techniques to avoid detection. **trojan** is a Trojan horse is malware that looks harmless or desirable but contains malicious code; trojans are often found in easily downloadable software; a trojan inserts backdoors or trapdoors into other programs or systems.

**worm**: software written with the intent/capability to copy and disperse without owner knowledge/cooperation, but without needing to modify other programs to contain copies of itself; malware that can self-propagate and spread through a network or a series of systems on its own by exploiting a vulnerability in those systems. A **zero-day** vulnerability is a weakness for which defenders lack an available effective fix at the relevant time, often before public disclosure or vendor remediation. A zero-day exploit uses such a weakness; unfamiliar malware is not automatically a zero-day.

<a id="subtopic-7-7-8"></a>

### 7.7.8 Machine learning and Artificial Intelligence (AI) based tools

**AI**: gives machines the ability to do things that a human can do better or allows a machine to perform tasks that we previously thought required human intelligence.

**Machine Learning** is a subset of AI and refers to a system that can improve automatically through experience.

An ML system starts with a set of rules or guidelines; ML techniques attempt to algorithmically discover knowledge from datasets. Both ML and AI require training data, but the level of human-defined structure differs.

Behavior-based detection is one way ML and AI can apply to cybersecurity.

An admin relates a baseline of normal activities and traffic on a network; the baseline in this case is similar to a set of rules given to a ML system. During normal operations, it detects anomalies and reports them; if the detection is a false positive (incorrectly classifying a benign activity, system state, or configuration as malicious or vulnerable), the ML system learns.

An AI system starts without a baseline, monitors traffic and slowly creates its own baseline based on the traffic it observes.

As it creates the baseline it also looks for anomalies. An AI system also relies on feedback from admins to learn if alarms are valid or false positives.

**Neural networks**: try to simulate the functioning of the human brain by arranging a series of layered calculations to solve problems; neural networks require extensive training on a particular problem before they are able to offer solutions. **Expert systems** is a branch of AI that uses knowledge-based systems to emulate the decision-making ability of human experts; expert systems have two main components: a knowledge base that uses a series of if/then rules, and an inference engine that harnesses that information to draw conclusions about other data.

### AI in this objective

**AI in operations.** Security Orchestration, Automation and Response (SOAR) can combine AI-assisted correlation with response workflows to reduce alert fatigue. [ISC2 AI guidance, Domain 7](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

Original application: Harbor can have a tool summarize related alerts for an analyst before granting it authority to disable accounts. Evaluate missed events and incorrect actions as well as time saved, and provide a practical override.

### Apply this objective

**Question.** Harbor installs an intrusion prevention system but leaves it without maintained rules or response ownership. What is the problem?

**Reasoning.** A product installation is not an operational control by itself. Assign maintenance, tuning, health monitoring, exception handling, and response responsibility, then verify that the deployed control detects or prevents the intended activity.

<a id="objective-7-8"></a>

## 7.8 Implement and support patch and vulnerability management

Vulnerability management is a continuing process of discovery, evaluation, treatment, and verification. Patching is one treatment, but configuration changes, isolation, replacement, or accepted exceptions may be needed. Priorities should reflect exploitability, exposure, affected assets, and business impact.

Harbor must balance the risk of leaving a weakness with the operational risk of change. Test where feasible, establish recovery options, deploy through an authorized process, and confirm the result. An emergency does not remove the need to record what changed.

**Vulnerability Management**: activities necessary to identify, assess, prioritize, and remediate information systems weaknesses.

Vulnerability management includes routine vuln scans and periodic vuln assessments.

Vuln scanners can detect known security vulnerabilities and weaknesses, like the absence of patches or weak passwords. Vuln scanners generate reports that indicate the technical vulnerabilities of a system and are an effective check for a patch management program. Vuln assessments extend beyond just technical scans and can include review and audits to detect vulnerabilities.

Patch and vulnerability management processes work together to help protect an organization against emerging threats; patch management ensures that appropriate patches are applied, and vuln management helps verify that systems are not vulnerable to known threats.

**Patch**: (AKA updates, quick or hot fixes) a blanket term for any type of code written to correct bug or vulnerability or to improve existing software performance; when installed, a patch directly modifies files or device settings without changing the version number or release details of the related software component.

In the context of security, admins are primarily concerned with security patches, which are patches that affect a system’s vulnerabilities.

**Patch Management**: systematic notification, identification, deployment, installation and verification of OS and application code revisions known as patches, hot fixes, and service packs.

An effective patch management program ensures that systems are kept up to date with current patches by evaluating, testing, approving, and deploying appropriate patches.

**Patch Tuesday**: several big-tech organizations (e.g. Microsoft, Adobe, Oracle etc) regularly release patches on the second Tuesday of every month. Patch management is often intertwined with change and configuration management, ensuring that documentation reflects changes; when an organization doesn't have an effective patch management program, it can experience outages and incidents from known issues that could have been prevented.

#### There are three methods for determining patch levels

Agent: update software (agent) installed on devices. Agentless: remotely connect to each device. Passive: monitor traffic to infer patch levels. Deploying patches can be done manually or automatically.

#### Common steps within an effective program

Evaluate patches: determine if they apply to your systems. Test patches: test patches on an isolated, non-production system to determine if the patch causes any unwanted side effects. Approve the patches: after successful testing, patches are approved for deployment; it’s common to use Change Management as part of the approval process. Deploy the patches: after testing and approval, deploy the patches; many organizations use automated methods to deploy patches, via third-party or the software vendor. Verify that patches are deployed: regularly test and audit systems to ensure they remain patched.

Regularly identifying vulnerabilities, evaluating them, and taking steps to mitigate risks associated with them. It isn’t possible to eliminate risks, and it isn’t possible to eliminate all vulnerabilities. A vuln management program helps ensure that an organization is regularly evaluating vulnerabilities and mitigating those that represent the greatest risk. One of the most common vulnerabilities within an organization is an unpatched system, and so a vuln management program will often work in conjunction with a patch management program.

### Apply this objective

**Question.** A critical patch cannot yet be applied to a production system. Is ignoring the finding until the next release acceptable?

**Reasoning.** No. Evaluate compensating protections, assign ownership, document the exception and residual risk, and set a review or remediation date. Track whether exposure or available fixes change.

<a id="objective-7-9"></a>

## 7.9 Understand and participate in change management processes

Change management makes alterations deliberate, traceable, and recoverable. A request should describe the purpose, affected systems, security and business impact, testing, implementation steps, rollback, and approval. Review the result to catch unintended consequences.

Emergency changes may use an expedited route, but should still have defined authority and later review. At Harbor, a rushed access-rule change can restore one service while exposing another; impact analysis should consider dependencies rather than only the immediate symptom.

**Change management**: formal process an organization uses to transition from the current state to a future state; typically includes mechanisms to request, evaluate, approve, implement, verify, and learn the change; ensures that the costs and benefits of changes are analyzed and changes are made in a controlled manner to reduce risks.

Change management processes allow various IT experts to review proposed changes for unintended consequences before implementing. Change management controls provide a process to control, document, track, and audit all system changes.

The change management process includes multiple steps that build upon each other:

Change request: a change request can come from any part of an organization and pertain to almost any topic; companies typically use some type of change management software. Assess impact: after a change request is made, however small the request might be, the impact of the potential change must be assessed. Approval/reject: based on the requested change and related impact assessment, common sense plays a big part in the approval process. Build and test: after approval, any change should be developed and tested, ideally in a test environment.

Schedule/notification: prior to implementing any change, key stakeholders should be notified. Implement: after testing and notification of stakeholders, the change should be implemented; it's important to have a roll-back plan, allowing personnel to undo the change. Validation: once implemented, senior management and stakeholders should again be notified to validate the change. Document the change: documentation should take place at each step; it's critical to ensure all documentation is complete and to identify the version and baseline related to a given change.

When a change management process is enforced, it creates documentation for all changes to a system, providing a trail of information if personnel need to reverse the change, or make the same change on other systems. Change management control is a mandatory element for some security assurance requirements (SARs) in the ISO Common Criteria.

### Apply this objective

**Question.** An urgent firewall change restores a customer connection. What should follow?

**Reasoning.** Verify that the intended connection works and that unintended access was not introduced, document the change and approval, and complete the emergency review. Preserve a rollback route if the broader effects prove unacceptable.

<a id="objective-7-10"></a>

## 7.10 Implement recovery strategies

Recovery strategies provide the resources needed to meet business recovery objectives. Backups preserve recoverable data; alternate sites provide a place to operate; redundancy and fault tolerance reduce some interruptions. These mechanisms solve related but different problems.

A replicated error or malicious deletion can affect several live copies, so replication does not replace recoverable backups. Harbor should compare strategies against RTO, RPO, dependency recovery, cost, and credible common failures.

**Recovery strategy** is a plan for restoring critical business components, systems, and operations following a disruption. **Disaster recovery (DR)** is a set of practices that enable an organization to minimize loss of, and restore, mission-critical technology infrastructure after a catastrophic incident. **Business continuity (BC)** is a set of practices that enables an organization to continue performing its critical functions through and after any disruptive event.

<a id="subtopic-7-10-1"></a>

### 7.10.1 Backup storage strategies (e.g., cloud storage, onsite, offsite)

**Backup**: copies of files or programs to facilitate recovery. Backup strategies are driven by organization goals and objectives and usually focus on backup and restore time as well as storage needs; the goal is to determine how and where data is stored for recovery in case of data loss, corruption, or disaster.

#### 3-2-1 rule

3 copies of critical files. 2 backups on different media. 1 backup stored offsite.

Onsite backup: storing backup data within the same location as the source data (AKA local backup); onsite backups have the downside that if through some disaster you lose your source data, there is a chance you could also lose your backup. Offsite backup: storing backup data at a different location from where the original data is stored; the offsite location should be geographically remote from, or far enough away from the source data that a single disaster doesn't compromise both. Cloud backup: storing backup data in the cloud, with the advantages of storage scalability, high availability, and you pay only for what you use.

**Archive bit**: technical detail (metadata) that indicates the status of a backup relative to a given backup strategy.

0 = file has been backed up (no new changes); 1 = file has been modified since last backup (needs to be backed up).

Different backup strategies deal with the archive bit differently; Incremental and differential backup strategies don't treat the archive bit in the same manner.

Once a full backup is complete, the archive bit on every file is reset, turned off, or set to 0.

#### Three types of backups

**Full backup**: store a complete copy of the data contained on the protected device or backup media; full backups duplicate every file on the system regardless of the setting of the archive bit.

**Incremental backup**: backs up only data that has changed since the last backup (whether full or incremental).

Only files that have the archive bit turned on, enabled, or set to 1 are duplicated. Once an incremental backup is complete, the archive bit on all duplicated files is reset, turned off, or set to 0.

#### Differential backup: changes since the last full backup

Only files that have the archive bit turned on, enabled, or set to 1 are duplicated. Unlike full and incremental backups, the differential backup process does not change the archive bit.

The most important difference between incremental and differential backups is the time needed to restore data in the event of an emergency.

A combination of full and differential backups will require only two backups to be restored: the most recent full backup and the most recent differential backup. A combination of full backups with incremental backups will require restoration of the most recent full backups as well as all incremental backups performed since that full backup. Differential backups don’t take as long to restore, but they take longer to create than incremental.

Grandfather/Father/Son, Tower of Hanoi, and Six Cartridge Weekly are all different approaches to rotating backup media, balancing media reuse with data retention concerns.

Grandfather/Father/Son (GFS): three or more backup cycles, such as daily, weekly and monthly; the daily backups are rotated on a 3-months basis using a FIFO system, the weekly backups are similarly rotated on a bi-yearly basis, and the monthly backup on a yearly basis. Tower of Hanoi: based on the puzzle of the same name, where the first backup is overwritten every other day, the second backup is overwritten every fourth day, and the third backup is overwritten every other day at a different increment than the first backup.

Six Cartridge Weekly: a method that involves six different media (cartridge, tape, drives etc) used for each day of the week; many small businesses that do not need to backup high volumes of data use this type of tape rotation schedule, and usually consists of using four media for incremental and differential backups between Monday and Thursday.

Backup storage best practices include keeping copies of the media in at least one offsite location to provide redundancy should the primary location be unavailable, incapacitated, or destroyed; common strategy is to store backups in a cloud service that is itself geographically redundant.

#### Two common backup strategies

Full backup on Monday night, then run differential backups every other night of the week.

If a failure occurs Saturday morning, restore Monday’s full backup and then restore only Friday’s differential backup.

Full backup on Monday night, then run incremental backups every other night of the week.

If a failure occurs Saturday morning, restore Monday’s full backup and then restore each incremental backup in the original chronological order.

| Feature    | Full Backup  | Incremental Backup | Differential Backup |
|---------------|------------------|-----------------------|--------------|
| **Description**  | A complete copy of all selected data  | Only backs up data that has changed since the last backup (regardless of type) | Backs up all changes made since the last full backup |
| **Storage Space**     | Requires the most storage space                     | Requires the least storage space                    | Requires more space than incremental but less than full |
| **Backup Speed**      | Slowest, as it copies all data                      | Fastest, as it only copies changed data since the last backup | Faster than full but slower than incremental, as it copies all changes since the last full backup |
| **Recovery Speed**    | Fastest, as all data is in one place                | Slowest, as it may require multiple incremental backups to restore to a specific point | Faster than incremental since it requires the last full backup and the last differential backup |
| **Complexity**        | Simplest, with no dependency on previous backups    | Complex, as it depends on a chain of backups from the last full backup to the most recent incremental backup | Less complex than incremental, requires the last full backup and the last differential backup for restoration |
| **Best Use Case**     | When backup time and storage space are not issues Ideal for less frequent backups | Suitable for environments where daily changes are minimal and quick backups are necessary | Ideal for environments where storage space is a concern but restoration time needs to be relatively quick |

Three main techniques used to create offsite copies of database content: electronic vaulting, remote journaling, and remote mirroring.

**electronic vaulting**: where database backups are moved to a remote site using bulk transfers. **remote journaling**: data transfers are performed in a more expeditious manner; remote journaling is similar to electronic vaulting in that transaction logs transferred to the remote site are not applied to a live database server but are maintained in a backup device. **remote mirroring** is the most advanced db backup solution, and the most expensive, with remote mirroring, a live db server is maintained at the backup site; the remote server receives copies of the db modifications at the same time they are applied to the production server at the primary site.

<a id="subtopic-7-10-2"></a>

### 7.10.2 Recovery site strategies (e.g., cold vs. hot, resource capacity agreements)

**Resource capacity agreement**: used to make sure the appropriate resources will be available in a recovery scenario. **Disruption**: unplanned event that causes a system to be inoperable for a length of time. Non-disaster: service disruption with significant but limited impact. **Disaster**: event that causes an entire site to be unusable for a day or longer (usually requires alternate processing facility). **Natural disaster**: events that commonly threaten organizations including earthquakes, floods, storms, fires, tsunamis, and volcanic eruptions. **Human-caused disasters**: explosions, electrical fires, terrorist acts, power outages and other utility failures, hardware/software failures, labor difficulties, theft, vandalism, etc.

Catastrophe: major disruption that destroys the facility altogether.

For disasters and catastrophes, an organization has 3 basic options: use a dedicated site that the organization owns/operates; lease a commercial facility (hot, warm, cold site); enter into a formal agreement with another facility/organization.

When a disaster interrupts a business, a disaster recovery plan should kick in nearly automatically and begin providing support for recovery operations.

In addition to improving your response capabilities, purchasing insurance can reduce the impact of financial losses.

Recovery site strategies consider multiple elements of an organization, such as people, data, infrastructure, and cost, as well as factors like availability and location.

When designing a disaster recovery plan, it’s important to keep your goal in mind — the restoration of workgroups to the point that they can resume their activities in their usual work locations.

Sometimes it's best to develop separate recovery facilities for different work groups.

To recover your business operations with the greatest possible efficiency, you should engineer the disaster recovery plan so that those business units with the highest priority are recovered first.

**Mutual Assistance Agreements (MAA)**: provide an inexpensive alternative to disaster recovery sites; *not commonly used* because they are difficult to enforce; organizations participating in an MAA may also be shut down by the same disaster, and MAAs raise confidentiality concerns. **Resource Capacity Agreements**: pre-arranged vendor agreements to secure the necessary resources required after a disruptive event; the goal is to ensure an organization has access to resources at a recovery site.

<a id="subtopic-7-10-3"></a>

### 7.10.3 Multiple processing sites

Building fully resilient recovery processes means including alternative processing sites for disaster recovery scenarios; multiple processing sites increase geographic diversity as well as resilience to calamitous events.

One of the most important elements of the disaster recovery plan is the selection of alternate processing sites to be used when the primary sites are unavailable.

**cold sites**: standby facilities large enough to handle the processing load of an organization and equipped with appropriate electrical and environmental support systems.

A cold site has NO COMPUTING FACILITIES (hardware or software) preinstalled. A cold site has no active broadband comm links.

**Advantages**

A cold site is the LEAST EXPENSIVE OPTION and perhaps the most practical.

**Disadvantages**

Tremendous lag to activate the site, often measured in weeks, which can yield a false sense of security. Difficult to test.

**warm sites** is a warm site is better than a cold site because, in addition to the shell of a building, basic equipment is installed.

A warm site contains the data links and pre-configured equipment necessary to begin restoring operations, but no usable data for information. Unlike hot sites, however, warm sites do not typically contain copies of the client’s data. Activation of a warm site typically takes at least 12 hours from the time a disaster is declared.

**hot sites** is a fully operational offsite data processing facility equipped with hardware and software; a backup facility that is maintained in constant working order, with a full complement of servers, workstations, and comm links.

A hot site is usually a subscription service. The data on the primary site servers is periodically or continuously replicated to corresponding servers at the hot site, ensuring that the hot site has up-to-date data.

**Advantages**

Unsurpassed level of disaster recovery protection.

**Disadvantages**

Extremely costly, likely doubling an organization’s budget for hardware, software and services, and requires the use of additional employees to maintain the site. Has (by definition) copies of all production data, and therefore increases your attack surface.

**Mobile sites**: non-mainstream alternatives to traditional recovery sites; usually configured as cold or warm sites, if your DR plan depends on a workgroup recovery strategy, mobile sites are an excellent way to implement that approach.

Cloud computing: many organizations now turn to cloud computing as their preferred disaster recovery option.

Some companies that maintain their own datacenters may choose to use these IaaS options as backup service providers.

A hot site is a subscription service, while a redundant site, in contrast, is a site owned and maintained by the organization (and a redundant site may be "hot" in terms of capabilities).

The exam differentiates between a hot site (a subscription service) and a redundant site (owned by the organization).

Cloud computing: organizations increasingly are turning to cloud computing (often via IaaS) as their preferred disaster recovery option.

<a id="subtopic-7-10-4"></a>

### 7.10.4 System resilience, High Availability (HA), Quality of Service (QoS), and fault tolerance

**System resilience** is the ability of a system to maintain an acceptable level of service during an adverse event.

**High Availability (HA)** is the use of redundant technology components to allow a system to quickly recover from a failure after experiencing a brief disruption.

**Clustering** refers to a group of systems working together to handle workloads; often seen in the context of web servers that use a load balancer to manage incoming traffic, and distributes requests to multiple web servers (the cluster).

**Redundancy**: unlike a cluster, where all members work together, redundancy typically involves a primary and secondary system; the primary system does all the work, and the secondary system is in standby mode unless the primary system fails, at which time activity can fail over to the secondary.

Both clustering and redundancy include high availability as a by-product of their configuration.

**Quality of Service (QoS)** controls protect the availability of data networks under load.

Many factors contribute to the quality of the end-user experience and QoS attempts to manage all of these factors to create an experience that meets business requirements.

**Factors contributing to QoS**

Bandwidth: the network capacity available to carry communications. Latency: the time it takes a packet to travel from source to destination. Packet loss: some packets may be lost between source and destination, requiring re-transmission. Interference: electrical noise, faulty equipment, and other factors may corrupt the contents of packets.

**Fault tolerance** is the ability of a system to suffer a fault but continue to operate.

**Redundant array of independent disks (RAID)** refers to multiple drives being used in unison in a system to achieve greater speed or availability; the most well-known RAID levels are:

RAID 0—Striping: provides significant speed, writing and reading advantages. RAID 1—Mirroring: uses redundancy to provide reliable availability of data. RAID 5—Parity Protection: requires a minimum of three drives and provides a cost-effective balance between RAID 0 and RAID 1; RAID 5 utilizes a parity bit, computed from an XOR operation, for purposes of storing and restoring data. RAID 6—Double Parity: similar to RAID 5 but uses two parity blocks, allowing two drives to fail simultaneously without data loss; requires a minimum of four drives. RAID 10—Mirroring and Striping: requires a minimum of four drives and provides the benefits of striping (speed) and mirroring (availability) in one solution; this type of RAID is typically one of the most expensive.

| Backup Method | Cost Implications                                                          | Time Implications for RPO                      |
|---------------|----------------------------------------------------------------------------|-----------------------------------------------|
| Incremental   | Lower cost due to reduced storage requirements as only changes are backed up | Longer recovery time as it requires the last full backup plus all subsequent incremental backups until the RPO |
| Differential  | Moderate cost; more storage is needed than incremental, but less than full, as it stores all changes since the last full backup | Faster recovery than incremental as it requires the last full backup and the last differential backup up to the RPO |
| Replication   | Higher cost due to the need for a duplicate environment ready to take over at any time; continuous data replication can also increase bandwidth costs | Minimal recovery time as the data is continuously updated, allowing for near-instant recovery up to the latest point before failure |
| Clustering    | Highest cost because it involves multiple servers (cluster) working together to provide high availability and redundancy | Minimal recovery time as the system is designed for immediate failover without data loss, ensuring the RPO can be met instantaneously |

| Site Recovery Method | Cost Implications                                                                 | Time Implications for RTO                         |
|----------------------|-----------------------------------------------------------------------------------|---------------------------------------------------|
| Cold Site            | Lowest cost option; facilities and infrastructure are available, but equipment and data need to be set up post-disaster | Longest recovery time as systems and data must be configured and restored from backups Suitable for non-critical applications with more flexible RTOs |
| Warm Site            | Moderate cost; a compromise between cold and hot sites, includes some pre-installed hardware and connectivity that can be quickly activated | Faster recovery than a cold site as the infrastructure is partially ready, but data and systems might still need updates to be fully operational |
| Hot Site             | High cost; a duplicate of the original site with full computer systems and near-real-time replication of data and ready to take over operations immediately | Minimal recovery time, designed for seamless takeover with data and systems up-to-date, allowing for critical operations to continue with little to no downtime |
| Redundant Site       | Highest cost; essentially operates as an active-active configuration where both sites are running simultaneously, fully mirroring each other | Instantaneous recovery, as the redundant site is already running in parallel with the primary site, ensuring no interruption in service |

### Apply this objective

**Question.** Harbor has two synchronized databases. Does that eliminate the need for backups?

**Reasoning.** No. Synchronization can copy corruption or unwanted deletion to both systems. Recovery needs protected historical copies and a tested restoration method, in addition to any availability architecture.

<a id="objective-7-11"></a>

## 7.11 Implement Disaster Recovery (DR) processes

A disaster recovery plan translates the recovery strategy into assigned work. It identifies activation criteria, authority, people, communication methods, assessment steps, restoration order, and validation. Infrastructure dependencies often need restoration before the visible business application.

A plan must work when ordinary communication and facilities are unavailable. Harbor should make necessary contacts and instructions accessible through appropriate alternate means and train people in their responsibilities.

**Business Continuity Management (BCM)** is the process and function by which an organization is responsible for creating, maintaining, and testing BCP and DRP plans. **Business Continuity Planning (BCP)** focuses on the survival of the business processes when something unexpected impacts it.

**Disaster Recovery Planning (DRP)** focuses on the recovery of vital technology infrastructure and systems.

BCM, BCP, and DRP are ultimately used to achieve the same goal: the continuity of the business and its critical and essential functions, processes, and services.

#### The key BCP/DRP steps are

Develop contingency planning policy. Conduct BIA. Identify controls. Create contingency strategies. Develop contingency plan. Ensure testing, training, and exercises. Maintenance.

As part of the Business Impact Analysis (BIA), four key measurements for BCP and DRP procedures:

**RPO (recovery point objective)**: max tolerable data loss measured in time. **RTO (recovery time objective)**: max tolerable time to recover systems to a defined service level; specifies the amount of time that business continuity planners find acceptable for the restoration of a service after a disaster. **WRT (work recovery time)**: max time available to verify system and data integrity as part of the resumption of normal ops. **MTD (max tolerable downtime)**: max time-critical system, function, or process can be disrupted before unacceptable/irrecoverable consequences to the business.

<a id="subtopic-7-11-1"></a>

### 7.11.1 Response

A disaster recovery plan should contain simple yet comprehensive instructions for essential personnel to follow immediately upon recognizing that a disaster is in progress or imminent. Emergency-response plans are often put together in a form of checklists provided to responders; arrange the checklist tasks in order of priority, with the most important task first! The response plan should include clear criteria for activation of the disaster recovery plan, define who has the authority to declare a disaster, and then discuss notification procedures.

<a id="subtopic-7-11-2"></a>

### 7.11.2 Personnel

A disaster recovery plan should contain a list of personnel to contact in the event of a disaster.

Usually includes key members of the DRP team as well as critical personnel.

Businesses need to make sure employees are trained on DR procedures and that they have the necessary resources to implement the DR plan.

Key activities involved in preparing people and procedures for DR include: develop DR training programs; conduct regular DR drills; provide employees with necessary resources and tools to implement the DR plan; communicate the DR plan to all employees.

<a id="subtopic-7-11-3"></a>

### 7.11.3 Communications (e.g., methods)

Ensure that response checklists provide first responders with a clear plan to protect life and property and ensure the continuity of operations.

The notification checklist should be supplied to all personnel who might respond to a disaster. The information provided should include alternate means of contact (e.g. mobile or alternate, pagers etc) as well as backup contacts for each role.

<a id="subtopic-7-11-4"></a>

### 7.11.4 Assessment

When the disaster recovery team arrives, one of their first priorities is to assess the situation; initial responders perform a quick assessment to triage the incident and begin the response, followed by more detailed evaluations to measure effectiveness and prioritize resources as the situation evolves.

<a id="subtopic-7-11-5"></a>

### 7.11.5 Restoration

Recovery and restoration are separate concepts. **Restoration**: bringing a business facility and environment back to a workable state. **Recovery**: bringing business operations and processes back to a working state. System recovery includes the restoration of all affected files and services actively in use on the system at the time of the failure or crash. When designing a disaster recovery plan, it’s important to keep your goal in mind — the restoration of workgroups to the point that they can resume their activities in their usual work locations.

<a id="subtopic-7-11-6"></a>

### 7.11.6 Training and awareness

As with a business continuity plan, it is essential that you provide training to all personnel who will be involved in the disaster recovery effort.

#### When designing a training plan consider the following

Orientation training for all new employees. Initial training for employees taking on a new DR role for the first time. Detailed refresher training for DR team members. Brief awareness refreshers for all other employees.

<a id="subtopic-7-11-7"></a>

### 7.11.7 Lessons learned

**Precursor**: signal from events suggesting a possible change of conditions, that may alter the current threat landscape. **Indicator**: technical artifact or observable occurrence suggesting that an attack is imminent, currently underway, or already occurred. A lessons learned session should be conducted at the conclusion of any disaster recovery operation or other security incident. The lessons learned process is designed to provide everyone involved with the incident response effort an opportunity to reflect on their individual roles and the team's overall response. Time is of the essence in conducting a lesson learned, before memories fade.

Usually a lessons learned session is led by trained facilitators.

NIST SP 800-61 offers a series of questions to use in the lessons learned process:

Exactly what happened and at what times? How well did staff and management perform in dealing with the incident? Were documented procedures followed? Were the procedures adequate? Were any steps or actions taken that might have inhibited the recovery? What would the staff and management do differently the next time a similar incident occurs? How could information sharing with other organizations have been improved? What corrective actions can prevent similar incidents in the future? What precursors or indicators should be watched for in the future to detect similar incidents?

What additional tools or resources are needed to detect, analyze, and mitigate future incidents? The team leader to document the lessons learned in a report that includes suggested process improvement actions.

### Apply this objective

**Question.** Harbor restores its portal servers before restoring the identity and network services they require. Why does the portal remain unavailable?

**Reasoning.** Recovery order ignored dependencies. The plan should identify prerequisites and validate the complete service, rather than count recovered machines as recovered business capability.

<a id="objective-7-12"></a>

## 7.12 Test Disaster Recovery Plans (DRP)

Recovery exercises provide evidence without always requiring a real outage. A document review can reveal missing information; a tabletop explores decisions; a walkthrough or simulation exercises coordination; parallel and interruption tests provide different levels of operational realism and risk.

Choose the exercise to answer a question, state success criteria, control the risks, and capture improvements. Harbor should progress toward evidence that its recovery objectives are achievable, rather than repeat the easiest exercise indefinitely.

Every DR plan must be tested on a periodic basis to ensure that the plan’s provisions are viable and that it meets an organization’s changing needs.

#### Five main test types

Read-through/checklist tests. Structured walk-throughs. Simulation tests. Parallel tests. Full-interruption tests.

<a id="subtopic-7-12-1"></a>

### 7.12.1 Read-through/tabletop

**Read-through test** is one of the simplest to conduct, but also one of the most critical; copies of a DR plan are distributed to the members of the DR team for review, accomplishing three goals:

Ensure that key personnel are aware of their responsibilities and have that knowledge refreshed periodically. Provide individuals with an opportunity to review and update plans, removing obsolete info. Helps identify situations in which key personnel have left the company and the DR responsibility needs to be re-assigned (note that DR responsibilities should be included in job descriptions).

**Tabletop** is an exercise where disaster recovery team members and key stakeholders gather together and talk through how they would respond to a disaster scenario, without actually disrupting systems or operation.

<a id="subtopic-7-12-2"></a>

### 7.12.2 Walkthrough

**Walk-through** can vary in scope, but in general, a walkthrough is a disaster recovery exercise that is more hands-on; it is a procedural test where participants follow the disaster recovery plan to verify that the process and tasks are accurate, complete, and workable.

<a id="subtopic-7-12-3"></a>

### 7.12.3 Simulation

**Simulation tests**: similar to the walk-throughs, where team members are presented with a scenario and asked to develop an appropriate response.

Unlike a read-through and walk-through, some of these response measures are then tested. This may involve the interruption of noncritical business activities and the use of some operational personnel.

<a id="subtopic-7-12-4"></a>

### 7.12.4 Parallel

**Parallel tests**: represent the next level, and involve relocating personnel to the alternate recovery site and implementing site activation procedures.

The relocated employees perform their DR responsibilities just as they would for an actual disaster. Operations at the main facility are not interrupted.

<a id="subtopic-7-12-5"></a>

### 7.12.5 Full interruption

**Full-interruption tests**: operate like parallel tests, but involve actually shutting down operations at the primary site and shifting them to the recovery site.

These tests involve a significant risk (shutting down the primary site, transfer recovery ops, followed by the reverse) and therefore are extremely difficult to arrange (management resistance to these tests is likely). The full interruption test proves that the disaster recovery plan actually works.

<a id="subtopic-7-12-6"></a>

### 7.12.6 Communications (e.g., stakeholders, test status, regulators)

Before starting DRP testing, it's important to inform all stakeholders on what to expect, including scheduled timing, potential impacts, the goals of testing. During testing it's important to provide regular updates, especially for larger full-interruption testing, ensuring that stakeholders are aware of progress, challenges, and end-time changes. Post-test debriefing sessions can be used to review outcomes, looking at successes and areas that need improvement. Many industries with stringent regulations require specific DR testing plans, and keeping regulators informed is important for compliance as well as governance.

### Apply this objective

**Question.** A tabletop goes smoothly. Does that prove a four-hour technical recovery target is achievable?

**Reasoning.** No. It supports confidence in discussion and coordination, but actual restoration time requires suitable technical evidence. Plan an appropriately controlled test that measures the needed recovery capability.

<a id="objective-7-13"></a>

## 7.13 Participate in Business Continuity (BC) planning and exercises

Business continuity sustains essential activities, which may require workarounds while technology recovers. It includes people, facilities, suppliers, communications, and priorities. Disaster recovery supports continuity by restoring technical services, but a restored server does not alone resume every business process.

Harbor might temporarily accept requests through a controlled alternate channel. The workaround needs capacity, privacy protection, staff training, and a method for reconciling records when normal service resumes.

Business continuity planning addresses how to keep an organization in business after a major disruption takes place.

It's important to note that the scope is much broader than that of DR. A security leader will likely be involved, but not necessarily lead the BCP effort.

#### The four primary BCP steps are

Project scope and planning. Business Impact Analysis (BIA). Continuity planning. Plan approval and implementation.

### Apply this objective

**Question.** The portal is unavailable, but staff can take requests by phone. What must the continuity plan address?

**Reasoning.** Define staffing, verification, record protection, prioritization, and later reconciliation, along with limits on what can be done safely. A workaround is a business process with its own risks.

<a id="objective-7-14"></a>

## 7.14 Implement and manage physical security

Physical security operations keep designed safeguards effective. Entrances, barriers, cameras, badges, guards, visitor procedures, and restricted rooms need inspection, maintenance, and response. A control that exists on a drawing but is routinely bypassed offers little protection.

Harbor should examine how employees and visitors actually move through the facility. Delivery routes, emergency exits, and maintenance access can create gaps if their operation is not part of the plan.

Physical access control mechanisms deployed to control, monitor and manage access to a facility.

Sections, divisions, or areas within a site should be clearly designated as public, private, or restricted with appropriate signage.

<a id="subtopic-7-14-1"></a>

### 7.14.1 Perimeter security controls

#### A fence is a perimeter-defining device and can consist of

Stripes painted on the ground. Chain link fences. Barbed wire. Concrete walls. Invisible perimeters using laser, motion, or heat detection. **Perimeter intrusion detection and assessment system (PIDAS)** is an advanced form of fencing that has two or three fences used in concert to optimize security; the space between the fences can serve as a corridor for guard patrols or wandering guard dogs; one or more fences can support touch detection capabilities; an exterior fence is used to keep animals and casual trespassers from accessing the main fence, which reduces the nuisance alarm rate (NAR) or false positives.

**Gate**: controlled exit and entry point in a fence or wall. **Turnstile** is a form of gate that prevents more than one person at a time from gaining entry and often restricts movement in one direction. **Access control vestibule**: (AKA mantrap) a double set of doors that is often protected by a guard or other physical layout preventing piggybacking and can trap individuals at the discretion of security personnel. **Security bollards** is a key element of physical security, which prevent vehicles from ramming access points and entrances.

**Barricades**: in addition to fencing, are used to control both foot traffic and vehicles. Lighting is the most commonly used form of perimeter security control providing the security benefit of deterrence (primary purpose is to discourage casual intruders, trespassers etc). Security guards are able to adapt and react to conditions and situations; guard dogs can be an alternative for perimeter control, functioning as detection and deterrent. All physical security controls ultimately rely on personnel to intervene and stop actual intrusions and attacks. KPIs (key performance indicators) of physical security are metrics or measurements of the operation of or failure of key security aspects; they should be monitored, recorded, and evaluated.

<a id="subtopic-7-14-2"></a>

### 7.14.2 Internal security controls

In all circumstances and under all conditions, the most important aspect of security is protecting people. Internal security controls include locks, badges, protective distribution systems (PDSs), motion detectors, intrusion alarms, and secondary verification systems.

If a facility is designed with restricted areas to control physical security, a mechanism to handle visitors is required.

**Visitor logs**: manual (or automated) list of non-employee entries or access to a facility/location.

Physical access logs can establish context for interpretation of logical logs.

Locks: designed to prevent access without proper authorization; a lock is a crude form of an identification and authorization mechanism.

### Apply this objective

**Question.** Staff prop open a controlled door because deliveries are inconvenient. What is a useful response?

**Reasoning.** Restore the control and address the delivery process that encouraged bypassing it. Combine practical procedures, training, and monitoring so the intended protection remains usable in daily work.

<a id="objective-7-15"></a>

## 7.15 Address personnel safety and security concerns

Personnel safety takes priority in an emergency. Travel, duress, social engineering, harassment, and physical hazards require preparation and clear reporting routes. Security measures should help people obtain assistance rather than leave them uncertain about whom to contact.

For Harbor, awareness includes recognizing suspicious authentication prompts and requests for information, while emergency procedures identify evacuation, accountability, and communication responsibilities. A plan should work for the people and locations it covers.

<a id="subtopic-7-15-1"></a>

### 7.15.1 Travel

Training personnel on safe practices while traveling can increase their safety and prevent security incidents:

Sensitive data: devices traveling with the employee shouldn’t contain sensitive data. Malware and monitoring devices: possibilities include physical devices being installed in a hotel room of a foreign country. Free wi-fi: sounds appealing but can be a used to capture a user's traffic. VPNs: employers should have access to VPNs that they can use to create secure connections.

<a id="subtopic-7-15-2"></a>

### 7.15.2 Security training and awareness (e.g., insider threat, social media impacts, two-factor authentication (2FA) fatigue)

Organizations should add personnel safety and security topics to their training and awareness program and help ensure that personnel are aware of duress systems, travel best practices, emergency management plans, and general safety and security best practices. Training programs should stress the importance of protecting people. Insider threats: employees should be educated on the risks of access or misuse of company data by employees, contractors or business partners, highlighting signs of potential insider threats and methods for reporting suspicious behavior. Social media impacts: educate employees on risks of oversharing on social platforms e.g. potential for social engineering attacks that use publicly available info.

2FA/MFA fatigue: educate employees about MFA fatigue attacks, where attackers send repeated push notifications hoping the user will approve one; employees should be trained to never approve MFA prompts they did not initiate, and to report unexpected prompts immediately.

<a id="subtopic-7-15-3"></a>

### 7.15.3 Emergency management

Emergency management plans and practices help an organization address personnel safety and security after a disaster. Safety of personnel should be a primary consideration during any disaster.

<a id="subtopic-7-15-4"></a>

### 7.15.4 Duress

An example of a duress system is a button that sends a distress call. Duress systems allow guards to raise alarms in response to emergencies, and for emergency management plans help the organization respond to disasters. Duress systems are useful when personnel are working alone. If a duress system is activated accidentally, code word(s) can be used to assure responding personnel it was an accident, or omit the word(s) keying an actual response.

Also see Understanding CISSP Domain 7, Security Operations - [part 1](https://blog.balancedsec.com/p/understanding-cissp-domain-7-security), and [part 2](https://blog.balancedsec.com/p/understanding-cissp-domain-7-security-79d) on the source author's blog, [The Cyber Leader](https://blog.balancedsec.com/) (note that some articles require a subscription).

### Apply this objective

**Question.** An employee receives repeated unexpected authentication approval requests. What should the employee do?

**Reasoning.** Do not approve an uninitiated request. Use the organization's reporting route so the team can investigate possible credential compromise, protect the account, and address the attempt to exploit approval fatigue.

## Chapter review

Return to the Harbor examples and explain each decision without looking at the answer. Identify the asset or business activity, the relevant requirement, the possible harm, the responsible owner, and the evidence that would support the decision. If two controls appear interchangeable, explain the different failure each addresses.

### Connections and common distinctions

Backups support recovery; replication supports other availability goals and may propagate errors. Incident response, disaster recovery, and business continuity overlap but are not identical. Operational priorities should trace back to Domain 1's requirements and Domain 2's data rules.

### Review questions and explained answers

**1. How would you explain this domain to Harbor's service owner?** Describe the decisions it governs using the examples in this chapter. A useful answer connects technical measures to customer service, accountability, and evidence rather than listing product names.

**2. Which assumption in the chapter's examples would most change your recommendation if it were false?** Choose a concrete assumption, such as data sensitivity, allowed downtime, or an identity's authority. Explain how a different assumption changes the relevant control or test. More than one answer can be sound when justified.

**3. How does adding the AI assistant change the work?** Follow the AI lessons in this chapter. Identify an additional asset, failure, or decision and describe its owner and verification method. The assistant still operates within ordinary governance, access, data, and recovery requirements.

### AI application review

**Question.** The assistant's answers deteriorate while the SOC automation disables several legitimate users. What should Harbor examine?

**Reasoning.** Investigate model performance changes and possible adversarial activity, preserve relevant evidence, and limit ongoing harm. Review the SOAR workflow, correlation inputs, and authority granted to automation. Reducing alert fatigue is useful only if the process still detects important events and avoids unacceptable response errors.

## Term index

This index points to explanations in the chapter. Terms retain the source guide's spelling where useful for recognition; corrected concepts are explained in context.

- [Access control vestibule](#subtopic-7-14-1)
- [accurate](#subtopic-7-1-1)
- [actions on objectives](#subtopic-7-2-6)
- [administrative](#objective-7-1)
- [admissible](#subtopic-7-1-1)
- [Adversarial AI incidents](#objective-7-6)
- [adware](#subtopic-7-7-7)
- [AI](#subtopic-7-7-8)
- [AI in operations](#objective-7-7)
- [Alarm types](#subtopic-7-7-1)
- [Allow list](#subtopic-7-7-3)
- [Allowed/Blocked listing](#subtopic-7-7-1)
- [Alternate site](#subtopic-7-7-1)
- [Analysis](#objective-7-6)
- [Application-Level](#subtopic-7-7-1)
- [Archive bit](#subtopic-7-10-1)
- [Audit trail](#subtopic-7-7-1)
- [authentic](#subtopic-7-1-1)
- [Backup](#subtopic-7-10-1)
- [Backup Speed](#subtopic-7-10-1)
- [Barricades](#subtopic-7-14-1)
- [Baseline](#objective-7-3)
- [Bastion host](#subtopic-7-7-1)
- [Behavior-based detection](#subtopic-7-2-7)
- [behavior-based detection](#subtopic-7-7-2)
- [best evidence rule](#subtopic-7-1-1)
- [Best Use Case](#subtopic-7-10-1)
- [boot sector infectors](#subtopic-7-7-7)
- [bot](#subtopic-7-7-7)
- [bot herder](#subtopic-7-7-7)
- [botnet](#subtopic-7-7-7)
- [Business continuity (BC)](#objective-7-10)
- [Business Continuity Management (BCM)](#objective-7-11)
- [Business Continuity Planning (BCP)](#objective-7-11)
- [chain of custody](#subtopic-7-1-1)
- [Change management](#objective-7-9)
- [Circuit-Level](#subtopic-7-7-1)
- [Circuit-Level Gateway Firewall](#subtopic-7-7-1)
- [circumstantial evidence](#subtopic-7-1-1)
- [civil](#objective-7-1)
- [Clipping](#subtopic-7-1-1)
- [Clustering](#subtopic-7-10-4)
- [cold sites](#subtopic-7-10-3)
- [Collusion](#subtopic-7-4-2)
- [command and control](#subtopic-7-2-6)
- [companion](#subtopic-7-7-7)
- [complete](#subtopic-7-1-1)
- [Complexity](#subtopic-7-10-1)
- [Computer crime](#subtopic-7-7-1)
- [Configuration Item (CI)](#subtopic-7-7-1)
- [Configuration Management (CM)](#objective-7-3)
- [Confinement](#subtopic-7-7-5)
- [Containment](#objective-7-6)
- [convincing](#subtopic-7-1-1)
- [corroborative evidence](#subtopic-7-1-1)
- [criminal](#objective-7-1)
- [Cyber forensics](#subtopic-7-1-1)
- [Cyber Kill Chain](#subtopic-7-2-6)
- [delivery](#subtopic-7-2-6)
- [demonstrated evidence](#subtopic-7-1-1)
- [Deny list](#subtopic-7-7-3)
- [Description](#subtopic-7-10-1)
- [Detection](#subtopic-7-6-1)
- [Differential backup](#subtopic-7-10-1)
- [direct evidence](#subtopic-7-1-1)
- [Disaster](#subtopic-7-10-2)
- [Disaster recovery (DR)](#objective-7-10)
- [Disaster Recovery Planning (DRP)](#objective-7-11)
- [Disruption](#subtopic-7-10-2)
- [DPI (Deep Packet Inspection)](#subtopic-7-7-1)
- [Dynamic techniques](#subtopic-7-2-7)
- [eDiscovery(E-Discovery)](#subtopic-7-1-4)
- [Egress monitoring](#subtopic-7-2-4)
- [electronic vaulting](#subtopic-7-10-1)
- [Entitlement](#subtopic-7-7-1)
- [Entity](#subtopic-7-2-7)
- [Eradication](#objective-7-6)
- [Event](#subtopic-7-7-2)
- [Expert systems](#subtopic-7-7-8)
- [exploitation](#subtopic-7-2-6)
- [false negatives](#subtopic-7-2-3)
- [false positives](#subtopic-7-2-3)
- [Fault tolerance](#subtopic-7-10-4)
- [fileless malware](#subtopic-7-7-7)
- [Firewall Type](#subtopic-7-7-1)
- [Full backup](#subtopic-7-10-1)
- [Full-interruption tests](#subtopic-7-12-5)
- [Gate](#subtopic-7-14-1)
- [Hackback](#subtopic-7-7-1)
- [Hardening a system](#objective-7-3)
- [hearsay evidence](#subtopic-7-1-1)
- [Heuristics](#subtopic-7-2-7)
- [High Availability (HA)](#subtopic-7-10-4)
- [hoaxes/pranks](#subtopic-7-7-7)
- [Honeynet](#subtopic-7-7-6)
- [Honeypots](#subtopic-7-7-6)
- [hot sites](#subtopic-7-10-3)
- [how much](#subtopic-7-4-1)
- [Human-caused disasters](#subtopic-7-10-2)
- [Incident](#subtopic-7-6-2)
- [Incident response (IR)](#objective-7-6)
- [Incremental backup](#subtopic-7-10-1)
- [Indicator](#subtopic-7-11-7)
- [Indicators of Compromise (IoC)](#subtopic-7-7-1)
- [Information Security Continuous Monitoring (ICSM)](#subtopic-7-7-1)
- [Information Sharing and Analysis Center (ISAC)](#subtopic-7-7-1)
- [installation](#subtopic-7-2-6)
- [Internal Segmentation Firewall (ISFW)](#subtopic-7-7-1)
- [Intrusion](#subtopic-7-2-1)
- [Intrusion detection](#subtopic-7-2-1)
- [Intrusion Detection System (IDS)](#subtopic-7-2-1)
- [Intrusion Prevention Systems (IPS)](#subtopic-7-2-1)
- [Investigation](#objective-7-1)
- [ISFW](#subtopic-7-7-1)
- [Job rotation](#subtopic-7-4-4)
- [Key Features](#subtopic-7-7-1)
- [Kill chain](#subtopic-7-2-6)
- [knowledge-based detection](#subtopic-7-7-2)
- [Lessons Learned](#subtopic-7-6-7)
- [Live evidence](#subtopic-7-1-4)
- [Locard exchange principle](#objective-7-1)
- [Log](#subtopic-7-2-5)
- [Log analysis](#subtopic-7-2-3)
- [Log management](#subtopic-7-2-5)
- [logic bomb](#subtopic-7-7-7)
- [Machine Learning](#subtopic-7-7-8)
- [macro](#subtopic-7-7-7)
- [Malware](#subtopic-7-7-7)
- [Media management](#subtopic-7-5-1)
- [Memorandum of Understanding (MOU)](#subtopic-7-4-5)
- [Mitigation](#subtopic-7-6-3)
- [Mobile sites](#subtopic-7-10-3)
- [Model drift](#objective-7-2)
- [Monitoring](#subtopic-7-2-3)
- [Motion detector types](#subtopic-7-7-1)
- [MTBF](#subtopic-7-5-1)
- [MTD (max tolerable downtime)](#objective-7-11)
- [MTTF](#subtopic-7-7-1)
- [MTTR](#subtopic-7-7-1)
- [multipartite](#subtopic-7-7-7)
- [Mutual Assistance Agreements (MAA)](#subtopic-7-10-2)
- [Natural disaster](#subtopic-7-10-2)
- [Netflow](#subtopic-7-7-1)
- [Neural networks](#subtopic-7-7-8)
- [Next-Generation Firewall (NGFW)](#subtopic-7-7-1)
- [NGFW](#subtopic-7-7-1)
- [OSI Layers](#subtopic-7-7-1)
- [Parallel tests](#subtopic-7-12-4)
- [parol evidence rule](#subtopic-7-1-1)
- [Patch](#objective-7-8)
- [Patch Management](#objective-7-8)
- [Patch Tuesday](#objective-7-8)
- [Perimeter intrusion detection and assessment system (PIDAS)](#subtopic-7-14-1)
- [Playbook](#subtopic-7-2-2)
- [polymorphic](#subtopic-7-7-7)
- [Precursor](#subtopic-7-11-7)
- [Preparation](#objective-7-6)
- [primary evidence](#subtopic-7-1-1)
- [Privileged Account Management (PAM)](#subtopic-7-4-3)
- [Provisioning](#objective-7-3)
- [Quality of Service (QoS)](#subtopic-7-10-4)
- [ransom attack](#subtopic-7-7-7)
- [ransomware](#subtopic-7-7-7)
- [Read-through test](#subtopic-7-12-1)
- [real evidence](#subtopic-7-1-1)
- [reconnaissance](#subtopic-7-2-6)
- [Recovery](#subtopic-7-6-5)
- [Recovery Speed](#subtopic-7-10-1)
- [Recovery strategy](#objective-7-10)
- [Redundancy](#subtopic-7-10-4)
- [Redundant array of independent disks (RAID)](#subtopic-7-10-4)
- [Reference Monitor Concept (RMC)](#subtopic-7-7-1)
- [Regression testing](#subtopic-7-7-1)
- [regulatory](#objective-7-1)
- [Remediation](#subtopic-7-6-6)
- [remote journaling](#subtopic-7-10-1)
- [remote mirroring](#subtopic-7-10-1)
- [Request For Change (RFC)](#subtopic-7-7-1)
- [Resource capacity agreement](#subtopic-7-10-2)
- [Resource Capacity Agreements](#subtopic-7-10-2)
- [Restoration](#subtopic-7-11-5)
- [rollover logging](#subtopic-7-2-5)
- [Root Cause Analysis](#subtopic-7-6-6)
- [rootkit](#subtopic-7-7-7)
- [RPO (recovery point objective)](#objective-7-11)
- [RTBH (Remote Triggered Black Hole)](#subtopic-7-7-1)
- [RTO (recovery time objective)](#objective-7-11)
- [Runbook](#subtopic-7-2-2)
- [Sampling](#subtopic-7-1-1)
- [sandbox](#subtopic-7-7-5)
- [Sandboxing](#subtopic-7-7-5)
- [SCCM](#subtopic-7-7-1)
- [secondary evidence](#subtopic-7-1-1)
- [Security bollards](#subtopic-7-14-1)
- [Security Incident](#subtopic-7-6-1)
- [Security Orchestration, Automation, and Response (SOAR)](#subtopic-7-2-2)
- [Segregation of Duties (SoD)](#subtopic-7-4-2)
- [Service Level Agreement (SLA)](#subtopic-7-4-5)
- [Simulation tests](#subtopic-7-12-3)
- [Split knowledge](#subtopic-7-4-2)
- [spyware](#subtopic-7-7-7)
- [Stateful Inspection](#subtopic-7-7-1)
- [Stateful Inspection Firewall](#subtopic-7-7-1)
- [Static code scanning techniques](#subtopic-7-2-7)
- [Static Packet Filtering](#subtopic-7-7-1)
- [stealth](#subtopic-7-7-7)
- [Storage Space](#subtopic-7-10-1)
- [Strengths](#subtopic-7-7-1)
- [Structured Threat Information eXpression (STIX)](#subtopic-7-2-6)
- [SWG (Secure Web Gateway)](#subtopic-7-7-1)
- [System resilience](#subtopic-7-10-4)
- [Tabletop](#subtopic-7-12-1)
- [TCP Wrappers](#subtopic-7-7-1)
- [Threat feed](#subtopic-7-2-6)
- [Threat hunting](#subtopic-7-2-6)
- [Threat intelligence](#subtopic-7-2-6)
- [trojan](#subtopic-7-7-7)
- [Trusted Automated eXchange of Intelligence Information (TAXII)](#subtopic-7-2-6)
- [Trusted Computing Base (TCB)](#subtopic-7-7-1)
- [Tuning](#subtopic-7-2-3)
- [Tuple](#subtopic-7-7-1)
- [Turnstile](#subtopic-7-14-1)
- [Two-person control](#subtopic-7-4-2)
- [UEBA (aka UBA)](#subtopic-7-2-7)
- [Vendor Management System (VMS)](#subtopic-7-7-1)
- [View-Based access controls](#subtopic-7-7-1)
- [virus](#subtopic-7-7-7)
- [Visitor logs](#subtopic-7-14-2)
- [Vulnerability Management](#objective-7-8)
- [Walk-through](#subtopic-7-12-2)
- [warm sites](#subtopic-7-10-3)
- [Weaknesses](#subtopic-7-7-1)
- [weaponization](#subtopic-7-2-6)
- [what](#subtopic-7-4-1)
- [worm](#subtopic-7-7-7)
- [WRT (work recovery time)](#objective-7-11)
- [zero-day](#subtopic-7-7-7)

## Sources and further reading

- [Original Domain 7 objectives and notes](../CISSP-Domain-7-2024+Objectives.md) by the repository's contributors; adapted under the repository license.
- [ISC2 CISSP exam outline and AI domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).
- [ISC2 AI guidance announcement](https://www.isc2.org/Insights/2026/04/ISC2-Publishes-Exam-Guidance-AI).
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

Additional references appear alongside the relevant concepts. Official Study Guide chapter references in the original objective files remain available for comparison.
