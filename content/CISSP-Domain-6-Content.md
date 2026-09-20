<a id="domain-6"></a>

# Domain 6: Security Assessment and Testing

Exam weight: 12%. Study edition: September 2026.

## Start here

Security assessment and testing asks whether a control really meets its requirement. You will learn to plan an evaluation, select methods, collect useful evidence, interpret findings, and support audits. The central skill is making a conclusion that is no broader than the evidence supporting it.

This chapter follows the published Domain 6 objectives. Read the opening explanation of each objective first, then the detailed lessons, and finish with its application check. Three-part numbers identify subtopics retained from the source guide. The examples use Harbor Services, a small organization launching a customer portal and an AI support assistant.

Artificial intelligence (AI) is the broad field of systems performing tasks associated with intelligence. Machine learning (ML) builds models from examples during training; inference uses a trained model to produce an output. A large language model (LLM) produces language using learned numerical parameters called model weights. These terms identify components and processes to protect, rather than establish that a system is correct or trustworthy.

The AI additions apply [ISC2's domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline) to existing objectives. Detailed placement and Harbor scenarios are editorial teaching choices. Named historical technologies remain useful for comparison; their inclusion is not a recommendation to deploy them.

## Chapter navigation

- [6.1 Design and validate assessment, test, and audit strategies](#objective-6-1)
- [6.2 Conduct security controls testing](#objective-6-2)
- [6.3 Collect security process data (e.g. technical and administrative)](#objective-6-3)
- [6.4 Analyze test output and generate report](#objective-6-4)
- [6.5 Conduct or facilitate security audits](#objective-6-5)

<a id="objective-6-1"></a>

## 6.1 Design and validate assessment, test, and audit strategies

An assessment evaluates a security question using evidence. Testing exercises behavior under defined conditions. An audit evaluates against criteria with an appropriate degree of independence. Decide the purpose, scope, authority, methods, and audience before collecting results.

Harbor might test its own configuration, commission an external assessment, and review a supplier's assurance report. Each provides a different perspective. A report is useful only if its systems, period, criteria, exceptions, and customer responsibilities match the decision being made.

Security audits assess controls against defined criteria and may be internal or external. Independence should be appropriate to the engagement.

<a id="subtopic-6-1-1"></a>

### 6.1.1 Internal (e.g., within organization control)

**Statistical Sampling** is a process of selecting subsets of examples from a population with the objective of estimating properties of the total population. **SCE**: Script Check Engine is designed to make scripts interoperable with security policy definitions. **Plan of Action and Milestones (POA&M)** is a document identifying tasks to be accomplished, including details, resources, milestones, and completion target dates. **Judgement Sampling**: AKA purposive or authoritative sampling, a non-probability sampling technique where members are chosen only on the basis of the researcher's knowledge and judgement. **ITSM**: IT Service Management tools include change management and associated approval tracking.

**IAM system**: identity and access management system combines lifecycle management and monitoring tools to ensure that identity and authorization are properly handled throughout an organization. **Functional order of controls**: deter, deny, detect, delay, determine, and decide. **Examination** is a process of reviewing/inspecting/observing/studying/analyzing specs/mechanisms/activities to understand, clarify, or obtain evidence. **Compliance Calendar**: tracks an organization's audits, assessments, required filings, due dates and related. **Artifact** is a piece of evidence such as text, or a reference to a resource which is submitted in response to a question.

Security management needs to perform a variety of activities to properly oversee the information security program.

Log reviews, especially for admin activities, ensure that systems are not misused. Account management reviews ensure that only authorized users have access to information and systems. Backup verification ensures that the organization's data protection process is working properly. Key performance and risk indicators provide a high-level view of security program effectiveness.

An organization’s audit strategy will depend on its size, industry, financial status and other factors.

A small non-profit, a small private company and a small public company will have different requirements and goals for their audit strategies. The audit strategy should be assessed and tested regularly to ensure that the organization is not doing a disservice to itself with the current strategy. There are three types of audit strategies: internal, external, and third-party.

An organization’s security staff can perform security tests and assessments, and the results are meant for internal use only, designed to evaluate controls with an eye toward finding potential improvements.

An internal audit strategy should be aligned to the organization’s business and day-to-day operations.

E.g. a publicly traded company will have a more rigorous internal auditing strategy than a privately held company.

Designing the audit strategy should include laying out applicable regulatory requirements and compliance goals. Internal audits are performed by an organization’s internal audit staff and are typically intended for internal audiences, and management use.

<a id="subtopic-6-1-2"></a>

### 6.1.2 External (e.g., outside organization control)

An external audit strategy should complement the internal strategy, providing regular checks to ensure that procedures are being followed and the organization is meeting its compliance goals.

#### External audits are performed by an outside auditing firm

These audits have a high degree of external validity because the auditors performing the assessment theoretically have no conflict of interest with the organization itself. Audits by these firms are generally considered acceptable by most investors and governing bodies. Third-party audit reporting is generally intended for the organization's governing body.

<a id="subtopic-6-1-3"></a>

### 6.1.3 Third-party (e.g., outside of enterprise control)

**Trust Services Criteria (TSC)**: used by an auditor when evaluating the suitability of the design and operating effectiveness of controls relevant to the security, availability, or processing integrity of information and systems or the confidentiality or privacy of the information processed by the entity. **Audit** is a process of reviewing a system for compliance against a standard or baseline (e.g. audit of security controls, baselines, financial records) can be formal and independent, or informal/internal. Third-party audits are conducted by, or on behalf of, another organization. In the case of a third-party audit, the organization initiating the audit generally selects the auditors and designs the scope of the audit.

The statement on **Standards for Attestation Engagements document 18 (SSAE 18)**, titled Reporting on Controls, provides a common standard to be used by auditors performing assessments of service organizations with the intent of allowing the organization to conduct external assessments, instead of multiple third-party assessments, and then sharing the resulting report with customers and potential customers.

Outside of the US, similar engagements are conducted under the International Standard for Attestation Engagements (ISAE) 3402, Assurance Reports on Controls at a Service Organization.

SSAE 18 and ISAE 3402 engagements are commonly referred to as a service organization controls (SOC) audits.

#### Three forms of SOC audits

**SOC 1 Engagements**: assess the organization’s controls that might impact the accuracy of financial reporting.

**SOC 2 Engagements**: assess the organization’s controls that affect the security and privacy of information stored in a system.

SOC 2 focuses on 5 **Trust Services Criteria (TSC)**: Security, Availability, Confidentiality, Processing Integrity, and Privacy. SOC 2 audit results are confidential and are usually only shared outside an organization under an NDA.

**SOC 3 Engagements**: assess the organization’s controls that affect the security (confidentiality, integrity, and availability) and privacy information stored in a system.

However, SOC3 audit results are intended for public disclosure; they are regarded primarily as marketing tools.

#### Two types of SOC reports

**Type I Reports**: provide the auditor’s opinion on the description provided by management and the suitability of the design of the controls.

Type I reports cover only a specific point in time, rather than an extended period. Think of Type I report as more of a documentation review.

**Type II Reports**: go further and also provide the auditor’s opinion on the operating effectiveness of the controls.

The auditor actually confirms the controls are functioning properly. Type II reports cover a specified period and evaluate operating effectiveness during that period. There is no universal six-month minimum inherent in the term Type II; inspect the actual coverage dates. [AICPA SOC resources](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services). Think of Type II report as similar to a traditional audit; the auditor is checking the paperwork, and verifying the controls are functioning properly.

Type I reports evaluate design at a specified date; Type II reports also examine operating effectiveness over a period. Both involve an auditor's work. Select the report appropriate to the assurance question and inspect exceptions. [AICPA SOC resources](https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services). **Exam tip** is a type I = point-in-time snapshot of control design; Type II = extended-period evaluation of control design AND operating effectiveness.

<a id="subtopic-6-1-4"></a>

### 6.1.4 Location (e.g., on-premise, cloud, hybrid)

On-premise assessment: focuses on evaluating the security measures and infrastructure of in-house systems, or within an organization's physical data centers and facilities. Cloud assessment: focus is on assessing the security of data and applications hosted in cloud service provider's environment. Hybrid assessment: assess connectivity and security measures used between on-premise and cloud resources; this assessment looks at data flow or interconnection and integration security controls.

### Apply this objective

**Question.** A supplier provides a report about a service Harbor does not use. Does it establish assurance for Harbor's service?

**Reasoning.** No. Check the report's scope, period, criteria, and relevant controls. Assurance about one service cannot automatically be transferred to another merely because the supplier has the same name.

<a id="objective-6-2"></a>

## 6.2 Conduct security controls testing

Control testing compares expected behavior with observed behavior. A vulnerability assessment looks for weaknesses; a penetration test attempts exploitation within authorized boundaries. Software tests, log reviews, simulations, and physical inspections can reveal different failures, so select a method that answers the question.

Coverage describes what was exercised, not proof that nothing can fail. A test can touch every code statement yet miss an important sequence or authorization condition. Record assumptions, limitations, evidence, and enough detail for a finding to be reproduced.

Security control testing can include testing of the physical facility, logical systems and applications; common testing methods include the following.

<a id="subtopic-6-2-1"></a>

### 6.2.1 Vulnerability assessment

**Testing** is a process of exercising one or more assessment objects (activities or mechanisms) under specified conditions to compare actual to expected behavior. **Substantive Test**: testing technique used by an auditor to obtain the audit evidence in order to support the auditor's opinion. **RoE**: Rules of Engagement, set of rules/constraints/boundaries that establish limits of participant activity; in ethical pen testing, an RoE defines the scope of testing, and to establish liability limits for both testers and the sponsoring organization or system owners. **Penetration Testing/Ethical Penetration Testing**: security testing and assessment where testers actively attempt to circumvent a system's security features; typically constrained by contracts to stay within specified Rules of Engagement (RoE).

**Mutation testing**: mutation testing modifies a program in small ways and then tests that mutant to determine if it behaves as it should or if it fails; technique is used to design and test software through mutation.

**Fuzzing** uses modified inputs to test software performance under unexpected circumstances.

Mutation (dumb) fuzzing modifies known inputs to generate synthetic inputs that may trigger unexpected behavior. Generational (intelligent) fuzzing develops inputs based on models of expected inputs to perform the same task.

**Findings**: results created by the application of an assessment procedure. **Compliance Tests** is an evaluation that determines if an organization's controls are being applied according to management policies and procedures. **Code testing suite**: usually used to validate function, statement, branch and condition coverage. **Chaos Engineering**: discipline of experiments on a software system in production to build confidence in the system's capabilities to withstand turbulent/unexpected conditions. **Assessment**: testing or evaluation of controls to understand which are implemented correctly, operating as intended and producing the desired outcome in meeting the security or privacy requirements of a system or organization.

Software testing provides evidence about behavior under tested conditions; it cannot prove that all security flaws are absent. Security assessment and testing include a variety of tools, such as vulnerability assessments, penetration tests, software testing, audits, and other control validation; every organization should have a security assessment and testing program defined and operational. Security assessment and testing programs are an important mechanism for validating the on-going effectiveness of security controls; this domain accounts for ~12% of the exam. **Vulnerabilities**: weaknesses in systems and security controls that might be exploited by a threat.

**Vulnerability assessments**: examining systems for these weaknesses; steps in the assessment:

Reconnaissance: passively gather publicly available info. Enumeration: active network discovery (i.e. find target IP address and ports). Vulnerability Analysis: Identify potential vulnerabilities to be exploited. Execution: attempt to exploit vulnerabilities; applies only if you are doing a penetration test. Document Findings: reporting on findings and severity.

The goal of a vulnerability assessment is to identify elements in an environment that are not adequately protected -- and not necessarily from a technical perspective; you can also assess the vulnerability of physical security or the external reliance on power, for instance.

Can include personnel testing, physical testing, system and network testing, and other facilities tests.

Vulnerability assessments are some of the most important testing tools in the information security professional’s toolkit.

**Security Content Automation Protocol (SCAP)** provides a common framework and suite of specifications that standardize how software flaws and security configuration is communicated both to machines and humans; provides discussion and facilitation of automation of interactions between different security systems (see [NIST 800-126](https://csrc.nist.gov/pubs/sp/800/126/r3/final)).

#### SCAP components related to vulnerability assessments

**Common Vulnerabilities and Exposures (CVE)** provides a naming system for describing security vulnerabilities. **Common Vulnerability Scoring Systems (CVSS)** provides a standardized scoring system for describing the severity of security vulnerabilities; it includes metrics and calc tools for exploitability, impact, how mature exploit code is, and how vulnerabilities can be remediated, and a means to score vulnerabilities against users' unique requirements. **Common Configuration Enumeration (CCE)** provides a naming system for system config issues. **Common Platform Enumeration (CPE)** provides a naming system for operating systems, applications, and devices.

**eXtensible Configuration Checklist Description Format (XCCDF)** provides a language for specifying security checklists. **Open Vulnerability and Assessment Language (OVAL)** provides a language for describing security testing procedures; used to describe the security condition of a system.

Vulnerability scans automatically probe systems, applications, and networks looking for weaknesses that could be exploited by an attacker.

Flaws may include missing patches, misconfigurations, or faulty code.

#### Four main categories of vulnerability scans

Network discovery scans. Network vulnerability scans. Web application vulnerability scans. Database vulnerability scans.

**Authenticated scans**: (AKA credentialed security scan) involves conducting vulnerability assessments and security checks on a network, system, or application using valid credentials; this approach enables the scanner to simulate the actions of an authenticated user, allowing it to access deeper layers of the target system, gather more information, and provide a more accurate assessment of vulnerabilities; often uses a read-only account to access configuration files.

<a id="subtopic-6-2-2"></a>

### 6.2.2 Penetration testing (e.g., red, blue, and/or purple team exercises)

Penetration tests go beyond vulnerability testing techniques because they attempt to exploit systems.

**Vulnerability management** is the cyclical process of identifying, classifying, prioritizing, and mitigating vulnerabilities; programs take the results of the tests as inputs and then implement a risk management process for identified vulnerabilities, with the following steps: Asset inventory; Identifying the value of each asset; Identifying the vulnerabilities for each asset; Ongoing review and assessment.

Testing stages: see steps in the assessment in 6.2.1 above.

NIST defines the penetration testing process as consisting of four phases:

**planning** includes agreement on the scope of the test and the rules of engagement.

Ensures that both the testing team and management are in agreement about the nature of the test and that it is explicitly authorized.

**information gathering and discovery** uses manual and automated tools to collect information about the target environment.

Basic reconnaissance (website mapping); network discovery; testers probe for system weaknesses using network, web and db vuln scans.

**attack**: seeks to use manual and automated exploit tools to attempt to defeat system security.

Step where pen testing goes beyond vuln scanning as vuln scans don’t attempt to actually exploit detected vulnerabilities.

**reporting**: summarizes the results of the pen testing and makes recommendations for improvements to system security.

#### Tests are normally categorized into three groups

#### White-box penetration test

AKA "**known environment tests**". White box provides the attackers with **detailed information** about the systems they target. This bypasses many of the reconnaissance steps that normally precede attacks, shortening the time of the attack and increasing the likelihood that it will find security flaws. In white-box testing, the tester has access to the source code and performs testing from a developer's perspective.

#### Gray-box penetration test

AKA **partial knowledge tests**, these are sometimes chosen to balance the advantages and disadvantages of white- and black-box penetration tests. This is particularly common when black-box results are desired but costs or time constraints mean that some knowledge is needed to complete the testing. These tests are sometimes called "**partially known environment**" tests. In gray-box testing, the tester evaluates software from a user perspective but has access to the source code.

#### Black-box penetration test

AKA "**unknown environment tests**". Does not provide attackers with any information prior to the attack. This simulates an external attacker trying to gain access to information about the business and technical environment before engaging in an attack.

Differences between vulnerability assessments and pen tests: vuln assessments are usually more automated, can be performed quickly, and no attempt is made to exploit vulnerabilities.

Red, blue and purple teams have been around for a long time, and are becoming more popular.

Red team: this is the in-house offensive security team, they are the simulated hackers or the threat providing: offensive security; ethical hacking; penetration testing; social engineering; threat intelligence.

Blue team: the blue team is the in-house defensive team, working to stop the threat: defensive security; security monitoring; incident response; digital forensics; security operations.

Purple: not a separate team, but purple represents the collaboration between the red and blue teams: red and blue teams working together; providing information sharing and healthy competition.

<a id="subtopic-6-2-3"></a>

### 6.2.3 Log reviews

**Security Information and Event Management (SIEM)**: packages that collect information using the syslog functionality present in many devices, operating systems, and applications. SIEM capabilities: aggregation, normalization, correlation, secure storage, analysis, reporting.

Log data is recorded in databases; common logs include: security, application, firewall, proxy, and change management logs.

Log files should be protected by centrally storing them and using permissions to restrict access, and archived logs should be set to read-only to prevent modification. Admins may choose to deploy logging policies through Windows Group Policy Objects (GPOs). Logging systems should also make use of the Network Time Protocol (NTP) to ensure that clocks are synchronized on systems sending log entries to the SIEM as well as the SIEM itself, ensuring information from multiple sources have a consistent timeline. Information security managers should also periodically conduct log reviews, particularly for sensitive functions, to ensure that privileged users are not abusing their privileges.

Network flow (NetFlow) logs are particularly useful when investigating security incidents.

<a id="subtopic-6-2-4"></a>

### 6.2.4 Synthetic transactions/benchmarks

**RUM**: real user monitoring is a passive monitoring technique that records user interaction with an application or system to ensure performance and proper application behavior; often used as a pre-deployment process using the actual user interface. **Synthetic transactions**: scripted transactions with known expected results. **Synthetic (AKA active) monitoring** uses emulated or recorded transactions to monitor for performance changes in response time, functionality, or other performance monitors. **Real User Monitoring (RUM)**: observes and captures data from actual users as they interact with an application or website; this is also known as **passive monitoring** because user activity is passively monitored; this is good for identifying specific user issues.

Dynamic testing may include the use of synthetic transactions to verify system performance; synthetic transactions are run against code and compare output to expected state.

<a id="subtopic-6-2-5"></a>

### 6.2.5 Code review and testing

Code review and testing is "one of the most critical components of a software testing program". These procedures provide third-party reviews of the work performed by developers before moving code into a production environment, possibly discovering security, performance, or reliability flaws in applications before they go live and negatively impact business operations. In code review, AKA peer review, developers other than the one who wrote the code review it for defects; code review can be a formal or informal validation process.

**Fagan inspections** is the most formal code review process follows six steps:

Planning. Overview. Preparation. Inspection. Rework. Follow-up. Entry criteria are the criteria or requirements which must be met to enter a specific process. Exit criteria are the criteria or requirements which must be met to complete a specific process.

**Static application security testing (SAST)**: evaluates the security of software without running it by analyzing either the source code or the compiled application; code reviews are an example of static application security testing. **Dynamic application security testing (DAST)**: evaluates the security of software in a runtime environment and is often the only option for organizations deploying applications written by someone else. **Interactive Application Security Testing (IAST)** combines elements of both SAST and DAST by analyzing code during runtime from within the application, providing more accurate results.

<a id="subtopic-6-2-6"></a>

### 6.2.6 Misuse case testing

**Misuse Case Testing**: testing strategy from a hostile actor's point of view, attempting to lead to integrity failures, malfunctions, or other security or safety compromises. **Misuse case testing**: AKA abuse case testing - used by software testers to evaluate the vulnerability of their software to known risks; focuses on behaviors that are not what the organization desires or that are counter to the proper function of a system/application. In misuse case testing, testers first enumerate the known misuse cases, then attempt to exploit those use cases with manual or automated attack techniques.

<a id="subtopic-6-2-7"></a>

### 6.2.7 Coverage analysis

A test coverage analysis is used to estimate the degree of testing conducted against new software; to provide insight into how well testing covered the use cases that an application is being tested for.

**Test coverage**: number of use cases tested / total number of use cases.

Requires enumerating possible use cases (which is a difficult task), and anyone using test coverage calcs to understand the process used to develop the input values.

#### Five common criteria used for test coverage analysis

**branch coverage** has every IF statement been executed under all IF and ELSE conditions? **condition coverage** has every logical test in the code been executed under all sets of inputs? **functional coverage** has every function in the code been called and returned results? **loop coverage** has every loop in the code been executed under conditions that cause code execution multiple times, only once, or not at all? **statement coverage** has every line of code been executed during the test?

**Test coverage report**: measures how many of the test cases have been completed; is used to provide test metrics when using test cases.

<a id="subtopic-6-2-8"></a>

### 6.2.8 Interface testing (e.g., user interface, network interface, application programming interface (API))

Interface testing assesses the performance of modules against the interface specs to ensure that they will work together properly when all the development efforts are complete.

Interface testing essentially assesses the interaction between components and users with API testing, user interface testing, and physical interface testing.

#### Three types of interfaces should be tested

Application programming interfaces (APIs): offer a standardized way for code modules to interact and may be exposed to the outside world through web services.

Should test APIs to ensure they enforce all security requirements.

User interfaces (UIs): examples include graphical user interfaces (GUIs) and command-line interfaces.

UIs provide end users with the ability to interact with the software, and tests should include reviews of all UIs.

Physical interfaces: exist in some applications that manipulate machinery, logic controllers, or other objects.

Software testers should pay careful attention to physical interfaces because of the potential consequences if they fail.

Also see [OWASP API security](https://owasp.organization/www-project-api-security/).

<a id="subtopic-6-2-9"></a>

### 6.2.9 Breach attack simulations

**FedRAMP**: (see Domain 1) a government-wide program that standardizes the security assessment, authorization, and monitoring of cloud services and products; the program was established in 2011 to help the federal government use cloud technologies while protecting federal information. **Breach and attack simulation (BAS)**: platforms that automate some aspects of penetration testing. The BAS platform helps conduct automated testing of security controls to identify deficiencies. A BAS system combines red team (attack) and blue team (defense) techniques together with automation to simulate advanced persistent threats (and other advanced threat actors) running against the environment.

Designed to inject threat indicators onto systems and networks in an effort to trigger other security controls (e.g. place a suspicious file on a server).

Detection and prevention controls should immediately detect and/or block this traffic as potentially malicious.

#### See

OWASP Web Security Testing Guide. OSSTMM (Open Source Security Testing Methodology Manual). MITRE ATT&CK framework. NIST 800-115. FedRAMP Penetration Test Guidance. PCI DSS Information Supplemental on Penetration Testing.

<a id="subtopic-6-2-10"></a>

### 6.2.10 Compliance checks

Organizations should create and maintain compliance plans documenting each of their regulatory obligations and map those to the specific security controls designed to satisfy each objective. Compliance checks are an important part of security testing and assessment programs for regulated firms: these checks verify that all of the controls listed in a compliance plan are functioning properly and are effectively meeting regulatory requirements.

### AI in this objective

**Testing model behavior.** AI red teaming can examine evasion, extraction, and harmful output behavior. Evasion seeks an incorrect result at use time; extraction seeks information about or a replica of a model. Define authorization and limits, preserve test conditions, and record observed results. Automated scanning supplies additional findings, not a substitute for an assessment of model and application behavior. [NIST adversarial ML taxonomy](https://csrc.nist.gov/News/2025/nist-ai-100-2-adversarial-machine-learning-taxonom).

### Apply this objective

**Question.** A scan reports a severe vulnerability on a critical server. Should the report immediately claim that customer data was stolen?

**Reasoning.** No. A vulnerability finding is evidence of a possible weakness, not proof of exploitation or data loss. Validate the finding and investigate exposure and activity separately, then communicate what the evidence supports.

<a id="objective-6-3"></a>

## 6.3 Collect security process data (e.g. technical and administrative)

Security process data shows whether work happens and whether it achieves a useful outcome. An approval record, access review, restore result, training exercise, or risk indicator can support an assessment. Define the question before collecting a large volume of data.

A key performance indicator measures performance toward an objective; a key risk indicator signals changing exposure. Harbor might track timely access removal as a performance measure and the number of overdue privileged-account reviews as a risk signal. Interpret both in context.

Many components of the information security program generate data that is crucial to security assessment processes; these components include: Account management process; Management review and approval; Key performance and risk indicators; Backup verification data; Data generated by disaster recovery and business continuity programs.

<a id="subtopic-6-3-1"></a>

### 6.3.1 Account management

Preferred attacker techniques for obtaining privileged user access include:

Compromising an existing privileged account: mitigated through use of strong authentication (strong passwords and multifactor), and by admins use of privileged accounts only for specific tasks. Privilege escalation of a regular account or creation of a new account: these approaches can be mitigated by paying attention to the creation, modification, and use of user accounts.

<a id="subtopic-6-3-2"></a>

### 6.3.2 Management review and approval

Account management reviews ensure that users only retain authorized permissions and that unauthorized modifications do not occur. Full review of accounts: time-consuming to review all, and often done only for highly privileged accounts. Sampling can be statistical or judgmental. Choose and explain a method suitable for the audit objective, account for selection risk, and avoid overstating what the sample supports. Adding accounts: should be a well-defined process, and users should sign an AUP. Adding, removing, and modifying accounts and permissions should be carefully controlled and documented.

Accounts that are no longer needed should be suspended.

#### ISO 9000 standards use a Plan-Do-Check-Act loop

Plan: foundation of everything in the ISMS, determines goals and drives policies. Do: security operations. Check: security assessment and testing (this objective). Act: formally do the management review.

<a id="subtopic-6-3-3"></a>

### 6.3.3 Key performance and risk indicators

**Security assessments**: comprehensive reviews of the security of a system, application, or other tested environment.

During a security assessment, a trained information security professional performs a risk assessment that identifies vulnerabilities in the tested environment that may allow a compromise and makes recommendations for remediation, as needed. A security assessment includes the use of security testing tools, but goes beyond scanning and manual penetration tests. The main work product of a security assessment is normally an assessment report addressed to management that contains the results of the assessment in nontechnical language and concludes with specific recommendations for improving the security of the tested environment.

**Key Performance Indicators (KPIs)**: measures that provide significance of showing the performance of an ISMS compared to stated goals; KPIs are backward looking.

Choose the factors that can show the state of security. Define baselines for some (or better yet all) of the factors. Develop a plan for periodically capturing factor values (use automation!). Analyze and interpret the data and report the results.

Key metrics or KPIs that should be monitored by security managers may vary from organization to organization, but could include: number of open vulnerabilities; time to resolve vulnerabilities; vulnerability/defect recurrence; number of compromised accounts; number of software flaws detected in pre-production scanning; repeat audit findings; user attempts to visit known malicious sites.

Develop a dashboard of metrics and track them.

**Key Risk Indicators (KRIs)**: indicate the level of exposure to operational risk; they help monitor potential future shifts in risk conditions or emerging risks; KRIs are forward-looking; example KRIs might include: percentage of systems running unsupported/EOL software; number of third-party vendors without current security assessments; volume of unencrypted sensitive data transmissions.

<a id="subtopic-6-3-4"></a>

### 6.3.4 Backup verification data

Managers should periodically inspect the results of backups to verify that the process functions effectively and meets the organization’s data protection needs.

This might include reviewing logs, inspecting hash values, or requesting an actual restore of a system or file.

<a id="subtopic-6-3-5"></a>

### 6.3.5 Training and awareness

Training and awareness programs play a crucial role in preparing an organization’s workforce to support information security programs. They educate employees about current threats and advise them on best practices for protecting information and systems under their care from attacks. Program should begin with initial training designed to provide foundation knowledge to employees who are joining the organization or moving to a new role; the initial training should be tailored to an individual’s role. Training and awareness should continue to take place throughout the year, reminding employees of their responsibilities and updating them on changes to the organization’s operating environment and threat landscape.

Use phishing simulations to evaluate the effectiveness of their security awareness programs. It's important to measure training effectiveness through metrics (e.g., phishing simulation click rates over time). Training should include requirements by role (e.g., developers receiving secure coding training), and take into consideration compliance-driven requirements (e.g., annual security awareness training mandated by regulations).

<a id="subtopic-6-3-6"></a>

### 6.3.6 Disaster Recovery (DR) and Business Continuity (BC)

**Business Continuity (BC)** is the processes used by an organization to ensure, holistically, that its vital business processes remain unaffected or can be quickly restored following a serious incident.

**Disaster Recovery (DR)** is a subset of BC, that focuses on restoring information systems after a disaster.

These programs should take a comprehensive approach to planning and include considerations related to the initial response effort, personnel involved, communication among the team members and with internal and external entities, assessment of response efforts, and restoration of services. DR programs should also include training and awareness efforts to ensure personnel understand their responsibilities and lessons learned sessions to continuously improve the program.

DR and BC plans need to be periodically assessed and tested to ensure they remain effective. Protection of life is of the utmost importance and should be dealt with first before attempting to save material things.

### Apply this objective

**Question.** Harbor reports that 99% of backup jobs succeeded. Is that enough evidence that recovery works?

**Reasoning.** No. Successful jobs indicate backup execution, while restoration tests establish whether the data is usable and the service can meet recovery needs. Collect both kinds of evidence.

<a id="objective-6-4"></a>

## 6.4 Analyze test output and generate report

A finding should connect a condition to a requirement and a consequence. Explain what was observed, why it matters, what evidence supports it, and what should happen next. Prioritize using business impact and exposure as well as technical severity.

Assign an owner and a target date, document exceptions and risk acceptance, and verify remediation. A management report should be understandable without losing the evidence needed by the team doing the repair. Responsible disclosure also requires coordination and an appropriate communication path.

#### Step 1: review and understand the data

The goal of the analysis process is to proceed logically from facts to actionable info. A list of vulnerabilities and policy exceptions is of little value to business leaders unless it's used in context, so once all results have been analyzed, you're ready to start writing the official report.

#### Step 2: determine the business impact of those facts

Ask "so what?".

#### Step 3: determine what is actionable

The analysis process leads to valuable results only if they are actionable.

<a id="subtopic-6-4-1"></a>

### 6.4.1 Remediation

Rather than software defects, most vulnerabilities in average organizations come from misconfigured systems, inadequate policies, unsound business processes, or unaware staff. Vuln remediation should include all stakeholders, not just IT.

<a id="subtopic-6-4-2"></a>

### 6.4.2 Exception handling

**Exception handling** in assessment reporting means managing deviations from requirements or remediation expectations through ownership, justification, risk acceptance, and review. Software exception handling concerns runtime errors and is a different use of the term.

"expect the unexpected", gracefully handle invalid input and improperly sequenced activity etc.

Sometimes vulnerabilities can't be patched in a timely manner (e.g. medical devices needing re-accreditation) and the solution is to implement compensatory controls, document the exception and decision, and revisit.

**compensatory controls**: measures taken to address any weaknesses of existing controls or to compensate for the inability to meet specific security requirements due to various different constraints. E.g. micro-segmentation of device, access restrictions, monitoring etc.

Exception handling may be required due to system crash as the result of patching (requiring roll-back).

<a id="subtopic-6-4-3"></a>

### 6.4.3 Ethical disclosure

While conducting security testing, cybersecurity pros may discover previously undiscovered vulnerabilities (perhaps implementing compensating controls to correct) that they may be unable to correct.

**Ethical disclosure** is the idea that security pros who detect a vuln have a responsibility to report it to the vendor, providing them with enough time to patch or remediate.

The disclosure should be made privately to the vendor providing reasonable amount of time to correct. If the vuln is not corrected, then public disclosure of the vuln is warranted, such that other professionals can make informed decisions about future use of the product(s).

### AI in this objective

**AI-assisted prioritization.** Threat-informed tools can help rank findings; the team still needs to validate the evidence and business consequences. [ISC2 AI guidance, Domain 6](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

Original application: if Harbor's ranking tool labels an exposed customer database low priority, compare the underlying facts with the rating before accepting it. Record the reason for the final decision.

### Apply this objective

**Question.** A team marks a finding closed because a patch was deployed. What evidence should the assessor request?

**Reasoning.** Evidence that the affected systems received the intended change and that the weakness is no longer present, including relevant retesting. Deployment is an action; closure should be supported by a verified result.

<a id="objective-6-5"></a>

## 6.5 Conduct or facilitate security audits

An audit starts with criteria and scope, then gathers and evaluates evidence to support findings and a conclusion. Independence improves credibility, including in internal audit where organizational reporting arrangements can separate reviewers from the work reviewed.

Sampling may be necessary, but explain how the sample was selected and what conclusions it supports. External assurance is not automatically complete or applicable. Harbor remains responsible for addressing findings and implementing any customer-side controls identified in supplier reports.

<a id="subtopic-6-5-1"></a>

### 6.5.1 Internal

Having an internal team conduct security audits has several advantages:

Understanding the internal environment reduces time. An internal team can delve into all parts of systems, because they have insider knowledge. Internal auditors can be more agile in adapting to changing needs, rescheduling failed assessment components quickly.

Disadvantages of using an internal team to conduct security audits:

The team may have limited exposure to new/other methodologies (e.g. the team may have depth but not breadth of experience and knowledge). Potential conflicts of interest (e.g. reluctance to throw other teams under the bus and accurately report their findings). Audit team members may start with an agenda (say to secure funding) and overstate faults, or have interpersonal motives.

<a id="subtopic-6-5-2"></a>

### 6.5.2 External

An external audit (sometimes called a second-party audit) is one conducted by (or on behalf of) a business partner. External audit scope depends on its purpose, applicable criteria, and engagement terms, including relevant regulatory obligations. It is not limited by definition to contractual requirements.

<a id="subtopic-6-5-3"></a>

### 6.5.3 Third-party

Third-party audits are often needed to demonstrate compliance with some government regulation or industry standard.

#### Advantages of having a third-party audit an organization

They likely have breadth of experience auditing many types of systems, across many types of organizations. They are not affected by internal dynamics or organization politics.

#### Disadvantage of using a third-party auditor

Cost: third-party auditors are going to be much more costly than internal teams; this means that the organization is not likely to conduct audits as frequently. Internal resources are still required to assist or accompany auditors, to answer questions and guide.

#### Some common third-party audit frameworks include

ISO 27001 (certification audits). PCI DSS (for payment card data). HIPAA (for healthcare).

<a id="subtopic-6-5-4"></a>

### 6.5.4 Location (e.g., on-premise, cloud, hybrid)

See 6.1.4 above. Also see Understanding CISSP Domain 6, Security Assessment and Testing - [part 1](https://blog.balancedsec.com/p/understanding-cissp-domain-6-security), and [part 2](https://blog.balancedsec.com/p/understanding-cissp-domain-6-security-cbf) on the source author's blog, [The Cyber Leader](https://blog.balancedsec.com/) (note that some articles require a subscription).

### Apply this objective

**Question.** An auditor finds that access reviews occurred for a sample of teams. Can the report state that every account was reviewed?

**Reasoning.** Not without evidence supporting that broader claim. Describe the sample, method, findings, and limits, and investigate exceptions or additional coverage as needed.

## Chapter review

Return to the Harbor examples and explain each decision without looking at the answer. Identify the asset or business activity, the relevant requirement, the possible harm, the responsible owner, and the evidence that would support the decision. If two controls appear interchangeable, explain the different failure each addresses.

### Connections and common distinctions

A scan is not proof of compromise, testing is not proof of flaw-free software, and an audit depends on criteria and scope. Type I and Type II reports answer different timing questions. Findings should drive the operational remediation in Domain 7 and development changes in Domain 8.

### Review questions and explained answers

**1. How would you explain this domain to Harbor's service owner?** Describe the decisions it governs using the examples in this chapter. A useful answer connects technical measures to customer service, accountability, and evidence rather than listing product names.

**2. Which assumption in the chapter's examples would most change your recommendation if it were false?** Choose a concrete assumption, such as data sensitivity, allowed downtime, or an identity's authority. Explain how a different assumption changes the relevant control or test. More than one answer can be sound when justified.

**3. How does adding the AI assistant change the work?** Follow the AI lessons in this chapter. Identify an additional asset, failure, or decision and describe its owner and verification method. The assistant still operates within ordinary governance, access, data, and recovery requirements.

### AI application review

**Question.** A scan finds no ordinary software vulnerability in the assistant. What remains to test?

**Reasoning.** Evaluate model and application behavior under authorized adversarial tests, including evasion, extraction, and harmful output scenarios. Record versions, conditions, evidence, and limits. Validate any automated finding or prioritization and connect the result to business consequences before recommending release.

## Term index

This index points to explanations in the chapter. Terms retain the source guide's spelling where useful for recognition; corrected concepts are explained in context.

- [AI-assisted prioritization](#objective-6-4)
- [Artifact](#subtopic-6-1-1)
- [Assessment](#subtopic-6-2-1)
- [attack](#subtopic-6-2-2)
- [Audit](#subtopic-6-1-3)
- [Authenticated scans](#subtopic-6-2-1)
- [black-box penetration test](#subtopic-6-2-2)
- [branch coverage](#subtopic-6-2-7)
- [Breach and attack simulation (BAS)](#subtopic-6-2-9)
- [Business Continuity (BC)](#subtopic-6-3-6)
- [Chaos Engineering](#subtopic-6-2-1)
- [Code testing suite](#subtopic-6-2-1)
- [Common Configuration Enumeration (CCE)](#subtopic-6-2-1)
- [Common Platform Enumeration (CPE)](#subtopic-6-2-1)
- [Common Vulnerabilities and Exposures (CVE)](#subtopic-6-2-1)
- [Common Vulnerability Scoring Systems (CVSS)](#subtopic-6-2-1)
- [compensatory controls](#subtopic-6-4-2)
- [Compliance Calendar](#subtopic-6-1-1)
- [Compliance Tests](#subtopic-6-2-1)
- [condition coverage](#subtopic-6-2-7)
- [detailed information](#subtopic-6-2-2)
- [Disaster Recovery (DR)](#subtopic-6-3-6)
- [Dynamic application security testing (DAST)](#subtopic-6-2-5)
- [Ethical disclosure](#subtopic-6-4-3)
- [Exam tip](#subtopic-6-1-3)
- [Examination](#subtopic-6-1-1)
- [Exception handling](#subtopic-6-4-2)
- [eXtensible Configuration Checklist Description Format (XCCDF)](#subtopic-6-2-1)
- [Fagan inspections](#subtopic-6-2-5)
- [FedRAMP](#subtopic-6-2-9)
- [Findings](#subtopic-6-2-1)
- [functional coverage](#subtopic-6-2-7)
- [Functional order of controls](#subtopic-6-1-1)
- [Fuzzing](#subtopic-6-2-1)
- [gray-box penetration test](#subtopic-6-2-2)
- [IAM system](#subtopic-6-1-1)
- [information gathering and discovery](#subtopic-6-2-2)
- [Interactive Application Security Testing (IAST)](#subtopic-6-2-5)
- [ITSM](#subtopic-6-1-1)
- [Judgement Sampling](#subtopic-6-1-1)
- [Key Performance Indicators (KPIs)](#subtopic-6-3-3)
- [Key Risk Indicators (KRIs)](#subtopic-6-3-3)
- [known environment tests](#subtopic-6-2-2)
- [loop coverage](#subtopic-6-2-7)
- [Misuse Case Testing](#subtopic-6-2-6)
- [Misuse case testing](#subtopic-6-2-6)
- [Mutation testing](#subtopic-6-2-1)
- [Open Vulnerability and Assessment Language (OVAL)](#subtopic-6-2-1)
- [partial knowledge tests](#subtopic-6-2-2)
- [partially known environment](#subtopic-6-2-2)
- [passive monitoring](#subtopic-6-2-4)
- [Penetration Testing/Ethical Penetration Testing](#subtopic-6-2-1)
- [Plan of Action and Milestones (POA&M)](#subtopic-6-1-1)
- [planning](#subtopic-6-2-2)
- [Real User Monitoring (RUM)](#subtopic-6-2-4)
- [reporting](#subtopic-6-2-2)
- [RoE](#subtopic-6-2-1)
- [RUM](#subtopic-6-2-4)
- [SCE](#subtopic-6-1-1)
- [Security assessments](#subtopic-6-3-3)
- [Security Content Automation Protocol (SCAP)](#subtopic-6-2-1)
- [Security Information and Event Management (SIEM)](#subtopic-6-2-3)
- [SOC 1 Engagements](#subtopic-6-1-3)
- [SOC 2 Engagements](#subtopic-6-1-3)
- [SOC 3 Engagements](#subtopic-6-1-3)
- [Standards for Attestation Engagements document 18 (SSAE 18)](#subtopic-6-1-3)
- [statement coverage](#subtopic-6-2-7)
- [Static application security testing (SAST)](#subtopic-6-2-5)
- [Statistical Sampling](#subtopic-6-1-1)
- [Substantive Test](#subtopic-6-2-1)
- [Synthetic (AKA active) monitoring](#subtopic-6-2-4)
- [Synthetic transactions](#subtopic-6-2-4)
- [Test coverage](#subtopic-6-2-7)
- [Test coverage report](#subtopic-6-2-7)
- [Testing](#subtopic-6-2-1)
- [Testing model behavior](#objective-6-2)
- [Trust Services Criteria (TSC)](#subtopic-6-1-3)
- [Type I Reports](#subtopic-6-1-3)
- [Type II Reports](#subtopic-6-1-3)
- [unknown environment tests](#subtopic-6-2-2)
- [Vulnerabilities](#subtopic-6-2-1)
- [Vulnerability assessments](#subtopic-6-2-1)
- [Vulnerability management](#subtopic-6-2-2)
- [white-box penetration test](#subtopic-6-2-2)

## Sources and further reading

- [Original Domain 6 objectives and notes](../CISSP-Domain-6-2024+Objectives.md) by the repository's contributors; adapted under the repository license.
- [ISC2 CISSP exam outline and AI domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).
- [ISC2 AI guidance announcement](https://www.isc2.org/Insights/2026/04/ISC2-Publishes-Exam-Guidance-AI).
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

Additional references appear alongside the relevant concepts. Official Study Guide chapter references in the original objective files remain available for comparison.
