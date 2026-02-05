[0.00 → 1.30] You guys ready to talk today?
[1.54 → 2.62] Today's a pretty good topic.
[3.12 → 3.92] Are you guys ready for today?
[4.84 → 5.32] I'm ready.
[5.52 → 6.02] Okay, yeah.
[6.16 → 7.18] I mean, I'm not ready.
[7.18 → 8.74] By the way, if you guys don't know, TJ is R&D.
[8.74 → 9.86] We're going to start anyway.
[14.54 → 19.46] Today we are talking about Phil C, the memory-safe C.
[19.58 → 20.22] Is it useful?
[20.34 → 20.78] Is it good?
[20.84 → 22.52] Is it the future of C?
[23.28 → 27.92] As always, we have with us Siege, creator of a C-based memory course on boot.dev,
[27.92 → 31.06] where you get to go over how a language – what was that, TJ?
[31.22 → 31.68] Good point.
[31.78 → 32.38] Yes, great point.
[32.38 → 34.14] Okay, well, don't interrupt me saying that.
[34.20 → 35.70] I'm like in the middle of a really strong intro.
[35.70 → 36.76] All right, anyway.
[37.08 → 38.70] As always, we have with us Siege,
[38.76 → 41.64] D.V., creator of a C-based memory course on boot.dev,
[41.68 → 43.20] where you go over how to create a garbage collector
[43.20 → 46.62] and Casey Juratory, legendary C-Chad game programmer.
[46.74 → 50.02] Check out ComputerEnhanced.com for his amazing courses and lecture.
[50.38 → 52.46] And we also have a special guest with us today,
[52.46 → 58.10] low-level security extraordinaire, and also C and ASM Chad.
[58.18 → 60.64] Check out low-level. Academy for amazing courses
[60.64 → 62.62] and all your low-level needs.
[63.04 → 63.38] Appreciate it.
[63.38 → 64.66] Now, hey, no problem, buddy.
[65.00 → 67.08] So now, let's talk a little bit about Phil C.
[67.08 → 69.68] Ed gets to say a comment, and it didn't break the intro.
[69.68 → 70.46] I'm the last one.
[70.60 → 71.18] Suck it, nerd.
[71.50 → 72.70] He said it cleanly.
[72.74 → 73.64] He said it cleanly.
[73.70 → 74.82] He got it in there, Siege.
[74.84 → 75.84] It was like part of the flow.
[75.84 → 76.70] All right, my apologies.
[76.70 → 78.48] I was talking, TJ, and you just were like,
[78.72 → 80.10] hey, that's a great point.
[80.10 → 83.78] I didn't even think about how that would be relevant to this today.
[85.24 → 86.86] So I was surprised.
[87.06 → 87.68] Go ahead, Brian.
[88.32 → 92.28] Anyway, just for everybody to understand a little bit about Phil C,
[92.40 → 97.14] here's some basic C code along with a special standard Phil up at the top
[97.14 → 100.20] that's brought in that allows a special kind of printing character
[100.20 → 101.36] called the capital P.
[101.76 → 103.36] And in there, it will actually print out,
[103.36 → 104.18] hey, look at this.
[104.24 → 106.46] This pointer actually has three values in it.
[106.60 → 109.84] You, the C developer, will only see just the integer.
[110.10 → 113.20] But underneath the hood, there's actually some extra information stored.
[113.28 → 115.50] And this actually shows its lower, and it's upper bound.
[115.66 → 117.70] You can see that we allocated 16 bytes.
[117.92 → 121.78] And of course, there's 16 bytes difference between the lower and the upper.
[121.88 → 122.58] That is fantastic.
[122.96 → 125.02] And with that, it allows for some special behaviour.
[125.24 → 125.84] So here we go.
[125.92 → 127.34] We mallow 16 bytes again.
[127.48 → 134.24] I attempt to access byte 42, or technically the 42nd index into here,
[134.32 → 135.40] which would be out of bounds.
[135.40 → 138.04] And Phil C says, ha, ha, ha, ha, ha.
[138.40 → 141.66] I've thwarted such an easy and very obvious thing.
[142.00 → 144.62] Now, some of the things about Phil C that makes it a little bit unique
[144.62 → 148.88] and probably is going to make a lot of people mad is it's actually garbage collected.
[149.00 → 149.46] That's right.
[149.54 → 151.34] It's a C that is garbage collected.
[151.44 → 153.90] So if you look underneath the hood, even if you call free,
[154.46 → 156.52] it does not technically free it.
[156.78 → 158.38] It marks it as being freed.
[158.38 → 164.06] And then later on, the asynchronous, multithreaded, behind-the-scenes garbage collector
[164.06 → 166.14] will go and free that memory.
[166.28 → 167.24] So it's a very different.
[167.26 → 169.36] This is not your grandfather's C, okay?
[169.50 → 171.58] This is modern C.
[172.06 → 173.38] Technically, whatever.
[173.64 → 173.96] That's fine.
[174.80 → 175.64] Good one, TJ.
[176.20 → 177.54] I'm just saying he made one.
[177.62 → 177.94] It's fine.
[178.00 → 178.26] It's okay.
[178.42 → 178.78] Keep going.
[178.92 → 180.44] They have garbage collector in C for a while.
[180.52 → 181.20] But yeah, that's okay.
[181.38 → 181.62] Go ahead.
[181.68 → 182.08] Yeah, I know.
[182.10 → 184.62] But that's not like your standard operation in C.
[184.72 → 185.76] People don't think C.
[185.88 → 187.54] Oh, yeah, that garbage collected language.
[187.54 → 189.94] Like, that's not the first thought that comes into people's heads.
[190.06 → 192.34] Whereas this is garbage collection at all times.
[192.50 → 195.10] Yeah, standard C does not have a garbage collector.
[195.16 → 195.86] That is true.
[196.12 → 199.56] You're talking about some additional thing when you talk about C garbage collection, right?
[199.62 → 199.94] Yes.
[200.16 → 200.60] Yes, yes.
[200.62 → 203.94] Whereas this is going to be like your standard experience is actually garbage collected.
[204.14 → 209.48] Now, obviously, Phil C does come with a lot of performance penalties and runtime checking.
[209.62 → 212.52] Like, when I did that little check into P42,
[213.18 → 216.06] it obviously did a runtime check on that when you attempt to run it.
[216.06 → 217.80] It crashes your program successfully.
[218.58 → 221.02] And so that is a yes, TJ.
[221.02 → 226.82] I was wondering, do we have any bouncing balls to show the performance penalty for charts?
[226.96 → 230.28] Because I feel like, as you said, performance penalties,
[230.54 → 236.78] I literally wanted to slap myself in the face that I did not bring a bouncing ball chart to benchmark this for Casey.
[236.98 → 238.34] I'm so angry.
[238.72 → 239.74] I'm so angry.
[239.74 → 242.48] As you can see from this diagram.
[243.26 → 243.66] Right.
[244.20 → 245.12] Very scientific.
[245.30 → 246.82] There are some performance penalties.
[246.96 → 250.64] It's like, no, actually, I can't see from that diagram because the diagram sucks.
[251.00 → 253.12] That's why I can't see it from that diagram.
[253.84 → 254.72] That's pretty funny.
[254.72 → 258.58] Look at all these engineers sitting at their neat little desks.
[259.30 → 261.84] It takes dirty work to keep a code base clean.
[262.34 → 265.76] Every day, sickos are out there committing unreviewed code.
[266.18 → 269.28] And when that happens, linters won't save you.
[269.64 → 271.30] You need someone like me.
[271.54 → 272.42] Match call!
[273.50 → 274.80] Feature-free, scumbag.
[274.98 → 276.20] Who are you calling scumbag?
[276.38 → 278.02] What's this slop you're trying to push?
[278.30 → 279.34] Unnecessary comments?
[279.78 → 280.76] Global state?
[281.24 → 282.24] Nested ternaries?
[282.24 → 283.62] Oh, my bad.
[283.78 → 285.14] I didn't even read the code yet.
[285.36 → 286.28] You disgust me.
[286.50 → 287.54] Step away from the keyboard.
[287.62 → 288.52] Just let me explain.
[288.94 → 289.56] Is that a mouse?
[289.82 → 290.78] He's a merchant of prod!
[291.08 → 292.70] You have the right to remain silent.
[292.90 → 295.50] Anything you push to GitHub can and will be used against you.
[295.56 → 296.86] You have the right to a debugger.
[297.18 → 300.56] But if you cannot afford one, a public stack trace will be made available to you.
[302.18 → 305.64] And one more code criminal off the streets and where they belong.
[306.30 → 306.62] HR.
[309.62 → 311.82] Look, I didn't yet...
[311.82 → 316.20] I know I didn't review any of the code, but I was going to have CodeRabbit review it from the start.
[316.54 → 319.74] With one-click fixes and style enforcement, I don't need Merge Cop.
[320.40 → 325.42] I would never merge unreviewed code, but a first pass with CodeRabbit always makes things go faster.
[325.66 → 328.12] Actually, you can try it too at coderabbit.ai.
[329.56 → 331.44] Next week on Merge Cop.
[331.60 → 334.56] The differ's out there, and I'm going to be the one to deprecate him.
[334.56 → 349.80] So, to kind of wrap it all up, so everybody understands how Phil C works, the runtime impact of Phil C is going to be somewhere between 1.2 to 4x is what I have seen.
[349.94 → 353.38] And then you will see comments on the internet that say something along the lines of,
[353.38 → 355.36] What's 20% these days?
[355.36 → 362.60] Nobody cares if you lose 20% performance, which I know that Casey will probably lose some sort of sleep or hair over with that kind of comments on the internet.
[363.10 → 368.00] Wait, how do we get from 1 to 4x and go from that to 20%?
[368.48 → 370.76] Well, because 1.2 would be, you know, 20%.
[370.76 → 378.84] Oh, you mean if you just took the minimum as assuming that you were going to get the minimum for some reason without evidence.
[379.00 → 379.66] Okay, sure.
[379.82 → 382.00] There is another performance penalty.
[382.36 → 384.28] Can we talk about that really quickly as well?
[384.28 → 384.46] Yeah, yeah.
[384.48 → 385.46] What's the other performance penalty?
[385.86 → 390.66] I just have to, I'm going to be a little bit on the rust side today, so I came prepared.
[391.88 → 392.14] Oh, no.
[394.12 → 394.56] Perfect.
[395.32 → 395.48] Okay.
[396.34 → 398.86] Hey, guys, it's Rusty checking in today.
[398.86 → 398.90] Okay.
[399.60 → 411.64] The other problem is that there's a serious memory additional performance constraint here in the sense that it's going to allocate a lot more memory for lots of different kinds of programs.
[411.84 → 413.86] So I just wanted to make sure that that's clear.
[414.20 → 416.04] It's not a zero-cost abstraction.
[416.46 → 417.70] Okay, it's not a zero-cost.
[417.84 → 419.12] So, Prime, you may continue.
[420.32 → 421.66] Actually, Ten is very, very correct.
[421.76 → 423.64] It is not, in fact, a zero-cost abstraction.
[423.64 → 431.24] Anyway, so I just wanted to talk about this because the thing that really sparked all of this was that Pseudo RS is kind of this new brand of pseudo.
[431.38 → 436.98] It's the new pseudo on the block, and Ubuntu is saying, hey, we're using it, but all the comments are like, why?
[437.42 → 438.38] What's, why are you doing?
[438.46 → 445.96] Like, it seems to be a at least it appears, I don't know if it's actually true in real life, but in Twitter life, it appears to be a largely negative experience.
[445.96 → 450.70] And so with that in mind, some people are saying, well, why don't you just use Phil C?
[450.78 → 459.26] The performance of pseudo is negligible, and you can get 90% of the safety without having to deal with Rust and a rewrite and rediscovering all the bugs.
[459.62 → 464.62] And so that's why we have with us Casey and low-level learning.
[464.74 → 465.94] TJ is just here for fun.
[465.94 → 478.00] And so, I think it'd be fun to start probably with the security side, just because I think that that is probably the most poignant or at least the most reasonable place to start when it comes to a memory-safe C.
[478.86 → 485.20] Ed, if you'd like to kick off any talks about that, I have a lot of questions about it, but any initial statements?
[485.94 → 489.64] Yeah, I mean, so I guess to kind of kick this conversation off, right, what is spawning this?
[489.64 → 501.92] If you guys aren't aware, pseudo, you know, well-known, well-loved program that tends to be the target of a lot of vulnerability research because it is one of the most widely available, widely used set UID binaries, right?
[501.94 → 505.62] It's a binary that runs as root, and you use it to run things either as root or somebody else.
[506.34 → 511.76] And so a memory corruption vulnerability in pseudo obviously violates a pretty hefty, pretty scary security boundary.
[512.20 → 518.42] And so as a result, there's a push to rewrite a lot of bin utils, one of them being pseudo, in Rust, right?
[518.42 → 519.58] Kind of cool idea.
[520.12 → 527.90] This also, for some reason, kicked off an effort to, like, rewrite all the core utils in Rust to include, like, echo, cat, SED, which is a whole other conversation.
[528.72 → 538.56] But unfortunately, despite it being written in Rust, shocking, I know, I think there were two CVEs that came out recently in the RS implementation of pseudo.
[539.08 → 540.68] So it kind of begs this bigger question.
[540.80 → 543.66] And I think, you know, we've talked about this in the previous episode that I was on with Casey.
[543.66 → 548.78] You know, all because you write it in Rust doesn't mean that you're going to get the exact same behaviour.
[549.28 → 555.42] And if you can't confirm via some set of testing that you have, you know, not regressed at all in your functionality,
[555.72 → 559.64] then you're potentially introducing new vulnerabilities to the code through logic errors.
[559.74 → 561.78] And that's, I think, exactly what we saw with pseudo RS.
[561.78 → 568.42] So instead of rewriting everything in Newland, and I'm sure we're going to iterate on Newland every 20 years,
[568.86 → 579.50] why not drop in a new compiler that has sanitizers, that has intermediate representation checks to put in on an arbitrary pointer the vector size, right?
[579.52 → 580.36] And that's what Phil C does.
[580.42 → 581.76] And I have not used Phil C personally.
[581.86 → 583.96] I'm kind of curious, Prime, how it went for you.
[584.02 → 586.44] But overall, I think Phil C is a great idea.
[586.44 → 588.60] There are some combat issues.
[588.72 → 594.44] You have to be compatible with the LLVM tool chain to make it work, which is kind of an issue for some pieces of software.
[594.54 → 595.60] But generally, great idea.
[595.72 → 596.44] I love the concept.
[596.70 → 598.14] So that's kind of my first take.
[598.88 → 599.34] Casey, what about you?
[600.68 → 602.00] I'm on the same page.
[602.46 → 606.44] Essentially, like, rewriting something in Rust, to me, is usually a pretty bad idea.
[606.44 → 615.84] Because the problem is that your really Rust can only guarantee you a couple security things that it's specifically designed to do.
[616.02 → 620.22] But all the other ways you can have bugs are still there.
[620.22 → 627.60] So it doesn't really handle all of, like, your logic errors or things like that that could result in your program doing something potentially catastrophic,
[627.80 → 630.46] especially in the case of, like, a core utility like pseudo.
[630.46 → 635.26] And so really, like, I would never have, like, I would be like, don't do that.
[635.46 → 640.90] Like, we know that there are memory, you know, safety problems in the languages these were written in,
[640.94 → 643.08] but they've been kind of beaten out over the years.
[643.38 → 645.34] And we can keep looking for them and so on.
[646.20 → 650.36] And so rewriting something in Rust like that is just very dangerous and, I think, ill-advised.
[650.36 → 653.88] So something like Phil C is kind of a very nice middle ground, I would say,
[653.96 → 660.38] which is that, like, hey, we can preserve the logic integrity of this thing that has now been battle-tested
[660.38 → 665.18] so that we're pretty sure that we've found a lot of the logic errors that I'm sure were in there originally
[665.18 → 668.16] that we've now kind of gotten out over the years as people found them.
[668.58 → 674.46] But now you can also get this added layer of memory checking just to make sure that memory things we haven't found yet,
[674.74 → 676.36] maybe this will protect against those.
[676.36 → 681.60] And then you're really just down to, like, okay, are there bugs in Phil C itself, right?
[681.90 → 684.24] And, you know, maybe those take a little while to sums out, too.
[684.30 → 689.90] Like, maybe there are some edge cases that, you know, will be found.
[690.48 → 695.00] But until then, it's like that seems like a much better – that would be true of Rust as well, right?
[695.00 → 696.88] Like, there's no difference between Rust and Phil C in that sense.
[696.90 → 699.00] You can always have bugs in the implementation of the memory safety.
[699.60 → 702.48] So it really does seem like a much more sensible approach
[702.48 → 708.56] if you're just talking about our goal here is to make sure that we're providing the safest possible version of something like Pseudo.
[710.22 → 710.58] Yeah.
[711.42 → 715.34] Okay, so, I mean, those are all kinds of, like, they feel like intellectual arguments
[715.34 → 717.34] more than actual, like, practical arguments.
[717.42 → 723.36] Do you think there's an actual practical argument to saying that Phil C is going to be something that is, like, fully usable?
[723.36 → 729.88] Like, Casey, could you use Phil C in a game, or would you even ever consider using something like Phil C in a game engine slash game?
[730.72 → 736.38] Well, I mean, you'd have to have some reason why you felt like what it's offering you is important.
[736.38 → 742.22] So, you know, there are some ways in which you could imagine this being important.
[742.22 → 754.76] For example, if you have a lot of user-generated content in a game where potential bad actors might be trying to use that ability to upload content
[754.76 → 758.96] to create sort of security exploits, right?
[759.50 → 762.94] You can imagine something like Roblox or Fortnite or whatever,
[762.94 → 771.22] where they're kind of constantly trying to increase the amount to which their users can contribute new games, new modes of play, whatever.
[772.22 → 781.42] You could imagine something like that where there are cases where you're very scared about things like memory protection and stuff like that.
[781.78 → 787.94] And so I could see maybe some arguments in certain specific scenarios where you're like, we really need this,
[787.98 → 791.56] so we're going to take this isolated part of the engine, and maybe we will use something like Phil C.
[791.72 → 794.24] We'll accept the performance hit, but we just really need this.
[794.38 → 796.32] We need all the security we can get.
[796.32 → 803.00] But for the majority where you're talking about just running a game in an isolated context on someone's machine,
[803.36 → 806.64] it's unclear what you really need this for, right?
[806.72 → 809.32] For the average game development, it's not really...
[809.92 → 810.32] And I don't...
[811.40 → 814.62] I mean, the person who created Phil C works at Epic, right?
[814.70 → 816.36] They are working on...
[816.36 → 820.96] I think they work on Verse, the Epic's Fortnite programming language thing.
[820.96 → 827.42] And so, like, you know, I would imagine most of, like, an Unreal Engine or something like that
[827.42 → 833.00] wouldn't really adopt something like Phil C, but you could see some specific cases where that might be important.
[833.14 → 838.90] And for example, Verse, which is their language, that would be a case where he probably is employing some of these techniques there.
[838.96 → 841.44] I don't have any inside knowledge of that, and I don't work on that.
[841.44 → 846.34] But so that would be my take on it, is that you'd have to be in an area where you really cared about it,
[846.36 → 849.30] because otherwise I'm not really sure what you would need it for.
[849.58 → 850.24] Does that make sense?
[852.34 → 852.70] Yes.
[853.08 → 854.64] I think that does make sense.
[855.64 → 860.44] I mean, where my big misunderstanding probably just comes from is that I don't understand...
[861.34 → 864.96] I was trying to read some of the things with the differences between, like, SAN and UB SAN,
[864.96 → 869.74] and how Phil C actually can circumvent some of those problems.
[870.20 → 875.00] But at the end of the day, TJ brought up perfect points, because he's being the resident Rust dev.
[875.40 → 879.56] There are things that Phil C just can't do, and they even shouted out, which is, like, file handles.
[880.36 → 885.34] They are something that can't be represented in the same kind of context.
[886.22 → 887.94] Well, here, I'll give the example.
[888.86 → 892.38] First off, that's probably the longest a Rust user has ever gone without speaking,
[892.38 → 898.50] so I just would like that to go into the record as a moment for allowing other people to speak.
[899.08 → 902.10] I do have Rust running in production right now,
[902.22 → 906.22] so that is something that also most Rust users have never done.
[906.34 → 910.56] So I would put myself ahead of almost every Rust user in the entire world.
[910.56 → 911.98] Hey, same guy. Listen.
[912.06 → 912.24] Yeah.
[912.46 → 917.84] So just throwing it out there as two things that make me very qualified to talk about this.
[918.22 → 918.84] But I do want to...
[918.84 → 920.22] I need to say one thing, though.
[920.22 → 928.42] You also did the 0 to I use Rust, by the way, at the same standard rate as any Rust dev who starts speaking.
[928.58 → 932.54] Within the first, like, five seconds, you mentioned the fact that you used Rust.
[932.76 → 933.16] By the way.
[933.72 → 934.12] By the way.
[935.46 → 936.24] I don't...
[936.24 → 939.62] I thought I wasn't allowed to run Rust C unless I did that.
[939.96 → 943.20] I still need to run Rust C sometimes, so I don't understand.
[943.20 → 944.30] So, okay, anyway.
[946.76 → 952.16] So this is, on a serious note, instead of Memling about Rust users,
[953.96 → 958.30] this is not a reason that I would rewrite a program.
[958.52 → 959.96] So this is, like, a different class of things.
[960.10 → 965.24] So if we want to start, we can maybe talk more about, like, the rewrite situation first,
[965.24 → 970.66] and then talk about, you know, like, if you were starting off a new project, which one you might want to choose in pros and cons.
[970.72 → 977.64] Because the thing that I think a lot of people are missing, and, Ed, in case you guys both alluded to this at the beginning,
[977.78 → 980.94] maybe I have to take my Rust hat off for this to say something nice about Phil C.
[980.94 → 985.76] is, like, you can't just rewrite everything.
[986.20 → 987.58] It actually doesn't work.
[987.90 → 991.30] Like, we don't have enough time or resources or a bunch of other things.
[991.36 → 997.46] Even just, like, if you think you can bug for bug, remake it exactly right, and handle every case,
[997.66 → 1000.20] it's just not realistic to make that happen.
[1000.20 → 1001.70] Like, even...
[1001.70 → 1007.68] Like, I think probably I could run Neovim, you know, at, like...
[1007.68 → 1012.24] Even at Phil C's current worst case, 4x, slower.
[1012.58 → 1014.80] And Neovim would still feel fast and good.
[1015.36 → 1015.78] For me.
[1015.94 → 1016.42] Right, you know what I'm saying?
[1016.48 → 1018.32] Like, even if it was four times slower.
[1018.68 → 1024.66] And that's assuming, and I see as well, we've got Pizzicato in the chat, who is the creator of Phil C, by the way.
[1025.04 → 1029.68] Like, Phil C is gonna, I think, get faster than what it is right now,
[1029.76 → 1033.96] as tends to happen for people who actually care about software and making excellent things.
[1033.96 → 1043.18] So it's like, I could run Neovim, and then I would not be able to be exploited by certain cases of memory safety bugs, right?
[1043.22 → 1045.86] Because I'm sometimes running slightly untrusted things in Neovim.
[1045.94 → 1047.10] I'm running someone else's code.
[1047.44 → 1050.20] Running, like, via a plugin, or other things like that.
[1050.54 → 1055.22] So, it's not realistic to just say, like, Neovim, just rewrite in Rust.
[1055.86 → 1058.42] That's, just do it, it'll be easy.
[1058.72 → 1060.34] That's insane behaviour.
[1060.72 → 1062.76] That's a that's a not realistic scenario.
[1062.76 → 1067.80] So that's the thing, for some reason, I feel like a bunch of Rust people are just, like, talking past it, of, like,
[1068.56 → 1070.76] you could just have a safer world today.
[1071.12 → 1073.90] In fact, Graydon Hor, creator of Rust, said,
[1074.18 → 1077.66] more memory safe programs is better for all of humanity, right?
[1077.72 → 1078.88] In talking about Phil C.
[1079.28 → 1080.04] So, anyway.
[1080.88 → 1080.98] Yeah.
[1081.32 → 1085.42] This may kind of be jumping backwards in the conversation a little bit there, but,
[1086.08 → 1090.04] Prime, I kind of heard you, I think, sort of raise the question.
[1090.04 → 1096.30] You said, like, I have questions about, like, what's the difference between, like, address sanitizer and using something like Phil C, right?
[1096.58 → 1096.80] Yeah.
[1096.82 → 1100.60] And I thought maybe that might be something that's worth, like, talking about a little bit.
[1101.14 → 1101.44] Yes.
[1101.60 → 1101.76] Yes.
[1102.08 → 1104.46] Because I've SAN'd a few times in my life.
[1104.54 → 1106.00] I'm no, I'm no SAN expert.
[1106.58 → 1114.88] And so I just know that it's caught, I've done silly things with standard vector in the old C++ world where they're just like, yo, you're doing stupid things.
[1114.88 → 1116.10] And I was like, oh, that is a stupid thing.
[1116.16 → 1117.28] Like, I just didn't know what I was doing.
[1117.98 → 1118.30] Right.
[1118.44 → 1132.20] So, just to be clear, the idea behind things like Phil C, and also, there's, like, kind of broader security idea here, actually, than just Phil C,
[1132.20 → 1144.14] which is that ARM chips, like, or the ARM specification, I should say, and certain vendors supply actual hardware support for the kinds of things that Phil C does.
[1144.22 → 1150.22] It's not exactly the same as Phil C does things beyond what this hardware would be doing for you.
[1150.36 → 1151.48] And we can talk about that a little bit.
[1151.48 → 1159.88] Like, X64 spec also has now introduced this, although I guess I haven't really followed closely enough whether anyone's shipped any of it yet.
[1159.96 → 1161.86] But, like, there is a specification for it.
[1161.92 → 1162.14] Right.
[1162.42 → 1168.10] And so I'm assuming that, like, Eons and, you know, Epic processors down the line will have this for servers or something.
[1168.22 → 1168.30] Right.
[1168.56 → 1170.42] I haven't followed out the update.
[1171.54 → 1176.44] But Apple M-series chips now, for example, do implement this ARM, this particular ARM extension.
[1176.44 → 1187.04] Anyway, these things are not designed to analyze your program when you're developing it and tell you whether they found security vulnerabilities.
[1187.48 → 1194.62] They're designed to actually just stop the program any time it's running when it would have done something bad.
[1194.62 → 1212.58] So the idea here is to make sure that something that address sanitizer maybe wouldn't catch because when you were running the program, you never exercised the code path that happens to do this thing or whatever else, you know, like the static analysis part can't catch things or, you know, whatever you were using.
[1213.40 → 1220.58] This is designed to basically say, look, the actual runtime model of this thing literally can't do these bugs.
[1220.58 → 1224.28] When they would have happened, the program simply halts.
[1224.62 → 1233.44] It's basically just a thing that says when you would have written to a piece of memory that was actually a different piece than this pointer was supposed to ever be able to write to, we just stop.
[1233.56 → 1235.60] The program faults and it closes.
[1235.72 → 1235.98] Yeah.
[1235.98 → 1240.56] And so again, it doesn't really prevent the bug in the sense of the program working.
[1240.64 → 1241.96] The program still doesn't work.
[1242.14 → 1246.78] What it does is it stops it from turning into anything other than basically a denial-of-service attack.
[1246.84 → 1247.10] Right.
[1247.68 → 1250.64] So does that make just light sense just to start with?
[1250.90 → 1251.16] Yeah.
[1251.16 → 1251.36] Yeah.
[1251.36 → 1251.56] Yeah.
[1251.56 → 1251.80] Yeah.
[1251.80 → 1251.98] Yeah.
[1251.98 → 1254.06] There's a lot of talk in chat right now about, about ASIN.
[1254.06 → 1264.06] We should probably highlight like ASIN, for example, is not meant to be an exploit mitigation in the sense that you use ASIN to block hackers.
[1264.06 → 1264.38] Right.
[1264.38 → 1274.52] Because all ASIN does is put a predictable pattern as a shadow region and a memory space so that when that is corrupted, it's like, hey, it's not the same.
[1274.58 → 1275.46] You probably should fix this.
[1275.58 → 1278.02] But the pattern that it puts is probably is deterministic.
[1278.02 → 1278.42] Right.
[1278.50 → 1286.40] So like an attacker could just put the Fas in the right spot and, you know, that would not trigger ASIN while still violating memory safety.
[1286.50 → 1296.24] So ASIN is more like a tool that you compile your code with to make it as fall over as fast as possible to put it in your fuzzing rig in CI.
[1296.50 → 1296.66] Right.
[1296.66 → 1300.64] So that in two weeks when your fuzzing is done, it hopefully has crashed at some point if there's a bug.
[1301.16 → 1319.88] Contrary to, you know, Casey's like the Phil C thing, which is lets instead of having ASIN just kill it, let's put in like intermediate representation logic within LLVM that says like, hey, we're going to assign lengths and things to see arrays such that you are not allowed to program in memory or memory on safety.
[1319.88 → 1326.44] So it's kind of two different schools of thought on like sanitization versus runtime, if that makes sense.
[1327.08 → 1343.82] And for people who don't know, because like a lot of people probably haven't written like systems level code, like maybe, Ed, you can just give a really brief, brief overview of like how that memory on safety leads to bad things happening on someone's computer.
[1343.92 → 1347.96] Because I feel like a lot of people, they just literally don't even know what's going on there.
[1348.18 → 1348.98] Yeah, 100%.
[1348.98 → 1354.12] I mean, so like the crux of every memory exploit boils down to this pattern.
[1354.30 → 1354.52] Okay.
[1354.88 → 1361.06] Let's take an array, and we want to index into that array using the index i.
[1361.24 → 1361.62] Right.
[1361.80 → 1362.02] Okay.
[1362.34 → 1369.80] Now let's, instead of that I being a number that we program into our code statically, we read I off of the network.
[1369.80 → 1377.66] And we're using some type length value network protocol where we have like the type of field, the length of a field, and then the number of, or the length of the field and the data.
[1377.92 → 1378.04] Right.
[1378.04 → 1378.08] Right.
[1379.68 → 1385.42] Most of the time, it just happens that oops, the developer forgot to validate that I is within the scope of that array.
[1385.82 → 1387.86] And so you get an arbitrary read, arbitrary write.
[1387.96 → 1392.16] And that ability to arbitrarily read and write data gives you SLR bypass.
[1392.46 → 1393.74] It gives you stack canary bypass.
[1393.96 → 1395.90] It gives you the ability to overwrite relocatable.
[1395.90 → 1398.06] So you can redirect program control to somewhere else.
[1398.16 → 1402.68] And that, like, that is the crux of almost 80% of memory corruption bugs.
[1402.72 → 1402.80] Right.
[1402.82 → 1403.90] There are some other ones that are a little more weird.
[1403.90 → 1415.78] So if you literally just create proper bounds in a language that is memory unsafe that disallow a user to write outside their confines, that solves the problem.
[1416.00 → 1417.60] And so Phil C, again, I haven't used it.
[1417.66 → 1419.08] I haven't explored too much into it.
[1419.08 → 1425.16] What I understand is that Phil C uses LLVM IR to say, like, oh, you've made an array that is 64 bytes.
[1425.32 → 1430.56] I'm going to put, you basically turn all arrays into vectors, and then do runtime checks on the vector before you do writes.
[1430.64 → 1432.74] And, like, oh, if you violate that, you can't continue.
[1432.74 → 1436.12] And so that stops most bug classes.
[1436.24 → 1436.96] I think Casey was talking.
[1437.58 → 1440.14] It's a little, it's more hardcore than that.
[1440.30 → 1450.18] Like, Phil C is, like, kind of, like, if you actually, if you're someone who is 100%, you know, at the Rust party ladling out the Rust Kool-Aid.
[1450.52 → 1450.72] Yeah.
[1450.92 → 1455.26] Into the little Rust cups that you hand out and go, like, let's do this, let's drink this, guys.
[1455.82 → 1459.46] Then you should love Phil C because it takes it way more seriously, even.
[1459.46 → 1470.58] So, essentially, the way that Phil C is designed to work is it's a lot like the hardware extensions, only instead of trying to be relatively transparent, it's saying, look, we're going to incur a cost.
[1471.40 → 1477.68] And so what it actually does is it tracks, essentially, all allocated objects of any kind.
[1477.68 → 1491.40] So anytime you actually do any kind of allocation, it's going to say, all right, I'm going to track that in using, I mean, what you would call, like, memory outside the addressable space of your language.
[1491.40 → 1500.52] Meaning, inside what, you know, doing what you're able to do inside a Phil C program, you cannot access the tracking data, if that makes sense.
[1500.52 → 1500.96] Right.
[1502.18 → 1511.00] And so that tracking data will then be used any time you're trying to work with one of these pointers, you know, like a regular C pointer.
[1511.26 → 1514.80] To you, it looks like you're working with the pointer normally, like you wouldn't see.
[1514.80 → 1525.58] But actually, Phil C is going to look to make sure that that pointer originated from the actual part of memory that you are accessing.
[1525.94 → 1526.08] Right.
[1526.22 → 1536.64] So it tracks not just are you in bounds, meaning not just are you within the particular object that you sort of claimed you were accessing.
[1536.94 → 1539.94] But are you in the one that this pointer originally came from?
[1539.94 → 1544.28] And this works even if you like to read and write pointers to like blind memory and stuff like this.
[1544.34 → 1544.52] Right.
[1545.36 → 1551.56] Because they're because essentially what Phil C is doing is it's using sort of almost like a pseudo pointer.
[1551.56 → 1555.74] It's using a 64 bit value that you don't directly use.
[1555.88 → 1565.52] You indirectly use it by looking at sort of that that backing, that tracking information to make sure that you're tagged, that you like match what you're trying to access.
[1565.52 → 1571.38] And so when they do this in hardware, it's a sort of weaker version of this.
[1571.78 → 1579.86] What they do is for pointers in the hardware versions of this, they just use the top bits of the pointer that wouldn't be used because you don't have that much memory.
[1579.96 → 1582.04] You know, you don't have 64 bits worth of memory in a machine.
[1582.04 → 1590.52] They use the top bits to assign, say, like a four bit tag, you know, a value between one and 15, let's say, and zero is usually reserved, that sort of stuff.
[1591.66 → 1593.14] They'll use that tag.
[1593.46 → 1605.04] And then every block of memory that you sort of allocate or rather that you mark, you can say like this region of memory, you can mark regions of memory with tags, whatever you want, some random tag that you associate.
[1605.04 → 1626.84] Every time you use a pointer to access some memory, it checks to see whether the tags match so that even if two blocks of memory are right next to each other, if you go from one to the other by incrementing the pointer, like low level was saying, if you go outside of like an array bound, the tags hopefully won't match because hopefully any two neighbouring regions got different tags.
[1627.18 → 1627.30] Right.
[1627.80 → 1632.22] But that's really like there's some other things that you can use that these extensions do.
[1632.32 → 1634.06] But, you know, for the most part, it's doing that sort of thing.
[1634.06 → 1637.50] And Phil C is just sort of like the on steroids version of that.
[1637.62 → 1637.72] Right.
[1637.82 → 1645.20] This it tracks everything about these so that you can't even have accidental conflicts of the tags, not just using some simple like four bit scheme.
[1645.36 → 1657.98] And it also does like more aggressive use after free tracking and all this other sorts of stuff by using garbage collection to like never remove those things so that it remembers like each region until it's actually not accessible by anyone anymore and so on.
[1658.10 → 1663.74] So hopefully that's just a little bit like that's like so it's a much more complete system than something like address sanitizer.
[1663.74 → 1664.54] Or if that makes sense.
[1664.64 → 1665.58] So I don't know.
[1665.58 → 1666.70] That's a lot of stuff in there.
[1666.70 → 1667.18] But yeah.
[1667.18 → 1676.14] Is it effectively turning all memory accesses into like a virtual pointer where like, yeah, it's like a look-up into another object table.
[1676.38 → 1676.92] And then it does.
[1677.56 → 1680.08] I mean, it's that's probably not.
[1680.32 → 1682.30] That's probably it sounds a little bit more.
[1682.30 → 1685.50] That might be a slightly more aggressive way to say it.
[1685.58 → 1690.76] You can think of it more like there's almost like a shadow version of thing.
[1690.94 → 1691.24] Yeah.
[1691.36 → 1692.24] You should go take a look.
[1692.32 → 1693.24] They have a very nice page.
[1693.24 → 1693.86] I wish I had done a little more.
[1694.16 → 1694.26] Yeah.
[1694.88 → 1697.06] I'll show you, but I have to power up first.
[1697.46 → 1698.50] Oh, Jesus Christ.
[1698.70 → 1699.68] Where do you have all these women from?
[1699.82 → 1700.08] Why?
[1700.46 → 1700.76] Why?
[1702.76 → 1703.12] Okay.
[1703.30 → 1703.88] That's pretty good.
[1704.00 → 1706.30] Now I'm super scion mode because we have a whiteboard.
[1706.48 → 1706.52] Okay.
[1706.58 → 1707.58] Super Saipan Rust user.
[1707.68 → 1708.08] I like it.
[1708.08 → 1708.34] Yeah.
[1708.70 → 1708.98] Okay.
[1709.42 → 1713.14] So in this case, right, we have like pointer X.
[1713.28 → 1715.00] It's pointing to 40, right?
[1715.06 → 1716.20] Y, 4, 4, right?
[1716.50 → 1719.52] You can imagine in memory, we've got these two pointers, right?
[1720.24 → 1723.20] What happens in normal C when you access like X5?
[1724.90 → 1725.30] Yeah.
[1725.30 → 1728.06] You just get zero or whatever, whatever, like the next element is.
[1728.16 → 1728.18] Yeah.
[1728.20 → 1728.94] We get over here.
[1729.08 → 1729.26] Yeah.
[1729.38 → 1734.82] But in fill C, it says, yo, this, if we did like Malik 4 and Malik 4 for both of these,
[1734.86 → 1735.02] right?
[1735.02 → 1740.70] In this case, it's going to say it's got a lower bound, a 4, 0, and an upper bound,
[1740.82 → 1741.44] a 4, 3.
[1741.72 → 1741.92] Yeah.
[1742.04 → 1743.16] And here's where it currently is.
[1743.16 → 1743.80] Well, I understand that.
[1743.86 → 1745.08] I'm more curious about the implementation, right?
[1745.16 → 1747.72] Like in the context of this example, what is X?
[1747.96 → 1751.02] Is X a pointer to a thing or is X able to definitely scatter?
[1751.48 → 1751.64] Yeah.
[1751.64 → 1751.78] Yeah.
[1751.88 → 1754.44] X to you, the user is still just this pointer.
[1754.70 → 1755.00] Interesting.
[1755.10 → 1759.76] But if this is, I'm assuming this is what, this is what I'm going to, I'm, maybe we can
[1759.76 → 1760.28] get confirmation.
[1760.28 → 1765.42] As far as I could tell from reading and everything else, it gives you back exactly this.
[1765.52 → 1766.78] This is what you think you've got.
[1766.96 → 1768.48] I think it's wider.
[1768.94 → 1770.64] So I don't think that's how it works.
[1770.84 → 1772.50] It's 16 bytes wide though, right?
[1773.02 → 1774.38] No, no, no, no, no.
[1774.42 → 1775.42] It's the same size.
[1775.54 → 1776.26] It's 64 bits.
[1776.68 → 1777.26] Oh, it is.
[1777.36 → 1777.56] Okay.
[1777.66 → 1778.48] It's the same size.
[1778.82 → 1780.32] I don't use fill C.
[1780.32 → 1784.98] And the first time I heard about fill C was when you guys said we were doing an episode
[1784.98 → 1785.70] about fill C.
[1786.02 → 1786.24] Nice.
[1786.38 → 1786.58] Okay.
[1786.92 → 1789.04] So I apologize for not knowing more about it.
[1789.14 → 1791.36] If I was a fill C user, I'd be happy to get the full explanation.
[1791.60 → 1795.92] I believe the way that it works is they use a shadow allocation.
[1796.12 → 1801.36] So every time you allocate something, they allocate twice that effectively, right?
[1801.48 → 1801.70] Yes.
[1801.76 → 1802.10] You're right.
[1802.46 → 1802.76] You're right.
[1802.76 → 1807.24] And then they use the so effectively what X is, is it's going into the shadow region,
[1807.24 → 1811.54] which then tells fill C where, like how to get the additional date, right?
[1811.82 → 1812.08] Data.
[1812.70 → 1816.00] In fact, you said the, the, um, the person who wrote it was in chat.
[1816.08 → 1818.34] Is that a correct, would that be a good summary?
[1818.72 → 1820.86] Because I read about this literally yesterday.
[1820.86 → 1821.94] So that's all I know.
[1821.94 → 1825.92] But that I believe was how it was explained in the, uh, in the documentation.
[1827.00 → 1827.44] Yes.
[1827.78 → 1828.02] Yes.
[1828.06 → 1828.68] I think you're right.
[1828.68 → 1828.86] Casey.
[1828.90 → 1829.08] Yes.
[1829.20 → 1829.44] Yeah.
[1829.56 → 1830.34] That was my apologies.
[1830.40 → 1832.10] It doesn't return the wider one.
[1832.18 → 1835.94] It has one somewhere else that it's holding onto that tells you.
[1835.94 → 1837.22] It's called Invisibles, right?
[1837.24 → 1840.92] It has the invisible capability stored off in a region in which you're not allowed to
[1840.92 → 1844.66] access in which the thing returned to you looks just like a pointer, acts like a pointer,
[1844.78 → 1845.42] smells like a pointer.
[1845.52 → 1846.92] And in C, it's just literally a number.
[1847.14 → 1849.90] And then boom, bad bing, it does that runtime checks against it.
[1850.14 → 1850.22] Right.
[1850.24 → 1854.18] And that's why you can still add to it and work with it like you normally would, because
[1854.18 → 1858.84] because they have a shadow region, they can still like figure out like what's going
[1858.84 → 1859.44] on there, right?
[1859.44 → 1860.16] Or things like this.
[1860.24 → 1861.96] And so I don't know the specifics.
[1861.96 → 1865.38] I want to now read more about it because I thought it was really cool when I was reading.
[1865.46 → 1866.74] It's like, oh, this is a really neat thing.
[1867.24 → 1871.16] So I'd like to go read about how they handle all the actual practical details.
[1871.38 → 1874.60] But I didn't immediately find sort of the document of that.
[1874.84 → 1876.88] Like there's perfect overview documents.
[1876.88 → 1878.46] But like, oh, how did you handle this?
[1878.50 → 1879.14] How did you handle that?
[1879.22 → 1881.10] Like that's, I didn't find that immediately.
[1881.24 → 1884.28] So I'd like to go read like, how do you actually use the shadow region?
[1884.40 → 1885.42] Like how is it doing that?
[1885.50 → 1886.42] And all that sort of stuff.
[1886.42 → 1890.96] And also the other important thing that they bring up in this documentation, which I think
[1890.96 → 1896.74] is important to mention as well, is that if like a naive implementation of stuff like
[1896.74 → 1900.92] this would have a lot of problems with threading potentially, because like different people
[1900.92 → 1904.42] can sort of mutate pointers and from, you know, and you can have race conditions, this
[1904.42 → 1904.88] sort of stuff.
[1904.88 → 1910.10] And so Phil sees also, also very careful to make sure that they get those things right,
[1910.18 → 1913.52] which again, like if you look at it, it's like, wow, this sounds very complicated.
[1913.52 → 1917.24] Like why did it have to, you know, why does it have to allocate all this extra memory or
[1917.24 → 1917.94] things like that?
[1917.94 → 1921.88] And the answer is because they were, they were trying to take this really seriously.
[1922.08 → 1927.98] Like not like, oh, we caught some memory bugs, but like, no, we really do provide a secure
[1927.98 → 1932.74] operating model, which is, which again, if you're drinking the rust Kool-Aid, you have
[1932.74 → 1933.30] to respect that.
[1933.40 → 1936.50] This is, this is doing it for real and on existing programs.
[1936.58 → 1937.12] It's pretty great.
[1937.74 → 1938.22] Yes.
[1938.32 → 1939.02] We like that.
[1939.40 → 1941.62] That's the crazy thing for the rust people.
[1941.90 → 1946.44] We, even with my rust super, super crazy here on right now that I don't really get
[1946.44 → 1948.22] is like, this is good.
[1948.32 → 1950.50] This stops this from happening right now.
[1950.50 → 1954.14] If you ran C code, and you did this, it would be, it would be chill.
[1954.94 → 1957.04] You're like, it would let you, it would be chill.
[1957.12 → 1958.54] It would let you just read from memory.
[1958.54 → 1959.96] That's not the thing that you're doing.
[1960.08 → 1960.86] That's bad.
[1960.90 → 1961.66] We don't like that.
[1961.72 → 1963.34] We want computers to work good.
[1963.66 → 1966.74] Like that was the that that's the thing that I don't get.
[1966.82 → 1969.26] I like, so that part's good.
[1969.26 → 1973.78] I, and, uh, and it seems like for some reason, everyone's mad about it and I don't really
[1973.78 → 1974.64] get why they're mad.
[1974.90 → 1975.44] I don't know.
[1975.44 → 1976.96] Maybe it's because it's, because it's good.
[1977.08 → 1978.26] Most people really hate it.
[1978.30 → 1981.52] When you introduce something good, that's not the thing that they were previously telling
[1981.52 → 1982.26] everyone was good.
[1982.26 → 1982.66] Right.
[1982.70 → 1985.92] Like, like they don't like to hear that someone else made something good.
[1985.92 → 1988.10] That might be a reason not to use their good thing.
[1988.22 → 1988.86] That's true.
[1989.28 → 1989.46] True.
[1989.46 → 1989.70] Right.
[1989.70 → 1990.88] Like, like heaven forbid.
[1991.08 → 1991.38] Right.
[1991.48 → 1997.38] Uh, but yeah, there's, I do have one question about Phil C, uh, that I, I wasn't able to answer
[1997.38 → 2001.44] directly from my sort of, uh, like five second read.
[2001.44 → 2006.44] So again, like, it'd be nice to meet, maybe, uh, if, if, if the author is in chat, maybe
[2006.44 → 2010.34] they can come on sometime and tell us so that they, so that people can have a more accurate
[2010.34 → 2011.74] description of what it's actually doing.
[2011.74 → 2012.76] Because that would be really nice.
[2012.76 → 2015.26] And obviously they would not get it wrong because they wrote it.
[2015.62 → 2022.12] Um, but what I was going to say is I don't really know how this works with things like,
[2022.12 → 2024.30] uh, okay.
[2024.30 → 2030.54] I create a block of memory that I'm going to sub allocate out of, and I wasn't sure like
[2030.54 → 2032.84] what it does for that.
[2032.84 → 2034.86] Like, that's what one thing looks like on my list.
[2034.92 → 2037.28] Now I'd like to go read about like how it deals with that.
[2037.28 → 2042.44] Um, and like, like, are there, is that just disallowed?
[2042.44 → 2043.28] Is it allowed?
[2043.88 → 2046.12] Um, and we just say, oh, well, it doesn't catch the problem.
[2046.34 → 2046.78] Capabilities right now.
[2047.14 → 2047.40] What?
[2047.70 → 2049.64] No sub capabilities right now.
[2049.82 → 2053.06] I assume that's because if you take a pointer from that region, you technically have a lower
[2053.06 → 2057.00] bound of the original lower and the upper bound of the, of the big upper.
[2057.26 → 2057.34] So.
[2057.84 → 2061.68] And so I was, and so like, that's a thing that makes it kind of hard to port a lot of existing
[2061.68 → 2062.14] programs.
[2062.14 → 2063.42] Cause a lot of them will do that.
[2063.42 → 2063.70] Right.
[2063.70 → 2067.48] And so then it's kind of like, okay, those programs kind of have to be rewritten to,
[2068.62 → 2072.70] uh, like maybe there's some way that, you know, Phil C could be extended to support that.
[2072.70 → 2074.96] Like, Hey, allow us to sort of write a section.
[2074.96 → 2079.56] That's like, here's the here's how the memory marking is going to work inside our thing.
[2079.56 → 2080.02] I don't know.
[2080.02 → 2084.26] But like that would, that would make it challenging to port programs that were written in that
[2084.26 → 2086.38] style, which is a very good style of writing.
[2086.38 → 2087.36] Like it's very efficient.
[2087.52 → 2091.20] And so it's kind of, um, I, I don't know what you do about that.
[2091.20 → 2096.58] If it's, you know, uh, in terms of, I want to use this in some subset and I want to just
[2096.58 → 2097.52] use my existing C code.
[2098.42 → 2103.10] Uh, effectively the creator, uh, PIZ is saying the best thing you can do with your arena allocators
[2103.10 → 2104.96] is to replace them with individual mallows.
[2106.04 → 2106.36] Okay.
[2106.46 → 2107.54] I mean, which is not that hard.
[2107.54 → 2113.52] Cause usually your arena allocations are going through like a pound define kind of a thing
[2113.52 → 2117.24] to like to allow you to switch them for debug and stuff like that anyway, or to mark like
[2117.24 → 2118.10] where they're coming from.
[2118.10 → 2118.92] And it's not that bad.
[2119.00 → 2122.02] And I assume, I guess, let me ask another question while we have the benefit of the author
[2122.02 → 2122.30] in chat.
[2122.66 → 2128.26] So, uh, do you then just like, how do you, cause normally arena freeze are just going to
[2128.26 → 2129.14] free the whole arena.
[2129.58 → 2132.00] So does that just taken care of by the garbage collector?
[2132.84 → 2133.60] Don't call them free.
[2133.70 → 2134.62] Let the GCP deal with it.
[2134.76 → 2135.04] Don't.
[2135.18 → 2135.26] Yeah.
[2135.42 → 2135.74] Then, yeah.
[2136.02 → 2138.42] Then, so that, then that's a not a hard port.
[2138.70 → 2139.02] Yeah.
[2139.10 → 2139.26] Right.
[2139.28 → 2140.78] That's not a that's not a difficult port.
[2140.82 → 2141.90] I don't think for most people.
[2141.90 → 2145.58] Cause like at least for my own code, I always have those running through a macro so you can
[2145.58 → 2147.36] mark them with file in line and debug and stuff like that.
[2147.42 → 2149.40] So that seems pretty, pretty reasonable.
[2150.20 → 2156.56] And, uh, and if you've been following along, we'll link as well, uh, Pizzlenator, your ex
[2156.56 → 2158.74] in the like description of the episode.
[2158.74 → 2165.28] But like Pizzlenator's been working on a bunch of different, like very complicated, very
[2165.28 → 2174.24] real world C programs that are big that you cannot just rewrite to Rust guys.
[2174.68 → 2176.04] You can't do it.
[2176.68 → 2181.36] And talking about like Emacs and Ruby and a few other ones, you can follow along, uh, as
[2181.36 → 2185.46] he's kind of like microblogging, as they say, that's, that's in these days, right?
[2185.46 → 2188.94] And microblogging, I'm on Tumblr, obviously, uh, you can tell from my hair.
[2189.60 → 2195.22] Um, so you can follow along there for a bunch of different ones and see, see, uh, what he's
[2195.22 → 2196.84] been up to and how he's gotten there, which is cool.
[2197.38 → 2197.52] Cool.
[2197.66 → 2197.84] All right.
[2197.96 → 2200.44] TJ, as the resident Rust expert.
[2200.62 → 2200.84] Yes.
[2200.88 → 2201.16] Thank you.
[2201.16 → 2206.52] Um, could you, could you help us understand things that Phil C doesn't do or why?
[2206.58 → 2211.22] Like, why would you like, if you're starting brand new, but you're perfect at C, why
[2211.22 → 2215.58] would you even want to choose Rust if you want to type like, or this level of safety
[2215.58 → 2218.86] and you're like, well, I could just use Phil C, but why would you want to choose Rust?
[2219.46 → 2219.62] Yeah.
[2219.70 → 2221.94] A blue field project, if you will, for me.
[2222.06 → 2222.20] Yes.
[2222.42 → 2222.82] Yes.
[2223.08 → 2225.60] Um, so blue sky project.
[2225.78 → 2226.30] Blue sky.
[2226.46 → 2227.26] A blue sky project.
[2227.54 → 2230.98] If I was starting a new blue sky project today, what would I pick?
[2231.34 → 2231.46] Yeah.
[2231.52 → 2231.92] Uh, okay.
[2231.92 → 2239.64] So one reason you wouldn't use Phil C, you don't enjoy writing C. That's one reason.
[2239.76 → 2240.06] Good answer.
[2240.16 → 2241.00] That's a legit reason.
[2241.12 → 2241.46] Okay.
[2241.66 → 2245.16] There are lots of projects that don't need to be written in C. Okay.
[2245.48 → 2246.08] That's fine.
[2246.18 → 2249.40] In fact, there are lots of projects that don't need to be written in Rust.
[2249.48 → 2251.44] I almost have to take this off when I say this, right?
[2251.78 → 2251.94] Yep.
[2251.98 → 2252.86] It's just true.
[2252.86 → 2253.54] It's just true.
[2253.74 → 2254.58] You lost your blue hair on that one.
[2254.82 → 2254.92] I know.
[2255.14 → 2255.28] I know.
[2255.42 → 2255.68] I get it.
[2256.38 → 2258.28] I think you're going to have to lose the wig, Teen.
[2258.48 → 2259.14] That was.
[2259.58 → 2259.86] Yes.
[2260.26 → 2260.86] You've been.
[2261.16 → 2261.56] Yeah.
[2261.56 → 2265.54] You've, you've been removed from your board seat on the Rust Foundation for that.
[2265.80 → 2266.10] But okay.
[2266.22 → 2266.42] Yes.
[2266.54 → 2271.26] But let's say, let's say you're starting out a new project and the requirements are such
[2271.26 → 2275.34] that Rust makes, or, or some systems language makes a good choice, right?
[2275.42 → 2278.20] So, um, or, or you just have some other requirements.
[2278.20 → 2284.06] The example for me that, uh, that like when I was working at Source graph, we have a very
[2284.06 → 2290.80] straightforward in and out system where we have text come in, and we need syntax highlights
[2290.80 → 2292.12] to come out on the other side.
[2292.52 → 2295.46] It actually matters for that to be really fast.
[2295.58 → 2297.00] You want it to go really fast.
[2297.14 → 2299.30] It's always going to look the same shape.
[2299.54 → 2301.02] You have text come in.
[2301.12 → 2302.06] You'd like to copy it.
[2302.10 → 2302.80] Not so often.
[2303.04 → 2308.22] You're going to run this for like lots of different files and lots of different languages for lots
[2308.22 → 2309.06] of different customers.
[2309.06 → 2312.44] You'd like this to be perfect and really nice and really, really fast.
[2312.52 → 2312.76] Okay.
[2312.88 → 2316.62] You have options for what you could do, right?
[2317.26 → 2321.94] Um, you could write that service in C, I guess, right?
[2321.96 → 2326.74] It's maybe a little bit, it's a little bit harder to picture, but there are like decent,
[2326.74 → 2330.56] like parser generators and other stuff you could use to get you part of the way there.
[2330.58 → 2333.48] And then you could apply some likes and text highlighting from that and all that good stuff.
[2333.48 → 2338.54] But now if you're going to go and do something with Phil C, you're going to experience a slowdown.
[2338.64 → 2343.50] And if you don't do that, you, you know, you're more likely to experience some bad security
[2343.50 → 2348.56] vulnerabilities on a bunch of untrusted input because you're highlighting random people's
[2348.56 → 2349.42] code, right?
[2349.42 → 2353.20] So, oh, they put in a Unicode character that was too wide for your thing and then overflowed
[2353.20 → 2353.56] this buffer.
[2353.64 → 2356.54] And now you access this, it's corrupted memory, and you screwed yourself over too bad.
[2356.58 → 2356.92] So sad.
[2357.12 → 2357.32] Right?
[2357.32 → 2364.50] So, uh, so in, in some cases like this, where you need, you need a lot of speed, you're maybe
[2364.50 → 2366.24] going to work on a lot of untrusted input.
[2366.24 → 2367.58] You're connected to the internet.
[2367.58 → 2368.74] You're doing other stuff like that.
[2369.20 → 2373.74] Um, like, I think there's good reasons why you might want to choose rust, and you'd be able
[2373.74 → 2376.78] to get like faster performance or something like that with rust.
[2376.88 → 2385.14] I mean, also I think, um, you know, from a like technical standpoint, a lot of people appreciate
[2385.14 → 2390.36] the some of the like type system guarantees you can get from rust that Phil C is not going
[2390.36 → 2390.78] to give you.
[2390.96 → 2397.44] You're hopefully now like you won't in, uh, in many cases have like an actual security
[2397.44 → 2398.30] vulnerability.
[2398.30 → 2403.06] You won't have a CVE from these kinds of problems, but it will crash like at runtime,
[2403.22 → 2403.90] which is good.
[2403.90 → 2405.24] That's objectively better.
[2405.62 → 2407.86] Also rust crashes at runtime for things too.
[2407.96 → 2409.70] That's also how it solves some problems.
[2409.82 → 2414.78] So that's not like if rust acts something, access to something outside, and it's unchecked,
[2414.78 → 2416.52] that's just an expect or of panic.
[2416.52 → 2417.66] And then it will crash.
[2417.94 → 2418.34] Sweet.
[2418.44 → 2419.28] That's memory safe.
[2419.38 → 2420.04] We are happy.
[2420.12 → 2420.96] That's actually good.
[2421.58 → 2423.46] Um, but like, there are lots of things.
[2423.46 → 2427.94] The example you had brought up earlier, um, for like file descriptors, right in rust,
[2427.94 → 2433.94] if I open up a file, and I am making my own, you know, like API for it, I'll have the file
[2433.94 → 2439.38] descriptor, uh, like, or I'll have the function, take a callback that callbacks.
[2439.38 → 2445.42] One of the parameters will be a reference to the file descriptor in rust.
[2445.52 → 2451.90] The borrow checker will prevent me at compile time from accessing that outside of the callback,
[2451.96 → 2452.08] right?
[2452.08 → 2455.32] So you couldn't like save the file descriptor to a global and then try and read from it
[2455.32 → 2455.58] later.
[2455.58 → 2457.60] That won't, that like won't work.
[2457.72 → 2458.12] Right.
[2458.60 → 2461.56] Um, and most of the time it's like not clonable and not copyable.
[2461.56 → 2465.32] So you would have to go through like a lot of hoops to try and even get that value out
[2465.32 → 2469.38] in a way you could even literally like just copy it is impossible in rust.
[2469.52 → 2471.62] It's so hard to use the callback pattern in rust.
[2471.84 → 2472.62] It's so freaking true.
[2473.12 → 2473.36] Yes.
[2473.46 → 2475.54] I still haven't figured out streams quite successfully yet.
[2475.94 → 2476.30] Yeah.
[2476.64 → 2479.58] Um, but that would be a thing, right?
[2479.58 → 2485.04] That like, if I try and use this value, this file descriptor outside the callback, the
[2485.04 → 2487.22] type system and the borrow checker, right?
[2487.22 → 2493.26] The linear type system that rust has will block you from being able to do that at compile
[2493.26 → 2495.34] time instead of like runtime.
[2495.98 → 2496.12] Right.
[2497.68 → 2501.30] That's like, for me, I'm a, I'm a type systems guy like types for me.
[2501.30 → 2502.24] That makes me happy.
[2502.24 → 2502.68] Right.
[2502.70 → 2506.30] Like, uh, of course, especially with the blue hair on that makes me really, really happy.
[2506.96 → 2511.56] Um, so that would be something where like, if what you want to do, right, like push left,
[2511.56 → 2514.86] we're going to push the errors to happen earlier along in the dev cycle.
[2514.86 → 2516.60] We're going to experience those at the compiler.
[2517.18 → 2522.50] And there's no like a hundred thousand lines of battle tested code that has a bunch of stuff.
[2522.50 → 2525.24] You might choose rust over like Phil C.
[2525.62 → 2525.82] Right.
[2526.16 → 2531.32] Um, and then you like, and that would be, I think a reasonable choice, but for me, that's,
[2531.62 → 2535.28] everyone seems to be talking past each other about that on the internet, which is surprising.
[2535.28 → 2537.44] Can I, can I ask a clarifying question there?
[2537.48 → 2539.10] I'm not sure I 100% followed that.
[2539.34 → 2545.48] First, I would also say that the phrase push left strongly like sort of suggests a left
[2545.48 → 2549.86] to right leading language, reading language, because that's the order you're going in.
[2549.86 → 2554.00] So I think you lose the blue hair on that one as well, but true.
[2554.84 → 2557.72] Uh, you should say more towards the beginning of a sentence.
[2557.82 → 2559.46] Push is the correct way to say that.
[2559.76 → 2560.14] Yeah, exactly.
[2560.26 → 2564.88] Uh, what I would say is what is the bug you're trying to prevent with this file handle scenario?
[2564.88 → 2569.68] Just so I understand what you mean by rust preventing this better than like, if you,
[2569.76 → 2572.28] if you have some function, right.
[2572.28 → 2577.02] That like opens up and then closes a file handle for you and says like, Hey, or a file descriptor,
[2577.02 → 2580.56] right. Or any kind of this thing, database connection, any kind of thing where you have
[2580.56 → 2581.66] like a handle, right?
[2581.76 → 2587.56] Uh, if you're writing this and like, this is not true of just C, but this would be like
[2587.56 → 2588.78] in Python or something too.
[2588.84 → 2593.58] You could just like save that handle inside your callback to some global value.
[2593.58 → 2594.80] It can escape its region.
[2595.38 → 2595.78] Right.
[2595.78 → 2602.14] So if you like to do with open file descriptor in Python, and then inside there, you like
[2602.14 → 2607.02] save the file descriptor and later in your program, after that original thing's already
[2607.02 → 2609.02] closed it, you're outside that region.
[2609.02 → 2610.80] Now you try and read from it again.
[2610.86 → 2611.56] It'll be an error.
[2611.66 → 2612.56] It will crash.
[2612.70 → 2613.14] Right.
[2613.72 → 2618.16] Cause that's pretty easy to implement in, in C or C plus as well.
[2618.16 → 2618.40] Right.
[2618.42 → 2619.76] Like especially C plus.
[2619.76 → 2622.34] To do what part?
[2622.84 → 2628.58] Just, you just wrap that, wrap file handles in an in, uh, in an accessor and that will
[2628.58 → 2628.94] just work.
[2628.94 → 2629.10] Right.
[2629.10 → 2631.56] So like, if you wanted that protection in C, you could just get it.
[2631.56 → 2631.82] Right.
[2633.86 → 2637.04] Um, like you don't need a language being defeated as we speak.
[2637.30 → 2639.68] No, I mean, like, I'm not trying to fish on rust.
[2639.68 → 2642.60] I'm just saying, I don't understand why you couldn't just make that same thing by just
[2642.60 → 2646.56] making sure that instead of using like an INT as your file descriptor, you actually use
[2646.56 → 2650.42] a struct that does something, you know, or, or, you know, a C plus class for
[2650.42 → 2651.70] option-oriented programmers, right?
[2651.74 → 2652.00] Whatever.
[2652.44 → 2657.42] But, but I'm saying like, sort of regardless of that, I think, I think we're not, we're
[2657.42 → 2658.44] not talking about the same thing.
[2658.46 → 2664.66] I'm saying like, we could prevent in like rust from the with the borrow checker, you can
[2664.66 → 2667.18] prevent the value from escaping its region.
[2667.84 → 2668.24] Right.
[2668.40 → 2673.98] Which I don't, which I, maybe there is a C plus, I'm sure there is a C plus, uh, thing
[2673.98 → 2674.72] that can do that.
[2674.80 → 2675.12] I don't know.
[2675.16 → 2676.28] I just assume everything.
[2676.28 → 2676.88] Everything is possible.
[2677.30 → 2681.60] You're just talking about like, you want like, because they have special cased file
[2681.60 → 2684.62] descriptors with the static analysis in rust or something like this.
[2684.62 → 2689.20] Uh, yeah, I think I'm, I'm talking about type system, and I'm like, well, the type system
[2689.20 → 2690.64] in both can do what you're talking about.
[2690.76 → 2693.88] So we're just talking about the type system as opposed to other things, right?
[2693.94 → 2694.22] Yes.
[2694.22 → 2699.94] I'm, I'm just talking about the kinds of things like this is, you know, as like, I'm, I'm
[2699.94 → 2703.50] trying to present the case for why someone would say they would rather write this kind
[2703.50 → 2704.40] of thing in rust, right?
[2704.40 → 2709.08] Is instead of experiencing a crash with Phil C at runtime.
[2709.32 → 2709.80] Okay.
[2710.36 → 2713.92] We could find that out from the compiler, right?
[2713.92 → 2716.80] That like, oh, this kind of access isn't allowed.
[2716.80 → 2718.22] That's not thread safe.
[2718.22 → 2722.66] That's not that escaped its region, but it shouldn't this kind of value, right?
[2722.72 → 2727.12] Like there, there are things that we can do there, right?
[2727.12 → 2732.64] In like rust with the type system that fight the same kinds of bugs.
[2732.64 → 2735.24] You might get, you might get solved from Phil C, right?
[2735.26 → 2740.04] But instead of, uh, instead of having a crash at runtime, we get, it doesn't compile.
[2740.04 → 2741.12] And I handle that case.
[2741.12 → 2741.28] Yeah.
[2741.28 → 2745.42] The borrow checker defeats use after free and double free at compile time.
[2745.68 → 2747.66] That is the objective of the borrow checker.
[2747.74 → 2748.04] Yes.
[2748.16 → 2748.28] Yeah.
[2748.44 → 2751.44] That's a probable way more succinct way to say that.
[2751.76 → 2752.70] Good job, Ed.
[2752.84 → 2753.18] Got it.
[2753.18 → 2756.28] I like to think of it is as just like, it's effectively a unique pointer.
[2756.62 → 2756.80] Yeah.
[2757.06 → 2757.94] But at compile time.
[2758.46 → 2758.98] Right.
[2758.98 → 2771.32] So, so my point being separately from, I think it's obviously good that there's an option where we can solve a bunch of these classes, classes of bugs in C and prevent it.
[2771.32 → 2771.66] Right.
[2771.82 → 2775.34] In this case of like, which language would I pick for certain projects?
[2775.64 → 2783.14] There are definitely like reasons you would pick rust over just picking Phil C for like a new Greenfield project.
[2783.22 → 2786.78] Of course, there are other reasons why you might pick C over rust as well.
[2786.78 → 2790.92] Um, like you might actually ship it and things like that, which is cool.
[2791.56 → 2795.20] Um, so, but that's like those kinds of bugs.
[2795.30 → 2798.64] Phil C does not solve that at compile time.
[2798.74 → 2801.26] That's all I'm trying to say as like a comparison of the two.
[2801.34 → 2804.58] And that's like a reasonable trade off that people want to make.
[2804.86 → 2805.22] Yes.
[2805.30 → 2807.32] And that's also, that's where you get the performance from.
[2807.32 → 2809.64] That's because of the borrow checker, not the type system.
[2809.64 → 2809.82] Right.
[2809.86 → 2811.28] Just so we're clear on that part.
[2811.32 → 2811.54] Right.
[2811.78 → 2812.50] Uh, yeah.
[2812.50 → 2812.94] I mean.
[2812.94 → 2814.64] Or just so I'm, just so I'm understanding it.
[2814.72 → 2815.10] I should say.
[2815.32 → 2815.34] Right.
[2815.40 → 2816.50] Because that was the part that threw me.
[2816.50 → 2818.18] I was like, why is that a type system problem?
[2818.30 → 2818.46] Okay.
[2818.78 → 2820.24] Tech, um, actually.
[2820.58 → 2820.88] Okay.
[2821.02 → 2822.56] So it is actually a type system.
[2822.84 → 2828.48] Well, the borrow checker is sort of like a result of the linear affine type system that rust has.
[2828.66 → 2829.04] Okay.
[2829.18 → 2829.52] And so.
[2829.52 → 2830.58] I'm too dumb with this conversation.
[2830.78 → 2831.42] I don't know what's going on.
[2831.42 → 2832.04] I would just say.
[2832.50 → 2832.70] Okay.
[2833.42 → 2834.28] They go together.
[2834.56 → 2835.12] You would like.
[2835.24 → 2835.46] Right.
[2835.46 → 2836.54] So you're talking about type system.
[2836.64 → 2839.28] The type system being like including the borrow checker.
[2839.42 → 2839.72] Yes.
[2839.92 → 2840.22] Okay.
[2840.22 → 2840.56] Gotcha.
[2840.68 → 2841.28] Yes, exactly.
[2841.42 → 2841.96] That makes sense.
[2841.96 → 2847.92] Uh, so I also have another question, which is that, uh, does rust catch all the same
[2847.92 → 2850.44] memory errors that Phil C does?
[2850.48 → 2852.30] Because I don't know if that's true.
[2852.52 → 2853.82] Phil C might catch more.
[2854.24 → 2854.84] It does.
[2855.18 → 2855.34] Yeah.
[2855.34 → 2856.24] That's the best part.
[2856.24 → 2859.32] Like if you really care about security, you probably shouldn't be using rust.
[2859.90 → 2860.34] Yeah.
[2860.96 → 2863.94] Rust will catch them, but like it'll turn the condition into a DOS.
[2864.18 → 2869.50] So it's like, it's not an exploitable memory access, but it's also not caught at compile time.
[2869.96 → 2871.82] So like, like you can do that.
[2871.82 → 2877.32] I mean, even, I mean, even at runtime, does Phil C catch things that rust doesn't catch is my question.
[2878.36 → 2879.00] At runtime?
[2879.00 → 2879.94] I thought I saw a condition.
[2879.94 → 2880.18] At runtime.
[2880.18 → 2884.84] I unfortunately forgot to save it, but it's a condition in which, uh, Phil C does not catch
[2884.84 → 2886.12] something in which rust does.
[2886.26 → 2888.92] I really wish I would have unsafe blocks.
[2888.92 → 2897.00] There are, I think certain things you can do that in rust inside unsafe blocks that
[2897.00 → 2901.72] rust does not check real quick, even all of its stuff.
[2901.72 → 2907.76] And maybe still, I'm not actually a hundred percent sure, uh, if it will do a CVE, but inside
[2907.76 → 2909.82] of unsafe blocks that Phil C does catch.
[2909.82 → 2911.16] I do have to go in five minutes.
[2911.26 → 2912.02] I have a question for the office.
[2912.02 → 2912.60] I have a question for the office real quick.
[2912.60 → 2912.62] I have a question for the office real quick.
[2912.62 → 2913.06] I have a question for the office real quick.
[2913.06 → 2913.76] Yes, go ahead.
[2913.96 → 2915.62] Miscall related memory safety issues.
[2915.70 → 2921.80] Are you saying, for example, in a miscall handler where it does a copy to user, like outside
[2921.80 → 2923.76] of the bounds of a memory region?
[2923.92 → 2925.64] Like what, what about miscalls in particular?
[2926.00 → 2927.34] I'm curious what you're saying there.
[2927.42 → 2928.12] And then I do have to run.
[2928.20 → 2928.64] I'm sorry, guys.
[2930.24 → 2935.02] I just want to say, he said, he did confirm CV in unsafe blocks is totally possible.
[2935.06 → 2935.54] He said yes.
[2935.78 → 2935.88] Okay.
[2935.88 → 2937.28] How would Phil C detect that?
[2938.34 → 2938.64] Yes.
[2938.64 → 2941.16] PIZ, give us the give us the, the nine yards.
[2941.28 → 2943.30] And then we'll have to just have Phil come on.
[2943.30 → 2943.48] Yeah.
[2943.66 → 2944.02] 100%.
[2944.02 → 2944.68] I'm so curious.
[2944.96 → 2947.38] The right thing is to have him on the show.
[2947.48 → 2950.18] If he, as long as he wants to come on, I mean, he said yes.
[2950.48 → 2950.72] Okay.
[2950.80 → 2951.04] Yes.
[2951.30 → 2951.62] Yes.
[2951.62 → 2952.38] Yes.
[2952.38 → 2953.94] There's also, I do think.
[2954.40 → 2956.28] I'll just mention one other thing.
[2956.60 → 2957.86] As the rust person.
[2958.06 → 2958.92] I'll just put this back on.
[2961.02 → 2961.46] Oh.
[2962.14 → 2968.90] Sometimes 20% slower or up to four times and 1.5 to two times as much memory actually makes
[2968.90 → 2972.68] it is not possible to do constrained hardware or like other stuff like that.
[2972.68 → 2972.96] Sure.
[2972.96 → 2973.96] We'll just literally make it.
[2974.00 → 2978.28] So this is just not possible to accept the performance hits because some places in the
[2978.28 → 2982.38] world performance still actually matters, and you can't just spin up 5,000 new lambdas
[2982.38 → 2985.08] and pay $10 million in cloud costs.
[2985.16 → 2985.28] Okay.
[2985.34 → 2985.62] There you go.
[2986.52 → 2987.12] You've just summoned.
[2987.18 → 2988.58] You're going to summon DHH, dude.
[2988.66 → 2989.36] You're going to summon him.
[2989.48 → 2990.44] He's going to be like, yes, we can.
[2990.46 → 2990.96] What if he just walked out?
[2990.98 → 2992.14] He's like, yes, we can.
[2992.20 → 2993.66] We will spin up all of them.
[2994.46 → 2995.16] No, he's against that.
[2995.16 → 2995.68] It's also true.
[2995.82 → 2996.38] You got to be careful.
[2996.48 → 2998.32] You can tactically spin up all of them.
[2998.38 → 2999.12] You just pay a lot of money.
[2999.82 → 3000.92] We got to have it on him.
[3001.04 → 3002.20] This is blowing my mind right now.
[3002.26 → 3005.32] He said that it intercepts all miscalls at the ABI layer, which makes sense.
[3005.32 → 3006.56] Phil, I know what we need.
[3006.56 → 3010.74] We need a slideshow with these examples, and we can work on it together.
[3010.88 → 3013.74] I'll message you after this on X, and we'll get this set up.
[3014.00 → 3014.46] Oh, yeah.
[3014.46 → 3018.34] With a slideshow with code examples and then, Ed, you can ask every single question you want.
[3018.44 → 3019.70] I've been wanting to do this a lot.
[3019.76 → 3028.58] Ever since Trash did the TypeScript presentation, I've been wanting to do more presentations and then have us all interrupt the presentation and be like, but what about this?
[3028.64 → 3029.20] What about this?
[3029.26 → 3029.74] What about this?
[3029.76 → 3031.74] And that was such a fun time.
[3032.48 → 3032.76] Yes.
[3033.24 → 3033.50] All right.
[3033.56 → 3033.74] Okay.
[3033.74 → 3035.40] Well, then let's end it right now.
[3035.50 → 3036.42] Low levels of a question.
[3036.62 → 3037.76] I just want to say one quick thing.
[3037.78 → 3038.30] Oh, go ahead, Brian.
[3038.36 → 3038.46] Sorry.
[3038.46 → 3044.44] I will say that every time I use a Union NC, I get so happy and so sad at the same time because it does make me happy.
[3044.46 → 3053.38] I will say that automatic tagged unions at the syntax level is just a thing of glory and beauty 100% of the time.
[3053.80 → 3053.88] Yeah.
[3053.92 → 3054.50] But don't worry.
[3054.58 → 3057.96] In another 50 years, the C++ committee will finally get one working.
[3057.96 → 3060.34] We're almost there, guys.
[3060.34 → 3060.76] It does suck.
[3060.76 → 3061.56] Just one more committee.
[3061.98 → 3063.02] One more version.
[3063.16 → 3069.08] One more 2,000-page revision and they'll get the discriminated unions working properly instead of sucking.
[3069.16 → 3074.60] Casey, if that were true, then why are some people using, like, C17 instead of C94?
[3074.74 → 3075.76] That doesn't even make sense then.
[3076.34 → 3077.22] It doesn't make sense.
[3077.34 → 3078.04] Go, checkmate.
[3078.60 → 3081.50] Because 94 is bigger than 17, so we should be using that one, don't you think?
[3081.56 → 3082.58] 2020, 2094.
[3082.88 → 3082.98] Yeah.
[3083.18 → 3083.38] Checkmate.
[3083.38 → 3084.54] All right, I got to go.
[3084.62 → 3084.76] Bye.
[3084.76 → 3085.74] Better than C99.
[3086.54 → 3087.70] Sounds worse then, really.
[3089.50 → 3092.82] All right, everybody, we'll go as well just because this is happening.
[3093.00 → 3095.28] Ed already left us and now the stream is completely screwed up.
[3095.62 → 3097.68] Thank you, everybody, for joining us for this.
[3097.68 → 3102.70] Hey, if you are watching on YouTube, you can see everything on Spotify.
[3102.88 → 3107.78] You get the full episode because you miss a lot of the banter when you only watch it on YouTube.
[3108.28 → 3109.54] So thank you very much for watching.
[3109.64 → 3110.60] Thank you for all the guests.
[3110.60 → 3112.98] Ed with low-level.academy.
[3113.32 → 3115.34] Casey with computerenhanced.com.
[3115.50 → 3118.16] And Siege with boot.dev slash Siege.
[3118.66 → 3119.66] Yeah, or by the way.
[3119.82 → 3123.60] Or by the way, if you want to support both TJ and I because I also have two courses on there as well.
[3123.94 → 3125.36] I just did, like, a Spider-Man thing.
[3125.72 → 3128.90] But the name is the Spider-Gen.
[3129.18 → 3129.42] All right.
[3129.52 → 3130.36] Thank you, everybody.
[3130.36 → 3136.74] I boot up the day, vibe caught when errors are my screen.
[3137.98 → 3141.56] Terminal coffee and hair.
[3142.52 → 3144.54] Live in the dream.
