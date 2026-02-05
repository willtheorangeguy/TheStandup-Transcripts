• Introduction to dev horror scenes
• Developer shares his first real job experience at Epic, working on Data Link application
• Project took three times as long as promised and was eventually deleted due to safety concerns
• New version of the project was later developed, but still had issues with patient safety escalations
• Developer describes a specific incident where a doctor noticed an external procedure listed incorrectly on a new mother's chart
• Incident led to a broader problem of incorrect procedures being attributed to wrong patients
• Discussion veers off-topic to advertise CodeRabbit, AI-powered code review tool
• Discussion about CodeRabbit extension and its features
• Medical insurance data and claim processing issues
• Epic Systems' software development process and testing procedures
• Comparison between old and new software development processes at Epic
• Custom software development environment
• Multi-step review and testing process involving multiple teams and approvals
• Potential for continuous iteration and revision of code changes
• Use of different branches and environments for development, QA, and deployment
• Process can be repetitive or time-consuming depending on the nature of the change
• Patch process takes weeks from start to finish
• Release time depends on significance of changes
• Story about building a custom solution for QA at Epic, including a fuzzy finder
• Solution allowed QA to test data automatically, reducing testing time from days to under an hour
• Inspiration for the idea came from discovering custom Excel parsing libraries in old code
• The speaker expresses disdain for using a company's custom IDE and prefers the one used at Epic, which is based on a proprietary programming language called MUMPS.
• MUMPS is described as a key-value store scripting language that allows business logic to be written in the same language as other backend code.
• The language was developed by programmers who worked at Massachusetts University Medical Centre and were known for its acronym not being very descriptive or fitting.
• The speaker finds it humorous that Epic uses this proprietary language, which is also used in a healthcare setting.
• They mention that Epic made more money than they can possibly dream of.
• Discussion of Epic, a healthcare software system
• Unique features of Mumps, a programming language used in Epic
• Benefits of sparse data sets in medical records
• Comparison to traditional healthcare systems in South Dakota
• Personal anecdotes and horror stories about working with the system
• Discussion of testing and deployment strategies for complex software systems
• The speaker is discussing a scenario where their site experienced a catastrophic failure due to cache clearing during load testing.
• The cache was cleared at a low-traffic time, but still caused significant downtime and affected multiple systems.
• The site's architecture involves microservices, which made it prone to cascading failures when one system went down.
• The speaker explains that the cache clearing overwhelmed downstream systems, leading to a chain reaction of outages.
• The incident was particularly distressing for the speaker, who described it as one of the worst moments in their career.
• Layers of a system, with the top layer being built on caching and not crucial to functionality
• Testing a system for CPU readings and reacting to X number of requests
• A freak accident occurred where cache had never been cleared
• System performance testing for steady baseline
• A previous project in data warehouse life, mapping soldiers to sign up for classes
• Stressful launch day experience due to high traffic
• Errors occurred in data mapping, causing people to sign up for the wrong thing
• The issue was not obvious and had to be analyzed through data
• A CRM system was built but became overwhelmed with tickets, leading to frustration
• The team had to accept the situation and fix it later
• They used pre-written queries to spot-check the data and reverse-engineer the logic
• People's schedules were affected, and many wanted to change their sign-ups
• Discussion of a past project where a catastrophic failure occurred
• Team effort and lessons learned from the experience
• Discussion of password usage in QA accounts
• Sharing of personal anecdotes about passwords and coding experiences
• Reference to previous stories, including the "repulsive grizzly attack" and File core/Fail core bug
• Storytelling about working with PHP startups and misunderstanding of static variables
• The speaker describes why old PHP was slow due to every request being its own process.
• The speaker shares a personal story of making a simple mistake with static variables, which was pointed out by their non-programming boss.
• The speaker discusses the challenges of implementing logging for UI elements in a large project, including handling various languages and formats.
• The speaker talks about their attempt to create a unified logging system called Atlas Mantis Logger, which they implemented for Groovy.
• Access to APIs for UI development
• Spent a million dollars in a day, API access revoked
• Rewriting a billboard for Lady Gaga's Netflix movie
• Testing issue caused page freeze during countdown
• Consequences of messing up in front of high-level executives
• Embarrassing stories and experiences as a developer
• Next.js and server-side rendering
• Issues with isomorphic JavaScript and GraphQL
• Site launch disaster due to poor performance
• Previous use of Pretender for caching results
• Traffic shedding and catastrophic performance issues
• Difficulty scaling containers and resolving problems
• Embarrassing failure to serve high requests per second
• Lack of stress testing and load testing
• Server-side rendering causing performance issues
• Misuse of GraphQL and over-querying data
• Inadequate knowledge of resolver weights and schema complexity
• Classic mistakes in implementing GraphQL
• Performance disaster caused by excessive queries on a large database