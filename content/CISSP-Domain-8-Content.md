<a id="domain-8"></a>

# Domain 8: Software Development Security

Exam weight: 10%. Study edition: September 2026.

## Start here

Software development security follows a feature from its requirements to its operation and eventual retirement. You will learn the vocabulary of development, protect the environment that builds software, evaluate acquired components, and recognize coding weaknesses. No programming experience is assumed; focus first on how information and authority move through a program.

This chapter follows the published Domain 8 objectives. Read the opening explanation of each objective first, then the detailed lessons, and finish with its application check. Three-part numbers identify subtopics retained from the source guide. The examples use Harbor Services, a small organization launching a customer portal and an AI support assistant.

Artificial intelligence (AI) is the broad field of systems performing tasks associated with intelligence. Machine learning (ML) builds models from examples during training; inference uses a trained model to produce an output. A large language model (LLM) produces language using learned numerical parameters called model weights. These terms identify components and processes to protect, rather than establish that a system is correct or trustworthy.

The AI additions apply [ISC2's domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline) to existing objectives. Detailed placement and Harbor scenarios are editorial teaching choices. Named historical technologies remain useful for comparison; their inclusion is not a recommendation to deploy them.

## Chapter navigation

- [8.1 Understand and integrate security in the Software Development Life Cycle (SDLC)](#objective-8-1)
- [8.2 Identify and apply security controls in development ecosystems](#objective-8-2)
- [8.3 Assess the effectiveness of software security](#objective-8-3)
- [8.4 Assess security impact of acquired software](#objective-8-4)
- [8.5 Define and apply secure coding guidelines and standards](#objective-8-5)

<a id="objective-8-1"></a>

## 8.1 Understand and integrate security in the Software Development Life Cycle (SDLC)

Software security starts with what a system is meant to do and the harms it must prevent. The software development lifecycle organizes requirements, design, implementation, testing, release, maintenance, and retirement. Waterfall, Agile, and DevOps organize this work differently, but each still needs security responsibilities and evidence.

DevSecOps integrates security into development and operations instead of leaving it to a final inspection. At Harbor, security requirements, threat modeling, tests, and release checks should evolve with the feature. A maturity model helps improve the process consistently; it is not proof that every product is secure.

<a id="subtopic-8-1-1"></a>

### 8.1.1 Development methodologies (e.g., Agile, Waterfall, DevOps, DevSecOps, Scaled Agile Framework)

**UAT**: User Acceptance Testing typically the last phase of the testing process; verifies that the solution developed meets user requirements, and validates against use cases.

**SDLC**: Software Development LifeCycle is a framework and systematic associated with tasks that are performed in a series of steps for building, deploying, and supporting software applications; begins with planning and requirements gathering, and ends with decommissioning and sunsetting; there are many different SDLCs, such as agile, DevSecOps, rapid prototyping, offering different approaches to defining and managing the software lifecycle;.

#### The SDLC consists of the following steps

Requirements gathering: why create the software, what it will do, and for whom it will be created. Design: encapsulating how the software will meet requirements. Development: creating/coding the software to meet spec, and integrating with other systems as required. Testing: verifying/validating software meets requirements. Operations and Maintenance: deploying, and ensuring it's appropriately configured, patched, and monitored.

**Agile methodology** is a project management approach to development that involves breaking the project into phases and emphasizes continuous collaboration and improvement; teams follow a cycle of planning, executing, and evaluating; focus is on iterative development and frequent feedback, collab between small self-organizing cross-functional teams.

#### Agile development emphasizes

The delivery of working software in short iterations, helping to get the software to market faster. Reduced risk by frequently testing and providing feedback, helping to identify and resolve issues earlier in the development process.

Agile was started by 17 pioneers in 2001, producing the "Manifesto for Agile Software Development" ([agilemanifesto.organization](https://agilemanifesto.organization)) that lays out the core philosophy of the Agile approach:

**individuals and interactions** over processes and tools. **working software** over comprehensive documentation. **customer collaboration** over contract negotiation. **responding to change** over following a plan.

#### Agile Manifesto also defines 12 principles

The highest priority is to satisfy the customer through early and continuous delivery of valuable software. Welcome changing requirements, even late in development; Agile processes harness change for the customer’s competitive advantage. Deliver working software frequently, from a couple of weeks to a couple of months, with a preference for the shorter timescale. Business people and developers must work together daily throughout the project. Build projects around motivated individuals; give them the environment, support, and tools and trust them to build. Emphasizing face-to-face conversation. Working software is the primary measure of progress.

Agile processes promote sustainable development; the team should be able to maintain a constant pace indefinitely. Continuous attention to technical excellence and good design enhances agility. Simplicity, or the art of maximizing the amount of work not done, is essential. The best architectures, requirements, and designs emerge from self-organizing teams. At regular intervals, the team reviews their effectiveness and adjusts for improvement.

Several methodologies have emerged that take these Agile principles and define specific processes around them:

**Scrum** is a management framework that teams use to self-organize and work towards a common goal; it describes a set of meetings, tools, and roles for efficient project delivery, allowing teams to self-manage, learn from experience, and adapt to change; named from the daily team meetings, called scrums; development focuses on short sprints that deliver finished products; integrated product teams (IPTs) were an early effort of this approach. **Kanban** is a visual system used to manage and keep track of work as it moves through a process; the word kanban is Japanese for "card you can see"; Kanban teams focus on reducing the time a project (or user story) takes from start to finish, using a kanban board and continuously improving their flow of work.

**Rapid Application Development (RAD)** is an agile software development approach that focuses more on ongoing software projects and user feedback and less on following a strict plan, emphasizing rapid prototyping over planning; RAD uses four phases: requirements planning, user design, construction, and cutover.

**Rational Unified Process (RUP)** is an agile software development methodology that splits the project life cycle into four phases:

Inception: which defines the scope of the project and develop business case. Elaboration: Plan project, specify features, and baseline the architecture. Construction: Building the product. Transition: providing the product to its users. During each of the phases, all six core development disciplines take place: business modeling, requirements, analysis and design, implementation, testing, and deployment.

**Agile Unified Process (AUP)** is a simplified version of the rational unified process, it describes a simple, easy to understand approach to developing business application software using agile techniques and concepts yet still remaining true to the RUP.

**Dynamic Systems Development Model (DSDM)** is an agile project delivery framework, initially used as a software development method; key principles:

Focus on the business need: DSDM teams establish a valid business case and ensure organizational support throughout the project. Deliver on time: work should be time-boxed and predictable, to build confidence in the development team.

**Extreme Programming (XP)** is an Agile project management methodology that targets speed and simplicity with short development cycles, [using five guiding values, and five rules](http://www.extremeprogramming.organization); the goal of the rigid structure, focused sprints and continuous integrations is higher quality product. **Scaled Agile Framework® (SAFe)** is a set of organization and workflow patterns for implementing agile practices at an enterprise scale; the framework is a body of knowledge that includes structured guidance on roles and responsibilities, how to plan and manage the work, and values to uphold.

#### Waterfall

A linear approach to development, where each phase needs to be completed fully before the next one begins (e.g. water only flows downhill or in one direction); developed by Winston Royce in 1970, the waterfall model uses a linear sequential life-cycle approach; all project requirements are gathered up front, and there is no formal way to integrate changes as more information becomes available.

Traditional model has 7 stages, as each stage is completed, the project moves into the next phase; the iterative waterfall model does allow development to return to the previous phase to correct defects.

System requirements; Software requirements; Preliminary design; Detailed design; Code and debug; Testing; Operations and maintenance.

A major criticism of this model is that it's very rigid, and not ideal for most complex projects which often contain many variables that affect the scope throughout the project's lifecycle.

**Spiral model**: improved waterfall, (developed by Barry Boehm) that has its own phases: (1) determine objectives, (2) identify and resolve risks, (3) develop and test, (4) plan the next iteration; it is a risk-driven development process that follows an iterative model while also including waterfall elements.

Following defined phases to completion and then repeats the process, resembling a spiral. The spiral model provides a solution to the major criticism of the waterfall model in that it allows devs to return to planning stages as technical demands and customer requirements iterate.

**V-Model** (Verification and Validation model), which extends the waterfall model by pairing each development phase with a corresponding testing phase; the V-Model illustrates the parallel relationship between development and verification activities.

**DevOps (Development and Operations)** is an approach to software development, quality assurance, and technology operations that unites siloed staff, and bring the three functions together in a single operational model; DevOps goal is to shorten the systems development lifecycle and provide continuous delivery.

Closely aligned with lean and the Agile development approach, DevOps aims to dramatically decrease the time required to develop, test, and deploy software changes. Using the DevOps model, and continuous integration/continuous delivery (CI/CD), organizations strive to roll out code dozens or even hundreds of times per day. This requires a high degree of automation, including integrating code repositories, the software configuration management process, and the movement of code between development, testing and production environments. The tight integration of development and operations also calls for the simultaneous integration of security controls.

Security must be tightly integrated and move with the same agility.

**DevSecOps** refers to the integration of development, security, and operations; extends DevOps by integrating security practices.

Provides for a merger of phased review (as in the waterfall SDLC) with the DevOps method, to incorporate the needs for security, safety, resilience or other emerging properties in the final system, at each turn of the cycle of development. DevSecOps supports the concept of software-defined security, where security controls are actively managed into the CI/CD pipeline.

<a id="subtopic-8-1-2"></a>

### 8.1.2 Maturity models (e.g., Capability Maturity Model (CMM), Software Assurance Maturity Model (SAMM))

**Software Quality Assurance**: variety of formal and informal processes that attempt to determine whether a software application or system meets all of its intended functions, doesn't perform unwanted functions, is free from known security vulnerabilities, and is free from insertion or other errors in design and function. **CAB**: Change Advisory Board purpose is to review and approve/reject proposed code changes. Maturity models help organizations move from inconsistent, unstructured software processes to more reliable and well-managed ones. Be able to describe the SW-CMM, IDEAL, and SAMM models.

Software Engineering Institute (SEI) (Carnegie Mellon University) created the Capability Maturity Model for Software (AKA Software Capability Maturity Model, abbreviated SW-CMM, CMM, or SCMM).

**SW-CMM** is a management process to foster the ongoing and continuous improvement of an organization's processes and workflows for developing, maintaining and using software. All software development moves through a set of maturity phases in sequential fashion, and CMM describes the principles and practices underlying software process maturity, intended to help improve the maturity and quality of software processes. CMM doesn't explicitly address security.

#### Stages of the CMM

**Level 1: Initial** is a process is disorganized; usually little or no defined software development process.

No KPIs; processes are ad-hoc, and immature; no basis for predicting project quality, time to completion etc; limited project management; limited software dev tools or automation; highly dependent on individual's skills and knowledge.

**Level 2: Repeatable**: in this phase, basic lifecycle management processes are introduced.

Focus on establishing basic project management policies; project planning; configuration management; requirements management; sub-contract management; software quality assurance.

**Level 3: Defined**: in this phase, software devs operate according to a set of formal, documented software development processes; marked by the presence of basic lifecycle management processes and reuse of code; includes the use of requirements management, software project planning, quality assurance, and configuration management.

Documentation of standard guidelines and procedures takes place; peer reviews; intergroup coordination; organization process definition; organization process focus; training programs.

**Level 4: Managed**: in this phase, there is better management of the software process; characterized by the use of quantitative software development measures.

Quantitative goals are set for software products and process; software quality management; quantitative management.

**Level 5: Optimizing: in this phase continuous improvement occurs**

Process change management. Technology change management. Defect prevention.

**Software Assurance Maturity Model (SAMM)** is an open source project maintained by the Open Web Application Security Project (OWASP).

Provides a framework for integrating security into the software development and maintenance processes and provides organizations with the ability to assess their maturity.

#### SAMM associates software development with 5 business functions

Governance: the activities needed to manage software development processes.

**This function includes practices for**

Strategy. Metrics. Policy. Compliance. Education. Guidance.

Design: process used to define software requirements and develop software.

**This function includes practices for**

Threat modeling. Threat assessment. Security requirements. Security architecture.

Implementation: process of building and deploying software components and managing flaws.

**This function includes**

Secure build. Secure deployment. Defect management practices.

Verification: activities undertaken to confirm code meets business and security requirements.

**This function includes**

Architecture assessment. Requirements-driven testing. Security testing.

Operations: actions taken to maintain security throughout the software lifecycle after code is released.

**Function includes**

Incident management. Environment management. Operational management.

**IDEAL Model**: developed by SEI, a model for software development that uses many of the SW-CMM attributes, using 5 phases:

Initiating: business reasons for the change are outlined, support is built, and applicable infrastructure is allocated. Diagnosing: in this phase, engineers analyze the current state of the organization and make general recommendations for change. Establishing: development of a specific plan of action based on the diagnosing phase recommendations. Acting: in this phase, the organization develops solutions and then tests, refines, and implements them. Learning: continuously analyze efforts to achieve these goals, and propose new actions as required.

IDEAL vs SW-CMM: remember that IDEAL is a process improvement model (how to improve), while SW-CMM is a maturity assessment model (where you currently are); the table below shows approximate conceptual alignment.

| IDEAL | SW-CMM |
|----------------|---------------|
| Initiating|Initial|
| Diagnosing  | Repeatable|
| Establishing | Defined|
| Acting  | Managed|
| Learning| Optimizing|

<a id="subtopic-8-1-3"></a>

### 8.1.3 Operations and maintenance

Once delivered to the production environment, software devs must make any additional changes to accommodate unexpected bugs, vulnerabilities, or interoperability issues.

They must also keep pace with changing business processes, and work closely with the operations team (typically IT), to ensure reliable operations.

Together, ops and development transition a new system to production and management of the system's config.

The dev team must continually provide hotfixes, patches, and new releases to address discovered security issues and identified coding errors.

<a id="subtopic-8-1-4"></a>

### 8.1.4 Change management

**Acceptance**: formal, structured hand-off of the completed software system to the customer organization; usually involves test, analysis and assessment activities.

Change management (AKA control management) plays an important role when monitoring systems in a controlled environment, and has 3 basic components:

**Request Control** is a process that provides an organized framework within which users can request modifications, managers can conduct cost/benefit analysis, and developers can prioritize tasks.

**Change Control** is the process of controlling specific changes that need to take place during the life cycle of a system, serving to document the necessary change-related activities; or the process of providing an organized framework within which multiple devs can create and test a solution prior to rolling it out in a production environment.

Where change management is the project manager’s responsibility for the overarching process, change control is what devs do to ensure the software or environment doesn’t break when changed. Change control is basically the process used by devs to re-create a situation encountered by a user and analyze the appropriate changes; it provides a framework where multiple devs can create and test a solution prior to rolling it out into a prod environment.

**Release Control**: once changes are finalized, they must be approved for release through the release control procedure.

One of the responsibilities of release control is ensuring that the process includes acceptance testing, confirming that any alterations to end-user work tasks are understood and functional prior to code release.

<a id="subtopic-8-1-5"></a>

### 8.1.5 Integrated Product Team (IPT)

**Integrated Product Team (IPT)**: Introduced by the US Department of Defense (DoD) as an approach to bring together multifunctional teams with a single goal of delivering a product or developing a process or policy, and fostering parallel, rather than sequential, decisions. Essentially, IPT is used to ensure that all aspects of a product, process, or policy are considered during the development process.

### Apply this objective

**Question.** A feature is almost ready when security first reviews its design. What process change would help future features?

**Reasoning.** Include security requirements and threat modeling earlier, with checks throughout development and maintenance. Early review can address design assumptions before they become expensive implementation dependencies.

<a id="objective-8-2"></a>

## 8.2 Identify and apply security controls in development ecosystems

A development environment is part of the software supply chain. Languages, libraries, tools, repositories, build systems, credentials, and runtime environments can all affect the released product. Protect source changes, dependencies, build authority, and release artifacts as well as the application itself.

Different tests reveal different evidence. Static analysis examines code without running it; dynamic analysis observes running behavior; composition analysis examines dependencies. These methods complement review and runtime controls. Database and programming concepts below explain why state, type handling, transactions, and interfaces affect security.

Applications, including custom systems, can present significant risks and vulnerabilities, and to protect against these it's important to introduce security controls into the entire system’s development lifecycle.

<a id="subtopic-8-2-1"></a>

### 8.2.1 Programming languages

**Trapdoor/backdoor**: AKA maintenance hook; hidden mechanism that bypasses access control measures; an entry point into an architecture or system that is inserted in software by devs during development to provide a method of gaining access for modification/support; can also be inserted by an attacker, bypassing access control measures designed to prevent unauthorized software changes. **TOCTOU attack**: time of check vs time of use (TOCTOU) attack takes advantage of the time delay between a security check (such as authentication or authorization) being performed and actual use of the asset.

**Threat surface**: total set of penetrations of a boundary or perimeter that surrounds or contains system elements. **Strong data typing**: feature of a programming language preventing data type mismatch errors; strongly typed languages will generate errors at compile time. **Spyware/Adware**: software that performs a variety of monitoring and data gathering functions; AKA potentially unwanted programs/applications (PUP/PUA), may be used in monitoring employee activities/use of resources (spyware), or advertising efforts (adware); both may be legit/authorized by system owners or unwanted intruders. **Source code**: program statements in human-readable form using a formal programming language's rules for syntax and semantics.

**Runtime Application Security Protection (RASP)**: security agents comprised of small code units built into an application which can detect set of security violations; upon detection, the RASP agent can cause the application to terminate, or take other protective actions. **Reputation monitoring** evaluates the reported trust or risk of destinations to help block harmful connections. It complements other defenses and cannot identify every new or compromised destination. **Representational State Transfer (REST)**: software architectural style for synchronizing the activities of two or more applications running on different systems on a network; REST facilitates these processes exchanging state information, usually via HTTP/S.

**Relational database model**: AKA relational database management system (RDBMS), data elements and records arranged in tables which are related or linked to each other to implement business logic, where data records of different structures or types are needed together in the same activity. **Regression testing**: test a system to understand whether recently approved modifications have changed performance of other approved functions or introduced other unauthorized behavior; testing that runs a set of known inputs against an application and compares to results previously produced (by an earlier version of the software).

**Refactoring**: partial or complete rewrite of a set of software to perform the same functions, but in a more straightforward, more efficient, or more maintainable form. **Ransom attack** is a form of attack that threatens destruction, denial, or unauthorized public release/remarketing of private information assets; usually involves encrypting assets and withhold the decryption key until a ransom is paid by the victim. **Query attack**: use of query tools to access data not normally allowed by the trusted front end, including the views controlled by the query application; could also result from malformed queries using SQL to bypass security controls; improper/incomplete checks on queries can be used in a similar way to bypass access controls.

**Procedural programming**: emphasizes the logical sequence of steps to be performed, where a procedure is a set of software that performs a particular function, requiring specific input data, producing a specific set of outputs, and procedures can invoke other procedures. **Polyinstantiation**: (literally "many versions") creates a new instance (copy) of a data item, with the same identifier or key, allowing each process to have its own version of that data; allows a system to store multiple versions of the same data item at different security levels to prevent unauthorized users from "inferring" the existence of sensitive information; by showing users only the version that matches their clearance, it ensures that a low-level user can’t detect the presence of higher-level data through system errors or duplicate conflicts.

**Pass-around reviews**: often done via email or code review system, allows devs to review code asynchronously. **Pair programming** requires two devs to work together, one writing code, and the other reviewing and tracking progress. **Object-oriented security**: systems security designs that make use of object-oriented programming characteristics such as encapsulation, inheritance, polymorphism, and polyinstantiation. **Object-oriented database model**: database model that uses object-oriented programming concepts like classes, instances, and objects to organize, structure, and store data and methods; schemas define the structure of the data, views specify table, rows, and columns that meet user/security requirements.

**Object**: encapsulation of a set of data and methods that can be used to manipulate that data. **Nonfunctional requirements**: broad characteristics that do not clearly align with system elements; many safety, security, privacy, and resiliency requirements can be deemed nonfunctional. **Network database model**: database model in which data elements and records are arranged in arbitrary linked fashion (e.g. lists, clusters, or other network forms). **Modified prototype model**: approach to system design/build that starts with a simplified version of the application; feedback from stakeholders is used to improve design of a second version; this is repeated until owners/stakeholders are satisfied with the final product.

**Mobile code (executable content)**: file(s) sent by a system to others, that will either control the execution of systems/applications on that client or be directly executed. **Metadata**: information that describes the format or meaning of other data, which can be used to provide a systematic method for describing resources and improving information retrieval. **Markup Language**: non-programming language used to express formatting or arrangement of data on a page/screen; usually extensible, allowing users to define additional/other operations to be performed. **Malformed input attack**: incorrectly handling input data is a common source of code errors that can result in arbitrary code exec, or misdirection of the program to other resources/locations.

**Living off the land** (non-malware based ransom attack): system attack where the system/resources compromised are used in pursuit of additional attacks (i.e. the attacker's agenda); anti-malware defense doesn't detect/prevent the attack given the attacker's methodology. **Level of abstraction**: how closely a source-code/design doc represents the details of the underlying object/system/component; lower-level abstractions generally have more detail than high-level ones. **Knowledge Management**: efficient/effective management of information and associated resources in an enterprise to drive business intelligence and decision-making; may include workflow management, business process modeling, doc management, db and information systems and knowledge-based systems.

**Knowledge Discovery in Database (KDD)**: mathematical, statistical, and visualization method of identifying valid and useful patterns in data. **Infrastructure as Code (IaC)**: instead of viewing hardware config as a manual, direct hands-on, one-on-one admin hassle, it is viewed as just another collection of elements to be managed in the same way that software and code are managed under DevSecOps. **Integrated Product and Process Development (IPPD)**: management technique that simultaneously integrates essential acquisition activities through the use of multidisciplinary teams to optimize the design, manufacturing, and supportability processes.

**Instance**: in object-oriented programming, an "instance of a class" refers to a specific object created from that class, which is a blueprint or template defining the characteristics and behaviors of objects. **Hierarchical database model**: data elements and records are arranged in tree-like parent-child structures. **Functional requirements** describes a finite task or process the system must perform; often directly traceable to specific elements in the final system's design and construction. **XML**, Extensible Markup Language, represents structured information with markup for documents and data exchange. It is not an extension of HTML, although applications can use both. [W3C](https://www.w3.organization/XML/).

**Executable/Object Code**: binary representation of the machine language instruction set that the CPU and other hardware of the target computer can directly execute. **Encapsulation**: note see network Encapsulation in [Domain 4](CISSP-Domain-4-Content.md) (disambiguation); enforcement of data/code hiding during all phases of software development and operational use; bundling together data and methods is the process of encapsulation (opposite of unpacking/revealing). **Emergent Properties** is an alternate/more powerful way of looking at systems-level behavior characteristics such as safety and security; helps provide a more testable, measurable answer to questions such as "how secure is our system?".

**Dirty read** occurs when one transaction reads a value from a database that was written by another transaction that didn't commit; this is a concurrency control issue that violates the **Isolation** property of ACID. **Design Reviews**: should take place after the development of functional and control specifications but before the creation of code. **Data-centric Threat Modeling**: methodology and framework focusing on the authorized movements and data input/output into and from a system; corresponds with protecting data in transit, at rest, and in use when classifying organizational data.

**Data Warehouse** is a collection of data sources such as separate internal databases to provide a broader base of information for analysis, trending and reference; may also involve databases from outside the organization. **Data Type Enforcement**: how a language protects a developer from trying to perform operations on dissimilar types of data, or in ways that would lead to erroneous results. **Data Protection and Data Hiding** restricts or prevents one software unit from reading or altering the private data of another software unit or in preventing data from being discovered or accessed by a subject.

**Data Modeling**: design process that identifies all data elements that the system will need to input, create, store, modify, output, and destroy during operational use; should be one of the first steps in analysis and design. **Data Mining**: analysis and decision-making technique that relies on extracting deeper meanings from many different instances and types of data; often applied to data warehouse content. **Data Lake** is a centralized repository that stores large volumes of raw data in its native format, including structured, semi-structured, and unstructured data; unlike a data warehouse, data in a data lake is not processed or structured at the time of storage.

**Data Contamination**: attackers attempt to use malformed inputs, at the field, record, transaction, or file level, in an attempt to disrupt the proper functioning of the system. **Covert Channels/Paths** is a method used to pass information over a path that is not normally used for communication; communication pathways that violate security policy or requirement (deliberately or unwittingly); basic types are timing and storage. **Configuration Control** is a process of controlling modifications to hardware, firmware, software, and documentation to protect the information system against improper modifications prior to, during, and after system implementation.

**CORBA**: Common Object Request Broker Architecture is a set of standards addressing interoperability between software and hardware products, residing on different machines across a network; providing object location and use across a network. **Object/Memory reuse**: systems allocate/release and reuse memory/resources as objects to requesting processes; data remaining in the object when it is reused is a potential security violation (i.e. data remanence). **Complete coverage**: testing all of the functions of software. **Code reuse**: reuse of code rather than re-inventing it means units of software (procedures/objects) provide higher productivity toward development requirements using correct, complete, safe code.

**Code protection/logic hiding** prevents one software unit from reading/altering the source/intermediate/executable code of another software unit. **Citizen programmers**: organizational members who codify work-related knowledge, insights, and ideas into (varying degrees of) usable software; the process and result is ad hoc, difficult to manage, and usually bereft of security considerations. **Bypass attack**: attempt to bypass front-end controls of a database to access information. **Buffer overflow**: source code vulnerability allowing access to data locations outside of the storage space allocated to the buffer; can be triggered by attempting to input data larger than the size of the buffer.

**Arbitrary code**: alternate set of instructions and data that an attacker attempts to trick a processor into executing. **Aggregation**: ability to combine non-sensitive data from separate sources to create sensitive info; note that aggregation is a "security issue", where as inference is an attack (where an attacker can pull together pieces of less sensitive information to derive information of greater sensitivity). **ACID Test**: data integrity provided by means of enforcing atomicity, consistency, isolation, and durability policies. **Accreditation**: AKA Security Accreditation a formal declaration by a designated accrediting authority (DAA) that an information system is approved to operate at an acceptable level of risk, based on the implementation of an approved set of technical, managerial, and procedural safeguards.

Security should be part of the design, and incorporated into the architecture, with the level of protection based on requirements and operating environment. In this domain you'll learn the basic principles behind securely designing, building, testing, operating and even decommissioning enterprise applications.

Domain 8 has a ~10% exam weighting, and is focused on helping security professionals understand and apply software or application security.

Applications can present significant risks, and we need to understand and balance these risks with business requirements and implement appropriate risk mitigation; if a company develops custom software, the custom solution can present additional, unique risks and vulnerabilities.

Organizations with custom solutions should be on the lookout for logic weaknesses (e.g. buffer overflow vulnerabilities), and guard against malicious changes (e.g. backdoors) that can leave the system vulnerable to attacks.

As software development environments have become increasingly complex, it's important to review this area -- one of the biggest threats to an organization's security.

Computers understand 1s and 0s (binary), and each CPU has its own (machine) language. **Assembly language** is a way of using mnemonics to represent the basic instruction set of a CPU. **Assemblers**: tools that convert assembly language source code into machine code.

Third-generation programming languages, such as C/C++, Java, and Python, are known as high-level languages.

High-level languages allow developers to write instructions that better approximate human communication.

**Compiled language**: converts source code into machine-executable format.

Compiled code is generally less prone to manipulation by a third party; however, because the source code is not visible in compiled form, it is also harder for reviewers to detect embedded backdoors or other security flaws.

**Decompilers**: convert binary executable back into source code. **Disassemblers**: convert back into machine-readable assembly language (an intermediate step during the compilation process). **Interpreted language** uses an interpreter to execute; sourcecode is viewable; e.g. Python, R, JavaScript, VBScript.

**Object-oriented programming (OOP)** defines an object to be set of a software that offers one or more methods, internal to the object, that software external to that object can request to access; each method may require specific inputs and resources and may produce a specified set of outputs; focuses on the objects involved in an interaction.

OOP languages include C++, Java, and C#. Think of OOP as a group of objects that can be requested to perform certain operations or exhibit certain behaviors, working together to provide a system’s functionality or capabilities. OOP has the potential to be more reliable and to reduce the propagation of program change errors, and is better suited to modeling or mimicking the real world. Each object in the OOP model has methods that correspond to specific actions that can be taken on the object. Objects can also be subclasses of other objects and inherit methods from their parent class; the subclasses can use all the methods of the parent class and have additional class-specific methods.

From a security standpoint, object-oriented programming provides a black-box approach to abstraction.

#### OOP terms

**message** is a communication to or input of an object. **method**: internal code that defines the actions of an object.

**Behavior: results or output exhibited by an object**

Behaviors are the results of a message being processed through a method.

**class** is a collection of the common methods, from a set of objects that defines the behavior of those objects. **instance**: objects are instances of or examples of classes that contain their methods. **inheritance** occurs when the methods from a class (parent or superclass) are inherited by another subclass (child) or object. **delegation** is the forwarding of a request by an object to another object or delegate. **polymorphism** is the characteristic of an object that allows it to respond with different behaviors to the same message or method because of changes in external conditions.

**cohesion** describes the strength of the relationship between the purposes of the methods within the same class.

If all methods have similar purposes, there is high cohesion, and a sign of good design.

**Coupling: the level of interaction between objects**

Lower coupling: means less interaction. Lower coupling provides better software design because objects are more independent, and code is easier to troubleshoot and update.

<a id="subtopic-8-2-2"></a>

### 8.2.2 Libraries

**Software library** is a pre-written collection of components (classes, procedures, scripts etc) that do specific tasks, useful to other components (e.g. software libraries for encryption algorithms, managing network connections, or displaying graphics).

Shared software libraries contain reusable code, improving developers efficiency, and reducing the need to write well-known algorithms from scratch; often available as open source.

Shared libraries can also include many security issues (e.g. Heartbleed), and devs should be aware of the origins of the shared code that they use, and keep informed about any security vulnerabilities that might be discovered in these libraries.

<a id="subtopic-8-2-3"></a>

### 8.2.3 Tool sets

Forcing all devs to use the same toolset can reduce productivity and job satisfaction; however letting every dev choose their own tools and environment widens an organization's attack surface.

A better approach is to use a change advisory board to validate developer tool requirements, assess associated risks; if approved, the sec team monitors controls.

Developers use a variety of tools, and one of the most important is the IDE (defined below).

<a id="subtopic-8-2-4"></a>

### 8.2.4 Integrated Development Environment

**Integrated Development Environment (IDE)**: software applications, their control procedures, supporting databases, libraries and toolsets that provide a programmer or team what they need to specify, code, compile, test, and integrate code; IDEs provide developers with a single environment where they can write their code, test and debug, and compile it.

<a id="subtopic-8-2-5"></a>

### 8.2.5 Runtime

**RunTime Environments (RTE)** allows the portable execution of code across different operating systems or platforms without recompiling (e.g. Java Virtual Machine (JVM)).

This is known as portable code, which needs translation between each environment, the role of the RTE.

<a id="subtopic-8-2-6"></a>

### 8.2.6 Continuous Integration and Continuous Delivery (CI/CD)

**Continuous Integration and Continuous Delivery**: workflow automation processes and tools that help reduce, if not eliminate, the need for manual communication and coordination between the steps of a software development process.

**Continuous integration (CI)**: all new code is integrated into the rest of the system as soon as the developer writes it, merging it into a shared repo.

This merge triggers a batch of unit tests. If it merges without error, it's subjected to integration tests. CI improves software development efficiency by identifying errors early and often. CI also allows the practice of continuous delivery (CD).

**Continuous Delivery (CD)**: incrementally building a software product that can be released at any time; because all processes and tests are automated, code can be released to production daily or more often.

Continuous delivery and continuous deployment are both automation-heavy DevOps practices that build on CI; the key difference is in the final step of the release process: human intervention. Continuous Delivery: code is always in a deployable state, but deployment to production requires a manual approval step. Continuous Deployment: every change that passes automated testing is automatically deployed to production with no manual intervention.

CI/CD relies on automation and often third-party tools which can have vulnerabilities or be compromised. Secure practices such as threat modeling, least privilege, defense in depth, and zero trust can help reduce possible threats to these tools and systems.

<a id="subtopic-8-2-7"></a>

### 8.2.7 Software Configuration Management

**Concurrency** is the ability of a system to handle multiple simultaneous operations; managed through locking mechanisms that allow an authorized user to make changes and unlock the data element after changes are complete, preventing conflicts.

**Software Configuration Management (SCM)** is a product that identifies the attributes of software at various points in time and performs methodical change control for the purpose of maintaining software integrity and traceability throughout the SDLC.

SCM tracks config changes, and verifies that the delivered software includes all approved changes. SCM systems manage and track revisions made by multiple people against a single master software repository, providing concurrency management, versioning, and synchronization.

Auditing and logging of software changes mitigates risk to the organization by:

Providing a detailed record of all modifications made to software applications. Allowing security teams to identify suspicious activity. Quickly detect unauthorized changes and investigate potential security breaches. And take corrective actions, ultimately protecting the integrity and confidentiality of the organization's data and systems.

<a id="subtopic-8-2-8"></a>

### 8.2.8 Code repositories

Software development is a collaborative effort, and larger projects require teams of devs working simultaneously on different parts.

Code repositories support collaborations, acting as a central storage point for source code.

GitHub, Bitbucket, and SourceForge are examples of systems that provide version control, bug tracking, web hosting, release management, and communications functionality.

<a id="subtopic-8-2-9"></a>

### 8.2.9 Application security testing (e.g., static application security testing (SAST), dynamic application security testing (DAST), software composition analysis, Interactive Application Security Test (IAST))

**Static Application Security Testing (SAST)**: AKA static analysis, tools and technique to help identify software defects (e.g. data type errors, loop/structure bounds violations, unreachable code) or security policy violations and is carried out by examining the code without executing the program (or before the program is compiled).

The term SAST is generally reserved for automated tools that assist analysts and developers, whereas manual inspection by humans is generally referred to as code review. SAST allows devs to scan source code for flaws and vulnerabilities; it also provides a scalable method of security code review and ensuring that devs are following secure coding policies.

**Dynamic Application Security Testing (DAST)**: AKA dynamic analysis, is the evaluation of a program while running in real time.

Tools that execute the software unit, application or system under test, in ways that attempt to drive it to reveal a potentially exploitable vulnerability. DAST is usually performed once a program has cleared SAST and basic code flaws have been fixed. DAST enables devs to trace subtle logical errors that are likely to cause security problems, without the need to create artificial error-inducing scenarios. Dynamic analysis is also effective for compatibility testing, detecting memory leakages, identifying dependencies, and analyzing software without accessing the software’s actual source code.

**Software Composition Analysis (SCA)**: tools and techniques that identify open-source and third-party components in a codebase, catalog their versions and licenses, and flag known vulnerabilities; SCA is critical for managing software supply chain risk. **Interactive Application Security Testing (IAST)** is the combination of SAST and DAST such application testing is done on the running system (DAST), with access to source code (SAST).

### AI in this objective

**AI-assisted development.** Generated code is a candidate implementation, not trusted evidence of correctness. Apply review, dependency checks, and security tests in continuous integration and delivery (CI/CD). A generated explanation may also invent facts, so validate its claims against the actual code and behavior. [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).

### Apply this objective

**Question.** Harbor protects production servers but allows anyone to replace a build dependency. What risk remains?

**Reasoning.** Malicious or vulnerable code can enter through the build and then be deployed through the trusted release process. Restrict and verify dependencies and changes, protect pipeline credentials, and validate release artifacts.

<a id="objective-8-3"></a>

## 8.3 Assess the effectiveness of software security

Software security effectiveness is established through evidence about the product and the process that changes it. Audit trails show what changed and who authorized it; risk analysis connects weaknesses to consequences; testing checks selected behaviors. No single metric proves the absence of vulnerabilities.

Harbor should review whether significant findings are addressed, whether tests cover important security requirements, and whether changes introduce new risks. A large test count is less useful than evidence that the right questions were tested.

<a id="subtopic-8-3-1"></a>

### 8.3.1 Auditing and logging of changes

Applications should be configured to log details of errors and other security events to a centralized log repository.

The Open Web Application Security Project (OWASP) Secure Coding Practices suggest logging the following events:

Input/output validation failures. Authentication attempts, especially failures. Access control failures. Tampering attempts. Use of invalid or expired session tokens. Exceptions raised by the OS or applications. Use of admin privileges. Transport Layer Security (TLS) failures. Cryptographic errors. High-risk functionality (admin actions or use of admin privileges, access to sensitive data, creation/deletion of system-level objects, data import/export etc.).

<a id="subtopic-8-3-2"></a>

### 8.3.2 Risk analysis and mitigation

Risk management is at the center of secure software development, in particular regarding the mapping of identified risks and implemented controls.

This is a difficult part of secure software dev, especially related to auditing.

Threat modeling is important to dev teams, and particularly in DevSecOps.

Assessors are also interested in the linkages between the software dev and risk management programs.

Software projects should be tracked in the organization’s risk matrix, to ensure the dev team is connected to the broader risk management efforts, and not working in isolation.

### Apply this objective

**Question.** A release has twice as many automated tests as the previous release. Does that alone justify a security approval?

**Reasoning.** No. Evaluate the requirements exercised, findings, limitations, and remaining risks. Additional tests are useful when they improve relevant evidence, not merely because the count increased.

<a id="objective-8-4"></a>

## 8.4 Assess security impact of acquired software

Acquired software brings dependencies and responsibilities into the organization. Commercial, open-source, managed, and cloud offerings differ in available evidence, update control, support, licensing, and exit options. Open source is not automatically insecure, and commercial support is not a security guarantee.

Harbor should assess the product's function, access, data use, provenance, maintenance, and integration. Plan how to respond if a critical dependency is compromised or abandoned and how to preserve access to necessary information when the relationship ends.

An SBOM has become increasingly important for assessing the security impact of acquired software; recall from Domain 1 that an SBOM provides a formal record of all components, libraries, and dependencies within a software product, enabling organizations to quickly identify affected systems when new vulnerabilities are disclosed.

<a id="subtopic-8-4-1"></a>

### 8.4.1 Commercial-off-the-shelf (COTS)

**Defensive Programming**: design/coding allowing acceptable but sanitized data inputs to a system; lack of defensive programming measures can result in arbitrary code execution, misdirection of the program to other resources/locations, or reveal information useful to an attacker. **Certification**: comprehensive technical security analysis of a system to ensure it meets all applicable security requirements. **Commercial Off-the-Shelf (COTS)**: software elements, usually applications, that are provided as finished products (not intended for alteration by or for the end-user).

Most widely used COTS software products have been tested by security researchers (both benign and malicious).

Researching discovered vulnerabilities and exploits can help us understand how seriously the vendor takes security. For niche products, you should research vendor certifications, such as ISO/IEC 27034 Application Security. Other than secure coding certification, you can look for overall information security management system (ISMS) certifications such as ISO/IEC 27001 and FedRAMP (which are difficult to obtain, and show that the vendor is serious about security).

If you can talk with a vendor, look for processes like defensive programming, which is a software development best practice that means as code is developed or reviewed, they are constantly looking for opportunities for things to go badly.

E.g. treating all input routines as untrusted until proven otherwise.

<a id="subtopic-8-4-2"></a>

### 8.4.2 Open source

**Open-source software**: source code and design information is made public, and often using licenses that allow modification and refactoring.

Open source is typically released with licensing allowing code access and inspection so devs can look for security issues.

Typically, however, this means that there is no service or support that comes with the software and requires in-house support for configuration, and security testing. It also means that both open-source devs as well as adversaries are able to review the code for vulnerabilities. Outdated open-source dependencies can introduce significant risk. Also assess provenance, maintainer support, malicious changes, licensing, and integration; the greatest risk depends on the situation. An organization should develop processes to ensure that all open-source software is periodically updated, likely in a way that differs from the process for updating COTS.

<a id="subtopic-8-4-3"></a>

### 8.4.3 Third-party

**Security Assessment**: testing, inspection, and analysis to determine the degree to which a system meets or exceeds the required security posture; may assess whether an as-built system meets the requirements in its specs, or whether an in-use system meets the current perception of the real-world security threats.

**Third-party software**: (AKA outsourced software) is software made specifically for an organization by a third party.

Third-party software is not considered COTS, since the software is custom or customized. Third-party software may rely on open-source software, but since it's customized, it may have different or additional vulnerabilities. It's best practice to use a third-party to do an external audit and security assessment; this should be built into the vendor's contract, with passing the audit conditional for finalizing software purchase.

<a id="subtopic-8-4-4"></a>

### 8.4.4 Managed services (e.g., enterprise applications)

**Managed services** can include services and assets that are available from on-premises resources (e.g. within the organization) or cloud-based; as organizations move more functionality to the cloud, they reap cloud-based conveniences (e.g. pay only for on-demand resource use, easy scalability etc.) but lose a degree of control since a portion of cloud-based resources are outside the organization's control.

<a id="subtopic-8-4-5"></a>

### 8.4.5 Cloud services (e.g., Software as a Service (SaaS), Infrastructure as a Service (IaaS), Platform as a Service (PaaS))

**PERT**: chart that uses nodes to represent milestones or deliverables, showing the estimated time to move between milestones. As organizations continue to migrate to the cloud (SaaS, IaaS, PaaS), they should increase the security assessment of those services.

The top reasons for cloud breaches continue to be misconfigurations, lack of visibility into access settings, and poor access controls.

Cloud service providers have tools to help mitigate these issues, and organizations should consider bringing in third-party experts to help if they don't have the internal expertise.

**Anything as a Service (XaaS)**: catchall term referring to any type of computing service that provides value to customers via a cloud solution.

### AI in this objective

**ML dependencies.** Evaluate acquired ML libraries, frameworks, and model artifacts as software-supply-chain dependencies. [ISC2 AI guidance, Domain 8](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

Original application: before adding an unfamiliar model package to Harbor's build, identify its source, permissions, version, and maintenance owner. Confirm how the team can investigate or replace it if its behavior changes.

### Apply this objective

**Question.** A useful library has no active maintainer. What should Harbor evaluate before adopting it?

**Reasoning.** Evaluate its exposure, review and patch capability, alternatives, licensing, and long-term ownership. Adoption should include a credible maintenance and replacement plan rather than relying solely on present functionality.

<a id="objective-8-5"></a>

## 8.5 Define and apply secure coding guidelines and standards

Secure coding prevents a program from treating untrusted input as authority, instructions, or unrestricted resource requests. Validate inputs against expected structure and meaning, use safe interfaces, enforce authorization, manage errors, and protect secrets. The right control depends on the failure mechanism.

For example, parameterized database queries keep data separate from query instructions. Output encoding protects a particular output context and does not replace authorization. Harbor should connect each weakness to its cause, consequence, prevention, and a test showing the protection works.

**Secure Coding Guidelines and Standards**: best practices identified by a variety of software and security professionals, that when used correctly can dramatically reduce the number of exploitable vulnerabilities introduced during development.

<a id="subtopic-8-5-1"></a>

### 8.5.1 Security weaknesses and vulnerabilities at the source-code level

A source code vulnerability is a code defect providing a threat actor with an opportunity to compromise the security of a software system.

Source code vulnerabilities are caused by design or implementation flaws. **design flaw**: if dev did everything correctly, there would still be a vulnerability. **implementation flaw**: dev incorrectly implemented part of a good design.

#### The OWASP top 10 vulnerabilities (2025 edition)

Broken access control. Security misconfiguration. Software supply chain failures. Cryptographic failures. Injection. Insecure design. Authentication failures. Software or data integrity failures. Security logging and alerting failures. Mishandling of exceptional conditions.

<a id="subtopic-8-5-2"></a>

### 8.5.2 Security of Application Programming Interfaces (APIs)

**Application Programming Interface (API)** specifies the manner in which a software component interacts with other components.

APIs reduce the effort of providing secure component interactions by providing easy implementation for security controls. APIs reduce code maintenance by encouraging software reuse, and keeping the location of changes in one place. **Parameter validation**: ensuring that any API parameter is checked against being malformed, invalid, or malicious helps ensure API secure use; validation confirms that the parameter values being received by an application are within defined limits before they are processed by the system.

<a id="subtopic-8-5-3"></a>

### 8.5.3 Security coding practices

Secure coding practices can be summarized as standards and guidelines.

**standards**: mandatory activities, actions, or rules. **guidelines**: recommended actions or ops guidelines that provide flexibility for unforeseen circumstances. Organizations greatly reduce source code vulnerabilities by enforcing secure coding standards and maintaining coding guidelines that reflect best practices.

To be considered a standard, coding practice must meet the following: reduces the risk of a particular type of vuln; enforceable across all of an organization's software development efforts; verifiably implemented.

Secure coding standards, rigorously applied, is the best way to reduce source code vulnerabilities; coding standards ensure devs always do certain things in a certain way, while avoiding others.

Secure coding guidelines are recommended practices that tend to be less specific than standards.

E.g. consistently formatted code comments, or keeping code functions short/tight.

<a id="subtopic-8-5-4"></a>

### 8.5.4 Software-defined security

**Software-defined security (SDS or SDSec)** is a security model in which security functions such as firewalling, IDS/IPS, and network segmentation are implemented in software within an SDN environment.

One of the advantages of this approach is that sensors (for systems like IDS/IPS) can be dynamically repositioned depending on the threat. SDS provides a decoupling from physical devices, because it abstracts security functions into software that can run on any compatible physical or virtual infrastructure, critical for supporting cloud services dynamic scaling and virtualized data centers.

DevSecOps supports the concept of software-defined security, where security controls are actively managed into the CI/CD pipeline.

Also see Understanding CISSP Domain 8, Software Development Security - [part 1](https://blog.balancedsec.com/p/understanding-cissp-domain-8-software?r=1k08iw), and [part 2](https://blog.balancedsec.com/p/understanding-cissp-domain-8-software-597?r=1k08iw) on the source author's blog, [The Cyber Leader](https://blog.balancedsec.com/) (note that some articles require a subscription).

### AI in this objective

**Model hijacking and inference attacks.** A model hijacking attack redirects behavior toward an unauthorized purpose. An inference attack seeks protected information from observable behavior or outputs; ordinary inference simply means using a model. Test the software interface and enforce controls around it. [NIST adversarial ML taxonomy](https://csrc.nist.gov/News/2025/nist-ai-100-2-adversarial-machine-learning-taxonom).

### Apply this objective

**Question.** A developer filters apostrophes to prevent SQL injection. What is a stronger design?

**Reasoning.** Use parameterized queries or another appropriate safe database interface, with least-privileged database access and validation. Ad hoc character filtering is fragile and does not reliably separate data from executable query structure.

## Chapter review

Return to the Harbor examples and explain each decision without looking at the answer. Identify the asset or business activity, the relevant requirement, the possible harm, the responsible owner, and the evidence that would support the decision. If two controls appear interchangeable, explain the different failure each addresses.

### Connections and common distinctions

Static, dynamic, and composition analysis inspect different aspects of software. A successful build is not a security approval. Secure coding does not replace architecture or operations. Connect development risks to Domain 1 and verify controls using Domain 6.

### Review questions and explained answers

**1. How would you explain this domain to Harbor's service owner?** Describe the decisions it governs using the examples in this chapter. A useful answer connects technical measures to customer service, accountability, and evidence rather than listing product names.

**2. Which assumption in the chapter's examples would most change your recommendation if it were false?** Choose a concrete assumption, such as data sensitivity, allowed downtime, or an identity's authority. Explain how a different assumption changes the relevant control or test. More than one answer can be sound when justified.

**3. How does adding the AI assistant change the work?** Follow the AI lessons in this chapter. Identify an additional asset, failure, or decision and describe its owner and verification method. The assistant still operates within ordinary governance, access, data, and recovery requirements.

### AI application review

**Question.** A generated feature uses a new ML dependency and passes a happy-path test. Is it ready for release?

**Reasoning.** Review generated code and dependencies, run appropriate security checks in the pipeline, and test misuse and information-disclosure behavior. Verify provenance and maintenance responsibility. Consider model hijacking and inference attacks separately from ordinary inference, then document remaining risks and the release decision.

## Term index

This index points to explanations in the chapter. Terms retain the source guide's spelling where useful for recognition; corrected concepts are explained in context.

- [Acceptance](#subtopic-8-1-4)
- [Accreditation](#subtopic-8-2-1)
- [ACID Test](#subtopic-8-2-1)
- [Aggregation](#subtopic-8-2-1)
- [Agile methodology](#subtopic-8-1-1)
- [Agile Unified Process (AUP)](#subtopic-8-1-1)
- [AI-assisted development](#objective-8-2)
- [Anything as a Service (XaaS)](#subtopic-8-4-5)
- [Application Programming Interface (API)](#subtopic-8-5-2)
- [Arbitrary code](#subtopic-8-2-1)
- [Assemblers](#subtopic-8-2-1)
- [Assembly language](#subtopic-8-2-1)
- [behavior](#subtopic-8-2-1)
- [Buffer overflow](#subtopic-8-2-1)
- [Bypass attack](#subtopic-8-2-1)
- [CAB](#subtopic-8-1-2)
- [Certification](#subtopic-8-4-1)
- [Change Control](#subtopic-8-1-4)
- [Citizen programmers](#subtopic-8-2-1)
- [class](#subtopic-8-2-1)
- [Code protection/logic hiding](#subtopic-8-2-1)
- [Code reuse](#subtopic-8-2-1)
- [cohesion](#subtopic-8-2-1)
- [Commercial Off-the-Shelf (COTS)](#subtopic-8-4-1)
- [Compiled language](#subtopic-8-2-1)
- [Complete coverage](#subtopic-8-2-1)
- [Concurrency](#subtopic-8-2-7)
- [Configuration Control](#subtopic-8-2-1)
- [Continuous Delivery (CD)](#subtopic-8-2-6)
- [Continuous integration (CI)](#subtopic-8-2-6)
- [Continuous Integration and Continuous Delivery](#subtopic-8-2-6)
- [CORBA](#subtopic-8-2-1)
- [coupling](#subtopic-8-2-1)
- [Covert Channels/Paths](#subtopic-8-2-1)
- [customer collaboration](#subtopic-8-1-1)
- [Data Contamination](#subtopic-8-2-1)
- [Data Lake](#subtopic-8-2-1)
- [Data Mining](#subtopic-8-2-1)
- [Data Modeling](#subtopic-8-2-1)
- [Data Protection and Data Hiding](#subtopic-8-2-1)
- [Data Type Enforcement](#subtopic-8-2-1)
- [Data Warehouse](#subtopic-8-2-1)
- [Data-centric Threat Modeling](#subtopic-8-2-1)
- [Decompilers](#subtopic-8-2-1)
- [Defensive Programming](#subtopic-8-4-1)
- [delegation](#subtopic-8-2-1)
- [design flaw](#subtopic-8-5-1)
- [Design Reviews](#subtopic-8-2-1)
- [DevOps (Development and Operations)](#subtopic-8-1-1)
- [DevSecOps](#subtopic-8-1-1)
- [Dirty read](#subtopic-8-2-1)
- [Disassemblers](#subtopic-8-2-1)
- [Dynamic Application Security Testing (DAST)](#subtopic-8-2-9)
- [Dynamic Systems Development Model (DSDM)](#subtopic-8-1-1)
- [Emergent Properties](#subtopic-8-2-1)
- [Encapsulation](#subtopic-8-2-1)
- [Executable/Object Code](#subtopic-8-2-1)
- [Extreme Programming (XP)](#subtopic-8-1-1)
- [Functional requirements](#subtopic-8-2-1)
- [guidelines](#subtopic-8-5-3)
- [Hierarchical database model](#subtopic-8-2-1)
- [IDEAL Model](#subtopic-8-1-2)
- [implementation flaw](#subtopic-8-5-1)
- [individuals and interactions](#subtopic-8-1-1)
- [Infrastructure as Code (IaC)](#subtopic-8-2-1)
- [inheritance](#subtopic-8-2-1)
- [Instance](#subtopic-8-2-1)
- [instance](#subtopic-8-2-1)
- [Integrated Development Environment (IDE)](#subtopic-8-2-4)
- [Integrated Product and Process Development (IPPD)](#subtopic-8-2-1)
- [Integrated Product Team (IPT)](#subtopic-8-1-5)
- [Interactive Application Security Testing (IAST)](#subtopic-8-2-9)
- [Interpreted language](#subtopic-8-2-1)
- [Isolation](#subtopic-8-2-1)
- [Kanban](#subtopic-8-1-1)
- [Knowledge Discovery in Database (KDD)](#subtopic-8-2-1)
- [Knowledge Management](#subtopic-8-2-1)
- [Level 1: Initial](#subtopic-8-1-2)
- [Level 2: Repeatable](#subtopic-8-1-2)
- [Level 3: Defined](#subtopic-8-1-2)
- [Level 4: Managed](#subtopic-8-1-2)
- [Level 5: Optimizing](#subtopic-8-1-2)
- [Level of abstraction](#subtopic-8-2-1)
- [Living off the land](#subtopic-8-2-1)
- [Malformed input attack](#subtopic-8-2-1)
- [Managed services](#subtopic-8-4-4)
- [Markup Language](#subtopic-8-2-1)
- [message](#subtopic-8-2-1)
- [Metadata](#subtopic-8-2-1)
- [method](#subtopic-8-2-1)
- [ML dependencies](#objective-8-4)
- [Mobile code (executable content)](#subtopic-8-2-1)
- [Model hijacking and inference attacks](#objective-8-5)
- [Modified prototype model](#subtopic-8-2-1)
- [Network database model](#subtopic-8-2-1)
- [Nonfunctional requirements](#subtopic-8-2-1)
- [Object](#subtopic-8-2-1)
- [Object-oriented database model](#subtopic-8-2-1)
- [Object-oriented programming (OOP)](#subtopic-8-2-1)
- [Object-oriented security](#subtopic-8-2-1)
- [Object/Memory reuse](#subtopic-8-2-1)
- [Open-source software](#subtopic-8-4-2)
- [Pair programming](#subtopic-8-2-1)
- [Parameter validation](#subtopic-8-5-2)
- [Pass-around reviews](#subtopic-8-2-1)
- [PERT](#subtopic-8-4-5)
- [Polyinstantiation](#subtopic-8-2-1)
- [polymorphism](#subtopic-8-2-1)
- [Procedural programming](#subtopic-8-2-1)
- [Query attack](#subtopic-8-2-1)
- [Ransom attack](#subtopic-8-2-1)
- [Rapid Application Development (RAD)](#subtopic-8-1-1)
- [Rational Unified Process (RUP)](#subtopic-8-1-1)
- [Refactoring](#subtopic-8-2-1)
- [Regression testing](#subtopic-8-2-1)
- [Relational database model](#subtopic-8-2-1)
- [Release Control](#subtopic-8-1-4)
- [Representational State Transfer (REST)](#subtopic-8-2-1)
- [Reputation monitoring](#subtopic-8-2-1)
- [Request Control](#subtopic-8-1-4)
- [responding to change](#subtopic-8-1-1)
- [Runtime Application Security Protection (RASP)](#subtopic-8-2-1)
- [RunTime Environments (RTE)](#subtopic-8-2-5)
- [Scaled Agile Framework® (SAFe)](#subtopic-8-1-1)
- [Scrum](#subtopic-8-1-1)
- [SDLC](#subtopic-8-1-1)
- [Secure Coding Guidelines and Standards](#objective-8-5)
- [Security Assessment](#subtopic-8-4-3)
- [Software Assurance Maturity Model (SAMM)](#subtopic-8-1-2)
- [Software Composition Analysis (SCA)](#subtopic-8-2-9)
- [Software Configuration Management (SCM)](#subtopic-8-2-7)
- [Software library](#subtopic-8-2-2)
- [Software Quality Assurance](#subtopic-8-1-2)
- [Software-defined security (SDS or SDSec)](#subtopic-8-5-4)
- [Source code](#subtopic-8-2-1)
- [Spiral model](#subtopic-8-1-1)
- [Spyware/Adware](#subtopic-8-2-1)
- [standards](#subtopic-8-5-3)
- [Static Application Security Testing (SAST)](#subtopic-8-2-9)
- [Strong data typing](#subtopic-8-2-1)
- [SW-CMM](#subtopic-8-1-2)
- [Third-party software](#subtopic-8-4-3)
- [Threat surface](#subtopic-8-2-1)
- [TOCTOU attack](#subtopic-8-2-1)
- [Trapdoor/backdoor](#subtopic-8-2-1)
- [UAT](#subtopic-8-1-1)
- [V-Model](#subtopic-8-1-1)
- [Waterfall](#subtopic-8-1-1)
- [working software](#subtopic-8-1-1)
- [XML](#subtopic-8-2-1)

## Sources and further reading

- [Original Domain 8 objectives and notes](../CISSP-Domain-8-2024+Objectives.md) by the repository's contributors; adapted under the repository license.
- [ISC2 CISSP exam outline and AI domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).
- [ISC2 AI guidance announcement](https://www.isc2.org/Insights/2026/04/ISC2-Publishes-Exam-Guidance-AI).
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

Additional references appear alongside the relevant concepts. Official Study Guide chapter references in the original objective files remain available for comparison.
