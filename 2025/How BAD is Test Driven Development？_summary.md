• TDD discussed as a topic
• Prime's recent experience with TDD and its limitations
• Designing an API in test, setting up tests to fail, then making it work
• Interface created for testing vs actual usage interface
• Difficulty of creating interfaces that are both good for testing and practical use cases
• Co-creating tests with code instead of traditional TDD approach
• TDD (test-driven development) may not be practical for every situation
• Writing tests first can lead to an "abstract mess" of interfaces and inversion of control
• It's better to write tests after implementation, especially when requirements change frequently
• Test-driven development is useful for specific scenarios, such as testing reusable code or complex systems
• Integration testing and modular design are often more effective than TDD in certain cases
• Criticism of object-oriented programming (OOP) and its emphasis on thinking in terms of objects
• Similar criticism of test-driven development (TDD), arguing it shifts focus away from actual use cases
• Discussion of the "zero sum" nature of programming time, where time spent on one task is not available for another
• Argument that TDD can lead to poor API design and a "mess" due to prioritizing tests over use cases
• Proposal to incorporate testing as part of the development process, rather than focusing on it from the outset.
• The speaker believes traditional testing approaches are sufficient and that test-driven development (TDD) is not necessary or effective.
• The speaker questions the effectiveness of TDD based on their own experiences with software from organizations that use it.
• The speaker provides an example of YouTube's play button issue, which has existed for eight years despite supposedly rigorous testing.
• The speaker suggests rethinking how time is allocated to testing and finding a balance between different approaches.
• The speaker favors snapshot or golden testing methods, where tests can be written to compare outputs before and after changes.
• Snapshots in testing can provide a lot of confidence that changes haven't caused unintended effects throughout the system.
• Snapshots are especially effective for certain types of problems, such as verifying references and expected outputs.
• However, they can be less effective when requirements change frequently or if no one actually knows what the expected output is.
• In some cases, snapshot tests may not be worth keeping if they just need to be constantly updated.
• Discussion of the speaker's experience with snapshot testing
• Difficulty in hand-eyeballing and verifying snapshots for big changes
• Comparison of snapshot testing to making a "golden trap" constantly
• Discussion of unit tests breaking and mature product issues with testing in general
• The speaker believes testing is not helpful for refactoring unless it's an end-to-end test
• Unit tests can be too tightly coupled to specific code, making them break when the code is refactored
• The speaker thinks unit testing is often overemphasized and doesn't always prevent headaches during refactoring
• Testing at the wrong level can lead to false confidence in changes made to the code
• The speaker prefers end-to-end tests for complex or "hard" parts of the codebase, rather than trying to test everything
• The speaker thinks some parts of the code are not refactorable anyway
• The importance of testing and verifying code, particularly in libraries
• A personal anecdote about adding a backdoor feature for a customer, which caused issues when it wasn't tested properly
• Reflection on the value of thorough testing to prevent future problems
• Mention of React updating its definition of the "sign" function, causing potential issues with legacy code
• Discussion of the limitations of testing methods
• Criticism of test-driven development (TDD) and its effectiveness
• Advocacy for progressive delivery (PDD) or progressive deployment over TDD
• Importance of measuring outcomes after releasing a new version
• Caution against releasing new versions without thorough testing
• The speaker is discussing the company Sonos and a software update it released that was widely criticized by customers
• The update caused feature regressions, didn't work properly, and tanked the company's reputation
• The speaker compares this to Google's frequent software updates, suggesting they often roll out changes that don't live up to expectations
• TJ is discussing his personal experience with Sonos products, including a failed attempt by the company to update their software
• The conversation also touches on the fact that Sonos had redeployed all of its servers and couldn't roll back the update
• Difference between hardware and software
• Twitter breaking down as an example of minor issue
• Sonos server failure as a major issue comparison
• Testing and deployment strategies for new features or products
• Discussion of a phone overheating in the sun
• TJ's personality and pitch for being on a podcast
• Discussion of pet peeves and ideal relationships (e.g. long walks, meaningful conversations)
• TJ's favorite project, Neo Vim, and its unique challenges (e.g. compatibility with Vim, edge cases)
• Importance of tests and test maintenance in software development
• Skill issue or other factors contributing to bugs in code
• Discussion of test-driven debugging and snapshot tests
• Comparison between NeoVim and a new development tool's testing approach
• Importance of considering the product's lifecycle stage (exploration vs mature) when introducing tests or golden values
• Discussing the value of snapshot testing in software development
• The importance of considering the stability of snapshots in testing
• The distinction between stable and unstable snapshot testing scenarios
• The need for consistent implementation to make snapshot testing effective
• Examples of snapshot testing being useful, such as parsing a specific language's specification
• Discussion of the limitations of test-driven development (TDD) and its potential drawbacks
• The concept of using TDD for specific tasks with low productivity, such as abstract programming
• An example of how to use TDD to create a concrete output for low-level features, increasing motivation and performance
• The author's skepticism towards using code coverage reports as a motivator for TDD
• Discussion of code coverage and its limitations
• Personal experience with a team requiring 100% test coverage at Netflix
• Falkor, a system used to retrieve data from the backend, and its potential for abuse (materializing all values)
• The Repulsive Grizzly Attack, a vulnerability discovered in Falkor that could DOS a service like Netflix
• Comparison of the name "Falkor" to the movie The Never Ending Story
• The speaker mentions refactoring and realizing a mistake was made
• A team member (Trash Dev) quits after being asked to help with a project
• Code coverage metrics are discussed and dismissed as "a lie"
• The meeting devolves into chaos, with speakers arguing and ultimately ending the stream
• TJ returns to the stream, seemingly out of nowhere
• A team leader wraps up the meeting by stating they're on track to meet OKRs and end with a positive note