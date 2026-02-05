[0.00 --> 1.88]  All right, you know what I think we should do?
[2.28 --> 2.72]  An intro.
[3.06 --> 4.52]  An intro to the stand-up, Prime.
[5.08 --> 5.38]  All right.
[5.50 --> 6.06]  You got this.
[6.40 --> 7.26]  Are we doing a podcast?
[8.98 --> 15.36]  We're doing a podcast today, every Wednesday and Friday, live on Twitch, 11 a.m., the stand-up
[15.36 --> 18.56]  happens, and today we have a special assortment of guests.
[18.66 --> 20.22]  We have Tiege, as always.
[20.32 --> 21.00]  Say hi, Tiege.
[21.22 --> 24.88]  I like when you say that the stand-up happens every day, but then you say it's Wednesdays
[24.88 --> 25.32]  and Fridays.
[25.44 --> 26.00]  That one's...
[26.00 --> 28.34]  You didn't say that this time, but you've said it the last few intros.
[28.42 --> 29.14]  Anyways, hi.
[29.14 --> 29.20]  Hi.
[29.20 --> 33.28]  Uh, actually, this is the second time I said what day it happened, so guess what?
[33.28 --> 33.56]  Oh, I know.
[33.82 --> 34.44]  Last time you said every...
[34.44 --> 35.22]  You're wrong with every few.
[35.22 --> 36.34]  Oh, we're being technical.
[36.56 --> 37.68]  Hi, I'm Technical TJ.
[38.10 --> 39.48]  Bring it back from the last episode.
[39.64 --> 44.64]  Stand-up, which is streamed every day, Wednesday at 11 and Friday at 11 a.m.
[44.64 --> 46.88]  You literally said it happens every day.
[47.34 --> 48.52]  Every day.
[48.74 --> 50.70]  Wednesdays and Fridays, which...
[50.70 --> 51.24]  So what we've learned...
[51.24 --> 51.46]  Okay.
[51.66 --> 53.88]  What we have learned today...
[53.88 --> 54.60]  This is insane.
[54.60 --> 58.80]  What we've learned today is that when Prime does actually do the intro correctly,
[58.80 --> 60.84]  Teej will then immediately derail.
[60.98 --> 61.48]  Torpedoes it.
[61.54 --> 62.34]  He torpedoes it.
[62.46 --> 62.98]  What the hell?
[62.98 --> 63.26]  That will derail.
[63.26 --> 64.58]  This was our one chance.
[64.68 --> 68.62]  The plane was, like, leaving the runway, and you were like, I'm gonna be the chicken that
[68.62 --> 69.50]  flies into the engine.
[69.94 --> 70.68]  Here's my question.
[70.82 --> 74.02]  Is this called the stand-up, or is it called the well-run meeting?
[74.52 --> 75.00]  Good point.
[75.00 --> 76.40]  Yeah, yeah.
[76.54 --> 76.96]  Yeah, yeah.
[77.12 --> 78.02]  Yeah, yeah, yeah, yeah.
[78.16 --> 79.40]  Yeah, yeah, yeah, yeah.
[79.90 --> 80.74]  Anyways, sorry.
[81.04 --> 81.36]  All right.
[81.48 --> 84.18]  We also have with us Casey, as usual.
[84.30 --> 85.08]  Say hi, Casey.
[85.52 --> 86.22]  Hi, Casey.
[86.72 --> 87.66]  I knew one of you.
[87.66 --> 89.54]  I knew one of you sons of bitches would do that.
[90.04 --> 93.28]  And a very special guest today, which is Ryan.
[93.42 --> 94.26]  Is it Fleure?
[96.26 --> 97.64]  That's perfect, actually.
[97.88 --> 99.44]  I was leaning into it, yeah.
[99.44 --> 99.72]  Yeah.
[99.90 --> 101.50]  I mean, I knew it was French.
[101.50 --> 104.70]  I didn't know what you gotta do with that, you know?
[104.88 --> 106.98]  Okay, well, anyways, say hello, Ryan Fleure.
[107.40 --> 108.60]  Hello, Ryan Fleure.
[109.86 --> 110.30]  Nice.
[110.32 --> 111.12]  Oh, that was wonderful.
[111.54 --> 111.96]  Thank you.
[112.04 --> 113.86]  And today, we have a very special topic.
[113.96 --> 115.40]  It's one of those evergreen topics.
[115.50 --> 116.72]  We're gonna be talking about debuggers.
[117.08 --> 120.58]  And since I'm a print-f debugger, TJ, I don't know what he is.
[120.92 --> 122.70]  Casey, definitely a debugger debugger.
[123.04 --> 127.40]  Ryan Fleure is the one who writes the debuggers, so we figured he'd be the best single person
[127.40 --> 129.94]  to bring on and help us understand all the buggers.
[129.94 --> 132.82]  Ryan, I have a very important question to kick this off.
[133.16 --> 137.82]  Is print-f debugging an abomination towards man, or is it a perfectly viable strategy?
[139.50 --> 141.22]  Well, yeah, I think so.
[141.42 --> 147.24]  The first thing I would probably say to introduce someone to the topic, if they had just started
[147.24 --> 150.74]  programming and they figured out how to insert log statements into the program to sort of
[150.74 --> 154.80]  see what happened, the first thing I would say is that there's no dichotomy between that
[154.80 --> 156.54]  and what a debugger is offering.
[156.54 --> 160.88]  Like, there's no dichotomy between logging and what a debugger, like the information
[160.88 --> 162.04]  that a debugger is actually getting.
[162.16 --> 167.46]  The only variable is what work you actually had to do in order to get a log of information
[167.46 --> 168.34]  out of your program.
[168.80 --> 172.48]  And so the first thing I would describe about a debugger is that it's collecting a log of
[172.48 --> 174.56]  information from your program in a sense.
[175.10 --> 178.60]  It's sort of, it's just another program on your computer that's running, and it's running
[178.60 --> 182.32]  alongside your actual program, the program you care about that you're working on.
[182.32 --> 188.48]  And it's sitting there collecting information from your program, and it's really in a log-like
[188.48 --> 188.88]  fashion.
[189.10 --> 193.90]  So now there are technical constraints about that, because obviously the debugger has to
[193.90 --> 198.66]  collect information without modifying the actual program, because it's running with it live
[198.66 --> 199.54]  and collecting information.
[200.46 --> 203.24]  So there are limited ways in which it can modify the program.
[203.36 --> 208.20]  Some of that varies depending on how well the kernel facilitates that process and stuff
[208.20 --> 208.62]  like that.
[209.12 --> 213.48]  But the point is, it's sort of, it's collecting the same kind of information.
[214.16 --> 219.02]  At the limit, when debuggers can't go too far, you do have to go back into your program and
[219.02 --> 223.10]  say, okay, now I'm going to print F here and here and here and here, or generate a log,
[223.24 --> 226.92]  or plenty of other versions of that exist.
[227.24 --> 231.26]  So it's not that like team debugger versus team logging.
[231.26 --> 237.02]  It's very much like there are no, people should kind of remove that boundary from their heads,
[237.12 --> 242.64]  because the degree to which debuggers could theoretically do logging is, I think, more extreme
[242.64 --> 246.52]  than people, maybe if they're just getting used to the idea of a debugger, they might
[246.52 --> 247.20]  not realize.
[247.62 --> 252.66]  So it's not an abomination, although I think it's a lot slower than the tools that debuggers
[252.66 --> 253.84]  do offer you in a lot of cases.
[254.18 --> 255.30]  That's how I would put it.
[255.30 --> 260.12]  But this is hard for my American mind, because I only know red versus blue.
[260.78 --> 265.00]  So this is like really, this is really difficult for me to have some sort of nuanced answer.
[265.48 --> 267.32]  Well, I mean, if you think, oh, sorry, go ahead, Ryan.
[267.58 --> 271.26]  I was going to say, you can re-slice it so that red is the people who think that there's
[271.26 --> 274.18]  a red versus blue, and then, or, you know, vice versa.
[274.30 --> 278.62]  So you're on team red, which knows that there's no red versus blue, but blue is all the people
[278.62 --> 281.22]  who do, and then it's just another red versus blue problem.
[281.52 --> 284.96]  Because I'm American too, so that's how you do that.
[286.20 --> 289.38]  This makes me want to light up a barbecue and eat apple pie.
[289.60 --> 290.30]  Yeah, exactly.
[291.12 --> 292.16]  Don't forget the curse light.
[292.84 --> 294.58]  Oh, I would never.
[296.64 --> 297.70]  I would never.
[298.98 --> 300.62]  Only the finest micro-brew.
[303.32 --> 306.52]  All right, someone has to have a real question here to kick this bad boy off.
[306.52 --> 309.48]  Well, I would keep going on that front, actually.
[310.12 --> 311.82]  Hey, Deej, just finished the front end.
[311.96 --> 313.00]  I'm going to get the back end in JS.
[313.10 --> 313.86]  Could you give me the database?
[313.86 --> 315.80]  That's node problem.
[316.02 --> 316.82]  You got it, boss.
[317.52 --> 319.36]  That was a mess without type safety.
[319.72 --> 321.40]  I rewrote our back end in TypeScript.
[321.70 --> 322.58]  Could you fix up the database?
[322.90 --> 324.36]  I'm going to fix the ES lint errors.
[324.72 --> 326.92]  Not any problem for me.
[327.20 --> 327.76]  I got this.
[327.76 --> 332.78]  Tiege, AI is so hot right now, and my professor's helping us rewrite our back end in Python.
[332.78 --> 334.24]  Could you get a database up for me?
[334.62 --> 335.10]  Certainly.
[335.32 --> 336.60]  I would love to assist you.
[336.76 --> 337.46]  You're correct.
[337.58 --> 338.82]  Let's delve into this.
[339.88 --> 340.64]  Hey, Tiege.
[341.82 --> 343.50]  Python scaled worse than TypeScript.
[343.76 --> 344.54]  We're going to need Go.
[345.08 --> 345.84]  Could you give me a DB?
[346.70 --> 347.22]  Fast?
[347.48 --> 347.94]  Predictable?
[348.20 --> 348.60]  Boring?
[348.60 --> 350.24]  I'm ready to go.
[352.74 --> 353.44]  Hey, Tiege.
[354.06 --> 355.38]  We're shipping a lot of features lately.
[355.74 --> 356.06]  I know.
[356.14 --> 357.32]  Maybe too many features.
[357.46 --> 358.70]  I'm worried they don't need both of us.
[359.10 --> 360.94]  We need to slow down, but we need to look smart.
[361.46 --> 363.50]  Are you thinking what I'm thinking?
[363.50 --> 374.62]  You don't want your tools to pick your sack?
[375.14 --> 376.68]  Neon does serverless Postgres.
[377.00 --> 377.96]  You choose the rest.
[378.26 --> 379.88]  Get your free plan at neon.com.
[380.40 --> 382.48]  So there are some issues.
[382.76 --> 387.66]  Like, one of the reasons why I think people like printf debugging and say,
[387.94 --> 390.38]  I don't want to use the debugger or I don't see the point of it.
[391.08 --> 392.64]  There are some valid...
[392.64 --> 395.10]  Like, I think those come from a valid place,
[395.20 --> 398.26]  but they're not actually describing the problem correctly.
[398.46 --> 401.94]  So the valid place they're coming from is the fact that the debuggers often suck.
[403.12 --> 403.32]  Okay?
[403.56 --> 403.96]  So, like...
[403.96 --> 404.16]  Yes.
[404.52 --> 406.98]  Like, I have complained about Linux debuggers many times,
[407.28 --> 409.68]  and that is in comparison to Windows debuggers,
[409.96 --> 412.76]  which also usually kind of suck.
[412.90 --> 415.10]  Like, Linux is, like, ultra-suck debugging,
[415.42 --> 419.28]  but Windows debuggers historically have also been pretty darn crappy.
[419.28 --> 424.70]  And so, you know, one of the things that's important to recognize
[424.70 --> 428.76]  is that debuggers could give you your printf debugging way faster
[428.76 --> 430.66]  than you actually writing your printf debugging
[430.66 --> 432.44]  if they weren't sucking so bad,
[432.60 --> 434.00]  but oftentimes they are sucking.
[434.16 --> 436.76]  So, when I am on Linux, for example,
[436.76 --> 440.62]  I use printf debugging a lot more.
[440.98 --> 441.34]  Right?
[441.58 --> 442.12]  We'll clip it and chip it.
[442.12 --> 442.80]  A lot more.
[443.32 --> 444.04]  All I heard...
[444.04 --> 445.32]  All we need is Casey saying,
[445.44 --> 446.68]  I use printf debugging.
[446.82 --> 447.64]  Don't give the context.
[447.72 --> 448.22]  Okay, sorry.
[448.42 --> 448.62]  Sorry.
[449.22 --> 449.60]  I need...
[449.60 --> 450.62]  It needs to be a clean thing.
[451.32 --> 451.96]  So...
[451.96 --> 454.28]  And the reason for that is because the debuggers are so bad.
[454.44 --> 456.52]  If I'm on Windows and I have something
[456.52 --> 459.52]  where I can do my data collection really efficiently
[459.52 --> 460.72]  because there's good debuggers,
[460.90 --> 462.58]  largely thanks to Ryan now,
[462.58 --> 465.50]  but also thanks to George Menhorn,
[465.58 --> 466.68]  the guy who wrote RemedyBG,
[466.78 --> 468.50]  which is a bugger that I've been using previously,
[469.26 --> 473.52]  when you have a debugger whose user interface and design
[473.52 --> 476.64]  is set up to get you the information that you need very quickly,
[476.92 --> 479.06]  it will beat the speed of printf debugging.
[479.38 --> 481.98]  Because the amount of time it takes you to go add those printf lines,
[482.10 --> 483.82]  recompile the program, rerun the program,
[484.50 --> 485.32]  see where it prints out,
[485.40 --> 487.56]  oh, then go, oh, wait, I should have a few more printf's,
[487.56 --> 488.28]  and then you go back in there.
[488.60 --> 491.82]  That speed, you can be way faster than that
[491.82 --> 493.68]  to collect the exact same information with a debugger
[493.68 --> 495.72]  if the debugger is actually good.
[496.16 --> 498.00]  Now, if the debugger isn't good,
[498.34 --> 499.68]  it won't beat that speed,
[499.68 --> 502.18]  and then I am right there with everyone who's like,
[502.24 --> 502.84]  why would I use the debugger?
[502.94 --> 505.78]  Yes, you're right, because the debugger is too freaking slow.
[506.28 --> 508.78]  And so part of what Ryan's project is with the rad debugger,
[508.78 --> 512.30]  for example, is to stop having that choice around.
[512.54 --> 516.48]  It should just be a given that the debugger will collect the data for you
[516.48 --> 519.06]  way faster than you could have collected it by instrumentation.
[519.24 --> 523.56]  But the sad reality is that a lot of times currently it isn't,
[523.72 --> 524.54]  especially on Linux,
[524.62 --> 527.22]  but also for certain circumstances on Windows as well.
[527.88 --> 530.90]  Thank you, Ryan, for actually tackling this problem for us.
[530.90 --> 533.62]  So when I say I use printf debugging,
[533.80 --> 536.32]  that's the exact same thing as saying I use Arch, by the way?
[537.90 --> 538.30]  Oh.
[539.64 --> 540.86]  It's like very, very close.
[540.86 --> 542.48]  No, I wouldn't necessarily go that far.
[542.64 --> 544.06]  I wouldn't necessarily go that far.
[544.58 --> 545.54]  I wouldn't go that far.
[546.64 --> 547.92]  All right, so, Ryan,
[548.02 --> 550.04]  are you actually trying to provide us a solution?
[550.16 --> 551.88]  That's Linuxites?
[552.60 --> 553.00]  Linuxies?
[553.10 --> 553.40]  Yeah.
[553.78 --> 555.06]  Yeah, that's like, so...
[555.06 --> 555.86]  Linusations.
[556.56 --> 557.36]  Linusations, sorry.
[557.56 --> 558.56]  Linusations, right.
[558.56 --> 561.94]  So, yeah, I mean, it's actually like...
[561.94 --> 563.18]  And if you go back and look at...
[563.18 --> 564.78]  I think it's on WebArchive at this point,
[564.84 --> 566.92]  but if you go back and look at the RADDebugger's, like,
[567.02 --> 569.14]  original, like, pitch page,
[569.20 --> 570.50]  where they actually described the project,
[570.78 --> 573.06]  that was one of, like, the primary ambitions of the project
[573.06 --> 573.90]  all the way back then.
[574.46 --> 576.48]  I think this would be, like, 2013 or something.
[577.06 --> 578.76]  And I was nowhere near the project.
[578.86 --> 579.56]  I was in high school.
[579.90 --> 582.78]  So I was, like, not even working on the project.
[582.84 --> 583.68]  But all the way back then,
[583.70 --> 586.04]  if you go back and look at what the original ambitions of the project were,
[586.04 --> 586.28]  it's like,
[586.28 --> 589.14]  let's get a viable debugging solution on Linux.
[589.74 --> 592.16]  And so that's still part of the ambition.
[592.28 --> 593.66]  And that's actually, like...
[593.66 --> 596.28]  I'm starting to work on that not quite full-time
[596.28 --> 597.78]  because there's a lot of stuff to fix and everything.
[597.98 --> 599.18]  I mean, with the debugger in general,
[599.18 --> 600.84]  there's, like, hundreds of possible problems
[600.84 --> 602.30]  you could work on at any point in time.
[602.84 --> 604.30]  But I'm starting at this point,
[604.34 --> 605.66]  it's gotten stable enough on Windows
[605.66 --> 608.22]  that I'm starting to do more of the Linux port work.
[608.30 --> 610.16]  And so I have, like, the UI running,
[610.28 --> 612.02]  and I'm starting to do process control,
[612.02 --> 614.92]  and we have dwarf debug info parsing and stuff like that.
[614.92 --> 616.66]  So, yeah, it's actually going to happen.
[616.92 --> 619.32]  Like, it'll show up at some point soon.
[619.44 --> 621.40]  Before we go further,
[621.70 --> 622.68]  I think there's a lot of people
[622.68 --> 625.02]  who don't know anything about Rad Debugger
[625.02 --> 626.70]  or Ryan or other stuff.
[626.78 --> 629.70]  I know we jumped right into the PrintF controversy.
[629.96 --> 630.94]  We wanted the hot take.
[631.02 --> 632.28]  But maybe we can just take a sec.
[632.74 --> 634.16]  You can walk us back a little bit.
[634.22 --> 636.36]  You can talk about maybe Rad Debugger
[636.36 --> 638.02]  and give people some info of what's going on.
[638.10 --> 640.98]  Casey's mentioned it, like, a thousand times on the channel.
[640.98 --> 643.56]  So I think we got to tell people what it is, you know?
[643.76 --> 645.94]  And is it Epic Games Debugger now,
[646.00 --> 647.02]  or is it still Rad Debugger?
[647.98 --> 649.36]  It's called Rad Debugger,
[649.64 --> 651.82]  but that's sort of just historical.
[652.94 --> 655.24]  Epic bought Rad Game Tools back,
[655.58 --> 657.58]  actually, shortly before I joined.
[657.64 --> 660.00]  So I was never technically a part of, like, Rad proper.
[661.18 --> 662.94]  But Epic owns it now,
[662.98 --> 665.02]  but it's still called the Rad Debugger,
[665.02 --> 667.30]  because, I don't know, that's just the...
[667.30 --> 668.26]  That's what they just...
[668.26 --> 668.66]  I don't know.
[668.86 --> 670.50]  Nobody's told me that it should be renamed,
[671.22 --> 672.16]  so I haven't renamed it.
[673.00 --> 675.12]  But, yeah, I mean, basically,
[675.26 --> 677.46]  like, the story of the project is...
[677.46 --> 679.32]  It started with what I said, like,
[679.52 --> 681.02]  they wanted a viable...
[681.02 --> 681.68]  To my knowledge,
[681.76 --> 684.30]  I wasn't even near the company at this point, so...
[684.30 --> 686.16]  I was there if you want the actual story.
[686.16 --> 687.56]  Yeah, maybe you should do the early,
[687.82 --> 689.42]  and then I can say what happened after.
[690.06 --> 690.32]  Yeah.
[690.32 --> 690.68]  Yeah.
[690.96 --> 693.18]  So what happened specifically was,
[693.42 --> 695.74]  and this'll just show you...
[695.74 --> 698.60]  Remember the idea of the Steam,
[698.82 --> 701.52]  like, the Steam PC, like, Steam Linux?
[701.94 --> 702.42]  Do you remember this?
[702.58 --> 703.42]  Way, way back?
[703.52 --> 707.28]  Like, way, way back in, like, the early 2010s.
[707.44 --> 710.62]  They were, like, gonna ship this Steam Linux set-top box thing.
[710.62 --> 712.48]  And it never really materialized.
[712.60 --> 715.02]  Like, some IHVs kind of did,
[715.10 --> 716.32]  but it never became a thing.
[716.88 --> 718.24]  And then, like, fast forward to today,
[718.24 --> 720.80]  and they redid, like, sort of a similar plan to that.
[720.92 --> 721.84]  And with similar people,
[721.94 --> 723.68]  like, I think Pierre-Lou and those guys were...
[723.68 --> 724.22]  Same...
[724.22 --> 725.52]  I think it's, like, similar team
[725.52 --> 726.96]  did do the Steam Deck,
[727.04 --> 727.82]  and that has hit.
[727.92 --> 728.62]  Like, that worked,
[728.68 --> 729.66]  and they are going with it.
[729.74 --> 730.68]  But way back,
[730.74 --> 731.66]  there was this sort of idea
[731.66 --> 733.72]  that they were gonna do a Steam Linux distribution.
[735.10 --> 737.56]  This is where it sort of actually started.
[738.24 --> 739.40]  Because, obviously,
[739.80 --> 740.86]  RAD is a...
[740.86 --> 742.48]  Does a lot of cross-platform stuff.
[742.68 --> 744.12]  They have to ship on Linux,
[744.24 --> 745.18]  as well as Mac,
[745.28 --> 746.56]  as well as XXXX.
[746.56 --> 748.28]  Like, in fact, when I worked at RAD,
[748.32 --> 749.78]  it was dizzying the platforms we support.
[749.90 --> 751.00]  Like, I'd build, you know,
[751.06 --> 752.22]  the character animation system,
[752.42 --> 754.48]  and it's just a laundry list of platforms.
[754.48 --> 756.42]  It's, like, 14 long or something like that.
[756.50 --> 757.64]  So that was where I learned
[757.64 --> 758.80]  cross-platform programming,
[758.92 --> 760.14]  like, the hardest way, right?
[760.40 --> 761.66]  I had a little bit of experience before,
[761.84 --> 762.96]  but that was the big one.
[763.80 --> 765.82]  And so, RAD and Valve
[765.82 --> 767.60]  were always historically very close.
[767.90 --> 769.42]  Like, Jeff and Gabe,
[769.56 --> 771.42]  so the two heads of the companies,
[771.54 --> 773.08]  used to have lunch pretty regularly.
[773.08 --> 774.52]  So they were never, like,
[774.60 --> 775.98]  at each other's throats at all.
[776.06 --> 777.90]  They were not competitors, really,
[777.96 --> 779.32]  or never thought of themselves that way,
[779.46 --> 780.86]  because they didn't really operate
[780.86 --> 781.94]  in similar business spaces.
[782.18 --> 784.22]  So they were actually fairly close,
[784.40 --> 785.34]  and oftentimes,
[785.78 --> 788.10]  they would even share employees sometimes.
[788.52 --> 789.58]  So there would be times,
[789.66 --> 790.12]  like, for example,
[790.18 --> 791.20]  on the VR projects,
[791.26 --> 792.40]  where some of the RAD people
[792.40 --> 794.24]  were still technically RAD employees,
[794.36 --> 795.68]  but, like, Valve would pay their salaries,
[795.76 --> 796.62]  and they were at Valve.
[796.86 --> 798.32]  There was all kinds of stuff like that.
[798.32 --> 799.32]  So it was kind of closer
[799.32 --> 800.70]  than people know about,
[800.80 --> 801.54]  because it's, you know,
[801.78 --> 803.14]  it's not like this is secret or anything,
[803.24 --> 804.12]  but just, like, you know,
[804.52 --> 805.98]  it doesn't get written about,
[806.06 --> 806.96]  or no one cares, or whatever.
[807.92 --> 809.30]  So because that was a very, like,
[809.34 --> 811.00]  closely, you know,
[811.10 --> 812.28]  they talked a lot,
[812.68 --> 813.86]  there was this idea,
[813.96 --> 815.30]  because Valve really wanted
[815.30 --> 816.92]  to do Linux stuff,
[816.96 --> 818.58]  and there isn't great debugging tools
[818.58 --> 819.82]  that game developers are used to.
[819.86 --> 821.20]  And again, we also need
[821.20 --> 822.54]  a lot of specialized debugging tools
[822.54 --> 824.16]  for debugging things like 3D geometry
[824.16 --> 824.98]  and this sort of stuff.
[825.16 --> 826.26]  So we need things like
[826.26 --> 827.64]  GPU intervention stuff,
[827.64 --> 828.58]  and we need things like
[828.58 --> 830.02]  to be able to visualize vectors
[830.02 --> 830.94]  and all this other stuff
[830.94 --> 832.32]  that you might not need.
[832.38 --> 834.10]  So we need ways to add that, too.
[834.46 --> 835.98]  So how are we going to get this stuff?
[836.52 --> 838.60]  And so what Gabe and Jeff decide
[838.60 --> 839.54]  is they're going to do
[839.54 --> 840.40]  a debugger project
[840.40 --> 841.88]  to get a good debugger
[841.88 --> 842.66]  going on Linux,
[842.86 --> 844.48]  and Valve's going to fund some of it,
[844.56 --> 845.82]  and RAD's going to fund some of it,
[846.10 --> 847.18]  and it's going to happen
[847.18 --> 848.32]  at the RAD offices.
[848.72 --> 851.12]  So they expanded the RAD offices,
[851.30 --> 851.70]  they added,
[851.82 --> 852.72]  there's, like, a new, like,
[852.80 --> 854.28]  area that got added on.
[855.12 --> 855.92]  They, like, grew
[855.92 --> 857.12]  and took over a little bit
[857.12 --> 857.90]  more of the floor.
[858.44 --> 858.88]  I assume,
[859.14 --> 859.96]  people seem to like
[859.96 --> 861.26]  when I go on Ridiculous Storytime,
[861.30 --> 862.54]  so I'm just telling the whole story.
[862.64 --> 863.18]  If this sucks,
[863.30 --> 864.42]  you can stop me at any point.
[864.56 --> 865.08]  Edit it out.
[865.08 --> 865.60]  It's great.
[865.62 --> 866.10]  We love it.
[866.28 --> 867.00]  We love it, Casey.
[867.42 --> 868.94]  Leave a comment on YouTube
[868.94 --> 869.36]  if you love this.
[869.36 --> 870.32]  I love the BC, yeah,
[870.36 --> 871.12]  I love the BC,
[871.26 --> 872.84]  and I can't wait for the AD coming up,
[872.88 --> 873.76]  so I'm super stoked on both sides.
[873.76 --> 874.58]  Yeah, well, Ryan will take the AD.
[874.74 --> 875.64]  We're going to hand it off,
[875.70 --> 876.84]  and then Ryan's going to do the AD.
[877.82 --> 879.30]  And so they had some people there,
[879.38 --> 880.24]  but it was always hard
[880.24 --> 881.16]  to get a team of people
[881.16 --> 882.26]  who actually would, like,
[882.32 --> 883.22]  get it to the point,
[883.28 --> 884.68]  like, where it needed to be,
[884.76 --> 887.18]  and, like, largely that was because
[887.18 --> 889.60]  debuggers are kind of,
[889.74 --> 891.10]  I guess if I had to say,
[891.66 --> 892.60]  how have I described them?
[893.40 --> 894.56]  They straddle a really
[894.56 --> 895.66]  uncomfortable boundary.
[895.66 --> 899.34]  You know, these nuts jokes aside,
[899.48 --> 901.16]  the straddle is very uncomfortable
[901.16 --> 903.64]  for a lot of programmers
[903.64 --> 905.82]  if they have to tackle it
[905.82 --> 909.12]  sort of, like, holistically,
[909.38 --> 910.10]  might be the way,
[910.64 --> 913.92]  or, like, head on, let's say.
[914.52 --> 915.92]  If they have to come at it
[915.92 --> 916.62]  from the front,
[917.02 --> 919.12]  then the straddle is very difficult.
[919.72 --> 921.00]  I just have to say, Casey,
[922.32 --> 923.76]  you've been hanging out with us a lot,
[923.80 --> 924.38]  and I love this.
[924.38 --> 924.66]  Okay.
[925.20 --> 926.86]  I feel like I'm allowed
[926.86 --> 928.06]  to say these sorts of things here,
[928.12 --> 928.60]  so I do.
[928.80 --> 929.04]  Yes.
[929.30 --> 930.26]  It's a safe space.
[930.36 --> 930.94]  It's a safe space.
[931.00 --> 933.58]  So, what I mean by that is
[933.58 --> 935.62]  it's a project that crosses
[935.62 --> 938.74]  between UI sort of, like,
[938.78 --> 940.40]  I need to know how to create
[940.40 --> 943.48]  visualizations and interactive things
[943.48 --> 945.44]  that show a lot of information
[945.44 --> 946.84]  in highly structured ways.
[947.08 --> 949.38]  If I had to rank programs
[949.38 --> 951.40]  by what is the hardest kind
[951.40 --> 953.30]  to write the front end for,
[953.30 --> 954.18]  it's actually debugger.
[954.80 --> 954.92]  Agreed.
[954.92 --> 956.36]  It is literally the hardest problem
[956.36 --> 957.02]  that I know of.
[957.06 --> 958.16]  If you wanted to see
[958.16 --> 959.52]  if a UI programmer
[959.52 --> 960.88]  is actually great
[960.88 --> 961.98]  or just kind of mediocre,
[962.52 --> 963.72]  have them try to do a debugger
[963.72 --> 965.02]  and see what you get out of it.
[965.12 --> 965.26]  Right?
[965.34 --> 966.12]  Because it is literally,
[966.12 --> 967.58]  I do not know of a harder problem
[967.58 --> 968.62]  that you would have to solve
[968.62 --> 971.62]  other than debugging, really.
[972.16 --> 972.20]  Right?
[972.20 --> 972.52]  Yeah.
[972.52 --> 973.74]  Ryan agrees wholeheartedly.
[973.86 --> 974.08]  He's like,
[974.14 --> 974.86]  you're so right, Casey.
[974.94 --> 974.96]  Yes.
[974.96 --> 975.20]  100.
[975.60 --> 976.42]  Yeah, totally.
[976.42 --> 977.42]  100%.
[978.20 --> 980.52]  I mean, maybe you could argue
[980.52 --> 982.14]  that, like, 3D editor,
[982.28 --> 982.86]  like, Blender,
[983.00 --> 984.54]  because it integrates the 3D part,
[984.68 --> 985.90]  like, those are the two
[985.90 --> 986.82]  that come to mind,
[986.82 --> 987.72]  and they each have
[987.72 --> 989.20]  kind of different stress points.
[989.76 --> 991.28]  Ryan decided to do both
[991.28 --> 992.64]  by adding 3D visualization
[992.64 --> 993.64]  to the debugger,
[993.72 --> 994.60]  so that's, you know,
[994.62 --> 995.18]  where he's at.
[995.62 --> 998.10]  But you have the hardest UI problem
[998.10 --> 999.60]  or close to the hardest UI problem
[999.60 --> 1000.28]  on one side,
[1000.36 --> 1001.44]  and then you have, like,
[1001.80 --> 1003.66]  system-level process control,
[1003.86 --> 1004.86]  register inspection,
[1004.86 --> 1005.96]  module loading,
[1006.02 --> 1006.82]  and disassembly
[1006.82 --> 1007.68]  on the other side,
[1007.72 --> 1009.80]  which is all ultra-low level,
[1009.98 --> 1010.24]  right?
[1010.78 --> 1012.40]  So when you put those two together,
[1012.50 --> 1014.34]  it's really hard to find
[1014.34 --> 1015.40]  a group of people
[1015.40 --> 1016.58]  who can actually go
[1016.58 --> 1017.98]  from zero to debugger.
[1018.22 --> 1020.18]  It's really, really difficult.
[1020.82 --> 1022.60]  And the project
[1022.60 --> 1023.90]  never really got off the ground
[1023.90 --> 1025.20]  because it just didn't have
[1025.20 --> 1026.00]  the right mix of people
[1026.00 --> 1027.26]  to actually make that happen.
[1027.36 --> 1028.80]  I'll spare the gory details of that.
[1029.92 --> 1030.32]  But.
[1030.92 --> 1031.90]  Can I jump in
[1031.90 --> 1032.66]  for one quick second?
[1032.98 --> 1034.08]  As many seconds as you want.
[1034.12 --> 1034.82]  It's your show, Prime.
[1035.08 --> 1036.04]  No, it's our show.
[1036.04 --> 1037.22]  It's our show.
[1037.54 --> 1037.56]  But.
[1037.82 --> 1038.40]  Oh, wow.
[1038.48 --> 1039.22]  Oh, my God.
[1039.22 --> 1040.92]  I'm feeling the love over here.
[1041.18 --> 1041.58]  Thank you.
[1041.90 --> 1043.28]  One reason why I've historically
[1043.28 --> 1045.30]  keep using Vim
[1045.30 --> 1047.20]  and then integrating DAPT,
[1047.34 --> 1048.62]  debugger adapter protocol,
[1049.00 --> 1050.84]  and then not using it
[1050.84 --> 1052.14]  is because the Vim UI
[1052.14 --> 1053.10]  just does not feel
[1053.10 --> 1054.14]  currently kind of set up
[1054.14 --> 1054.70]  for debugger
[1054.70 --> 1055.44]  because I do believe
[1055.44 --> 1056.20]  a debugger UI
[1056.20 --> 1057.84]  is a very visual experience.
[1058.06 --> 1058.86]  It is not like a,
[1059.38 --> 1060.48]  it's not just a separate
[1060.48 --> 1062.20]  buffers and text.
[1062.32 --> 1063.18]  There's more to it
[1063.18 --> 1063.68]  and every time
[1063.68 --> 1064.68]  it just feels very clunky.
[1064.74 --> 1065.28]  So I agree with you.
[1065.66 --> 1067.34]  UIs are like super duper hard
[1067.34 --> 1068.46]  to be able to build.
[1069.08 --> 1069.34]  Yes.
[1070.06 --> 1071.38]  And debugger UIs
[1071.38 --> 1072.38]  because they have to marshal
[1072.38 --> 1073.34]  so much information
[1073.34 --> 1074.66]  and the entire value
[1074.66 --> 1075.36]  of the debugger
[1075.36 --> 1076.70]  is can it present,
[1077.06 --> 1077.78]  is can it allow you
[1077.78 --> 1079.48]  to edit that information display
[1079.48 --> 1080.84]  and update and present
[1080.84 --> 1081.92]  that information display
[1081.92 --> 1083.16]  as smoothly
[1083.16 --> 1084.40]  and as quickly as possible.
[1084.62 --> 1085.70]  Because there are plenty of debuggers.
[1086.46 --> 1086.90]  WinDBG
[1086.90 --> 1088.52]  would be a classic example
[1088.52 --> 1089.22]  of a debugger
[1089.22 --> 1090.64]  that has all the features
[1090.64 --> 1091.52]  under the hood
[1091.52 --> 1092.92]  and is largely
[1092.92 --> 1094.06]  completely unusable
[1094.06 --> 1095.18]  99% of the time.
[1095.28 --> 1096.50]  Like you will only fire it up
[1096.50 --> 1097.76]  if you need a feature
[1097.76 --> 1098.58]  that only it has
[1098.58 --> 1099.54]  like time travel debugging.
[1099.92 --> 1101.16]  Otherwise it's completely useless
[1101.16 --> 1101.96]  because the amount of time
[1101.96 --> 1102.66]  it will take you
[1102.66 --> 1104.10]  to actually set it up
[1104.10 --> 1105.42]  to do the debugging you want,
[1105.56 --> 1106.40]  you could have just done
[1106.40 --> 1107.14]  your printout, right?
[1107.18 --> 1108.80]  Like it's the canonical example
[1108.80 --> 1109.56]  of what we were talking about
[1109.56 --> 1109.92]  at the beginning
[1109.92 --> 1110.88]  where it's like anyone
[1110.88 --> 1112.50]  who was given only WinDBG
[1112.50 --> 1112.86]  and was like,
[1112.94 --> 1113.84]  I pretty much only use printout debugging.
[1113.92 --> 1114.68]  I'm like, yep, me too.
[1114.98 --> 1116.18]  Yep, like absolutely, right?
[1116.92 --> 1118.80]  So anyway,
[1119.22 --> 1120.56]  the project kind of languished
[1120.56 --> 1121.62]  as a result of this.
[1121.70 --> 1122.70]  So really not much
[1122.70 --> 1124.50]  actual usable work happened
[1124.50 --> 1125.30]  between, you know,
[1125.60 --> 1126.54]  that when it's actually,
[1126.64 --> 1128.54]  it started in the early 2010s
[1128.54 --> 1129.80]  and later.
[1129.92 --> 1131.60]  Now I tried to hire Ryan,
[1132.14 --> 1132.76]  full disclosure,
[1133.54 --> 1134.42]  out of college.
[1135.04 --> 1136.88]  Like not when he finished college
[1136.88 --> 1137.86]  but while I was in college.
[1137.96 --> 1138.80]  I was like, hey,
[1139.10 --> 1142.10]  do you want to come work on this?
[1143.56 --> 1145.20]  And he turned us down.
[1145.20 --> 1146.72]  So that didn't work out.
[1147.42 --> 1148.92]  So eventually,
[1149.70 --> 1150.30]  eventually.
[1150.30 --> 1150.66]  You just wanted him
[1150.66 --> 1151.40]  to come on the pod
[1151.40 --> 1152.66]  to air the dirty laundry case?
[1152.66 --> 1152.94]  Yes.
[1152.94 --> 1153.68]  I love it.
[1153.68 --> 1154.68]  And suck it, Ryan.
[1154.80 --> 1155.82]  We hate your guts.
[1155.94 --> 1156.24]  Yeah.
[1156.38 --> 1157.00]  We hate you.
[1157.10 --> 1157.98]  I came later.
[1158.06 --> 1158.82]  I don't know what to say.
[1158.82 --> 1159.26]  I love it.
[1159.28 --> 1160.84]  I was so delighted.
[1161.22 --> 1162.38]  I was super happy
[1162.38 --> 1164.16]  but I was so unhappy then.
[1164.22 --> 1165.12]  I'm like, damn it.
[1165.16 --> 1165.48]  All right.
[1165.66 --> 1167.24]  I should have been more aggressive.
[1167.78 --> 1168.18]  But anyway,
[1168.84 --> 1170.92]  so we tried to hire Ryan
[1170.92 --> 1171.80]  and that didn't work out.
[1171.80 --> 1174.16]  But eventually,
[1174.16 --> 1175.24]  it does work out
[1175.24 --> 1176.64]  and not only do we get Ryan
[1176.64 --> 1178.00]  but we got Nick
[1178.00 --> 1179.66]  and we also got Alan Webster.
[1179.88 --> 1181.56]  So like three people.
[1181.72 --> 1182.22]  And also,
[1182.38 --> 1182.56]  I mean,
[1182.62 --> 1184.02]  I guess Martin's never really
[1184.02 --> 1184.76]  went on that project
[1184.76 --> 1185.54]  but he was another person
[1185.54 --> 1186.12]  I tried to hire
[1186.12 --> 1186.68]  and succeeded.
[1186.68 --> 1190.82]  So out of those four people
[1190.82 --> 1192.12]  that I tried to hire,
[1192.28 --> 1193.68]  we ended up getting all four
[1193.68 --> 1196.14]  and through some combination of them
[1196.14 --> 1198.02]  then they were basically able to reboot
[1198.02 --> 1199.86]  and successfully complete this project.
[1200.84 --> 1202.52]  And now it's like
[1202.52 --> 1204.18]  it's a totally usable debugger already
[1204.18 --> 1204.92]  even though technically
[1204.92 --> 1205.52]  it's only in alpha
[1205.52 --> 1207.02]  and they really haven't been working on it
[1207.02 --> 1207.62]  that long
[1207.62 --> 1209.52]  because even though the project was very long
[1209.52 --> 1211.56]  most of it was not actually usable.
[1211.90 --> 1212.16]  So anyway,
[1212.50 --> 1213.42]  Ryan can now pick it up
[1213.42 --> 1215.26]  from that sort of modern era.
[1215.34 --> 1216.04]  How did it happen?
[1217.30 --> 1217.44]  Yeah,
[1217.52 --> 1220.04]  so I came on board in 2021
[1220.04 --> 1221.32]  and I think Alan,
[1221.68 --> 1222.98]  I don't remember when Nick joined
[1222.98 --> 1224.02]  but I think maybe Alan
[1224.02 --> 1224.94]  was slightly before Nick
[1224.94 --> 1226.22]  but Alan and Nick showed up
[1226.22 --> 1227.20]  and they were working on,
[1227.82 --> 1229.12]  Alan had inherited the project
[1229.12 --> 1230.82]  from Wan Chun,
[1231.10 --> 1231.66]  I believe.
[1232.24 --> 1232.52]  And he,
[1232.72 --> 1233.78]  so he had a bunch of stuff
[1233.78 --> 1234.34]  and it's,
[1234.88 --> 1235.68]  the thing about debuggers
[1235.68 --> 1236.38]  is that there's like
[1236.38 --> 1237.44]  a thousand problems
[1237.44 --> 1238.52]  like you have to know
[1238.52 --> 1239.84]  how to parse debug info formats.
[1240.22 --> 1241.30]  Everything that Casey was talking about,
[1241.36 --> 1242.02]  you need to know
[1242.02 --> 1242.98]  how to do process control.
[1243.14 --> 1244.12]  Reading registers even
[1244.12 --> 1245.52]  is like more work
[1245.52 --> 1246.14]  than it might seem
[1246.14 --> 1246.80]  like it would be.
[1247.52 --> 1247.54]  And,
[1247.60 --> 1248.96]  and so they have all this
[1248.96 --> 1249.58]  binary too.
[1249.70 --> 1250.62]  Like you have to be like
[1250.62 --> 1252.06]  patch the binary for breaks
[1252.06 --> 1253.14]  and data breakpoints
[1253.14 --> 1253.94]  and all this crap.
[1254.06 --> 1254.56]  It's huge.
[1254.64 --> 1254.82]  Yep.
[1255.14 --> 1255.34]  Yeah.
[1255.34 --> 1256.12]  Like even how to implement
[1256.12 --> 1257.00]  like line stepping
[1257.00 --> 1257.80]  is already like,
[1257.92 --> 1258.26]  that's a,
[1258.38 --> 1259.86]  that's a deep rabbit hole already.
[1259.86 --> 1260.66]  Um,
[1260.98 --> 1261.28]  so,
[1261.28 --> 1262.02]  uh,
[1262.38 --> 1263.48]  there was a ton of work
[1263.48 --> 1264.30]  done in that direction.
[1264.30 --> 1264.80]  And then,
[1264.84 --> 1265.20]  um,
[1265.26 --> 1266.30]  once Wan had left,
[1266.38 --> 1267.42]  Alan sort of,
[1267.84 --> 1268.12]  uh,
[1268.24 --> 1269.34]  Alan and Nick worked together
[1269.34 --> 1271.26]  on a bunch of the problems around.
[1271.38 --> 1272.40]  I think Alan was focusing
[1272.40 --> 1273.72]  mostly on the debugger stuff.
[1273.84 --> 1274.74]  Nick was working on,
[1275.26 --> 1275.56]  um,
[1275.74 --> 1276.74]  Nick is really good at like
[1276.74 --> 1277.84]  reverse engineering,
[1277.84 --> 1280.46]  like how the PDB format
[1280.46 --> 1281.30]  stores certain things
[1281.30 --> 1282.34]  or how do you do unwinding,
[1282.34 --> 1283.08]  uh,
[1283.12 --> 1283.38]  you know,
[1283.38 --> 1284.36]  in this particular case
[1284.36 --> 1286.12]  or all that sort of family
[1286.12 --> 1286.76]  of problems.
[1286.76 --> 1288.10]  Nick is really good at kind of
[1288.10 --> 1289.64]  drilling deep and figuring out
[1289.64 --> 1290.50]  how that actually works.
[1290.60 --> 1291.28]  So he was kind of working
[1291.28 --> 1291.72]  on that stuff.
[1291.82 --> 1293.58]  Alan was trying to think,
[1293.74 --> 1294.76]  like work through the problem
[1294.76 --> 1295.10]  of like,
[1295.16 --> 1296.12]  how do you actually build,
[1296.26 --> 1296.42]  like,
[1296.88 --> 1297.22]  um,
[1297.30 --> 1297.94]  how do you actually build
[1297.94 --> 1299.32]  an architecture for the actual
[1299.32 --> 1300.64]  debugger sort of engine,
[1300.80 --> 1300.88]  if,
[1300.94 --> 1301.36]  if you will.
[1301.88 --> 1302.24]  Um,
[1302.30 --> 1303.14]  and then I joined
[1303.14 --> 1305.78]  and my role initially
[1305.78 --> 1306.74]  was sort of like,
[1306.94 --> 1307.74]  I was helping with a bunch
[1307.74 --> 1308.94]  of the debug info parsing stuff,
[1308.94 --> 1310.44]  but I was going to build the UI.
[1310.58 --> 1311.50]  Like that was the end goal.
[1311.62 --> 1312.66]  Like I would be on the UI,
[1312.76 --> 1313.74]  like the front end side,
[1314.54 --> 1315.66]  Alan would be doing the engine.
[1315.66 --> 1316.68]  Nick would be doing like
[1316.68 --> 1317.54]  debug info format,
[1317.66 --> 1318.10]  parsing,
[1318.38 --> 1318.78]  unwinding,
[1318.94 --> 1320.06]  like figuring that stuff out.
[1320.74 --> 1321.14]  Um,
[1321.30 --> 1324.32]  and for a while we were just
[1324.32 --> 1325.60]  working on debug info parsing.
[1325.66 --> 1326.40]  So that was 2021
[1326.40 --> 1329.74]  and maybe six months in
[1329.74 --> 1330.48]  or eight months in,
[1330.54 --> 1331.26]  I built like,
[1331.84 --> 1332.74]  I switched over to building
[1332.74 --> 1333.88]  like a little prototype debugger
[1333.88 --> 1334.64]  just so I could like
[1334.64 --> 1335.54]  familiarize myself
[1335.54 --> 1336.44]  with the problem space.
[1336.90 --> 1338.46]  That has been like thrown away.
[1338.56 --> 1339.00]  So that's not,
[1339.08 --> 1340.82]  that's no longer in the code base,
[1340.84 --> 1341.36]  but it was just like
[1341.36 --> 1342.16]  a really crappy little,
[1342.24 --> 1342.34]  like,
[1342.34 --> 1342.94]  let me figure out
[1342.94 --> 1344.08]  how you even do things
[1344.08 --> 1344.58]  like stepping.
[1344.58 --> 1346.96]  Like how do you actually specify
[1346.96 --> 1348.76]  how a step is even supposed to happen?
[1349.76 --> 1350.02]  Um,
[1350.20 --> 1350.96]  and,
[1351.08 --> 1351.68]  and then,
[1351.68 --> 1352.42]  um,
[1353.68 --> 1355.18]  Alan worked,
[1355.30 --> 1356.32]  the last thing he worked on
[1356.32 --> 1356.62]  before,
[1356.62 --> 1357.10]  uh,
[1357.10 --> 1359.02]  he left was the,
[1359.48 --> 1361.20]  we also have a custom debug info format.
[1361.20 --> 1363.06]  So both PDB and dwarf,
[1363.16 --> 1363.52]  one of the,
[1363.66 --> 1364.94]  so one of the problems
[1364.94 --> 1365.46]  you have to deal with,
[1365.46 --> 1365.98]  with debuggers,
[1366.04 --> 1367.46]  especially one that tries to ship
[1367.46 --> 1368.78]  to both Windows and Linux,
[1369.10 --> 1369.98]  is you have to deal with like
[1369.98 --> 1372.16]  the situation of the different tool chains.
[1372.42 --> 1373.96]  One of the realities of that situation
[1373.96 --> 1375.90]  is that these two different tool chains
[1375.90 --> 1377.60]  use completely different debug info formats,
[1377.78 --> 1379.48]  both of which are extremely complicated.
[1380.10 --> 1380.46]  Um,
[1380.60 --> 1380.82]  and,
[1380.94 --> 1381.82]  and they're very different
[1381.82 --> 1382.86]  in how they actually organize
[1382.86 --> 1383.74]  and slice information.
[1384.38 --> 1385.04]  And so,
[1385.62 --> 1386.00]  um,
[1386.52 --> 1388.46]  we had kind of always talked,
[1388.58 --> 1388.90]  at least for,
[1389.08 --> 1389.82]  I'm sure they talked
[1389.82 --> 1390.62]  before I even got there,
[1390.68 --> 1390.82]  but,
[1391.18 --> 1391.50]  uh,
[1391.66 --> 1392.78]  while I was there also,
[1392.84 --> 1393.66]  we were talking about like,
[1394.08 --> 1395.48]  this debug info format problem
[1395.48 --> 1397.72]  is really difficult to deal with actually.
[1398.00 --> 1398.34]  And so,
[1398.62 --> 1399.90]  if we could actually move
[1399.90 --> 1400.96]  to our own format instead,
[1401.16 --> 1401.28]  and,
[1401.28 --> 1402.90]  and if you start with PDB and dwarf,
[1402.98 --> 1404.52]  you can convert to our format
[1404.52 --> 1405.86]  and then build the debugger on that
[1405.86 --> 1406.74]  and then it works everywhere.
[1407.00 --> 1408.14]  You don't have to deal with like
[1408.14 --> 1409.14]  an abstraction layer,
[1409.26 --> 1409.66]  for example,
[1409.76 --> 1409.88]  over,
[1410.08 --> 1411.76]  over incrementally parsing dwarf or PDB.
[1411.84 --> 1413.10]  It gets really nasty really quick.
[1413.72 --> 1414.00]  Um,
[1414.28 --> 1415.22]  we tried to do that
[1415.22 --> 1415.90]  and then it was like,
[1415.92 --> 1417.52]  it turned out to be really complicated.
[1417.52 --> 1417.96]  And so,
[1418.30 --> 1418.46]  uh,
[1418.46 --> 1419.34]  the last thing Alan did
[1419.34 --> 1420.46]  was he designed the first version
[1420.46 --> 1421.98]  of that debug info format.
[1423.02 --> 1424.62]  We should mention Alan's not there anymore.
[1424.76 --> 1426.26]  So that's why it's like the last thing he did
[1426.26 --> 1427.80]  because he left shortly after that.
[1427.88 --> 1427.96]  Yeah.
[1428.38 --> 1428.68]  Yeah.
[1428.78 --> 1428.98]  Yeah.
[1429.02 --> 1429.18]  Yeah.
[1429.24 --> 1429.50]  So,
[1429.82 --> 1430.22]  um,
[1430.66 --> 1431.44]  and then at that point,
[1431.46 --> 1431.96]  once he left,
[1432.04 --> 1432.28]  I,
[1432.48 --> 1434.06]  I was building the UI for,
[1434.16 --> 1434.74]  for the debugger.
[1434.74 --> 1436.52]  And then I just sort of took over the pieces
[1436.52 --> 1437.16]  that he had,
[1437.42 --> 1438.22]  he had written.
[1438.22 --> 1439.14]  And I either,
[1439.14 --> 1439.68]  uh,
[1440.74 --> 1441.58]  I either took them over,
[1441.74 --> 1442.04]  rewrote,
[1442.10 --> 1442.54]  rewrote them,
[1442.56 --> 1443.16]  or they kind of like,
[1443.30 --> 1443.54]  you know,
[1443.58 --> 1444.52]  dissipated because,
[1444.52 --> 1445.04]  um,
[1445.82 --> 1446.08]  you know,
[1446.08 --> 1446.82]  it's just as the,
[1446.90 --> 1447.76]  as the system evolves,
[1447.76 --> 1448.82]  if there was a layer that he wrote
[1448.82 --> 1449.68]  that I wasn't familiar with,
[1449.70 --> 1450.12]  I was like,
[1450.22 --> 1450.52]  I don't,
[1450.64 --> 1451.74]  I'm not really sure what to do with this.
[1451.82 --> 1452.94]  I'll rewrite that part or whatever.
[1453.50 --> 1453.86]  So,
[1454.02 --> 1454.76]  so,
[1454.90 --> 1455.22]  um,
[1455.30 --> 1456.58]  understanding to replacement.
[1457.36 --> 1457.72]  Yes,
[1457.84 --> 1458.50]  exactly.
[1459.14 --> 1460.52]  So I kind of,
[1460.64 --> 1461.08]  at that point,
[1461.08 --> 1462.78]  I took over most of the debugger stuff.
[1462.96 --> 1463.16]  Nick,
[1463.36 --> 1465.16]  Nick actually works on a linker.
[1465.16 --> 1467.26]  This is another very deep rabbit hole
[1467.26 --> 1468.08]  we could get into.
[1468.40 --> 1469.52]  So Nick works mostly on the linker,
[1469.58 --> 1471.12]  but he still does a bunch of like the,
[1471.42 --> 1473.44]  like he built the dwarf format
[1473.44 --> 1475.48]  to our debug info format called RDI.
[1475.78 --> 1477.62]  He built that converter recently.
[1477.90 --> 1478.12]  Um,
[1478.12 --> 1478.54]  it's still,
[1478.66 --> 1479.14]  it's still early,
[1479.20 --> 1479.40]  but he,
[1479.40 --> 1481.40]  he did like a first pass on it.
[1481.68 --> 1482.06]  Um,
[1482.06 --> 1483.36]  so he's working on problems
[1483.36 --> 1484.72]  that overlap with the debugger,
[1484.76 --> 1485.14]  but he,
[1485.34 --> 1486.90]  he spent most of his time over the past
[1486.90 --> 1487.92]  like year or two,
[1488.02 --> 1490.08]  maybe a year and a half on the linker.
[1490.76 --> 1492.20]  And then I've just been on the debugger.
[1492.28 --> 1492.48]  So,
[1493.34 --> 1493.72]  and the,
[1493.82 --> 1494.54]  I guess that's,
[1494.54 --> 1495.14]  that's the story.
[1495.16 --> 1495.96]  The story of the project.
[1496.12 --> 1496.88]  What it actually is,
[1496.92 --> 1498.28]  is it's a graphical debugger
[1498.28 --> 1502.10]  that you can debug your programs with.
[1502.62 --> 1503.16]  So one thing,
[1503.30 --> 1504.86]  one thing that I think people,
[1505.20 --> 1506.30]  so one of the things
[1506.30 --> 1507.48]  that I was literally complaining about
[1507.48 --> 1508.46]  on Twitter just recently
[1508.46 --> 1509.30]  was people are like,
[1509.38 --> 1509.48]  well,
[1509.52 --> 1510.98]  game programmers just don't understand
[1510.98 --> 1512.16]  all like the real problems
[1512.16 --> 1513.60]  that banking people face
[1513.60 --> 1514.30]  or something like this,
[1514.30 --> 1515.66]  which is one of the most absurd things
[1515.66 --> 1516.24]  I've ever heard.
[1516.24 --> 1517.44]  And I'm really sick of it,
[1517.44 --> 1518.30]  but like,
[1518.34 --> 1520.86]  just to underscore how like much
[1520.86 --> 1522.30]  that kind of thing is ridiculous.
[1522.30 --> 1525.50]  I have not ever actually heard
[1525.50 --> 1528.44]  of any other project besides Fortnite
[1528.44 --> 1530.82]  that hit the limit of PDB.
[1531.30 --> 1531.98]  Yeah.
[1532.14 --> 1536.14]  So the literal output of debug information
[1536.14 --> 1537.14]  on Windows,
[1537.54 --> 1540.28]  Fortnite got so large as a project,
[1540.28 --> 1542.40]  it could no longer be built
[1542.40 --> 1545.66]  because the debug info could not be stored.
[1545.66 --> 1548.14]  I just want to,
[1548.20 --> 1549.36]  there's a file limit size,
[1549.44 --> 1549.60]  right?
[1549.68 --> 1551.26]  That exists on Windows.
[1551.44 --> 1551.78]  So if you,
[1551.88 --> 1552.20]  you know,
[1552.20 --> 1554.62]  it's not a file limit size on Windows.
[1554.72 --> 1556.54]  It's a file limit size in PDB.
[1556.88 --> 1558.02]  The way that one of the sections,
[1558.20 --> 1558.34]  yeah,
[1558.44 --> 1559.60]  one of the sections 32 bit.
[1559.84 --> 1560.06]  Yeah.
[1560.10 --> 1561.30]  They use 32 bit offsets.
[1561.40 --> 1561.62]  Actually,
[1561.62 --> 1563.14]  they use signed 32 bit offsets
[1563.14 --> 1564.72]  into like,
[1564.72 --> 1565.14]  it's like the,
[1565.28 --> 1567.00]  one of the type information sections.
[1567.00 --> 1568.36]  And so once you get enough types,
[1568.36 --> 1569.46]  and especially once you're doing like
[1569.46 --> 1571.48]  heavy C++ template metaprogramming
[1571.48 --> 1572.76]  or lots of Lambda functions,
[1572.82 --> 1573.50]  those generate types,
[1573.58 --> 1574.88]  every single one of those generates types.
[1574.88 --> 1575.98]  And so you get this just
[1575.98 --> 1577.96]  massive expansion of type information.
[1578.28 --> 1578.42]  Yeah.
[1578.48 --> 1579.92]  And then you run out of that space
[1579.92 --> 1581.06]  like pretty quick once you're at.
[1581.06 --> 1581.92]  So JP Morgan,
[1582.42 --> 1583.68]  call me up and let me know
[1583.68 --> 1585.64]  when you had to write your own linker
[1585.64 --> 1588.00]  because you exceeded the PDB file size.
[1588.08 --> 1588.46]  I'll wait.
[1589.24 --> 1590.64]  I was wondering though,
[1590.72 --> 1591.20]  like Ryan,
[1591.30 --> 1592.64]  which collab was it
[1592.64 --> 1593.70]  that pushed them over the limit?
[1593.80 --> 1594.84]  Was it like Star Wars?
[1595.22 --> 1595.74]  Or was it like,
[1595.80 --> 1597.14]  which one was the...
[1597.14 --> 1598.64]  That's a good question.
[1599.00 --> 1599.32]  You know,
[1599.66 --> 1600.10]  oh my goodness,
[1600.16 --> 1601.66]  it might have been all the Star Wars characters.
[1601.84 --> 1602.04]  Oops,
[1602.10 --> 1603.26]  it's the Pokemon collabs.
[1603.26 --> 1603.64]  You know,
[1603.64 --> 1605.14]  we gotta make sure it's got all the Pokemon.
[1605.82 --> 1606.04]  You know,
[1606.10 --> 1607.98]  I think it might have been the Snoop Dogg skins.
[1607.98 --> 1610.34]  Like when they added the Snoop Dogg,
[1610.34 --> 1610.66]  you know,
[1610.80 --> 1611.74]  doggy dog skins.
[1612.06 --> 1613.16]  That was like,
[1613.26 --> 1614.12]  this is too much.
[1614.32 --> 1616.26]  It was when they stored all the Darth Vader voice lines
[1616.26 --> 1617.08]  that got them in trouble.
[1617.42 --> 1617.72]  Yeah.
[1618.92 --> 1619.14]  Yeah.
[1619.14 --> 1619.38]  Well,
[1619.38 --> 1621.00]  Sabrina Carpenter lyrics,
[1621.22 --> 1623.62]  they don't get compressed very well in the PDB.
[1623.82 --> 1625.52]  So the problem is like that just,
[1625.72 --> 1627.76]  and it was a problem and it's fine.
[1628.36 --> 1629.28]  But most of the songs,
[1629.40 --> 1629.72]  like six,
[1629.92 --> 1631.42]  like six different words.
[1631.60 --> 1632.74]  They just don't compress very well.
[1632.74 --> 1633.86]  Cause they're so creative,
[1634.00 --> 1634.32]  teach.
[1634.40 --> 1634.62]  Right.
[1635.32 --> 1635.52]  Teach.
[1635.52 --> 1635.88]  Sorry.
[1635.98 --> 1637.32]  They're practically white noise.
[1637.42 --> 1638.04]  They're so creative.
[1638.38 --> 1638.78]  They wanted,
[1638.92 --> 1640.84]  they wanted to compute them at compile time too.
[1640.94 --> 1644.08]  So each word was a template instantiation.
[1644.08 --> 1645.94]  And so that's why there's so many types.
[1646.14 --> 1646.66]  That makes sense.
[1646.76 --> 1647.24]  That makes sense.
[1647.40 --> 1649.60]  So long story short,
[1649.68 --> 1654.36]  there are some pretty cool things about this that if you read between the lines are there,
[1654.44 --> 1655.52]  that's really awesome.
[1655.52 --> 1656.96]  And I think will be very,
[1657.08 --> 1658.54]  very interesting to people going forwards.
[1659.08 --> 1660.70]  One is rad.
[1660.70 --> 1662.66]  It did release the linker,
[1662.76 --> 1667.10]  which means that now if you want to bypass the entire crappy,
[1667.10 --> 1670.78]  like Microsoft and or Clang linking scenario on windows,
[1670.90 --> 1671.28]  at least,
[1671.86 --> 1673.34]  and eventually presumably Linux,
[1673.34 --> 1674.08]  you can,
[1674.22 --> 1677.06]  you can have a much faster linker that produces RDI.
[1677.66 --> 1679.62]  Is it RDI is the name of the file type or something?
[1680.24 --> 1680.64]  Yeah.
[1680.98 --> 1681.42]  Directly.
[1681.48 --> 1683.44]  So you can have that debug info,
[1683.58 --> 1686.82]  which is more efficient to use and much more like well-documented.
[1687.10 --> 1687.12]  And,
[1687.16 --> 1687.62]  and like,
[1687.68 --> 1688.38]  this is easy,
[1688.44 --> 1688.56]  you know,
[1688.58 --> 1689.66]  it's easy to kind of get into.
[1689.76 --> 1690.66]  That's pretty awesome.
[1691.12 --> 1691.88]  But two,
[1692.22 --> 1693.36]  those RDIs also,
[1693.48 --> 1696.14]  now there's like this convenient sort of thing you can look at where it's like,
[1696.22 --> 1696.90]  here's a code base.
[1697.04 --> 1700.42]  If you would like to access the debug information for your own programs,
[1700.58 --> 1702.66]  to write your own instrumentation tools,
[1702.66 --> 1704.12]  your own inspection tools,
[1704.22 --> 1705.32]  your own metaprogramming tools,
[1705.38 --> 1706.30]  whatever you want.
[1706.68 --> 1707.04]  Now,
[1707.14 --> 1710.04]  Rad has done that for you or Epic has done that for you.
[1710.04 --> 1710.26]  Right.
[1710.92 --> 1712.46]  And so this,
[1712.54 --> 1716.02]  this project has a lot more cool stuff in it than just the debugger.
[1716.02 --> 1719.60]  Cause they chose to tackle a bunch of other hard problems at the same time and succeeded.
[1719.60 --> 1720.90]  I got a question for you,
[1720.96 --> 1721.16]  Ryan,
[1721.60 --> 1721.98]  uh,
[1721.98 --> 1723.38]  as someone who also worked at Epic,
[1723.48 --> 1724.26]  but a different one,
[1724.60 --> 1725.12]  uh,
[1725.32 --> 1725.80]  how,
[1726.18 --> 1727.02]  how often,
[1727.10 --> 1728.46]  like on a weekly basis,
[1728.46 --> 1730.34]  after you tell someone you work at Epic,
[1730.42 --> 1730.74]  do you get,
[1731.22 --> 1731.42]  whoa,
[1731.50 --> 1731.64]  bro,
[1731.68 --> 1733.36]  that's Epic every time.
[1733.48 --> 1733.66]  Like,
[1733.74 --> 1734.98]  cause I feel like it's,
[1735.06 --> 1735.66]  you're like,
[1735.70 --> 1735.96]  guys,
[1736.04 --> 1736.40]  come on.
[1736.46 --> 1736.72]  I'm,
[1736.88 --> 1737.90]  everyone said that joke already.
[1737.90 --> 1738.56]  You can relax.
[1739.50 --> 1740.12]  It definitely,
[1740.12 --> 1740.76]  definitely happened.
[1740.86 --> 1741.24]  It's funny.
[1741.24 --> 1743.14]  Cause I was wearing an Epic shirt to,
[1743.22 --> 1743.62]  um,
[1743.82 --> 1745.32]  to a hospital at some point.
[1745.32 --> 1745.68]  Oh,
[1745.74 --> 1746.62]  yes.
[1747.30 --> 1747.92]  And they're like,
[1747.94 --> 1749.24]  can you help us with this quick?
[1749.66 --> 1749.74]  Like,
[1750.78 --> 1753.28]  just like fix my chart problems really fast.
[1753.42 --> 1753.56]  Yeah.
[1754.04 --> 1754.26]  Yeah.
[1754.46 --> 1755.20]  And like,
[1755.24 --> 1755.66]  it was like,
[1755.76 --> 1759.52]  it was one particular short design where you could see Epic very clearly from a distance,
[1759.56 --> 1761.50]  but you couldn't see the games part very clearly.
[1761.86 --> 1762.84]  And so they were like,
[1762.92 --> 1763.12]  Oh,
[1763.24 --> 1763.50]  Epic.
[1763.64 --> 1763.82]  Yeah.
[1763.82 --> 1764.72]  We use Epic here.
[1764.78 --> 1765.14]  I was like,
[1765.40 --> 1766.84]  don't tell me they're putting on real engine,
[1766.92 --> 1768.76]  like in the MRI machines or whatever.
[1769.06 --> 1770.68]  Like it's a brand new therapy.
[1770.82 --> 1772.12]  We've put them on Fortnite.
[1772.46 --> 1774.76]  It's like the days go so fast.
[1774.76 --> 1775.88]  Before you know it,
[1775.92 --> 1776.34]  you're healed.
[1776.64 --> 1776.82]  You know,
[1776.88 --> 1777.72]  it took six months,
[1777.98 --> 1780.70]  but all the surgeons are like flossing in the room.
[1780.92 --> 1782.26]  Like they're like doing stuff and you're like,
[1782.34 --> 1783.26]  what is happening?
[1783.38 --> 1783.82]  And they're like,
[1783.84 --> 1784.80]  it's an emote.
[1784.98 --> 1785.16]  Sorry.
[1785.30 --> 1786.20]  Don't worry about it.
[1786.34 --> 1788.08]  They always emote after a surgery.
[1788.28 --> 1788.54]  Yeah.
[1789.18 --> 1789.72]  Crushed it,
[1789.80 --> 1790.06]  bro.
[1790.26 --> 1790.56]  Yeah.
[1790.86 --> 1791.28]  Yeah.
[1791.48 --> 1792.06]  New heart,
[1792.32 --> 1792.86]  new heart,
[1793.06 --> 1793.62]  new heart,
[1793.76 --> 1794.28]  new heart.
[1794.38 --> 1795.52]  Closed up that valve.
[1796.26 --> 1796.82]  All right.
[1796.84 --> 1797.34]  So I actually have,
[1797.40 --> 1798.54]  I have a pretty serious question.
[1798.78 --> 1800.10]  Since you do work at Epic,
[1800.10 --> 1801.22]  do you get free Fortnite?
[1803.18 --> 1804.46]  Isn't Fortnite already free?
[1804.76 --> 1808.52]  Yes.
[1809.28 --> 1810.88]  The Sabrina Carpenter skin.
[1811.02 --> 1812.24]  Can you get that for free?
[1812.34 --> 1813.12]  Is what he's asking.
[1813.86 --> 1814.14]  Oh,
[1814.22 --> 1815.40]  just asking for a friend.
[1815.50 --> 1815.82]  Okay.
[1816.38 --> 1816.78]  I see.
[1816.86 --> 1817.18]  I see.
[1817.34 --> 1818.20]  I haven't tried,
[1818.40 --> 1818.76]  but I can,
[1818.82 --> 1819.14]  I can,
[1819.18 --> 1820.30]  I can check for you.
[1820.54 --> 1820.86]  I'll,
[1820.90 --> 1821.06]  I'll,
[1821.12 --> 1821.88]  I'll let you know.
[1821.96 --> 1822.80]  At my Epic,
[1822.96 --> 1825.48]  they had my favorite phrase,
[1825.68 --> 1828.22]  which was consider your salary,
[1828.22 --> 1829.86]  a stipend for that.
[1829.86 --> 1831.24]  Like whenever people are like,
[1831.30 --> 1832.14]  are you kidding me?
[1832.54 --> 1835.56]  Why isn't gym membership included in our paycheck?
[1835.56 --> 1835.88]  Right.
[1835.92 --> 1836.22]  Cause like,
[1836.30 --> 1837.78]  that's the big tech thing to do is like,
[1837.84 --> 1837.96]  right.
[1837.96 --> 1838.16]  Right.
[1838.16 --> 1842.46]  We're going to micromanage your life and give you a hundred extra dollars a month to pay for like a gym.
[1842.54 --> 1842.90]  Right.
[1842.96 --> 1844.36]  And I loved Judy,
[1844.60 --> 1845.62]  Judy on stage,
[1845.86 --> 1847.54]  like 12,000 people answered at one time,
[1847.54 --> 1848.84]  like consider your salary,
[1848.92 --> 1850.32]  a stipend for that.
[1850.40 --> 1852.24]  And I love that so much.
[1852.30 --> 1852.64]  I was like,
[1852.72 --> 1853.28]  yes.
[1853.82 --> 1855.56]  What do you think we are?
[1855.64 --> 1857.44]  Some kind of healthcare company here?
[1858.36 --> 1858.80]  Well,
[1858.82 --> 1858.94]  they,
[1859.04 --> 1860.86]  they did give really good health insurance.
[1860.96 --> 1862.36]  I missed that after I left.
[1862.44 --> 1862.88]  They were like,
[1862.94 --> 1863.22]  you know,
[1863.26 --> 1863.90]  but yes,
[1865.24 --> 1865.58]  but it was,
[1865.64 --> 1865.74]  yeah,
[1865.74 --> 1867.56]  they probably just hack into like,
[1867.62 --> 1867.90]  it's,
[1867.90 --> 1869.00]  it's running all the systems.
[1869.00 --> 1869.44]  It's just,
[1869.50 --> 1872.76]  they set all their employees to zero dollars every time.
[1872.76 --> 1873.12]  Right.
[1873.50 --> 1874.04]  It's like,
[1874.04 --> 1875.38]  we're providing healthcare.
[1875.84 --> 1876.04]  Zero.
[1876.50 --> 1876.66]  Yeah.
[1876.96 --> 1877.30]  Oh yeah.
[1877.30 --> 1883.00]  The other thing about the Epic misunderstanding TJ is not,
[1883.14 --> 1885.52]  so you probably don't have this side of the problem.
[1885.60 --> 1886.24]  So they're like,
[1886.28 --> 1886.36]  oh,
[1886.38 --> 1886.88]  you work at Epic.
[1886.88 --> 1887.34]  And it's like,
[1887.58 --> 1887.84]  it's like,
[1887.88 --> 1888.00]  no,
[1888.00 --> 1888.08]  no,
[1888.08 --> 1888.18]  no,
[1888.18 --> 1888.72]  not that Epic.
[1888.72 --> 1889.84]  The one who makes like unreal.
[1889.84 --> 1890.26]  And they're like,
[1890.32 --> 1890.42]  oh,
[1890.46 --> 1891.12]  that's unreal.
[1891.30 --> 1893.68]  So there's like two words I can say.
[1894.28 --> 1894.64]  Yeah,
[1894.74 --> 1894.98]  exactly.
[1895.28 --> 1895.88]  So it gets,
[1896.10 --> 1896.96]  that gets rough,
[1897.18 --> 1901.58]  but I just had the look of like intense sadness when they found out I didn't make Fortnite.
[1901.90 --> 1905.36]  Like the only thing they thought they were going to be able to connect with me on,
[1905.46 --> 1906.56]  like I'm a software developer.
[1906.56 --> 1907.64]  I work at Epic and they're like,
[1908.14 --> 1908.66]  oh,
[1908.78 --> 1909.20]  cool.
[1909.70 --> 1910.94]  Something interesting.
[1910.94 --> 1911.58]  And I'm like,
[1911.64 --> 1912.08]  no,
[1912.88 --> 1915.18]  electronic medical health records.
[1915.18 --> 1919.22]  And I work in an insurance and billing section.
[1922.22 --> 1922.82]  They're like,
[1922.90 --> 1923.06]  well,
[1923.10 --> 1923.48]  that's,
[1923.90 --> 1924.40]  that,
[1924.52 --> 1926.00]  that's kind of cool too.
[1926.36 --> 1926.98]  It's like,
[1926.98 --> 1930.02]  almost like making the world's biggest video game.
[1930.10 --> 1931.16]  It's almost there.
[1932.76 --> 1934.38]  What language do you write in?
[1934.50 --> 1934.70]  Oh,
[1934.92 --> 1935.34]  mumps.
[1935.82 --> 1937.04]  The conversation's over.
[1937.04 --> 1939.94]  I did a little bit of programming in college.
[1940.04 --> 1940.34]  What is it?
[1940.38 --> 1941.42]  C plus plus C?
[1941.58 --> 1941.74]  Oh,
[1941.80 --> 1942.00]  mumps.
[1942.12 --> 1942.22]  Oh,
[1942.36 --> 1942.52]  okay.
[1942.66 --> 1943.72]  What the hell is mumps?
[1944.26 --> 1946.00]  That's the language that they use at,
[1946.00 --> 1946.78]  at Epic.
[1947.00 --> 1947.14]  Oh,
[1947.20 --> 1947.50]  that's right.
[1947.54 --> 1947.76]  Casey,
[1947.86 --> 1949.10]  you weren't there for when we,
[1949.24 --> 1950.30]  the hell is mumps.
[1950.50 --> 1950.82]  That's a,
[1950.82 --> 1951.60]  that's a disease.
[1952.18 --> 1956.12]  Why is a healthcare company programming in a language that's named after disease?
[1956.22 --> 1957.36]  What the hell is happening?
[1957.88 --> 1958.12]  Casey,
[1958.18 --> 1958.88]  but this is like,
[1959.10 --> 1960.02]  why do people,
[1960.46 --> 1962.38]  why do programmers think of dumb names?
[1962.38 --> 1963.20]  Cause they're stupid.
[1963.30 --> 1963.80]  What is mumps?
[1963.88 --> 1964.20]  Tell me,
[1964.26 --> 1964.36]  no,
[1964.42 --> 1965.48]  I want to know what mumps is though.
[1965.58 --> 1970.90]  It stands for like Massachusetts university multipurpose system or like something like,
[1970.96 --> 1971.60]  it's like some,
[1971.74 --> 1976.04]  they made it at some hospital in like the seventies or something like this.
[1976.04 --> 1977.04]  I don't remember exactly.
[1977.30 --> 1977.58]  All right.
[1977.58 --> 1980.14]  And so they don't call it mumps anymore for exactly,
[1980.28 --> 1981.06]  they call it M,
[1981.32 --> 1982.22]  but it's,
[1982.22 --> 1983.26]  it's not better.
[1983.80 --> 1984.92]  They just call it M.
[1985.04 --> 1985.78]  That's very confusing.
[1986.62 --> 1986.72]  Well,
[1986.76 --> 1986.94]  yes,
[1987.04 --> 1988.98]  I'm just James Bond now.
[1989.10 --> 1989.52]  Like it's like,
[1989.56 --> 1989.72]  Oh,
[1989.76 --> 1990.98]  that's Q and that's M.
[1990.98 --> 1994.24]  They also skipped like D E F G.
[1994.42 --> 1995.46]  Like they sort of see it.
[1995.58 --> 1995.78]  Okay.
[1995.78 --> 1996.22]  Yes.
[1996.26 --> 1996.74]  But guys,
[1996.82 --> 1997.44]  there's trade-offs.
[1997.58 --> 2001.48]  The option is presenting the doctors with this was built with mumps or this was built
[2001.48 --> 2001.92]  with M.
[2002.00 --> 2002.28]  Okay.
[2002.54 --> 2004.54]  They're going to say something fine.
[2004.60 --> 2006.06]  Sometimes they say inner systems cache.
[2006.24 --> 2007.68]  Cause that's one of the people that provided.
[2007.86 --> 2007.98]  All right.
[2007.98 --> 2013.06]  I would just like to point out that basically all of the D language stands out there are
[2013.06 --> 2015.72]  now furious at prime for saying they skipped D.
[2016.08 --> 2016.52]  Wow.
[2017.46 --> 2019.08]  That's going to hurt some people.
[2019.62 --> 2020.48]  One of them.
[2020.48 --> 2020.92]  Wow.
[2020.92 --> 2022.38]  Seven of you in the comments.
[2022.52 --> 2023.62]  Let us know that you've written a line.
[2024.02 --> 2025.20]  Oh my God.
[2026.30 --> 2026.70]  Oh,
[2026.80 --> 2029.62]  we have collection and manual memory management.
[2029.78 --> 2029.88]  Oh,
[2029.92 --> 2031.16]  but you don't have users.
[2031.32 --> 2031.64]  Okay.
[2031.80 --> 2037.08]  So what's the one thing that both C plus plus and rust users can agree on.
[2037.32 --> 2037.92]  D sucks.
[2038.08 --> 2038.22]  Right?
[2038.30 --> 2038.40]  Like,
[2038.40 --> 2042.08]  Oh my God,
[2042.12 --> 2042.48]  you guys.
[2042.54 --> 2042.92]  All right.
[2042.94 --> 2044.22]  I'm not involved in this.
[2044.68 --> 2045.36]  This is nothing.
[2045.48 --> 2046.20]  I don't want to,
[2046.28 --> 2048.34]  I don't want to have a fight with D people.
[2048.34 --> 2049.76]  We're cutting that out.
[2049.86 --> 2051.82]  We're putting the whole thing in here and we're putting in a,
[2051.88 --> 2052.48]  you laughing.
[2052.68 --> 2054.22]  We're just going to splice you out of context.
[2054.46 --> 2055.08]  Oh yes.
[2055.40 --> 2057.04]  I should never have let you guys have edit.
[2057.26 --> 2058.48]  You should never have been able to edit.
[2058.48 --> 2060.16]  Do you actually know anything about D?
[2060.74 --> 2061.00]  Me?
[2061.08 --> 2061.36]  I do.
[2061.44 --> 2061.62]  Yeah.
[2061.62 --> 2061.72]  Yeah.
[2061.72 --> 2061.84]  Yeah.
[2061.96 --> 2064.18]  You can just say what's D a very little bit.
[2064.90 --> 2066.40]  You can just say that if you need to.
[2066.94 --> 2067.06]  What?
[2067.12 --> 2067.30]  Casey,
[2067.42 --> 2068.50]  but explain this then.
[2068.62 --> 2069.58]  If you're such a big fan of D,
[2069.64 --> 2070.98]  then why is it not D moratory?
[2072.42 --> 2072.74]  Yeah.
[2073.36 --> 2074.58]  I'm not a fan of D.
[2074.66 --> 2075.50]  I'm just saying like,
[2075.58 --> 2075.90]  Oh,
[2076.06 --> 2076.62]  we got him.
[2076.90 --> 2078.08]  He's not a fan of D.
[2078.40 --> 2079.02]  Cut it in.
[2079.10 --> 2079.90]  Pice it up boys.
[2080.02 --> 2080.62]  Put it in.
[2083.94 --> 2084.38]  All right.
[2084.40 --> 2084.52]  Well,
[2084.52 --> 2085.80]  thank you D moratory for that.
[2086.00 --> 2086.22]  You know,
[2086.30 --> 2087.32]  I'm not going to lie to you,
[2087.36 --> 2087.60]  Ryan,
[2087.60 --> 2089.92]  you've been suspiciously quiet about Oodle.
[2089.92 --> 2093.14]  Could you please explain why you haven't talked about Oodle once yet?
[2093.26 --> 2093.46]  What?
[2093.64 --> 2094.76]  He doesn't work on Oodle.
[2095.58 --> 2096.02]  Yeah.
[2096.06 --> 2096.28]  I don't,
[2096.36 --> 2097.18]  I don't work on it.
[2098.92 --> 2101.26]  Obviously you'd use the compression in all of your debugging.
[2101.42 --> 2101.90]  So I,
[2101.98 --> 2103.10]  I would assume so at least.
[2104.10 --> 2104.50]  I,
[2104.70 --> 2108.12]  I don't actually like the only thing I use,
[2108.12 --> 2109.76]  like one header file that,
[2109.82 --> 2112.22]  that Jeff gave me for compressing,
[2112.26 --> 2113.74]  but I don't even think it's any of the Oodle stuff.
[2113.74 --> 2114.24]  It's just,
[2114.38 --> 2114.96]  so I'm,
[2114.96 --> 2115.36]  I'm very,
[2115.50 --> 2115.70]  yeah,
[2115.70 --> 2115.84]  I'm,
[2115.84 --> 2117.50]  I'm very Oodle adjacent,
[2117.74 --> 2118.78]  if you will.
[2118.78 --> 2120.82]  Do you want to talk about Oodle prime?
[2120.96 --> 2121.06]  No,
[2121.06 --> 2121.92]  I don't actually.
[2122.50 --> 2122.58]  Okay.
[2124.24 --> 2126.90]  They would come on and probably one of them might,
[2127.10 --> 2128.60]  I don't know if you want to talk about Oodle,
[2128.74 --> 2130.92]  but I just wanted to ask an Oodle question at some point.
[2130.96 --> 2131.32]  Okay.
[2131.38 --> 2133.58]  It was very important to me because it's such a funny name.
[2133.82 --> 2134.10]  Okay.
[2134.10 --> 2135.92]  We'll do an Oodle stream next time.
[2136.10 --> 2137.02]  This time though,
[2137.16 --> 2139.48]  can we talk about debugger information stuff?
[2139.48 --> 2140.58]  Cause I'd like to talk about that.
[2141.00 --> 2141.70]  I actually will.
[2141.82 --> 2143.46]  Can I do a real followup question?
[2143.62 --> 2143.88]  Please.
[2143.88 --> 2146.06]  You said something Ryan inside your talk,
[2146.10 --> 2147.40]  which is how do steps work?
[2147.40 --> 2148.44]  And I thought the same thing.
[2148.44 --> 2148.70]  I'm like,
[2148.72 --> 2149.48]  how do magnets work?
[2149.52 --> 2150.32]  How do steps work?
[2150.54 --> 2153.50]  And so can you explain why that's such a,
[2153.50 --> 2154.66]  like a tremendous problem?
[2155.74 --> 2156.10]  Um,
[2156.50 --> 2157.08]  yeah.
[2157.08 --> 2157.36]  So,
[2157.58 --> 2160.46]  so I don't know what a magnet is exactly.
[2161.04 --> 2161.48]  Uh,
[2161.56 --> 2162.40]  maybe no one,
[2162.40 --> 2163.58]  you don't have to answer that one.
[2163.68 --> 2164.40]  It's not possible.
[2164.76 --> 2165.40]  This is not going to be,
[2165.48 --> 2167.30]  we don't want this to become a Christian stream right now.
[2167.30 --> 2168.58]  So please don't answer that question.
[2168.58 --> 2171.02]  They don't know the reference prime.
[2171.28 --> 2173.34]  They don't know the reference.
[2173.52 --> 2173.78]  No,
[2173.84 --> 2174.78]  he does know the reference.
[2174.92 --> 2176.16]  That's why you said that.
[2177.36 --> 2177.88]  No,
[2177.90 --> 2179.02]  I don't think he does the reference.
[2179.52 --> 2184.24]  Take a look at this fine creation and enjoy it better with appreciation.
[2184.70 --> 2186.60]  I don't think I know this work.
[2186.90 --> 2187.64]  He doesn't know.
[2187.76 --> 2188.16]  That's fine.
[2188.26 --> 2189.10]  Neither does chat.
[2189.38 --> 2189.70]  Move on.
[2189.70 --> 2190.06]  Okay.
[2190.14 --> 2190.54]  Got it.
[2190.70 --> 2191.04]  Got it.
[2191.86 --> 2192.14]  Okay.
[2192.22 --> 2193.10]  I think that,
[2193.76 --> 2195.40]  that was the perfect response.
[2195.40 --> 2196.64]  If you did know though,
[2196.64 --> 2199.68]  that was like so good because we don't know how magnets work.
[2199.82 --> 2200.08]  I mean,
[2200.08 --> 2200.70]  no one does,
[2200.78 --> 2200.96]  right?
[2201.00 --> 2201.86]  That's the whole point.
[2202.30 --> 2202.52]  Yes.
[2202.52 --> 2203.22]  Thank you,
[2203.28 --> 2203.52]  Casey.
[2204.66 --> 2205.22]  I see.
[2205.80 --> 2206.06]  All right.
[2206.12 --> 2206.48]  Okay.
[2206.48 --> 2207.52]  So I can explain how,
[2207.74 --> 2208.48]  let's get back to this.
[2208.56 --> 2209.40]  How do steps work?
[2210.12 --> 2210.52]  Okay.
[2210.54 --> 2211.14]  So stepping,
[2211.40 --> 2212.58]  so line stepping is,
[2213.86 --> 2215.54]  okay.
[2215.54 --> 2216.14]  Um,
[2216.38 --> 2220.06]  I guess the first thing to understand about the problem of stepping is sort of
[2220.06 --> 2220.54]  how,
[2220.54 --> 2225.82]  how a debugger interacts with like another running program in like another native
[2225.82 --> 2227.48]  running program on an operating system.
[2227.48 --> 2232.18]  So basically the debugger has the opportunity to like make changes to memory
[2232.18 --> 2233.40]  and make changes to registers.
[2233.58 --> 2236.46]  And then it can suspend or resume certain threads.
[2236.46 --> 2238.40]  Like you can basically set up certain threads to run or,
[2238.40 --> 2239.34]  or others to not.
[2239.46 --> 2240.42]  And then it just says,
[2240.54 --> 2242.46]  go basically can just say to the operating system.
[2242.54 --> 2242.74]  Okay.
[2242.74 --> 2244.58]  Now you can schedule this program's threads again.
[2244.94 --> 2249.24]  And then like the debugger loses all control at that point until that
[2249.24 --> 2249.86]  program,
[2249.86 --> 2250.46]  um,
[2250.76 --> 2252.32]  does something that would,
[2252.46 --> 2255.54]  that would cause the kernel to transfer control back to the debugger.
[2256.34 --> 2259.90]  And so if you think about what it actually means to like step over a line
[2259.90 --> 2260.62]  of source code,
[2260.82 --> 2263.06]  first you have to,
[2263.20 --> 2264.48]  first you have the problem of like,
[2264.48 --> 2265.20]  um,
[2265.72 --> 2267.24]  locating where the,
[2267.42 --> 2267.74]  uh,
[2267.94 --> 2269.54]  like where a threads instruction pointer,
[2269.64 --> 2271.96]  because you're stepping a thread over some line of source code that it's on.
[2272.02 --> 2272.38]  First,
[2272.44 --> 2275.70]  you have to like extract the register value that stores the instruction
[2275.70 --> 2277.10]  pointer of whatever thread you're stepping.
[2277.52 --> 2280.76]  You have to then understand where that actually map,
[2280.90 --> 2282.86]  like what source code that actually maps to.
[2283.70 --> 2284.62]  Once you know that,
[2284.70 --> 2284.88]  you know,
[2284.88 --> 2288.68]  the range of addresses that are associated with that particular line of source
[2288.68 --> 2290.56]  code that that thread happens to be stopped on.
[2291.46 --> 2293.00]  And then you have to say like,
[2293.68 --> 2294.12]  um,
[2294.40 --> 2294.68]  you know,
[2294.74 --> 2295.20]  let me,
[2295.42 --> 2299.48]  basically I have to produce the effect that this thread will stop execution.
[2299.48 --> 2303.52]  Like the program will stop execution when this thread leaves this line of source
[2303.52 --> 2303.78]  code.
[2304.20 --> 2309.02]  Now a very naive algorithm you could do to do that is what would be to say,
[2309.08 --> 2311.90]  there's something on a CPUs where you can single step a thread,
[2311.90 --> 2313.18]  which at that level,
[2313.18 --> 2315.18]  it's just stepping over one single instruction.
[2315.48 --> 2315.84]  Um,
[2315.84 --> 2317.06]  and then it immediately interrupts.
[2317.08 --> 2320.32]  So you can basically set a bit in one register on the CPU and you can say,
[2320.38 --> 2320.48]  okay,
[2320.48 --> 2322.22]  step over one instruction and then stop.
[2322.22 --> 2325.02]  Can I interject real quick here for the folks at home?
[2325.86 --> 2329.24]  So just to be clear for anyone who hasn't looked at this kind of thing before.
[2329.44 --> 2331.40]  So when you have a line of source code,
[2331.60 --> 2336.74]  a compiler is turning that into potentially many assembly language instructions that
[2336.74 --> 2338.00]  will actually be executed by a CPU.
[2338.14 --> 2339.54]  So there's this mapping.
[2339.54 --> 2343.56]  And not only is it a like one to potentially many mapping,
[2343.70 --> 2346.72]  meaning one line of source code could produce many assembly language instructions,
[2346.72 --> 2349.78]  but also in more sophisticated builds,
[2349.78 --> 2351.54]  like when you're running an optimizer,
[2351.86 --> 2355.80]  those assembly language instructions do not occur in a chunk.
[2355.80 --> 2358.80]  So it's not like going from one to like three instructions in a row.
[2358.90 --> 2363.02]  It could be going from one of your source lines to several instructions peppered
[2363.02 --> 2364.38]  throughout other instructions.
[2364.38 --> 2367.52]  It has been mixed with that come from other lines of source code.
[2367.72 --> 2367.86]  Right?
[2367.86 --> 2370.04]  So the mapping is very messy.
[2370.40 --> 2374.90]  And one of the reasons that debug information is not a super easy problem is because
[2374.90 --> 2378.28]  the whole point of that thing that Ryan was talking about before with PDBs and
[2378.28 --> 2378.54]  dwarf,
[2378.68 --> 2381.08]  like this debug info that gets produced when you build your program.
[2381.48 --> 2386.34]  One of the reasons that's so messy is because that is trying to store in some way
[2386.34 --> 2389.28]  that a debugger can use among many other things.
[2389.44 --> 2393.88]  How do you go from a line of text that the user typed into Vim,
[2394.12 --> 2394.42]  right?
[2395.02 --> 2397.34]  To which assembly language instructions,
[2397.34 --> 2398.54]  the CPU is going to execute,
[2398.78 --> 2400.44]  which ones it caused?
[2400.74 --> 2402.54]  Because when you're going through an optimizer,
[2402.64 --> 2403.92]  it's combining instructions.
[2403.92 --> 2405.30]  It's like removing instructions.
[2405.30 --> 2406.44]  It's reordering instructions.
[2406.90 --> 2409.26]  And so even just that one part is messy.
[2409.38 --> 2411.20]  So everything's Ryan's talking about now when he's saying,
[2411.30 --> 2412.16]  how do you go from one to the other?
[2412.20 --> 2412.34]  Like,
[2412.50 --> 2413.24]  just keep in your head.
[2413.28 --> 2415.16]  That's a very messy mapping between those two.
[2415.36 --> 2416.24]  That's all I wanted to throw in there.
[2416.24 --> 2417.44]  I had to also throw in a,
[2417.44 --> 2419.52]  just a quick like question to answer along the way,
[2419.60 --> 2422.46]  which is when you break point or you hit some sort of stopping condition and
[2422.46 --> 2423.62]  you're in the middle of a line,
[2423.70 --> 2424.88]  does that ever happen as well?
[2424.88 --> 2425.66]  Like where you're just like,
[2425.72 --> 2426.86]  I'm halfway through a line.
[2426.96 --> 2428.00]  What line do you appear on?
[2428.28 --> 2430.92]  Does that screw up debugging information that causes confusion?
[2431.52 --> 2433.50]  I'm very curious about that.
[2434.42 --> 2434.52]  Yeah.
[2434.62 --> 2436.30]  So that definitely does happen.
[2436.48 --> 2437.42]  And it can even happen.
[2437.56 --> 2437.62]  Like,
[2437.70 --> 2438.16]  for example,
[2438.16 --> 2440.08]  if you step out of a function call,
[2440.20 --> 2441.10]  like you're inside of a function,
[2441.16 --> 2443.72]  you want to return to whoever called you generally,
[2443.86 --> 2444.58]  like you might,
[2444.74 --> 2447.74]  there might still be some instructions to execute after you've actually popped
[2447.74 --> 2448.24]  from the call.
[2448.34 --> 2450.24]  So if you do a step out operation,
[2450.24 --> 2452.06]  you'll end up in the middle of the line.
[2452.10 --> 2455.24]  You're not just at the first address of the lines source machine code.
[2455.32 --> 2457.24]  You might be at some instruction in the middle.
[2457.24 --> 2458.00]  Um,
[2458.40 --> 2461.90]  and so basically that's just an extra wrinkle in the problem.
[2462.00 --> 2462.40]  You don't,
[2462.48 --> 2462.66]  um,
[2462.66 --> 2463.78]  it doesn't really screw anything up,
[2463.80 --> 2465.32]  but you just basically have to say like,
[2465.66 --> 2466.86]  this is a range of instructions.
[2466.86 --> 2469.00]  And if the thread ends up anywhere in here,
[2469.00 --> 2471.74]  I have to associate that with this particular line of source code.
[2471.80 --> 2473.12]  So it's one detail in the mapping,
[2473.12 --> 2473.80]  but it's not,
[2473.90 --> 2474.54]  um,
[2474.66 --> 2477.10]  it's not like a showstopper by any means.
[2477.60 --> 2477.96]  Um,
[2478.20 --> 2479.38]  so,
[2479.98 --> 2480.48]  um,
[2480.88 --> 2481.50]  so yeah,
[2481.50 --> 2483.32]  if you wanted to step over a line of source code,
[2483.32 --> 2487.16]  if you wanted to like basically proceed this thread until it has exited,
[2487.24 --> 2488.50]  this particular line of source code,
[2489.04 --> 2489.28]  you,
[2489.68 --> 2489.92]  um,
[2490.18 --> 2495.44]  one simple thing would be to single step that thread until you see it has left the line.
[2495.44 --> 2498.30]  Like you just keep mapping the instruction pointer every time it comes back.
[2498.74 --> 2500.32]  And then if it leaves the,
[2500.44 --> 2500.54]  if,
[2500.62 --> 2503.10]  if it's changed the source code line that it's on,
[2503.20 --> 2503.80]  then,
[2504.00 --> 2504.90]  then the step is done.
[2504.96 --> 2505.26]  So that's,
[2505.32 --> 2506.40]  that's a very simple algorithm.
[2506.96 --> 2507.40]  Um,
[2507.44 --> 2513.54]  it also is enormously slow because remember that each one of these interrupt instructions that comes back,
[2513.54 --> 2514.10]  uh,
[2514.10 --> 2514.48]  or sorry,
[2514.90 --> 2515.12]  each,
[2515.32 --> 2515.56]  um,
[2515.70 --> 2518.34]  each one of the single step fit,
[2518.40 --> 2518.64]  uh,
[2518.66 --> 2519.54]  after a single step has,
[2519.62 --> 2520.26]  has completed,
[2520.26 --> 2524.22]  basically what's going to happen is the kernel is going to schedule that thread and it's going to say,
[2524.28 --> 2524.42]  okay,
[2524.50 --> 2525.52]  execute one instruction.
[2525.64 --> 2527.40]  It's going to immediately trigger an interrupt.
[2527.52 --> 2528.86]  The kernel will then,
[2528.86 --> 2529.34]  um,
[2530.12 --> 2531.52]  it'll switch to the kernel and the kernel will say,
[2531.58 --> 2531.72]  okay,
[2531.72 --> 2532.80]  now this is,
[2532.92 --> 2535.76]  I need to report this debug event to the debugger.
[2535.76 --> 2536.72]  So it has to transition,
[2536.72 --> 2537.22]  uh,
[2537.22 --> 2540.06]  it has to context switch over to the actual debugger itself.
[2540.06 --> 2542.34]  And so every single time you do a single step,
[2542.44 --> 2543.84]  it's one of these round trips.
[2543.84 --> 2545.84]  You can think of it as between the debug,
[2546.04 --> 2550.26]  the debuggy or the target process and the debugger itself.
[2550.26 --> 2554.72]  And so if you've got a line that has a hundred or a thousand instruction,
[2554.86 --> 2555.08]  I mean,
[2555.28 --> 2555.60]  you know,
[2555.64 --> 2556.72]  you can make it arbitrarily,
[2557.00 --> 2557.78]  arbitrarily long,
[2557.82 --> 2558.06]  really.
[2558.58 --> 2558.98]  Um,
[2559.64 --> 2559.96]  you know,
[2560.02 --> 2560.30]  you're,
[2560.46 --> 2563.26]  you're causing a round trip every single time someone,
[2563.26 --> 2563.98]  uh,
[2564.30 --> 2564.90]  every,
[2565.02 --> 2566.44]  every single instruction within that line.
[2566.48 --> 2567.36]  So that gets very slow.
[2567.36 --> 2569.84]  So instead what you kind of want to do is say like,
[2570.06 --> 2571.48]  I'm going to set up a bunch of,
[2571.54 --> 2572.18]  there's another thing,
[2572.24 --> 2573.46]  another concept that I should introduce,
[2573.50 --> 2575.30]  which is the int three instruction on X,
[2575.38 --> 2576.02]  on X64,
[2576.22 --> 2577.92]  but there's equivalents elsewhere,
[2577.92 --> 2579.50]  um,
[2579.62 --> 2581.38]  where you can basically put a,
[2582.12 --> 2585.30]  it's a one byte instruction that you can use to overwrite any instruction,
[2585.42 --> 2585.74]  basically,
[2585.80 --> 2586.64]  because it's just one byte.
[2586.64 --> 2587.04]  So it's,
[2587.12 --> 2588.40]  it's the minimum instruction size.
[2588.52 --> 2589.60]  And you can go ahead and say,
[2589.68 --> 2590.82]  I'm going to put this here.
[2590.82 --> 2592.32]  And then when the thread executes,
[2592.32 --> 2594.18]  this instruction is called an int three.
[2594.72 --> 2595.46]  And when it,
[2596.24 --> 2596.68]  uh,
[2596.68 --> 2596.86]  I don't,
[2596.98 --> 2598.46]  there's other kinds of interrupt codes,
[2598.46 --> 2602.56]  but in three specifically is this one byte instruction that you can put anywhere in the code stream.
[2602.62 --> 2605.06]  And when a thread executes that it'll immediately interrupt.
[2605.06 --> 2605.54]  So it does,
[2605.64 --> 2608.04]  it has the same effect sort of as the single step,
[2608.08 --> 2610.18]  except it's caused by an instruction you put in the code.
[2610.38 --> 2611.26]  And so then you,
[2611.48 --> 2614.20]  so in order to avoid all of these round trips,
[2614.20 --> 2617.62]  what you can start doing is saying when the thread is in this line,
[2617.62 --> 2618.12]  and I say,
[2618.22 --> 2619.36]  step over this line of code,
[2619.36 --> 2620.84]  I'm going to basically set up,
[2620.84 --> 2621.16]  um,
[2622.04 --> 2622.46]  an int three.
[2622.46 --> 2623.18]  It's called an int three.
[2623.26 --> 2625.02]  It's also called a trap is what people call it.
[2625.02 --> 2630.80]  So what you can basically do is start putting these traps anywhere you think the thread might go within this line.
[2630.92 --> 2631.14]  Now,
[2631.20 --> 2632.40]  if it's pure linear code,
[2632.40 --> 2635.76]  like it's going to do a bunch of mobs and then an ad and then,
[2635.88 --> 2636.08]  you know,
[2636.12 --> 2636.38]  whatever,
[2636.74 --> 2637.96]  very simple linear code.
[2638.14 --> 2639.70]  There's only one trap you actually have to place,
[2639.76 --> 2641.10]  which is at the beginning of the next line.
[2641.62 --> 2643.78]  But it starts to get more complicated.
[2643.88 --> 2644.52]  If you,
[2644.64 --> 2645.10]  for example,
[2645.44 --> 2646.64]  um,
[2646.76 --> 2648.86]  if inside of that line of source code,
[2648.86 --> 2651.46]  you've got a jump instruction or a call,
[2651.46 --> 2653.80]  then you have to start thinking about like where,
[2653.96 --> 2656.62]  where are all the places this thread might actually go to.
[2657.04 --> 2658.98]  And so then you might have to start doing things like,
[2659.02 --> 2659.14]  okay,
[2659.14 --> 2660.16]  let's disassemble the line.
[2660.24 --> 2663.64]  Let's figure out like where the control flow will lead to in this line.
[2663.64 --> 2665.96]  And let's go place traps in all of those places.
[2666.50 --> 2667.36]  And then it gets,
[2667.74 --> 2669.22]  it gets a little bit more complicated too,
[2669.28 --> 2669.58]  because,
[2669.78 --> 2670.04]  um,
[2670.22 --> 2670.78]  for example,
[2670.78 --> 2672.50]  if you're in a recursive function call,
[2673.14 --> 2673.38]  like,
[2673.48 --> 2673.68]  uh,
[2673.68 --> 2676.46]  so two variants of stepping exist for people who haven't used debuggers.
[2676.58 --> 2678.12]  There's step over and step into.
[2678.68 --> 2681.04]  There's a lot of other steps you might imagine doing,
[2681.04 --> 2683.84]  but those are the two like common ones and step out.
[2684.40 --> 2685.14]  Step over will,
[2685.40 --> 2685.66]  um,
[2686.04 --> 2686.58]  well basically,
[2686.86 --> 2687.24]  uh,
[2687.28 --> 2688.72]  it won't follow call instructions.
[2688.82 --> 2689.72]  So if you do a step into,
[2689.94 --> 2693.88]  you're sort of stopped at a function call and you want to go into the function call and see what,
[2694.10 --> 2695.72]  what's actually happening inside of the function call.
[2696.40 --> 2697.28]  With a step over,
[2697.38 --> 2699.20]  you don't care about what's going on inside the function.
[2699.20 --> 2703.56]  So you just want to step to the next line and have whatever happens inside the function happen.
[2704.38 --> 2704.78]  Um,
[2704.96 --> 2706.20]  now,
[2706.26 --> 2708.14]  if you wanted to do a step over,
[2709.14 --> 2710.24]  you could imagine,
[2710.40 --> 2710.82]  um,
[2711.44 --> 2714.00]  if you are in a function that is recursive,
[2714.00 --> 2715.24]  and remember,
[2715.40 --> 2718.48]  a debugger has to deal with any code that someone could write and feed into it.
[2718.52 --> 2719.02]  Like it doesn't,
[2719.10 --> 2720.90]  it has to kind of handle all these cases gracefully.
[2720.98 --> 2722.46]  There's lots of recursive code that exists.
[2723.12 --> 2723.36]  Um,
[2723.52 --> 2728.26]  so if you're stopped at one particular line and it's a recursive call into the same function,
[2728.26 --> 2733.96]  it gets more tricky because if you just place a trap at the next line and then you try to step over,
[2734.16 --> 2734.60]  you're,
[2734.68 --> 2737.02]  you're going to hit that same trap address,
[2737.22 --> 2739.58]  but in one layer deeper in the call stack.
[2739.58 --> 2741.98]  So you basically have descended to the next call,
[2742.26 --> 2743.06]  hit the same trap,
[2743.18 --> 2746.24]  but it wasn't actually a step over because the step over,
[2746.46 --> 2748.46]  it didn't step over the line.
[2748.56 --> 2751.14]  It didn't step over all of the calls work that happened.
[2751.30 --> 2752.94]  Now you're one layer deeper in the call stack.
[2752.94 --> 2756.06]  So there's no way anymore to actually step over that line of code.
[2756.06 --> 2757.38]  So you have to get tricky about like,
[2757.90 --> 2758.12]  okay,
[2758.20 --> 2758.58]  have I,
[2759.08 --> 2759.28]  uh,
[2759.28 --> 2761.08]  has my stack pointer changed?
[2761.32 --> 2763.90]  When do I update which value of the,
[2764.00 --> 2766.10]  of the stack pointer that I want to check against?
[2766.10 --> 2770.32]  It becomes kind of basically like a little program you have to send down and say,
[2770.32 --> 2770.60]  like,
[2770.80 --> 2771.78]  if it hits this trap,
[2771.88 --> 2772.30]  do this.
[2772.34 --> 2773.36]  And if it hits this trap,
[2773.36 --> 2773.66]  trap,
[2773.76 --> 2774.12]  do this.
[2774.14 --> 2776.22]  And if it hits this trap and single step here,
[2776.24 --> 2776.50]  and like,
[2776.62 --> 2779.38]  it becomes a very complicated sort of state machine that you actually have to implement.
[2780.08 --> 2780.16]  I,
[2780.30 --> 2780.44]  okay.
[2780.48 --> 2781.00]  So hold on.
[2781.10 --> 2781.46]  I can,
[2781.46 --> 2782.06]  can I get one more?
[2782.14 --> 2782.46]  Oh no.
[2782.52 --> 2783.12]  TJ wants it.
[2783.12 --> 2784.08]  I just got a,
[2784.08 --> 2784.76]  just a quick question.
[2784.86 --> 2786.70]  I was just wondering like on average,
[2786.86 --> 2789.42]  what your step count is every day.
[2789.54 --> 2790.18]  You know what I'm saying?
[2790.36 --> 2790.72]  Like,
[2790.84 --> 2792.36]  cause for me personally,
[2792.36 --> 2792.72]  like,
[2792.78 --> 2794.80]  I don't know if this makes me a debugger,
[2794.90 --> 2796.10]  like a step debugger or not,
[2796.10 --> 2796.48]  but like,
[2796.48 --> 2799.58]  I've got my own like walking treadmill now at my desk.
[2799.84 --> 2800.02]  Yeah.
[2800.02 --> 2802.16]  I didn't know if this is kind of like what,
[2802.28 --> 2804.84]  like what scenario this kind of goes on.
[2804.90 --> 2806.64]  So I just didn't know how this related to debugger.
[2806.70 --> 2808.94]  Does this make me a step driven debugger?
[2809.14 --> 2809.82]  Like if I'm reading,
[2810.02 --> 2810.86]  you're stepping into,
[2810.94 --> 2811.82]  you're not stepping over.
[2812.14 --> 2813.06]  So we're talking about stepping,
[2813.12 --> 2813.70]  over right now.
[2813.76 --> 2814.12]  Okay.
[2814.16 --> 2814.90]  I'm trying now.
[2814.96 --> 2815.34]  There you go.
[2815.50 --> 2816.62]  Like I'm trying to step out.
[2816.62 --> 2817.74]  That's the harder one to do.
[2817.80 --> 2818.00]  Which,
[2818.06 --> 2818.94]  which one is hard to,
[2819.00 --> 2820.94]  how do I do recursive treadmills?
[2821.24 --> 2823.34]  You're on an inch three and it's inside the stack.
[2823.34 --> 2824.70]  You put that treadmill on a treadmill.
[2825.88 --> 2826.24]  Oh,
[2826.30 --> 2827.40]  that makes so much more sense.
[2827.48 --> 2828.46]  And then it's running too.
[2828.64 --> 2828.92]  Yes,
[2828.94 --> 2829.34]  exactly.
[2829.46 --> 2829.64]  Right.
[2830.26 --> 2830.78]  I got it.
[2830.80 --> 2830.96]  Okay.
[2831.16 --> 2831.36]  Okay.
[2831.52 --> 2831.88]  Anyways,
[2831.88 --> 2832.68]  you can continue now.
[2832.74 --> 2832.92]  Thanks.
[2833.08 --> 2833.12]  Okay.
[2833.34 --> 2833.70]  TJ,
[2833.88 --> 2834.36]  how I,
[2834.50 --> 2834.60]  okay.
[2834.60 --> 2835.62]  Now we have a sub question.
[2835.72 --> 2836.02]  Now we're,
[2836.02 --> 2836.34]  we,
[2836.44 --> 2837.38]  our stack has been pushed.
[2837.50 --> 2837.70]  TJ,
[2837.84 --> 2839.20]  how long have you been waiting for that?
[2839.30 --> 2839.98]  And also you have a,
[2843.12 --> 2847.18]  immediately after we started talking about step stuff,
[2847.22 --> 2848.24]  I put my,
[2848.30 --> 2848.78]  I put my,
[2849.14 --> 2851.70]  I put it into standing mode and I was getting ready.
[2851.78 --> 2852.86]  I had to set up that scene.
[2852.86 --> 2855.06]  I did not have the video thing ready.
[2855.24 --> 2855.64]  Wow.
[2856.38 --> 2859.48]  So I probably heard about 5% of what Ryan said,
[2859.56 --> 2861.90]  but I was so excited for this joke.
[2862.28 --> 2862.78]  Wow.
[2863.32 --> 2863.80]  Okay.
[2863.86 --> 2866.18]  I was so excited for this one.
[2866.50 --> 2866.92]  That is,
[2866.92 --> 2869.78]  that is some serious professional level podcasting.
[2869.86 --> 2870.24]  All right.
[2870.40 --> 2870.90]  All right.
[2871.18 --> 2871.86]  So when,
[2871.86 --> 2873.96]  when it comes to stepping and putting in all these in threes,
[2874.02 --> 2875.32]  do you also have like,
[2875.62 --> 2878.22]  cause I don't precisely understand how jump instructions work.
[2878.26 --> 2880.32]  I believe there are relative and absolute ones.
[2880.40 --> 2886.76]  Does that mean you also have to update all the relative instructions around all these places that you put these in threes?
[2886.76 --> 2890.94]  Cause theoretically you shifted down some amount of like assembly.
[2891.46 --> 2892.62]  So you're not inserting.
[2893.44 --> 2893.88]  Okay.
[2893.88 --> 2896.56]  I thought you were dynamically at like runtime being like,
[2896.62 --> 2896.92]  okay,
[2897.28 --> 2898.56]  like they're stepping next.
[2898.66 --> 2900.08]  Let's actually insert some,
[2900.24 --> 2900.74]  some stuff.
[2900.74 --> 2901.06]  You're over,
[2901.06 --> 2902.26]  you're overwriting it.
[2902.40 --> 2902.60]  You're,
[2902.84 --> 2903.50]  you're over.
[2903.60 --> 2908.14]  That's why it's crucial that in three has a one bite version because you're,
[2908.26 --> 2910.40]  you're romping it over the instruction.
[2910.62 --> 2914.74]  One of the things Ryan didn't mention because he had to mention like 8,000 things.
[2914.74 --> 2916.38]  Cause this is incredibly complicated.
[2916.38 --> 2919.22]  Is that actually when you write,
[2919.30 --> 2921.00]  when you put that in three in there,
[2921.06 --> 2925.06]  you have to remember which bite you overwrote because once you are done stepping,
[2925.10 --> 2928.34]  you have to go replace all of those with the bites you overwrote.
[2928.34 --> 2930.74]  So that happened as part of this process.
[2931.62 --> 2932.60]  Oh my gosh.
[2932.68 --> 2932.88]  Okay.
[2932.88 --> 2937.38]  So does that mean when you literally overwrite assembly and then when it hits that int,
[2937.66 --> 2941.00]  you then have to put back in the correct assembly so that it,
[2941.10 --> 2942.20]  when it executes the line,
[2942.24 --> 2943.42]  it correctly executes line.
[2943.68 --> 2943.90]  Correct.
[2944.54 --> 2945.04]  That's a,
[2945.22 --> 2945.74]  that's,
[2945.74 --> 2946.06]  that's,
[2946.06 --> 2947.38]  that's crazy dog.
[2947.58 --> 2948.12]  That's great.
[2948.12 --> 2948.54]  I don't know.
[2948.66 --> 2950.64]  It sounds like probably debuggers.
[2950.64 --> 2953.30]  It's as easy as making a regular crud app guys.
[2953.30 --> 2953.42]  Dude,
[2953.52 --> 2954.88]  have you seen a banking app though,
[2954.90 --> 2955.16]  Ryan?
[2955.34 --> 2957.16]  Do you have any idea about a banking app?
[2957.42 --> 2957.72]  Yeah.
[2958.06 --> 2958.42]  Uh,
[2959.06 --> 2959.32]  yeah,
[2959.32 --> 2960.22]  I can't even imagine.
[2961.66 --> 2962.34]  It's just,
[2962.64 --> 2965.80]  that's like magnet level stuff right there.
[2966.04 --> 2966.24]  Yeah.
[2966.96 --> 2968.08]  How do banks work?
[2968.18 --> 2968.52]  Actually,
[2968.60 --> 2969.34]  we don't know.
[2969.86 --> 2970.30]  Actually,
[2970.30 --> 2971.94]  if you would have been paying attention to Twitter,
[2972.28 --> 2974.92]  Lori wire just tweeted how AHC works,
[2975.02 --> 2976.52]  which is literally a FTP.
[2977.20 --> 2977.60]  So yes.
[2977.90 --> 2978.42]  All right.
[2978.48 --> 2980.16]  We do now know how banks work.
[2980.64 --> 2981.00]  Yes,
[2981.02 --> 2981.30]  we do.
[2981.48 --> 2982.60]  That's why it anyways.
[2982.86 --> 2984.62]  So under underlying all of this,
[2984.66 --> 2984.90]  right.
[2984.90 --> 2986.22]  Is like the,
[2986.34 --> 2986.66]  this is,
[2986.80 --> 2989.00]  this is also why you may have noticed.
[2989.00 --> 2992.34]  There was a little snippet of Ryan at the better software conference,
[2992.34 --> 2994.22]  doing a little thing with Wukash,
[2994.22 --> 2994.66]  uh,
[2994.66 --> 2996.28]  where he asked him like,
[2996.38 --> 3000.34]  what was the one OS feature that you would like to have that you don't have
[3000.34 --> 3000.84]  right now?
[3000.84 --> 3002.20]  And Ryan said,
[3002.30 --> 3005.72]  I would like to have user level in three.
[3005.84 --> 3006.50]  And it's like,
[3006.50 --> 3006.78]  what,
[3007.24 --> 3007.98]  what is that?
[3007.98 --> 3008.28]  Right.
[3008.72 --> 3009.10]  Um,
[3009.10 --> 3011.32]  and that underlies this entire thing.
[3011.40 --> 3013.24]  So what happens is in the CPU,
[3013.38 --> 3013.60]  right?
[3014.10 --> 3016.02]  There's this thing called the interrupt table,
[3016.02 --> 3018.38]  or there are things called interrupt tables and CPUs.
[3018.38 --> 3018.60]  Right.
[3019.04 --> 3022.44]  And the reason for this is right at the beginning,
[3022.44 --> 3022.82]  this is,
[3022.90 --> 3024.14]  this is in like 8086,
[3024.40 --> 3026.42]  like the original 8086 chip has this.
[3026.46 --> 3027.66]  This is not like a new thing.
[3028.16 --> 3030.32]  They've been upgraded over time to have different capabilities,
[3030.32 --> 3031.46]  but generally speaking,
[3031.46 --> 3033.16]  this exists for a very long time.
[3033.98 --> 3034.38]  Um,
[3034.74 --> 3039.90]  so they have these tables because what you often want to do is you wanted to have
[3039.90 --> 3043.28]  some kind of like higher level supervisor,
[3043.42 --> 3043.78]  higher levels,
[3043.86 --> 3044.18]  wrong term,
[3044.24 --> 3044.46]  uh,
[3044.46 --> 3045.38]  supervisory,
[3045.38 --> 3045.92]  uh,
[3045.92 --> 3046.64]  system level.
[3046.70 --> 3047.94]  I should always say lower level code,
[3048.02 --> 3048.76]  operating system code,
[3048.82 --> 3049.10]  whatever.
[3049.10 --> 3055.06]  You want to have some code that you can trigger from anywhere instantaneously.
[3055.06 --> 3060.48]  Meaning you don't have to like know in advance that you were going to use this code at this time.
[3060.48 --> 3060.84]  Right.
[3060.84 --> 3064.88]  A call is when you know you were going to use it at this point in the code.
[3064.98 --> 3065.92]  I call this function,
[3066.02 --> 3066.22]  right?
[3066.70 --> 3067.36]  This is like,
[3067.38 --> 3069.06]  we have no idea what we're going to do.
[3069.32 --> 3070.52]  We just suddenly have to do it.
[3070.56 --> 3074.64]  And one of the big reasons for this originally is like servicing hardware.
[3074.92 --> 3079.04]  The CPU has to read something from some bus on some hardware,
[3079.26 --> 3079.50]  you know,
[3079.50 --> 3083.18]  like the original keyboard input or whoever knows what's happening.
[3083.18 --> 3083.46]  Right.
[3084.10 --> 3086.40]  And so what would happen is an interrupt,
[3086.88 --> 3088.80]  literally the reason it's called the interrupt in three,
[3088.96 --> 3089.44]  interrupt three,
[3089.44 --> 3092.46]  an interrupt would happen that stops the normal execution.
[3092.46 --> 3093.58]  What the CPU was doing.
[3094.06 --> 3097.16]  It looks in a table for what it should start doing.
[3097.24 --> 3098.86]  It goes and does that.
[3098.98 --> 3101.58]  And then it resumes back to wherever it was in the program.
[3101.66 --> 3103.18]  It's literally what it sounds like.
[3103.18 --> 3103.94]  It's an interrupt.
[3104.12 --> 3105.78]  And this was used for doing things.
[3105.78 --> 3106.12]  Like I said,
[3106.14 --> 3107.82]  like reading hardware and stuff like that,
[3107.82 --> 3112.34]  because bytes would like come into the CPU that it had to like look at right now.
[3112.44 --> 3114.32]  So it would stop the program.
[3114.52 --> 3114.66]  You know,
[3114.74 --> 3117.08]  this is back when you didn't have multiple cores or anything like that.
[3117.14 --> 3117.28]  Right.
[3117.36 --> 3119.06]  Stop the program as it's executing,
[3119.06 --> 3120.86]  right in the middle of whatever it's doing.
[3121.08 --> 3122.66]  Go service this interrupt.
[3122.74 --> 3123.88]  It's called servicing the interrupt.
[3123.96 --> 3124.08]  Right.
[3124.14 --> 3125.74]  Go jump to that code.
[3126.06 --> 3126.38]  Do it.
[3126.42 --> 3126.60]  Right.
[3126.92 --> 3128.86]  So what an interrupt really is,
[3129.18 --> 3130.58]  is it's basically the,
[3130.78 --> 3132.80]  it's the same kind of thing as a function call,
[3132.92 --> 3136.04]  but it's one where you didn't know what was going to happen.
[3136.04 --> 3138.80]  It's a function call that happens out of nowhere.
[3138.80 --> 3146.06]  And the reason that this is very useful for something like debugging is because one of the things that a function call will do,
[3146.06 --> 3146.62]  right,
[3146.76 --> 3151.18]  is it's going to save what the instruction pointer was before it does the call.
[3151.36 --> 3154.22]  So it will put the instruction pointer onto the stack,
[3154.48 --> 3154.60]  right?
[3154.60 --> 3155.82]  This is a call instruction.
[3155.82 --> 3158.12]  We'll put the instruction pointer onto your program stack.
[3158.28 --> 3162.40]  It then transfers control over to whatever the location is you're going.
[3162.46 --> 3165.56]  So it changes the IP to point to whatever the function is that you wanted to call,
[3165.92 --> 3166.54]  does that.
[3166.54 --> 3168.20]  And then when it goes to do a return,
[3168.78 --> 3170.42]  it will pop off the stack,
[3170.52 --> 3172.20]  whatever that instruction pointer was.
[3172.28 --> 3174.60]  So it's basically a thing that uses your program stack,
[3174.70 --> 3178.68]  your standard program stack to track where you are in the program.
[3178.80 --> 3180.22]  That's a normal function call.
[3180.98 --> 3183.58]  And int can't do that because the,
[3183.70 --> 3186.32]  it doesn't even know if there is a stack.
[3186.40 --> 3188.90]  It's happening in the middle of any code.
[3189.04 --> 3190.52]  There may not even be a stack frame.
[3190.66 --> 3194.88]  You may not even be using the stack pointer as a stack frame at that time,
[3194.88 --> 3196.10]  technically in 8086.
[3196.54 --> 3200.88]  So what it has to do is do some special work to preserve,
[3201.30 --> 3201.56]  right?
[3201.60 --> 3204.16]  Like the IP in this way that will like,
[3204.24 --> 3206.80]  we know we can preserve just what the instruction pointer is.
[3207.16 --> 3209.54]  Then we're going to go into whatever.
[3209.68 --> 3213.02]  We're going to look in this special table that the CPU literally has a hard
[3213.02 --> 3214.78]  coded register that sells it where it is.
[3214.88 --> 3216.52]  So it's separately stored,
[3216.52 --> 3216.88]  right?
[3217.16 --> 3218.16]  We're going to go there,
[3218.42 --> 3219.64]  look up where we should go.
[3219.64 --> 3220.42]  And by the way,
[3220.48 --> 3222.12]  nowadays we also look up a bunch of information,
[3222.32 --> 3225.56]  like whether we should be transferring control to like a different level.
[3225.56 --> 3225.80]  Like,
[3225.88 --> 3229.58]  should we be dropping down to a ring zero from ring three and all this other
[3229.58 --> 3229.82]  stuff?
[3229.90 --> 3233.02]  There's all a bunch of crap in that table and off you go.
[3233.46 --> 3235.62]  So the way debuggers are written currently,
[3235.86 --> 3239.36]  because they have to be is on something like windows.
[3239.36 --> 3242.38]  They are written as a user level application,
[3242.38 --> 3244.90]  which is fine because that's roughly what you want.
[3244.94 --> 3247.66]  You don't want your debugger to crash to take down your whole system,
[3247.74 --> 3247.84]  right?
[3247.84 --> 3249.76]  You don't want crowd strike happening here,
[3249.82 --> 3250.00]  right?
[3250.32 --> 3255.04]  So you want the debugger to be running at ring three on windows so that it's
[3255.04 --> 3256.84]  running up like a normal program.
[3256.84 --> 3257.92]  And if it screws up,
[3257.98 --> 3260.30]  like if Ryan on like the one buggy has,
[3260.42 --> 3260.76]  right?
[3261.10 --> 3261.92]  If that bug,
[3262.02 --> 3264.16]  if you hit that bug and it crashes your system,
[3264.16 --> 3265.26]  you just want the debugger to crash.
[3265.26 --> 3266.78]  You don't want your whole system to blue screen.
[3267.10 --> 3268.54]  So it's good that it's doing this,
[3269.20 --> 3272.94]  but the problem there is it needs to do all the things that Ryan just says.
[3273.04 --> 3274.50]  It needs access to the memory.
[3274.60 --> 3276.46]  It needs to be able to put in like these things,
[3276.52 --> 3277.92]  like in threes that will happen.
[3278.40 --> 3281.36]  And the problem is when you are at user level,
[3281.60 --> 3281.88]  right?
[3282.18 --> 3286.34]  The kernel doesn't want you doing stuff like messing with the interrupt table
[3286.34 --> 3287.10]  or,
[3287.22 --> 3287.58]  you know,
[3287.78 --> 3291.40]  saying that you're going to be the person who gets whenever an int three
[3291.40 --> 3292.14]  happens in this,
[3292.24 --> 3294.92]  on this core that you're the one who's going to get it or whatever.
[3295.04 --> 3295.22]  Right?
[3295.56 --> 3298.44]  It didn't want any of those things for security and stability reasons.
[3298.68 --> 3299.76]  So as a result,
[3299.98 --> 3304.00]  the debuggers have to do all of the work that Ryan described through an API
[3304.00 --> 3306.06]  that the kernel will then use.
[3306.18 --> 3306.22]  It,
[3306.26 --> 3306.34]  you know,
[3306.34 --> 3307.52]  it takes your API calls and goes,
[3307.62 --> 3307.80]  Oh,
[3307.82 --> 3308.24]  I see.
[3308.40 --> 3312.26]  You wanted me to tell you when this guy hits an int three.
[3312.64 --> 3313.76]  So you go,
[3313.88 --> 3313.98]  you,
[3314.10 --> 3314.30]  you know,
[3314.32 --> 3317.08]  I'll let you access his memory through my memory mapping APIs.
[3317.18 --> 3317.44]  You go,
[3317.52 --> 3318.22]  you poke it in there.
[3318.22 --> 3319.58]  You poke your int threes wherever you want.
[3319.64 --> 3319.86]  Great.
[3319.86 --> 3321.42]  When the int three gets hit,
[3321.76 --> 3323.92]  the kernel's the one who's going to get called,
[3324.38 --> 3325.28]  not the debugger.
[3325.42 --> 3328.76]  And then it's going to go through the API to let the debugger know that it
[3328.76 --> 3329.10]  happened.
[3329.64 --> 3333.08]  What this means is that now all of these things Ryan's talking about,
[3333.18 --> 3336.78]  every one of these traps that gets hit is a full round trip.
[3337.26 --> 3338.82]  Debuggy is running at ring three.
[3339.08 --> 3340.28]  The trap gets hit.
[3340.36 --> 3341.22]  The int three gets hit.
[3341.42 --> 3343.10]  It's got a drop to ring zero,
[3343.38 --> 3344.24]  wakes up the kernel.
[3344.38 --> 3344.98]  The kernel goes,
[3345.16 --> 3345.32]  wait,
[3345.40 --> 3346.08]  what is happening?
[3346.22 --> 3346.44]  Oh,
[3346.54 --> 3346.74]  right.
[3346.74 --> 3348.20]  This is a debug executable.
[3348.20 --> 3350.18]  I know I should tell the debugger about it.
[3350.26 --> 3350.54]  Okay.
[3350.74 --> 3354.96]  Let me re switch the task over to the debuggers context.
[3355.18 --> 3359.40]  Let me wake up the debugger in ring three and resume execution of a debugger
[3359.40 --> 3360.30]  thread to handle this.
[3360.38 --> 3361.24]  The debugger then goes,
[3361.38 --> 3362.04]  what just happened?
[3362.16 --> 3362.26]  Oh,
[3362.32 --> 3363.70]  the kernel told me I had a trap.
[3364.10 --> 3364.44]  All right.
[3364.48 --> 3366.10]  Let me go fix up the trap things.
[3366.40 --> 3368.28]  Let me set any new traps that I need.
[3368.28 --> 3373.80]  And then let me retell the kernel back at ring zero to resume the debuggy back.
[3373.90 --> 3374.80]  We go to ring zero.
[3374.94 --> 3379.96]  It then switches in the context of the debuggy back up to ring three and we resume where we
[3379.96 --> 3380.38]  were going.
[3380.38 --> 3380.66]  Right.
[3381.00 --> 3384.82]  This is wicked fricking slow for so many reasons.
[3384.82 --> 3385.14]  Right.
[3385.14 --> 3387.28]  And so what Ryan was talking about is,
[3387.38 --> 3387.76]  Hey man,
[3388.46 --> 3393.00]  what if we could just set the int three to just jump to something in the actual,
[3393.16 --> 3395.24]  the person who's being debugged that program,
[3395.50 --> 3397.12]  the debugger could like,
[3397.52 --> 3402.72]  JIT compile some code that just does the trap operation that it wants to do and resets whatever
[3402.72 --> 3403.96]  it needs or anything else,
[3404.06 --> 3404.24]  right?
[3404.30 --> 3405.00]  Checks conditions,
[3405.14 --> 3405.92]  anything it wants to.
[3406.38 --> 3409.36]  We just set the int three to not do any of that.
[3409.56 --> 3410.44]  Don't tell the kernel,
[3410.70 --> 3411.78]  don't take your in transition.
[3411.78 --> 3414.00]  Just jump right to that thing,
[3414.34 --> 3415.96]  do the stuff and then resume.
[3416.10 --> 3419.02]  It would be so much faster getting rid of that.
[3419.06 --> 3420.34]  Like first ring transition,
[3420.52 --> 3421.56]  back up ring transition,
[3421.68 --> 3422.66]  back down ring transition,
[3422.80 --> 3423.86]  back up ring transition,
[3423.96 --> 3424.14]  right?
[3424.14 --> 3425.42]  It gets rid of all of that.
[3425.54 --> 3426.94]  So that's what he was asking for.
[3427.00 --> 3428.62]  And this would be like a huge feature.
[3428.62 --> 3431.10]  If there are any kernel devs out there watching,
[3431.28 --> 3433.08]  please add this user level.
[3433.14 --> 3435.08]  Interrupt handling like this would be so useful.
[3435.50 --> 3436.50]  And then that thing,
[3436.60 --> 3441.70]  if it actually wanted to do that huge transition thing can just have a sys call that
[3441.70 --> 3445.18]  it does called actually transfer control to the debugger.
[3445.26 --> 3445.46]  Right?
[3445.74 --> 3446.20]  So anyway,
[3446.40 --> 3448.74]  whole big thing of coolness there.
[3450.52 --> 3451.36]  We can't do it.
[3451.36 --> 3454.02]  All I got from that is horse and debuggy is slow.
[3454.26 --> 3454.96]  That's what I got.
[3455.08 --> 3455.32]  Casey.
[3456.26 --> 3457.96]  I tried so hard,
[3458.06 --> 3458.22]  Ryan.
[3458.36 --> 3459.54]  I tried so hard.
[3459.94 --> 3461.60]  TJ also tries hard.
[3461.72 --> 3462.24]  That's the problem.
[3462.54 --> 3462.72]  Sorry.
[3463.36 --> 3463.60]  Anyway.
[3465.04 --> 3465.48]  Yeah.
[3465.58 --> 3466.02]  Like what,
[3466.08 --> 3466.92]  what example of,
[3467.12 --> 3468.14]  so at a high level,
[3468.26 --> 3470.02]  what you might imagine doing in a debugger that uses,
[3470.02 --> 3473.98]  that sort of where you want that kernel level feature would be,
[3474.10 --> 3474.44]  um,
[3474.66 --> 3476.86]  if you set a break point on a particular line of source code,
[3476.86 --> 3477.72]  if you hit,
[3477.84 --> 3480.10]  if you like run your program within the debugger,
[3480.14 --> 3480.32]  you say,
[3480.40 --> 3480.92]  stop here.
[3481.38 --> 3481.78]  Um,
[3482.06 --> 3482.98]  that's perfectly,
[3483.18 --> 3484.20]  that's like reasonably fast.
[3484.20 --> 3484.60]  Cause those,
[3484.66 --> 3485.14]  those,
[3485.14 --> 3486.14]  uh,
[3486.70 --> 3489.68]  like two transition or three or four transitions,
[3489.68 --> 3490.90]  actually the,
[3491.00 --> 3491.22]  um,
[3491.42 --> 3492.62]  you pay that cost once.
[3492.62 --> 3493.70]  And at the scale of like,
[3493.74 --> 3493.90]  Oh,
[3493.90 --> 3494.64]  run to this line.
[3494.76 --> 3495.54]  It's not really noticeable.
[3496.06 --> 3497.96]  And you wanted to come back to the debugger anyway.
[3497.96 --> 3499.88]  So it's like doing what you wanted roughly.
[3500.04 --> 3500.22]  Right?
[3500.62 --> 3500.92]  Yeah.
[3501.30 --> 3503.10]  So when that gets really,
[3503.30 --> 3506.14]  when you actually really have to pay that cost at a,
[3506.24 --> 3509.72]  to a sort of prohibitive degree in many cases is when you wanted to say,
[3509.80 --> 3511.18]  stop at this line of source code,
[3511.24 --> 3513.40]  but only if this condition is true.
[3513.40 --> 3515.94]  So conditional break points are like super common debugger feature.
[3516.48 --> 3520.76]  And it's like kind of the first version of fancier stuff that a debugger would want to do.
[3521.42 --> 3521.48]  Um,
[3521.82 --> 3524.90]  but this is where it gets really slow because then basically,
[3524.90 --> 3525.52]  um,
[3525.66 --> 3530.62]  the debugger can't like do this installation of code that checks the condition inside of the debuggee.
[3530.78 --> 3535.04]  And so what has to happen is it hits the int three controls transferred back to the debugger.
[3535.12 --> 3536.40]  The debugger checks the condition,
[3536.48 --> 3537.46]  it evaluates some expression.
[3537.46 --> 3540.84]  It like does whatever evaluation stuff it needs to do to check the condition.
[3540.96 --> 3542.34]  And if that condition is false,
[3542.40 --> 3544.98]  then it goes back to the debuggee.
[3545.10 --> 3547.10]  And so if you imagine you put this in a loop,
[3547.10 --> 3549.08]  that's supposed to run a million times,
[3549.08 --> 3550.36]  maybe it happens instantly,
[3550.36 --> 3551.14]  um,
[3551.20 --> 3551.64]  normally,
[3551.64 --> 3555.52]  but because you're paying this round trip cost every single time the thread hits that int three,
[3555.96 --> 3556.36]  it's,
[3556.48 --> 3556.68]  uh,
[3556.68 --> 3558.32]  it just becomes like prohibitively slow.
[3558.42 --> 3558.50]  Now,
[3558.54 --> 3559.70]  if you're doing it once per frame,
[3559.70 --> 3561.16]  like it's still worth for,
[3561.36 --> 3563.98]  it's still worth it for debuggers to have conditional break points today,
[3563.98 --> 3567.24]  but they're like dramatically pessimized just from this problem.
[3567.72 --> 3569.32]  But if that problem were addressed,
[3569.36 --> 3570.70]  you could start doing lots of other things.
[3570.70 --> 3571.96]  Like another thing,
[3572.16 --> 3575.16]  something like printf debugging is profiling,
[3575.34 --> 3575.86]  like marking,
[3576.02 --> 3576.24]  uh,
[3576.24 --> 3577.88]  inserting profiling markup in your program.
[3577.88 --> 3578.66]  Like if you wanted to say,
[3578.66 --> 3578.84]  oh,
[3578.86 --> 3580.46]  I want to sample the time here,
[3580.56 --> 3581.22]  sample the time here.
[3581.52 --> 3582.22]  Let me measure that.
[3582.28 --> 3583.76]  Build me a flame graph of this kind of,
[3583.88 --> 3584.78]  of this kind of thing.
[3584.86 --> 3586.24]  That has the same problem as print debugging,
[3586.34 --> 3586.66]  where it's like,
[3586.72 --> 3586.86]  okay,
[3586.86 --> 3587.84]  go back to the source code,
[3587.96 --> 3589.40]  insert the things that I was looking for,
[3589.74 --> 3590.42]  build the program,
[3590.52 --> 3590.98]  run the program,
[3591.04 --> 3593.02]  get back into the state that I wanted to be looking at,
[3593.24 --> 3594.54]  and then inspect the log.
[3594.78 --> 3595.32]  And then it's like,
[3595.42 --> 3595.58]  oh,
[3595.62 --> 3597.74]  I need to drill one layer deeper into this,
[3597.80 --> 3599.66]  into this like flame graph here,
[3599.70 --> 3601.04]  but I didn't add the markup there.
[3601.16 --> 3602.54]  So let me go back to the program,
[3602.62 --> 3603.28]  add the markup there.
[3603.28 --> 3604.38]  And you can't do it too much.
[3604.44 --> 3605.36]  You can't do it at every function,
[3605.44 --> 3605.82]  for example,
[3605.82 --> 3606.20]  because then,
[3606.50 --> 3606.70]  you know,
[3606.74 --> 3607.16]  then the,
[3607.48 --> 3607.60]  that,
[3607.64 --> 3610.46]  that profiling cost will start adding up like dramatically.
[3610.46 --> 3613.08]  And then you won't even be able to see what the actual performance costs were.
[3613.30 --> 3614.80]  So what,
[3614.92 --> 3616.20]  what the debugger could do is like,
[3616.46 --> 3618.46]  let's just do that dynamically in the debugger.
[3618.52 --> 3619.50]  Let's say add a,
[3619.60 --> 3620.64]  add a line of markup here,
[3620.68 --> 3623.02]  like a sampling line here,
[3623.24 --> 3624.28]  add a sampling line here,
[3624.28 --> 3626.58]  and then it could gather that data completely dynamically.
[3626.70 --> 3630.14]  It'd be way faster to like drill down into problems when it's really uncertain,
[3630.46 --> 3632.12]  what you need to be looking at basically.
[3632.76 --> 3632.86]  So,
[3633.22 --> 3633.96]  so yeah,
[3634.12 --> 3635.04]  that's like the high level,
[3635.04 --> 3636.50]  what you would expect as the user.
[3636.50 --> 3637.88]  If you had this kernel level feature,
[3637.94 --> 3638.28]  basically.
[3638.82 --> 3641.32]  And so what we have to do now,
[3641.40 --> 3641.78]  basically,
[3641.90 --> 3642.10]  right.
[3642.10 --> 3643.46]  If you want to do this kind of thing,
[3643.50 --> 3644.54]  you can still do it,
[3644.54 --> 3648.36]  but what you have to do now is you have to handle a crap ton,
[3648.42 --> 3649.36]  more edge cases,
[3649.58 --> 3649.92]  basically.
[3650.48 --> 3653.34]  So what happens is if you want to,
[3653.64 --> 3656.72]  you can still do effectively this by not using in three,
[3656.84 --> 3657.26]  right?
[3657.28 --> 3660.10]  Cause remember that the important part about three is it's a one byte instruction.
[3660.10 --> 3663.74]  So even if it's overwriting another one byte instruction,
[3663.94 --> 3665.04]  it's okay.
[3665.32 --> 3667.68]  All the code will still work exactly as it should,
[3667.68 --> 3669.54]  because you only have the in three,
[3669.66 --> 3671.60]  just exactly where it needs to be.
[3671.60 --> 3675.44]  And anyone who's like jumping to the bite immediately after that,
[3675.50 --> 3677.94]  doing something weird or who knows what it's fine.
[3677.94 --> 3678.36]  Right?
[3679.36 --> 3679.72]  However,
[3680.08 --> 3684.40]  if we wanted to implement a feature like this without the assistance of in three
[3684.40 --> 3688.70]  or halt or any of the other instructions that go through a table and are one
[3688.70 --> 3688.96]  byte,
[3689.14 --> 3689.26]  right?
[3689.32 --> 3689.70]  There aren't,
[3689.74 --> 3690.22]  there very,
[3690.32 --> 3690.88]  there aren't very many.
[3690.96 --> 3692.18]  I think there might only be those two.
[3692.26 --> 3693.22]  I don't know if there's a third one,
[3693.34 --> 3693.82]  but anyway,
[3694.52 --> 3695.70]  on X86 anyway.
[3696.50 --> 3698.24]  So if you want to do that without this,
[3698.28 --> 3698.94]  and you know,
[3699.00 --> 3701.48]  Ryan has looked at this sort of stuff and this is this kind of thing people are
[3701.48 --> 3702.28]  currently doing.
[3702.34 --> 3703.30]  So this is how you have to do it.
[3703.60 --> 3707.90]  You have to input some kind of a jump or a call actual instruction there,
[3707.90 --> 3709.70]  which takes more than one bite.
[3709.92 --> 3712.00]  So you can still do everything we just said,
[3712.08 --> 3715.80]  but you have to overwrite the thing you were going to overwrite with several
[3715.80 --> 3716.62]  bites potentially.
[3716.90 --> 3718.14]  And when you do that,
[3718.18 --> 3719.54]  now you run the risk of,
[3719.78 --> 3719.88]  Oh,
[3719.98 --> 3724.14]  if those several bites overflow and go into the next instruction,
[3724.40 --> 3727.32]  that could have been instruction that someone was jumping to.
[3727.54 --> 3730.12]  So now we have to do all this checking to figure out like,
[3730.26 --> 3734.14]  is someone jumping into the place that we had to overwrite to and blah,
[3734.16 --> 3734.24]  blah,
[3734.26 --> 3734.32]  blah.
[3734.32 --> 3738.70]  So now what should have been a very straightforward extension of just
[3738.70 --> 3742.54]  patching in an int three and everything works perfectly and guaranteed no
[3742.54 --> 3743.10]  problems.
[3743.44 --> 3746.30]  What should have been a perfect extension of that is now this huge,
[3746.70 --> 3746.76]  like,
[3746.90 --> 3747.14]  Oh,
[3747.24 --> 3748.58]  do we catch all the corner cases?
[3748.74 --> 3749.12]  Oh crap.
[3749.16 --> 3750.64]  It doesn't work in this one place.
[3750.64 --> 3753.72]  And now we got these bug reports and these guys who were doing this thing.
[3753.72 --> 3753.98]  And like,
[3754.04 --> 3754.26]  you know,
[3754.26 --> 3757.98]  and so if the colonel could just add this feature,
[3758.18 --> 3759.82]  all of that complexity goes away.
[3759.92 --> 3760.18]  And there's,
[3760.28 --> 3760.56]  like I said,
[3760.60 --> 3762.08]  so this is a thing that people have done.
[3762.14 --> 3763.06]  It's not like you can't do it.
[3763.24 --> 3763.70]  It's just,
[3763.80 --> 3766.78]  it turns what would have been a very simple problem into a very complicated
[3766.78 --> 3767.16]  problem.
[3767.16 --> 3769.00]  And so that's why it would be great if the colonel could do it.
[3769.56 --> 3770.56]  Colonels are great at that.
[3771.40 --> 3771.70]  Yes.
[3772.00 --> 3773.14]  That's why we call them colonels.
[3773.14 --> 3775.68]  Cause they're like a colonel in a military thing where they,
[3776.18 --> 3777.34]  I don't actually know.
[3777.94 --> 3778.38]  I like it.
[3778.38 --> 3779.02]  Keep going.
[3779.38 --> 3779.52]  Yeah.
[3779.60 --> 3780.40]  We'll cut it out in post.
[3780.40 --> 3781.62]  Where does the colonel keep his armies?
[3782.40 --> 3782.54]  Shoot,
[3782.64 --> 3783.30]  shoot for it again,
[3783.30 --> 3783.74]  Casey here.
[3783.80 --> 3785.24]  It's like the colonels are great at that.
[3785.34 --> 3785.52]  Yeah.
[3785.60 --> 3785.76]  Yeah.
[3785.76 --> 3787.46]  Just like we're going to take it made.
[3787.70 --> 3788.06]  I beep.
[3791.14 --> 3791.78]  Does it,
[3791.84 --> 3795.08]  so are all these things you're describing effectively gone in things like
[3795.08 --> 3797.30]  JavaScript or in any interpreted language,
[3797.30 --> 3799.26]  which has a VM because then the VM can go,
[3799.38 --> 3799.46]  well,
[3799.46 --> 3802.40]  I can just insert and interrupt like right into the bytecode.
[3802.40 --> 3804.80]  I don't even have to worry about it since I'm processing these things.
[3805.40 --> 3808.68]  This do a lot of these problems effectively because the Chrome debugger is
[3808.68 --> 3810.40]  actually shockingly a great debugger.
[3810.40 --> 3812.40]  Well,
[3813.12 --> 3813.84]  okay.
[3815.36 --> 3815.68]  Well,
[3815.78 --> 3816.02]  I mean,
[3816.06 --> 3817.26]  you got to remember you're debugging JavaScript.
[3817.40 --> 3818.02]  There's not like a lot,
[3818.10 --> 3818.30]  you know,
[3818.32 --> 3818.44]  it's,
[3818.44 --> 3818.84]  it's,
[3818.84 --> 3818.88]  it's,
[3818.88 --> 3818.94]  it's,
[3818.94 --> 3819.80]  I've had a lot of,
[3819.96 --> 3820.24]  I've,
[3820.30 --> 3823.78]  I've been not that happy with its accuracy in catching break points and
[3823.78 --> 3824.56]  things like that actually.
[3824.56 --> 3827.06]  So I would not categorize it as a great debugger personally.
[3827.60 --> 3827.96]  Really?
[3827.96 --> 3828.48]  I would,
[3828.48 --> 3831.28]  I would say it's a pretty mediocre debugger in my opinion.
[3832.80 --> 3834.20]  You don't even program JavaScript.
[3834.36 --> 3834.68]  Don't even try.
[3834.68 --> 3834.94]  I do.
[3835.22 --> 3836.20]  I program a lot of JavaScript.
[3836.20 --> 3837.66]  I already know that this is a trap.
[3837.82 --> 3838.76]  This is an int three.
[3839.02 --> 3839.54]  I am not,
[3839.62 --> 3842.12]  I am not getting bamboozled here,
[3842.22 --> 3842.48]  Casey.
[3842.48 --> 3844.36]  I have,
[3844.54 --> 3846.90]  I have used that debugger a bunch.
[3847.04 --> 3848.90]  I had to use that debugger on electron,
[3849.16 --> 3849.78]  even prime.
[3849.90 --> 3850.60]  So I,
[3850.64 --> 3851.90]  I use it locally,
[3851.90 --> 3852.96]  that might be different though.
[3853.14 --> 3854.72]  Local electron fun.
[3854.86 --> 3856.40]  And that was a huge ball.
[3856.56 --> 3857.26]  Like that was,
[3857.32 --> 3857.84]  that was great.
[3857.98 --> 3858.68]  That might be different.
[3858.80 --> 3859.12]  I'm not,
[3859.20 --> 3859.40]  I'm not.
[3859.40 --> 3859.70]  It's not,
[3859.80 --> 3860.20]  it's the same,
[3860.20 --> 3861.32]  but I've used both of them.
[3861.44 --> 3861.58]  Yeah.
[3862.54 --> 3863.12]  It has,
[3863.28 --> 3863.60]  it has,
[3863.66 --> 3865.52]  I feel like it is not reliable.
[3865.76 --> 3867.16]  It is not reliable on a couple of things.
[3868.02 --> 3869.46]  Restarting and catching break points.
[3869.46 --> 3870.82]  When a webpage is reloaded,
[3870.82 --> 3873.12]  I have found it to be fairly unreliable actually.
[3873.18 --> 3874.36]  And that's a very important thing.
[3874.36 --> 3876.38]  Cause if you're trying to bug stuff that happens at startup,
[3876.54 --> 3876.74]  right?
[3876.78 --> 3877.18]  Like at,
[3877.28 --> 3878.38]  at load time,
[3878.38 --> 3879.04]  it just,
[3879.16 --> 3880.02]  and so,
[3880.24 --> 3880.60]  you know,
[3880.82 --> 3881.16]  it's,
[3881.22 --> 3883.02]  it's one of those things where I didn't,
[3883.10 --> 3884.18]  when you use a debugger,
[3884.22 --> 3885.22]  you get this feeling of,
[3885.40 --> 3886.88]  is it solid or is it not solid?
[3886.88 --> 3887.22]  Right?
[3887.26 --> 3887.46]  Not,
[3887.46 --> 3887.68]  not,
[3887.68 --> 3890.82]  not the S O L L D like acronym S O L I G thing,
[3890.90 --> 3892.16]  not list off substitution principle,
[3892.16 --> 3892.80]  but like,
[3892.80 --> 3895.20]  is this thing reliable so that if I set a break point,
[3895.20 --> 3900.44]  I know for sure that this code only got executed when the break point got hit and no other time.
[3900.44 --> 3902.50]  And I definitely can guarantee you that was,
[3902.64 --> 3903.96]  I think I can actually explain that one.
[3904.06 --> 3905.44]  That one I think I can explain because you,
[3905.60 --> 3907.64]  if you use the keyword debugger inside JavaScript,
[3907.76 --> 3909.06]  you'll actually get it every single time.
[3909.06 --> 3911.34]  But if you use the actual Chrome debugger to do that,
[3911.60 --> 3913.66]  it uses the CDP,
[3913.74 --> 3914.92]  the Chrome debugger protocol.
[3915.12 --> 3915.44]  Okay.
[3915.44 --> 3918.18]  And so it has to do some sort of async communication with your process,
[3918.18 --> 3920.10]  which if it loads fast enough,
[3920.10 --> 3921.80]  you're going to miss that entire plane is,
[3922.00 --> 3922.50]  is what I'm,
[3922.54 --> 3924.58]  I'm like 99% sure that's what's happening.
[3924.58 --> 3926.12]  Cause I've ran into a bunch of these issues.
[3926.32 --> 3926.64]  Okay.
[3926.74 --> 3927.16]  Working on,
[3927.24 --> 3928.20]  working on that protocol.
[3928.20 --> 3929.68]  Also now you've run into the issues,
[3929.76 --> 3930.52]  Prime at first.
[3930.58 --> 3930.76]  Yeah.
[3930.76 --> 3931.24]  You said,
[3931.30 --> 3931.42]  yeah.
[3931.60 --> 3931.82]  Oh,
[3931.82 --> 3932.12]  okay.
[3932.22 --> 3933.16]  It is a great one.
[3933.16 --> 3933.46]  If you're,
[3933.58 --> 3934.70]  if you use it correctly,
[3934.70 --> 3935.08]  right?
[3935.10 --> 3935.42]  I mean,
[3935.42 --> 3935.90]  come on,
[3935.96 --> 3938.78]  but that you shouldn't have to write the point of a debugger to save you time.
[3938.78 --> 3942.28]  If I have to go research why this thing can't set a break point and it's like,
[3942.36 --> 3942.66]  Oh,
[3942.80 --> 3945.14]  the thing that's supposed to set the break point,
[3945.32 --> 3946.96]  you don't set break points that way.
[3947.00 --> 3948.40]  You have to use this other thing.
[3948.40 --> 3950.42]  That's not how you set a break point to set a break point.
[3950.50 --> 3951.34]  Like then it's,
[3951.46 --> 3952.74]  then that's worthless because again,
[3952.74 --> 3953.86]  I could have just done printf,
[3953.98 --> 3955.00]  which by the way is what I do.
[3955.00 --> 3957.34]  I do console.log when that kind of thing happens.
[3957.54 --> 3958.82]  So this is why I say,
[3958.94 --> 3960.72]  I totally understand people who like go,
[3960.84 --> 3961.34]  I don't use the bugger.
[3961.36 --> 3961.54]  It's like,
[3961.58 --> 3961.74]  yeah,
[3961.82 --> 3963.46]  because when the debugger is unreliable,
[3963.62 --> 3964.92]  it's not useful.
[3967.40 --> 3967.72]  Yeah.
[3967.72 --> 3968.08]  For me,
[3968.12 --> 3970.62]  I just try to not write bugs in JavaScript and that seems like,
[3970.74 --> 3970.90]  all right.
[3971.12 --> 3971.24]  Yeah.
[3971.24 --> 3972.36]  I don't have any bugs.
[3972.56 --> 3972.70]  So,
[3972.80 --> 3972.96]  you know,
[3973.02 --> 3974.16]  that's why I don't use the bugger.
[3974.24 --> 3975.36]  I don't ever have any bugs.
[3975.42 --> 3976.16]  So I'm not really sure.
[3976.22 --> 3976.70]  Like it's cool.
[3976.82 --> 3977.62]  If you have bugs,
[3977.66 --> 3978.00]  I mean,
[3978.00 --> 3978.84]  you could use one,
[3978.88 --> 3979.36]  I guess.
[3979.36 --> 3979.64]  I mean,
[3979.70 --> 3980.18]  I get it.
[3980.26 --> 3980.40]  Yeah.
[3981.00 --> 3982.98]  Why prime might need one.
[3983.14 --> 3983.34]  Yeah.
[3983.44 --> 3983.66]  Yeah.
[3983.66 --> 3985.72]  That's because I always forget no mistakes.
[3986.22 --> 3986.88]  It's just like,
[3986.92 --> 3988.86]  if I could just add that to the end of my AI prompt,
[3988.94 --> 3989.66]  everything would be great.
[3990.20 --> 3990.40]  See,
[3990.46 --> 3990.88]  that's the problem.
[3990.96 --> 3992.40]  You got to put it in the agent instructions.
[3992.56 --> 3993.98]  So no mistakes is in every one.
[3994.26 --> 3994.48]  See,
[3995.06 --> 3995.92]  make it secure,
[3996.18 --> 3996.84]  make it good.
[3997.04 --> 4000.28]  Don't put it in a Firebase bucket with no authentication.
[4001.66 --> 4004.72]  But also if we could expound on why I don't think the Chrome debugger is
[4004.72 --> 4005.12]  very good.
[4005.28 --> 4007.20]  So going further along those lines.
[4007.74 --> 4008.50]  So again,
[4008.86 --> 4010.46]  in order for a debugger to actually be valuable,
[4010.46 --> 4013.70]  it has to do a lot more things than just stopping where I tell it to
[4013.70 --> 4013.98]  stop,
[4014.08 --> 4015.56]  which already it didn't do.
[4016.12 --> 4019.68]  So the other things that needs to be able to do is gather and like
[4019.68 --> 4022.86]  Marshall and display information to me like cleanly and quickly.
[4022.86 --> 4023.30]  Right.
[4023.30 --> 4025.28]  And it also doesn't do that very well.
[4025.48 --> 4025.52]  Like,
[4025.64 --> 4025.82]  yeah,
[4025.88 --> 4027.42]  it kind of has a watch window.
[4027.42 --> 4029.32]  That's not absolutely horrible or anything,
[4029.32 --> 4031.30]  but it can't do any of the kind of stuff.
[4031.40 --> 4034.28]  Like I love like all the rad debugger features where you can kind of go
[4034.28 --> 4034.46]  like,
[4034.56 --> 4034.78]  Hey,
[4034.92 --> 4036.16]  here's my data structures.
[4036.26 --> 4037.76]  I want to turn that into tabular data.
[4037.76 --> 4040.12]  So like walk this link list for me and show it to me.
[4040.12 --> 4041.92]  Like it was a table and like all that stuff.
[4041.94 --> 4044.40]  Like it can't do any of that stuff as far as I know.
[4044.46 --> 4045.74]  And if you want it to do that stuff,
[4045.76 --> 4047.52]  you'd basically be like programming JavaScript.
[4048.18 --> 4048.44]  You know,
[4048.48 --> 4048.66]  you'd,
[4048.66 --> 4051.86]  you'd have to be like writing your own like JavaScript stuff to do that right in
[4051.86 --> 4053.86]  there,
[4053.86 --> 4054.52]  which is again,
[4054.52 --> 4055.58]  it's taking me more time.
[4055.58 --> 4056.52]  I just do a console log.
[4056.52 --> 4056.58]  And so I think like,
[4056.78 --> 4056.94]  yeah,
[4056.94 --> 4058.62]  like Chrome debugger is pretty mediocre.
[4058.62 --> 4059.98]  I I'm glad they built it,
[4059.98 --> 4060.34]  but it's,
[4060.40 --> 4060.98]  it's not,
[4061.14 --> 4062.48]  it's not in the top tier.
[4062.48 --> 4063.40]  Like it's not an S tier.
[4064.08 --> 4064.36]  Yeah.
[4064.36 --> 4065.04]  Or by any time.
[4065.04 --> 4065.28]  Oh,
[4065.34 --> 4068.14]  we got to come back with a debugger tier list.
[4068.28 --> 4068.52]  Casey,
[4068.52 --> 4070.76]  we're going to do that offline and we'll publish a video.
[4071.46 --> 4072.62]  I think Ryan actually,
[4072.76 --> 4073.80]  could we end with some of that?
[4073.86 --> 4077.24]  Can you talk a little bit about like the cool rad debug features?
[4077.24 --> 4078.74]  Cause like some of that stuff is really cool.
[4078.86 --> 4079.76]  Most people don't know.
[4079.82 --> 4081.76]  You can view like 3d models and rad debug,
[4082.04 --> 4082.38]  right?
[4082.70 --> 4083.06]  Yeah.
[4083.26 --> 4083.50]  Yeah.
[4083.56 --> 4085.40]  So the 3d models,
[4085.52 --> 4086.52]  like some of it's early.
[4086.52 --> 4088.52]  So the 3d model it's solid,
[4088.64 --> 4088.98]  but it's,
[4089.12 --> 4089.58]  but it's,
[4089.60 --> 4089.94]  it's,
[4090.32 --> 4092.06]  I need to work on each,
[4092.14 --> 4095.62]  each visualizer is like a complicated problem that I have to dig into later.
[4095.62 --> 4096.18]  And so,
[4096.28 --> 4096.46]  but I,
[4096.52 --> 4097.68]  but I do have a 3d visualizer.
[4097.68 --> 4099.84]  So basically the way you can,
[4100.40 --> 4104.54]  the way it works is basically what the debugger has got a watch window and in the
[4104.54 --> 4105.22]  watch window you can,
[4105.42 --> 4107.62]  you can enter expressions and they show you,
[4107.68 --> 4109.02]  you can expand them and all that kind of thing.
[4110.86 --> 4114.06]  You can also extend these expressions with like visualizer rules.
[4114.24 --> 4115.82]  So if you wanted to view like some,
[4115.96 --> 4116.58]  like some,
[4117.18 --> 4117.54]  the,
[4117.58 --> 4121.54]  the very common example is viewing like pixel data or bitmap data.
[4121.74 --> 4122.78]  If you wanted to say,
[4122.84 --> 4123.24]  for example,
[4123.24 --> 4126.44]  like I have this pointer to some giant blob of data.
[4126.44 --> 4126.84]  That's,
[4126.94 --> 4128.38]  that's just a sprite sheet or some,
[4128.46 --> 4128.80]  some,
[4128.86 --> 4129.10]  you know,
[4129.10 --> 4131.90]  font at Atlas or something like that.
[4131.90 --> 4132.66]  Um,
[4133.30 --> 4134.52]  what you can basically say is like,
[4135.20 --> 4135.60]  okay,
[4135.60 --> 4139.36]  I want to say that this is a bitmap and then I want to specify some extra
[4139.36 --> 4141.76]  information about like what kind of bitmap it is.
[4141.78 --> 4142.40]  Like how big,
[4142.50 --> 4142.62]  how,
[4142.76 --> 4143.48]  how wide is it?
[4143.50 --> 4144.10]  How tall is it?
[4144.16 --> 4144.30]  What,
[4144.38 --> 4145.82]  what pixel format is it in?
[4146.64 --> 4148.26]  And the expression language,
[4148.26 --> 4151.24]  like in the debugger watch window just allows you to express that kind of
[4151.24 --> 4151.36]  thing.
[4151.38 --> 4154.14]  So you can say like bitmap and then the first argument to,
[4154.40 --> 4156.50]  it's like a call to bitmap and you can say,
[4156.60 --> 4157.10]  here's my pointer,
[4157.22 --> 4157.70]  here's my width,
[4157.74 --> 4158.22]  here's my height.
[4158.28 --> 4159.14]  Those are just expressions.
[4159.14 --> 4160.86]  So they can come from variables in your program.
[4160.86 --> 4161.86]  Um,
[4161.86 --> 4162.28]  and then you can say,
[4162.38 --> 4165.26]  here's my format and then you can expand it and it's going to show you
[4165.26 --> 4167.08]  an actual preview of,
[4167.18 --> 4168.32]  of the image itself.
[4168.50 --> 4170.94]  You can also like pull it out to your own tab and like see like,
[4170.98 --> 4171.10]  Oh,
[4171.16 --> 4171.92]  like here's a full,
[4172.10 --> 4173.72]  fully featured at the limit.
[4173.74 --> 4174.62]  Like once I'm done with it,
[4174.68 --> 4175.48]  it'll be fully featured,
[4176.10 --> 4176.20]  but,
[4176.32 --> 4177.64]  but it's like,
[4177.80 --> 4178.08]  uh,
[4178.08 --> 4178.86]  pull it out to a,
[4178.86 --> 4179.72]  to a tab and then it's like,
[4179.74 --> 4179.80]  Oh,
[4179.82 --> 4180.40]  here's a bitmap view.
[4180.46 --> 4181.08]  I can pan around.
[4181.14 --> 4181.80]  I can zoom in,
[4182.08 --> 4183.68]  check the pixel values and all that kind of thing.
[4184.40 --> 4184.72]  Um,
[4185.32 --> 4189.30]  now every visualization feature in the debugger is sort of implemented in
[4189.30 --> 4189.58]  this way.
[4189.58 --> 4189.82]  So,
[4189.82 --> 4190.38]  uh,
[4190.38 --> 4193.70]  another common one that debuggers often support is like a memory
[4193.70 --> 4194.00]  viewer,
[4194.12 --> 4195.62]  like a hex view of some memory.
[4196.06 --> 4199.18]  It's exactly the same feature in the rad debugger where you can say,
[4199.28 --> 4199.40]  okay,
[4199.46 --> 4200.22]  memory call,
[4200.56 --> 4201.40]  let me call memory.
[4201.52 --> 4202.02]  Here's my pointer.
[4202.14 --> 4202.76]  Here's my size.
[4202.76 --> 4204.34]  Like you can say like number of columns,
[4204.42 --> 4204.60]  number,
[4204.86 --> 4208.72]  all kinds of parameters that you want to do for building this hex viewer.
[4208.82 --> 4210.16]  Basically you expand it.
[4210.24 --> 4212.56]  It's just a memory view of whatever parameters you,
[4212.62 --> 4213.54]  you specify to it.
[4213.98 --> 4214.78]  As Casey said,
[4214.80 --> 4216.02]  there's also a geometry one.
[4216.44 --> 4216.80]  Um,
[4216.82 --> 4217.42]  so if you,
[4217.50 --> 4217.80]  if you,
[4218.02 --> 4218.30]  uh,
[4218.30 --> 4220.16]  you have to specify some pieces of information,
[4220.16 --> 4220.84]  um,
[4221.12 --> 4221.82]  where you can say like,
[4221.86 --> 4222.78]  here's an index buffer.
[4222.86 --> 4223.94]  Here's a vertex buffer.
[4224.38 --> 4225.90]  Here's how many indices I have.
[4225.96 --> 4226.28]  Here's how many,
[4226.28 --> 4226.90]  uh,
[4226.90 --> 4227.84]  vertices I have.
[4228.20 --> 4228.56]  Um,
[4228.98 --> 4230.72]  I don't know if you need to specify the number of vertices.
[4230.82 --> 4231.66]  I have to go look at it.
[4231.72 --> 4231.94]  Um,
[4232.08 --> 4232.26]  but,
[4232.56 --> 4232.88]  uh,
[4232.88 --> 4235.50]  you can basically say this kind of information and,
[4235.72 --> 4236.00]  um,
[4236.84 --> 4237.44]  if you expand it,
[4237.46 --> 4239.12]  you just get the 3d representation of like,
[4239.16 --> 4240.70]  here's all the geometry data that you actually,
[4240.88 --> 4241.56]  actually wanted.
[4241.62 --> 4245.32]  And because this is in a watch window and it's not just like parsing a
[4245.32 --> 4246.68]  format that you dump out of your program,
[4246.68 --> 4248.86]  you see it update live as you step.
[4248.94 --> 4252.42]  So you actually like step over as these vertices are being built and you
[4252.42 --> 4255.16]  can see the vertices change in real time.
[4255.16 --> 4255.58]  So it's,
[4255.64 --> 4257.32]  it's way more useful than like,
[4257.52 --> 4257.96]  uh,
[4258.00 --> 4261.34]  dumping it and then like dumping it to an OBJ and then looking at like
[4261.34 --> 4262.32]  some OBJ viewer,
[4262.44 --> 4263.60]  like this 3d model or whatever,
[4263.70 --> 4264.62]  same thing with texture data.
[4265.24 --> 4265.60]  Um,
[4266.06 --> 4268.04]  and so there's also a bunch of other visualization features,
[4268.04 --> 4270.06]  like more basic ones,
[4270.06 --> 4270.56]  uh,
[4270.56 --> 4272.16]  like viewing multi-line text.
[4272.40 --> 4272.76]  Um,
[4272.78 --> 4273.34]  for example,
[4273.70 --> 4276.20]  it's something that every debugger has to do anyways to show you source
[4276.20 --> 4276.48]  code,
[4276.48 --> 4277.12]  but it's like,
[4277.50 --> 4281.30]  you should just be able to apply that same exact path to like just
[4281.30 --> 4282.98]  viewing any arbitrary textual data.
[4283.48 --> 4283.84]  Um,
[4283.90 --> 4285.80]  the disassembly viewer is also implemented this way.
[4285.84 --> 4286.70]  It's just a visualizer.
[4287.22 --> 4287.54]  Um,
[4287.62 --> 4289.96]  and then there's a bunch of different rules that you can introduce to
[4289.96 --> 4291.06]  like change how it,
[4291.44 --> 4292.30]  how the watch tree.
[4292.46 --> 4293.92]  So when you put in like a watch expression,
[4294.12 --> 4295.26]  if you expand it,
[4295.88 --> 4296.26]  um,
[4296.34 --> 4296.54]  you know,
[4296.54 --> 4299.44]  you get rows generally they're formed by looking at the members of
[4299.44 --> 4301.24]  whatever type you expand or something like that.
[4301.42 --> 4303.98]  There's a bunch of ways you can customize exactly how that looks like as
[4303.98 --> 4304.16]  well.
[4304.18 --> 4304.50]  And that's,
[4304.50 --> 4306.46]  that's sort of more like sort of what visual students do.
[4306.46 --> 4307.44]  Studio did with NatViz.
[4307.52 --> 4308.38]  It's a very similar kind of,
[4308.48 --> 4309.34]  although it's not an X,
[4309.68 --> 4311.74]  you don't specify that in XML in the red fucker,
[4311.78 --> 4311.94]  but,
[4312.04 --> 4313.66]  but you can do like the same kind of thing there.
[4314.04 --> 4314.40]  Um,
[4314.58 --> 4316.04]  and then I guess the final layer,
[4316.18 --> 4318.78]  I could dig into more if of any of that,
[4318.82 --> 4318.92]  but,
[4319.02 --> 4319.58]  uh,
[4319.58 --> 4323.12]  the final layer on top is you can also automatically associate certain types
[4323.12 --> 4324.98]  with certain visualizer expressions.
[4324.98 --> 4326.12]  So you can go ahead and say,
[4326.22 --> 4327.14]  I've got a struct,
[4327.30 --> 4328.22]  it's called bitmap.
[4328.36 --> 4329.08]  It's got a pointer,
[4329.30 --> 4330.44]  a width and a height in a format.
[4330.78 --> 4331.86]  And I'm going to say,
[4331.98 --> 4335.18]  if you evaluate this type anywhere in the program or anywhere,
[4335.18 --> 4338.06]  like if you're in the debugger and you're evaluating anything of this type,
[4338.06 --> 4340.78]  just automatically say it's a bitmap visualizer.
[4340.86 --> 4342.60]  So you're sort of extending type information.
[4342.60 --> 4344.16]  You can put this directly in your program.
[4344.24 --> 4345.60]  You can put it in the debugger configuration,
[4345.60 --> 4347.42]  like really wherever you want.
[4347.58 --> 4351.14]  And then anytime you evaluate that in the debugger by default,
[4351.28 --> 4353.26]  it'll show you that visualization automatically.
[4353.26 --> 4355.02]  So that includes hover evaluation.
[4355.18 --> 4357.22]  So if you hover the bitmap variable in your program,
[4357.34 --> 4359.04]  you'll see the bitmap just pop up.
[4359.16 --> 4360.28]  If you put it in the watch window,
[4360.40 --> 4361.54]  it'll just be the bitmap.
[4361.78 --> 4362.44]  Like it's,
[4362.98 --> 4363.26]  you know,
[4363.52 --> 4364.06]  that's,
[4364.14 --> 4365.42]  that's sort of the final layer to it,
[4365.42 --> 4369.38]  where you can basically extend your program's type info to be automatically
[4369.38 --> 4371.76]  associated with this visualization information.
[4371.86 --> 4372.86]  Now you can always go back.
[4372.92 --> 4373.38]  Like if you're like,
[4373.58 --> 4374.74]  I don't want to look at it as a bitmap.
[4374.80 --> 4375.08]  I want to,
[4375.14 --> 4377.54]  I want to look at it as a struct because that's what it is.
[4377.68 --> 4379.50]  You can always reverse it.
[4379.60 --> 4379.88]  There's,
[4380.00 --> 4380.38]  there's a,
[4380.62 --> 4382.50]  there's a way you can do that inside of the visualization,
[4382.82 --> 4383.10]  like,
[4383.24 --> 4386.10]  or within the expression syntax as well.
[4386.24 --> 4386.38]  So,
[4386.98 --> 4387.98]  but yeah,
[4387.98 --> 4390.18]  there's lots and lots of stuff you can do.
[4390.76 --> 4391.60]  And it's,
[4391.70 --> 4392.22]  that's,
[4392.66 --> 4393.62]  that's like the,
[4394.12 --> 4395.30]  that's a good first run through,
[4395.30 --> 4395.72]  I think.
[4396.28 --> 4397.70]  It also loads fast.
[4398.50 --> 4398.90]  Yeah.
[4399.68 --> 4400.08]  Yeah.
[4400.08 --> 4400.50]  I mean,
[4400.50 --> 4400.96]  it's not,
[4401.10 --> 4403.00]  it's not hard to beat visual studio,
[4403.40 --> 4406.90]  but visual studio can't beat visual studio.
[4407.06 --> 4409.92]  So it's more difficult than maybe they think,
[4410.00 --> 4410.38]  you know?
[4410.38 --> 4411.60]  So I just throwing it out there.
[4411.64 --> 4414.00]  I feel like it's a cool feature is that it actually loads.
[4414.00 --> 4414.16]  Yeah.
[4415.16 --> 4415.60]  Well,
[4415.90 --> 4418.64]  also like some of the things that Ryan was talking about just then are
[4418.64 --> 4421.08]  important in the way that I was trying to describe before.
[4421.22 --> 4421.88]  In other words,
[4422.54 --> 4424.84]  it's really important to remember that a debugger,
[4424.84 --> 4427.04]  having a feature doesn't matter.
[4427.24 --> 4429.64]  If it takes you longer to use that feature,
[4429.64 --> 4431.88]  then print F debugging would have been to find it.
[4432.20 --> 4432.32]  Right.
[4432.40 --> 4435.26]  Or we can extend like the phrase print F debugging.
[4435.40 --> 4437.70]  We're using that as shorthand because like for bitmaps,
[4437.74 --> 4439.10]  you wouldn't be print F debugging,
[4439.24 --> 4440.64]  but you would be doing a similar thing,
[4440.64 --> 4442.88]  which is like dumping the bitmap multiple times.
[4442.94 --> 4446.84]  I've literally written this code before I had rad debugger where like in
[4446.84 --> 4447.18]  the,
[4447.18 --> 4448.70]  in image processing code,
[4448.70 --> 4450.50]  I just insert like dump image here,
[4450.60 --> 4451.18]  dump image here,
[4451.28 --> 4451.86]  dump image here,
[4451.94 --> 4452.48]  dump image here.
[4452.56 --> 4453.54]  And I look to see,
[4453.70 --> 4453.90]  right?
[4454.00 --> 4455.84]  Like where did the problem happen?
[4455.86 --> 4456.16]  And I'm like,
[4456.22 --> 4456.36]  Oh,
[4456.42 --> 4456.70]  okay.
[4456.78 --> 4456.98]  Right.
[4457.28 --> 4460.06]  And so it has to be faster than that.
[4460.32 --> 4462.12]  Cause if it's not faster than that,
[4462.16 --> 4464.20]  there was no point to the debugger having this feature.
[4464.32 --> 4466.80]  And so some of the things that Ryan's talking about are way more
[4466.80 --> 4467.84]  important than they sound.
[4468.14 --> 4471.52]  The ability just to view something as an edit as an image in your
[4471.52 --> 4472.64]  debugger isn't enough.
[4473.10 --> 4475.70]  It's really crucial to have the ability to also say,
[4475.80 --> 4475.98]  look,
[4476.04 --> 4478.58]  when I built this program and this is a really cool feature of a
[4478.58 --> 4478.82]  debugger.
[4479.00 --> 4479.78]  When I built this program,
[4479.78 --> 4483.70]  I just included this little macro that I put that sticks some stuff in
[4483.70 --> 4484.96]  the type information automatically.
[4484.96 --> 4486.64]  When I build the program that just says,
[4486.74 --> 4488.82]  anytime I'm looking at my struct bitmap,
[4489.00 --> 4489.34]  you know,
[4489.38 --> 4489.84]  structure,
[4490.04 --> 4493.00]  it should automatically set it up so that I can view it as the
[4493.00 --> 4493.32]  bitmap.
[4493.76 --> 4496.02]  That is like one little line of code I put in.
[4496.02 --> 4499.70]  And then for the rest of anyone ever using this program inside rad
[4499.70 --> 4500.10]  debugger,
[4500.18 --> 4502.86]  they'll always get it shown as a bitmap automatically with the right
[4502.86 --> 4504.08]  width and height and all that stuff.
[4504.08 --> 4504.32]  Right.
[4504.76 --> 4507.86]  And that is a massive time savings for everyone.
[4508.04 --> 4510.22]  Whereas if it just has this way of like,
[4510.30 --> 4513.60]  I load a plugin and then I instantiate the plugin and I say that I want
[4513.60 --> 4514.30]  it bound to like,
[4514.30 --> 4517.42]  if I'm doing that every time I have to do my bitmap,
[4517.62 --> 4520.56]  it's not saving me the time that I actually needed the debugger for.
[4520.66 --> 4522.42]  So all of these things are wicked important.
[4522.52 --> 4523.58]  And that's why it's so cool.
[4523.58 --> 4526.58]  Like that rad debugger is taking that approach of like,
[4526.70 --> 4528.48]  we actually care about saving you time.
[4528.64 --> 4529.36]  Not just,
[4529.44 --> 4531.06]  we cared about writing on the thing.
[4531.32 --> 4532.10]  It can view an image,
[4532.18 --> 4532.38]  right?
[4532.82 --> 4534.26]  Features can view image.
[4534.44 --> 4535.88]  They got the thing on the front page.
[4536.04 --> 4536.96]  That is not enough,
[4537.06 --> 4537.24]  right?
[4537.30 --> 4538.70]  It needs to be,
[4538.84 --> 4543.22]  I can view and debug image processing faster than if I was print up.
[4543.30 --> 4545.32]  That is the actual feature you want in the debugger.
[4545.40 --> 4546.02]  Cause otherwise,
[4546.16 --> 4546.92]  why are we using it?
[4547.70 --> 4548.14]  Yeah.
[4548.24 --> 4548.40]  Yeah.
[4548.40 --> 4548.70]  You'll see,
[4548.78 --> 4550.66]  you'll see demos of that exact feature too.
[4550.82 --> 4551.32]  Not to not,
[4551.32 --> 4552.38]  I don't want to pick on anyone,
[4552.50 --> 4554.28]  but you can go look at like demo videos.
[4554.36 --> 4554.64]  If they're like,
[4554.70 --> 4554.80]  look,
[4554.84 --> 4556.62]  we can view like images inside of our debugger.
[4556.94 --> 4558.68]  And in the demo video,
[4558.68 --> 4562.60]  it takes like 10 seconds to load or like 30 seconds,
[4562.62 --> 4563.04]  even to,
[4563.12 --> 4564.30]  I can't even remember what it was,
[4564.34 --> 4564.86]  but it was just like,
[4565.12 --> 4565.54]  it's not,
[4565.66 --> 4566.08]  and it's,
[4566.16 --> 4567.22]  it's not just 30 seconds.
[4567.28 --> 4567.96]  And then you can see it.
[4567.96 --> 4568.70]  It's 30 seconds.
[4568.80 --> 4569.84]  Every time you step,
[4569.88 --> 4572.22]  like it's not updating like right away.
[4572.22 --> 4572.66]  So it's,
[4572.66 --> 4573.18]  it's just like,
[4573.28 --> 4574.52]  how is that helping me?
[4574.52 --> 4574.76]  Like,
[4575.38 --> 4576.74]  yeah.
[4577.12 --> 4577.38]  So,
[4577.54 --> 4579.50]  and also another good example of printf.
[4579.56 --> 4580.72]  That's not printf exactly.
[4580.84 --> 4582.16]  It would be graph is like,
[4582.20 --> 4582.56]  if you,
[4582.68 --> 4583.80]  if you log a bunch of,
[4583.90 --> 4586.38]  like if you print off a bunch of graph is like textual data,
[4586.54 --> 4588.32]  you get like a pointer graph view,
[4588.46 --> 4591.04]  or you can like print out a pointer graph.
[4591.08 --> 4593.72]  And then you get this graph structure that you can visualize and see like,
[4593.76 --> 4593.90]  Oh,
[4593.94 --> 4595.14]  is this tree wrong here?
[4595.18 --> 4596.10]  Or is it here or wherever?
[4597.16 --> 4598.92]  I haven't implemented this visualizer yet.
[4598.92 --> 4600.26]  So it's not in the ride debugger yet,
[4600.26 --> 4600.68]  but it's like,
[4600.74 --> 4603.04]  that's the kind of thing where I'd like to push it where it's like,
[4603.04 --> 4603.18]  no,
[4603.22 --> 4603.62]  you can just,
[4604.10 --> 4607.82]  you can just see your pointer graphs update in real time as you step.
[4607.94 --> 4608.00]  And,
[4608.00 --> 4608.28]  and,
[4608.28 --> 4609.02]  and so,
[4609.96 --> 4610.22]  so yeah,
[4610.22 --> 4611.62]  that kind of thing would be really nice.
[4612.58 --> 4613.70]  We have to write in it.
[4613.78 --> 4615.26]  We have to write a real language though.
[4615.66 --> 4616.04]  I know.
[4616.16 --> 4617.56]  I'm sitting here thinking the whole time,
[4617.70 --> 4617.78]  like,
[4617.86 --> 4618.16]  man,
[4618.74 --> 4621.38]  TJ made me do Elixir and now I can't change.
[4621.50 --> 4622.32]  Like now I want to,
[4622.42 --> 4622.76]  now I want,
[4622.84 --> 4622.98]  I,
[4623.04 --> 4625.36]  I can't change languages just to use it.
[4625.44 --> 4627.28]  We have observer in Elixir.
[4627.38 --> 4628.14]  We have observer.
[4628.14 --> 4629.34]  It is actually good.
[4629.62 --> 4630.38]  Like it actually is.
[4630.58 --> 4632.06]  Elixir is not a compiled language.
[4633.04 --> 4635.14]  It compiles to a VM stuff.
[4635.28 --> 4635.46]  Yeah.
[4635.78 --> 4636.54]  And then it runs,
[4637.20 --> 4639.94]  but the observation tools are very cool.
[4639.94 --> 4643.68]  Cause it actually is set up to observe everything across your distributed system,
[4643.68 --> 4645.42]  which is like sometimes kind of difficult.
[4645.42 --> 4647.48]  They can be running on other computers and everything,
[4647.48 --> 4647.72]  right?
[4647.72 --> 4648.58]  Like it's not so,
[4648.66 --> 4650.32]  not so simple to do,
[4650.38 --> 4653.00]  but Elixir has very nice tooling around this.
[4653.06 --> 4653.10]  Well,
[4653.10 --> 4653.90]  that's kind of a bummer,
[4654.02 --> 4654.42]  but like,
[4654.46 --> 4654.60]  yeah,
[4654.60 --> 4654.90]  any,
[4655.00 --> 4657.46]  any compiled language you could be using around it.
[4657.46 --> 4657.60]  Like,
[4657.64 --> 4657.80]  you know,
[4657.80 --> 4659.14]  you could use rust or something,
[4659.24 --> 4659.40]  right?
[4659.48 --> 4659.70]  You don't,
[4659.78 --> 4660.94]  it doesn't have to be C++.
[4661.18 --> 4664.32]  If it's compiled and produces debug info,
[4664.32 --> 4666.16]  then it can do it.
[4666.26 --> 4666.40]  So,
[4666.52 --> 4666.66]  you know,
[4666.72 --> 4669.00]  you could be using it with ginger bill was on.
[4669.08 --> 4669.86]  You could use it with Odin,
[4669.98 --> 4670.78]  I believe just fine.
[4670.82 --> 4671.06]  Right.
[4671.24 --> 4672.16]  So ginger bill,
[4672.38 --> 4674.22]  well known debugger hater.
[4674.22 --> 4674.74]  Uh,
[4674.74 --> 4676.06]  he said it doesn't work for Odin.
[4676.20 --> 4681.96]  So I doubt that hates package managers and LSP as well.
[4681.96 --> 4682.32]  Uh,
[4682.44 --> 4684.30]  but that's just a joke from yesterday.
[4684.48 --> 4684.74]  Okay.
[4684.84 --> 4685.28]  I,
[4685.28 --> 4686.96]  I happen to know it's false too.
[4687.02 --> 4687.56]  Cause he,
[4687.68 --> 4691.60]  he literally put in special features into the Odin compiler to work better with the
[4691.60 --> 4691.76]  random.
[4691.90 --> 4694.38]  He was literally in chat five seconds ago saying,
[4694.46 --> 4695.90]  I'm going to go watch from the beginning.
[4696.14 --> 4696.62]  Uh,
[4696.62 --> 4697.70]  so that I can see what's happening.
[4697.70 --> 4700.26]  I just wanted to say I use rad debugger every day.
[4700.26 --> 4700.50]  Yeah.
[4700.50 --> 4701.62]  That's what I was going to say.
[4701.78 --> 4703.18]  Like ginger bill,
[4703.18 --> 4705.34]  part of the episode and he's going to be mauled.
[4705.78 --> 4706.14]  Yeah.
[4706.32 --> 4706.44]  Yeah.
[4706.58 --> 4708.22]  I cannot wait for the comment.
[4708.52 --> 4708.66]  Oh,
[4708.72 --> 4709.28]  you actually do.
[4709.30 --> 4709.44]  Oh,
[4709.48 --> 4709.72]  okay.
[4709.72 --> 4710.18]  They were joking.
[4712.00 --> 4715.22]  I'm about to get a very angry email and then he's going to watch the rest of the episode.
[4715.26 --> 4716.02]  It was in his BS.
[4716.20 --> 4719.00]  It was his better software BSC comp talk.
[4719.12 --> 4719.72]  He literally pointed.
[4719.80 --> 4720.78]  He was like rad debugger.
[4720.98 --> 4722.98]  He announced that it was coming to Mac OS,
[4723.04 --> 4723.82]  which it's not.
[4724.30 --> 4725.98]  So that was interesting.
[4725.98 --> 4726.58]  Right.
[4727.84 --> 4728.76]  So I don't know.
[4728.76 --> 4729.20]  He,
[4729.20 --> 4729.50]  he,
[4729.50 --> 4730.68]  he basically is forcing.
[4730.86 --> 4732.12]  He's this is a,
[4732.12 --> 4734.58]  this is a well-known like a Gabe Newell tactic.
[4734.76 --> 4736.46]  He will just announce something to,
[4736.56 --> 4740.52]  so that then everyone has to ship the thing because it's been said publicly.
[4740.52 --> 4740.82]  Right.
[4740.82 --> 4741.54]  And so like he,
[4741.54 --> 4741.76]  he,
[4741.80 --> 4743.86]  he took a page from that playbook as like,
[4743.92 --> 4744.14]  well,
[4744.24 --> 4745.62]  if I announce it's coming to Mac,
[4745.68 --> 4746.60]  it's got to come to Mac.
[4746.84 --> 4747.36]  That's a,
[4747.46 --> 4748.10]  that's TDD,
[4748.34 --> 4748.52]  right?
[4748.60 --> 4749.64]  Talk driven development.
[4749.72 --> 4750.02]  Yes.
[4750.02 --> 4750.30]  Oh,
[4750.38 --> 4750.64]  yes.
[4750.74 --> 4750.94]  Yes.
[4750.94 --> 4751.10]  Right.
[4751.36 --> 4753.06]  P P P D D press driven development.
[4753.24 --> 4753.42]  Yeah.
[4753.94 --> 4754.30]  Well,
[4754.30 --> 4755.14]  I'm very happy,
[4755.24 --> 4755.46]  Ryan,
[4755.54 --> 4759.32]  you came on the standup today to announce Linux is going to be happening in the next few weeks.
[4759.32 --> 4761.40]  So thank you very much for doing that.
[4762.78 --> 4763.56]  It's crazy.
[4763.88 --> 4764.94]  You heard it here first.
[4765.18 --> 4765.48]  Yeah.
[4765.52 --> 4767.40]  You heard it here first.
[4768.14 --> 4768.52]  Thank you.
[4768.58 --> 4768.94]  At last.
[4769.14 --> 4769.70]  Ryan said,
[4769.78 --> 4771.88]  Tim Sweeney personally told me that we,
[4771.88 --> 4772.86]  there you go.
[4774.08 --> 4774.48]  Yep.
[4775.04 --> 4775.32]  Yep.
[4776.76 --> 4777.12]  Yeah.
[4777.24 --> 4777.34]  Well,
[4777.36 --> 4777.94]  thanks for,
[4778.06 --> 4778.76]  thanks for having me though.
[4778.76 --> 4779.16]  It was,
[4779.30 --> 4779.94]  it was a lot of fun.
[4780.18 --> 4780.40]  Yeah.
[4780.64 --> 4781.20]  This is great.
[4781.60 --> 4784.00]  Thanks for explaining how complicated step stuff is.
[4785.36 --> 4785.72]  It's,
[4785.80 --> 4788.12]  it's so ridiculous when you think it's going to be easy,
[4788.12 --> 4788.40]  right?
[4788.40 --> 4788.72]  It's like,
[4788.74 --> 4790.00]  I just stepping over this line.
[4790.02 --> 4790.38]  It's like,
[4790.38 --> 4790.70]  Nope.
[4790.98 --> 4791.28]  Yep.
[4791.62 --> 4791.86]  Yep.
[4792.52 --> 4792.76]  Yeah.
[4792.76 --> 4792.96]  Sorry.
[4793.02 --> 4795.74]  The recursive one really blew my mind because that actually just,
[4795.84 --> 4796.08]  I mean,
[4796.10 --> 4796.60]  that one I was,
[4796.84 --> 4797.56]  cause now you're counting,
[4797.68 --> 4798.92]  you're like ref counting basically.
[4798.92 --> 4799.28]  Right?
[4799.38 --> 4799.62]  Like,
[4799.66 --> 4799.84]  yeah.
[4799.96 --> 4800.22]  Yeah.
[4800.44 --> 4802.30]  I thought the stack pointer thing was really clever.
[4802.40 --> 4803.88]  Do you use the stack pointer effectively?
[4803.88 --> 4805.98]  Like save the original address at that time.
[4805.98 --> 4808.64]  And then until you return to that stack pointer,
[4808.64 --> 4808.98]  you're like,
[4809.06 --> 4812.38]  I'm somewhere within the recursive realm.
[4813.00 --> 4814.66]  We do have that path,
[4814.66 --> 4818.72]  but we actually figured out something cleverer for the recursive step case.
[4818.84 --> 4819.58]  Cause generally like,
[4819.84 --> 4820.46]  nice try,
[4820.56 --> 4820.84]  buddy.
[4821.10 --> 4821.94]  Nice try.
[4821.94 --> 4824.70]  But actually we thought of something not stupid.
[4826.36 --> 4826.80]  Okay.
[4827.00 --> 4827.60]  First off,
[4827.72 --> 4828.84]  own second off.
[4828.96 --> 4829.44]  Wrecked.
[4831.96 --> 4832.38]  All right.
[4832.44 --> 4832.80]  So tell,
[4832.90 --> 4833.94]  tell my dumbness,
[4834.02 --> 4834.84]  how you do it then?
[4835.18 --> 4835.58]  Ryan.
[4835.80 --> 4837.40]  I remember when I was naive,
[4837.78 --> 4839.36]  I thought that might be an option.
[4840.62 --> 4841.06]  Actually,
[4841.10 --> 4841.36]  you know what?
[4841.36 --> 4843.10]  I want TJ to explain it really quick.
[4843.52 --> 4843.58]  Yeah.
[4843.64 --> 4843.84]  Yeah.
[4843.84 --> 4844.88]  Any,
[4845.02 --> 4848.32]  anytime a guest tries to politely say how they did something,
[4848.50 --> 4849.34]  TJ is just like,
[4849.46 --> 4851.62]  this is an opportunity to make fun of prime.
[4851.86 --> 4852.22]  Yeah.
[4852.22 --> 4852.68]  That's true.
[4852.80 --> 4853.54]  For me,
[4853.72 --> 4854.74]  stepping's very easy.
[4854.82 --> 4855.98]  I just do left foot.
[4856.28 --> 4856.58]  Right.
[4857.30 --> 4857.70]  Right.
[4858.42 --> 4860.24]  That's like what I was showing earlier.
[4860.24 --> 4861.66]  I literally did a live demo.
[4862.00 --> 4862.48]  I was like,
[4862.48 --> 4863.60]  here's how I want.
[4863.94 --> 4865.40]  I'm stepping right now.
[4865.40 --> 4865.88]  Okay.
[4867.14 --> 4867.58]  Okay.
[4867.68 --> 4869.04]  So what is the cleverer way?
[4869.46 --> 4869.68]  Yeah.
[4870.00 --> 4870.40]  Yes.
[4870.50 --> 4876.12]  So the clever way you can do is instead of checking the stack pointer on every recursive,
[4876.38 --> 4879.92]  like every recursion downstream of wherever you wanted to step over,
[4880.12 --> 4882.46]  you would hit that trap and have to check the stack pointer.
[4882.78 --> 4883.72]  What you can do.
[4883.94 --> 4887.54]  And so like recursive calls get very expensive to step over that way.
[4887.68 --> 4893.40]  What you can do instead is you can basically say when you call into the recursive call,
[4893.40 --> 4895.60]  or really whenever you call into anything,
[4895.60 --> 4896.14]  because it could,
[4896.22 --> 4897.36]  it could call into one function,
[4897.38 --> 4898.54]  which calls back into the same phone.
[4898.56 --> 4900.88]  It could be one of those like ping pong recursions.
[4901.04 --> 4902.54]  So anytime you call into anything,
[4902.76 --> 4906.58]  I want to catch whenever that call returns back to me,
[4906.58 --> 4908.62]  which I don't,
[4908.68 --> 4911.14]  I can't rely on the code address to do that.
[4911.14 --> 4911.54]  Cause again,
[4911.84 --> 4912.98]  it'll hit that trap first.
[4912.98 --> 4917.58]  So what I can do instead is basically turn off all the traps that I've set to,
[4917.66 --> 4918.72]  to catch this step.
[4918.80 --> 4922.84]  And then I'm just going to completely fake an instruction pointer on the stack.
[4922.84 --> 4923.22]  So it'll,
[4923.66 --> 4923.80]  when,
[4923.94 --> 4924.36]  so it,
[4924.50 --> 4924.96]  cause when,
[4925.06 --> 4925.54]  when you call,
[4925.62 --> 4928.32]  it pushes the return address of the instruction pointer onto the stack.
[4928.34 --> 4929.54]  And then when the call completes,
[4929.54 --> 4929.78]  it'll,
[4929.88 --> 4931.22]  it'll jump back to that,
[4931.22 --> 4931.52]  uh,
[4931.52 --> 4932.64]  that call address.
[4932.78 --> 4933.16]  Yeah.
[4933.22 --> 4933.46]  Yeah.
[4933.52 --> 4934.10]  So it's,
[4934.10 --> 4934.42]  it's,
[4934.46 --> 4935.18]  it's super nice.
[4935.18 --> 4937.02]  Cause then you can say after this call happens,
[4937.02 --> 4938.88]  it's going to have pushed some address onto the stack,
[4938.90 --> 4939.80]  which is the real return.
[4939.96 --> 4940.54]  I'll romp it.
[4940.54 --> 4941.86]  I'm going to fake that.
[4942.04 --> 4942.30]  Nice.
[4942.46 --> 4943.62]  And then whenever they return,
[4943.74 --> 4944.46]  I'll get an exception,
[4944.80 --> 4945.66]  not from an int three,
[4945.80 --> 4946.20]  but from,
[4946.46 --> 4947.64]  I just executed some rent,
[4947.78 --> 4949.22]  like whatever the bogus address was.
[4949.32 --> 4950.60]  We happen to use nine one.
[4950.60 --> 4950.88]  One.
[4951.20 --> 4952.16]  So we just like,
[4952.22 --> 4953.22]  we just say like,
[4953.60 --> 4955.42]  we put nine one one in there as the return address.
[4955.42 --> 4956.46]  And then we'll get an exception.
[4956.46 --> 4956.86]  That's like,
[4957.12 --> 4957.42]  Oh,
[4957.48 --> 4958.24]  like I don't even,
[4958.38 --> 4959.76]  I can't even access that page.
[4959.76 --> 4960.54]  Like there's no code there.
[4960.60 --> 4962.76]  How I'm trying to access address nine one one.
[4962.76 --> 4963.82]  And to the debugger,
[4963.90 --> 4964.26]  that means,
[4964.46 --> 4964.68]  Oh,
[4964.84 --> 4965.92]  you've finished the call,
[4966.18 --> 4969.78]  move back to the original return address and then reset all the traps.
[4970.50 --> 4971.52]  So very clever.
[4971.84 --> 4972.98]  Nice question.
[4973.12 --> 4973.30]  Yeah.
[4973.30 --> 4975.14]  That I have two questions.
[4975.24 --> 4975.98]  I have actually.
[4976.70 --> 4977.06]  Okay.
[4977.16 --> 4979.54]  So the first one is,
[4979.76 --> 4980.28]  hold on.
[4980.36 --> 4981.10]  I got to pee.
[4981.32 --> 4982.14]  I have to pee.
[4982.14 --> 4982.44]  Oh my God.
[4982.64 --> 4982.96]  Okay.
[4983.78 --> 4984.14]  Hey,
[4984.18 --> 4984.36]  prime.
[4984.42 --> 4984.88]  Nice shirt.
[4986.80 --> 4987.80]  Did you guys see a shirt?
[4987.90 --> 4988.40]  It's pretty good.
[4988.52 --> 4989.40]  I didn't see the shirt.
[4990.00 --> 4990.30]  I just,
[4990.42 --> 4991.10]  when he comes back,
[4991.18 --> 4991.36]  you'll,
[4991.46 --> 4992.08]  you'll laugh.
[4994.08 --> 4994.48]  Okay.
[4994.80 --> 4995.02]  Casey,
[4995.08 --> 4995.84]  just ask your questions.
[4995.90 --> 4996.20]  It's okay.
[4996.46 --> 4997.20]  I can watch it.
[4997.28 --> 4997.98]  Watch it back later.
[4997.98 --> 4999.86]  Well,
[4999.96 --> 5001.98]  can you go grab,
[5002.22 --> 5003.82]  like when they edit this together,
[5004.00 --> 5006.78]  grab video of prime still sitting there going like,
[5007.92 --> 5008.16]  Oh,
[5008.28 --> 5008.56]  smart.
[5008.72 --> 5009.00]  Very smart.
[5009.10 --> 5009.26]  Right.
[5009.34 --> 5011.44]  So it looks like he's watching the whole time.
[5011.78 --> 5012.22]  Well,
[5012.30 --> 5013.10]  at the tower,
[5013.36 --> 5014.84]  because we use wireless mics,
[5015.02 --> 5018.40]  I think one or two times he went pee with the mic still on.
[5018.52 --> 5019.68]  And you could hear it in your,
[5019.80 --> 5021.02]  you could hear it in your ears.
[5021.20 --> 5022.04]  Trigger and assert.
[5023.00 --> 5024.16]  When I click here,
[5024.30 --> 5024.84]  that's sick.
[5025.46 --> 5026.44]  Which is pretty good.
[5026.50 --> 5027.82]  That's courtesy of low level.
[5027.98 --> 5028.18]  Hey,
[5028.26 --> 5028.52]  Hey,
[5028.52 --> 5030.72]  can we move at least the line down?
[5030.84 --> 5031.08]  Dude.
[5031.22 --> 5032.16]  Oh my goodness.
[5032.52 --> 5032.88]  Prime.
[5033.24 --> 5033.60]  Prime.
[5034.12 --> 5034.80]  Oh God.
[5034.88 --> 5035.08]  Prime.
[5035.12 --> 5035.56]  He's doing it.
[5035.62 --> 5035.92]  No.
[5036.20 --> 5037.82]  That's literally like the naked gun,
[5037.96 --> 5038.16]  right?
[5038.22 --> 5041.18]  Like that's literally a scene from the first naked gun movie.
[5041.34 --> 5041.50]  Yeah.
[5041.82 --> 5042.66]  And we,
[5042.76 --> 5044.06]  I had in ear monitoring,
[5044.06 --> 5044.54]  you know,
[5044.54 --> 5047.24]  for like our mics to make sure levels were fine and stuff.
[5047.32 --> 5047.66]  So like,
[5047.80 --> 5048.68]  I'm just sitting here,
[5048.78 --> 5051.12]  I'm sitting in the middle of the room and I just hear him.
[5051.28 --> 5051.66]  And I'm like,
[5051.76 --> 5052.94]  what is that again?
[5053.66 --> 5053.90]  Yeah.
[5053.90 --> 5054.34]  Okay.
[5058.80 --> 5060.58]  So my first question is,
[5060.78 --> 5061.12]  uh,
[5061.50 --> 5064.60]  what happens?
[5064.60 --> 5065.94]  Cause I have no idea.
[5065.94 --> 5071.00]  What happens in that scenario with like the return address,
[5071.26 --> 5073.30]  the special return address stack?
[5073.36 --> 5074.50]  Does it actually,
[5074.72 --> 5075.78]  is it smart enough?
[5075.88 --> 5082.84]  Is the CPU smart enough to go like somebody modified the IP on the actual stack?
[5082.84 --> 5089.16]  So I'm going to like go modify the return address stack or does the CPU always,
[5089.16 --> 5090.26]  I've never looked at this before.
[5090.34 --> 5093.50]  Does the CPU always check when it pops?
[5093.72 --> 5096.20]  You might not know this cause maybe it just works when it,
[5096.26 --> 5097.88]  when it actually goes to do a ret,
[5097.94 --> 5099.96]  does it just check the return address stack and go,
[5100.12 --> 5101.04]  if it didn't match,
[5101.04 --> 5103.06]  then I don't do it or something.
[5103.22 --> 5104.56]  Or do you know?
[5104.80 --> 5105.04]  I,
[5105.48 --> 5106.08]  to my knowledge,
[5106.08 --> 5108.36]  it always will just take the address and jump to it.
[5108.42 --> 5108.76]  So it'll,
[5108.84 --> 5109.18]  it'll,
[5109.56 --> 5109.86]  it'll,
[5109.86 --> 5111.20]  and I don't,
[5111.30 --> 5114.08]  I don't know for sure because it did just work where basically we're like,
[5114.14 --> 5115.44]  let's just phony this address.
[5115.44 --> 5116.90]  And then it just went to it.
[5116.90 --> 5117.38]  And we were like,
[5117.40 --> 5117.62]  okay,
[5117.84 --> 5119.08]  it went to it.
[5119.20 --> 5119.82]  So then Ed says,
[5119.90 --> 5120.20]  yes,
[5120.60 --> 5121.12]  a hundred percent.
[5121.20 --> 5121.46]  You're right.
[5121.48 --> 5123.46]  Ryan low level TV confirms in the chat.
[5124.10 --> 5127.98]  Nice confirms what exactly what you said that it doesn't check.
[5129.20 --> 5129.60]  Ah,
[5129.70 --> 5129.94]  okay.
[5130.02 --> 5130.86]  Doesn't check.
[5131.24 --> 5131.88]  Then you say it doesn't,
[5131.94 --> 5132.72]  it just doesn't pop.
[5132.78 --> 5133.14]  I don't know.
[5133.24 --> 5134.42]  That's what it has to check.
[5134.42 --> 5138.66]  So just to be clear inside a lot of CPUs now there.
[5138.66 --> 5141.56]  So there's the stack as you think of the stack,
[5141.66 --> 5145.54]  meaning the actual program stack that we push like arguments and stuff on,
[5145.64 --> 5147.76]  or like stack variables or whatever the crap,
[5147.86 --> 5148.00]  right?
[5148.06 --> 5150.84]  Like things that don't fit in registers when we're passing or any other things
[5150.84 --> 5151.24]  like that.
[5151.88 --> 5152.20]  Uh,
[5152.44 --> 5153.08]  and we put,
[5153.22 --> 5154.42]  push the IPs on there,
[5154.44 --> 5157.20]  but that's not where the IPs to return to actually come from.
[5157.26 --> 5158.96]  They come from a thing called the shadow stack,
[5159.02 --> 5159.24]  right?
[5159.26 --> 5162.52]  Which is like another thing that's kept as like a separate,
[5162.78 --> 5163.22]  right?
[5163.22 --> 5163.78]  You know what I'm saying?
[5164.14 --> 5164.34]  Anyone?
[5165.16 --> 5165.96]  And there's also a thing called,
[5165.96 --> 5168.44]  there's also a thing called a return address,
[5168.44 --> 5168.82]  but there's,
[5168.94 --> 5171.78]  there's a bunch of things in the CPU that are tracking this information.
[5171.78 --> 5173.82]  It's not actually from the stack anymore.
[5173.82 --> 5175.46]  Like that's kind of like old news,
[5175.50 --> 5175.72]  right?
[5176.24 --> 5176.68]  Uh,
[5176.74 --> 5178.80]  low level TV saying the shadow stack is rarely used.
[5178.88 --> 5179.80]  They go on the real stack,
[5179.80 --> 5180.84]  but there,
[5180.96 --> 5181.70]  but it's there.
[5181.74 --> 5183.24]  So what happens if that is,
[5183.30 --> 5185.38]  what I'm asking is what happens if that is on,
[5185.66 --> 5188.28]  we should just get Ed in here and he should just explain it.
[5188.28 --> 5188.50]  Okay.
[5189.08 --> 5189.96]  Next episode.
[5190.38 --> 5191.10]  Next episode.
[5191.28 --> 5191.74]  That's true.
[5191.84 --> 5192.10]  Yeah.
[5192.10 --> 5194.00]  I want to know what happens if you,
[5194.12 --> 5194.36]  I want,
[5194.44 --> 5195.20]  cause I don't know,
[5195.26 --> 5196.36]  like I,
[5196.40 --> 5201.94]  I assume the CPU actually has like some kind of a path for this or
[5201.94 --> 5202.46]  something,
[5202.46 --> 5204.68]  meaning like it would look and go like,
[5205.12 --> 5205.34]  Oh,
[5205.38 --> 5206.88]  someone did modify the stack.
[5206.98 --> 5209.74]  So I can't just assume that it's,
[5209.80 --> 5210.88]  yeah,
[5210.88 --> 5211.48]  I don't know.
[5211.48 --> 5211.82]  Like,
[5213.24 --> 5213.84]  like,
[5213.84 --> 5213.94]  like,
[5213.94 --> 5214.06]  like,
[5214.06 --> 5215.74]  I don't know what they did there.
[5215.74 --> 5217.66]  And maybe I can probably just go read it.
[5217.66 --> 5219.50]  Like it's probably in the Intel architecture manual.
[5219.68 --> 5219.94]  Right.
[5220.00 --> 5220.44]  So I,
[5220.46 --> 5221.40]  I will go do that after,
[5221.40 --> 5222.70]  but I'm just curious if you ran into it.
[5222.70 --> 5222.96]  It's probably in the W3C spec.
[5223.34 --> 5224.48]  It's probably in the W3C.
[5224.86 --> 5225.18]  Yeah.
[5225.34 --> 5225.58]  Yeah.
[5225.58 --> 5226.12]  I didn't,
[5226.50 --> 5227.62]  I did not run into that.
[5227.86 --> 5228.54]  So it just works.
[5228.68 --> 5229.52]  I did the naive thing.
[5229.64 --> 5229.84]  Yeah.
[5229.84 --> 5232.98]  I did the naive thing that assumes it is on the stack and then it
[5232.98 --> 5233.22]  worked.
[5233.34 --> 5233.52]  Yeah.
[5233.58 --> 5235.14]  So I only know about the shadow dom.
[5236.08 --> 5236.70]  Shadow dom.
[5236.98 --> 5237.18]  Well,
[5237.38 --> 5238.78]  cause there's stuff like that where like,
[5238.78 --> 5239.86]  if you do code pages,
[5239.94 --> 5240.02]  right,
[5240.02 --> 5241.34]  if you do self modifying code,
[5241.38 --> 5241.76]  for example,
[5241.76 --> 5244.06]  that doesn't really work anymore unless you invalidate the
[5244.06 --> 5244.78]  instruction cache.
[5245.00 --> 5245.20]  Right.
[5245.20 --> 5248.40]  Like that was the thing that actually broke because of,
[5248.50 --> 5250.02]  because of having like multiple efforts.
[5250.12 --> 5252.48]  So I didn't know if there would be something like that with all
[5252.48 --> 5254.70]  these additional ways that return addresses get checked because
[5254.70 --> 5257.66]  they just assume that no one's patching the return address.
[5257.88 --> 5257.90]  And,
[5258.02 --> 5260.34]  and so I didn't know if that was an actual assumption.
[5260.42 --> 5261.50]  And so you would be like,
[5261.56 --> 5261.90]  Oh yeah,
[5261.90 --> 5266.96]  we had to call the like invalidate the return address stack thing or
[5266.96 --> 5267.28]  whatever.
[5267.28 --> 5267.68]  Right.
[5267.68 --> 5268.08]  And,
[5268.28 --> 5269.30]  or if it just works.
[5269.30 --> 5270.56]  And I guess the answer is it just works.
[5270.90 --> 5272.20]  My second question was,
[5272.32 --> 5274.68]  would a data break point work for that?
[5274.68 --> 5276.88]  You got to expand on what a data break point.
[5277.02 --> 5278.16]  If you set a break point,
[5278.16 --> 5282.02]  if you set a break point where you said this,
[5282.16 --> 5284.04]  at this location on the stack,
[5284.14 --> 5285.90]  I am setting a break point.
[5286.18 --> 5288.74]  If anyone reads it or something like this.
[5289.56 --> 5290.04]  Yeah,
[5290.06 --> 5291.06]  I guess you could,
[5291.12 --> 5293.20]  I guess the reason why you wouldn't want to is,
[5293.34 --> 5296.50]  is to keep those slots for like open for user break points.
[5296.72 --> 5296.88]  Yeah.
[5297.16 --> 5297.60]  So,
[5297.92 --> 5299.68]  so I didn't think of doing that,
[5299.70 --> 5301.28]  but I think you probably could do that.
[5301.28 --> 5303.20]  I don't know if it would catch the,
[5303.34 --> 5303.50]  like,
[5304.00 --> 5306.70]  will that catch instructions that aren't literal reads,
[5306.76 --> 5309.16]  but just mechanisms that the CPU uses to pull the return address.
[5309.26 --> 5310.34]  I'm not a hundred percent sure,
[5310.46 --> 5311.94]  but it's good idea.
[5312.02 --> 5312.52]  Like with the ret,
[5312.58 --> 5315.68]  like ret maybe bypasses the data break point possibly.
[5315.68 --> 5316.00]  Right.
[5316.70 --> 5317.06]  Yeah.
[5317.06 --> 5318.20]  I'm not a hundred percent sure.
[5318.30 --> 5318.52]  I don't know.
[5318.58 --> 5318.80]  All right.
[5319.08 --> 5319.76]  I know nothing,
[5319.86 --> 5320.70]  but I'd like to give my,
[5320.86 --> 5322.20]  I'd like to shoot my shot as well.
[5322.30 --> 5322.94]  Could you push a,
[5323.10 --> 5328.20]  like a fake stack frame on that has a single instruction function that is just an
[5328.20 --> 5331.82]  int three or whatever the break is and then continue on and let it go.
[5331.88 --> 5332.76]  And then when it comes back,
[5332.80 --> 5332.90]  it,
[5333.04 --> 5337.14]  so it has to bypass through that function,
[5337.18 --> 5337.66]  no matter what.
[5338.34 --> 5339.36]  In one sense,
[5339.42 --> 5339.60]  like,
[5339.66 --> 5341.64]  so we actually started this idea back when,
[5341.80 --> 5343.30]  back when I was prototyping stepping,
[5343.30 --> 5344.78]  we started with that idea.
[5344.78 --> 5345.74]  Um,
[5346.20 --> 5347.72]  we didn't move to nine one one.
[5349.00 --> 5349.66]  Just like,
[5349.96 --> 5350.22]  yeah,
[5350.24 --> 5351.50]  we tried that dumb.
[5352.26 --> 5353.00]  Nice try.
[5354.86 --> 5358.02]  How can I hear from the nicest way since I'm the guest?
[5358.18 --> 5360.14]  He literally said they started with it.
[5360.20 --> 5362.68]  Like he's basically saying that prime's idea was good.
[5362.74 --> 5363.94]  And it was the same idea as them.
[5364.02 --> 5364.80]  And T just like,
[5365.12 --> 5365.44]  well,
[5365.44 --> 5366.72]  that means prime's an idiot.
[5367.16 --> 5367.90]  All right.
[5368.04 --> 5369.62]  I guess he doesn't know anything.
[5369.62 --> 5371.78]  I'm collecting L's right now.
[5371.78 --> 5372.00]  Yeah.
[5372.42 --> 5374.06]  How did you get there from that?
[5374.06 --> 5375.78]  He said they started with it.
[5375.86 --> 5377.56]  Like it was their idea too.
[5378.14 --> 5378.30]  Casey,
[5378.30 --> 5378.86]  you have a great point.
[5378.94 --> 5379.62]  You're very smart.
[5381.36 --> 5382.00]  Shut up,
[5382.10 --> 5382.34]  TJ.
[5383.48 --> 5386.14]  TJ just does not want these L's to flow down from you.
[5386.18 --> 5386.68]  He can't,
[5386.68 --> 5388.46]  he can't handle you having to win prime.
[5388.56 --> 5390.30]  He can't handle a W in the,
[5390.30 --> 5391.04]  in the prime corner.
[5391.04 --> 5392.26]  I'm literally wearing an,
[5392.32 --> 5393.62]  I love TJ t-shirt.
[5393.68 --> 5394.34]  Oh my God.
[5395.70 --> 5396.96]  Just to like help,
[5396.96 --> 5398.46]  like bolster his confidence.
[5398.46 --> 5399.90]  And he's still thunking on me.
[5402.06 --> 5402.50]  True.
[5402.50 --> 5403.10]  Um,
[5404.06 --> 5404.28]  yeah.
[5404.28 --> 5405.04]  So we,
[5405.08 --> 5405.94]  we did start with that.
[5406.00 --> 5408.02]  We did push an extra frame onto the stack,
[5408.02 --> 5409.30]  but we just,
[5409.70 --> 5411.00]  instead of moving to nine one one,
[5411.10 --> 5415.14]  we just allocated a code page where there was an int three and then move and
[5415.14 --> 5415.72]  then put it in that.
[5416.14 --> 5417.80]  We changed the return address to that,
[5417.80 --> 5420.96]  but you can save that extra code page injection.
[5420.96 --> 5421.72]  Like it,
[5421.84 --> 5423.10]  it kind of gives you the same effect,
[5423.10 --> 5425.24]  but when you move to address nine one one,
[5425.24 --> 5429.10]  instead you don't have to inject that extra code page and treat in threes
[5429.10 --> 5429.46]  differently.
[5429.46 --> 5430.70]  Like it kind of just gives you,
[5431.16 --> 5433.20]  it's just a little bit simpler version of the same idea.
[5433.28 --> 5434.14]  Now you wouldn't,
[5434.32 --> 5436.50]  I don't think you'd want to push further onto the stack.
[5436.50 --> 5437.96]  Cause then you're kind of changing,
[5437.96 --> 5438.26]  like,
[5438.60 --> 5438.84]  you know,
[5438.84 --> 5439.64]  how deep is this?
[5439.78 --> 5440.72]  How deep is their stack?
[5440.78 --> 5441.78]  Are they close to a stack overflow?
[5441.86 --> 5443.16]  Are you doing things that are like,
[5444.18 --> 5444.46]  you know,
[5444.46 --> 5447.08]  you're kind of changing the way the program is running a little bit too much.
[5447.08 --> 5448.12]  I think in that case,
[5448.20 --> 5448.62]  um,
[5448.86 --> 5449.22]  I mean,
[5449.22 --> 5450.00]  you could do it though.
[5450.16 --> 5450.28]  You,
[5450.36 --> 5450.76]  well,
[5451.26 --> 5451.46]  yeah,
[5451.46 --> 5452.10]  you would probably,
[5452.18 --> 5453.76]  you would probably take that approach prime.
[5453.76 --> 5457.28]  If you actually had some things you needed to do,
[5457.28 --> 5458.92]  like if you had,
[5459.04 --> 5460.32]  if you had a really good,
[5460.32 --> 5460.74]  like,
[5460.92 --> 5463.84]  like a reason for injecting more code,
[5463.86 --> 5465.86]  that would probably be the right thing to do.
[5465.86 --> 5466.08]  Right.
[5466.34 --> 5466.66]  Uh,
[5466.96 --> 5467.20]  yeah.
[5467.20 --> 5467.86]  So this is,
[5467.86 --> 5469.08]  you can actually test this too.
[5471.02 --> 5471.60]  Let's go.
[5472.70 --> 5474.08]  This is actually how visual studio,
[5474.18 --> 5476.58]  like if you're in visual studio and you want to evaluate a function,
[5476.74 --> 5478.12]  it'll actually do that.
[5478.22 --> 5478.32]  So,
[5478.44 --> 5479.96]  so inside the watch window,
[5479.96 --> 5480.66]  if you,
[5480.90 --> 5481.52]  if you say like,
[5481.56 --> 5484.18]  I want to evaluate this function or in the immediates window,
[5484.24 --> 5486.16]  probably you want to evaluate a function,
[5486.16 --> 5486.94]  um,
[5486.98 --> 5487.92]  to evaluate it,
[5487.92 --> 5489.28]  but it's a function from the program.
[5489.28 --> 5492.80]  What it'll literally do is take your selected thread and it'll push a new
[5492.80 --> 5495.68]  call frame onto it and call whatever function you wanted to run.
[5495.90 --> 5497.54]  And you can actually test and verify this.
[5497.62 --> 5498.08]  You can put like,
[5498.62 --> 5498.90]  Oh,
[5498.98 --> 5500.50]  call sleep 1000 or whatever.
[5500.70 --> 5501.84]  And then if you pause the thread,
[5501.92 --> 5504.80]  it's in sleep on top of whatever code you were actually executing.
[5504.80 --> 5505.90]  So it doesn't inject a thread.
[5505.98 --> 5509.76]  It just uses whatever thread you had injected or you had selected.
[5509.96 --> 5510.66]  Um,
[5510.84 --> 5511.68]  so that actually does.
[5512.28 --> 5513.44]  You may not realize this.
[5513.54 --> 5513.82]  Um,
[5513.86 --> 5517.86]  but you just insulted me great gravely by saying that I have the same level of
[5517.86 --> 5519.14]  ideas as visual studio,
[5519.14 --> 5520.28]  which is a little.
[5520.54 --> 5523.06]  That's the meanest thing anyone said to him today.
[5525.20 --> 5526.42]  I'm so sorry.
[5526.88 --> 5528.00]  Same idea.
[5528.30 --> 5530.68]  I want to be clear.
[5530.80 --> 5532.20]  I would never,
[5532.28 --> 5533.42]  I would never.
[5533.74 --> 5534.18]  Okay.
[5534.18 --> 5538.14]  There's a line between friendly banter and proper insulting.
[5538.14 --> 5541.10]  And I would never cross that line for my good friend.
[5542.36 --> 5543.90]  I'm S I'm so sorry.
[5544.08 --> 5544.58]  I did not.
[5544.86 --> 5545.26]  Uh,
[5545.32 --> 5545.58]  yeah,
[5545.66 --> 5546.66]  I didn't mean to offend.
[5546.74 --> 5550.16]  Can we get the primogen subtitle changed to visual studio developer?
[5550.50 --> 5550.86]  Uh,
[5550.92 --> 5552.22]  like at the,
[5552.22 --> 5552.36]  like at the,
[5552.36 --> 5554.64]  he never shows his,
[5554.80 --> 5556.22]  even though I write good ones for him.
[5556.46 --> 5559.52]  I know that's because I actually use my real camera as opposed to because if I
[5559.52 --> 5559.82]  didn't,
[5559.88 --> 5563.12]  I'd actually get the leggy version of myself talking.
[5563.32 --> 5564.76]  So I have to use my real camera.
[5565.64 --> 5566.16]  All right.
[5566.24 --> 5567.58]  So debuggers,
[5567.68 --> 5568.06]  everyone,
[5568.06 --> 5569.10]  they're awesome.
[5569.10 --> 5571.02]  If they're good and they're useless,
[5571.02 --> 5572.40]  if they're not right,
[5572.44 --> 5573.02]  that's what,
[5573.14 --> 5576.14]  that's the TLDR for this stream is like,
[5576.14 --> 5577.48]  if a debugger is awesome,
[5577.66 --> 5578.64]  you should use it.
[5578.64 --> 5579.76]  Cause it saves you a lot of time.
[5579.76 --> 5580.54]  And if it's not,
[5580.56 --> 5581.58]  it's just a waste of time.
[5581.58 --> 5584.68]  And you can keep doing your print def debugging because it would be just as good.
[5585.10 --> 5585.46]  There you go.
[5585.46 --> 5585.66]  Well,
[5585.66 --> 5586.64]  I actually do.
[5586.72 --> 5589.06]  There is something inside of me that always comes to the same,
[5589.06 --> 5590.48]  like kind of conclusion,
[5590.48 --> 5593.06]  which is I've also not used enough,
[5593.06 --> 5594.20]  like Vim dapping.
[5594.36 --> 5596.72]  I haven't dapped hard enough with the boys yet.
[5596.72 --> 5598.24]  Is that when they,
[5598.24 --> 5599.28]  when they do the foot,
[5599.38 --> 5600.38]  the thing like this,
[5600.48 --> 5600.68]  Oh,
[5600.74 --> 5601.64]  Bill Gates does this,
[5601.72 --> 5603.18]  which is my favorite version of dapping.
[5603.32 --> 5605.68]  But when that,
[5605.80 --> 5616.72]  sometimes I think maybe my speed at a debugger is also skill issues that maybe I need to actually invest more into learning the dap side of things and the navigation being fast with it.
[5616.84 --> 5619.80]  But I also don't run into that issues very often that it's like,
[5620.60 --> 5622.30]  so it's like,
[5622.34 --> 5623.68]  it's been this kind of a difficult thing,
[5623.74 --> 5624.68]  but I need to give pride.
[5624.84 --> 5625.08]  Pride,
[5625.18 --> 5625.40]  by the way,
[5625.42 --> 5626.70]  is the Elixir version.
[5626.96 --> 5628.24]  Of some level of debugging.
[5628.38 --> 5629.42]  So I'd like to pry it up and,
[5629.42 --> 5632.98]  and drop that at printf debugging after this.
[5633.02 --> 5634.80]  Cause you guys make the bugger seem so like this,
[5634.88 --> 5636.48]  like exotic place that I got to go,
[5636.62 --> 5639.50]  but I also don't do game development or C plus plus or any of those things.
[5639.50 --> 5640.52]  Why don't we do it when you,
[5640.68 --> 5643.38]  next time you're going to be doing a project in a compiled language,
[5643.38 --> 5644.36]  like whenever that,
[5644.42 --> 5645.46]  whenever that next happens,
[5645.46 --> 5645.80]  right?
[5645.98 --> 5647.48]  We should do a stream where we're like,
[5647.52 --> 5648.52]  we'll do some debugging.
[5648.52 --> 5651.10]  Like we'll show you what we normally do is you can just see like,
[5651.24 --> 5651.84]  here's how we do it.
[5651.84 --> 5652.56]  Let's do a good seat.
[5652.70 --> 5653.42]  Let's do like,
[5653.46 --> 5655.68]  I wouldn't do the devil's language C plus plus.
[5655.68 --> 5656.86]  Let's do the Lord's language C.
[5657.20 --> 5657.38]  Okay.
[5657.62 --> 5657.98]  Odin.
[5658.10 --> 5658.26]  Yeah.
[5658.68 --> 5658.84]  Yeah.
[5658.92 --> 5660.00]  Odin could be a great one.
[5660.08 --> 5660.72]  Odin's like,
[5661.72 --> 5665.00]  is actually trying to make stuff good for rad debugging.
[5665.10 --> 5665.68]  So let's do that.
[5666.38 --> 5667.48]  Both of those will work.
[5668.16 --> 5668.54]  Right.
[5668.54 --> 5669.52]  I will say though,
[5669.70 --> 5670.40]  the thing,
[5670.94 --> 5673.78]  if you're not in like compiled language land like this,
[5673.88 --> 5675.28]  when your language has a REPL,
[5675.32 --> 5678.56]  you can get some of the experience from true.
[5678.66 --> 5681.00]  Like when you're running Elixir and you're running,
[5681.08 --> 5682.68]  like you can run stuff from the REPL,
[5682.74 --> 5683.62]  you can send messages,
[5683.86 --> 5685.22]  you can go inspect data,
[5685.24 --> 5685.76]  you can do all that.
[5685.76 --> 5686.64]  So there is like,
[5687.72 --> 5687.96]  you know,
[5688.02 --> 5689.36]  there are some other options too,
[5689.44 --> 5690.86]  that you can explore even in,
[5690.92 --> 5692.20]  in some of these other languages.
[5692.82 --> 5693.18]  Well,
[5693.20 --> 5695.46]  and some VM languages have full debuggers,
[5695.62 --> 5695.80]  right?
[5695.80 --> 5696.14]  I mean,
[5696.32 --> 5697.06]  Java does,
[5697.28 --> 5697.54]  right?
[5697.78 --> 5699.34]  Even when it's running in a VM,
[5699.48 --> 5700.70]  you can do full debugging in Java.
[5700.90 --> 5701.02]  Yeah.
[5701.02 --> 5703.36]  I think Python has Pube G or whatever it's called.
[5703.66 --> 5704.34]  That's also like that.
[5704.34 --> 5706.70]  Pube G is the name of the debugger.
[5707.06 --> 5707.88]  In my head,
[5707.92 --> 5708.78]  I call it Pube G,
[5709.14 --> 5710.82]  but I actually can't remember what it is,
[5710.86 --> 5712.08]  but it's like P-U-D-B.
[5712.36 --> 5713.76]  It's pronounced Pub G.
[5713.88 --> 5714.50]  It's a video game.
[5714.56 --> 5714.80]  Yeah.
[5715.16 --> 5715.32]  Yeah.
[5715.46 --> 5715.78]  Okay.
[5716.18 --> 5716.90]  It's completely,
[5717.24 --> 5719.86]  unless you're playing something completely different than everyone else has been playing.
[5720.02 --> 5720.16]  Okay.
[5721.12 --> 5722.06]  All I know is that.
[5722.06 --> 5722.58]  Pube G Underground?
[5722.76 --> 5723.16]  Crazy.
[5723.52 --> 5723.74]  Yeah.
[5723.74 --> 5726.00]  All I know is when I saw it,
[5726.12 --> 5729.00]  I had such severe dyslexia that all I saw was Pub G,
[5729.44 --> 5731.14]  and so now I can't unsee it,
[5731.60 --> 5732.30]  and so I'm just like,
[5732.34 --> 5732.46]  ah,
[5732.48 --> 5732.96]  it's Pube G.
[5733.48 --> 5734.94]  That's what the Python one is.
[5734.94 --> 5735.56]  That's all I know.
[5736.42 --> 5737.38]  For some reason,
[5737.54 --> 5740.68]  I played PlayerUnknown's Battlegrounds for many hours
[5740.68 --> 5742.84]  and somehow never thought Pube G.
[5744.42 --> 5745.86]  And now I will.
[5746.38 --> 5746.78]  Crazy.
[5747.22 --> 5747.66]  Crazy.
[5747.66 --> 5751.06]  I'm pretty sure if you were on the stand-up when you were playing it,
[5751.06 --> 5751.34]  I would have.
[5751.34 --> 5752.04]  That same time frame,
[5752.14 --> 5753.38]  it would be top of mind.
[5753.66 --> 5753.88]  You know?
[5754.10 --> 5755.10]  We should actually do,
[5755.18 --> 5756.50]  because I've never played Pube G,
[5756.88 --> 5758.22]  we should do like a,
[5758.52 --> 5760.76]  Casey introduces us to Pube G.
[5761.44 --> 5762.14]  Call out that.
[5762.14 --> 5762.56]  Oh, God.
[5762.62 --> 5762.82]  I mean,
[5762.88 --> 5764.48]  it has been so long since I've played it.
[5764.72 --> 5765.58]  I would be the worst.
[5765.66 --> 5766.90]  We'd just all get shot immediately,
[5767.00 --> 5767.78]  would be what would happen.
[5767.86 --> 5768.16]  And I'd be like,
[5768.20 --> 5768.40]  well,
[5768.48 --> 5769.84]  I didn't get a chance to show you anything,
[5770.04 --> 5770.58]  but sorry,
[5770.68 --> 5771.00]  guys.
[5771.76 --> 5772.40]  But we can try.
[5772.62 --> 5772.74]  I like that.
[5772.82 --> 5772.96]  Sure.
[5773.18 --> 5773.64]  I'd try.
[5774.12 --> 5774.44]  Next,
[5774.44 --> 5774.98]  stand-up.
[5775.08 --> 5776.10]  Let's just play video games for now.
[5776.10 --> 5776.88]  We're just playing PUBG.
[5776.88 --> 5779.64]  That's actually much closer to a,
[5779.64 --> 5779.92]  you know,
[5780.00 --> 5781.46]  a FANG level startup anyways.
[5781.58 --> 5782.52]  Friday stand-up.
[5782.60 --> 5783.58]  Time for some team building.
[5783.74 --> 5784.76]  Let's pick a video game.
[5785.10 --> 5785.48]  All right,
[5785.50 --> 5785.58]  folks.
[5785.58 --> 5785.68]  Dude,
[5785.68 --> 5787.60]  team building stream would be so funny.
[5788.32 --> 5788.52]  Okay,
[5788.58 --> 5788.74]  well,
[5788.74 --> 5789.78]  we'll talk about that offline.
[5790.06 --> 5790.46]  I gotta go.
[5790.54 --> 5791.34]  I got another podcast.
[5791.98 --> 5792.22]  Oh,
[5792.30 --> 5792.52]  sorry.
[5792.60 --> 5793.04]  Our bad.
[5793.44 --> 5794.18]  Podcast TJ.
[5795.26 --> 5795.70]  Sorry.
[5796.24 --> 5796.48]  Hey,
[5796.48 --> 5796.90]  Ryan,
[5796.90 --> 5797.40]  good ideas.
[5797.50 --> 5798.36]  I want it to be clear.
[5798.96 --> 5799.14]  Yeah.
[5799.32 --> 5800.60]  I appreciate that.
[5800.68 --> 5800.78]  Hey,
[5801.02 --> 5801.24]  Ryan,
[5801.30 --> 5802.44]  where can everybody find you at?
[5803.80 --> 5804.50]  You can,
[5804.78 --> 5807.84]  I'm on Twitter at,
[5808.06 --> 5808.56]  or X.
[5809.12 --> 5810.32]  I'm linking it right now.
[5811.32 --> 5812.36]  It's Ryan J.
[5812.50 --> 5812.82]  Fleury,
[5812.94 --> 5814.44]  F-L-E-U-R-Y.
[5815.04 --> 5818.46]  And then I've got a substack that I,
[5818.64 --> 5820.68]  I have a couple of blog posts on,
[5820.72 --> 5822.24]  on like debuggers and how they work.
[5822.26 --> 5823.42]  And then I've got a bunch of other stuff.
[5823.42 --> 5824.10]  Uh,
[5824.10 --> 5825.44]  that's R Fleury,
[5825.52 --> 5827.26]  F-L-E-U-R-Y.com.
[5827.80 --> 5828.20]  Um,
[5828.56 --> 5831.22]  and then I think that's basically everything.
[5831.30 --> 5832.54]  Where can they find the rad debugger?
[5833.30 --> 5833.92]  Oh yeah.
[5834.48 --> 5834.74]  Uh,
[5834.74 --> 5837.04]  you can go to github.com slash.
[5837.20 --> 5837.32]  It's,
[5837.38 --> 5838.44]  it's kind of a complicated URL,
[5838.44 --> 5839.06]  uh,
[5839.06 --> 5840.70]  but it's github.com slash.
[5840.78 --> 5840.96]  Actually,
[5840.96 --> 5841.78]  can I put it in the chat?
[5842.10 --> 5842.12]  Yeah,
[5842.12 --> 5842.24]  yeah,
[5842.24 --> 5842.34]  yeah.
[5842.44 --> 5843.68]  I literally,
[5843.78 --> 5848.02]  you can also just search for rad space debugger or epic space rad debugger.
[5848.16 --> 5848.90]  I usually in Google,
[5848.96 --> 5849.52]  it will come up.
[5850.00 --> 5850.40]  Yep.
[5850.50 --> 5850.70]  Yeah.
[5850.74 --> 5851.78]  I guess I don't have,
[5851.78 --> 5852.14]  Oh,
[5852.24 --> 5852.92]  studio chat.
[5853.00 --> 5853.40]  Here we go.
[5853.84 --> 5854.52]  I just see.
[5854.56 --> 5854.74]  Yep.
[5854.74 --> 5855.46]  Someone already linked it.
[5855.52 --> 5856.64]  It's rad games extension.
[5856.84 --> 5857.44]  Rad debugger.
[5857.46 --> 5858.54]  Your fans are in the chat.
[5858.84 --> 5859.00]  Yeah.
[5859.06 --> 5859.62]  You got a lot of fans.
[5859.90 --> 5861.56]  Is a return address from your sub stack?
[5861.68 --> 5862.28]  Nine one one.
[5862.84 --> 5863.74]  Ha ha ha.
[5865.50 --> 5865.90]  Uh,
[5865.90 --> 5866.14]  no,
[5866.18 --> 5867.04]  but it maybe should be.
[5867.10 --> 5867.28]  Yeah.
[5867.28 --> 5867.48]  Yeah.
[5867.48 --> 5868.20]  That's a good idea.
[5870.42 --> 5870.82]  Prime.
[5871.38 --> 5872.02]  You did it.
[5872.34 --> 5873.02]  I got one.
[5873.32 --> 5873.70]  He did it.
[5873.70 --> 5874.52]  He said it's a good idea.
[5874.80 --> 5875.34]  I got one.
[5877.14 --> 5878.76]  Take that universe.
[5879.06 --> 5879.42]  All right,
[5879.44 --> 5879.80]  everybody.
[5879.80 --> 5881.38]  Thank you very much for joining us.
[5881.50 --> 5881.78]  Casey,
[5881.90 --> 5883.20]  computer enhance.com.
[5883.20 --> 5885.02]  If you want to actually learn how computers work,
[5885.48 --> 5885.84]  TJ,
[5886.30 --> 5887.54]  he streams by the way.
[5887.54 --> 5889.38]  And the name is the primogen.
[5889.50 --> 5890.44]  Thank you for joining us.
[5891.24 --> 5891.40]  Thank you.
[5891.52 --> 5893.14]  That was a great outro.
[5893.52 --> 5894.02]  I know.
[5894.14 --> 5895.36]  That's pretty damn good.
[5895.62 --> 5895.96]  Thank you.
[5895.96 --> 5896.26]  Thank you.
[5896.28 --> 5896.58]  Thank you.
[5896.58 --> 5896.82]  Thank you.
[5896.86 --> 5897.74]  Thank you.
[5897.74 --> 5902.74]  Vibe called and errors on my screen
[5902.74 --> 5907.58]  Terminal coffee and hand
[5907.58 --> 5910.52]  Living the dream
