# Beginner-friendly CISSP study guide: proposed content outline

Status: implemented as eight separate content chapters in `content/`; the original domain objective files remain the source baseline. See [the chapter index](content/README.md).

## Alignment and scope

Use the [current ISC2 CISSP exam outline](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline) as the structural authority. Verified September 20, 2026: the published effective date remains April 15, 2024. ISC2 also provides AI guidance across the eight existing domains. Include that guidance within relevant objectives, with source references and clear separation from our teaching examples.

The eight existing `CISSP-Domain-*-2024+Objectives.md` files provide the content baseline. They contain 62 top-level objectives and 275 numbered subtopics. Preserve the concepts in their introductory glossaries, nested notes, examples, formulas, tables, and references as well as the numbered sections. The archived guides are historical material and are outside this rewrite.

“Rubric alignment” means alignment with ISC2's published objectives, domain weights, and action verbs. The teaching checks below are our editorial criteria, not an official ISC2 scoring rubric. Do not imply that a study guide reproduces confidential exam questions or guarantees coverage of every possible question.

## AI guidance and proposed placement

Use ISC2's [CISSP domain-level AI guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline) as the source for the AI additions below. ISC2 announced its [Exam Guidance for Artificial Intelligence on April 2, 2026](https://www.isc2.org/Insights/2026/04/ISC2-Publishes-Exam-Guidance-AI).

The AI lesson placements below are our editorial mapping to existing objectives, not new official objective numbers. Each block cites the corresponding domain in ISC2's guidance. Integrate these lessons into the indicated sections during rewriting. The scenarios are original teaching examples.

Introduce artificial intelligence (AI), machine learning (ML), large language models (LLMs), training, inference, and model weights in a brief prerequisite explanation. Extend the running example with a proposed customer-support assistant, following its approval, data preparation, deployment, access, testing, operation, and maintenance. Explain these prerequisites again where needed so chapters remain independently readable.

## Common chapter structure

1. **Start here:** a short explanation of the domain's purpose, its business relevance, and what a newcomer will learn. Introduce only the prerequisites needed to begin.
2. **A running example:** follow a small organization introducing an online customer service. Reuse its staff, customer records, cloud systems, suppliers, and service outage scenarios across domains.
3. **Objective-based sections:** retain official two-part objective numbers and order. Use descriptive subheadings to break large objectives into readable lessons. Keep existing three-part references traceable, identifying them as guide subtopics rather than separately numbered official objectives.
4. **Explanation before terminology:** introduce the problem, explain the concept in short connected paragraphs, define the term and expand its acronym at first use, then show how it applies. Explain important limitations and relationships to nearby concepts.
5. **Examples and comparisons:** use worked examples for calculations and processes; use compact tables for genuinely comparable concepts. Reserve bullets for steps, checklists, and short collections rather than the main explanation.
6. **Application checks:** conclude each objective with a short decision scenario and an explained answer. Match the objective's verb: explain for “understand,” choose and justify for “select,” work through a process for “implement,” and compare evidence for “assess.”
7. **Chapter review:** summarize the connections, distinguish commonly confused concepts, provide review questions with rationales, and finish with an alphabetical term index linking back to explanations and a source list.

Keep detailed coverage in the main lessons or clearly linked deeper-reading subsections. A glossary is a navigation aid, not a substitute for teaching the material. Preserve useful Official Study Guide chapter references as supporting references rather than letting them dominate headings.

## Domain 1 — Security and Risk Management

Teaching arc: understand what the organization values, who is accountable, and how security decisions support its mission.

- **1.1 — Professional responsibility:** explain the ethics canons and organizational ethics through conflicts of interest, competence, and responsibility to others.
- **1.2 — What security protects:** connect confidentiality, integrity, availability, authenticity, and nonrepudiation to everyday business failures and protective controls.
- **1.3 — Governance and accountability:** explain strategy, organizational change, roles, frameworks, due care, and due diligence; distinguish governance from daily management.
- **1.4 — Obligations and constraints:** organize existing legal, privacy, intellectual property, licensing, cross-border, and contractual material by the decisions each affects. Verify jurisdiction-specific claims before rewriting them.
- **1.5 — Types of investigation:** compare administrative, criminal, civil, regulatory, and industry investigations, including their purposes and constraints; link evidence procedures to Domain 7.
- **1.6 — Turning intent into instructions:** show how policies, standards, procedures, and guidelines work together in one organizational example.
- **1.7 — Business continuity requirements:** explain business impact analysis, critical activities, dependencies, and prioritization before introducing recovery requirements.
- **1.8 — The employment lifecycle:** follow screening, agreements, onboarding, transfers, departure, and contractor access.
- **1.9 — Making risk decisions:** introduce assets, threats, vulnerabilities, likelihood, and impact; work through qualitative and quantitative analysis, existing formulas, treatment choices, controls, monitoring, and reporting.
- **1.10 — Anticipating threats:** teach the existing threat-modeling approaches using one system and explain how their perspectives differ.
- **1.11 — Supplier risk:** connect acquisition and service-provider risks to assessment, contractual requirements, provenance, monitoring, and technical safeguards.
- **1.12 — Helping people act securely:** distinguish awareness, education, and training; explain delivery methods, emerging-topic reviews, and measures of effectiveness.

