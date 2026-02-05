• Discussion about Microsoft's use of AI and its potential for creating vulnerabilities
• Introduction to a stand-up comedy segment about security
• Topic shift to FFMPEG and its security concerns
• Guest expert Time Casey, aka Low Level, joins the conversation
• Discussion of Google's OSS Fuzz project and its use of AI to find software vulnerabilities
• FFmpeg Twitter account controversy over Google's 90-day disclosure period for a vulnerability report
• Disclosure timelines for vulnerabilities in open source software
• Use-after-free bug in FFmpeg and Google's role in discovering it
• Responsibility of large corporations using open source software to fix issues promptly
• Rationale behind disclosure timelines and potential risks of early disclosure
• Mitigation vs. public disclosure, including the possibility of increased exploitation
• The speaker discusses a vulnerability in FFMPEG discovered by Google's AI
• The vulnerability is in an old codec used only in the 1995 video game Rebel Assault 2 and is unlikely to affect anyone
• Google submitted an AI report on the issue, but it's unclear what action should be taken
• The discussion highlights the increasing number of CVEs (Common Vulnerabilities and Exposures) and the potential for over-disclosure by companies like Google
• Responsible disclosure and the ethics of publicly disclosing vulnerabilities are debated
• Google's AI has found a critical bug in an old codec, which is not widely used.
• The researcher discussing the issue feels that Google's pressure to disclose vulnerabilities may be misplaced, as they often don't involve human researchers.
• Disclosure of vulnerabilities is meant to inform defenders and potentially mitigate attacks, rather than giving credit to researchers.
• The AI's automation and lack of customization to the actual attack surface are contributing factors to the controversy surrounding this issue.
• FFmpeg deals with many codecs at scale, but the handling of such issues is not clear.
• There's a larger issue about how static analysis tools like Coverity compare to AI-generated reports in finding bugs.
• The scalability issue with using LLMs to find security vulnerabilities
• Signal-to-noise ratio is low for LLM-generated bug reports (1 real out of 50)
• Google's OSS Fuzz project and it's fuzzing of open-source software, including FFMPEG
• Questions about the contractual arrangements between Google and FFMPEG
• Concerns about the tradeoff between finding vulnerabilities and mitigating them
• The argument that companies should spend money on mitigations in addition to vulnerability discovery
• The conversation discusses a software project (Neovim) and its use of Coverity scanning for vulnerability detection.
• The speaker notes that while Coverity scanning is valuable, it can create pressure on maintainers and projects with tight deadlines and public disclosure timelines.
• They mention the potential consequences of not addressing reported vulnerabilities, such as negative ratings in secure software listings.
• The conversation also touches on the human factor in bug reporting and fixing, including the reluctance to allocate resources to minor issues.
• Companies submitting bugs have a high expectation of prioritization and rapid resolution
• Large companies may not submit bugs in good faith, but rather to pressure developers into implementing their features or priorities
• This can lower the value of projects and reduce developer motivation
• Triage time is often lost when dealing with large company bug reports
• Developers must balance prioritizing vulnerabilities with limited hours and resources