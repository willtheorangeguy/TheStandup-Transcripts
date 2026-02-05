[0.00 --> 8.92]  Microsoft is a corporation that turns CEO claims 30% of new code is AI into so many vulnerabilities, dude.
[9.02 --> 10.50]  It's crazy.
[10.86 --> 11.78]  Hello, chat. How we doing?
[12.10 --> 13.00]  Good afternoon.
[13.36 --> 14.54]  That's a great intro, Ed.
[14.62 --> 16.36]  I really appreciated that intro.
[17.04 --> 20.78]  Yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah.
[20.82 --> 21.74]  Anyway, sorry.
[21.86 --> 22.62]  All right, are you guys ready?
[23.22 --> 23.74]  Let's do it.
[24.56 --> 25.00]  Welcome.
[25.36 --> 26.40]  Okay, guys, don't interrupt.
[26.54 --> 27.70]  You can't laugh about it.
[27.70 --> 29.48]  I'm just asking if you guys are ready, okay?
[30.00 --> 30.98]  Welcome to the stand-up.
[31.04 --> 34.44]  Today, we are talking about FFMPEG and security.
[34.60 --> 39.86]  We brought on with us resident security expert and Timu Casey, low-level learning.
[40.58 --> 41.52]  That's crazy.
[41.82 --> 42.18]  Hello.
[42.28 --> 43.16]  You're the one that says it.
[43.16 --> 43.56]  Hello, chat.
[43.64 --> 44.10]  How we doing?
[44.32 --> 45.34]  What an insult.
[45.36 --> 46.20]  I didn't make that up.
[46.32 --> 47.30]  I'm just taking your words.
[47.30 --> 50.16]  I said in Prime's chat, I set the stage.
[50.24 --> 50.56]  It's okay.
[50.62 --> 51.26]  I'm not insulted.
[51.40 --> 51.86]  It's true.
[51.98 --> 52.28]  I am Timu Casey.
[52.28 --> 53.28]  It's a compliment, bro.
[53.52 --> 54.80]  To be in the same category?
[54.80 --> 55.34]  Timu Casey.
[55.52 --> 58.84]  Dude, I'm Casey for the low, low price of $4.99 made out of plastic.
[58.84 --> 59.78]  Manufactured in Beijing.
[59.90 --> 60.88]  That's pretty good, dude.
[60.98 --> 61.44]  That's good.
[61.56 --> 62.52]  I don't even get that.
[62.80 --> 63.04]  Okay?
[63.44 --> 64.64]  Like, I got none of it.
[64.84 --> 66.50]  Or we always have with us Teej.
[66.54 --> 67.86]  We always have with us Trash.
[67.94 --> 68.86]  Everybody say hi.
[69.32 --> 69.72]  All right.
[69.80 --> 70.24]  So, Casey.
[70.46 --> 70.66]  Hi.
[70.78 --> 71.06]  Oh, Casey.
[71.20 --> 71.42]  Sorry.
[71.68 --> 72.98]  Wrong person.
[73.50 --> 74.62]  This is going well.
[74.94 --> 75.82]  This is going great.
[76.00 --> 76.98]  We're crushing it, bro.
[77.54 --> 78.42]  Oh, man.
[78.42 --> 82.52]  Edward, can you please just walk this dog to the park?
[82.62 --> 84.72]  Tell us how, what's going on.
[85.72 --> 86.38]  I don't know.
[86.82 --> 87.32]  Let's do it.
[87.58 --> 88.00]  So, yeah.
[88.18 --> 88.46]  Hey.
[89.18 --> 90.78]  My name is Timu Casey, also known as Low Level.
[91.08 --> 91.46]  So, yeah.
[91.52 --> 92.82]  I'm a security guy, right?
[93.22 --> 97.62]  And you've probably seen maybe a few of my videos about the world of, like, AI, CBEs.
[97.62 --> 98.60]  Can you zoom in a little bit?
[98.64 --> 101.40]  Because you're pixelated and it's, like, impossible to read that tweet.
[102.08 --> 102.56]  Trust me.
[102.58 --> 103.04]  I'll get there.
[103.06 --> 103.40]  I'll get there.
[104.20 --> 105.62]  He's streamed before, bro.
[105.70 --> 107.38]  Bro, I know how to computer, technically.
[108.06 --> 111.40]  Anyways, FFmpeg is this piece of software you're probably all very familiar with.
[111.58 --> 112.72]  It has kind of two components.
[112.72 --> 116.62]  It has the FFmpeg software stack, open source volunteer project.
[116.76 --> 120.58]  It also has the FFmpeg Twitter, which is kind of a whole other animal.
[120.66 --> 122.72]  It's just two parts of the project.
[122.88 --> 124.50]  In and of itself, right?
[124.94 --> 128.02]  And so, FFmpeg's Twitter has got a little bit of heat recently.
[128.18 --> 130.84]  They've kind of stirred the pot for Google.
[131.00 --> 134.12]  So, Google has a couple of projects to find vulnerabilities in software.
[134.68 --> 136.10]  One of them is OSSFuzz.
[136.20 --> 141.70]  Basically, they fuzz or inject bad data into open source projects, wait for bugs to fall out, and report them.
[141.70 --> 144.96]  And their new push is to do LLM-based security, right?
[145.02 --> 153.18]  So, they use a giant LLM to read software and then use the reading of the software to maybe find, like, use after freeze, kind of more complex bugs that fuzzing has a harder time finding.
[153.76 --> 156.66]  And so, Google did report a vulnerability.
[156.92 --> 161.44]  It found a vulnerability in FFmpeg, and it was submitted via their AI system.
[161.44 --> 165.46]  And this kind of pissed off the FFmpeg Twitter guy.
[165.56 --> 169.14]  Again, I don't know if this guy's actually a maintainer or if he, like, runs just the Twitter or if he's a bot.
[169.18 --> 169.76]  I have no idea.
[170.24 --> 179.20]  But basically, his argument is that Google submitted a vulnerability, but they submitted it with a 90-day disclosure period.
[179.30 --> 181.58]  It basically says, hey, this bug is private.
[181.66 --> 184.56]  We're not going to tell anybody until 90 days have elapsed.
[184.56 --> 188.94]  After 90 days, if there is no patch, we will make it public.
[189.54 --> 191.20]  Go and do with that what you will.
[191.34 --> 193.60]  And this kind of started the conversation with FFmpeg.
[193.66 --> 200.64]  FFmpeg is saying, hey, if Google has the compute to find vulnerabilities, they should also be patching the vulnerabilities, right?
[200.64 --> 211.40]  It should not be on a volunteer organization to be at the whim of this company that has all this compute and kind of be held at gunpoint by Google, right?
[211.40 --> 225.46]  And so, it kind of started the whole conversation on Twitter about not only the security disclosure timeline, but also, like, is it right that multi-billion dollar corporations use FFmpeg, Netflix, looking at you, Prime, you know, probably a Prime candidate.
[225.60 --> 228.26]  So, I'm kind of curious what you guys think about the situation, right?
[228.26 --> 233.64]  Is it wrong that Google submitted a bug report to an open source project using large amounts of compute?
[233.78 --> 238.78]  Is it Google's responsibility to find the vulnerability and fix it?
[238.82 --> 239.42]  What do you guys think?
[239.56 --> 241.24]  And I think we may have lost Prime, but we'll keep going here.
[242.32 --> 243.86]  I want to hear Trash's take.
[244.34 --> 244.58]  Yeah.
[245.00 --> 245.86]  You want to hear my take?
[246.36 --> 246.78]  Yeah, I do.
[246.84 --> 248.08]  I want to hear what you've got to say, Trash.
[248.64 --> 254.30]  I personally think it's fair, especially something as popular as FFmpeg, right?
[254.60 --> 255.80]  If anyone's consuming it.
[255.80 --> 260.90]  I don't – the 90-day thing is kind of interesting because, like, they call it as a volunteer thing.
[261.00 --> 262.90]  Like, they shouldn't really be subjected to some timeline.
[263.22 --> 267.28]  But I guess there is some responsibility for having a project as popular as FFmpeg, right?
[267.90 --> 269.32]  So, like, I see it from that angle.
[269.96 --> 273.90]  But, you know, like, how do they hold them accountable to that?
[274.02 --> 278.10]  Like, I mean, sure, they go public with the bug, but does that mean they stuff the picture?
[278.20 --> 281.54]  It's not really like pay us by 90 days or we're going to kill your family.
[281.54 --> 285.22]  No, it's literally just, like, 90 days will go by and then we will publish the bug.
[285.74 --> 286.14]  Broadstone!
[286.64 --> 287.18]  What happened?
[287.38 --> 287.84]  I don't know.
[287.94 --> 288.56]  Did you push?
[288.82 --> 289.58]  On a Friday?
[289.86 --> 290.18]  Never!
[290.40 --> 291.24]  How are we going to figure this out?
[291.50 --> 293.06]  How are we going to figure this out?
[293.30 --> 294.04]  Did I just hear Broadstone?
[294.80 --> 295.38]  Do you guys need the wheel?
[295.38 --> 305.42]  New Vim config.
[305.78 --> 306.88]  That makes sense.
[306.92 --> 308.16]  I'm going to spend a couple hours refactoring.
[308.36 --> 309.00]  I'll beat the plugins.
[312.90 --> 314.36]  Don't guess where your issues are.
[314.54 --> 317.06]  You can see exactly where they are happening with Sentry.
[317.34 --> 319.72]  Get all the context you need to debug any problem.
[319.86 --> 322.64]  Because code breaks, so fix it faster with Sentry.
[322.64 --> 327.10]  So this kind of started the conversation on Twitter about, like, why we even have these disclosure timelines.
[327.28 --> 330.08]  And the rationale behind that is this is a bug in software.
[330.66 --> 334.04]  Whether or not we discovered the bug, the bug exists, right?
[334.04 --> 338.70]  So that means that right now in reality, like, someone is vulnerable to the vulnerability this exposes.
[339.04 --> 340.20]  So we have an option here.
[340.26 --> 345.52]  We can disclose it publicly now and let attackers and defenders know about it.
[345.52 --> 351.10]  Or we wait, try to mitigate it, and then give a disclosure after it's been mitigated.
[351.16 --> 355.76]  But the problem is if you release it before the mitigation, you don't have a patch.
[355.84 --> 357.24]  And now everyone knows a bug exists, right?
[357.24 --> 361.02]  So you kind of heighten the likelihood that it gets attacked, right?
[361.06 --> 361.32]  Right.
[361.50 --> 365.88]  Like, I don't get that threat of, like, making it public because it just does more harm than anything.
[366.02 --> 368.48]  Like, why don't they just help fix it, right?
[368.54 --> 368.82]  Well, sure.
[368.82 --> 374.02]  And that's kind of the question is, like, why, like, this bug is not that it's simple, but it's not that complicated.
[374.12 --> 375.18]  It's a use after free, right?
[375.18 --> 380.54]  Which basically means pointer gets freed, still has a pointer variable in it, but you can use that pointer somewhere else.
[380.56 --> 383.92]  A simple, like, pointer equals null after the free would literally fix this.
[383.98 --> 386.92]  So the question kind of becomes, why did Google not fix this?
[387.18 --> 391.92]  You know, why did Google, who has resources to find the bug, not just fix the bug at the same time?
[391.92 --> 405.36]  Um, my thought here is that just, like, literally they found it in an automated fashion and just submitted the ticket and, like, no one was, like, the process of finding the bug did not also include mitigation because I don't think they had the scale of people to do that.
[405.40 --> 409.32]  I'm not sure if Big Sleep, um, can find and mitigate bugs, if that makes sense.
[409.56 --> 410.80]  But what are your thoughts, Teej?
[410.80 --> 427.74]  Yeah, I mean, it's, there's definitely, like, a give and take here of it's nice to get bug reports that are reproducible and can tell you exactly what happens and how to do this and what the path is to fix.
[427.74 --> 431.72]  That's, like, that is a valuable thing that Google's providing, so that's nice.
[431.72 --> 440.36]  But it does feel, like, really crummy to be on the receiving end of them where it's, like, one, it's not super obvious.
[440.68 --> 445.90]  I don't know in this particular case, but at least generally, like, is this really even exploitable?
[446.14 --> 449.40]  Is this really, like, a thing that actually could happen in practice?
[449.72 --> 453.64]  Is this, like, you know, does someone have to do something insane?
[453.64 --> 461.04]  Like, oh, this only happens when someone tries to cut out minute, you know, seven in a 49-hour video or something like that, right?
[461.04 --> 474.44]  Like, and so, especially, I can understand the difficulty of being on the maintainer side and you're getting effectively, like, an automated LLM bug report from Google.
[474.54 --> 476.72]  And Google's just like, well, you guys should just fix this, bro.
[477.00 --> 478.04]  Like, bro, just fix it.
[478.18 --> 478.86]  Just deal with it.
[479.30 --> 480.20]  Registrate, just deal with it.
[480.22 --> 480.70]  And we're going to.
[480.70 --> 483.48]  You don't have billions of dollars of recruiting spend like we do?
[483.62 --> 484.48]  Whoa, what do you mean?
[484.64 --> 485.26]  That's not possible.
[485.26 --> 511.72]  And so that part and the, especially, like, from the maintainer side, they probably see this, like, upward slope of how many times they're going to get issues and disclosures like this where they're like, how could we possibly keep up with potentially the volume of how many things Google could be, like, sending or submitting to us all the time?
[511.72 --> 513.42]  And then it's like, that's just Google.
[513.62 --> 516.94]  What if, like, Amazon wants to do the same thing and Netflix wants to do the same thing?
[517.20 --> 530.62]  And now you're like, I have, like, 25 of the, you know, Fortune 500 sending me bug reports every day of things that we need to fix and then no, like, follow-up situation or, like, no maintenance fee or nothing.
[530.74 --> 532.52]  It's kind of just, like, just fix it.
[532.52 --> 539.96]  But, I mean, the software is, like, I mean, I don't know what FFMPEG's license is, but I'm assuming it's provided without warranty.
[540.62 --> 541.10]  So it's, like.
[541.10 --> 541.92]  Yeah, it's in the license.
[542.24 --> 542.86]  Yeah, yeah, right.
[542.86 --> 543.74]  So, yeah, that's a good question.
[543.86 --> 544.78]  That's a good point you've brought up.
[544.80 --> 546.84]  And that's actually what FFMPEG highlights, I think, in this.
[546.92 --> 550.94]  So to kind of bring up Trash's point and your point about, like, how exploitable is this?
[551.02 --> 553.90]  How much does this matter, right?
[554.04 --> 554.24]  Yeah.
[554.24 --> 559.44]  So the vulnerability is actually in a codec written by a hobbyist from 1995.
[559.80 --> 564.76]  Not that the code is from 1995, but it supports a codec that has only been used in 1995.
[565.42 --> 573.56]  It is a proprietary LucasArts codec used in a video game, Rebel Assault 2, for the first 20 to 10 frames, 10 to 20 frames.
[574.58 --> 579.44]  And this is basically the only use of this codec that we're aware of.
[579.90 --> 582.30]  And Google submitted an AI report to it, right?
[582.30 --> 584.84]  So it's kind of a two-sided sword.
[584.96 --> 594.02]  It's like, okay, they're spending all of this compute spend and basically bombarding open source with these issues, comma, but also no one is vulnerable to this vulnerability.
[594.34 --> 596.26]  So, like, why are we talking about it so much?
[596.30 --> 597.54]  Why has it gotten so much attention?
[597.86 --> 602.86]  And I think it highlights to what you're talking about, the increasing slope of CVEs.
[602.90 --> 606.26]  I think AI, while it's not good right now at bug hunting, it's going to get better.
[606.32 --> 607.46]  It's only going to keep getting better.
[607.46 --> 614.12]  And so for an organization like FFMPEG, if they get 1,000 bug reports from Google's big sleep, what are they supposed to do?
[614.80 --> 619.74]  It's a good thing, naturally, that they found the vulnerabilities, but now what?
[619.90 --> 620.26]  You know what I mean?
[620.28 --> 621.18]  What are they supposed to do with that?
[621.18 --> 629.04]  Yeah, the thing, too, is like, and I get it, you know, the public, like, at some point they want to make it public.
[629.36 --> 631.58]  They want to be able to say, we found these things.
[631.68 --> 637.78]  They feel like they need to do some disclosure of it, et cetera, to let people know who are or potentially could be affected by it.
[637.78 --> 650.14]  But it's also kind of like sending it public makes it so that attackers now target this thing who don't have access to a trillion dollars of GPUs and all of the latest things to find the bug.
[650.14 --> 658.10]  So, like, maybe attackers would literally never find this bug, except that now Google's like, hey, here's a bunch of unfixed security issues in FFMPEG.
[658.32 --> 660.82]  Like, in case anyone was wondering, we've got a full platter.
[661.26 --> 663.04]  Try and exploit them if you like.
[663.36 --> 665.68]  Yeah, and so that's the whole argument about disclosure, right?
[665.68 --> 677.48]  It's like you are disclosing in a bug exists that defenders can do the defender thing, but also you are now removing the act of vulnerability research and just giving pox to attackers, right?
[677.48 --> 680.26]  So, not sure there actually is an answer to this question.
[680.62 --> 685.34]  I just think it spawned a very useful conversation on Twitter.
[685.74 --> 695.66]  And I would like, you know, people, I think, I'm also curious to hear people that are not in, like, security spaces say, because obviously I have a very biased, you know, potentially myopic lens of how I look at this.
[695.68 --> 699.46]  But, you know, people actually maintain software as their day job is probably very different.
[699.66 --> 700.84]  So, Prime, what do you think about this, man?
[701.18 --> 719.70]  So, here's my big problem with the whole situation and really responsible disclosure overall is that none of this takes into account who or what they're disclosing upon, which I think is, I don't know if you guys talked about it, but I think that that's just like a huge, it's just a huge problem, right?
[719.70 --> 734.52]  Because if you have, say, a product that everybody uses and it's a paid-for service in which company has actual engineers and it's their jobs to maintain, then, yeah, I feel like you are more allowed to be like, hey, you need to fix this bug and we are disclosing this.
[734.80 --> 737.12]  But what does, like, Google gain about disclosing?
[737.12 --> 748.76]  I always figure disclosing is a mechanism in which you try to pressure someone to either, A, make a fix, or, B, you want to get the street cred for being able to find this really unique, novel security thing so it helps your resume.
[749.16 --> 751.42]  This is just Google's big AI.
[752.14 --> 753.78]  They can just be a chart.
[753.88 --> 758.52]  We found 47 critical bugs and 14 different OSS projects.
[758.72 --> 758.98]  Boom.
[758.98 --> 763.50]  Like, they only need high-level stuff, so I don't understand even Google's, like, pressuring to begin with.
[763.80 --> 768.36]  The thing that they're pressuring against isn't created by people being paid or full-time employees.
[768.42 --> 775.88]  So it's like all of it just seems just wrong in itself because there's no individual person that's actually getting, like, some sort of street credit.
[775.94 --> 781.52]  It's not like Bob from, you know, the security department found this really cool 1995 Kodak issue.
[782.04 --> 785.20]  He was playing some Star Wars, realized something, and hacked his mainframe.
[785.20 --> 792.96]  Like, it's just, like, not happening, and so that's – I guess that's where my confusion at is why is Google doing this to these people to begin with?
[794.80 --> 796.58]  Yeah, so, I mean, it's a good question.
[796.94 --> 804.44]  I don't think that the disclosure process is a process meant to give people credit.
[804.70 --> 807.56]  I think that is a side effect of disclosure, right?
[807.56 --> 817.60]  I think when a researcher discloses, it is supposed to be that they are disclosing to tell the vendor and to tell the public, hey, your stuff is vulnerable, comma, also look at me.
[817.64 --> 818.44]  I found this bug, right?
[818.46 --> 821.32]  If you're doing disclosure for clout, that's a separate conversation.
[821.52 --> 824.30]  Now, to your point, this is not done by a researcher.
[824.60 --> 826.68]  This is done by an AI, right?
[826.70 --> 830.16]  So you could argue that, like, Google is getting clout, but realistically –
[830.16 --> 830.76]  Very human of it.
[831.26 --> 831.60]  What's that?
[831.60 --> 833.02]  Like, give me the credit, bro.
[833.06 --> 834.74]  It's the most human thing a Google AI has ever done.
[834.74 --> 836.06]  I want it right now.
[836.14 --> 836.84]  Yeah, exactly.
[837.30 --> 839.50]  Maybe they said chaos orbs were on the line.
[839.74 --> 840.16]  You know what I mean?
[840.20 --> 840.68]  Like, I don't know.
[840.84 --> 842.92]  And it's like, I've got to put this on Twitter right now.
[843.00 --> 843.84]  I've got to go talk about this.
[844.72 --> 845.66]  No, I mean, that's the thing.
[845.92 --> 852.52]  Disclosure is about telling – I don't know if you missed this, Prime, because you may have been out with internet issues, but disclosure is about telling defenders.
[852.76 --> 858.48]  Disclosure is about, like, hey, whether or not we report on this publicly, the bug exists, right?
[858.48 --> 862.24]  And we know about it secretly, attackers may know about it secretly, right?
[862.28 --> 867.88]  So we have to inform people that this bug exists because you may be at risk of its exploitation.
[868.48 --> 873.28]  Now, that's kind of the problem with this codec is that, like, literally nobody has this codec enabled.
[873.40 --> 875.62]  Like, this does not compile by default into FFmpeg.
[875.66 --> 877.06]  You have to explicitly enable it.
[877.34 --> 879.94]  And the only place it's known to be used is in a game from 1995.
[880.20 --> 886.86]  So it's like – to me, it feels like Google's AI is set up to fuzz open source software.
[886.86 --> 889.70]  That's what OSS fuzz does, and I'm sure that's exactly how Big Sleep operates.
[890.14 --> 898.20]  And so the AI probably triages all the codecs that exist, and it found a bug in a codec, and it gave it the default disclosure timeline.
[898.70 --> 907.36]  And I think it's the combination of, like, all of those factors, like the automation behind it, the lack of customization to the actual attack surface that pisses people off.
[907.42 --> 912.66]  It's like you spent a billion dollars or whatever on this niche codec, found a bug, and now it's my problem.
[912.84 --> 913.36]  You know what I mean?
[913.36 --> 918.24]  But it does highlight a larger issue that you highlighted, like, how does FFmpeg deal with this at scale?
[918.38 --> 919.16]  That I don't know.
[919.62 --> 920.28]  So two things.
[920.38 --> 922.78]  One, there's this whole AI finding bug thing.
[923.04 --> 925.50]  I know you're saying AI is really great at finding bugs.
[925.86 --> 931.10]  They have been pretty good at finding bugs, especially if you give them stack traces and you give some sort of hinting to them.
[931.10 --> 939.24]  But generally, all the security reports I've seen where things are just like, go find a security bug have all come up as, you know, predominantly noise.
[939.36 --> 948.54]  I know Daniel, gosh, I can't seem to remember his last name, from Curl is just like, you don't submit AI-generated reports.
[948.62 --> 950.36]  You are not allowed to do this at all.
[950.60 --> 952.14]  And he gets just constantly bogged down.
[952.20 --> 953.24]  A bunch of people are getting bogged down.
[953.24 --> 959.20]  So I don't know how convenient these things are comparatively to something some coding guy is suggesting, which is Coverity.
[960.48 --> 967.18]  What's your experience with Coverity at finding, say, use after free bugs comparatively or static analysis tools in general compared to these AI things?
[968.18 --> 968.30]  Yeah.
[968.40 --> 973.14]  So a static analysis tool will always be concretely better.
[973.68 --> 973.76]  Right?
[973.76 --> 978.76]  Like, it will always, like, if Coverity says there's a use after free, there is use after free.
[978.84 --> 979.42]  There is no question.
[979.54 --> 979.64]  Yeah.
[979.92 --> 986.62]  The problem is that is basically a one-for-one scaler against human talent.
[987.00 --> 987.28]  Right?
[987.38 --> 995.90]  Like, you need the engineer equipped that knows how to use Coverity, that knows the code base, to use Coverity and to triage if the use after free is actually there.
[995.94 --> 996.06]  Right?
[996.06 --> 996.66]  Which it likely is.
[997.24 --> 1003.66]  The attempt with LLMs is to take security talent, which does not scale well against software engineering talent, and scale it.
[1003.96 --> 1004.12]  Right?
[1004.50 --> 1012.90]  But the problem that we run into is kind of what I think whoever said that in chat is talking about is the problem that Sean Healan talked about in his article, where he basically found a zero day with LLMs.
[1013.40 --> 1016.66]  But the problem is that the – let me see if I can find the verbiage here.
[1017.08 --> 1025.10]  The signal-to-noise ratio, which is basically how many are real versus how many are fake, of LLM-generated bug reports is 1 to 50.
[1025.10 --> 1038.06]  So, you may ask an LLM for find me a use after free vulnerability in the SMB server for Linux, and it will give you 50 reports, all of which detail this huge stack.
[1038.12 --> 1039.98]  And, like, this is the bug right here.
[1040.92 --> 1042.70]  Only one of them are real, if that.
[1043.04 --> 1043.30]  You know?
[1043.30 --> 1047.46]  So, that's when I say, like, LLMs are getting there.
[1047.56 --> 1048.42]  They're not good yet.
[1048.56 --> 1050.70]  Like, an LLM can find a bug in software, right?
[1050.74 --> 1054.56]  The problem is just, like, how do you deal with the scale of that?
[1054.60 --> 1058.38]  Because now I have to triage 50 potentially fake vulnerabilities, you know?
[1059.96 --> 1060.52]  So, yeah.
[1060.52 --> 1069.46]  Yeah, and, like, Google and some of these other places, they don't have any, like, contractual things with FFMPEG or anything.
[1069.62 --> 1070.66]  That's what seems crazy to me.
[1070.82 --> 1086.14]  Like, I feel like wouldn't you – if you're using it, like, an insane amount for that core of a thing – like, I get it that, like, okay, maybe, you know, like, left pad 37, you can't figure out that it's an important, like, dependency for your company, and so you don't.
[1086.14 --> 1090.06]  It seems like they don't have people funding, like, FFMPEG time or something.
[1090.06 --> 1091.38]  Like, I literally have no idea.
[1091.56 --> 1096.30]  I couldn't find or see anything there where they had, like, maybe some SLA or whatever with them.
[1096.98 --> 1097.04]  Yeah.
[1097.12 --> 1105.60]  I am not aware of the contractual or, like, legal nature of this arrangement, but Google does spend a lot of resources on fuzzing open source software.
[1106.20 --> 1108.34]  This is a project Google OSS Fuzz.
[1108.34 --> 1126.16]  Literally, the Google team spends Google Compute in Google Cloud Platform to constantly be pulling, setting up harnesses for and fuzzing a variety of open source software, which is, like, for example, FFMPEG is literally a target inside of OSS Fuzz.
[1126.26 --> 1132.12]  If you go to projects here, you'll see they have all these fuzzers and harnesses set up for all this software, one of them being FFMPEG that I'm getting to.
[1132.12 --> 1138.18]  And so they have been spending a lot of money on finding vulnerabilities, right, which is a good thing, naturally.
[1138.34 --> 1140.86]  But, like, where does that tradeoff happen, right?
[1140.86 --> 1143.82]  Like, when do you now also help mitigate the vulnerabilities?
[1143.82 --> 1160.04]  Because if you're acknowledging that, like, you are a big company, you are doing this altruistic thing to help make the world a safer place, but you also acknowledge you have more money than every volunteer organization, like, how do you go about, you know, rectifying that?
[1160.14 --> 1163.82]  And the answer, in my opinion, is, like, spend some money on mitigations as well.
[1163.96 --> 1165.02]  I don't think that's been done so far.
[1165.10 --> 1171.40]  And that's the whole argument that FFMPEG is making is, like, hey, just give us a, you know, a patch file or something.
[1171.40 --> 1173.78]  Can I ask a quick question?
[1174.20 --> 1174.34]  Yeah.
[1174.82 --> 1178.84]  What do you think the chances are that Trash is looking at Pokemon or paying attention right now?
[1178.90 --> 1180.56]  That's so intense right now.
[1180.56 --> 1188.76]  I was looking at the readme for OSS fuzz, and I was trying to understand how does a project qualify to be fuzzed by this?
[1189.54 --> 1190.38]  That I don't know.
[1190.86 --> 1191.64]  That I do not know.
[1191.66 --> 1192.74]  Trash, great question.
[1193.16 --> 1193.90]  Good question.
[1194.10 --> 1194.46]  Doubters?
[1194.70 --> 1199.82]  See, what if they start fuzzing my code base and they start sending me stuff?
[1199.82 --> 1202.98]  I'm like, whoa, buddy, I don't maintain this code no more.
[1203.00 --> 1207.98]  Yeah, do projects opt in to be a part of this Google sleuth or whatever they call it, Google?
[1208.12 --> 1208.92]  That's actually a great question.
[1209.06 --> 1209.88]  I do not know.
[1209.96 --> 1212.16]  I do not know the process there.
[1212.44 --> 1216.94]  Because I don't like that because it feels like FFMPEG should be able to say, hey, we don't want these reports.
[1217.32 --> 1219.78]  Like, you shouldn't file CVEs against us.
[1219.78 --> 1223.54]  Well, I mean, so I think the argument there is, like, why would you opt out?
[1224.42 --> 1225.54]  Yeah, I think they want them.
[1225.54 --> 1229.72]  It's just there's probably a signal to noise.
[1230.08 --> 1230.30]  Well, it didn't sound like they wanted them.
[1230.34 --> 1231.32]  They wanted them to fix it.
[1231.44 --> 1233.76]  They didn't even want, like, they're like, oh, well, just send us a patch.
[1233.82 --> 1234.84]  They don't want the report.
[1234.96 --> 1236.02]  They want the result.
[1236.08 --> 1236.48]  Well, sure.
[1236.60 --> 1245.56]  I think in this particular case, I'm not sure if the complaint was generally speaking that they want, like, Google engineers just sending a bunch of fixes for everything.
[1245.56 --> 1250.56]  But, like, in this particular case, it felt like, okay, the fix is relatively simple.
[1250.84 --> 1254.52]  You know, Ed, you gave an example of one way that you could fix it, like, quite easily.
[1254.92 --> 1256.56]  Like, don't send us a report.
[1256.66 --> 1258.48]  Just send us, like, a fix for this.
[1258.78 --> 1258.92]  Yeah.
[1259.20 --> 1261.68]  And then, like, because that makes sense.
[1261.74 --> 1271.32]  But there's going to be use after freeze or other, like, actual, you know, slightly more complicated vulnerabilities that they could find that, like, you would still like, I think, to get those.
[1271.32 --> 1281.30]  So, like, for NeoVim, I know we've had, I'm pretty sure Coverity scanning for a long time and, like, used that for large open source projects.
[1281.38 --> 1282.56]  I'm pretty sure it's free as well.
[1283.12 --> 1284.80]  Like, I'm pretty sure it was free for NeoVim.
[1285.36 --> 1291.44]  And so there are, like, and we've fixed real things with that and also sent, like, upstream patches to Vim.
[1291.60 --> 1294.34]  And, like, overall, that's, like, helpful.
[1294.34 --> 1295.06]  Right.
[1295.16 --> 1306.02]  But in general, I don't think Coverity, I don't think NeoVim gets a deadline for when this is to fix and, like, a disclosure timeline of when it's going to get published.
[1306.02 --> 1306.38]  Right.
[1306.38 --> 1310.36]  It's, like, it's a private, you log into this and view a dashboard.
[1310.74 --> 1311.18]  Yeah.
[1311.18 --> 1311.58]  Right.
[1311.66 --> 1323.68]  And then also there's, like, some severity levels and some other stuff like that where you could at least try and decide if it's even worth fixing or it's, like, okay, sure, this happens when XYZ thing happens, whatever.
[1323.82 --> 1325.56]  It's not actually, like, a big deal.
[1327.20 --> 1329.66]  So, you know, so it's, like, it is valuable.
[1329.78 --> 1330.70]  It's very valuable to get.
[1330.78 --> 1336.46]  It helps you fix things and, like, keep the project in a better state and less, you know, big hacks.
[1336.46 --> 1347.82]  But, yeah, it does feel, I can see how, like, with this timeline pressure applied to it and, like, there's no, like, cool, you're donating this thing to us to give it to us and stuff and that's nice and everything.
[1348.44 --> 1352.62]  But it also does apply real pressure on maintainers and, like, projects.
[1352.78 --> 1363.18]  And if they don't close, I thought I was reading from them, like, if they don't close enough of these, they get, like, dinged in, like, other, like, ratings of stuff like how secure their project is or something.
[1363.18 --> 1379.24]  And of just, like, hey, if you have a bunch of CVEs reported and you don't fix them, even if they're, like, you know, not important, you get, like, dinged somewhere in some universe of, like, secure software that can run places and people are happy to use.
[1379.36 --> 1380.12]  I don't know exactly.
[1380.28 --> 1382.20]  That's, I don't have any secure software.
[1382.40 --> 1384.04]  So, like, trash, you know.
[1384.28 --> 1385.32]  Nothing written in rust, baby.
[1385.48 --> 1385.84]  Unfortunately.
[1385.98 --> 1391.16]  So, someone in chat linked how you get accepted into this project and I'm about to submit all of Dax's projects.
[1391.66 --> 1392.88]  Oh, that's the thing.
[1393.18 --> 1398.10]  And so he could start tweeting, hey, man, I just got an LLM bug report.
[1398.20 --> 1398.96]  This is insane.
[1401.74 --> 1403.36]  Open code is going in there.
[1403.70 --> 1406.86]  Open code CVEs left and right.
[1406.98 --> 1407.62]  I love this.
[1408.18 --> 1408.22]  Beautiful.
[1408.40 --> 1408.76]  Trash.
[1409.00 --> 1410.94]  I'm going to make the PR and link it.
[1411.62 --> 1412.50]  That's so good.
[1412.76 --> 1413.50]  That's amazing.
[1414.20 --> 1414.60]  Yeah.
[1414.78 --> 1415.64]  So, I mean, that's pretty much it.
[1415.68 --> 1418.18]  It's less of an answer, less of a, wow, crazy bug.
[1418.18 --> 1423.08]  It's more just, like, a higher level discussion about, like, you know, it is a good thing that people are finding bugs in software.
[1423.18 --> 1424.42]  That is a naturally good thing.
[1424.48 --> 1425.38]  But, like, then what?
[1425.50 --> 1425.66]  Right?
[1425.70 --> 1430.02]  Like, what are you supposed to do if you're a team of 10 people against Giga Corporation X?
[1430.10 --> 1430.26]  Right?
[1430.28 --> 1431.66]  And, you know, I don't know the answer to that.
[1432.12 --> 1432.26]  Yeah.
[1432.28 --> 1433.46]  I mean, it's already like that at work.
[1433.54 --> 1437.76]  If someone reports a bug on my software internally, I'm like, oh, I don't want to fix that right now.
[1438.16 --> 1438.98]  You know what I mean?
[1439.88 --> 1440.70]  You know what I'm saying?
[1440.76 --> 1442.48]  Like, I mean, it depends on the severity.
[1442.64 --> 1445.36]  Like, in this case, it was like, like you said, it was such a niche bug.
[1445.42 --> 1449.88]  So, if someone reports that, I'm like, you know, make a Jira ticket and then maybe I'll open Jira next year.
[1450.06 --> 1450.30]  You know?
[1450.80 --> 1453.90]  Trash, you said you admitted last week you've never opened Jira in your lifetime.
[1453.90 --> 1456.22]  I said maybe if I opened up Jira next year.
[1456.68 --> 1457.30]  Oh, okay.
[1457.38 --> 1457.66]  All right.
[1458.12 --> 1458.34]  Yeah.
[1458.40 --> 1462.20]  I mean, that is one, like, human factor that I think a lot of people tend to forget.
[1462.30 --> 1463.42]  Like, maybe the FFMPEG guy.
[1463.42 --> 1464.56]  I don't know where he's worked or whatever.
[1464.92 --> 1465.94]  But, like, even where I work.
[1466.06 --> 1467.44]  Like, large company, right?
[1467.84 --> 1474.34]  If we on my team submit a bug to the engineers, like, they have to reallocate resources to fix that bug.
[1474.40 --> 1478.56]  And, like, some bugs we submitted, they're like, hey, that's going to take an entire quarter to deal with.
[1478.66 --> 1480.98]  Like, we don't have the people right now.
[1480.98 --> 1482.26]  I assume that's the minimum at Microsoft.
[1483.12 --> 1483.62]  What's that?
[1485.06 --> 1487.78]  I assume that's the minimum at any big company, right?
[1487.90 --> 1488.52]  Like, Amazon.
[1488.52 --> 1488.94]  Netflix.
[1488.94 --> 1490.40]  It's just like no matter where you submit the bug.
[1490.40 --> 1490.72]  Amazon, anybody.
[1490.72 --> 1491.46]  Yeah, 100%.
[1491.46 --> 1491.64]  Yeah.
[1491.64 --> 1492.68]  I was speaking of Microsoft.
[1492.80 --> 1493.06]  Hold on a minute.
[1493.06 --> 1493.86]  I had a meme.
[1493.94 --> 1494.28]  Give me a second.
[1494.50 --> 1494.68]  Hold on.
[1494.72 --> 1494.86]  Yeah.
[1495.12 --> 1496.42]  Yeah, it's just like no matter where.
[1496.52 --> 1496.98]  Yeah, there you go.
[1497.00 --> 1497.80]  That's the one I was looking at.
[1498.02 --> 1498.32]  Yeah.
[1498.38 --> 1499.86]  Dude, it's so good.
[1500.00 --> 1501.28]  I love this.
[1501.50 --> 1504.58]  And what's funny is that, like, it wasn't this big.
[1504.64 --> 1506.46]  It started as a single article.
[1506.72 --> 1509.66]  And as more bugs came out, people kept us appending to the meme.
[1510.34 --> 1511.44]  Oh, it's so good, dude.
[1511.46 --> 1512.22]  Oh, that's funny.
[1512.64 --> 1512.82]  Yeah.
[1512.92 --> 1513.20]  Anyway.
[1513.34 --> 1513.78]  So, I mean.
[1513.98 --> 1514.84]  That at these big corporations.
[1514.96 --> 1516.00]  Because I know at Netflix, we'd have.
[1516.58 --> 1518.26]  It depends on who submits it to.
[1518.38 --> 1520.40]  And so, I think there's one thing that's really important here.
[1520.40 --> 1530.74]  Or at least I think something that can happen is if Google does submit these things and put a lot of pressure on people, also the value of the project does go down.
[1531.20 --> 1535.26]  Because now when I hear someone making this kind of submission, I'm like, oh, this isn't that important.
[1535.26 --> 1541.68]  Because one time I got a bug from Reed Hastings himself saying, hey, there needs to be a vignette on this thing.
[1542.04 --> 1544.42]  And so, it's just like, you know how fast that got fixed?
[1544.50 --> 1548.86]  It got fixed way, way faster when your VP is telling you what the big man said upstairs.
[1548.86 --> 1549.60]  A vignette?
[1549.72 --> 1550.22]  Are you kidding?
[1550.32 --> 1551.84]  I got to fix that yesterday.
[1552.40 --> 1558.64]  But, you know, like, but if a company keeps on submitting things and they kind of tarnish their name, people may not take the things they say as seriously.
[1558.64 --> 1561.58]  And so, there is kind of like a, there's a whole problem there.
[1562.06 --> 1576.80]  The other thing that, which I think is a completely reasonable, like, complaint from FFMPEG team and more broadly in, like, open source generally is just like, it also takes time not only to do the fix, but to do the triage.
[1577.36 --> 1577.76]  Right?
[1577.82 --> 1579.04]  And it, like, is oftentimes lost.
[1579.12 --> 1581.40]  Like, getting a bug report is not free.
[1581.40 --> 1586.46]  So, there is something, I don't know how to weight that, right?
[1586.50 --> 1593.04]  Like, I would still probably, on average, I guess, prefer to know what vulnerabilities exist in the software I'm maintaining versus not.
[1593.30 --> 1597.12]  But also, like, there's just only so many hours in the day, bro.
[1597.24 --> 1599.78]  There's just, like, there's only so many hours.
[1599.78 --> 1610.84]  And if I'm going to spend all of it on triaging BigCo threat vector level low sent to me, like, I'm going to be sad, you know?
[1610.96 --> 1613.68]  I'm just going to not want to work anymore or do anything.
[1613.92 --> 1614.90]  And, like, that, yeah.
[1615.98 --> 1616.68]  I don't know.
[1617.58 --> 1618.24]  Yeah, it's tough, man.
[1619.44 --> 1619.84]  Interesting.
[1620.48 --> 1621.36]  Interesting, pinteresting.
[1621.62 --> 1626.08]  You know, this kind of flows nicely into something we can talk about here for a moment here.
[1626.48 --> 1628.18]  What a transition, though.
[1628.18 --> 1631.38]  I'm going to announce the transition, and we shall transition.
[1631.92 --> 1633.84]  Let's just end the episode.
[1634.40 --> 1635.06]  I'm done.
[1635.06 --> 1635.50]  I'm done.
