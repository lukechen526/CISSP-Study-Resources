<a id="domain-5"></a>

# Domain 5: Identity and Access Management

Exam weight: 13%. Study edition: September 2026.

## Start here

Identity and access management determines who or what may perform an action on a resource. You will learn to distinguish identity proofing, authentication, authorization, and accountability, then maintain access through enrollment, use, review, and removal. The same principles apply to people and automated services.

This chapter follows the published Domain 5 objectives. Read the opening explanation of each objective first, then the detailed lessons, and finish with its application check. Three-part numbers identify subtopics retained from the source guide. The examples use Harbor Services, a small organization launching a customer portal and an AI support assistant.

Artificial intelligence (AI) is the broad field of systems performing tasks associated with intelligence. Machine learning (ML) builds models from examples during training; inference uses a trained model to produce an output. A large language model (LLM) produces language using learned numerical parameters called model weights. These terms identify components and processes to protect, rather than establish that a system is correct or trustworthy.

The AI additions apply [ISC2's domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline) to existing objectives. Detailed placement and Harbor scenarios are editorial teaching choices. Named historical technologies remain useful for comparison; their inclusion is not a recommendation to deploy them.

## Chapter navigation

- [5.1 Control physical and logical access to assets](#objective-5-1)
- [5.2 Design identification and authentication strategy (e.g., people, devices, and services)](#objective-5-2)
- [5.3 Federated Identity with a third-party service](#objective-5-3)
- [5.4 Implement and manage authorization mechanisms](#objective-5-4)
- [5.5 Manage the identity and access provisioning lifecycle](#objective-5-5)
- [5.6 Implement authentication systems](#objective-5-6)

<a id="objective-5-1"></a>

## 5.1 Control physical and logical access to assets

Access control connects a subject to an object through an allowed operation. A person, program, or service may be a subject; a file, application, device, or facility may be an object. Reading a record, updating it, and administering its storage are different privileges.

At Harbor, a support representative may need to read a customer's contact details without changing billing rules or administering the database. Physical and logical controls should support the same protection goal so that one route does not bypass the other.

Controlling access to assets (assets are anything of value to the organization); tangible assets are things you can touch, and non-tangible assets are things like information and data; controlling access to assets is a central theme of security. Understand that there is no security without physical security: admin, technical and logical access controls aren't effective without control over the physical env. Understand that identity is the new perimeter.

#### Understand what assets you have, and how to protect them

**physical security controls**: such as perimeter security and environmental controls.

Control access and the environment.

**logical access controls**: automated systems that authentication or deny access based on verification that identity presented matches that which was previously approved; technical controls used to protect access to information, systems, devices, and applications.

Includes authentication, authorization, and permissions. Permissions help ensure only authorized entities can access data. Logical controls restrict access to config settings on systems/networks to only authed individuals. Applies to on-prem and cloud.

In addition to personnel, assets can be information, systems, devices, facilities, applications or services.

<a id="subtopic-5-1-1"></a>

### 5.1.1 Information

An organization’s information includes all of its data, stored in simple files (on servers, computers, and small devices), or in databases.

<a id="subtopic-5-1-2"></a>

### 5.1.2 Systems

An organization’s systems include anything that provide one or more services; a web server with a database is a system; permissions assigned to user and system accounts control system access.

<a id="subtopic-5-1-3"></a>

### 5.1.3 Devices

Devices refer to any computing system (e.g. routers & switches, smartphones, laptops, and printers); BYOD has been increasingly adopted, and the data stored on the devices is still an asset to the organization.

<a id="subtopic-5-1-4"></a>

### 5.1.4 Facilities

Any physical location, building, rooms, complexes etc; physical security controls are important to help protect facilities.

<a id="subtopic-5-1-5"></a>

### 5.1.5 Applications

Apps provide access to data; permissions are an easy way to restrict logical access to applications.

<a id="subtopic-5-1-6"></a>

### 5.1.6 Services

The point of identity management is to control access to any asset including data, systems, and services; services include a wide range of process functionality such as printing, end-user support, network capacity etc; as above, access control is important to secure these services.

### Apply this objective

**Question.** A visitor cannot sign in to the portal but can enter an unlocked equipment room. Is logical access control enough?

**Reasoning.** No. Physical access may expose storage, consoles, or network equipment. Protect the asset through all relevant routes, using physical and logical controls that reinforce one another.

<a id="objective-5-2"></a>

## 5.2 Design identification and authentication strategy (e.g., people, devices, and services)

Identification is a claim; authentication supplies evidence for the claim. Authorization decides permitted actions, and accounting records relevant activity. Identity proofing establishes an identity at enrollment, while session management maintains and ends the authenticated interaction.

Authentication factors should be independent when multiple factors are required. Two passwords remain two examples of knowledge, not two different factors. Biometrics introduces false acceptance and false rejection tradeoffs; stronger authentication also needs usable recovery and credential management.

**Identification** is the process of a subject claiming, or professing an identity.

**Authentication**: verifies the subject’s identity by verifying an identity through knowledge, ownership, or characteristic; comparing one or more factors against a database of valid identities, such as user accounts.

A core principle with authentication is that all subjects must have unique identities. Identification and authentication occur together as a single two-step process. Users identify themselves with usernames and authenticate (or prove their identity) with passwords.

<a id="subtopic-5-2-1"></a>

### 5.2.1 Groups and Roles

**Whaling attack**: phishing attack targeting highly-placed officials/private individuals with sizeable assets authorizing large-fund wire transfers. **Template** is a digital representation of someone's unique biometric features (i.e. a one-way math function representing biometric data); templates can be used as "1:N" for identification (where user's template is used to search for the identity of the user), or "1:1" for authentication (where the user is identified and the template is used as a factor to authenticate the user). **Synchronous token** (authentication by ownership hard/soft token): both the token generator and authentication server generate the same token or one-time password every 30-60 seconds (see asynchronous token).

**Smart card**: authentication by ownership factor that contains an embedded integrated circuit (IC) chip that generates unique authentication data with every transaction (see memory card).

#### Seven Laws of Identity

1: User control and consent: identity systems should only reveal user-identifying information with the user's consent. 2: Minimal disclosure for a constrained use: the identity system should disclose the least identifying information possible. 3: Justifiable parties: systems should only disclose information to parties that have a justified need. 4: Directed identity: highlights the need for both public and private identifiers, giving individuals control of their identities and how they establish trust. 5: Pluralism of operators and technologies: identity systems should interoperate with agreed-upon protocols and a unified user experience.

6: Human integration: businesses should establish very reliable communication between a system and users and test safeguards regularly. 7: Consistent experience across context: the unifying identity system should guarantee users a simple, consistent experience, allowing users to decide what identity to use in what context.

**Self-service identity management**: elements of the identity management lifecycle which the end-user (identity in question) can initiate or perform on their own (e.g. password reset, changes to challenge questions etc). **Passwords authentication** is the weakest form of authentication, but password policies help increase security by enforcing complexity and history requirements. **Memory card**: authentication by ownership factor typically uses a magnetic strip as memory, where the same data is read from the strip with every transaction.

**FAR**: False Acceptance Rate (Type 2) is the probability of incorrectly authenticating a claimed identity as legit, recognizing and granting access on that basis; expressed as a percentage.

Remember: A Type 1 error is like being rejected at your own front door; Type 2 error is like letting a stranger in.

**FRR**: False Rejection Rate (Type 1) is the probability of incorrectly denying authentication to a legit identity and therefore denying access; expressed as a percentage. **Cross-Site Request Forgery (CSRF)**: (AKA XSRF) an attack that forces authenticated users to submit a request to a Web application against which they are currently authenticated; in CSRF attack the intended target is the web application itself; the attack exploits the trust that the web application has in the user's browser, and by tricking the authentication'd user into submitting a forged request, the attacker can cause the web application to perform actions as if it were initiated by the legit user.

**Crossover Error Rate (CER)** identifies the accuracy of a biometric method, and is the point at which false acceptance rate (FAR or Type 2) equals the false rejection rate (FRR or Type 1) for a given sensor, in a given system and context; it is the optimal point of operation if the potential impacts of both types of errors are equivalent.

A **lower CER indicates a more accurate biometric system**.

**CAS**: Central Authentication Service (an SSO implementation). **CAPTCHA**: Completely Automated Public Turing test to tell Computers and Humans Apart is a security measure used to protect against account creation automation and spam & brute-force password decryption attacks. **Asynchronous token** (authentication by ownership hard/soft token): involves a challenge and response; they are more complicated (and expensive), but also more secure (see synchronous token). **ADFS**: identity access solution that provides client computers (internal or external to your network) with seamless SSO access to protected Internet-facing applications or services, even when the user accounts and applications are located in completely different networks or organizations.

Single sign-on (SSO) technologies allow users to authenticate once and access any resources in a network or the cloud, without authenticating again.

The three primary authentication factors are authentication by knowledge (something you know), authentication by ownership (something you have), and authentication by characteristic (something you are); types 4 and 5 are often considered supplementary or contextual factors rather than primary authentication types.

Something you know: Type 1 authentication (passwords, pass phrase, PIN etc). Something you have: Type 2 authentication (ID, passport, smart card, token, cookie on PC etc). Something you are: Type 3 authentication, includes biometrics (fingerprint, iris or retinal scan, facial geometry etc.). Somewhere you are: Type 4 authentication (IP/MAC address). Something you do: Type 5 authentication (signature, pattern unlock).

**Authenticator Assurance Levels (AAL)** is a measure of the robustness of the authentication process; AAL levels are ranked from AAL1 (least robust) to AAL3 (most robust), and described in [NIST 800-63-3b](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf).

AAL1 (some assurance that the user controls an authenticator bound to their account): allows single-factor or multi-factor authentication, with less stringent requirements on authenticator types. AAL2 (high confidence): requires MFA, and must be resistant to replay attacks. AAL3 (very high confidence): requires hardware-based MFA, and mandates verifier impersonation and phishing resistance.

The identity and Access Management (IAM) domain focuses on issues related to granting and revoking privileges to access data or perform actions on systems, and comprises ~13% of the exam.

**Roles** is a set of permissions that correspond to a job function within an organization, rather than a group of users; a user is assigned a role, and granted the permissions associated with that role.

Another way of saying this is that roles are function-centric, for instance say a helpdesk analyst, level-1, is a specific role that defines the specific permission available. Role-based access means that a role with specific permissions is created and then assigned to someone in that role or job.

**Groups** is a group is a collection of users, and admins can assign permissions to the group instead of assigning permissions to individual users; this makes it easier to manage larger numbers of users.

Groups are user-centric, focusing on the collective identity of that group of users.

Identity and access management is a collection of processes and technologies that are used to control access to critical assets; its purpose is the management of access to information, systems, devices, and facilities.

Identity Management (IdM) implementation techniques generally fall into two categories:

**centralized access control**: implies a single entity within a system performs all authorization verification.

Potentially creates a single point of failure; small team can manage initially, and can scale to more users.

**decentralized access control**: (AKA distributed access control) implies several entities located throughout a system perform authentication verification.

Requires more individuals or teams to manage, and admin may be spread across numerous locations. Difficult to maintain consistency. Changes made to any individual access control point needs to be repeated at others.

With ubiquitous mobile computing and anywhere, anytime access (to applications & data), identity is the "new perimeter".

<a id="subtopic-5-2-2"></a>

### 5.2.2 Authentication, Authorization and Accounting (AAA) (e.g., multi-factor authentication (MFA), password-less authentication)

**Subject**: entities, such as users, that access passive objects. **Objects**: things a subject accesses, such as files; a user is a subject who accesses objects while performing some action or accomplishing a task. **Identification** is the process of a subject claiming, or professing, an identity; subjects claim an identity through identification. **Access Control System**: ensuring access to assets is authorized and restricted based on business and security requirements. **Accountability**: after authenticating subjects, systems authorize access to objects based on their proven identity; auditing logs and audit trails record events, including the identity of the subject performing the action; the combination of effective identification, authentication, and auditing provides accountability; note that the **principle of access control** is accountability.

**Access control services**: (AKA AAA services) identification, authentication, authorization, and accountability.

The four key access control services: Identification (assertion of identity), Authentication (verification of identity), Authorization (definition of access), Accountability (responsibility of actions).

AAA is the same principles of Authentication, Authorization, and using the word Accounting instead of Accountability (but it's the same principle). And remember that the three factors of authentication that you need to understand is knowledge, ownership, and characteristic (see above).

Two important security elements in an access control system are authorization and accountability.

**Authorization**: subjects are granted access to objects based on proven identities; the level of access defined for the identified and authenticated user or process. **Accountability AKA Principle of Access Control**: proper identification, authentication, and authorization that is logged and monitored; users and other subjects can be held accountable for their actions when auditing is implemented; accountability is maintained for individual subjects through the use of auditing; logs record user activities and users can be held accountable for their logged actions; this encourages good user behavior and compliance with the organization's security policy; also see definitions/interpolations in Domain 2, and above.

**Auditing**: tracks subjects and records when they access objects, creating an audit trail in one or more audit logs. Auditing provides accountability.

FIDO2 and WebAuthn are related technical standards that enable phishing-resistant, passwordless authentication across the internet.

**FIDO2 (Fast IDentity Online 2)** is an overarching project and set of specifications developed by the FIDO Alliance designed to replace passwords with cryptographic keys. **WebAuthn (Web Authentication)** is a specific web API standard developed by the World Wide Web Consortium (W3C) in collaboration with FIDO that allows websites (known as "Relying Parties") to communicate directly with a user’s browser to perform secure authentication.

**Single-factor authentication** is any authentication using only one proof of identity. **Two-factor authentication (2FA)** requires two different proofs of identity.

**Multifactor authentication (MFA)** is any authentication using two or more factors.

Multifactor authentication must use multiple types or factors, such as something you know and something you have. Requiring users to enter a password and a PIN is NOT multifactor (both are something you know).

#### Two-factor methods

**Hash Message Authentication Code (HMAC)** includes a hash function used by the HMAC-based One-Time Password (HOTP) standard to create onetime passwords.

**Time-based One-Time Password (TOTP)**: similar to HOTP, but uses a timestamp and remains valid for a certain time frame (e.g. 30 or 60 seconds).

E.g. phone-based authenticator application, where your phone is mimicking a hardware TOTP token (combined with userid/password is considered two-factor or two-step authentication).

**Email challenge**: popular method, used by websites, sending the user an email with a PIN. Short Message Service (SMS): to send users a text with a PIN is another 2-factor method; note that NIST SP 800-63B points out vulnerabilities, and deprecates use of SMS as a two-factor method for federal agencies.

**Password-less authentication** is a method of verifying a user's identity without requiring them to enter a password; uses alternate verification forms like biometrics, security tokens, or mobile device.

This is an important topic, because password use (and misuse) provide many security headaches and problems.

#### Advantages of password-less authentication include

Increased security. Improved user convenience. Reduction risk of phishing: if attacker gains access to a password, but password-less authentication makes it much more difficult for the attacker to access the associated device (say if password-less authentication is via mobile device).

#### Disadvantages of password-less authentication

Dependency on devices (e.g. if via mobile phone, that device is required for access). Biometric issues associated with reliability and privacy. Implementation costs associated with additional hardware devices etc.

<a id="subtopic-5-2-3"></a>

### 5.2.3 Session management

**Session**: what is created as a result of a successful user identification, authentication, and authorization process; represents the connection and interaction between a user and a system. **Session management** is the management of sessions created by successful user identification, authentication, and authorization process; session management help prevent unauthorized access by closing unattended sessions; developers commonly use web frameworks to implement session management, allowing devs to ensure sessions are closed after they become inactive for a period of time. Session management is important to use with any type of authentication system to prevent unauthorized access.

#### Session termination strategies

Schedule limitations: setting hours when a system is available. Login limitation: preventing simultaneous logins using the same userID. Time-outs: session expires after a set amount of inactivity. Screensavers: activated after a period of inactivity, requiring re-authentication.

Session termination and re-authentication helps to prevent or mitigate session hijacking. The Open Web Application Security Project (OWASP) publishes “cheat sheets” that provide application developers with specific recommendations.

<a id="subtopic-5-2-4"></a>

### 5.2.4 Registration, proofing, and establishment of identity

**Knowledge-based authentication (KBA)** is a process of asking a user a series of questions based on their history that is recorded in authoritative sources; e.g. a bank asks a customer a series of questions about past addresses they've lived, and current payment amounts for car/mortgage. **Identity proofing**: AKA registration, process of confirming someone is who they claim to be; process of collecting/verifying information about someone who has requested access/credential/special privilege to establish a relationship with that person; identity proofing includes knowledge-based authentication and cognitive passwords, where a user is asked a series of questions that only they would know.

Within an organization, new employees prove their identity with appropriate documentation during the hiring process.

In-person identity proofing includes things like passport, DL, birth cert etc.

Online organizations often use **knowledge-based authentication (KBA)** for identity-proofing of someone new (e.g. a new customer creating a new bank/savings account).

Example questions include past vehicle purchases, amount of mortgage payment, previous addresses, DL numbers. They then query authoritative information (e.g. credit bureaus or gov agencies) for matches.

**Cognitive Passwords**: security questions that are gathered during account creation, which are later used as questions for authentication (e.g. name of pet, color of first car etc).

One of the flaws associated with cognitive passwords is that the information is often available on social media sites or general internet searches.

<a id="subtopic-5-2-5"></a>

### 5.2.5 Federated Identity Management (FIM)

Federated Identity Management (FIM) systems (a form of SSO) are often used by cloud-based applications. A federated identity links a user’s identity in one system with multiple identity management systems.

FIM allows multiple organizations to join a federation or group, agreeing to share identity information.

Users in each organization can log in once in their own organization, and their credentials are matched with a federated identity. Users can then use this federated identity to access resources in any other organization within the group. Where each organization decides what resources to share.

Methods used to implement federated identity management systems include: Security Assertion Markup Language (SAML); OAuth; OpenID Connect (OIDC).

Cloud-based federation typically uses a third-party service to share federated identities. Federated identity management systems can be hosted on-premises, in the cloud, or in a combination of the two as a hybrid system.

<a id="subtopic-5-2-6"></a>

### 5.2.6 Credential management systems (e.g., Password vault)

**Credential management systems**: provide storage space for usernames and passwords.

These systems help developers easily store usernames/passwords and retrieve them when a user revisits a website, allowing users to log on automatically to a site without entering their credentials again.

The World Wide Web Consortium (W3C) published the Credential Management Level 1 API as a working draft in January 2019, which many browsers have adopted.

Some federated identity management solutions use the Credential Management API, allowing web applications to implement SSO using a federated identity provider.

E.g. using your Google or Facebook account to sign into Zoom.

**Password vault (AKA password manager)** is a system meant to store and manage credentials; credentials are typically kept in an encrypted database protected by a master password or key.

In modern life we need access to many different systems, and re-using one (or even a few) passwords with many systems means that if an attacker deduces your password, they then have access to many systems (and much of your data). Password managers make it much easier to create strong and different passwords for each system, without the need to memorize them. The downside of course is that if your master password is compromised, the attacker will have access to all your systems.

<a id="subtopic-5-2-7"></a>

### 5.2.7 Single Sign On (SSO)

**Single Sign-On (SSO)** is a centralized access control technique allowing a subject to be authenticated once on a system and access multiple resources without authenticating again.

#### Advantages of using SSO include

Reduces the number of passwords that users need to remember, and they are less likely to write them down. Eases administration by reducing the number of accounts.

#### Disadvantages

SSO creates a **single point of compromise** — if the SSO credential is compromised, all linked resources are exposed (which is why requiring MFA for SSO credential is important).

Within an organization, a central access control system, such as a directory service, is often used for SSO.

**directory service** is a centralized database that includes information about subjects and objects, including authentication data. Many directory services are based on the Lightweight Directory Access Protocol (LDAP).

<a id="subtopic-5-2-8"></a>

### 5.2.8 Just-In-time (JIT)

Federated identity solutions that support just-in-time (JIT) provisioning automatically create the relationship between two entities so that new users can access resources. JIT provisioning creates user accounts on third-party sites the first time a user logs into the site; JIT reduces the admin workload. A JIT solution creates the connection without any administrative intervention. JIT systems commonly use SAML to exchange required data.

### AI in this objective

**Adaptive authentication.** Behavioral biometrics and contextual signals can inform an authentication decision. Evaluate error rates, privacy, and recovery as well as convenience. [ISC2 AI guidance, Domain 5](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

### Apply this objective

**Question.** Harbor requires a password and a second secret question. Is this multi-factor authentication?

**Reasoning.** No. Both are knowledge factors. A design requiring distinct factors might combine a password with a protected authenticator, while also securing enrollment, recovery, and session handling.

<a id="objective-5-3"></a>

## 5.3 Federated Identity with a third-party service

Federation allows one organization or service to rely on identity information supplied by another. The identity provider authenticates the user and supplies an assertion or token; the relying service checks the evidence and applies its own access policy. Single sign-on describes the user experience and does not automatically mean that every application has the same permissions.

Harbor should validate who issued the assertion, who it is intended for, whether it is current, and how it is protected. Trust agreements, account linkage, and termination behavior are as important as the sign-in screen.

<a id="subtopic-5-3-1"></a>

### 5.3.1 On-premise

#### In a purely on-premise scenario, all infra is managed internally

IdP: typically an internal directory service (e.g., AD). Federated identity management can be hosted on-premise, and typically provides an organization with the most control.

Requires in-house expertise and capital investments.

<a id="subtopic-5-3-2"></a>

### 5.3.2 Cloud

**IDaaS**: cloud-based service that brokers IAM functions to target systems on customers' premise and/or in the cloud; refers to implementation/integration of identity services in a cloud-based environment; services include provisioning, administration, SSO, MFA, directory services, on-prem and in the cloud.

Cloud-based applications use federated identity management (FIM) systems, which are a form of SSO.

IdP: In a cloud-only scenario, identity management is delivered via third-party (IDaaS). Cloud-based federation typically uses a third-party service to share federated identities (e.g. training sites use federated SSO systems) commonly matching the user's internal login ID with a federated identify.

Requires relinquishing some direct control and relying on third-party uptime and security.

<a id="subtopic-5-3-3"></a>

### 5.3.3 Hybrid

A hybrid federation is a combination of a cloud-based solution and an on-premise solution.

IdP: identity typically originates on-prem (e.g., AD) with a cloud service acting as the central IdP.

Requires careful integration, and is the most complex scenario to manage.

### Apply this objective

**Question.** A valid identity assertion was issued for a different application. Should Harbor's portal accept it because the issuer is trusted?

**Reasoning.** No. It must validate the intended audience and other required conditions. Trusting an issuer does not make every assertion it issues valid for every relying service.

<a id="objective-5-4"></a>

## 5.4 Implement and manage authorization mechanisms

Authorization translates policy into decisions about actions. Different models express different rules: ownership, mandatory labels, job roles, attributes, or risk context. Compare them by asking who controls the policy, what inputs it uses, and how the decision is enforced.

A policy decision point evaluates a request; a policy enforcement point carries out the result. The application must enforce the decision on the actual resource, not merely hide a button. Harbor's portal should check access whenever a customer record is requested.

Authorization ensures that the requested activity or object access is possible, given the authenticated identity's privileges.

E.g. ensuring that users with appropriate privileges can access resources.

#### Common authorization mechanisms include

Implicit deny. Access control lists. Access control matrixes. Capability tables. Constrained interfaces. Content-dependent controls. Context-dependent controls.

<a id="subtopic-5-4-1"></a>

### 5.4.1 Role Based Access Control (RBAC)

**XST**: Cross-Site Tracing (XST) attack involves the use of Cross-site Scripting (XSS) and the TRACE or TRACK HTTP methods; this could potentially allow the attacker to steal a user's cookies.

**XSS**: Cross-Site Scripting (XSS) essentially uses reflected input to trick a user's browser into executing untrusted code from a trusted site; these attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites; XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user; flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

**Split-response attack**: attack that causes the client to download content that was not an intended element of a requested web page, storing it in browser cache. **SESAME**: Secure European System for Applications in a Multi-Vendor Environment an improved version of Kerberos; a protocol for SSO (like Kerberos), but has the advantage of supporting both symmetric and asymmetric cryptography (and therefore solves Kerberos' problem of key distro); it also issues multiple tickets mitigating attacks like TOCTOU. **Server-Side Request Forgery (SSRF)**: if an API fetches a remote resource without validating the user-supplied URI, this vuln lets the attacker exploit the application to send a crafted request to an unexpected destination (regardless of firewall/VPN protection).

**Granularity of controls**: level of abstraction or detail which in a security function can be configured or tuned for performance and sensitivity. **Ethical Wall** is the use of administrative, physical/logical controls to establish/enforce separation of information, assets or job functions for need-to-know boundaries or prevent conflict of interest situations; AKA compartmentalization. **Context-dependent access control** applies additional context before granting access, with time as a commonly used context. **Content-dependent control**: Content-dependent access control adds additional criteria beyond identification and authentication: the actual content the subject is attempting to access; all employees of an organization may have access to the HR database to view their accrued sick time and vacation time, but should an employee attempt to access the content of the CIO's HR record, access is denied.

**Capability tables**: list privileges assigned to subjects and identify the objects that subjects can access. **Cache poisoning**: adding content to cache that wasn't an intended element (of say a web page); once poisoned, a legit web doc can call on a cached item, activating the malicious cache. **Access Control Token**: based on the parameters like time, date, day etc a token defines access validity to a system. **Access control principles**: need to know, least privilege, and separation of duties. Assets include information, systems, devices, facilities, and applications, and organizations use both physical and logical access controls to protect them.

**Role-Based Access Control (RBAC)**: key characteristic is the use of roles or groups; RBAC models use task-based roles, and users gain privileges when admins place their accounts into a role or group; taking a user out of a role removes the permissions granted through the role membership.

Instead of assigning permissions directly to users, user accounts are placed in roles and administrators assign privileges to the roles (typically defined by job function).

If the user account is in a role, the user has all privileges assigned to the role.

MS Windows OS uses this model with groups. RBAC models can group users into roles based on the organization's hierarchy, and it is a non-discretionary access control model; central authority access decisions can use the RBAC model. RBAC allows assignment of privileges to users with minimum admin overhead.

<a id="subtopic-5-4-2"></a>

### 5.4.2 Rule Based access control

**Rule-based Access Control**: use a set of rules, restrictions, or filters to determine access; key characteristic is that it applies global rules to all subjects.

E.g. firewalls access control lists use a list of rules that define what access is allowed and what access is blocked.

Rules within the rule-based access control model are sometimes referred to as restrictions or filters.

<a id="subtopic-5-4-3"></a>

### 5.4.3 Mandatory Access Control (MAC)

**Mandatory Access Control (MAC)**: access control that requires the system itself to manage access controls in accordance with the organization's security policies.

A key characteristic of the MAC model is the use of labels applied to both subjects and objects; subjects need matching labels to access objects.

E.g. a label of top secret grants access to top-secret documents.

When documented in a table, the MAC model sometimes resembles a lattice (i.e. climbing rosebush framework), so it is referred to as a lattice-based model. The MAC model enforces the need to know principle and supports a hierarchical environment, a compartmentalized environment, or a combination of both (hybrid environment).

<a id="subtopic-5-4-4"></a>

### 5.4.4 Discretionary Access Control (DAC)

**Discretionary Access Control (DAC)**: access control model in which the asset or system owner decides who gets access.

A key characteristic of the DAC model is that every object has an owner, and the owner can grant or deny access to any other subjects.

E.g. you create a file and are the owner, and can grant permissions to that file.

All objects have owners, owners can modify permission. Each object has an access control list defining permissions (e.g. read and modify files). All other models are non-discretionary models, and admins centrally manage non-discretionary controls. New Technology File System (NTFS) used in Windows, uses the DAC model. **Non-discretionary Access Control**: somebody other than the asset owner determines access.

<a id="subtopic-5-4-5"></a>

### 5.4.5 Attribute Based Access Control (ABAC)

**Access control** is a collection of mechanisms working together to protect organizational assets, allowing controlled access to authorized subjects, allowing management to specify which users can access what resources, and what operations they can perform; providing individual accountability. **Attribute-Based Access Control (ABAC)** is an advanced implementation of a rule-based access model, applying rules based on attributes; an access control paradigm where access rights are granted to users with policies that combine attributes together.

A key characteristic of the ABAC model is its use of rules that can include multiple attributes about users, the environment, a user's action and the target resource.

This allows it to be much more flexible than a rule-based access control model that applies the rules to all subjects equally. Many software-defined networks (SDNs) use the ABAC model.

ABAC allows administrators to create rules within a policy using plain language statements such as "Allow Managers to access the WAN using a mobile device". ABAC uses XACML (eXtensible Access Control Markup Language) which defines attribute-based access control policy language, architecture, and a processing model.

<a id="subtopic-5-4-6"></a>

### 5.4.6 Risk based access control

**Risk-based access control**: evaluates the environment and the situation, and makes decisions based on software security policies.

A model that grants access after evaluating risk; it can control access based on multiple factors such as a user's location, determined by IP addresses, whether the user has logged on with MFA, and the user's device. Advanced models use machine learning, making predictive conclusions about current activity based on past activity. A risk-based access control can be used, as an example, to block malicious traffic from an infected IoT device by evaluating the environment and situation, and using that information to block traffic deemed abnormal.

<a id="subtopic-5-4-7"></a>

### 5.4.7 Access policy enforcement (e.g., policy decision point, policy enforcement point)

**Policy Decision Point (PDP)**: make decisions on authorization requests sent from PEP, based on pre-defined rules. **Policy Enforcement Point (PEP)**: application component that receives authentication requests, functioning as a gatekeeper, sending the request on to the PDP; once a decision is provided by the PDP, the PEP enforces it (grant/deny). **Access policy enforcement**: enforcing access control policies within an organization to regulate and manage access. Policy Decision Point (PDP): the system responsible for making access control decisions based on predefined access policies and rules; a PDP evaluates access requests.

Policy Enforcement Point (PEP): responsible for enforcing the access control decisions made by the PDP; the PEP acts as a gatekeeper.

### AI in this objective

**Agent authority.** Give an assistant only the functions and privileges required for its task. Harbor can let it draft a response without letting it issue refunds. Consequential actions need authorization at the tool or service boundary; a model's explanation is not an access-control decision. [OWASP excessive agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/).

### Apply this objective

**Question.** The interface hides an administrative action, but the server still accepts the request from a normal user. Which part is missing?

**Reasoning.** Effective authorization enforcement is missing. Interface presentation is not a security boundary; the server must evaluate and enforce the policy for the requested action and object.

<a id="objective-5-5"></a>

## 5.5 Manage the identity and access provisioning lifecycle

Identity management is a lifecycle, not a one-time account creation task. Provisioning gives approved access, reviews check whether it remains justified, transfers revise it, and deprovisioning removes it. Include service accounts and other non-human identities in the same accountability system.

Harbor should know who owns an account, why it exists, which privileges it has, how its credentials are protected, and when it should expire. Unused accounts and accumulated privileges can survive long after their original business purpose disappears.

<a id="subtopic-5-5-1"></a>

### 5.5.1 Account access review (e.g., user, system, service)

Administrators need to periodically review user, system and service accounts to ensure they meet security policies and that they don’t have excessive privileges. Be careful in using the local system account as an application service account; although it allows the application to run without creating a special service account, it usually grants the application more access than it needs. You can use scripts to run periodically and check for unused accounts, and check privileged group membership, removing unauthorized accounts.

#### Guard against two access control issues

Excessive privilege: occurs when users have more privileges than assigned work tasks dictate; these privileges should be revoked. Creeping privileges (AKA privilege creep): user accounts accumulating additional privileges over time as job roles and assigned tasks change.

<a id="subtopic-5-5-2"></a>

### 5.5.2 Provisioning and deprovisioning (e.g., on/off boarding and transfers)

Identity and access provisioning lifecycle refers to the creation, management, and deletion of accounts.

This lifecycle is important because without properly defined and maintained user accounts, a system is unable to establish accurate identity, perform authentication, provide authorization, and track accountability.

**Privileged Access Management (PAM)** is a critical component of the identity and access provisioning lifecycle; PAM solutions manage, monitor, and audit privileged account access and include features like session recording, credential vaulting, and just-in-time privileged access.

#### Provisioning/Onboarding

Provisioning ensures that accounts have appropriate privileges based on task requirements and employees receive needed hardware; said another way, includes the creation, maintenance, and removal of user objects from applications, systems, and directories.

Proper user account creation, or provisioning, ensures that personnel follow specific procedures when creating accounts.

New-user account creation is AKA enrollment or registration.

**automated provisioning**: information is provided to an application, that then creates the accounts via pre-defined rules (assigning to appropriate groups based on roles).

Automated provisioning systems create accounts consistently.

**workflow provisioning**: provisioning that occurs through an established workflow, like an HR process. Provisioning also includes issuing hardware, tokens, smartcards etc to employees. It’s important to keep accurate records when issuing hardware to employees.

After provisioning, an organization can follow up with onboarding processes, including: the employee reads and signs the acceptable use policy (AUP); explaining security best practices (like infected emails); reviewing the mobile device policy; ensuring the employee’s computer is operational, and they can log in; configure a password manager; explaining how to access help desk; show how to access, share and save resources.

#### Deprovisioning/Offboarding

Deprovisioning processes disable or delete an account when employees leave, and offboarding processes ensure that employees return all hardware the organization issued them. Deprovisioning/offboarding occurs when an employee leaves the organization or is transferred to a different department.

**account revocation**: deleting an account is the easiest way to deprovision.

An employee's account is usually first disabled. Supervisors can then review the user’s data and determine if anything is needed. If terminated employee retains access to a user account after the exit interview, the risk for sabotage is very high.

Deprovisioning includes collecting any hardware issued to an employee such as laptops, mobile devices and authentication tokens.

<a id="subtopic-5-5-3"></a>

### 5.5.3 Role definition and transition (e.g., people assigned to new roles)

When a new job role is created, it's important to identify privileges needed by someone in that role; this ensures that employees in the new roles do not have excessive privileges.

Employee responsibilities can change in the form of transfers to a different role, or into a newly created role.

For new roles, it’s important to define the role and the privileges needed by the employees in that role.

Roles and associated groups need to be defined in terms of privileges.

<a id="subtopic-5-5-4"></a>

### 5.5.4 Privilege escalation (e.g., use of sudo, auditing its use)

**Privilege escalation** is gaining additional access. It can be authorized and controlled, such as approved sudo use, or unauthorized through exploitation. Distinguish legitimate elevation from an attack. Attackers use privilege escalation techniques to gain elevated privileges, after exploiting a single system; typically, they try to gain additional privileges on the exploited systems first. **Horizontal privilege escalation**: gives an attacker similar privileges as the first compromised user, but from other accounts.

**Vertical privilege escalation** provides an attacker with significantly greater privileges.

E.g. after compromising a regular user’s account an attacker can use vertical privilege escalation techniques to gain administrator privileges on the user’s computer. The attacker can then use horizontal privilege escalation techniques to access other computers in the network. This horizontal privilege escalation throughout the network is AKA **lateral movement**.

Limit service-account privileges and tightly control authorized elevation using tools such as **sudo**. Sudo is a command and policy mechanism, not an account.

<a id="subtopic-5-5-5"></a>

### 5.5.5 Service accounts management

**Service accounts**: used by applications, services, systems to interact with other resources, services, or databases without human intervention.

Regardless of the fact that these accounts are not primarily used by humans for authentication, doesn't mean they can be ignored; these accounts and the security of these accounts need to reviewed and managed.

**Service account management** is the process of creating, configuring, monitoring, and maintaining service accounts.

Ensuring service accounts are secured, reducing the risk of unauthorized access or misuse.

### AI in this objective

**Non-human identity lifecycle.** Assign the assistant a managed service identity with an owner, limited credentials, review, and revocation. [ISC2 AI guidance, Domain 5](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).

Original application check: Harbor retires its assistant but keeps the integration token active. The service is not fully deprovisioned; revoke the token and review any remaining permissions and scheduled jobs.

### Apply this objective

**Question.** A scheduled reporting job uses the credentials of an employee who is leaving. What should happen?

**Reasoning.** Move the job to an appropriately managed service identity with limited privileges and ownership, then revoke the employee's access through the normal departure process. Keeping the departed employee's account active obscures accountability.

<a id="objective-5-6"></a>

## 5.6 Implement authentication systems

Authentication systems implement the strategy with protocols, credentials, servers, and clients. Understand the exchange: what secret or proof is presented, what the verifier checks, and whether the connection protects the evidence. Then consider replay, impersonation, relay, and credential theft.

Different protocols serve different purposes. A directory can store identity information, a ticket system can support authenticated service access, and a federation protocol can convey assertions. Do not treat every identity-related technology as interchangeable.

### Concepts in context

**Authentication**: verifies the subject’s identity by comparing one or more authentication factors against a database holding authentication information for users; subjects prove their identity by providing authentication credentials.

Federated Identity Management (FIM): (AKA federated access), also see definition in 5.2.5;  one-time authentication to gain access to multiple systems, including those associated with other organizations; FIM systems link user identities in one system with other systems to implement SSO; FIM systems are implemented on-premise (providing the most control), via third-party cloud services, or as hybrid systems; using your Microsoft account to authenticate to a third-party SaaS is an example of FIM.

FIM trust relationships include: principal/user, identity provider (entity that owns the identity and performs the authentication), and relying party (AKA service provider). FIM protocols include SAML, WS-Federation, OpenID (authentication), and OAuth (authorization). Compare FIM with SSO: user authenticates one time using SSO to access multiple systems in one organization; a user authenticates one time using FIM to access multiple systems inside and outside an organization because of multiple-entity trust relationships.

**Extensible Markup Language (XML)** represents structured information using markup. It is not a set of HTML extensions; applications use it for documents and data exchange, including SAML assertions. [W3C XML](https://www.w3.organization/XML/).

XML does more than describing how to display data, it describes the data itself using tags.

#### Security Assertion Markup Language (SAML)

**Security Assertion Markup Language (SAML)** is an open XML-based standard commonly used to exchange authentication and authorization (AA) information between federated organizations. Frequently used to integrate cloud services and provides the ability to make authentication and authorization assertions. SAML provides SSO capabilities for browser access. Organization for the Advancement of Structured Information Standards (OASIS) maintains it. SAML 2.0 is an open XML-based standard.

#### SAML 2.0 spec utilizes three entities

**Principal or User Agent** is the principal is the user attempting to use the service. **Service Provider (SP) (or relying party)**: providing a service for the user. **Identity Provider (IdP)** is a third-party that holds the user authentication and authorization info.

#### IdP can send three types of XML messages known as assertions

**Authentication Assertion** provides proof that the user agent provided the proper credentials, identifies the identification method, and identifies the time the user agent logged on. **Authorization Assertion**: indicates whether the user agent is authorized to access the requested service; if denied, includes why. **Attribute Assertion**: attributes can be any information about the user agent.

#### OpenID Connect (OIDC) / Open Authorization (Oauth)

**OpenID provides authentication**.

**OpenID Connect (OIDC)** is an authentication layer using the OAuth 2.0 authorization framework, maintained by the OpenID Foundation (not IETF); OIDC provides both authentication and authorization (by using the OAuth framework).

OIDC is a RESTful, JSON (JavaScript Object Notation)-based authentication protocol that, when paired with OAuth can provide identity verification and basic profile info; uses JSON Web Tokens (JWT), (AKA ID token).

OAuth and OIDC are used with many web-based applications to share information without sharing credentials.

OAuth provides authorization. OIDC uses the OAuth framework for authorization and builds on the OpenID technologies for authentication.

**OAuth 2.0** is an open authorization framework described in RFC 6749 (maintained by Internet Engineering Task Force (IETF)).

OAuth exchanges data via APIs. OAuth is the most widely used open standard for authorization and delegation of rights for cloud services. The most common protocol built on OAuth is OpenID Connect (OIDC); OpenID is used for authentication. OAuth 2.0 enables third-party applications to obtain limited access to an HTTP service, either on behalf of a resource owner (by orchestrating an approval interaction), or by allowing third-party applications to obtain access on its own behalf; OAuth provides the ability to access resources from another service. OAuth 2.0 is often used for delegated access to applications, e.g. a mobile game that automatically finds your new friends from a social media application is likely using OAuth 2.0.

Conversely, if you sign into a new mobile game using a social media account (instead of creating a user account just for the game), that process might use OIDC.

#### Kerberos

**Kerberos is the most common SSO method used within organizations**. **The primary purpose of Kerberos is authentication**. **Kerberos uses symmetric cryptography and tickets to prove identification and provide authentication**. **Kerberos relies on NTP (Network Time Protocol) to sync time between server and clients**. **Kerberos uses port 88 for authentication communications**, clients communicate with KDC servers over the port so that users can effectively access privileged network resources. Kerberos is a network authentication protocol widely used in corporate and private networks and found in many LDAP and directory services solutions such as Microsoft Active Directory.

It provides single sign-on and uses cryptography to strengthen the authentication process and protect logon credentials. Ticket authentication is a mechanism that employs a third-party entity to prove identification and provide authentication. Kerberos is a well-known ticket system. After users authenticate and prove their identity, Kerberos uses their proven identity to issue tickets, and user accounts present these tickets when accessing resources. Kerberos version 5 relies on symmetric-key cryptography (AKA secret-key cryptography) using the Advanced Encryption Standard (AES) symmetric encryption protocol. Kerberos provides confidentiality and integrity for authentication traffic using end-to-end security and helps protect against eavesdropping and replay attacks.

Kerberos uses port 88, typically UDP but also TCP for larger tickets. See section 3.7.12 for an overview of Kerberos attacks.

#### Kerberos elements

**Key Distribution Center (KDC)** is the trusted third party that provides authentication services.

The **Key Distribution Center (KDC)** provides an authentication service (AS) and ticket-granting service (TGS). [RFC 4120](https://www.rfc-editor.organization/rfc/rfc4120).

**ticket-granting service (TGS)** provides proof that a subject has authenticated through a KDC and is authorized to request tickets to access other objects.

The ticket for the full ticket-granting service is called a ticket-granting ticket ([TGT](https://learn.microsoft.com/en-us/windows/win32/secauthn/ticket-granting-tickets)); when the client asks the KDC for a ticket to a server, it presents credentials in the form of an authenticator message and a ticket (a TGT) and the ticket-granting service opens the TGT with its master key, extracts the logon session key for this client, and uses the logon session key to encrypt the client's copy of a session key for the server. A TGT is encrypted and includes a symmetric key, an expiration time, and user’s IP address.

Subjects present the TGT when requesting tickets to access objects.

The **authentication service (AS)** processes initial authentication requests and supplies credentials used to request service tickets. The TGS handles subsequent ticket requests. [RFC 4120](https://www.rfc-editor.organization/rfc/rfc4120).

**Ticket (AKA service ticket (ST))** is an encrypted message that provides proof that a subject is authorized to access an object. **Kerberos Principal**: typically a user but can be any entity that can request a ticket. **Kerberos realm** is a logical area (such as a domain or network) ruled by Kerberos.

#### Kerberos login process

User provides authentication credentials (types a username/password into the client).

**Client/TGS key generated**

In a typical password-based Kerberos exchange, the client identifies its principal and supplies required pre-authentication evidence; it does not simply encrypt the username as the authentication mechanism. [RFC 4120](https://www.rfc-editor.organization/rfc/rfc4120). The KDC verifies the username against a db of known credentials. The KDC generates a symmetric key that will be used by the client and the Kerberos server. It encrypts this with a hash of the user’s password.

TGT generated - the KDC generates an encrypted timestamped TGT.

**Client/server ticket generated**

The KDC then transmits the encrypted symmetric key and the encrypted timestamped TGT to the client. The client installs the TGT for use until it expires. The client also decrypts the symmetric key using a hash of the user’s password.

The client’s password is never transmitted over the network, but it is verified.

The server encrypts a symmetric key using a hash of the user’s password, and it can only be decrypted with a hash of the user’s password.

User accesses requested service.

When a client wants to access an object (like a hosted resource), it must request a ticket through the Kerberos server, in the following steps:

The client sends its TGT back to the KDC with a request for access to the resource. The KDC validates the ticket and authenticator and applies ticket-issuance policy. The destination service remains responsible for its resource-authorization decision. [RFC 4120](https://www.rfc-editor.organization/rfc/rfc4120). The KDC generates a service ticket and sends it to the client. The client sends the ticket to the server or service hosting the resource. The service normally validates the service ticket using its own long-term key and checks the authenticator, rather than contacting the KDC for every validation. [RFC 4120](https://www.rfc-editor.organization/rfc/rfc4120).

Once identity and authorization are verified, Kerberos activity is complete.

The server or service host then opens a session with the client and begins communication or data transmission.

Remote Authentication Dial-in User Service (RADIUS) / Terminal Access Controller Access Control System Plus (TACACS+).

Several protocols provide centralized authentication, authorization, and accounting services; network (or remote) access systems use AAA protocols.

**Remote Authentication Dial-in User Service (RADIUS)**: centralizes authentication for remote access connections, such as VPNs or dial-up access.

A user can connect to any network access server, which then passes on the user’s credentials to the RADIUS server to verify authentication and authorization and to track accounting. In this context, the network access server is the RADIUS client, and a RADIUS server acts as an authentication server. The RADIUS server also provides AAA services for multiple remote access servers. RADIUS uses the User Datagram Protocol (UDP) by default and encrypts only the password’s exchange. RADIUS using Transport Layer Security (TLS) over TCP (port 2083) is defined by RFC 6614.

RADIUS uses UDP port 1812 for RADIUS messages and UDP port 1813 for RADIUS Accounting messages. RADIUS encrypts only the password’s exchange by default. It is possible to use RADIUS/TLS to encrypt the entire session.

Cisco developed **Terminal Access Control Access Control System Plus (TACACS+)** and released it as an open standard.

Provides improvements over the earlier version and over RADIUS, it separates authentication, authorization, and accounting into separate processes, which can be hosted on three different servers. Additionally, TACACS+ encrypts all of the authentication information, not just the password, as RADIUS does. TACACS+ uses TCP port 49, providing a higher level of reliability for the packet transmissions.

**Diameter AAA protocol** is an advanced system designed to address the limitations of the older RADIUS protocol (diameter is twice the radius!); Diameter improves on RADIUS by providing enhanced security (uses IPsec or TLS instead of MD5 hashing), supports more extensive attribute sets (suitable for large, complex networks), and can handle complex sessions.

Diameter is based on RADIUS and improves many of its weaknesses, but Diameter is not compatible with RADIUS. Diameter is designed to use TCP and Stream Control Transmission Protocol (SCTP) at the transport layer, specifically to address the reliability issues found in RADIUS.

Also see Understanding CISSP Domain 5: Identity and Access Management (IAM) - [part 1](https://blog.balancedsec.com/p/understanding-cissp-domain-5-identity), and [part 2](https://blog.balancedsec.com/p/understanding-cissp-domain-5-identity-3f0) on the source author's blog, [The Cyber Leader](https://blog.balancedsec.com/) (note that some articles require a subscription).

### Apply this objective

**Question.** Harbor captures an authentication exchange during troubleshooting. Why must the capture be protected?

**Reasoning.** Depending on the protocol, it may contain credentials, reusable tokens, or evidence useful in offline attacks. Troubleshooting records need restricted access, appropriate retention, and secure disposal just like other sensitive information.

## Chapter review

Return to the Harbor examples and explain each decision without looking at the answer. Identify the asset or business activity, the relevant requirement, the possible harm, the responsible owner, and the evidence that would support the decision. If two controls appear interchangeable, explain the different failure each addresses.

### Connections and common distinctions

Identification claims an identity; authentication supports the claim; authorization permits actions. SSO and federation are related but distinct. Provisioning, review, and revocation apply to human and service identities alike. Connect access decisions to asset ownership in Domain 2.

### Review questions and explained answers

**1. How would you explain this domain to Harbor's service owner?** Describe the decisions it governs using the examples in this chapter. A useful answer connects technical measures to customer service, accountability, and evidence rather than listing product names.

**2. Which assumption in the chapter's examples would most change your recommendation if it were false?** Choose a concrete assumption, such as data sensitivity, allowed downtime, or an identity's authority. Explain how a different assumption changes the relevant control or test. More than one answer can be sound when justified.

**3. How does adding the AI assistant change the work?** Follow the AI lessons in this chapter. Identify an additional asset, failure, or decision and describe its owner and verification method. The assistant still operates within ordinary governance, access, data, and recovery requirements.

### AI application review

**Question.** Should the assistant use an administrator's account because its tasks change frequently?

**Reasoning.** No. Use a managed non-human identity with limited privileges, an accountable owner, credential protection, reviews, and revocation. Expand permissions only through an approved process. Adaptive authentication and behavioral signals can help assess human access but do not replace authorization for the assistant's actions.

## Term index

This index points to explanations in the chapter. Terms retain the source guide's spelling where useful for recognition; corrected concepts are explained in context.

- [Access control](#subtopic-5-4-5)
- [Access control principles](#subtopic-5-4-1)
- [Access control services](#subtopic-5-2-2)
- [Access Control System](#subtopic-5-2-2)
- [Access Control Token](#subtopic-5-4-1)
- [Access policy enforcement](#subtopic-5-4-7)
- [account revocation](#subtopic-5-5-2)
- [Accountability](#subtopic-5-2-2)
- [Accountability AKA Principle of Access Control](#subtopic-5-2-2)
- [Adaptive authentication](#objective-5-2)
- [ADFS](#subtopic-5-2-1)
- [Agent authority](#objective-5-4)
- [Asynchronous token](#subtopic-5-2-1)
- [Attribute Assertion](#objective-5-6)
- [Attribute-Based Access Control (ABAC)](#subtopic-5-4-5)
- [Auditing](#subtopic-5-2-2)
- [Authentication](#objective-5-2)
- [Authentication Assertion](#objective-5-6)
- [authentication service (AS)](#objective-5-6)
- [Authenticator Assurance Levels (AAL)](#subtopic-5-2-1)
- [Authorization](#subtopic-5-2-2)
- [Authorization Assertion](#objective-5-6)
- [automated provisioning](#subtopic-5-5-2)
- [Cache poisoning](#subtopic-5-4-1)
- [Capability tables](#subtopic-5-4-1)
- [CAPTCHA](#subtopic-5-2-1)
- [CAS](#subtopic-5-2-1)
- [centralized access control](#subtopic-5-2-1)
- [Cognitive Passwords](#subtopic-5-2-4)
- [Content-dependent control](#subtopic-5-4-1)
- [Context-dependent access control](#subtopic-5-4-1)
- [Credential management systems](#subtopic-5-2-6)
- [Cross-Site Request Forgery (CSRF)](#subtopic-5-2-1)
- [Crossover Error Rate (CER)](#subtopic-5-2-1)
- [decentralized access control](#subtopic-5-2-1)
- [Diameter AAA protocol](#objective-5-6)
- [directory service](#subtopic-5-2-7)
- [Discretionary Access Control (DAC)](#subtopic-5-4-4)
- [Email challenge](#subtopic-5-2-2)
- [Ethical Wall](#subtopic-5-4-1)
- [FAR](#subtopic-5-2-1)
- [FIDO2 (Fast IDentity Online 2)](#subtopic-5-2-2)
- [FRR](#subtopic-5-2-1)
- [Granularity of controls](#subtopic-5-4-1)
- [Groups](#subtopic-5-2-1)
- [Hash Message Authentication Code (HMAC)](#subtopic-5-2-2)
- [Horizontal privilege escalation](#subtopic-5-5-4)
- [IDaaS](#subtopic-5-3-2)
- [Identification](#objective-5-2)
- [Identity proofing](#subtopic-5-2-4)
- [Identity Provider (IdP)](#objective-5-6)
- [Kerberos Authentication Server](#objective-5-6)
- [Kerberos is the most common SSO method used within orgs](#objective-5-6)
- [Kerberos Principal](#objective-5-6)
- [Kerberos realm](#objective-5-6)
- [Kerberos uses port 88 for auth communications](#objective-5-6)
- [Key Distribution Center (KDC)](#objective-5-6)
- [Knowledge-based authentication (KBA)](#subtopic-5-2-4)
- [knowledge-based authentication (KBA)](#subtopic-5-2-4)
- [lateral movement](#subtopic-5-5-4)
- [logical access controls](#objective-5-1)
- [lower CER indicates a more accurate biometric system](#subtopic-5-2-1)
- [Mandatory Access Control (MAC)](#subtopic-5-4-3)
- [Memory card](#subtopic-5-2-1)
- [Multifactor authentication (MFA)](#subtopic-5-2-2)
- [Non-discretionary Access Control](#subtopic-5-4-4)
- [Non-human identity lifecycle](#objective-5-5)
- [OAuth 2.0](#objective-5-6)
- [Objects](#subtopic-5-2-2)
- [OpenID Connect (OIDC)](#objective-5-6)
- [OpenID provides authentication](#objective-5-6)
- [Password vault (AKA password manager)](#subtopic-5-2-6)
- [Password-less authentication](#subtopic-5-2-2)
- [Passwords authentication](#subtopic-5-2-1)
- [physical security controls](#objective-5-1)
- [Policy Decision Point (PDP)](#subtopic-5-4-7)
- [Policy Enforcement Point (PEP)](#subtopic-5-4-7)
- [Principal or User Agent](#objective-5-6)
- [principle of access control](#subtopic-5-2-2)
- [Privilege escalation](#subtopic-5-5-4)
- [Privileged Access Management (PAM)](#subtopic-5-5-2)
- [Remote Authentication Dial-in User Service (RADIUS)](#objective-5-6)
- [Risk-based access control](#subtopic-5-4-6)
- [Role-Based Access Control (RBAC)](#subtopic-5-4-1)
- [Roles](#subtopic-5-2-1)
- [Rule-based Access Control](#subtopic-5-4-2)
- [Security Assertion Markup Language (SAML)](#objective-5-6)
- [Self-service identity management](#subtopic-5-2-1)
- [Server-Side Request Forgery (SSRF)](#subtopic-5-4-1)
- [Service account management](#subtopic-5-5-5)
- [Service accounts](#subtopic-5-5-5)
- [Service Provider (SP) (or relying party)](#objective-5-6)
- [SESAME](#subtopic-5-4-1)
- [Session](#subtopic-5-2-3)
- [Session management](#subtopic-5-2-3)
- [Seven Laws of Identity](#subtopic-5-2-1)
- [single point of compromise](#subtopic-5-2-7)
- [Single Sign-On (SSO)](#subtopic-5-2-7)
- [Single-factor authentication](#subtopic-5-2-2)
- [Smart card](#subtopic-5-2-1)
- [Split-response attack](#subtopic-5-4-1)
- [Subject](#subtopic-5-2-2)
- [Synchronous token](#subtopic-5-2-1)
- [Template](#subtopic-5-2-1)
- [Terminal Access Control Access Control System Plus (TACACS+)](#objective-5-6)
- [The primary purpose of Kerberos is authentication](#objective-5-6)
- [Ticket (AKA service ticket (ST))](#objective-5-6)
- [ticket-granting service (TGS)](#objective-5-6)
- [Time-based One-Time Password (TOTP)](#subtopic-5-2-2)
- [Two-factor authentication (2FA)](#subtopic-5-2-2)
- [Vertical privilege escalation](#subtopic-5-5-4)
- [WebAuthn (Web Authentication)](#subtopic-5-2-2)
- [Whaling attack](#subtopic-5-2-1)
- [workflow provisioning](#subtopic-5-5-2)
- [XSS](#subtopic-5-4-1)
- [XST](#subtopic-5-4-1)

## Sources and further reading

- [Original Domain 5 objectives and notes](../CISSP-Domain-5-2024+Objectives.md) by the repository's contributors; adapted under the repository license.
- [ISC2 CISSP exam outline and AI domain guidance](https://www.isc2.org/certifications/cissp/cissp-certification-exam-outline).
- [ISC2 AI guidance announcement](https://www.isc2.org/Insights/2026/04/ISC2-Publishes-Exam-Guidance-AI).
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

Additional references appear alongside the relevant concepts. Official Study Guide chapter references in the original objective files remain available for comparison.
