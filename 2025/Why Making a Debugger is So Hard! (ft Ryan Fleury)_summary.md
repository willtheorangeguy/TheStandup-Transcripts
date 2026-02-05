• Introduction to the stand-up podcast
• Discussion of the frequency of the stand-up (every day, Wednesday and Friday)
• Introductions of guests Tiege, Casey, and Ryan Fleure (also known as "Fleure")
• Topic announcement: debugging
• Explanation of print-f debugging by guest Ryan Fleure
• Discussion of the relationship between logging and debugging
• Debating the difference between using debuggers and logging in programming
• Discussing the limitations of current debuggers and how they can be improved
• Introducing a nuanced perspective on the concept of "red vs blue" (team debugger vs team logging)
• Addressing issues with debugging tools, including Linux and Windows debuggers
• Comparing different programming languages (Python, TypeScript, Go) in terms of their scalability and suitability for various tasks
• The speaker mentions using printf debugging due to bad debuggers
• Good debuggers can collect data faster than printf debugging
• Ryan's RADDebugger project aims to provide a viable debugging solution on Linux
• The original ambition of the project was to get a good debugger for Linux
• The speaker is now working on porting the Windows version to Linux
• Rad Debugger/ Epic Games Debugger
• Ryan's history with the project
• Steam Linux and the Steam Deck
• Cross-platform programming at RAD Game Tools
• Relationship between Valve (Steam) and RAD Game Tools/Epic Games
• RAD and Valve shared employees on VR projects
• Valve funded some salaries for RAD employees working at Valve offices
• Debugger project to develop a good debugger for Linux, funded by both Valve and RAD
• Debugger project took place at RAD offices after they expanded their space
• Debuggers are challenging to work with due to straddling an uncomfortable boundary between programming languages
• A project that creates visualizations and interactive things to show complex information is difficult to implement.
• Debugger UI is one of the hardest problems to solve in programming, as it requires a high level of technical skill and expertise.
• The combination of low-level system control and 3D visualization makes for an extremely challenging task.
• It's rare to find people who can go from zero to debugger creation.
• A well-designed debugger UI is essential but difficult to create due to its visual nature and the need to integrate various components.
• Debugger features and usability issues
• WinDBG as a classic example of a debugger with too many features
• Project languished due to lack of usable work
• Hiring struggles, including unsuccessful attempts to hire Ryan
• Team eventually assembled, including Ryan, Nick, Alan Webster, and Martin
• The project was inherited by Alan from Wan Chun in 2021.
• The team, including Nick and possibly others, worked on various aspects of the debugger.
• Specific issues included debugging info formats, process control, register reading, and binary patching.
• Nick focused on reverse engineering, PDB format, and unwinding problems.
• Alan tackled building an architecture for the actual debugger engine.
• The narrator initially assisted with debug info parsing and later worked on a prototype debugger to familiarize themselves with the problem space.
• Discussion of abandoned code in the code base
• Custom debug info format and its relation to PDB and dwarf formats
• Challenges of dealing with different tool chains and their respective debug info formats
• Attempt to create an abstraction layer for parsing dwarf or PDB, which proved complicated
• Alan's work on designing a custom debug info format before leaving the team
• The need for a simpler solution to handle debug information
• Project's graphical debugger development
• Debugger vs linker work distribution (Nick working on linker)
• PDB file size limit and its impact on large projects (Fortnite example)
• Type information section overflow due to C++ template metaprogramming and Lambda functions
• Comparison with other projects that exceeded the PDB file size limit
• Pokemon and Snoop Dogg skins added to a game
• Issue with compressed files causing problems
• Rad project's linker release allows for faster linking on Windows
• Directories (RDIs) provide efficient debug information
• Rad project tackles multiple hard problems simultaneously, including debugging and metaprogramming tools.
• Chart problems discussed
• Difficulty seeing certain parts of Epic's design from a distance
• Discussion about Epic Games' use in medical therapy
• Question about free Fortnite and the Sabrina Carpenter skin
• Health insurance and employee benefits at Epic Games
• Misconceptions about working at Epic Games (the game development company vs. other companies)
• The conversation starts with the speaker expressing intense sadness when people found out they didn't make Fortnite.
• They mention working at Epic as a software developer but actually work on electronic medical health records and insurance billing.
• A discussion ensues about the language "mumps" which was used in programming, and its confusing name that is now obsolete.
• The conversation turns to the D programming language, with some programmers expressing frustration over being called out for skipping D when naming languages.
• There's a humorous discussion about how both C++ and Rust users can agree on one thing: D sucks.
• Discussion about removing a person from a conversation without context
• Reference to the programming language D and its moratorium status
• Questioning of Ryan's involvement with Oodle and his lack of discussion about it
• Explanation of Oodle adjacency (being familiar with or related to Oodle)
• Discussion of wanting to talk about debugger information and stepping mechanisms
• Mention of a reference that only some people are aware of, but was not fully explained
• Debugger interactions with running programs
• Stepping over lines of source code
• Understanding how a debugger interacts with another running program on an OS
• CPUs and single stepping threads
• Compiler to assembly language instruction mapping and optimization
• Messy mapping between source code and assembly instructions
• Difficulty in storing debug information for debugging tools
• Mapping between source code lines and assembly language instructions
• Complexity of debugger functionality when dealing with optimizer changes
• Handling breakpoints and stopping conditions in the middle of a line
• Association of thread execution with specific lines of source code
• Algorithm for single-stepping threads until they leave a line of source code
• The current single-stepping process is slow due to frequent round trips between the debugger and target process.
• Using the int three instruction (a one-byte interrupt) can be used as a trap or "single-step" instruction within code, avoiding multiple round trips.
• Traps can be placed at strategic points in the code stream to allow single-stepping without context switching.
• The placement of traps becomes more complex when dealing with control flow instructions like jumps and calls.
• Issues with stepping over function calls in a debugger
• Recursive function calls and their impact on debugging
• Complications of implementing "step over" functionality in recursive code
• Debugger state machine implementation for handling trap addresses in recursive call stacks
• Personal anecdote about using a step debugger (walking treadmill)
• Discussion of interrupted conversation
• Explanation of stepping and putting in threes in assembly
• Understanding of relative and absolute jump instructions
• Overwriting assembly instructions during the stepping process
• Correcting overwritten assembly after stepping is complete
• Comparing complex code to banking apps and debuggers
• Discussion about how banks work and a humorous reveal that AHC (Auction House Corporation) works like FTP
• Ryan asked Wukash about one OS feature he'd like to have but doesn't
• The answer was user level in three (interrupt 3)
• Interrupts are used for servicing hardware and stopping normal execution to handle interrupts
• CPU looks up a table, executes the interrupt service routine, then resumes back to where it left off
• Program stack tracking and function calls
• Debugger limitations at user level on Windows
• Accessing memory and interrupt tables through API
• Full round trip process for traps and interrupts involving kernel and debugger
• Debugging process is slow due to multiple ring transitions
• Proposal to set int three to jump directly to the debugger's code for JIT compilation of trap operations
• Interruption of kernel-level feature to allow user-level interrupt handling
• Idea to replace current debugging process with a sys call to transfer control to the debugger
• Conditional breakpoints in debuggers can be slow due to the round trip cost of checking conditions
• This slows down debugging and makes it prohibitively expensive for large loops or frequent frame sampling
• Similar issues exist with printf debugging and profiling markup insertion
• A kernel-level feature that dynamically adds markup would improve performance and user experience
• However, implementing such a feature requires handling additional edge cases
• Overwriting instructions with "int three" has limitations
• Limitations arise when overwriting multi-byte instructions
• Extra checks are needed to prevent overflow and incorrect jumps
• VMs in interpreted languages like JavaScript can simplify this process
• Debugger tools like the Chrome debugger can effectively handle these issues
• Debugger for JavaScript has limitations and can be unreliable
• Restarting and catching breakpoints are problematic areas
• Unreliability occurs when reloading webpages or trying to debug startup issues
• Chrome's debugger protocol (CDP) contributes to the issue
• Using the "debugger" keyword in code ensures consistent results
• Criticism of the Chrome debugger's reliability and usefulness
• Preference for console.log over using a debugger to troubleshoot issues
• Discussion of features that would make a debugger valuable, including gathering and displaying information in a clean and quick manner
• Lack of ability to perform certain tasks with the Chrome debugger, such as walking data structures or turning them into tabular data
• Comparison of using the Chrome debugger to programming JavaScript
• Ranking a game's debug features
• Plans to create an offline debugger tier list video
• Discussion of the 3D model visualizer in the debugger
• Explanation of how to view pixel data and bitmap images using expression language rules
• Overview of visualization features in the debugger, including pan and zoom capabilities
• The rad debugger's memory viewer allows for customization of the data displayed.
• A hex view of memory can be created with customizable parameters.
• Geometry and texture data can be visualized in real-time as it is being built.
• Other visualization features include viewing multi-line text, disassembly viewers, and customizable rules for the watch tree.
• Automatic association of types with certain visualizer expressions is also possible.
• Bitmap visualization in a debugger
• Extending type information with visualizations
• Automatic display of bitmap visuals on hover or in watch window
• Ability to switch back to original type display
• Performance and loading speed of the feature
• Comparison to traditional debugging methods (e.g. print F debugging)
• Importance of usability and performance when implementing a new debugger feature
• Time-saving features of the rad debugger
• Automatic type information and viewing as bitmap
• Loading plugins and instantiating them
• Viewing images inside the debugger
• Comparing different debugging approaches
• Real-time pointer graph visualizer in the rad debugger
• Importance of real-time visualization for debugging
• Discussion of using Elixir and its built-in observer tool
• Comparison of compiled languages, including C++ and Rust
• Mention of Ginger Bill and his comments on the Odin compiler and rad debugger
• Humorously joking about Ginger Bill's supposed hatred for package managers and LSP
• Reference to a tactic used by Gabe Newell where announcements are made to create pressure on developers
• Talk Driven Development (TDD) vs Press Driven Development
• Announcement that Linux will be happening in the next few weeks
• Discussion about a conversation with Tim Sweeney regarding the development process
• Explanation of a recursive step case in coding
• Comparison of different methods for handling stack pointers and recursion
• Recursive calls being expensive due to hitting traps and checking stack pointer
• Alternative approach of turning off traps, faking instruction pointer on the stack, and catching exceptions instead
• Using a fake return address, such as 0x911, to trigger an exception when attempting to access it
• Debugger resetting traps after finishing call
• The speaker is using wireless microphones and mentions a humorous incident where someone used the restroom while still wearing a microphone.
• Discussion about a software or technical issue, possibly related to return addresses and stack manipulation in computer programming.
• Explanation of CPU behavior regarding checking return address stacks when performing a "ret" instruction.
• Clarification that some CPUs do not check the return address before jumping to it.
• Explanation of the concept of a shadow stack, which stores actual return addresses.
• The concept of a return address and its relationship to the stack
• The existence of a "shadow stack" or alternative tracking method for return addresses
• Uncertainty about how the CPU handles multiple methods of tracking return addresses
• Discussion of potential issues with self-modifying code and instruction cache invalidation
• Querying about whether data breakpoints could be used to track changes to return addresses
• Discussion of bypassing data breakpoints using return instructions
• Idea to push a fake stack frame with an int3 instruction to change the return address
• Reference to a previous prototype where this idea was explored but not pursued
• Joking and teasing about "L's" (losses) and "W's" (wins)
• Explanation of how the team implemented a similar concept, but with fewer code page injections
• The conversation discusses debugging techniques and tools
• The speaker explains how Visual Studio evaluates functions and adds call frames to selected threads
• A misunderstanding about the level of expertise in debugging leads to an apology and explanation
• The speaker clarifies the difference between friendly banter and insult
• The conversation shifts to a lighthearted discussion about using good debuggers, and not wasting time with bad ones
• The speaker mentions their own debugging methods, including print statements and Vim debugging
• The importance of debugging skills in a debugger
• Learning the "dap" side of things for faster navigation
• Using the Elixir version of Pride for debugging
• Plans to drop Elixir and use printf debugging after this project
• Ideas for future streams on debugging in various languages, including C, Odin, and other compiled languages
• The ability to debug using REPLs or full debuggers in VM languages like Java and Python with PDB (or "Pube G")
• Mention of a game called Pube G and a desire to play it, with one person being hesitant
• Discussion of playing video games as team building for a podcast or stream
• Mention of PUBG (PlayerUnknown's Battlegrounds) and its similarity to startup environments
• Ryan J. Fleury introduces himself, sharing his social media handles and website
• Discussion of the Rad Debugger, including its GitHub page and how to find it
• Substack return address with "nine one one" written in it
• Discussion of a possible joke or meme
• Mention of TJ and his streaming platform, computer enhance.com
• Outro discussion, including praise for Casey's outro
• Vibe called with errors on screen