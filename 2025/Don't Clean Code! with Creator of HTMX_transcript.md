[0.00 --> 4.94]  Okay, so I don't really know how to introduce today's stand-up, but TJ, are we recording?
[5.56 --> 7.18]  Oh, we're recording. We've been recording.
[7.40 --> 11.72]  Oh, we're recording. Okay. My wife is calling me. Of course, she's gonna... Here.
[12.58 --> 14.12]  Put her in the call, dude.
[14.46 --> 16.00]  Discuss amongst yourself.
[16.40 --> 17.04]  Hot mic in.
[18.28 --> 21.34]  What are we talking, guys? What are we talking? I have stuff to do.
[21.86 --> 22.86]  What are we doing today?
[23.24 --> 26.54]  Well, so for me, I'm a little bit blocked on QA.
[26.54 --> 32.12]  They told me they'd be able to finish everything by end of month, last month.
[32.32 --> 34.92]  But sure enough, fours turned to fives.
[35.58 --> 40.10]  And so that's where I'm at. I'm mostly blocked on them.
[40.44 --> 44.52]  I've been updating documentation, but that's it. That's an update from my end. Carson?
[46.72 --> 53.44]  I'm dealing with student grading and trying to figure out how GitHub Actions work.
[53.44 --> 57.48]  And I don't know. It's gonna be... It's a long way. A lot of points.
[57.94 --> 60.20]  There's a lot of points on the board right now.
[61.06 --> 63.68]  I thought everyone just got A's these days. What happened to that?
[63.90 --> 66.76]  Yeah, I know. I try not to be like that, but it is easy.
[67.20 --> 68.12]  It's like, just shut up.
[68.76 --> 70.00]  It is easy.
[71.02 --> 74.62]  Look, if they're gonna use AI to write their papers, just use AI to grade them.
[74.90 --> 76.22]  I tell the kids, like...
[76.22 --> 76.76]  That's fair.
[76.76 --> 78.84]  I tell the kids, like... I know, exactly.
[78.84 --> 82.92]  I tell the kids, like, look, I'm a pretty good programmer, and I can teach you how to program.
[86.12 --> 87.14]  All right, here we are.
[87.52 --> 88.40]  All right, here we are.
[88.88 --> 90.68]  All right, we're all set, Prime. See you later.
[91.48 --> 92.78]  All right, you guys already had a stand-up?
[92.78 --> 93.00]  Good talk, guys.
[93.54 --> 95.82]  Hey, I have no blockers. I have no blockers.
[96.72 --> 98.32]  No blockers? Wow, I'm very blocked.
[98.40 --> 99.50]  That's why I haven't got anything done.
[99.56 --> 101.86]  Can you explain why you haven't turned in any code for three weeks?
[101.86 --> 107.56]  I've been committing a bunch. It's just all configuration for my new Arch install.
[107.72 --> 110.80]  So, like, I'm unblocked committing so much configuration.
[111.56 --> 113.70]  You're still sharpening the axe, I see.
[114.20 --> 117.44]  Sharpening the axe. You have no idea how sharp this axe is at this point.
[120.10 --> 122.00]  Today we have a special guest on.
[122.10 --> 128.86]  We have Carson Gross, professor at Montana State University, author of HTMX, which is a web...
[128.86 --> 131.54]  How do you describe that?
[131.72 --> 135.88]  It's taking every popular trend on the internet and doing the opposite of it.
[136.38 --> 141.22]  And at MSU, he teaches system programmings, databases, and operating systems.
[141.40 --> 141.96]  Did I get that correct?
[142.58 --> 146.12]  I teach compilers. I don't teach OS.
[146.52 --> 146.80]  Okay.
[146.82 --> 147.84]  I don't want to teach OS.
[148.20 --> 149.18]  Yeah, I'm playing on that one.
[149.74 --> 150.34]  Fair enough.
[150.34 --> 155.98]  Okay, so just classic embedded systems guy writing web frameworks is who we've invited on.
[155.98 --> 158.18]  And again, normally we have Tiege.
[158.54 --> 159.86]  Tiege needs no introduction.
[160.04 --> 161.04]  He streams, by the way.
[161.50 --> 163.04]  And Casey Miratori.
[163.56 --> 166.04]  Amazing game dev and computerenhance.com.
[166.14 --> 166.88]  Am I right, Casey?
[167.12 --> 167.56]  Am I right?
[167.90 --> 168.40]  You're right.
[169.04 --> 171.52]  Also, avid bird enthusiast.
[171.74 --> 173.72]  Avid bird enthusiast.
[173.94 --> 175.28]  Ornithology specialist.
[175.66 --> 175.92]  Exactly.
[176.52 --> 179.20]  Many people are wondering why TrashDev isn't here today.
[179.46 --> 183.32]  It's because Carson figured out the one password, and Trash is locked out of his account.
[183.48 --> 183.60]  Yep.
[183.98 --> 188.76]  As soon as Trash successfully resets all his passwords, he'll be back on the program.
[189.12 --> 193.54]  Unfortunately, he has an alphabetical order, and he has to go through every single website
[193.54 --> 195.48]  to be able to have his one password back in.
[195.90 --> 197.20]  Trash$1.
[197.20 --> 199.46]  All right.
[199.60 --> 205.72]  So with that, today we're going to be discussing a special topic, which is really the, what
[205.72 --> 207.86]  is it, the bizarro world of clean code?
[208.00 --> 211.26]  It is Coding Dirty by Carson Gross.
[212.42 --> 216.36]  Carson, why don't you give us a quick introduction of what Coding Dirty is, and then maybe your
[216.36 --> 220.42]  kind of stance on why people should consider coding this way.
[222.02 --> 225.22]  Well, you know, I have to say, like, so thanks for having me on.
[225.22 --> 230.80]  And I, the Coding Dirty was an essay that had been kicking around in my head for, for a
[230.80 --> 231.48]  long time.
[231.98 --> 235.36]  And, you know, you guys have talked to Uncle Bob, who's the clean code guy.
[235.76 --> 241.40]  And the, that clean code essay or book, I guess, sort of came out of like the agile
[241.40 --> 242.58]  world like this.
[242.66 --> 247.54]  And I had grown up, like when I was, when I first started programming professionally,
[247.80 --> 249.12]  Java was like, yeah, there you go.
[249.70 --> 251.98]  Java just like started being the big thing.
[251.98 --> 258.12]  And so I kind of grew up with like the patterns and like the agile manifesto and then test driven
[258.12 --> 258.48]  development.
[258.68 --> 262.26]  A lot of that stuff was really baked into the world that I was in.
[262.50 --> 267.42]  And so I just finally like got to a point that I'd always, I, there was something about
[267.42 --> 268.70]  it that didn't sit right with me.
[268.88 --> 273.18]  And so I finally just was like, you know what, I'm going to write an essay and try and like
[273.18 --> 274.76]  sort of go the other way with it.
[274.76 --> 279.72]  Um, so, um, and, uh, there were, you know, I do, I do have to say there's a lot of stuff
[279.72 --> 282.30]  and Uncle Bob, he's been a really good sport on Twitter.
[282.30 --> 284.94]  So I've got, I don't have anything bad to say about it.
[284.94 --> 287.32]  He was just a cool guy on, on Twitter the last couple of days.
[287.84 --> 293.18]  Um, but, uh, the, there were a few things really that stood out to me when I, you know,
[293.18 --> 296.04]  you guys had, had him on to talk about clean code and all that stuff.
[296.04 --> 299.46]  And I was like, you know, I just got to write this essay, um, that talks about the way
[299.46 --> 300.40]  that I write code.
[300.48 --> 305.66]  And one thing I do in the essay is I say, look, I'm not saying you need to write code
[305.66 --> 309.42]  this way because the way that I write code isn't necessarily the way you're going to write
[309.42 --> 310.60]  code or whatever.
[310.92 --> 312.18]  Um, and, but that's okay.
[312.18 --> 316.02]  But I want to show that like, I've had a pretty successful programming career and I do things
[316.02 --> 320.20]  pretty differently, uh, than the clean code, uh, suggests.
[320.36 --> 324.60]  Um, and so like the three things that I really focus on in the essay is number one, like I think
[324.60 --> 325.78]  methods can be big.
[325.78 --> 328.82]  Like I've got no problem with, uh, actually very large methods.
[328.82 --> 331.28]  Yeah, exactly.
[331.48 --> 332.36]  I like big methods.
[332.96 --> 337.76]  Um, and, uh, uh, I also, I'm not a huge fan of unit tests.
[338.02 --> 339.00]  Um, I like that.
[339.10 --> 340.54]  I don't want to say I'm not a huge fan.
[340.58 --> 344.68]  I like, I don't use unit tests to drive my development is I guess the way I would say it.
[344.82 --> 350.10]  And then the last thing that I'd say is I really think, um, particularly in the Java world,
[350.10 --> 355.74]  um, and this appears to be the case to at least some extent in, uh, um, the rust and like
[355.74 --> 358.56]  the other and, and, uh, TypeScript and so forth.
[358.78 --> 361.82]  Like I, I think there's often too many classes.
[361.82 --> 365.84]  Like we, we expose too much stuff to end users.
[365.84 --> 369.14]  Um, and we, we just try and like, you know, decompose everything.
[369.14 --> 374.34]  And, um, you know, it tends to lead towards what I would consider over architected code.
[374.34 --> 379.42]  Um, and I think there's some, some good ideas, like for example, you know, a class should
[379.42 --> 384.00]  be coherent is, uh, something that you'll hear, you know, very smart people say, and
[384.00 --> 384.60]  that's true.
[384.74 --> 389.82]  But also if you worry too much about coherence, um, where every little thing has to be its
[389.82 --> 393.02]  own class, then you get into this sort of morass of code.
[393.08 --> 396.86]  So, so those are sort of the, uh, big three points that I wanted to talk about.
[396.96 --> 400.22]  Um, and, uh, you know, I'm happy to drill into each one, uh, if you like.
[400.66 --> 401.66]  TJ got a book.
[401.66 --> 405.76]  I was waiting until later to pull this one out.
[405.86 --> 409.18]  I figured if I have one book, I have to have the other hypermedia systems guys.
[409.32 --> 410.24]  That's a good one.
[410.46 --> 411.36]  It's a really nice.
[411.44 --> 413.98]  It's an excellent hardcover, beautiful cover, by the way.
[413.98 --> 414.22]  Yeah.
[414.64 --> 415.54]  Available on Amazon.
[415.98 --> 416.52]  Look at this.
[416.60 --> 417.84]  It's wonderful inside.
[417.90 --> 418.74]  I've read it cover to cover.
[418.86 --> 419.30]  No lie.
[419.42 --> 419.90]  Thank you.
[419.98 --> 420.62]  I appreciate that.
[420.62 --> 420.70]  Yeah.
[421.52 --> 421.88]  Yeah.
[422.08 --> 422.64]  That's a book.
[422.76 --> 427.74]  I was waiting to pull that out like as a prop later, but you kind of outed that I had
[427.74 --> 428.22]  pulled it there.
[428.32 --> 430.28]  Like I've got, let's pull it out again as a prop later.
[430.28 --> 433.60]  Cause I'd like to know more about this book, but now it's probably not the best time since
[433.60 --> 436.14]  the, in, we were supposed to be talking about the code thing.
[436.38 --> 438.36]  So let's, let's bring, bring that out again though.
[438.48 --> 439.18]  Keep that handy.
[439.42 --> 439.86]  We'll bring it back.
[439.88 --> 440.64]  We'll circle back.
[440.76 --> 442.00]  We have to do standup language.
[442.44 --> 442.68]  Sorry.
[443.46 --> 444.12]  We'll circle back.
[444.36 --> 445.22]  We won't take it offline.
[445.62 --> 447.86]  We're going to leave it in the standup, but we're going to keep it online.
[448.06 --> 448.42]  Yes.
[448.62 --> 449.48]  Keep it online.
[449.48 --> 451.70]  That's the name of the game for us for sure.
[452.12 --> 452.26]  Yeah.
[452.30 --> 461.40]  So I would say that this is one of, it is definitely a big departure from what is, you know, adamantly
[461.40 --> 467.80]  stated in, you know, the, the official quote unquote clean code lectures and book to say
[467.80 --> 470.48]  that you're going to have larger functions, right?
[470.48 --> 475.78]  Like larger functions seems to be something that is, is extremely portrayed extremely negatively.
[475.78 --> 482.44]  And it's not really immediately clear why, uh, as with many things like no empirical evidence
[482.44 --> 483.64]  is given for this.
[483.64 --> 489.64]  And also no examples really are given for it oftentimes, meaning there aren't like normally
[489.64 --> 494.72]  if you were going to do architecture stuff, which I have given lectures on in the past briefly,
[494.72 --> 498.28]  but you know, it's not something that I spend most of my time talking about.
[498.28 --> 502.22]  If you're going to do architecture stuff, you should at least have like gamed it out.
[502.42 --> 505.36]  Like, okay, here's all the ways we could have written this.
[505.54 --> 508.34]  And let's look at each of them and see like, what is the benefit?
[508.50 --> 509.24]  What's the drawback?
[509.56 --> 511.24]  And we're going to try a couple different things.
[511.38 --> 513.96]  So let's look at a function that has this kind of properties.
[514.06 --> 515.66]  Let's look at functions that have this kind of properties.
[515.66 --> 517.44]  And what does it look like when they're bigger or small?
[517.56 --> 518.72]  None of that happens, right?
[518.74 --> 521.52]  It's just, Hey, they should all be small next thing.
[521.58 --> 521.84]  Right.
[521.86 --> 524.18]  And it doesn't, it's all vocab, right?
[524.18 --> 528.06]  It's all just descriptive, but doesn't actually show code.
[528.06 --> 532.56]  And then when you actually do look at some code, like the example code or something in clean code, it's really bad.
[532.68 --> 532.80]  Right.
[532.80 --> 535.46]  It's like, there's so many things I would criticize about this.
[535.50 --> 538.90]  And I picked one small segment for the clean code, horrible performance video.
[538.90 --> 539.18]  Right.
[539.54 --> 542.02]  And just said, here's all the reasons I think this is terrible.
[542.02 --> 542.48]  Right.
[542.56 --> 543.92]  But that's just one snippet.
[543.94 --> 545.06]  You could do that for everything.
[545.06 --> 546.06]  Sure.
[546.06 --> 552.98]  And so I would say that like you actually cited in your essay an actual study, right?
[553.14 --> 555.46]  From Code Complete where they looked at it.
[555.66 --> 563.16]  And I guess what you were saying is they found the opposite, is that larger functions actually don't have empirical evidence against them so much.
[563.28 --> 564.86]  If anything, it's slightly for them.
[564.90 --> 565.50]  Is that correct?
[565.50 --> 565.94]  Yeah.
[567.14 --> 573.54]  So I do cite a couple of, there's a book, an older book called Clean Code, which talks about method length.
[573.72 --> 581.64]  And the studies they went through suggested that actually longer methods are higher quality and that there are fewer lines of bugs per line of code.
[581.64 --> 585.28]  And which is, you know, that's a metric that's reasonable.
[585.52 --> 588.08]  There's a more recent paper.
[588.22 --> 589.14]  Someone threw it at me.
[589.22 --> 591.74]  It's like, oh, because I was saying, oh, longer methods are fine.
[591.76 --> 593.84]  And they were like, OK, well, we have.
[594.04 --> 599.84]  And I've cited this old older book, which most of that research cited in that book is from the 60s and 70s.
[599.84 --> 601.16]  So, you know, a little dated.
[602.00 --> 605.40]  And they sort of threw another essay at me and were like, short methods are better.
[605.44 --> 606.84]  And I went and actually read the paper.
[607.00 --> 608.58]  Never throw a paper at an academic.
[609.10 --> 609.32]  Yeah.
[609.32 --> 618.08]  And I went and read the paper and it was like, OK, first of all, this the paper here, this paper says that methods up to 20 lines,
[618.12 --> 624.02]  which is much longer than the four to five lines recommended by Clean Code are ideal.
[624.44 --> 629.64]  And then when you look, we actually read and like the statistics, the statistics that they were using,
[629.64 --> 637.70]  the one that had the least correlation with with function size was bugs, bugs per function.
[637.70 --> 643.46]  And so like that had no correlation with the with code length.
[643.46 --> 647.46]  And I was like, that's the only one that matters because the other ones were like change prone proneness.
[648.26 --> 648.74]  Well, yeah.
[648.76 --> 652.50]  Like if you put everything in one method, of course, it's going to be more change prone because it's all there.
[652.74 --> 653.58]  Like that doesn't count.
[653.58 --> 655.00]  There's 10 times as many functions.
[655.24 --> 657.46]  There's probably going to be less bugs per function.
[657.46 --> 659.32]  But that doesn't mean there's less.
[659.32 --> 666.20]  Well, and that's like that's what I if I if I wasn't so lazy, I'd go and do the math and like get the data set from these guys and be like,
[666.20 --> 671.38]  this looks to me like you're saying that there are fewer bugs per line of code in larger functions.
[671.96 --> 675.24]  So, you know, and then and then I also went out in that section.
[675.38 --> 681.16]  So all this stuff's on in the essays page on HTMX dot org, the code and dirty essay.
[681.16 --> 692.74]  And I go out and I find in like, you know, Chrome and Redis and like IntelliJ, like all these big, successful software projects that have very high quality levels.
[693.44 --> 701.24]  And they all have massive functions in them, like hundreds, you know, like in the height, you know, close to 100 lines or more functions in them.
[701.24 --> 707.36]  And so I just don't I think, you know, again, I don't want to say you have to have long functions, but I think they're good.
[707.66 --> 712.12]  There's good evidence that long functions are not bad and maybe even good.
[712.14 --> 719.88]  And I do make one philosophical argument for big functions, which is when functions are big, when you're when you're important functions are big.
[719.96 --> 721.54]  That like that's a physical.
[721.74 --> 724.12]  It's an aesthetic like hint.
[724.16 --> 725.22]  Like this is important.
[725.48 --> 727.50]  Like there's no 100 line function.
[727.50 --> 728.50]  That's not important.
[728.94 --> 729.38]  Right.
[729.38 --> 737.18]  Like and if you try and break everything up into like a bunch of five line functions, you kind of smear the importance around in your code module quite a bit.
[737.42 --> 739.06]  And I just don't think that's good.
[739.12 --> 743.56]  If there's code reuse to be found by extracting methods out, then that's OK.
[743.62 --> 745.38]  Now you've got a reason to do it for sure.
[745.56 --> 753.20]  But if there isn't, you know, I don't I just don't think small functions for their own sake is is a good approach to to writing software.
[753.72 --> 756.22]  I think there's also it's just not the way I do it.
[756.22 --> 766.66]  I think there's also some other, you know, aspects of that, too, which is that like in a long function, it's easier for the programmer to digest because I can just go.
[766.90 --> 770.26]  They're just reading it top to bottom and they go, OK, I see exactly what this thing does.
[770.26 --> 777.62]  I don't have to stop every so often and go look at another function that I might not know exactly what the specifics are.
[778.12 --> 778.48]  Right.
[778.72 --> 780.94]  And easier to debug.
[781.08 --> 788.82]  If you have a lot of context, like if you find yourself passing a lot of arguments around with like context stuff like, OK, just just make it's all there and it's fine.
[789.58 --> 790.22]  You know.
[790.30 --> 791.46]  Yeah, I think that's true, too.
[791.62 --> 791.96]  I'm sorry.
[792.08 --> 793.10]  I got to go.
[793.22 --> 793.76]  Stupid robe.
[794.08 --> 794.48]  That's all right.
[794.84 --> 795.98]  All solo robe.
[796.06 --> 796.36]  It's all right.
[796.38 --> 797.46]  I can't take mine off.
[797.46 --> 801.06]  The other thing that I think this one, it's OK.
[801.52 --> 802.30]  No, it's all right.
[802.34 --> 803.32]  I'm not ready for that.
[804.66 --> 811.66]  The other thing, too, I think is I've noticed this for like in Golang.
[811.66 --> 823.08]  Golang, it's easy or it's easy to see when something like iterates over a list because they don't have fancy ways to like do list iteration on accident.
[823.08 --> 823.44]  Right.
[823.50 --> 830.16]  And one of their ideas is like, yo, if something's expensive, you should like put it like you should make it obvious.
[830.16 --> 831.06]  You'll put it in a loop.
[831.18 --> 832.50]  It does it for all of these things.
[832.50 --> 834.90]  So you're like, oh, it does it for all the things.
[835.74 --> 844.18]  And I do find for myself when I've done like NeoVim has a bunch of functions that are like incredibly large.
[844.18 --> 848.22]  Some of them I wish they weren't, but like also whatever, like it's fine.
[848.28 --> 852.30]  And also NeoVim, I would say, is like pretty successful software or whatever.
[852.44 --> 852.60]  Right.
[852.66 --> 854.66]  But I see the for loops.
[856.18 --> 856.60]  Right.
[856.64 --> 858.90]  I know this thing goes over all the things.
[858.90 --> 862.64]  That's actually like really useful information for me as a programmer.
[862.64 --> 869.00]  And I was like, oh, that function gets called over all the elements or all of the elements twice.
[869.16 --> 869.56]  Right.
[869.60 --> 876.28]  Or something like or we have nested for loops and suddenly you're like, oh, now we really have to be worried about something.
[876.40 --> 878.54]  Where if it's like a function and a function and a function.
[878.54 --> 880.56]  Or probably not if you hit the network at any point.
[880.76 --> 882.34]  Well, yeah, that's a separate.
[882.64 --> 882.86]  Yes.
[883.08 --> 883.34]  Right.
[883.34 --> 891.16]  But I guess I'd also say the talking about the change proneness was mentioned.
[891.70 --> 904.48]  I think there's additional things for large functions that speak to that, which is assuming that the code is going to change, which is the most important thing to be considering when you're thinking about architecture.
[904.48 --> 913.52]  Like usually the most important thing for architecture long term is how is it going to handle the fact that we have to change some things.
[913.80 --> 913.92]  Right.
[914.94 --> 919.94]  Short term architecture, you know, is about does this thing work well at all.
[920.06 --> 920.24]  Right.
[920.28 --> 930.72]  But long term is does it support us making different decisions because we decide, oh, we really need to do this or we need to deport to this platform that does some differences or who knows what it is.
[930.82 --> 932.10]  We want to add these features.
[932.10 --> 943.68]  And one of the things about large functions is that if you have small functions, every time you make a change to the smaller function, these tiny little functions, you have to be aware.
[943.82 --> 955.28]  You almost need assistance from your tooling to know who calls that function, because if you change something about how it behaves, you may be in trouble if there was any possibility of leakage.
[956.76 --> 959.94]  And it's very hard to guarantee that you don't have any of that.
[959.94 --> 969.28]  You know, people who are really into solid and all these things pretend that they're like some that they're somehow also functional programmers, that there's no side effects, but they never write things that way.
[969.28 --> 971.04]  The objects are getting changed all the time.
[971.14 --> 971.26]  Right.
[971.26 --> 979.00]  And so really, you look at this function and they're very rarely in a solid code base or things like that.
[979.06 --> 982.48]  Very rarely are there no side effects in these small functions as well.
[982.48 --> 992.98]  And as a result, if you have one large function and you just look at all these steps in the middle of that, you don't really have to ask yourself, is someone else calling into the middle of this function?
[992.98 --> 997.44]  Because that's basically impossible unless you've got labels and long jumps or something crazy going on.
[997.48 --> 997.66]  Right.
[997.88 --> 999.24]  No one can come in there.
[999.30 --> 1000.66]  You know that they have to start at the top.
[1000.66 --> 1004.58]  If you have all these other little tiny things and that's how this operation is happening.
[1004.76 --> 1007.80]  So instead of a thousand line function, you have 110 line functions.
[1008.10 --> 1013.98]  All of a sudden for each one of those, you've got to remember, wait, did anyone else use this function for something that I'm about to change?
[1014.10 --> 1017.94]  Or should I maybe just leave it and make copy it and make a new function?
[1018.16 --> 1021.88]  That's even worse because now I've got two copies of something that does something very similar, but I changed one.
[1021.88 --> 1036.32]  And so keeping functions large if there's no other reason to pull the pieces out is actually important for a lot of reasons, not just because it's easier to read, but also because it may be easier to change and to have confidence in changing as well.
[1037.28 --> 1040.76]  You know, easier to test too because it's just it's that function that you're testing.
[1041.20 --> 1043.30]  Now you're not like, oh, wait, okay, crap.
[1043.42 --> 1048.32]  I hope we had coverage tests for this test for this function everywhere else it was used because I just changed how it worked.
[1048.68 --> 1049.36]  Blah, blah, blah, blah, blah.
[1049.48 --> 1049.68]  Right.
[1049.68 --> 1062.14]  So I have maybe a little bit different of a reason why I like larger functions is that often when associated with a bunch of small functions, you also have a bunch of kind of inversion of control things that are passed in on construction that are like, okay, call with this thing.
[1062.62 --> 1068.46]  And so you have this kind of upside down tree effect that's happening where you jump into a function and it calls four other functions.
[1068.58 --> 1069.40]  Like that's all it does.
[1069.44 --> 1070.56]  It's just function A, B, and C.
[1070.62 --> 1072.28]  And then you're like, okay, I can kind of get this.
[1072.38 --> 1073.64]  But then it's behind a strategy pattern.
[1073.68 --> 1076.10]  So you're like, okay, what's the implementer of this thing?
[1076.10 --> 1078.58]  Then you jump into the implementer of that thing and you have to find it.
[1078.58 --> 1079.92]  And there's like three different versions of it.
[1079.98 --> 1081.64]  Then you go, okay, which one are we looking at?
[1081.66 --> 1082.30]  We're looking at this one.
[1082.38 --> 1085.16]  And you just do this progressive nail, like drill down.
[1085.28 --> 1093.42]  And by the time you've hopped across two or three or four functions, I start to forget like what was the original function that I was actually in.
[1093.62 --> 1096.26]  And so I have a relatively short context window.
[1096.44 --> 1100.94]  I can get about four functions in before I forget what just like, where was I?
[1101.18 --> 1102.94]  How did I get here?
[1102.94 --> 1109.38]  And then I'm just like spamming control O if you're in Vim and just trying to like hop backwards going, okay, okay, I'm back in.
[1109.48 --> 1110.14]  I'm back in.
[1110.24 --> 1113.74]  And then I go forward, go forward, go forward, jump once and go, I forgot everything again.
[1113.80 --> 1114.20]  Hold on.
[1114.44 --> 1116.44]  What was it two, like two jumps in?
[1116.50 --> 1118.42]  Because then you just get into this like hopping business.
[1118.52 --> 1125.10]  And I think LSPs have made this worse because LSPs have made the navigation of short functions easier,
[1125.10 --> 1132.12]  which means that those that are very adept at remembering like 19 function calls in a row, which I'm just not that person.
[1132.32 --> 1137.00]  It is very easy for them to keep on adding because they can navigate super fast.
[1137.22 --> 1139.66]  Whereas before it was probably a little bit harder.
[1139.80 --> 1141.12]  You'd have to remember your file.
[1141.22 --> 1142.86]  You'd have to fuzzy file find into it.
[1142.90 --> 1145.30]  Then you'd have to search for the function and then jump to the function, right?
[1145.36 --> 1150.84]  You couldn't as easily do it for every single language under the sun unless if you were in some sort of paid for editor.
[1151.32 --> 1154.74]  And so, but obviously Java being having a lot of access to that.
[1154.74 --> 1158.54]  But nonetheless, I just find that I can't understand small functions well.
[1158.88 --> 1162.04]  Like it's just purely a, I lose track of where I was going.
[1162.40 --> 1166.62]  And once you throw in strategy pattern, I just like, I just lose the game.
[1166.62 --> 1169.68]  And I have to like debug a whole bunch with print statements.
[1169.68 --> 1171.74]  Cause that feels like the only way I can contain the context.
[1172.36 --> 1177.44]  Cause actually step debugging becomes too difficult at that point for me to even like walk through it.
[1178.22 --> 1178.66]  Yeah.
[1179.02 --> 1180.20]  I have a different kind of problem.
[1180.40 --> 1181.02]  So there you go.
[1181.52 --> 1182.60]  I totally agree.
[1182.60 --> 1188.54]  I think one thing, like I said this on Twitter the other day, like we need to stop pretending that abstraction is cost-free.
[1188.60 --> 1197.64]  Like it's not like whenever you make something abstract, whenever you slap a class, like you take an if statement and turn it into dynamic dispatch, which is a joke I made today.
[1197.64 --> 1200.44]  Like anytime you do that, like there might be good reasons to do it.
[1200.48 --> 1203.48]  I'm not saying never do it, but don't pretend that's cost-free.
[1203.52 --> 1205.10]  Like there's a bunch of names you got to remember.
[1205.10 --> 1206.54]  Now there's a bunch more crap.
[1206.58 --> 1210.60]  You got to understand, like just who's doing what, what's the dynamic type.
[1210.60 --> 1220.12]  Like it's a lot, it just gets a lot harder to understand and good old loops, ifs and loops, you know, say well and well, they, they, they do what they do and they're easy to, they're easy to understand.
[1220.12 --> 1231.12]  And so we, we shouldn't, you know, get intimidated into creating overly complicated solutions to software because we, you know, we, we're just used to this one tool abstraction.
[1231.30 --> 1237.06]  So we just, whenever there's, whenever stuff starts to look a little ugly, we're like, all right, throw some abstraction at it.
[1237.08 --> 1239.66]  And it just, it can make things significantly worse at times.
[1239.66 --> 1242.16]  But it does make the end product look really nice.
[1242.32 --> 1245.96]  There's like this moment where you have like four lines of code and it does everything.
[1246.10 --> 1251.56]  So I understand kind of that, like the purity pursuit of it all, where you're just like, look at those four lines.
[1251.82 --> 1257.48]  I'm like, set it up, make it run, do a little printing, close gracefully.
[1257.56 --> 1258.98]  And I'm like patting myself on the back.
[1259.00 --> 1260.32]  I'm like, this is beautiful.
[1260.62 --> 1262.92]  And then you just have to do something and then it's horrible.
[1262.92 --> 1274.52]  Well, you know, well, it's worth pointing out that like all of this discussion about long functions is just to support the fact that if you feel like a long function is working well for you, it probably is.
[1275.02 --> 1280.98]  Obviously there's also, I mean, I write plenty of short functions, so I would never criticize a short function for being short.
[1281.20 --> 1285.02]  If that's the appropriate length for the function, then great.
[1285.14 --> 1285.28]  Right.
[1285.28 --> 1289.22]  So I think it's more, it's, it's more just like functions take all sizes.
[1289.50 --> 1289.94]  Right.
[1289.94 --> 1292.84]  Um, like stop fat shaming functions.
[1292.94 --> 1294.14]  Beautiful at any size.
[1294.30 --> 1297.26]  Beautiful at any size is literally where I'm at on functions.
[1297.46 --> 1297.98]  Yeah.
[1298.02 --> 1300.34]  I would point out one more thing because you brought up abstraction.
[1301.06 --> 1312.30]  So I feel like there is a, uh, in the, in the didactic or in the, in the pedagogical versions of these things where people are like making these claims.
[1312.30 --> 1313.92]  And again, they're never proven.
[1313.92 --> 1324.46]  They will say things like, oh, well, the reason it's fine to have all these small functions is you just give them good names and then you just write the code and the names are there.
[1324.88 --> 1328.10]  Now, this is, this is just, just completely false.
[1328.10 --> 1334.44]  And the reason it's completely false is because if that were true, those names would just be the programming language.
[1334.44 --> 1335.22]  You would, right.
[1335.22 --> 1345.30]  If the name could actually capture all of what you actually needed to know to understand how the code behaved, then that would be the programming language.
[1345.30 --> 1358.32]  The reason it's not the programming language is because actually every time we give a function, even a five or six line function, a name, we lose some information about what it actually did.
[1358.42 --> 1359.62]  Some edge case.
[1359.62 --> 1362.12]  It didn't handle some bug that was in there.
[1362.12 --> 1367.40]  Some thing that it's simplifying because we know in this code base, we don't need to do that thing.
[1367.92 --> 1373.06]  Something is getting left out of that name because the name isn't as long as the function is right.
[1373.06 --> 1378.06]  The function is in the language that's the most concise way we know to represent that or we'd be using a different language.
[1378.68 --> 1388.94]  So when you do that, you're creating, and as you do that level upon level, you're creating this sort of complete false sense of what the program's actually doing.
[1389.44 --> 1393.50]  You read something and your brain thinks that's what this function does.
[1393.56 --> 1399.86]  But actually this function does so many other things and doesn't do a bunch of things you were assuming when you read the name.
[1399.86 --> 1403.42]  And so that's why that's not a simple answer to this problem.
[1404.04 --> 1410.76]  It's fine to do this structure because we do need functional decomposition to program for reuse, for just managing.
[1410.96 --> 1415.22]  At some point, if the function's 100,000 lines long, that's going to be pretty difficult to manage, right?
[1415.46 --> 1420.40]  So we do need functional decomposition and we do need to give them names because that's all we can do as humans.
[1420.66 --> 1425.02]  That's the only way we can abstract a thing is to give it a name.
[1425.52 --> 1428.68]  But you have to remember that's not a solution to these problems.
[1428.68 --> 1433.08]  It doesn't solve the problem of is there a bug lurking in here?
[1433.28 --> 1434.80]  Does it not do something I was thinking?
[1434.98 --> 1437.58]  Will this name mislead me into thinking something else was happening?
[1437.70 --> 1438.38]  Blah, blah, blah, blah, blah.
[1438.48 --> 1440.94]  The name isn't a substitute for the understanding.
[1441.28 --> 1447.36]  No matter how good you are, it's not a failure of the programmer that they didn't make a name that perfectly captures it.
[1447.54 --> 1450.34]  If you could, you would be the best language designer in the world.
[1450.48 --> 1452.78]  So that's a given.
[1452.88 --> 1454.34]  So I think it's important to internalize that.
[1454.76 --> 1456.36]  Hey, we need to hear from TJ.
[1456.36 --> 1458.60]  TJ has been silent sitting in a bathrobe.
[1459.10 --> 1460.90]  I think he's actually in a hot tub right now.
[1460.96 --> 1461.82]  I can't tell what's happening.
[1462.16 --> 1463.94]  I'm just absorbing all this great info.
[1464.30 --> 1471.92]  The thing that I was going to say about two, sometimes when you split, and I think you kind of touched a little bit on this prime, but to like expand a little bit more.
[1471.92 --> 1482.80]  One thing that becomes really difficult is there's a temptation to smush a bunch of somewhat related but not exactly the same.
[1482.94 --> 1489.66]  Like push it under one abstraction, and then you pass in like 37 switches to this like top level function.
[1489.66 --> 1494.54]  And then it's going to like do all the things maybe.
[1495.06 --> 1498.80]  And like you might even only construct it one way anyways, which is kind of funny.
[1498.88 --> 1504.18]  You might have accidentally wrote all of these like crazy convoluted option things, blah, blah, blah, blah, blah.
[1504.44 --> 1506.70]  You literally only have one top level caller anyways.
[1506.70 --> 1511.28]  Anyways, that happens quite a bit because you're thinking I'm going to need this later, and then you never do.
[1511.40 --> 1515.80]  The company shuts down, and you could have shipped six months earlier, and maybe your company would have existed.
[1515.94 --> 1519.38]  I've never had that happen to me, except maybe I did.
[1519.48 --> 1530.10]  But anyways, like so sometimes you end up doing this, and it would have been much simpler to understand just because you didn't have to pass all of –
[1530.10 --> 1536.38]  I think Carson, you had mentioned too, like pass all this extra context and everything else inside of these and switch off of all the conditions.
[1536.90 --> 1540.66]  You just write it top to bottom, and you can see what the control flow looks like.
[1540.66 --> 1545.86]  And it's a lot simpler for some of those complex cases to just spell it out for yourself.
[1546.40 --> 1550.54]  You know, sometimes an if statement is more than you need.
[1550.80 --> 1552.54]  You don't always need polymorphism.
[1553.14 --> 1557.30]  You know, like sometimes an if statement is perfectly valid.
[1557.30 --> 1560.16]  All right, sometimes an if statement is just an if statement.
[1560.16 --> 1561.18]  It's just an if.
[1561.32 --> 1563.38]  Just write the if statement, guys.
[1563.42 --> 1563.94]  It's all good.
[1564.84 --> 1570.68]  All right, so to keep this thing kind of tight because often we end up discussing for way too long.
[1571.08 --> 1571.80]  There is one more.
[1571.88 --> 1573.66]  You can't go too long on the stand-up.
[1573.76 --> 1574.64]  It's literally the whole –
[1574.64 --> 1575.88]  Well, Carson may have to go.
[1576.62 --> 1576.98]  Oh, yeah.
[1577.92 --> 1578.54]  No, I'm good.
[1578.80 --> 1581.84]  No, we're trying to – remember, we're just trying to generally keep episodes to 30 minutes.
[1582.28 --> 1582.52]  What?
[1582.52 --> 1582.96]  That's not true.
[1582.96 --> 1585.18]  I don't want to accidentally be an hour and a half on one topic.
[1585.18 --> 1586.30]  Okay, well, I don't know –
[1586.30 --> 1586.60]  Me neither.
[1587.30 --> 1587.42]  Okay.
[1588.54 --> 1589.46]  Relax, Prime.
[1589.46 --> 1591.26]  I've got it slotted in for an hour, buddy.
[1591.36 --> 1591.50]  Relax.
[1591.82 --> 1592.92]  You know what the problem is, Prime?
[1592.96 --> 1593.90]  You're not in a bathrobe.
[1594.12 --> 1596.78]  I feel like I don't have bathrobe mentality right now.
[1596.78 --> 1597.86]  You need bathrobe energy.
[1598.02 --> 1599.96]  Big bathrobe is coming for you, Prime.
[1600.18 --> 1602.62]  YouTube, leave a comment if you want this to be an hour.
[1603.00 --> 1604.48]  Leave a comment if you want this to be an hour.
[1604.60 --> 1604.78]  Yeah.
[1605.16 --> 1606.66]  Okay, well, maybe I'm wrong.
[1607.18 --> 1613.60]  But the real question I have for you, because you said you don't like unit tests as a means to drive development.
[1613.60 --> 1614.04]  Yeah.
[1614.04 --> 1623.64]  My only, I guess, counter for that is that I really like any form of testing that I can drive a feature that I find too complicated to write once.
[1623.64 --> 1628.46]  Meaning that if you just ask me to, like, sum a list of elements, I'm not going to test it.
[1628.58 --> 1629.48]  I'm just not going to do that.
[1629.52 --> 1631.44]  I'm just going to write a for loop and sum the thing.
[1631.54 --> 1632.90]  Like, that's what I'm going to do.
[1632.90 --> 1638.18]  And so there's a lot of logic I just simply don't test because it is stuff I can write one shot.
[1638.28 --> 1641.02]  And if there ends up being a bug in it, it's pretty straightforward.
[1641.58 --> 1644.24]  It's, like, not something that I need to worry too heavily about.
[1644.48 --> 1650.00]  But every now and then you get into these situations where you're just like, okay, this is actually a pretty complicated state to transform.
[1650.36 --> 1652.42]  And it's also complicated to get running.
[1652.60 --> 1654.48]  So I want this to be a unit test.
[1654.54 --> 1661.66]  I want to be able to drive the development of this via a unit test, not because I love TDD or that I'm even writing the test first.
[1661.66 --> 1664.48]  I just don't want to have a bad development cycle.
[1665.10 --> 1673.50]  And so that's kind of my only defense or against what you said about don't use unit tests is that I just like it for the implementation side when it's too hard.
[1674.12 --> 1674.60]  Yeah.
[1675.30 --> 1677.82]  It's always dangerous because I don't want to come across as anti.
[1677.94 --> 1679.70]  I'm a huge fan of testing.
[1680.44 --> 1680.86]  No, you're not.
[1681.12 --> 1682.14]  You can just admit it here.
[1682.22 --> 1682.90]  It's okay, Carson.
[1683.84 --> 1687.88]  And I think, you know, one thing that's tough here is the language.
[1688.06 --> 1688.94]  Like, what's a unit?
[1688.94 --> 1693.24]  You know, and like you'll get people that it's just it means whatever it means anything.
[1693.42 --> 1693.54]  Okay.
[1693.60 --> 1697.32]  Well, if everything's a unit test, then nothing's a unit test type situation.
[1697.42 --> 1698.48]  It tests my whole product.
[1698.68 --> 1699.48]  That's one unit.
[1701.14 --> 1703.84]  The smallest unit we have is the product.
[1704.26 --> 1704.74]  Right.
[1704.74 --> 1714.36]  So, you know, these unfortunately, these things can often devolve into just like miscommunication around definitions, which is just that's the Internet.
[1714.92 --> 1716.36]  Why else even be here?
[1716.58 --> 1718.26]  Honestly, we're not going to argue about terms.
[1718.26 --> 1719.58]  We're not going to argue definitions.
[1719.58 --> 1730.96]  But I think like what I would say is like when I say I'm not a huge fan of TDE and unit test, I mean it in the sort of the original sense that you were talking about, which is I'm writing a solution to a problem.
[1731.28 --> 1735.28]  And I'm going to like write one method and then I'm going to exhaustively test that method.
[1735.38 --> 1738.34]  And then I'm going to write another method and I'm going to exhaustively test that method.
[1738.34 --> 1744.10]  And then I'm going to eventually get to like, okay, now I've got my solution because every method does exactly what I expect.
[1744.42 --> 1753.40]  And then maybe I'll maybe write some what I would call integration tests, which is like calling the more high level methods that maybe invoke three or four things.
[1753.40 --> 1756.86]  Or if you're a fan of larger functions, a function that does quite a bit.
[1756.92 --> 1764.32]  There's not really a unit, you know, and at least in my opinion on that, given the way it's typically used by TDD advocates.
[1764.32 --> 1775.82]  So what I prefer to do is like, and I think this is kind of getting at what you're talking about, which is, and so much of this depends on where you are in the software development cycle.
[1776.08 --> 1780.08]  Like when you're first starting out, you have no idea what the solution is typically.
[1780.08 --> 1782.86]  If it's like a new feature, you just don't have any idea.
[1783.22 --> 1784.50]  You don't understand the concepts.
[1784.64 --> 1786.46]  You don't understand what the domain looks like.
[1786.48 --> 1788.28]  You don't understand what the API should look like.
[1788.28 --> 1793.60]  And so you need to like play around and like find like what's the core ideas here.
[1793.60 --> 1797.30]  And then so, you know, in my GrugBrain essay, I call that a cut point.
[1797.30 --> 1799.38]  Like you find like, okay, here's the API.
[1799.50 --> 1800.38]  Like this is the API.
[1800.50 --> 1801.80]  This is what this thing is going to do.
[1801.94 --> 1810.08]  And then I would say exhaustively test that, which is getting at what you're talking about, Prime, where it's like, okay, I really need to like hammer this down.
[1810.14 --> 1814.62]  But I'm not going to look at the functions and test every individual function necessarily.
[1814.74 --> 1816.94]  Instead, I'm going to focus on the higher level.
[1817.14 --> 1819.02]  What I, again, I would call these integration tests.
[1819.02 --> 1822.74]  I'm going to focus on the higher level API for this system.
[1822.74 --> 1824.68]  And then I'm going to exhaustively test that.
[1824.76 --> 1827.98]  I'm going to try and get all the corner cases as best I can when I'm doing that.
[1828.02 --> 1829.70]  And so that's one approach.
[1829.80 --> 1831.80]  There are times when TDD makes sense.
[1831.80 --> 1836.94]  Like if you're going in and adding like a really small feature to a huge, like existing code base.
[1837.04 --> 1837.42]  Okay.
[1837.42 --> 1840.00]  Like is there an existing set of unit tests?
[1840.32 --> 1840.56]  Yes.
[1840.66 --> 1840.88]  Okay.
[1840.88 --> 1844.32]  Then do a unit test for that one small piece of functionality.
[1844.80 --> 1854.42]  And if there isn't unit tests for it, like maybe you need to go back and add these integration tests before you add that feature so you're sure you're not screwing things up.
[1854.42 --> 1863.00]  So it's just, I guess, and this gets back to what we sort of said at the start, which is like there's this ideological approach to coding.
[1863.42 --> 1865.04]  It's like do this.
[1865.34 --> 1868.66]  And it's like, no, like so many things are situational.
[1868.98 --> 1871.26]  I know no one wants to hear it depends, but it does.
[1871.34 --> 1872.24]  It depends on stuff.
[1872.36 --> 1876.96]  Like if you go into a code, like, okay, you know, object oriented programming versus functional programming.
[1877.26 --> 1882.52]  Well, if I go into a functional code base, I'm not going to impose object oriented programming on top of it.
[1882.52 --> 1884.86]  I'm going to be a functional programmer and vice versa.
[1885.16 --> 1891.38]  Like, you know, you got to vibe match the code base if there's a lot of code or you're just going to be a wreck and you're going to make things worse.
[1891.92 --> 1904.14]  So, so much of this advice is, that's, I guess, like my big meta point here is like there's a lot of advice that's like not bad in, you know, in a lot of cases, but it's just too ideological and it's too easy to over apply it.
[1905.64 --> 1907.84]  It may also put the focus in the wrong place.
[1907.84 --> 1918.00]  Because that's often what I say about auditory programming, for example, is I'm like, you may end up with objects as you are programming because that's the natural, like you'll find natural places where those things occur.
[1918.00 --> 1926.44]  The problem with the way that it's taught, at least in my opinion, is that you end up in situations where programmers, I just, I see this.
[1926.58 --> 1929.38]  Programmers are hyper focused on needing to create objects.
[1929.52 --> 1934.40]  It's like, it's now become an activity in their head that is like the end in and of itself.
[1935.06 --> 1938.70]  But that's like objects for object's sake don't do anything for you, right?
[1938.76 --> 1944.26]  They only make sense if they take on a particular structure that is beneficial to the code base.
[1944.26 --> 1949.64]  And so it's one of those things where you're just like, look, the problem is the focus sometimes.
[1950.12 --> 1954.52]  The problem is, it's like we were saying, maybe it is good advice to have.
[1954.66 --> 1956.20]  Sometimes this function was too long.
[1956.30 --> 1957.58]  We should break it into smaller functions.
[1957.80 --> 1958.96]  That could be very true.
[1959.36 --> 1960.56]  It could also be very false.
[1960.90 --> 1966.10]  The point is to learn what the metrics are is do you want this thing at this time?
[1966.26 --> 1968.28]  It's that's part of learning to be a good programmer.
[1968.28 --> 1972.56]  And anyone who says, oh, it's just this rule is usually wrong, right?
[1972.66 --> 1976.98]  Unless there's something that's so bad we can tell you don't ever do this one thing, right?
[1977.30 --> 1979.32]  But, you know, that's what goes around.
[1979.34 --> 1980.46]  Do not nest ternary statements.
[1981.64 --> 1983.78]  Yeah, even I don't nest ternary statements.
[1983.94 --> 1985.28]  And I like ternary statements.
[1985.48 --> 1986.00]  I do too.
[1986.14 --> 1987.54]  That's probably a safe one to say.
[1987.74 --> 1988.44]  That's a safe one.
[1988.50 --> 1989.28]  There's always one.
[1989.38 --> 1990.48]  And that is the safe one.
[1990.56 --> 1992.18]  And also don't use repeat until.
[1992.18 --> 1992.38]  It's statements, baby.
[1992.86 --> 1994.34]  Repeat until the devil's loop.
[1994.94 --> 1996.64]  Do while the Lord's loop, okay?
[1997.10 --> 1998.24]  It's very, very obvious.
[1999.38 --> 2007.18]  I was going to say I just had one quibble with Casey's thing of saying, like, you know, creating objects for object's sake doesn't do anything.
[2007.34 --> 2012.08]  It does give you a chance to make significant performance improvements in Q2.
[2013.12 --> 2016.98]  So that's like you've got to be thinking a little bit bigger, Casey.
[2017.34 --> 2020.82]  Like, there's you've got to be thinking, oh, I could remove these objects later.
[2020.82 --> 2021.26]  Okay.
[2021.50 --> 2022.38]  Oh, baby.
[2022.60 --> 2023.08]  Speed up.
[2023.20 --> 2023.82]  Here we come.
[2024.06 --> 2024.42]  I see.
[2024.42 --> 2026.94]  You got the plan for what you're doing when you're on vacation.
[2027.32 --> 2027.56]  Exactly.
[2027.56 --> 2030.06]  This is Silicon Valley mindset right there.
[2030.16 --> 2030.50]  That's what that is.
[2030.50 --> 2033.20]  You are not bathrobe maxing like me, Casey.
[2033.20 --> 2033.54]  I agree.
[2033.54 --> 2035.00]  You can't possibly understand.
[2035.16 --> 2035.70]  But that's okay.
[2036.02 --> 2036.32]  Yep.
[2036.44 --> 2036.80]  All right.
[2037.18 --> 2037.36]  Yeah.
[2038.82 --> 2039.50]  Fair enough.
[2039.84 --> 2046.60]  To be also to kind of double click on yours, Carson, with this whole unit versus all this, I use the term unit.
[2046.60 --> 2048.98]  But really, in my head, there's only actually two sides.
[2048.98 --> 2050.62]  There's end to end.
[2050.72 --> 2055.06]  Like, I actually start up the whole program and kind of black box the entire thing.
[2055.44 --> 2061.44]  Or I'm trying to unit test some easy startup and go, and I just call that a unit, despite it not being like literally just a function.
[2061.60 --> 2062.58]  It could be many functions.
[2062.68 --> 2064.24]  It could be a function that calls many functions.
[2064.82 --> 2065.56]  And I, you know what?
[2065.74 --> 2068.78]  This whole idea of having, I don't know the difference between like functional integration.
[2068.78 --> 2074.10]  I don't know when unit becomes functional and when functional becomes integration and when integration becomes end to end test.
[2074.24 --> 2081.36]  I just like the idea of there's the whole thing, and then there's just like some discrete unit, and that's it.
[2081.72 --> 2082.08]  Yeah.
[2082.26 --> 2087.78]  You use the difference in the terms whenever you want to make your opponents things look bad, right?
[2087.82 --> 2088.26]  Exactly.
[2088.50 --> 2089.60]  That's what's infuriating.
[2091.98 --> 2094.96]  See, what you were writing there, that's a functional test.
[2094.96 --> 2095.46]  But that isn't really a unit, man.
[2095.58 --> 2097.34]  Real unit testing hasn't been tried.
[2097.34 --> 2101.06]  Yeah, and so you can get them with that, and you'll instantly win.
[2101.28 --> 2104.08]  Like, once again, you're not bathrobe maxing on this, Brian.
[2104.96 --> 2112.12]  Maybe that's my problem is that I haven't lived the bathrobe life, and once I do, so many new parts of my mind will open up.
[2112.14 --> 2115.22]  It's kind of like taking LSD for the first time, except without all the consequences.
[2115.50 --> 2118.18]  It's just all the mind-opening experience.
[2119.26 --> 2121.08]  I just don't have a bathrobe-opening experience.
[2121.16 --> 2121.86]  That's all I ask.
[2122.44 --> 2124.58]  This is as close as I get to LSD.
[2127.34 --> 2133.06]  Yeah, one thing I should say about end-to-end tests, I love end-to-end tests, and they're really important.
[2133.28 --> 2138.28]  But that's an area where you have to be super disciplined about not overdoing end-to-end tests.
[2138.46 --> 2142.46]  I've been in multiple companies where our end-to-end test suite got too big.
[2143.08 --> 2146.68]  And the Grug Brain essay, there's a section on testing, and I mentioned that.
[2146.68 --> 2158.12]  You need to have an end-to-end test suite, but that needs to be religiously maintained, and it has to focus on the most important things in your app.
[2158.18 --> 2164.14]  Because if you add too many, they become non-deterministic, and then they start breaking, and people stop paying attention to them.
[2164.20 --> 2167.84]  And they're absolutely the best canary in the coal mine you can have.
[2167.84 --> 2169.96]  So there's that balance.
[2170.12 --> 2172.26]  People are like, oh, end-to-end tests are good.
[2172.34 --> 2173.18]  Let's have more of them.
[2173.20 --> 2175.52]  And it's like, no, no, you've got to be balanced about this stuff.
[2175.72 --> 2179.40]  You can't overdo your end-to-end test suite, or it becomes less valuable.
[2180.24 --> 2183.50]  And it's just one of those weird things you've just got to figure out.
[2183.90 --> 2191.00]  And they're also disproportionately harder when it comes to any sort of data or service refactor.
[2191.54 --> 2194.70]  Like any of those, it's a lot more work to get anything done.
[2194.70 --> 2201.32]  Yeah, like when you've got a big system refactor, they can be absolutely crucial to like, okay, we didn't break the whole system.
[2201.60 --> 2205.42]  But if you have too many of them, or if you don't have enough of them, it's just tough balance.
[2205.64 --> 2208.98]  Or you're testing the wrong outputs, too.
[2209.12 --> 2218.04]  It's really easy to be like, oh, I'm going to assert 75 things about internal state when we get done.
[2218.16 --> 2221.32]  And you're like, oh, now you really are locked into that.
[2221.32 --> 2226.18]  It's going to be very hard to like, make a change and assert the behaviors the same.
[2226.18 --> 2234.18]  Because it's not clear which thing is actually like, behavior versus random stuff you kept at the end of your thing.
[2234.18 --> 2239.96]  This is one of the things that like, I see a lot why I get really annoyed with like, AI generated tests.
[2239.96 --> 2252.64]  Is they like, at least from all the ones that I've seen people do both in demos and in practice is like, they really assert a lot about the internal state of things and are tightly coupled to the integration.
[2252.64 --> 2257.64]  And it's like, dude, if you ever want to change anything, all your tests will break every single time.
[2257.82 --> 2261.88]  Like you won't get any of the good feelings of knowing the system still works.
[2261.88 --> 2265.10]  Because you broke everything every time you change them.
[2265.34 --> 2271.06]  That's kind of unfortunate because AI should be like, AI should be leading the way in not doing that.
[2271.14 --> 2275.08]  It's like, dude, you've got something that can literally parse the screen visually.
[2275.50 --> 2283.14]  Why are you testing internal state instead of looking to see whether the program produced the correct, even graphical output if you wanted to?
[2283.14 --> 2286.12]  That would be an incredibly beneficial feature, right?
[2286.20 --> 2295.92]  So it's like, you would want AI, hopefully, I assume we'll get there or someone already has, but just not widespread to get to the point where the AI testing is actually really helpful.
[2296.06 --> 2300.94]  You can just be like, oh, here's what the program looks like when we run it normally, right?
[2301.02 --> 2305.68]  And remember that and tell me if it ever stops doing this, right?
[2306.00 --> 2307.24]  You know, like tell me.
[2307.62 --> 2310.78]  And then, you know, hopefully it can do that at some point pretty well, right?
[2310.78 --> 2312.74]  Yeah, there are some cool solutions to that.
[2313.14 --> 2315.42]  I've used before, but they're not like AI.
[2315.70 --> 2317.84]  They do other stuff for it mostly, but.
[2318.38 --> 2321.68]  Yeah, I mean, we've had things like OCR and edge detection, things like that.
[2321.72 --> 2326.96]  So it's not like you couldn't do graphical testing before, but it's like this would make it a lot faster for people to create, right?
[2326.98 --> 2328.16]  They could create anything.
[2328.28 --> 2332.94]  You know, in games we have this problem a lot where it's like, how do you make tests for the end product?
[2332.94 --> 2335.92]  Because it's kind of hard to know what it should look like.
[2336.22 --> 2340.36]  Well, an AI could easily do things like, you know, play the game, find some things, look at things.
[2340.36 --> 2341.92]  Oh, that object fell off.
[2341.98 --> 2343.28]  It's not supposed to fall off that thing.
[2343.52 --> 2348.80]  You know, I could imagine things like that that were very hard to create tests for before that maybe AI could help with.
[2348.88 --> 2351.52]  I mean, I can't say for sure that it will, but it could, right?
[2351.70 --> 2351.82]  So.
[2352.04 --> 2352.18]  Yeah.
[2352.58 --> 2352.86]  That's all.
[2352.86 --> 2369.54]  I do think the thing, it's hard because like business, I don't know, constraints and outcomes can change, but it is kind of nice if you write like a test that is associated with the actual like business out business logic outcome that you want.
[2369.54 --> 2372.92]  Because then if that changes, then it's okay to delete the test, right?
[2372.98 --> 2378.76]  You know, for sure, like, oh, we were supposed to calculate tax on this and then the rules change and we aren't.
[2378.84 --> 2380.26]  You're like, yeah, cool.
[2380.54 --> 2380.76]  Okay.
[2380.78 --> 2384.70]  Well then I need to delete the test because it's lying now.
[2384.82 --> 2385.74]  Like that's good.
[2385.86 --> 2391.34]  And I think a lot of times people don't actually test kind of like the requirements or the constraints of the system.
[2391.34 --> 2399.10]  They just test like whatever pops into their mind or like random boundary points.
[2399.42 --> 2406.20]  You know, that's another important point that, and I make, and it's not in the Grug Brain essay, but it's in the Code and Dirty essay.
[2406.94 --> 2411.16]  Like test suites, they take on their own mass.
[2411.16 --> 2419.54]  And like, if you have too many tests, like you got to be careful with it because the tests sort of force you to, you're committed.
[2419.54 --> 2422.80]  And it's like, I can't make this change because I'm going to just break a bunch of crap.
[2422.96 --> 2428.24]  And so that's why, like I say, like sometimes it's better to just throw the unit tests away and keep the high level tests.
[2428.44 --> 2437.10]  Like the test at the highest level you can get away with, because the higher level those tests are, the longer those invariants about the system stay true.
[2437.20 --> 2439.82]  And then you have flexibility at a lower level.
[2439.82 --> 2444.98]  If you've got a thousand unit tests for every single function in some, you know, code module, like you're not going to change it.
[2445.24 --> 2445.88]  Like you're just not.
[2446.00 --> 2451.20]  That's just, it's just this, it leans on you in a way that, you know, people I think don't appreciate.
[2451.40 --> 2456.56]  And again, this is something where like testing is good, but too much of it can be bad and doing it, you know.
[2456.66 --> 2459.22]  And so I think you have to be really careful with these things.
[2459.84 --> 2461.82]  It gets back to a cost benefit analysis.
[2462.00 --> 2468.00]  The reason that you, that tests, the only reason tests can be good is if they benefit you more than they cost, right?
[2468.00 --> 2478.00]  They're making, you know, less bugs show up in production that were harder to find, or they're preventing some catastrophic thing from happening, or they're making development quicker because you don't have as many bugs during development, whatever it is.
[2478.38 --> 2486.00]  If you go too far, the cost of the tests starts outweighing the cost of the bugs that you are finding, right?
[2486.00 --> 2490.48]  And so when you've hit that point, now you're just doing bad engineering, right?
[2491.22 --> 2498.90]  Making the project cost more because you were testing it is not a plus if it doesn't actually produce more reliable software at the end.
[2498.98 --> 2504.98]  So you have to make sure you're hitting that, you're hitting that programmer time is zero sum is the way to say it.
[2505.48 --> 2508.20]  Time they're spent writing tests is not time they're spent writing the code.
[2508.44 --> 2513.96]  If you've, if you've got that cost benefit tradeoff incorrect, you're actually hurting the project, not helping it.
[2513.96 --> 2520.06]  And you have, so you have to be intelligent about where you put your tests, how you write them, just like you do for regular code.
[2520.14 --> 2525.52]  You have to have a good idea, a good sense of what should be taking your time and what shouldn't be right.
[2525.96 --> 2532.56]  To be, to be completely fair, you know, CrowdStrike really tested all their stuff.
[2532.86 --> 2533.08]  Yeah.
[2533.18 --> 2534.66]  They had a lot of tests.
[2534.70 --> 2540.28]  They had many, many tests, but they managed to turn off the world for like a week.
[2540.28 --> 2541.82]  And so that was a real thing.
[2541.92 --> 2545.02]  So it just, you know, not, not all tests are valuable.
[2546.36 --> 2546.72]  Yeah.
[2546.82 --> 2556.06]  And I think you mentioned this when we had our episode on testing prime, you were like, you know, shipped to a very small number of people and be very careful about that as you staged rollouts.
[2556.06 --> 2556.36]  Right.
[2556.36 --> 2567.92]  And like the CrowdStrike is why it's like, look, the slower you can roll these things out, which in their case, I guess they just didn't feel like they could do it any slower because it's, you know, it's, you're trying to stay ahead of zero day stuff or whatever.
[2567.92 --> 2576.42]  But the slower you can roll things out, the easier it is for you to get those canaries early and not ruin 100% of your users' lives by something you didn't catch.
[2576.56 --> 2576.66]  Right.
[2577.08 --> 2577.30]  Yeah.
[2577.36 --> 2581.96]  And I think a really good thing to always remember is that tests catch bugs that are known.
[2583.64 --> 2583.76]  Yeah.
[2583.76 --> 2587.30]  They're not a blanket for catching things that do not, that you do not know about.
[2587.54 --> 2587.68]  Yeah.
[2587.76 --> 2593.58]  Things that are too subtle for you to have thought of, you may just well not catch in a test because you didn't think to check for that.
[2593.66 --> 2593.78]  Right.
[2593.82 --> 2594.40]  Yeah, exactly.
[2594.54 --> 2596.12]  They only test for things that have been discovered.
[2596.12 --> 2599.80]  There's still plenty of, there's still plenty of them lurking about that you just haven't figured out yet.
[2600.72 --> 2604.70]  Hey, so Carson, you are kind of known as a meme master.
[2606.26 --> 2606.74]  Okay.
[2606.74 --> 2616.82]  In fact, I've heard that every time you have a meme that doesn't hit great on Twitter, you whisper to a mutual friend of ours.
[2617.80 --> 2618.32]  What?
[2618.58 --> 2622.00]  A quotation from Jesus, which is, I believe Jesus.
[2622.00 --> 2633.44]  It could be, hey, it could be, it could be Solomon, but that you say that you do not throw your pearls before the swine because they just did not quite, they did not quite get the meme and the meme was not good enough.
[2633.94 --> 2635.18]  And so you are a meme master.
[2636.46 --> 2636.82]  Yeah.
[2637.22 --> 2639.92]  Well, no, I don't agree with that, but I do, I do make memes.
[2640.42 --> 2641.40]  Don't even lie to me.
[2641.66 --> 2642.82]  We've already talked about this.
[2642.82 --> 2646.14]  You've already said that the only time you're super serious is when you're about to make a joke.
[2646.24 --> 2646.70]  It's time.
[2647.00 --> 2649.76]  It's time to be super serious to make this joke.
[2651.00 --> 2653.06]  He sent you those in confidence, Brian.
[2653.50 --> 2653.56]  Like.
[2655.22 --> 2655.58]  Okay.
[2655.72 --> 2656.66]  Maybe I'm that friend.
[2656.92 --> 2657.94]  Maybe I'm the mutual.
[2658.46 --> 2658.56]  But.
[2658.78 --> 2659.94]  You should have known better, Carson.
[2660.08 --> 2661.88]  He's literally known as the leakagen.
[2662.20 --> 2662.38]  Yeah.
[2662.46 --> 2663.86]  Maybe I did know better, Teej.
[2664.18 --> 2664.36]  Yeah.
[2664.36 --> 2665.22]  Maybe I did know better.
[2665.56 --> 2665.78]  Yeah.
[2665.78 --> 2669.18]  Maybe he's, maybe this is a, you know, 40 chess move, Teej.
[2669.38 --> 2669.72]  Yeah.
[2670.24 --> 2672.34]  I'm just trying to sell Greg brain books, man.
[2672.62 --> 2673.38]  That's all I'm doing here.
[2674.42 --> 2675.46]  Here's the deal, Teej.
[2675.80 --> 2676.08]  Yeah.
[2676.44 --> 2677.12]  Oh, well.
[2677.16 --> 2677.46]  Yeah.
[2677.62 --> 2678.38]  Teej, what was that?
[2678.46 --> 2680.30]  Oh, you don't have the latest edition, Teej.
[2680.48 --> 2681.56]  I figured you wouldn't.
[2682.14 --> 2682.76]  Not a big deal.
[2682.78 --> 2684.12]  There's an updated version of this?
[2684.68 --> 2687.10]  There's a soft cover, which is, I got a sweet cover.
[2687.10 --> 2689.06]  It's like this pixel art, like.
[2689.42 --> 2689.76]  Oh, yeah.
[2689.80 --> 2691.48]  Everyone buy hypermedia.systems.
[2691.56 --> 2693.98]  And then go to gregbrain.dev and buy the book there, too.
[2694.20 --> 2694.92]  What's this book?
[2694.92 --> 2696.54]  Let's, let's do a quick little.
[2696.74 --> 2698.06]  Let's talk about that, actually.
[2698.20 --> 2700.42]  So, Carson, tell us about this book.
[2700.56 --> 2701.48]  I'm interested now.
[2701.58 --> 2702.36]  I didn't know about it.
[2702.94 --> 2707.74]  So, hypermedia.systems, you can go to hypermedia.systems and you can read it online for free.
[2707.88 --> 2709.94]  And then there's a hard cover and a soft cover.
[2710.16 --> 2710.94]  They're different covers.
[2711.12 --> 2714.66]  The hard cover was done by, it's now US graphics.
[2714.66 --> 2716.38]  It was Berkeley graphics at the time.
[2716.40 --> 2717.34]  Makes the best fonts.
[2717.66 --> 2718.10]  The best fonts.
[2718.26 --> 2719.52]  Yeah, he makes awesome fonts.
[2719.60 --> 2720.16]  Berkeley mono.
[2720.26 --> 2721.26]  I love that font.
[2721.40 --> 2722.50]  Berkeley mono is really good.
[2722.50 --> 2722.80]  Best font.
[2723.16 --> 2725.74]  And so, there's that.
[2725.80 --> 2726.54]  And then the soft cover.
[2726.62 --> 2727.38]  Prime, hold that one up.
[2727.44 --> 2728.28]  That one's really good, too.
[2728.36 --> 2728.82]  Do you have that?
[2729.02 --> 2729.40]  Yeah, yeah.
[2729.56 --> 2730.38]  I have that one.
[2730.96 --> 2732.04]  It's mirrored right now.
[2732.40 --> 2733.56]  But it's blurry.
[2733.72 --> 2734.90]  I'd have to go manually adjust it.
[2734.96 --> 2735.76]  Yeah, but that's pretty cool.
[2735.86 --> 2736.52]  That was also sick.
[2736.52 --> 2741.24]  And then you can, so anyways, it's a book basically on HT, it's three sections.
[2741.62 --> 2745.10]  And it's basically, you know, HTMX is sort of hypermedia oriented.
[2745.34 --> 2749.56]  And so, like, the first section is like, hey, kids, here's how the web actually works.
[2749.82 --> 2750.08]  Okay.
[2750.34 --> 2750.60]  Okay.
[2750.62 --> 2752.44]  Here's how hypermedia actually worked.
[2752.44 --> 2755.68]  Like, it's a web 1.0 style app.
[2755.78 --> 2756.84]  And we build that out.
[2756.92 --> 2760.78]  And then the middle chapters are like, okay, we've done that.
[2760.90 --> 2762.78]  Like, let's make it better with HTMX.
[2762.82 --> 2767.74]  Let's improve it sort of incrementally with HTMX, which is building on the same idea as
[2767.74 --> 2772.34]  sort of the hypermedia, you know, fundamentals of the web, I guess is what I'd say.
[2772.34 --> 2781.86]  And then the last section is on a mobile hypermedia called HyperView, which is this guy, Adam Stepinski,
[2782.22 --> 2786.80]  I'm good friends with, he built a mobile hypermedia system, basically.
[2787.38 --> 2792.06]  And so that kind of is like, hey, just to show that hypermedia isn't only about the web,
[2792.18 --> 2796.70]  like, here's a cool thing that sort of gives you the nice thing about HyperView is like,
[2796.72 --> 2801.38]  you don't have to update your, you don't have to update your mobile app on the app store
[2801.38 --> 2803.16]  to get an update out to your users.
[2803.42 --> 2807.26]  It sort of leverages the same deployment model that the web does.
[2807.76 --> 2811.12]  And who would you say is the best target audience for the book?
[2811.98 --> 2817.96]  I think it's, I wrote it for younger web developers, like people who, but I think a lot of, you know,
[2818.06 --> 2821.44]  to be honest, like a lot of the older guys like it because it's like, oh, I remember this.
[2821.48 --> 2821.96]  This is cool.
[2822.28 --> 2827.14]  But it was sort of written for the younger developers who came of age in the last decade
[2827.14 --> 2828.60]  when it's just like, here's React.
[2828.60 --> 2831.76]  And like, all it is, is like React and JSON APIs.
[2831.92 --> 2832.76]  And that's what you're used to.
[2832.82 --> 2837.74]  And so you don't have this like sort of background in like how the web was designed
[2837.74 --> 2840.90]  and how hypermedia, like what is hypermedia?
[2840.98 --> 2842.10]  What's special about it?
[2842.14 --> 2846.54]  Like why was the web so effective in growing as a distributed system
[2846.54 --> 2848.54]  versus other distributed systems?
[2848.54 --> 2853.74]  And a lot of that boils down to what is called the uniform interface of the web.
[2853.74 --> 2857.82]  And so you can read the book and there's some essays too about it.
[2858.12 --> 2858.14]  So.
[2859.36 --> 2860.04]  All right.
[2860.38 --> 2862.48]  I'd say it's like, I read it.
[2863.72 --> 2864.52]  It's 2025.
[2864.92 --> 2866.66]  What Carson, that had to be like a year and a half ago.
[2866.72 --> 2870.32]  It was just right when I started talking about HTMX first time.
[2871.08 --> 2872.48]  And I thought it was awesome.
[2872.48 --> 2877.42]  Like it's very interesting to think about a bunch of different options that you have like out in the web.
[2877.42 --> 2880.84]  And then it was cool because I just didn't want to write JavaScript all the time.
[2881.06 --> 2885.32]  So it was fun to explore using HTMX like with different backend languages.
[2885.60 --> 2892.10]  And then you could still have a website that didn't reload the whole page anytime you wanted to do something,
[2892.10 --> 2895.20]  which is like terrible UX.
[2895.20 --> 2901.80]  And it's sad that browsers haven't found a way to give people that tool separately.
[2902.36 --> 2902.84]  Yeah.
[2903.54 --> 2903.90]  All right.
[2903.90 --> 2909.58]  So as a meme master, the reason why I said that is because I believe Casey ran into a bit of trouble.
[2910.36 --> 2910.52]  Yeah.
[2910.64 --> 2913.40]  So I wanted to talk to you guys about this.
[2913.48 --> 2916.76]  And I didn't know Carson was going to be on, nor did I know that he was a meme master.
[2916.90 --> 2919.62]  So this turns out to be extra appropriate that we're doing it today.
[2919.62 --> 2925.14]  But it's just something that I know at least like Prime and TJ already knew you guys.
[2925.34 --> 2927.44]  I mean, you're out there on the social medias.
[2927.96 --> 2932.82]  You know how to get the crowd engaged in a meme.
[2932.82 --> 2935.24]  I get a lot of likes on the Facebook.com.
[2935.36 --> 2935.72]  Yeah, exactly.
[2935.72 --> 2940.90]  I mean, you're all over the Facebook.com, the MySpace, some of these up and coming platforms.
[2941.10 --> 2942.12]  Way more than five friends.
[2942.72 --> 2947.32]  So I felt like it was a good time to talk about a personal experience that I had.
[2947.94 --> 2950.16]  Please tell me it's bird sex, bird sex spiral.
[2950.76 --> 2952.62]  Sadly, you know, I wish that it was.
[2952.86 --> 2953.10]  Okay.
[2953.10 --> 2955.46]  I wish that it was, but unfortunately it wasn't.
[2955.96 --> 2967.10]  And I want you to sort of cast your mind back quite some time to sort of the era when...
[2967.10 --> 2975.22]  I don't want to say a bad thing about Microsoft, but obviously as the web was sort of ascendant,
[2975.22 --> 2979.80]  you had FAANG, you noticed the F-A-A-N-G acronym was there.
[2980.14 --> 2982.42]  There's no M in that acronym, right?
[2982.46 --> 2982.68]  Correct.
[2982.84 --> 2984.52]  Microsoft was not the hotness.
[2984.76 --> 2985.86]  The web was taking over.
[2986.00 --> 2989.94]  They were kind of considered this older player that's not that relevant anymore.
[2990.20 --> 2993.66]  Like, if anything, I just use Windows to launch a browser, right?
[2993.66 --> 3001.46]  And so they had to start becoming cool because all of the new recruits, right, all of the
[3001.46 --> 3005.72]  summer interns who were coming out of college, who people were trying to hire, they're all
[3005.72 --> 3006.38]  going to Google.
[3006.52 --> 3007.60]  They're all going to Amazon.
[3007.90 --> 3008.88]  They're all going to Apple.
[3009.06 --> 3010.90]  They're not going to Microsoft, right?
[3012.16 --> 3016.78]  So back in the day, and this is maybe five or six years ago, I think, right?
[3017.30 --> 3023.24]  Back in the day, for some unknown reason, probably driven by this situation I was just talking
[3023.24 --> 3023.58]  about.
[3024.84 --> 3031.12]  They, one of their recruiters went ahead and sent this memo, and I'm posting it to Twitter
[3031.12 --> 3032.66]  right now as promised, Prime.
[3033.26 --> 3034.58]  Oh, I was hoping you're going to put it on your screen.
[3034.70 --> 3036.26]  I made you full screen for this moment.
[3036.90 --> 3037.80]  No, no, no, no.
[3037.88 --> 3039.26]  This is going to go out for everybody.
[3039.42 --> 3040.80]  You can do this, Prime, in fact.
[3040.88 --> 3041.88]  What's your Twitter account?
[3042.56 --> 3047.88]  It's CMuratori, C-M-U-R-A-T-O-R-I, and I will read you what this said.
[3047.88 --> 3055.64]  This is the email that one of their recruiters sent to all of the interns, and it says,
[3056.34 --> 3059.04]  hey, bae, intern, B-A-E, right?
[3059.42 --> 3063.64]  And it's got the little, yeah, that's the opening of the email, okay?
[3064.30 --> 3069.82]  It says, hey, bae, intern, and it has a little, it's got the party hat with the little testicles.
[3069.94 --> 3071.42]  I don't know what that emoji is supposed to be.
[3071.48 --> 3074.22]  It's like a less than followed by a three.
[3074.22 --> 3075.48]  That's a heart sign.
[3075.60 --> 3076.14]  It's not testicles.
[3076.14 --> 3076.52]  That's a heart, dude.
[3076.74 --> 3077.40]  Oh, it's testicles.
[3077.58 --> 3080.94]  I mean, when I see that, I see testicles with a party hat on, but fine.
[3081.04 --> 3081.54]  It's a heart.
[3081.72 --> 3083.36]  Hey, bae, intern, right?
[3083.46 --> 3085.68]  That's what she opened with, I guess.
[3085.86 --> 3089.64]  Or I guess I don't know anything about this recruiter, but he or she.
[3089.78 --> 3097.24]  We'll say they, because Kim, I actually know a guy named Kim, so I don't know exactly who the recruiter was.
[3097.92 --> 3101.58]  It says, hi, I am Kim, a Microsoft University recruiter.
[3101.58 --> 3110.60]  My crew is coming down from our HQ in Seattle to hang with you and the crowd of Bay Area interns at Internapalooza on 7-11.
[3110.90 --> 3121.16]  But more importantly, in green underline text, we're throwing an exclusive party the night of the event at our San Francisco office, and you're invited.
[3121.66 --> 3123.12]  And here's the money part right here.
[3123.12 --> 3135.40]  There will be hella noms, lots of dranks, D-R-A-N-K-S, the best beats, and just like last year, we're breaking out of the Yammer beer pong tables.
[3136.12 --> 3140.38]  The closing line is, all caps in orange for some reason.
[3140.62 --> 3141.06]  Scroll down.
[3141.06 --> 3144.32]  Hell yes to getting lit on a Monday night.
[3144.32 --> 3149.34]  Okay, so you got, do you have the idea now?
[3149.40 --> 3150.96]  Do you see what I'm talking about?
[3151.74 --> 3153.20]  Time, let's throw this party, dude.
[3153.34 --> 3154.08]  Let's throw this party.
[3154.08 --> 3155.68]  I think we should throw this party.
[3155.80 --> 3159.64]  Not only should we do this party in San Francisco, but I, dude, I know.
[3159.88 --> 3160.84]  Live stand-up episode.
[3161.26 --> 3161.66]  I know.
[3161.86 --> 3162.10]  I know.
[3162.10 --> 3162.84]  I think we should do this.
[3162.90 --> 3167.54]  But on top of it, you know that meme where it's the scientist holding up a green vial,
[3167.54 --> 3170.48]  and it's just like, I have distilled pure cringe?
[3170.90 --> 3171.00]  Yeah.
[3171.00 --> 3174.06]  This is what I'm currently experiencing right now.
[3174.08 --> 3178.24]  There are people in the chat that don't think that this came directly from Bill Gates,
[3178.32 --> 3180.98]  and it's just incredibly disappointing to me.
[3181.36 --> 3181.82]  Yeah, yes.
[3181.90 --> 3184.74]  If you think Bill Gates didn't write this, you're out of your mind.
[3184.80 --> 3185.94]  He wasn't there anymore.
[3185.96 --> 3187.48]  Bill Gates was like, here we go.
[3187.60 --> 3189.14]  No, this was not there.
[3189.16 --> 3190.28]  He's a shadow governor.
[3192.12 --> 3193.02]  Not there.
[3193.12 --> 3193.96]  Listen to this guy.
[3194.16 --> 3195.34]  This is Bill Gates.
[3195.34 --> 3196.62]  This is classic Bill Gates.
[3196.74 --> 3197.64]  All right, all right.
[3197.74 --> 3200.80]  Yeah, it's quote-unquote Kim, but we all know it's Bill Gates.
[3200.80 --> 3201.96]  It's Bill G, secretly.
[3202.66 --> 3205.54]  Yeah, where's the metadata on this email?
[3205.80 --> 3208.66]  Is there like an eventually from Bill G at Microsoft?
[3209.68 --> 3212.82]  Yeah, we need a Freedom of Information Act situation here.
[3213.22 --> 3219.36]  Okay, but separately before the meme, we should throw this party in San Francisco and do a live episode.
[3220.82 --> 3223.24]  Developers, developers, developers, developers.
[3223.24 --> 3224.66]  Did you see my recent one?
[3224.76 --> 3225.78]  I reenacted that, Carson.
[3225.88 --> 3226.42]  Did you see that?
[3226.42 --> 3227.06]  Are you serious?
[3227.24 --> 3227.32]  I didn't see it.
[3227.34 --> 3227.68]  I'm sorry.
[3227.80 --> 3228.74]  I did not see that.
[3228.74 --> 3230.18]  I went very, very deep on this.
[3231.58 --> 3232.60]  We'll play it at the end.
[3232.74 --> 3233.46]  Yeah, yeah, yeah.
[3233.48 --> 3234.66]  Please, I want to see that.
[3234.76 --> 3236.28]  I want to hear your meme now, though.
[3236.38 --> 3237.90]  Yeah, we'll do one meme at a time.
[3237.98 --> 3238.60]  Yeah, one meme at a time.
[3238.60 --> 3238.90]  Exactly.
[3239.04 --> 3239.70]  Smart, smart, smart, smart.
[3240.02 --> 3242.48]  So here's, and I'm just going to tell you what happened.
[3242.90 --> 3248.04]  And then, like I said, what I'd like is for you guys to explain to me, why did I screw up this meme?
[3248.10 --> 3250.26]  I felt like this should have been a slam dunk, okay?
[3250.26 --> 3252.66]  And I totally, and no one cared.
[3252.96 --> 3254.02]  I posted this on Twitter.
[3254.64 --> 3255.26]  No one gave.
[3255.26 --> 3255.86]  It's beautiful.
[3256.00 --> 3256.76]  This is so good.
[3257.08 --> 3257.30]  Okay.
[3257.76 --> 3259.50]  So here's what I thought to myself.
[3259.96 --> 3264.98]  I'm like, okay, hell yes to getting lit on a Monday night has got to be a meme.
[3265.12 --> 3266.38]  Like, that's got to be a meme.
[3266.46 --> 3267.70]  How does that not become a meme?
[3268.32 --> 3275.18]  So what I did, and this is obviously in the era before AI image generation, so I'm loading up, you know, an image editing package.
[3275.54 --> 3281.36]  And I go and I find a picture of Satya Nadella, who's the CEO at the time.
[3281.40 --> 3283.12]  So he's already taken over at this point.
[3283.16 --> 3283.96]  It's not Steve Ballmer.
[3284.50 --> 3285.54]  He's already gone.
[3286.74 --> 3289.38]  So I find a picture of...
[3289.38 --> 3290.78]  Dude, RIP Jack Johnson.
[3290.90 --> 3291.68]  That's all I got to say.
[3292.28 --> 3293.22]  Jack Johnson?
[3293.58 --> 3294.30]  Sorry, keep going.
[3294.56 --> 3294.74]  Okay.
[3295.44 --> 3295.88]  Sorry.
[3296.72 --> 3297.36]  Separate meme.
[3297.70 --> 3298.02]  Okay.
[3298.82 --> 3304.86]  So I find a picture of Satya Nadella giving a lecture, like giving one of his presentations as CEO.
[3305.46 --> 3315.00]  Where his hands, I like look for one where the hands are already in a position where I think it could be holding like one really big water bong.
[3315.40 --> 3315.60]  Right?
[3315.60 --> 3319.18]  I just look for something that's like close to that.
[3319.48 --> 3326.40]  I know I'm going to have to move the hands a little, but I want something pretty close to him holding like something real big.
[3326.40 --> 3328.86]  And like he's getting really lit on Monday night.
[3328.92 --> 3331.66]  He's not like slightly getting a little toasty.
[3331.74 --> 3332.90]  He's like going all the way.
[3333.02 --> 3333.16]  Okay.
[3333.16 --> 3335.02]  I do that.
[3335.68 --> 3337.38]  I find this.
[3337.38 --> 3340.26]  I find the craziest water bong I can.
[3340.72 --> 3347.66]  That's positioned like it's rotated such that it will go to his mouth correctly.
[3348.32 --> 3348.80]  Right?
[3348.80 --> 3351.08]  I photoshopped those two together.
[3352.52 --> 3354.98]  I even, I like comp the lighting, right?
[3355.02 --> 3356.16]  I work in computer graphics.
[3356.28 --> 3357.46]  So I'm like, so I comp the lighting.
[3357.62 --> 3358.68]  I try to get the shadowing right.
[3359.02 --> 3361.60]  I get this big old smoke plume.
[3361.98 --> 3363.58]  Like, so it's just cover it.
[3363.64 --> 3367.54]  Like, it's just, he is hitting this thing hard on stage.
[3367.54 --> 3371.46]  And I'm like, this is the greatest meme ever.
[3371.86 --> 3372.82]  Everyone's going to love it.
[3372.92 --> 3376.02]  I post it and no one cared.
[3376.76 --> 3377.82]  And here it is.
[3377.92 --> 3379.16]  I'm putting it in the reply.
[3379.70 --> 3380.00]  Okay.
[3380.54 --> 3380.98]  Yes.
[3381.12 --> 3381.98]  Put in the reply.
[3382.44 --> 3383.82]  And what did I do wrong?
[3385.60 --> 3387.00]  I'm pulling it up right now.
[3387.06 --> 3388.06]  I'm pulling it up right now.
[3388.14 --> 3389.52]  Where did you post it?
[3389.60 --> 3390.14]  Did you quote?
[3390.26 --> 3392.72]  How did you send this meme originally, Casey?
[3392.98 --> 3394.40]  I don't know.
[3394.54 --> 3395.78]  We'd have to go back and look.
[3397.70 --> 3398.14]  All right.
[3398.34 --> 3399.00]  Hold on.
[3399.68 --> 3400.04]  Hold on.
[3400.04 --> 3401.02]  It's so good, though.
[3401.12 --> 3402.40]  It is really good, Casey.
[3402.40 --> 3406.30]  I'm pretty sure if I just took the meme right now, I would get a thousand likes on it.
[3406.38 --> 3406.72]  Yeah.
[3406.82 --> 3407.92]  Just steal it.
[3408.08 --> 3408.82]  Steal it, Brian.
[3409.08 --> 3410.20]  Steal it quickly.
[3410.94 --> 3412.62]  Copy paste that to a brand new.
[3412.62 --> 3413.38]  There you go.
[3413.38 --> 3414.48]  I've already posted it.
[3414.56 --> 3415.54]  I've already posted it.
[3415.54 --> 3415.56]  Okay.
[3415.84 --> 3417.08]  Brand new tweet.
[3417.54 --> 3418.66]  Blow it up, boys.
[3418.96 --> 3419.24]  Yep.
[3419.28 --> 3420.12]  I'm doing it, too.
[3420.22 --> 3420.80]  Blow it up.
[3420.80 --> 3421.24]  Yeah.
[3422.92 --> 3423.28]  Yeah.
[3423.46 --> 3425.42]  I think you maybe overcooked it a little bit.
[3425.52 --> 3426.72]  That's what I was thinking, too.
[3426.78 --> 3428.42]  I was like, did I go too far?
[3428.68 --> 3429.54]  The image is too.
[3429.82 --> 3432.18]  You need to JPEG-ify it a little bit more.
[3432.30 --> 3433.60]  That's actually the problem, I think.
[3433.80 --> 3436.02]  It's such a good image, by the way.
[3436.26 --> 3436.92]  Like, you really.
[3436.92 --> 3437.30]  It is a good one.
[3437.78 --> 3439.38]  And by the way, you did call this a beer bong.
[3439.50 --> 3441.62]  That's just an old-fashioned bong.
[3442.54 --> 3443.84]  I called it a water bong.
[3444.26 --> 3444.62]  Oh, okay.
[3444.90 --> 3445.78]  It's a water pipe.
[3446.30 --> 3446.84]  Oh, sorry.
[3446.92 --> 3447.32]  Water pipe.
[3447.96 --> 3448.58]  I went to Berkeley.
[3448.84 --> 3450.22]  He knows all about this.
[3450.22 --> 3454.46]  I've always heard them referred to as water bongs, but I don't know, so I'm not an expert.
[3454.46 --> 3458.40]  Casey, I have the way that this could have been a huge meme for you.
[3458.56 --> 3458.84]  Okay.
[3459.54 --> 3463.18]  And there's still time, because no one knows why Prime is posting this one.
[3463.52 --> 3463.70]  Okay.
[3463.70 --> 3469.22]  Take the original image and put it over top at, like, 50% opacity.
[3470.56 --> 3471.00]  Right?
[3471.00 --> 3476.84]  The original text that's saying, hey, bae interns, what's up?
[3476.92 --> 3477.22]  Okay.
[3477.48 --> 3477.96]  And then.
[3478.14 --> 3479.58]  Hey, bae interns is pretty good.
[3479.58 --> 3481.00]  I think you can do a lot of that.
[3481.00 --> 3481.88]  You've got a hit.
[3481.88 --> 3481.90]  You've got a hit.
[3481.90 --> 3481.92]  You've got a hit.
[3481.92 --> 3484.80]  It's so good because they're from the Bay Area, but it's spelled like.
[3484.82 --> 3485.20]  I know.
[3485.20 --> 3486.14]  The other kind of Bay, dude.
[3486.22 --> 3487.34]  It's so good.
[3487.70 --> 3487.80]  I know.
[3487.80 --> 3489.24]  I don't know about that stuff.
[3489.54 --> 3496.28]  Because that's, I feel like if you've got the overlay, it's going to do 100,000 likes.
[3496.34 --> 3499.12]  I don't know about that, but it's worth reshooting.
[3499.58 --> 3499.82]  Okay.
[3499.82 --> 3500.72]  Send it out tomorrow.
[3500.90 --> 3502.14]  We'll juice it in the algorithm.
[3502.14 --> 3506.34]  So we'll try some different approaches to this meme, see if we can get it to latch.
[3506.56 --> 3506.70]  Okay.
[3506.98 --> 3507.46]  Yeah, exactly.
[3507.64 --> 3512.34]  Hopefully people listening back to this later have already seen the meme before they hear
[3512.34 --> 3513.70]  it in the stand-up.
[3513.76 --> 3514.76]  Now, that would be cool.
[3515.40 --> 3515.64]  All right.
[3515.64 --> 3517.62]  So I do want to throw this out here.
[3517.62 --> 3523.24]  I think something else is that this meme, I personally look at it and I say that its
[3523.24 --> 3526.52]  quality is in a reply, not in a standalone.
[3527.12 --> 3527.26]  Yeah.
[3527.36 --> 3533.82]  If that email was leaked and it was out and then you replied to it with this, I think that
[3533.82 --> 3537.10]  it could ratio the original one just because it's so hilarious.
[3537.82 --> 3541.84]  And so I think the power in this one is more in the reply than it is in of itself.
[3542.18 --> 3542.50]  Okay.
[3542.82 --> 3543.08]  Okay.
[3543.08 --> 3543.18]  Yeah.
[3544.08 --> 3548.80]  Quote tweeting or whatever is very effective for sure.
[3549.22 --> 3550.48]  Because it's like a one-two.
[3551.00 --> 3554.90]  I think also like the meme picks the man, the man doesn't pick the meme.
[3555.12 --> 3557.78]  Like sometimes it happens and sometimes it doesn't.
[3558.08 --> 3559.40]  And like you just, you know.
[3559.54 --> 3562.14]  You just don't throw your pearls before the swine.
[3562.22 --> 3562.96]  That's all you got to say.
[3562.96 --> 3563.06]  Yeah.
[3563.26 --> 3565.66]  You just got to do it.
[3565.98 --> 3567.68]  I mean, I've had so many fall flat.
[3568.04 --> 3568.96]  Like it's like.
[3569.36 --> 3571.18]  Just delete them and pretend they didn't happen.
[3571.18 --> 3573.48]  If they didn't get a lot of views, nobody will even know.
[3573.48 --> 3575.72]  Or leave them and just sit with it and get used to being cringy.
[3576.22 --> 3576.58]  Yeah.
[3576.66 --> 3577.26]  That's true too.
[3577.36 --> 3578.22]  Embrace the cringe.
[3578.62 --> 3579.60]  I'm wearing a bathrobe.
[3579.76 --> 3580.98]  So what are you going to do?
[3582.30 --> 3583.80]  Casey, did you say a two though?
[3583.84 --> 3584.66]  Or did you just have one?
[3584.74 --> 3585.56]  Just that one.
[3585.72 --> 3589.92]  That was the only time that I really felt like I was like, I'm going to try and make
[3589.92 --> 3590.38]  a meme.
[3590.80 --> 3592.70]  And then it got nothing.
[3593.00 --> 3593.10]  Right.
[3593.10 --> 3594.36]  It's a great job.
[3594.36 --> 3599.46]  I spent hours on memes that like get 10 likes and then I'll just like say like something
[3599.46 --> 3602.36]  stupid to in reply to someone and it gets a thought.
[3602.52 --> 3604.14]  Like you can't get attention to that stuff.
[3604.48 --> 3604.62]  Yeah.
[3604.64 --> 3605.54]  You got to keep shooting.
[3605.92 --> 3606.56]  You got to keep shooting.
[3606.78 --> 3611.48]  There is something to be said though that every, I'd say like every 10 minutes you spend
[3611.48 --> 3611.90]  on a meme.
[3612.74 --> 3615.72]  I do think it's, it goes down in its quality.
[3616.08 --> 3616.24]  Yeah.
[3616.32 --> 3616.90]  You could be right.
[3616.90 --> 3617.68]  Something about that.
[3617.78 --> 3621.18]  Like, because the reason why you saw the meme and you thought it was funny to begin
[3621.18 --> 3624.22]  with is because there's something that turned in you and just like, was like, oh, that's
[3624.22 --> 3624.50]  funny.
[3624.80 --> 3626.98]  And so you have to like Twitter.
[3627.12 --> 3630.44]  You only get about that amount of time for someone to like or dislike it.
[3630.74 --> 3633.10]  That's why I never think about what I'm going to tweet beforehand.
[3633.24 --> 3634.44]  I have zero scheduled tweets.
[3634.66 --> 3636.00]  I've never scheduled a tweet.
[3636.12 --> 3638.48]  The moment it happens, I'm like, that's the time.
[3638.48 --> 3643.48]  To be fair though, Prime, we did spend a lot of time and then rent a yacht to make a music
[3643.48 --> 3643.86]  video.
[3644.10 --> 3644.76]  So that's different.
[3644.80 --> 3646.14]  That's a different piece of media.
[3646.14 --> 3648.14]  That's a YouTube, that's a YouTube video.
[3648.40 --> 3649.56]  That's not a tweet.
[3650.22 --> 3652.02]  It is a meme, but it's a different kind of meme.
[3652.10 --> 3653.52]  It's a different kind of consumable meme.
[3653.96 --> 3657.08]  So when it comes to Twitter, I truly believe that it dictates a lot.
[3657.68 --> 3657.88]  Yeah.
[3658.10 --> 3661.78]  I believe that the best memes come from your heart or Twitch chat.
[3661.96 --> 3663.90]  They do not come from your brain.
[3664.24 --> 3666.58]  The medium is the meme, says Marshall McLuhan.
[3666.58 --> 3668.78]  The medium informs the message.
[3669.06 --> 3669.40]  Seriously.
[3669.72 --> 3671.22]  The medium informs the message.
[3671.32 --> 3672.54]  True for a lot of things as well.
[3672.78 --> 3676.02]  It's why your tweet's probably not going to change anybody's mind about anything.
[3676.14 --> 3678.40]  So play to your audience and have fun instead.
[3678.56 --> 3678.84]  Exactly.
[3678.84 --> 3679.60]  Real life advice.
[3679.68 --> 3679.98]  Sorry.
[3680.30 --> 3681.08]  I forgot about the standup.
[3681.08 --> 3682.24]  That was really good advice.
[3682.44 --> 3684.40]  And I don't know if that's accepted around here.
[3684.46 --> 3684.70]  Yeah.
[3684.70 --> 3684.98]  Sorry.
[3685.38 --> 3687.26]  We're deep in the standup by now.
[3687.34 --> 3687.74]  So it's okay.
[3688.08 --> 3693.10]  Prime, just play from one minute 20 on the thing that I sent in chat so that they can see
[3693.10 --> 3694.14]  the Steve Ballmer situation.
[3694.14 --> 3697.72]  It'd be best if you could get audio in for Casey and Carson.
[3698.00 --> 3701.36]  I know the audio by heart of this movie.
[3701.58 --> 3704.34]  So then it's very important that you can hear my audio.
[3704.72 --> 3705.16]  Okay.
[3705.44 --> 3705.72]  Okay.
[3705.96 --> 3706.90]  Because I studied.
[3707.78 --> 3707.90]  Yeah.
[3708.06 --> 3709.56]  Who said sit down?
[3710.84 --> 3712.42]  That's my favorite part.
[3712.48 --> 3713.14]  Did you do that?
[3713.42 --> 3714.44]  I didn't do that part.
[3714.64 --> 3715.52]  Oh, TJ.
[3716.20 --> 3716.68]  Sorry.
[3716.82 --> 3717.08]  Sorry.
[3717.08 --> 3717.48]  He didn't.
[3718.86 --> 3722.12]  He's very angry that someone sat down in the audience.
[3722.16 --> 3723.36]  Are we doing the Steve Jobs one?
[3723.36 --> 3724.62]  Have you seen his retirement one?
[3725.08 --> 3725.28]  Yeah.
[3725.36 --> 3727.10]  Prime, it's one minute 20 into this one.
[3728.42 --> 3728.62]  Okay.
[3728.62 --> 3729.30]  So start at 120.
[3729.30 --> 3730.50]  One minute 20 are still on Steve Jobs.
[3730.76 --> 3731.14]  I know.
[3731.30 --> 3733.82]  I want him to see the Steve Jobs thing and then the transition in.
[3734.44 --> 3738.74]  Well, the problem is that I can't get audio for them to listen to in Riverside.
[3739.10 --> 3739.42]  Okay.
[3739.48 --> 3740.08]  Well, just here.
[3740.28 --> 3740.38]  No.
[3740.78 --> 3743.14]  Post it on Twitter and I'll go click on it so I can watch.
[3743.14 --> 3743.32]  Okay.
[3743.36 --> 3743.50]  Here.
[3743.56 --> 3744.02]  It's in chat.
[3744.14 --> 3744.54]  It's in chat.
[3744.86 --> 3745.02]  Yeah.
[3745.02 --> 3745.32]  There you go.
[3745.38 --> 3745.96]  You can see it in chat.
[3745.96 --> 3746.16]  Here.
[3746.16 --> 3750.16]  I'll jump out and I'll play it on screen and people will be able to hear it.
[3750.32 --> 3750.42]  Yeah.
[3750.58 --> 3752.72]  It's just you won't be able to hear it.
[3752.86 --> 3755.80]  Just give Casey a countdown for when he should start at 120.
[3756.22 --> 3757.02]  What chat?
[3757.38 --> 3758.28]  It's not in the chat.
[3758.62 --> 3758.94]  Oh, sorry.
[3759.04 --> 3759.18]  Twitch chat.
[3759.26 --> 3759.60]  Loser?
[3759.86 --> 3761.00]  I'll send it in here too, Casey.
[3761.70 --> 3762.66]  I'm 48.
[3762.80 --> 3763.94]  I don't have a Twitch chat.
[3764.02 --> 3765.00]  What even does that mean?
[3765.14 --> 3765.88]  No one knows what that means.
[3765.88 --> 3766.22]  Here, Casey.
[3766.62 --> 3768.08]  I sent it in studio chat too.
[3768.12 --> 3768.14]  Thank you.
[3768.14 --> 3771.02]  I accidentally streamed on Twitch once for like 30 seconds.
[3771.62 --> 3772.44]  There you go.
[3773.06 --> 3774.76]  I was just like, what does this button do?
[3774.76 --> 3776.26]  At least stream on Twitch.
[3776.68 --> 3776.90]  All right.
[3776.90 --> 3778.24]  You do it all the time.
[3778.46 --> 3778.74]  OBS.
[3779.10 --> 3781.28]  I signed in with Twitch and then I hit start streaming.
[3781.46 --> 3782.18]  I didn't know what happened.
[3782.82 --> 3783.78]  I'm still worried.
[3783.82 --> 3785.64]  Prime is going to leak several meetings.
[3785.64 --> 3787.30]  Like he's going to leave stream on all day.
[3787.42 --> 3788.94]  We had it happen last week.
[3789.08 --> 3793.58]  Fortunately, Twitch chat messaged me in my chat and I happened to have it open on my side
[3793.58 --> 3793.92]  thing.
[3793.96 --> 3794.84]  And I saw that.
[3794.84 --> 3796.82]  They were like, yo, Prime is still live.
[3796.92 --> 3798.32]  We can hear your meeting.
[3799.22 --> 3799.50]  Yeah.
[3799.82 --> 3800.36]  I'm going to.
[3800.56 --> 3801.02]  That's not.
[3801.12 --> 3802.12]  That's a bad situation.
[3802.18 --> 3803.02]  That's a bad situation.
[3803.06 --> 3803.22]  All right.
[3803.24 --> 3803.98]  Everyone be quiet.
[3804.06 --> 3806.60]  I'm going to start it in three, two, one.
[3807.76 --> 3813.28]  I'm going to pass it over to our CTO, Steej Baltimore, for more information.
[3814.62 --> 3815.64]  Take it away, Steej.
[3818.34 --> 3820.22]  Is someone leaking it or is it just me?
[3820.30 --> 3820.90]  There was an echo.
[3822.16 --> 3823.00]  Meet your mic, TJ.
[3823.00 --> 3824.12]  Was it me?
[3824.20 --> 3825.28]  Maybe I was listening to you.
[3826.36 --> 3826.84]  Go again.
[3826.92 --> 3827.20]  Go again.
[3827.84 --> 3829.12]  Oh, cow.
[3829.34 --> 3830.50]  I'm going to have to toughen up.
[3830.76 --> 3831.20]  Here we go.
[3832.04 --> 3834.66]  What's the $64,000 question for the field?
[3835.46 --> 3836.74]  What is the most asked question?
[3836.76 --> 3837.50]  I love the bend.
[3837.66 --> 3838.74]  I love the bending over.
[3839.02 --> 3842.58]  What the beans are we going to do about coffee, Steej?
[3843.80 --> 3845.50]  It's a very good question.
[3845.50 --> 3850.72]  And it's got a very, very clear answer.
[3852.04 --> 3852.60]  Developers.
[3853.00 --> 3855.18]  The key to coffee.
[3855.80 --> 3858.68]  The key to industry transformation.
[3859.42 --> 3862.90]  The key to SSH is developers.
[3863.12 --> 3863.68]  Developers.
[3863.68 --> 3866.10]  It's so much easier to not hate these guys now.
[3866.34 --> 3866.62]  Developers.
[3867.62 --> 3868.16]  Developers.
[3868.28 --> 3868.48]  Developers.
[3868.48 --> 3869.12]  Oh, wow.
[3869.20 --> 3870.36]  This is really well done.
[3870.36 --> 3870.80]  Developers.
[3870.80 --> 3871.52]  Developers.
[3871.78 --> 3872.36]  Developers.
[3875.00 --> 3875.52]  Yes.
[3877.04 --> 3877.28]  So.
[3877.28 --> 3879.66]  Yep.
[3879.82 --> 3880.32]  Oh, no.
[3880.70 --> 3881.04]  Oh, no.
[3881.12 --> 3882.66]  I got DMCA'd.
[3883.12 --> 3883.34]  Yeah.
[3883.34 --> 3883.92]  You should have known.
[3883.98 --> 3884.84]  You should have known better, Prime.
[3885.16 --> 3886.02]  So here's the thing.
[3886.14 --> 3888.98]  You still have the opportunity to do Who Said Sit Down?
[3889.06 --> 3891.24]  Because that's the one where he runs out on stage.
[3891.34 --> 3891.76]  It's not that.
[3891.76 --> 3893.34]  It's a different one than the developers one.
[3893.44 --> 3893.56]  Yeah, true.
[3893.56 --> 3897.58]  So there could be a second Steve Ballmer with the Who Said Sit Down?
[3897.70 --> 3899.44]  With Get on your feet.
[3899.64 --> 3900.02]  I'll try.
[3900.02 --> 3901.84]  We can release another one.
[3901.94 --> 3902.26]  Yeah, yeah.
[3902.60 --> 3903.38]  Guys, I tried.
[3903.52 --> 3906.18]  I actually dumped water all over that shirt and everything.
[3906.38 --> 3912.06]  I also rode really hard for a while before doing a two, but the shirt was just getting
[3912.06 --> 3912.80]  translucent.
[3912.98 --> 3915.88]  It wasn't turning dark blue, so it wasn't really working.
[3915.88 --> 3919.66]  It was showing more than I wanted to show, if you guys know what I mean on that.
[3919.80 --> 3922.14]  So it kind of dried out a little bit, but I tried.
[3922.30 --> 3923.48]  I did dump water on it.
[3923.58 --> 3926.06]  It just wasn't the look we were going for.
[3926.50 --> 3926.74]  Yeah.
[3927.06 --> 3928.50]  Yeah, it was the wrong kind of material.
[3928.68 --> 3929.82]  It was pretty good mime.
[3930.02 --> 3933.34]  It was pretty good copying of his movements, right?
[3933.34 --> 3934.28]  The bending over.
[3934.78 --> 3939.78]  He has a very sort of primal stance.
[3941.20 --> 3942.64]  I'm not joking you.
[3943.28 --> 3950.48]  I seriously watched it at least 30 times in a row before I was doing it.
[3950.84 --> 3953.04]  Whole thing through, get the whole thing down.
[3953.16 --> 3954.02]  I was dedicated.
[3954.86 --> 3956.04]  It's very good work.
[3956.98 --> 3962.08]  Just further proof that cringe is like, for lack of a better word, is good.
[3962.60 --> 3963.08]  It's good.
[3963.66 --> 3964.40]  And eternal.
[3965.40 --> 3966.28]  It's good, man.
[3966.28 --> 3972.44]  It's just, a thousand years from now, no one's going to remember your super hip post, but
[3972.44 --> 3973.70]  they're going to be playing the bomber.
[3973.70 --> 3975.68]  Oh, I hope so, dude.
[3976.06 --> 3980.58]  If I could be immortalized as a Steve Baltimore impersonator, that would be so sick.
[3981.54 --> 3983.94]  It would really be the end-all be-all of everything.
[3984.40 --> 3984.80]  I think that's...
[3984.80 --> 3985.28]  They don't know.
[3985.42 --> 3987.56]  I started streaming so that I could do that.
[3987.76 --> 3988.04]  You know?
[3988.04 --> 3994.14]  I think one thing that people forget is that when it comes to being cringed, if you just
[3994.14 --> 3998.80]  embrace it, it somehow becomes less and less cringy.
[3999.38 --> 4002.20]  Even when you can get other people to cringe.
[4002.28 --> 4004.08]  I mean, that's the entire show of The Office.
[4004.54 --> 4008.40]  It's just you cringing incredibly hard at Michael Scott.
[4009.00 --> 4011.28]  There's some episodes that are so painful to watch.
[4011.32 --> 4013.00]  What's that one that we were watching just recently?
[4013.48 --> 4015.96]  I think it's time for you to leave on Netflix.
[4015.96 --> 4019.90]  Just the entire time, you're just sitting there like, I feel so deeply uncomfortable.
[4020.42 --> 4022.96]  And that's just because it's just this amazing...
[4023.64 --> 4025.02]  Just the cringe is amazing.
[4025.74 --> 4026.04]  I know.
[4026.20 --> 4027.24]  Well, I think there's like...
[4027.24 --> 4028.32]  You got to have solidarity.
[4028.78 --> 4032.20]  Like, we cringey types have to have solidarity.
[4032.54 --> 4038.70]  Like, there's a quote from Chesterton that's like, the comedy of man survives the tragedy of
[4038.70 --> 4038.94]  man.
[4038.94 --> 4044.14]  And it's just like, every person, no matter how cringey they are, and like, you know, it's
[4044.14 --> 4046.10]  like, there's a human being there.
[4046.22 --> 4047.50]  And like, it's all good.
[4047.54 --> 4048.78]  We're all trying to figure it out.
[4049.04 --> 4050.56]  Like, and it can be really funny.
[4050.62 --> 4054.84]  Like, when someone just goes ape, you're like, dude, yeah, man, that's pretty funny.
[4055.24 --> 4056.76]  And like, it doesn't have to be...
[4056.76 --> 4061.52]  I feel like a lot of that attitude of like, Corinne, it's just like, just, you know, this
[4061.52 --> 4063.42]  is just another person trying to figure it out.
[4063.60 --> 4064.00]  It's all good.
[4064.00 --> 4064.14]  Yeah.
[4064.46 --> 4064.88]  Agreed.
[4065.56 --> 4067.26]  I feel like that's the end right there.
[4067.60 --> 4068.08]  That was perfect.
[4068.36 --> 4069.28]  That's the closer.
[4069.74 --> 4070.54]  We'll see you guys later.
[4070.90 --> 4071.16]  Yeah.
[4071.16 --> 4072.52]  Hey, good stand-up.
[4072.52 --> 4074.06]  No blockers for me this week.
[4074.22 --> 4075.60]  Check out Hypermedia Systems.
[4076.06 --> 4076.30]  Yeah.
[4076.42 --> 4077.56]  Oh, GregBrain.deb.
[4077.64 --> 4078.20]  Buy the book.
[4078.62 --> 4078.82]  Yeah.
[4079.22 --> 4081.14]  Clean code, I'm indifferent towards, but...
[4081.14 --> 4083.00]  Don't read it to know what he says, though.
[4083.04 --> 4085.64]  It's still a good read, even if you don't agree with everything.
[4085.82 --> 4086.90]  Thanks, Uncle Bob, for the bathroom idea.
[4086.90 --> 4086.92]  Yeah, I agree with that.
[4086.92 --> 4090.82]  And I have to say, he did mention, he was like, oh, because I was like, oh, it's too ideological.
[4090.82 --> 4093.94]  And he's like, at the start, I say, this is the way I do things.
[4094.04 --> 4097.64]  And in fairness to him, I'd never read the introduction, because I never read introductions.
[4097.64 --> 4101.38]  But he does say in the introduction, like, hey, this is the way that I code.
[4101.48 --> 4103.28]  And there are other people that disagree with it.
[4103.62 --> 4104.28]  So I have to give him that much.
[4104.28 --> 4105.54]  Do you read four words?
[4106.72 --> 4107.84]  I tend to.
[4108.06 --> 4108.74]  Like, I'll read...
[4108.74 --> 4112.34]  We're not sure if you can read four words, let alone five, dude.
[4112.78 --> 4113.94]  I could read a four word.
[4114.18 --> 4115.14]  I mean, I've done it before.
[4115.48 --> 4120.08]  I can't give you a percentage, but I know I've read four words before.
[4120.08 --> 4125.30]  Well, if you buy Uncle Bob's new book, We Programmers, you can read my four word that I threw in there.
[4125.42 --> 4125.50]  Okay.
[4126.08 --> 4126.28]  Yeah.
[4126.42 --> 4129.08]  Threw in there like you just...
[4129.60 --> 4130.84]  Like a YouTube comment?
[4131.20 --> 4132.50]  Just get through it in there like a YouTube comment.
[4132.50 --> 4134.28]  He wrote it for real, and it's good.
[4134.34 --> 4135.08]  I've read both.
[4135.16 --> 4135.54]  It's good.
[4135.64 --> 4135.84]  Yeah.
[4136.08 --> 4136.26]  Yeah.
[4137.14 --> 4137.50]  Yeah.
[4138.36 --> 4139.96]  Well, Carson, thanks for joining us today.
[4140.00 --> 4140.56]  It was awesome.
[4141.16 --> 4141.68]  Yeah, absolutely.
[4141.96 --> 4143.18]  And I'll be checking out your book for sure.
[4143.60 --> 4145.36]  Uncle Bob on the stand-up would break the internet.
[4145.50 --> 4146.66]  It may happen at some point.
[4147.20 --> 4147.48]  Yeah.
[4147.76 --> 4148.98]  Give me an Uncle Bob on here.
[4148.98 --> 4149.38]  Let's go.
[4149.38 --> 4150.06]  All right.
[4151.08 --> 4152.50]  I'll sit that one out.
[4152.60 --> 4153.60]  You guys can have my slot.
[4154.84 --> 4155.34]  All right.
[4155.38 --> 4158.10]  Hey, thank you, everybody, for being a part of the stand-up.
[4158.12 --> 4159.20]  The stand-up, episode seven.
[4159.48 --> 4164.56]  Hey, if you're still around at this point, I want you to say something sufficiently stupid.
[4164.56 --> 4164.68]  All right.
[4164.72 --> 4169.68]  Escapac para la trustworthy.
[4169.88 --> 4173.82]  .
[4173.90 --> 4174.32]  A toast sun.
[4174.40 --> 4174.72]  It or a drink.
[4174.72 --> 4178.64]  and Harold live in the tree.