**AI lessons — proposed placement:** ethics and bias (1.1, 1.3); privacy (1.4); model risk (1.9); supplier transparency (1.11). [ISC2, Domain 1](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

AI application: decide what evidence the organization needs before approving the customer-support assistant and who must accept any remaining risk.

Chapter application: recommend and justify a risk treatment for a new customer service. Retain every existing framework, legal term, and calculation, with corrections supported by sources.

## Domain 2 — Asset Security

Teaching arc: follow information from its creation to its eventual disposal, showing who makes decisions and who carries them out.

- **2.1 — Identify value and sensitivity:** introduce information and asset classification, existing label schemes, personal and proprietary information, and consequences of mishandling.
- **2.2 — Handling rules:** explain labeling, access, storage, sharing, transport, and handling requirements through one customer record.
- **2.3 — Establish ownership and inventory:** distinguish accountability from custody; cover tangible and intangible assets, provisioning, inventory, and management.
- **2.4 — The data lifecycle:** explain roles, collection, location, maintenance, retention, remanence, and destruction in sequence. Compare the existing sanitization methods and their limitations.
- **2.5 — Retaining and retiring assets:** separate retention needs from end-of-life and end-of-support decisions, including dependencies on readable formats and supported systems.
- **2.6 — Choose protection for the context:** connect data states, scoping, tailoring, standards, DRM, DLP, and CASB to handling requirements.

**AI lessons — proposed placement:** datasets, models, weights (2.1); poisoning and lifecycle integrity (2.4); masking and differential privacy (2.6). [ISC2, Domain 2](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

AI application: assess whether historical support conversations are suitable for the assistant, then explain ownership, handling, retention, and disposal requirements.

Chapter application: follow a sensitive record from collection through authorized disposal. Preserve all existing classification, privacy, and sanitization terminology.

## Domain 3 — Security Architecture and Engineering

Teaching arc: explain how design choices create protection, then apply those choices to systems, cryptography, and facilities.

- **3.1 — Design security into the system:** teach each secure-design principle with a failure it prevents and a tradeoff it introduces.
- **3.2 — Models that express security rules:** explain subjects, objects, states, and information flow before comparing Bell–LaPadula, Biba, and every other existing model and property.
- **3.3 — Select controls from requirements:** connect business requirements to assurance, evaluation, and control selection, preserving the existing criteria and standards.
- **3.4 — Protection inside a computer:** explain processor and memory concepts, isolation, trusted components, and cryptographic capabilities. Correct “Trusted Platform Model” to “Trusted Platform Module.”
- **3.5 — Different architectures, different risks:** give each existing platform a short lesson covering its operation, trust boundaries, vulnerabilities, and mitigations. Cover clients, servers, databases, cryptographic systems, industrial systems, cloud, distributed systems, IoT, microservices, containers, serverless, embedded, high-performance, edge, and virtualized systems.
- **3.6 — Cryptography from first principles:** start with plaintext, ciphertext, keys, and security goals; explain symmetric and asymmetric methods, hashes, signatures, hybrid systems, key management, and PKI. Retain all algorithms and mathematical examples; clearly identify historical methods and distinguish quantum key distribution from post-quantum cryptography.
- **3.7 — How cryptographic protections fail:** organize attacks by what the attacker knows, controls, or observes. Preserve every named attack and explain attacks on implementations and credentials as well as algorithms.
- **3.8 — Selecting and designing a site:** connect location, hazards, access, and business requirements.
- **3.9 — Protecting facilities:** follow the path from the perimeter to rooms, storage, utilities, fire protection, and power, explaining each existing control and safety concern.
- **3.10 — The system lifecycle:** follow requirements through design, implementation, integration, verification, validation, deployment, operation, and retirement.

**AI lessons — proposed placement:** explainability (3.1, 3.3); secure enclaves (3.4); prompt injection, adversarial inputs, cloud responsibility, compute resilience (3.5). [ISC2, Domain 3](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

AI application: draw the assistant's trust boundaries and explain how a customer message could influence its behavior. Evaluate several protective layers and explain their limitations.

Chapter application: explain the design of a secure service and its hosting facility. Move the opening term collection into relevant lessons and retain a linked index.

## Domain 4 — Communication and Network Security

Teaching arc: follow a message across a network before explaining how to protect its route and endpoints.

- **4.1 — Network architecture:** retain the existing subtopic sequence but break this large objective into short lessons. Explain OSI and TCP/IP models; addressing and delivery patterns; protocols and encapsulation; converged traffic; topology and network planes; performance; traffic direction; physical, logical, and micro-segmentation; edge connectivity; wireless and cellular systems; CDNs; SDN; VPCs; and monitoring. Introduce each device, medium, protocol, port, and attack where it first becomes relevant.
- **4.2 — Protect network components:** explain infrastructure resilience and support, transmission media, admission controls, and endpoint protection.
- **4.3 — Protect communication channels:** apply the architecture to collaboration, remote administration, data links, and supplier connectivity; explain trust boundaries and suitable channel protections.

**AI lessons — proposed placement:** workload micro-segmentation, zero trust, AI-driven network detection (4.1); distributed-data transport and edge-inference channels (4.3). [ISC2, Domain 4](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

AI application: trace a request between the customer, assistant, and data service; explain which connections are necessary and how to protect and monitor them.

Chapter application: trace a remote employee's connection to the customer service. Keep reference tables for ports and protocols after their explanations; distinguish obsolete protocols from current secure choices.

## Domain 5 — Identity and Access Management

Teaching arc: follow an identity from registration to authentication, authorization, review, and removal.

- **5.1 — Subjects, objects, and access:** explain physical and logical protection across information, systems, devices, facilities, applications, and services.
- **5.2 — Establish and verify identity:** cover proofing, groups, roles, AAA, authentication factors, biometrics, passwordless methods, credentials, sessions, federation, SSO, and just-in-time access. Work through existing biometric error measures.
- **5.3 — Trusting an external identity provider:** explain federation in on-premises, cloud, and hybrid environments with a sign-in journey and explicit trust relationships.
- **5.4 — Decide what an identity may do:** compare the existing access-control models using the same resource, then explain policy decisions and enforcement.
- **5.5 — Maintain access over time:** follow joining, moving roles, access review, privilege changes, service-account management, and leaving.
- **5.6 — Put authentication into practice:** explain the existing authentication systems and protocols, their exchanges, weaknesses, and safeguards; cross-reference strategy in 5.2.

**AI lessons — proposed placement:** behavioral biometrics, adaptive authentication (5.2); agent least privilege (5.4); non-human identities and service accounts (5.5). [ISC2, Domain 5](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

AI application: give the assistant access to approved support records and explain how to prevent access to unrelated payroll records, review permissions, and revoke credentials.

Chapter application: design access for an employee, supplier, and automated service. Preserve all existing protocols, attacks, and access-control terms while resolving overlaps with Domains 4 and 8 through links.

## Domain 6 — Security Assessment and Testing

Teaching arc: start with the claim that a control works, identify the evidence needed, and explain how findings lead to action.

- **6.1 — Plan an assessment:** distinguish assessment, testing, and audit; explain scope, independence, authorization, and deployment location.
- **6.2 — Test controls appropriately:** compare vulnerability assessment and penetration testing, then explain log review, synthetic transactions, code and misuse testing, coverage, interfaces, attack simulation, and compliance checks. Retain existing testing techniques and team terminology.
- **6.3 — Gather process evidence:** connect account records, approvals, indicators, backup results, training, and continuity evidence to measurable questions.
- **6.4 — Turn results into decisions:** explain validation, prioritization, reporting, remediation, exceptions, disclosure, and follow-up.
- **6.5 — Conduct an audit:** follow planning, evidence collection, findings, and reporting across the existing internal, external, third-party, and location contexts.

**AI lessons — proposed placement:** AI red teaming, evasion, extraction, output flaws, automated scanning (6.2); threat-informed remediation prioritization (6.4). [ISC2, Domain 6](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

AI application: plan an authorized evaluation of the assistant, define expected results, and explain how findings affect the release decision. Distinguish a repeatable test result from an unsupported claim of safety.

Chapter application: turn a technical finding into a useful management report. Preserve every existing metric, technique, and reporting term.

## Domain 7 — Security Operations

Teaching arc: explain normal operations first in the introduction, then use the official objective order to teach investigation, protection, response, and recovery.

- **7.1 — Investigations and evidence:** follow an artifact from identification to preservation, analysis, and reporting; cover existing evidence rules, chain of custody, forensic methods, and tools.
- **7.2 — Understand operational signals:** explain logs, IDPS, SIEM, tuning, egress monitoring, intelligence, hunting, and UEBA through one suspicious event.
- **7.3 — Maintain known configurations:** introduce baselines, provisioning, automation, and drift.
- **7.4 — Limit operational misuse:** connect least privilege, need-to-know, separation of duties, privileged access, rotation, and service commitments.
- **7.5 — Protect resources in use:** explain media management and protection of stored and transmitted information.
- **7.6 — Manage an incident:** walk through detection, response, mitigation, reporting, recovery, remediation, and lessons learned, explaining ownership and decision points.
- **7.7 — Operate defensive controls:** explain every existing firewall, detection, filtering, sandbox, deception, malware, and AI-based control, including what operators must maintain.
- **7.8 — Manage vulnerabilities and patches:** follow identification, prioritization, testing, deployment, exceptions, and verification.
- **7.9 — Control change:** explain requests, impact analysis, approval, implementation, rollback, and review.
- **7.10 — Choose recovery arrangements:** compare backups, recovery sites, multiple sites, resilience, availability, QoS, and fault tolerance; retain existing recovery measures and examples.
- **7.11 — Carry out disaster recovery:** explain personnel, communications, assessment, restoration, training, and improvement.
- **7.12 — Exercise recovery plans:** compare read-through, tabletop, walkthrough, simulation, parallel, and interruption approaches and their risks.
- **7.13 — Sustain the business:** link continuity exercises and dependencies to Domain 1's business requirements.
- **7.14 — Operate physical safeguards:** explain perimeter and internal controls, linking design decisions to Domain 3.
- **7.15 — Keep people safe:** address travel, awareness, emergency action, duress, and existing personnel threat scenarios.

**AI lessons — proposed placement:** model drift (7.2); adversarial incident response (7.6); SOAR integration, event correlation, alert fatigue (7.7). [ISC2, Domain 7](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

AI application: investigate a decline in the assistant's answer quality alongside suspicious requests. Explain what to observe, when to involve an operator, and how to restore an acceptable service.

Chapter application: follow an incident through evidence preservation and service recovery. Distinguish incident response, disaster recovery, and business continuity throughout.

## Domain 8 — Software Development Security

Teaching arc: follow a feature from requirements to release and maintenance, explaining development vocabulary as it becomes necessary.

- **8.1 — Security throughout development:** introduce the SDLC, existing development methodologies, maturity models, maintenance, change control, and team responsibilities.
- **8.2 — Secure the development environment:** explain languages, libraries, tools, IDEs, runtime, pipelines, configuration, repositories, and application testing. Integrate existing programming, database, and data-management foundations into relevant lessons or linked prerequisite sections.
- **8.3 — Evaluate software protection:** connect change records, audit evidence, risk analysis, and mitigation to release and maintenance decisions.
- **8.4 — Evaluate acquired software:** compare commercial, open-source, third-party, managed, and cloud software using responsibilities, dependencies, evidence, and ongoing support.
- **8.5 — Prevent coding weaknesses:** explain every existing vulnerability, attack, and secure-coding practice through cause, impact, and prevention; include API protection and software-defined security.

**AI lessons — proposed placement:** AI-assisted coding and pipeline testing (8.2); ML supply-chain dependencies (8.4); generated-code weaknesses, model hijacking, inference attacks (8.5). [ISC2, Domain 8](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

AI application: review an assistant feature built with generated code and an external ML library. Explain the review and test evidence needed before release. Clarify that ordinary inference means using a model, while an inference attack seeks information that should remain protected.

Chapter application: review a proposed feature and its release process. Preserve all existing programming, database, testing, and attack terminology without assuming the learner already writes code.

## Coverage and editorial checks before completion

Create a coverage ledger before rewriting, with one row per source concept or distinct supporting detail: original file and location, term or claim, destination objective and heading, and disposition (retained, combined with an equivalent explanation, corrected with a citation, or expanded). Include unbolded material and introductory glossaries; counting headings or bold terms alone cannot prove preservation.

Check the ledger against every official objective and its listed topics. Preserve existing supplementary material, but identify it as supporting context when it goes beyond the published outline. Verify the latest guidance again when rewriting starts, and source any additions. Never silently retain a factual error merely to preserve wording.

For each chapter, verify that:

- Every baseline concept and supporting detail has an explained destination; merged duplicates retain all distinct meaning.
- Every AI lesson above has a destination, a source citation, a beginner explanation, and an application check; distinguish ISC2 guidance from our mapping and examples.
- Every required objective and topic is covered in the correct section or by an explicit, useful cross-reference.
- Acronyms and prerequisite concepts are introduced before use; examples teach relationships rather than merely restating definitions.
- Historical technologies, current recommendations, legal requirements, and context-dependent claims are distinguished and checked against primary sources.
- Application questions have reasoned answers and do not rely on blanket test-taking rules.
- Headings, tables of contents, internal links, source links, and cross-domain references work after reorganization.

Rewrite and check one domain at a time, starting with Domain 1. Update guide navigation and regenerate any agreed publication outputs only after the Markdown content passes these checks. The content chapters and combined PDF implement this outline; original objective files remain unchanged for comparison.
