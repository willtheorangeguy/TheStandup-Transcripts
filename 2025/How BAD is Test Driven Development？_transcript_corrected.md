[0.00 → 2.62] So today's stand-up, we are going to talk about TDD.
[3.12 → 5.12] Okay, we're not going to have some topical topic.
[5.38 → 7.56] We're going to go after the big stuff, okay?
[8.50 → 12.04] TDD, is it good? Is it bad? Do you use it?
[12.90 → 16.16] TJ's just smiling, looking like an absolute champ in that freeze-frame.
[16.46 → 21.02] Dude, somehow TJ's the only human I know that gets freeze-framed, and it's a good picture.
[21.68 → 21.92] Yep.
[22.68 → 24.36] Yeah, look at TJ. Look at that Labrador.
[24.36 → 25.90] I can't handle this right now.
[26.90 → 28.98] I cannot handle this right now.
[30.76 → 35.30] All right, Casey, you probably have the strongest opinion, potentially, out of all of us.
[36.84 → 40.10] Okay. I doubt that, but okay.
[40.58 → 43.02] All right, because I also have a strong opinion, but I'm willing to...
[43.02 → 43.62] It's probably you, then.
[44.00 → 46.72] Yeah, I think, Prime, you got to lead off the strong opinions here.
[46.90 → 51.08] I'll lead off with the strong one, which is, so I recently just tried another round of TDD.
[51.32 → 56.72] Prime, Prime, you have to say, hey, everyone, welcome to the stand-up.
[57.16 → 58.92] We got a great show for you tonight.
[58.92 → 61.04] I'm your host, the Prime-A-Gen.
[61.30 → 63.44] With me, as always, are TJ.
[64.06 → 65.70] Hello, Trash.
[65.96 → 66.98] Hey, everyone.
[67.26 → 68.06] See me, Satori.
[68.40 → 69.58] Great to be here, Prime.
[69.68 → 70.08] Thanks.
[70.82 → 72.10] Today's topic is...
[72.10 → 74.48] Have you ever heard a podcast before?
[74.48 → 77.84] Thanks, everybody, for joining.
[77.94 → 82.20] You're watching the hottest podcast on the greatest software engineering topics, the stand-up.
[82.28 → 86.34] Today, we have with us Teen, who's in the basement fixing something.
[87.34 → 87.98] I know.
[87.98 → 90.96] Is that a Home Depot ad?
[91.30 → 91.90] Look at him.
[91.90 → 93.58] He's showing us his router.
[94.70 → 99.66] We have with us Trash Dev, Bromate winning a judo competition, still living off that high.
[100.04 → 103.28] And Mortar, the actual good programmer among us.
[103.74 → 104.54] Oh, all right.
[104.62 → 105.72] I got a lot to live up to.
[106.14 → 106.72] Yeah, you got...
[106.72 → 107.32] Don't worry.
[107.32 → 109.10] It's not hard to live up to, at least in this crowd.
[109.44 → 110.84] I'll kind of start us off on this one.
[110.90 → 113.12] So we've been developing a game called The Towers of Moratoria.
[113.40 → 117.66] We came up with the name from an AI, and AI generated that name for us.
[118.00 → 122.74] And effectively, I decided at one point, I have this kind of really black box experience.
[123.20 → 126.54] I have a deck of cards that I need to be able to draw cards out.
[126.76 → 130.74] When they're played, they either need to go to the discard pile or the exhaust pile.
[131.16 → 134.40] When there's no more cards in my hand or not enough to be able to draw cards,
[134.56 → 137.08] I need to be able to take all the discard cards.
[137.08 → 139.32] Dude, Teen is just flexing on his touching grass right now.
[139.32 → 146.20] Put all the discard cards, shuffle everything up, and then draw new cards back out,
[146.52 → 148.16] replenish the draw pile, right?
[148.22 → 151.70] This sounds like a TDD pinnacle problem.
[152.12 → 153.10] There are black boxes.
[153.24 → 154.32] There are a few operations.
[154.54 → 155.50] I'm going to be able to do this.
[155.58 → 157.46] And so I just did this like a week and a half ago on stream.
[157.68 → 158.34] It was amazing.
[159.24 → 162.56] I did the whole thing, designed the entire API in the test,
[162.90 → 165.36] then set up all the tests, set up it all to fail.
[165.64 → 167.58] Then it did work, or then it failed.
[167.58 → 170.36] Then I made it work, then it worked, and it was great, and everything was perfect.
[170.44 → 171.30] And I was like, there we go.
[171.40 → 172.02] We just did it.
[172.10 → 174.10] I just TDD'd, and it was a good experience.
[174.56 → 178.34] So then I took what I made, and I went to integrate it into the game,
[178.46 → 181.72] and realized I made an interface that's perfect for testing
[181.72 → 186.22] and not actually good for the actual thing I was making, and I had to redo it.
[186.56 → 190.62] And so it always, you know, that's kind of been a lot of my experience with TDD,
[190.62 → 194.76] is that either the thing is simple enough and a super black box enough
[194.76 → 199.26] that I can make it, and both the testing interface and the usage interface is the same,
[199.48 → 202.32] or I create an interface that's really great for testing,
[202.60 → 205.50] and it's actually not that great for the practical use case.
[205.90 → 209.20] And I know people talk about how it's a great way to develop your, you know,
[209.44 → 211.18] your architecture and all this kind of stuff.
[211.32 → 213.02] I've just yet to really buy it.
[213.02 → 214.92] But I will say the thing that I do like doing
[214.92 → 219.24] is on problems that are hard to develop and have many moving constraints,
[219.60 → 224.00] I do like to co-create tests with it, meaning that I come up with an idea.
[224.28 → 225.44] How do I want to use it?
[225.60 → 226.64] I program it out.
[226.92 → 229.60] Then I go create a test, which is backwards from TDD.
[230.12 → 231.70] Go, okay, this is what I want to see.
[231.80 → 233.02] Am I even correct on this?
[233.08 → 237.00] Can I get a fast iteration loop being like, no, no, no, yes.
[237.14 → 237.76] Okay, got it.
[237.94 → 239.34] Next thing, I want to make sure it does this.
[239.34 → 240.22] No, no, no, yes.
[240.32 → 240.84] Okay, got it.
[240.84 → 246.10] And so I do like the fast iteration cycle of getting tests in early,
[246.24 → 249.78] but few problems feel like I can actually have that.
[249.86 → 252.54] And I feel like this, all things need to be tested immediately
[252.54 → 253.72] and need to be written first.
[253.90 → 255.76] You just write dumb interfaces.
[256.40 → 258.16] Everything becomes inversion of control.
[258.66 → 259.66] Everything's an interface.
[259.90 → 262.46] And you just have this abstract mess at the end of it
[262.46 → 266.56] because testing was the requirement, not, hey, use it when it's good.
[266.56 → 269.12] So that's my TDD experience.
[269.12 → 271.18] And I feel fairly strong about that.
[271.24 → 273.62] And if you say TDD is good, I feel like I'm going to jump kick you.
[276.66 → 279.38] I can respond to that, or Casey, if you have strong feelings.
[279.76 → 282.54] No, I think trash, let's go to trash take first.
[282.98 → 284.30] Yeah, no blockers on my end.
[289.26 → 292.24] First, you couldn't like to deter me from doing any task
[292.24 → 295.50] than to tell me I need to like to start off by writing tests first off.
[295.50 → 299.30] Second, I kind of had a very similar experience recently building a seal.
[299.30 → 300.52] Hold on, can you rewind for a second?
[300.74 → 302.72] What did you just say for your first point?
[303.42 → 306.78] I said you couldn't deter me from doing work
[306.78 → 309.56] if you let off with me having to write tests first.
[310.68 → 312.02] I don't even know what that means.
[312.40 → 314.10] You mean you couldn't deter me anymore?
[314.34 → 315.98] Like that's the most deterring thing?
[316.44 → 316.76] Or...
[316.76 → 318.74] Oh, man, am I stupid?
[318.74 → 319.54] You are.
[319.68 → 322.44] Can you try using a different word to describe what you feel?
[322.94 → 324.50] Okay, let's reword this.
[325.10 → 326.34] Flip, please take this out.
[326.60 → 327.24] Flip, leave it in.
[327.24 → 328.64] I don't like test-driven development.
[328.88 → 334.42] However, however, I just built something recently at work
[334.42 → 336.66] which was very kind of similar to what Prime was saying.
[337.78 → 340.22] I ended up doing a little bit of test-driven development.
[342.74 → 343.38] But...
[343.38 → 344.94] You wouldn't notice this,
[344.98 → 347.52] but I'm actually really kind of passionate about testing.
[347.52 → 349.52] So I'm going to kind of like...
[350.18 → 354.50] When I test, I would say 2% of the time
[354.50 → 356.72] I actually ended up with test-driven development.
[357.08 → 359.00] And the rest is usually post-implementation
[359.00 → 364.40] because one, requirements and all these things change afterwards, right?
[364.88 → 366.70] So it's like why write tests for things
[366.70 → 368.18] that are potentially going to change
[368.18 → 369.60] and you don't really know what's going to happen.
[369.82 → 372.78] But I do write tests for very granular things
[372.78 → 374.32] that I think are going to be used all the time.
[374.40 → 376.76] So for instance, like if I wrote a parser
[376.76 → 377.82] for like my CLI,
[378.40 → 380.48] the parser is going to be reused by multiple commands,
[380.58 → 381.92] probably never going to change.
[382.34 → 383.92] So I typically will write that.
[384.02 → 385.34] And I'll also write tests
[385.34 → 387.26] for things that take multiple steps to test.
[387.96 → 390.26] So like, you know, people argue for end-to-end tests
[390.26 → 391.66] because you test just like a user.
[391.82 → 393.14] So that's kind of how I like to develop.
[393.22 → 395.52] I like to use it like I would use it for anybody else.
[395.78 → 397.40] But if I got to do like three steps
[397.40 → 398.68] to get to the point I want to test,
[399.06 → 400.16] I'm like, all right, screw this.
[400.16 → 401.80] I'm just going to write a test specifically
[401.80 → 403.42] for this like instance.
[403.78 → 406.06] And then I save time that way.
[406.42 → 408.18] So that's usually the time I arrive
[408.18 → 409.16] at test-driven development
[409.16 → 410.74] is specifically in those scenarios.
[411.30 → 413.44] Otherwise, it's purely just like, you know,
[414.04 → 414.96] what do you call it?
[415.00 → 416.42] Integration testing and stuff like that.
[416.42 → 418.76] Because you end up with stuff like Prime said,
[418.88 → 419.82] like when you write tests,
[419.88 → 421.18] you write everything so granular
[421.18 → 422.96] and everything works so modular
[422.96 → 424.28] that you just don't even know
[424.28 → 426.40] what it's like when you actually put them together.
[426.54 → 426.98] So that's why,
[427.12 → 428.66] that's kind of like the way I approach things.
[428.66 → 429.84] That being said,
[429.98 → 432.86] like people that kind of like live and die
[432.86 → 433.80] by test-driven development,
[434.02 → 435.56] I don't get it.
[436.80 → 439.62] But I was hoping someone would be pro-TDD in this group
[439.62 → 440.78] so I could argue with them.
[442.20 → 443.58] That's all I got for right now.
[445.28 → 448.86] I'm pretty much right there with trash on this one.
[449.26 → 452.36] My feeling on TDD is pretty much the same
[452.36 → 454.42] as my feeling on OOP, right?
[454.64 → 458.46] The problem is not if you end up with an object
[458.46 → 461.94] or something that looks like an object in your code in OOP,
[462.38 → 463.00] that's fine.
[463.28 → 465.52] The problem is the object-oriented part.
[465.66 → 467.22] The like thinking in terms of that
[467.22 → 468.30] wastes a lot of your time
[468.30 → 469.88] and leads you to bad architecture, I think.
[470.60 → 471.66] TDD is the same way.
[471.82 → 473.50] I think testing is very good,
[473.80 → 475.40] but test-driven development,
[475.58 → 477.50] meaning forcing the programmer to think
[477.50 → 479.24] in terms of tests during development,
[479.36 → 480.90] like that is what your primary thing is
[480.90 → 481.90] is I'm making tests,
[482.10 → 483.44] to drive the development,
[483.58 → 484.34] the TD part,
[484.64 → 485.88] that's actually the problem.
[485.88 → 488.26] I think the reason for that's pretty straightforward
[488.26 → 490.38] and it's kind of weird
[490.38 → 492.42] because usually the people who advocate for TDD
[492.42 → 494.38] are the same people who would poo-poo
[494.38 → 496.72] any similar suggestion,
[496.98 → 498.40] like any suggestion that like,
[498.48 → 500.70] oh, we should measure performance during development.
[500.82 → 501.88] They'll be like, that's ridiculous.
[502.00 → 503.06] You're wasting so much program time.
[503.10 → 505.18] We're like, what about the 8,000 tests
[505.18 → 506.52] that no one ever needed
[506.52 → 508.70] because we ended up deleting that system anyway?
[508.78 → 509.82] And they're like, well, you know,
[510.04 → 511.20] test-driven development is very good.
[511.20 → 513.88] So I think like the problem
[513.88 → 515.44] with all of those sorts of things,
[515.58 → 516.22] any of them,
[516.98 → 519.02] is just putting emphasis on something
[519.02 → 521.96] instead of talking about it like what it really is,
[522.02 → 523.32] which is a trade-off.
[523.86 → 525.86] If you're spending time making tests
[525.86 → 528.94] or you're orienting things towards making tests,
[529.06 → 531.08] that is necessarily programming time
[531.08 → 533.00] that isn't being spent doing something else.
[533.10 → 534.54] Like programming is zero-sum.
[534.72 → 536.36] If you spend time doing one thing,
[536.42 → 538.30] you're not spending time doing another thing.
[538.30 → 539.78] And so, for example,
[539.94 → 541.54] if you end up spending a lot of your time
[541.54 → 543.74] making the interface revolve around tests,
[544.22 → 545.88] you weren't spending a lot of your time
[545.88 → 548.28] making the interface revolve around actual use cases
[548.28 → 549.22] because actual use cases
[549.22 → 550.46] don't usually look like tests.
[551.04 → 552.90] Therefore, sometimes you get the exact situation
[552.90 → 554.04] that Prime was talking about
[554.04 → 555.58] where you do test-driven development
[555.58 → 557.32] and you end up with a completely unusable mess,
[557.42 → 559.62] which is actually very common in my experience, right?
[560.28 → 561.34] I wouldn't call it a mess.
[561.46 → 562.42] You know, I write pretty good.
[562.52 → 564.04] I mean, it was like pretty easy.
[564.22 → 564.56] I just want to say.
[564.56 → 565.14] No, the API.
[565.48 → 566.72] The API is a mess.
[566.72 → 567.96] Not the code.
[568.30 → 568.50] Right?
[568.58 → 569.82] Like the code has been tested
[569.82 → 570.94] and it probably works.
[571.08 → 572.54] But the API is a mess, right?
[572.60 → 574.44] I mean, that's what happens
[574.44 → 577.02] because it wasn't designed specifically
[577.02 → 580.08] for the kinds of use cases it was meant to tackle.
[580.44 → 581.68] And so you end up with that problem.
[581.72 → 583.68] And again, it was shifting the developer's focus
[583.68 → 585.56] was all it took to make that happen.
[585.88 → 588.12] Good APIs are hard to make in the first place, right?
[588.28 → 590.72] So if you're adding more complexity
[590.72 → 591.80] to the programmer's workflow
[591.80 → 593.14] when they're trying to make an API
[593.14 → 595.88] that's good for the actual use case,
[596.22 → 597.88] you're just going to get a worse result.
[598.30 → 599.00] Again, zero-sum.
[599.38 → 601.86] So what I would say is like testing is better
[601.86 → 605.08] something that you do as the thing takes shape.
[605.08 → 605.86] When you're like, okay,
[605.86 → 609.02] we now have figured out like how this system works properly.
[609.02 → 610.34] We're really happy with it.
[610.58 → 611.96] The API is working nicely.
[612.22 → 613.44] We check the performance
[613.44 → 615.12] and we think we've got like reasonable,
[615.48 → 616.78] we've got a reasonable path
[616.78 → 618.54] towards having this perform really well.
[619.08 → 620.76] Now let's start seeing what are the
[620.90 → 621.82] what is the overlay?
[621.96 → 623.58] Like what are the parts we can now start
[623.58 → 625.94] to add some little substrate to,
[626.46 → 629.10] to test that we think are going to have bugs
[629.10 → 630.36] that will be hard to find?
[630.62 → 631.74] Because that's usually the way I look at it.
[631.74 → 633.40] Like what are the parts of this system
[633.40 → 635.96] whose bugs will be either very hard to find
[635.96 → 636.98] or really catastrophic?
[637.24 → 638.48] Like they'll cost us a lot of money
[638.48 → 640.90] or they'll crash the user's computer or whatever, right?
[641.74 → 643.90] And then you put the tests for that, right?
[644.26 → 645.92] And that's how I've always approached it.
[645.94 → 647.28] And I think that works pretty well.
[647.28 → 650.12] And you do want to do that step,
[650.32 → 652.84] but I don't think you want test driven development.
[653.02 → 654.66] It just seems like a terrible idea.
[654.92 → 657.88] And to be honest, when I use software
[657.88 → 660.62] that comes from people who are like TDD,
[660.86 → 662.32] this organization's TDD, whatever,
[662.56 → 664.74] it's full of bugs all the time, right?
[664.78 → 667.56] Like I'm not getting these pristine software things.
[667.70 → 669.74] I mean, I would imagine that the people at YouTube
[669.74 → 671.54] do a lot of testing and code reviews.
[671.96 → 674.38] And yet for the past eight years,
[674.56 → 676.92] the play button cannot properly represent
[676.92 → 678.28] whether something is playing or not.
[678.38 → 679.58] For eight years, right?
[679.68 → 681.80] Sometimes it's paused, and it has the play thing.
[681.86 → 683.80] And sometimes it's playing, and it has the play thing.
[684.32 → 685.52] And sometimes both of those times,
[685.56 → 686.32] it shows the pause thing.
[687.24 → 691.30] It's just, it doesn't seem like the testing is working, guys.
[691.50 → 693.30] So again, I'd say, you know,
[693.52 → 694.92] I think you have to kind of rethink
[694.92 → 696.70] how you're allocating that time.
[696.78 → 697.52] That's what I would say.
[698.50 → 699.80] Can we get TJ in here?
[699.94 → 702.46] Can Playboy TJ get on this one?
[702.58 → 702.96] Can we?
[703.26 → 704.74] Am I coming in loud and clear?
[705.74 → 706.10] Yeah.
[706.10 → 707.38] Your voice sounds good.
[707.68 → 708.54] Your voice sounds good.
[708.54 → 709.26] You're looking good.
[709.26 → 710.24] The grass looks good.
[711.04 → 711.56] Thank you.
[711.62 → 711.94] Thank you.
[712.28 → 714.68] So I would say, I'm, I'm, uh,
[714.68 → 717.48] I think I agree mostly with what everybody is saying.
[717.48 → 720.10] Although I would say for a few kinds of problems,
[720.10 → 724.30] the problem is I, I, I think people,
[724.30 → 727.24] when you say TDD, they just mean 10,000 different things.
[727.24 → 728.98] So this is like one of the problems, right?
[728.98 → 731.40] There's like people who are like TDD is only
[731.40 → 734.30] if you do red green cycle before you write the code,
[734.30 → 735.86] you have to write the tests and like,
[735.90 → 737.94] you can't write any code until you've written a failing test
[737.94 → 741.34] and blah, blah, blah, which like I get, uh,
[741.40 → 743.72] that maybe they're the people who invented the word
[743.72 → 745.16] so they can define it that way.
[745.62 → 748.18] Uh, but like, I find that not,
[748.30 → 749.82] not very useful for some stuff,
[749.82 → 754.58] but, uh, there are like testing or like projects
[754.58 → 757.54] where I think I test like basically everything.
[757.54 → 760.54] And there are just ways that you can do it
[760.54 → 762.68] that are like more effective versus less effective.
[762.68 → 766.18] Like my favourite kind of testing is if you can find a way
[766.18 → 769.02] to do like snapshot or like golden testing, whatever,
[769.02 → 770.82] you know, people have different names for it,
[770.82 → 773.92] but where you can basically just write a test
[773.92 → 776.78] and then say, assert that the output is the same
[776.78 → 777.64] as it used to be.
[778.00 → 778.36] Right.
[778.60 → 780.24] Uh, like, so in you,
[780.30 → 782.02] I usually I've seen those called snapshot tests
[782.02 → 783.00] or expect tests.
[783.00 → 785.90] I find that those are like super often.
[786.46 → 786.90] Yeah.
[786.94 → 787.06] Yeah.
[787.06 → 788.68] Or like people will use them in regression,
[788.68 → 790.68] but like the kinds that I've done it before,
[790.68 → 794.64] like, uh, maybe I'm building up a complex data structure
[794.64 → 797.90] to like to represent the state of like a bunch of users,
[797.90 → 800.04] or maybe it's the parse tree of something,
[800.04 → 801.72] or maybe it's the type system,
[801.82 → 803.14] like whatever it is.
[803.14 → 805.26] If you can find a way to represent that
[805.26 → 806.92] in like a human-readable way,
[807.00 → 809.58] usually just by like printing it in tests that I've done,
[809.96 → 812.50] you can just like to compare the diff
[812.50 → 815.04] between this one, and before you made the changes
[815.04 → 817.10] and they're, they should be fast.
[817.10 → 818.44] At least if they're not fast,
[818.44 → 819.50] then that's a separate problem.
[819.50 → 821.64] Like your tests have to be fast for people to run them.
[821.72 → 822.78] Otherwise they don't run them.
[823.38 → 827.00] Um, then, then those kinds of things tend to be,
[827.06 → 828.38] I find like very effective
[828.38 → 830.16] and give you a lot of confidence
[830.16 → 832.06] that you haven't like scuffed anything
[832.06 → 833.58] throughout the system with your changes.
[833.58 → 834.00] Right.
[834.00 → 835.00] Because you're sort of like
[835.00 → 837.44] asserting the entire state of something.
[837.68 → 838.88] And if something changes,
[838.88 → 839.92] it's really easy to update.
[839.92 → 840.70] Cause you just say,
[840.70 → 843.08] Oh, snapshot update this.
[843.52 → 843.64] Cool.
[843.94 → 844.18] Done.
[844.48 → 845.16] One second.
[845.26 → 846.34] All your tests are updated.
[846.60 → 848.26] You walk through them and change them.
[848.44 → 850.10] You get some other side benefits too.
[850.18 → 851.00] Like in code review,
[851.00 → 853.78] you literally see the diff of the snapshot
[853.78 → 855.34] and you can be like,
[855.68 → 857.00] um, that looks wrong.
[857.12 → 858.30] That used to say false.
[858.36 → 859.22] And now it says true.
[859.26 → 861.10] Those things that shouldn't have been flipped
[861.10 → 861.84] between those.
[862.38 → 864.50] So there are like certain problems
[864.50 → 868.68] where I've employed like nearly TDD
[868.68 → 870.44] in this snapshot style,
[870.44 → 872.46] in the sense that the snapshot always fails
[872.46 → 873.58] on the first time you run it.
[874.10 → 875.68] Cause there's nothing to expect.
[876.76 → 879.04] And then you accept that snapshot
[879.04 → 879.82] if it looks good
[879.82 → 881.04] or keep changing the code
[881.04 → 881.88] until it does look good.
[882.02 → 883.92] And then you like move on to the next thing.
[884.28 → 885.16] So, but that,
[885.26 → 886.58] but it's kind of like a unique case.
[886.58 → 888.52] Like I wouldn't want to snapshot test
[888.52 → 893.04] a like HTML page, right?
[893.06 → 893.72] It would just like,
[894.26 → 896.18] there's no way that they're reproducible.
[896.36 → 898.20] It feels like, uh, anyway.
[898.74 → 900.14] Uh, but like, so there's,
[900.24 → 902.14] there's, it's only for like certain subsets
[902.14 → 902.62] of problems,
[902.62 → 903.74] which have been more effective.
[903.74 → 904.42] Like for me,
[904.46 → 905.98] because I've made a lot of dev tools
[905.98 → 908.02] in my career and stuff like that.
[908.02 → 910.60] So you want to do like verify
[910.60 → 912.02] that all the references
[912.02 → 913.40] of something look like X, Y, Z.
[913.50 → 913.80] Okay.
[913.82 → 915.30] Very easy to do with snapshots.
[915.30 → 918.40] Um, that's,
[918.40 → 919.38] so that's kind of the main,
[919.62 → 920.68] the, the one thing
[920.68 → 921.96] that I wanted to throw out there
[921.96 → 923.36] is like that style of testing.
[923.36 → 924.52] I find really powerful
[924.52 → 925.72] and I've used it a lot
[925.72 → 926.54] like across projects
[926.54 → 927.98] you wouldn't really expect as well.
[928.82 → 931.12] I've always had the opposite experience
[931.12 → 932.10] with snapshot tests.
[932.48 → 933.94] I feel like it's okay.
[933.94 → 935.16] Maybe if like it's you
[935.16 → 936.08] and maybe some other people
[936.08 → 937.20] that actually know
[937.20 → 938.74] the expected output of a snapshot.
[939.10 → 941.60] My experience is it changes
[941.60 → 942.12] and they're like,
[942.16 → 943.76] Oh, let's just update it.
[943.76 → 945.38] And then the test passed again
[945.38 → 946.44] and then you're kind of just
[946.44 → 948.72] left with the snapshot
[948.72 → 949.36] and you're just like,
[949.40 → 949.66] all right.
[949.90 → 950.66] So it's to the point
[950.66 → 951.48] like where it's like,
[951.50 → 951.68] all right,
[951.68 → 953.08] let's just get rid of them
[953.08 → 953.84] because they're just changing
[953.84 → 954.90] every time requirements change
[954.90 → 955.76] and no one actually knows
[955.76 → 957.46] what the expected output is.
[957.86 → 958.12] Um,
[958.12 → 959.12] one more point I want to make.
[959.18 → 959.88] Someone said something
[959.88 → 961.34] about like test helper refactoring.
[961.34 → 962.46] I think that's true
[962.46 → 964.46] after a product is actually mature
[964.46 → 966.56] because you're just going to be,
[966.64 → 968.10] it's kind of like a snapshot test
[968.10 → 969.36] where you're just going to keep
[969.36 → 970.18] updating your tests
[970.18 → 971.76] every time something changes
[971.76 → 972.72] to the point where
[972.72 → 973.58] it's kind of pointless.
[973.72 → 974.94] So I always find
[974.94 → 975.90] when tests are like that,
[976.14 → 977.52] I usually just delete them immediately.
[978.16 → 978.70] Oh yeah.
[978.88 → 979.22] Go ahead.
[979.30 → 979.86] All right.
[979.86 → 980.04] All right.
[980.04 → 980.70] I called you trash.
[980.82 → 981.16] Oh my God.
[981.16 → 981.86] You call me trash.
[981.98 → 982.24] Your,
[982.40 → 984.74] your comment filled prime
[984.74 → 985.80] with so much joy.
[985.80 → 987.50] It translated into physical
[987.50 → 988.68] up and down motion.
[989.06 → 989.34] Yeah.
[989.52 → 992.00] I was literally watching him
[992.00 → 992.86] as I was talking
[992.86 → 993.60] and I was like,
[993.64 → 994.40] let's just see
[994.40 → 995.42] how hype we can get.
[995.62 → 995.86] Yeah.
[996.00 → 998.52] I wish I could see you guys.
[998.74 → 999.52] I see nothing.
[1001.20 → 1001.50] Yeah.
[1001.84 → 1002.16] Yeah.
[1002.16 → 1002.82] We see you.
[1002.90 → 1003.72] We see you guys.
[1003.80 → 1003.94] Yeah.
[1003.94 → 1004.06] Yeah.
[1004.06 → 1005.56] We can see you TJ.
[1005.82 → 1006.02] Enjoy.
[1006.02 → 1006.36] TJ,
[1006.52 → 1008.24] if you see a strange mushroom
[1008.24 → 1009.04] in the grass,
[1009.20 → 1010.18] do not eat it.
[1010.24 → 1010.56] Oh yeah.
[1010.60 → 1011.04] Don't eat it.
[1011.04 → 1012.64] Don't eat the strange mushroom TJ.
[1012.82 → 1013.54] When you're mowing,
[1013.76 → 1014.80] there's a strange mushroom.
[1015.80 → 1016.08] Guys,
[1016.18 → 1016.42] do I,
[1016.48 → 1017.78] I don't have my AI glasses.
[1018.10 → 1019.24] Do I eat this or not?
[1019.40 → 1020.46] Do I eat it or not guys?
[1022.36 → 1022.68] No,
[1022.96 → 1023.92] don't eat the mushroom.
[1024.80 → 1025.72] Eat the mushroom.
[1025.78 → 1026.56] That's all I heard.
[1026.66 → 1026.90] Okay.
[1027.12 → 1028.10] I'm going for it.
[1028.64 → 1028.84] Prime,
[1028.94 → 1029.44] say your thing.
[1029.60 → 1030.16] All right.
[1031.76 → 1032.24] All right.
[1032.24 → 1033.72] So the reason why
[1033.72 → 1034.80] I actually agree with trash
[1034.80 → 1035.42] a lot on this one
[1035.42 → 1036.34] is that I've done
[1036.34 → 1037.78] a lot of snapshot testing
[1037.78 → 1038.88] and I think there's probably
[1038.88 → 1039.74] does exist a world
[1039.74 → 1040.30] where this makes
[1040.30 → 1040.86] a lot of sense.
[1041.14 → 1042.52] It's just all the times
[1042.52 → 1043.54] I've ever done it.
[1043.94 → 1045.42] Whenever a requirement change,
[1045.42 → 1047.10] or I have to make a change
[1047.10 → 1048.22] that warrants changing
[1048.22 → 1048.74] the snapshot,
[1049.16 → 1049.96] I've also had to make
[1049.96 → 1051.04] some decent,
[1051.38 → 1052.80] some non-minor change
[1052.80 → 1053.90] also to some logic
[1053.90 → 1054.78] throughout the program.
[1055.18 → 1056.70] So when my snapshot breaks,
[1056.94 → 1057.90] I also don't know
[1057.90 → 1058.70] if I got it right.
[1058.94 → 1059.62] So now I'm like trying
[1059.62 → 1060.88] to hand eyeball through
[1060.88 → 1062.44] this thing like one end of line
[1062.44 → 1062.62] like,
[1062.70 → 1062.82] okay,
[1062.88 → 1064.64] is this really what I meant
[1064.64 → 1066.10] for it to be at this moment?
[1066.40 → 1067.04] How do I know
[1067.04 → 1067.62] I should change this
[1067.62 → 1068.28] from true to false?
[1068.28 → 1069.96] Like I have to re-reason
[1069.96 → 1070.46] about everything
[1070.46 → 1071.10] and I find that
[1071.10 → 1072.28] true snapshot testing
[1072.28 → 1072.90] on big things
[1072.90 → 1075.40] feels very difficult.
[1076.20 → 1077.08] Though I love it.
[1077.24 → 1077.64] Like I want,
[1077.76 → 1078.18] like ultimately
[1078.18 → 1079.08] that's what I always want.
[1079.24 → 1080.08] I fall into the
[1080.20 → 1080.28] hey,
[1080.32 → 1081.92] let's just make a golden trap
[1081.92 → 1083.02] constantly.
[1083.38 → 1083.88] Like that is like
[1083.88 → 1084.90] my default go-to.
[1085.00 → 1085.36] It's just like
[1085.36 → 1086.38] it's golden time
[1086.38 → 1087.86] and then I always get sad.
[1088.02 → 1088.68] As far as like
[1088.68 → 1091.56] the whole unit test breaking
[1091.56 → 1092.52] and mature product thing,
[1092.70 → 1093.66] I just find that
[1093.66 → 1094.60] testing generally,
[1095.06 → 1096.14] I do not think
[1096.14 → 1097.46] testing helps for refactoring
[1097.46 → 1098.66] unless it's a true
[1098.66 → 1099.62] end-to-end test.
[1099.96 → 1100.96] Like you use the product
[1100.96 → 1102.38] from the very hippy top
[1102.38 → 1103.86] and you only have
[1103.86 → 1104.74] the very bottom
[1104.74 → 1105.26] of the output.
[1105.40 → 1106.46] You have nothing else
[1106.46 → 1107.00] you look at
[1107.00 → 1108.68] but often I don't,
[1109.04 → 1110.42] like that's really hard
[1110.42 → 1111.08] to test
[1111.08 → 1112.40] because I'll write a function
[1112.40 → 1112.90] that I know
[1112.90 → 1113.68] is very difficult
[1113.68 → 1114.30] to get right
[1114.30 → 1115.56] and I just want to test
[1115.56 → 1116.26] those five things
[1116.26 → 1117.38] so I'm going to make a
[1117.46 → 1118.34] I'm going to make a test
[1118.34 → 1119.16] that's highly coupled
[1119.16 → 1120.10] to that piece
[1120.10 → 1121.20] and if you decide
[1121.20 → 1122.08] to refactor it,
[1122.52 → 1122.86] yeah,
[1123.06 → 1123.84] the tests all break.
[1124.00 → 1125.04] Like that's just a part of it.
[1125.14 → 1125.66] I wrote it
[1125.66 → 1127.00] so that this one thing works,
[1127.00 → 1127.58] this one way
[1127.58 → 1128.22] and I wrote a test
[1128.22 → 1129.10] that runs that one thing
[1129.10 → 1129.46] to make sure
[1129.46 → 1130.58] you didn't screw it up
[1130.58 → 1131.06] if you had to make
[1131.06 → 1132.22] a minor bug fix to it.
[1132.50 → 1133.46] I don't try to do
[1133.46 → 1134.02] that whole,
[1135.48 → 1136.76] I just really think
[1136.76 → 1137.32] this whole idea
[1137.32 → 1138.06] of unit testing
[1138.06 → 1138.78] and oh,
[1138.90 → 1139.88] it will prevent you
[1139.88 → 1140.50] from having headaches
[1140.50 → 1141.26] while refactoring
[1141.26 → 1142.98] has just been a lie
[1142.98 → 1143.44] from the beginning
[1143.44 → 1144.40] and then what you'll hear
[1144.40 → 1144.94] is people do
[1144.94 → 1145.58] the exact same thing
[1145.58 → 1145.94] every time.
[1146.24 → 1146.68] Oh, that's because
[1146.68 → 1147.10] you're testing
[1147.10 → 1147.84] at the wrong level.
[1148.20 → 1148.66] It's just like,
[1148.76 → 1149.44] I'm just testing
[1149.44 → 1150.42] the things that I want
[1150.42 → 1150.84] to test.
[1151.04 → 1151.70] I don't test
[1151.70 → 1152.42] all the things
[1152.42 → 1153.70] and what happens
[1153.70 → 1154.20] if you're testing
[1154.20 → 1154.78] on the wrong level
[1154.78 → 1155.46] just simply means
[1155.46 → 1156.44] that you broke
[1156.44 → 1157.20] a bunch of tests
[1157.20 → 1157.68] but then some
[1157.68 → 1158.40] of your tests didn't
[1158.40 → 1159.36] and that gave you
[1159.36 → 1159.88] the confidence
[1159.88 → 1160.32] that you did
[1160.32 → 1160.84] the right thing
[1160.84 → 1161.90] and I just don't,
[1162.96 → 1163.64] I just am not
[1163.64 → 1164.04] going to test
[1164.04 → 1164.50] the universe.
[1164.62 → 1164.88] I'm going to have
[1164.88 → 1165.64] a few end to end,
[1165.92 → 1166.22] I'm going to have
[1166.22 → 1167.04] the hard parts
[1167.04 → 1167.96] and that's that,
[1168.40 → 1168.86] no more.
[1168.86 → 1170.52] I also think like,
[1170.64 → 1170.84] I mean,
[1170.88 → 1171.30] when I'm thinking
[1171.30 → 1172.04] back to times
[1172.04 → 1172.94] when I've done
[1172.94 → 1173.46] testing,
[1174.42 → 1175.30] like,
[1176.04 → 1176.78] a lot of times
[1176.78 → 1178.02] when I will
[1178.02 → 1178.80] break out testing
[1178.80 → 1179.54] it's for things
[1179.54 → 1180.56] that I know
[1180.56 → 1181.38] aren't really
[1181.38 → 1182.52] all that refactorable
[1182.52 → 1183.38] or changeable anyway.
[1183.72 → 1184.24] It's like,
[1184.52 → 1185.00] oh, okay,
[1185.30 → 1185.72] I, you know,
[1185.76 → 1186.94] I made this memory
[1186.94 → 1187.42] allocator
[1187.42 → 1189.12] and we pretty much
[1189.12 → 1190.32] know what it does,
[1190.38 → 1190.56] right?
[1190.60 → 1191.22] You have these,
[1191.22 → 1191.40] like,
[1191.48 → 1192.10] two ways you can
[1192.10 → 1192.96] allocate memory from it
[1192.96 → 1193.82] and you have one way
[1193.82 → 1194.58] to free or something
[1194.58 → 1195.18] like that
[1195.18 → 1197.22] and then I just
[1197.22 → 1197.82] have these tests
[1197.82 → 1198.70] to make sure
[1198.70 → 1199.20] that, you know,
[1199.24 → 1200.12] it doesn't end up
[1200.12 → 1200.78] in bad states
[1200.78 → 1201.50] or whatever it is
[1201.50 → 1202.54] and that's a really
[1202.54 → 1203.60] useful thing,
[1203.66 → 1203.90] right?
[1203.94 → 1204.74] I've definitely done that.
[1204.80 → 1205.88] I do that for math libraries.
[1206.00 → 1206.12] Like,
[1206.14 → 1207.08] we kind of all know
[1207.08 → 1208.74] what the sign
[1208.74 → 1209.66] of something
[1209.66 → 1210.40] should return
[1210.40 → 1211.36] so if I'm making
[1211.36 → 1212.12] a math library
[1212.12 → 1212.66] that implements
[1212.66 → 1213.54] the sign function
[1213.54 → 1214.98] that's not,
[1215.10 → 1215.22] like,
[1215.24 → 1215.68] I don't have to
[1215.68 → 1216.80] think too hard
[1216.80 → 1218.24] about refactoring sign
[1218.24 → 1218.92] because math
[1218.92 → 1219.46] has been around
[1219.46 → 1219.92] for, like,
[1220.30 → 1220.62] you know,
[1220.96 → 1221.64] hundreds of years
[1221.64 → 1222.18] and isn't going
[1222.18 → 1222.96] to change tomorrow.
[1223.20 → 1223.28] Like,
[1223.32 → 1223.46] hell,
[1223.56 → 1224.32] bad news guys,
[1224.46 → 1224.58] like,
[1224.66 → 1225.96] React updated
[1225.96 → 1227.32] and now the definition,
[1227.32 → 1228.34] the mathematical definition
[1228.34 → 1228.80] of sign
[1228.80 → 1229.54] is different today.
[1229.74 → 1230.76] So I'm so happy
[1230.76 → 1231.24] that's not even
[1231.24 → 1231.92] a possibility
[1231.92 → 1232.60] that React
[1232.60 → 1233.58] does stuff with math
[1233.58 → 1234.54] because we'd be screwed.
[1234.54 → 1234.76] You know,
[1235.16 → 1235.36] guys,
[1235.46 → 1236.38] there's still time.
[1236.70 → 1237.72] There's still time.
[1238.98 → 1239.42] Yeah.
[1240.14 → 1240.62] So,
[1240.70 → 1241.56] so I do,
[1241.66 → 1242.54] I do like him
[1242.54 → 1242.98] for that
[1242.98 → 1243.94] and actually,
[1244.10 → 1244.26] like,
[1244.34 → 1244.84] there was a
[1244.94 → 1245.48] I can think
[1245.48 → 1246.56] of a specific time
[1246.56 → 1248.16] when I was shipping
[1248.16 → 1248.94] game libraries
[1248.94 → 1251.06] when we had
[1251.06 → 1252.16] a terrible bug
[1252.16 → 1254.46] that caused a problem
[1254.46 → 1255.30] for one particular
[1255.30 → 1256.28] customer that took
[1256.28 → 1257.28] forever to find
[1257.28 → 1258.94] and it was because
[1258.94 → 1259.94] it was in a thing
[1259.94 → 1260.82] that I had added
[1260.82 → 1261.58] to the library
[1261.58 → 1262.86] just for that customer
[1262.86 → 1263.28] as, like,
[1263.30 → 1263.98] a backdoor,
[1264.44 → 1264.62] right?
[1264.68 → 1265.10] They're like,
[1265.14 → 1266.22] we need this one thing
[1266.22 → 1266.84] really quick
[1266.84 → 1267.18] and I was like,
[1267.22 → 1267.46] okay,
[1267.54 → 1268.26] and I put it in there
[1268.26 → 1269.64] and it had a bug in it
[1269.64 → 1270.32] and, of course,
[1270.36 → 1271.30] it wasn't in any
[1271.30 → 1272.40] of my standard testing
[1272.40 → 1273.00] or anything.
[1273.00 → 1273.94] It wasn't even really
[1273.94 → 1275.02] in anyone's use case,
[1275.08 → 1275.32] right?
[1275.96 → 1277.32] And so,
[1277.56 → 1277.60] like,
[1278.84 → 1279.08] you know,
[1279.16 → 1279.48] that was,
[1279.66 → 1280.06] to me,
[1280.10 → 1280.52] I was like,
[1280.60 → 1280.84] okay,
[1280.92 → 1281.60] that's a pretty,
[1281.74 → 1283.34] that's pretty good evidence
[1283.34 → 1283.74] that, like,
[1283.78 → 1284.72] the testing that I was
[1284.72 → 1286.12] doing before was good
[1286.12 → 1286.84] and, like,
[1286.92 → 1288.04] wasn't a waste of time
[1288.04 → 1288.64] because, like,
[1288.66 → 1289.52] the one time
[1289.52 → 1290.46] it didn't happen,
[1291.04 → 1291.96] it caused a significant
[1291.96 → 1292.74] problem, right?
[1292.82 → 1293.28] And so,
[1293.82 → 1294.06] you know,
[1294.18 → 1295.14] presumably I would have
[1295.14 → 1296.32] had more of those
[1296.32 → 1298.32] in actual other customers
[1298.32 → 1299.48] had the main,
[1299.56 → 1300.24] had all the stuff
[1300.24 → 1300.92] that normally shifts
[1300.92 → 1301.38] to the library
[1301.38 → 1302.22] not been tested
[1302.22 → 1303.62] in the way that I thought
[1303.62 → 1304.26] it should have been.
[1304.48 → 1304.86] And, you know,
[1304.86 → 1305.56] from then I was like,
[1305.56 → 1306.18] you know,
[1306.18 → 1306.56] don't,
[1306.88 → 1308.12] never do a one-off ad.
[1308.24 → 1308.42] Like,
[1308.48 → 1309.16] if I'm going to add
[1309.16 → 1309.84] something for a customer,
[1310.00 → 1310.60] I'll add it,
[1310.68 → 1310.90] like,
[1311.14 → 1311.76] the right way
[1311.76 → 1312.92] and actually put in
[1312.92 → 1313.62] the testing for it
[1313.62 → 1314.26] or I'll just tell them,
[1314.32 → 1315.34] I'm sorry I can't
[1315.34 → 1316.14] do that right now
[1316.14 → 1316.48] because,
[1316.60 → 1316.72] you know,
[1316.72 → 1317.14] I'm too busy
[1317.14 → 1317.46] or whatever.
[1317.86 → 1318.38] And so,
[1318.70 → 1319.26] I do think,
[1319.36 → 1319.56] like,
[1320.08 → 1320.36] yeah,
[1320.82 → 1322.00] when you can actually
[1322.00 → 1322.72] talk about,
[1322.90 → 1324.12] this is isolated,
[1324.24 → 1325.16] this is what this thing does,
[1325.18 → 1325.64] I'm pretty sure
[1325.64 → 1326.44] it's not going to change.
[1326.72 → 1327.78] I think the tests are great
[1327.78 → 1329.04] but before then,
[1329.20 → 1329.36] yeah,
[1329.44 → 1329.74] it's just,
[1329.82 → 1330.24] and also,
[1331.16 → 1332.10] this was just kind of
[1332.10 → 1332.82] going off on a random
[1332.82 → 1333.64] anecdote but,
[1333.68 → 1334.94] just to circle back,
[1335.22 → 1335.88] the thing that Prime
[1335.88 → 1336.78] was saying is absolutely true,
[1336.86 → 1337.10] it's like,
[1337.22 → 1338.20] refactor testing,
[1338.60 → 1339.20] not really.
[1339.34 → 1339.46] Like,
[1339.52 → 1340.06] that's only,
[1340.38 → 1341.42] you can only really get,
[1341.52 → 1341.58] like,
[1341.60 → 1342.48] a very high level
[1342.48 → 1343.44] confidence from that.
[1343.68 → 1344.52] You can't really know,
[1344.54 → 1345.34] there could be all sorts
[1345.34 → 1345.96] of things that aren't
[1345.96 → 1346.52] really working
[1346.52 → 1347.96] because whole system
[1347.96 → 1348.74] testing like that
[1348.74 → 1349.50] is going to miss,
[1349.82 → 1350.44] it's going to miss,
[1350.48 → 1350.66] like,
[1350.94 → 1352.10] weird edge cases
[1352.10 → 1353.02] that can overlap
[1353.02 → 1354.18] and the only way
[1354.18 → 1354.96] you catch those
[1354.96 → 1355.40] with test-driven
[1355.40 → 1356.36] development is knowing
[1356.36 → 1357.46] about those edge cases
[1357.46 → 1359.12] and making tests
[1359.12 → 1360.52] to kind of target them
[1360.52 → 1361.84] and you can't do that
[1361.84 → 1362.82] if you just refactored
[1362.82 → 1363.02] everything
[1363.02 → 1363.98] because now the edge cases
[1363.98 → 1364.50] are different,
[1364.62 → 1364.84] right?
[1365.08 → 1365.48] So,
[1365.82 → 1365.94] yeah,
[1365.98 → 1367.32] I think TDD people
[1367.32 → 1368.54] overstate the degree
[1368.54 → 1369.58] to which that really works.
[1370.22 → 1371.12] That's why I'm,
[1371.16 → 1374.00] I'm a huge fan of PDD,
[1374.74 → 1375.78] prog-driven development.
[1376.26 → 1377.28] I think that every time
[1377.28 → 1377.72] you release
[1377.72 → 1378.30] and you have a bunch
[1378.30 → 1379.08] of people that use
[1379.08 → 1379.54] your product,
[1380.06 → 1380.80] you should do
[1380.80 → 1381.66] a slow release,
[1382.10 → 1382.86] you should measure
[1382.86 → 1383.36] the outcome
[1383.36 → 1384.00] because it's just
[1384.00 → 1384.48] going to test
[1384.48 → 1385.36] all the weird things
[1385.36 → 1385.92] you're never going
[1385.92 → 1386.58] to be able to think
[1386.58 → 1387.34] of or set up
[1387.34 → 1388.82] and if it starts,
[1388.94 → 1390.48] if it starts breaking,
[1391.00 → 1391.68] you know that
[1391.68 → 1392.34] you screwed up.
[1392.52 → 1393.24] Previous version
[1393.24 → 1393.78] worked better
[1393.78 → 1394.54] than the new version.
[1394.76 → 1395.86] You can't release
[1395.86 → 1396.56] this new version.
[1396.78 → 1397.62] You got to back it up.
[1397.76 → 1398.54] Not P. Diddy.
[1398.84 → 1399.62] P. Diddy, okay?
[1399.70 → 1400.24] Stop saying P.
[1400.24 → 1401.24] There's no baby oil
[1401.24 → 1403.28] in this situation, okay?
[1403.70 → 1404.06] But I mean,
[1404.26 → 1404.96] to me, it's like-
[1404.96 → 1405.94] Shots fired at Sonos
[1405.94 → 1406.76] or Sonos
[1406.76 → 1407.60] or whatever that company
[1407.60 → 1408.04] is called.
[1408.90 → 1409.38] I don't know what,
[1409.44 → 1410.24] I don't know what they did.
[1410.30 → 1411.02] I don't know what them did.
[1411.02 → 1411.18] Yeah.
[1411.90 → 1412.26] So,
[1412.70 → 1413.12] you don't,
[1413.26 → 1415.06] you guys are supposed
[1415.06 → 1416.46] to be the web dev people.
[1416.66 → 1417.20] What's going on?
[1417.20 → 1417.70] What the hell
[1417.70 → 1419.04] are you talking about, Casey?
[1419.96 → 1420.40] Sonos,
[1420.58 → 1421.32] the company that makes
[1421.32 → 1421.82] the speakers.
[1424.48 → 1424.92] Nobody?
[1425.48 → 1425.72] Bose?
[1425.72 → 1426.16] I don't.
[1426.28 → 1426.46] Bose.
[1426.48 → 1427.12] Are you kidding me?
[1427.44 → 1428.48] You guys are the web dev.
[1428.72 → 1429.32] Everything got.
[1429.70 → 1430.74] Beats by DRE?
[1431.48 → 1433.12] No, this is like legendary.
[1433.46 → 1434.66] Like everyone knew about this.
[1434.94 → 1435.92] So, there's this company
[1435.92 → 1436.56] called Sonos.
[1436.64 → 1437.78] They make like the most popular
[1437.78 → 1438.86] internet powered speakers
[1438.86 → 1439.48] in the world.
[1439.48 → 1441.08] Like everyone has these things.
[1441.44 → 1441.96] I mean, not me
[1441.96 → 1443.70] because there's no way
[1443.70 → 1444.40] in hell I'm connecting
[1444.40 → 1445.32] speakers to the internet.
[1445.52 → 1446.18] That's just a way
[1446.18 → 1446.92] to make them not work,
[1446.92 → 1448.00] which Sonos went ahead
[1448.00 → 1449.36] and demonstrated for me.
[1449.62 → 1450.92] They had a product
[1450.92 → 1451.68] that everyone liked.
[1451.76 → 1452.32] They were extremely
[1452.32 → 1453.14] popular speaker.
[1453.78 → 1455.10] They then did a big
[1455.10 → 1456.10] software update
[1456.10 → 1457.02] where like they were like,
[1457.10 → 1457.78] we're rolling out
[1457.78 → 1458.64] our new system.
[1458.84 → 1459.14] Like, you know,
[1459.16 → 1459.90] kind of like how Google
[1459.90 → 1460.86] does every couple years.
[1460.92 → 1461.24] They're like,
[1461.60 → 1462.20] hey, guess what?
[1462.42 → 1463.20] Gmail is going to suck
[1463.20 → 1464.60] way harder than before today.
[1464.76 → 1465.08] Like you're,
[1465.40 → 1466.24] you have five,
[1466.38 → 1466.54] you know,
[1466.58 → 1467.58] you'll get five months
[1467.58 → 1468.42] of being able to switch
[1468.42 → 1468.88] between them
[1468.88 → 1469.46] and then you're on
[1469.46 → 1470.28] to the new bad one.
[1470.78 → 1471.68] They did that
[1471.68 → 1473.02] only there were no five months.
[1473.12 → 1474.14] They just basically said like,
[1474.14 → 1475.36] here's the new rollout
[1475.36 → 1476.42] and it was awful.
[1476.58 → 1478.38] Like tons of feature regressions.
[1478.54 → 1479.72] It didn't really work.
[1480.08 → 1480.84] Customers couldn't do
[1480.84 → 1481.42] most of the things
[1481.42 → 1482.00] they used to
[1482.00 → 1483.48] and it is like tanked
[1483.48 → 1484.00] the company.
[1484.16 → 1485.26] Like it was just like
[1485.26 → 1487.46] immediately everyone hated it
[1487.46 → 1488.20] and nobody wanted
[1488.20 → 1489.02] to buy their stuff
[1489.02 → 1489.66] and they had to do
[1489.66 → 1490.22] this walk back
[1490.22 → 1492.58] and they couldn't roll back
[1492.58 → 1493.30] because they had
[1493.30 → 1494.92] redeployed all their servers
[1494.92 → 1496.16] and I guess they didn't know
[1496.16 → 1497.70] how to like deploy them.
[1497.70 → 1498.70] So they couldn't,
[1498.82 → 1499.84] you couldn't go back
[1499.84 → 1500.74] to the old app.
[1501.00 → 1501.26] It was,
[1501.72 → 1502.70] go read about this.
[1502.76 → 1503.36] I can't believe
[1503.36 → 1504.14] no one knows about this
[1504.14 → 1504.44] but me.
[1504.60 → 1505.88] It was a massive failure.
[1506.16 → 1506.54] I know it.
[1506.54 → 1507.18] Never heard of them.
[1507.70 → 1508.28] I heard it.
[1508.36 → 1508.56] Okay.
[1508.72 → 1508.98] Casey,
[1509.10 → 1509.82] I don't know if you guys
[1509.82 → 1510.20] can hear me
[1510.20 → 1510.98] but I heard that.
[1511.72 → 1511.86] Okay.
[1512.54 → 1513.42] We can hear you.
[1513.44 → 1514.22] We can hear you, TJ.
[1514.36 → 1515.26] We can't really see you.
[1515.36 → 1517.12] You have very few expressions.
[1517.98 → 1518.52] That's fine.
[1518.80 → 1519.16] But I do,
[1519.36 → 1519.52] okay,
[1519.96 → 1520.76] your point is that
[1520.76 → 1521.82] hardware is definitely
[1521.82 → 1522.94] different from software.
[1523.54 → 1523.68] You know,
[1523.72 → 1525.08] if Twitter has a small
[1525.08 → 1526.04] breaking thing
[1526.04 → 1526.78] because they made something,
[1526.78 → 1527.42] Twitter,
[1527.60 → 1528.38] all these major sites
[1528.38 → 1529.08] they break all the time,
[1529.10 → 1529.28] right?
[1529.36 → 1530.44] I have much more
[1530.44 → 1531.24] forgiveness for that.
[1531.74 → 1532.04] This is,
[1532.24 → 1532.52] you know,
[1532.54 → 1533.92] that's obviously different
[1533.92 → 1534.24] than,
[1534.92 → 1535.22] you know,
[1535.68 → 1536.66] you got to play the field
[1536.66 → 1537.34] a little bit different
[1537.34 → 1538.64] when I say break production.
[1538.82 → 1540.38] If I'm building a game
[1540.38 → 1540.78] that only,
[1540.98 → 1541.28] you know,
[1541.44 → 1542.42] so many people play,
[1542.50 → 1543.00] you don't want it
[1543.00 → 1544.14] just crashing nonstop
[1544.14 → 1545.86] while you're testing features.
[1546.02 → 1547.14] There are probably some levels
[1547.14 → 1547.70] but if you're Twitter
[1547.70 → 1548.74] and all of a sudden
[1548.74 → 1549.74] you can't post for
[1549.74 → 1550.74] five minutes
[1550.74 → 1552.64] and only .001%
[1552.64 → 1553.00] of the people
[1553.00 → 1554.12] couldn't post for five minutes,
[1554.40 → 1555.14] it's just not going to
[1555.14 → 1555.88] make a huge splash
[1555.88 → 1556.64] and it's probably not going to
[1556.64 → 1557.50] deter them from actually
[1557.50 → 1558.26] using the product again.
[1558.66 → 1558.80] Well,
[1558.86 → 1559.30] I was actually,
[1559.42 → 1559.50] no,
[1559.54 → 1560.24] I was agreeing with you
[1560.24 → 1560.78] with the Sonos thing.
[1560.84 → 1561.54] What I was saying was
[1561.54 → 1562.62] they should have done
[1562.62 → 1563.68] exactly what you're talking about.
[1564.04 → 1564.84] They should have taken
[1564.84 → 1567.70] and deployed a small server bank
[1567.70 → 1569.10] for what they were doing.
[1569.28 → 1569.44] Oh,
[1569.50 → 1569.70] I see.
[1569.72 → 1571.36] Given it to 1% of their users
[1571.36 → 1572.18] and their users would have been like,
[1572.26 → 1573.62] this is utter garbage
[1573.62 → 1574.98] and I do not want it
[1574.98 → 1575.74] and they would have been like,
[1575.82 → 1576.02] okay,
[1576.44 → 1577.16] pull that on back.
[1577.58 → 1578.34] Nobody saw it.
[1578.64 → 1579.08] We're fine,
[1579.26 → 1579.46] right?
[1579.58 → 1580.94] So exactly what you're saying,
[1581.04 → 1582.36] I was totally agreeing with you.
[1582.42 → 1582.66] I'm like,
[1582.96 → 1583.28] Sonos,
[1583.28 → 1584.28] if they had done that,
[1584.34 → 1585.14] they would have totally
[1585.14 → 1586.00] saved their company
[1586.00 → 1587.94] literally like six months of hell.
[1588.26 → 1591.30] Had they just given a slice of users
[1591.30 → 1592.94] this thing for a while,
[1593.18 → 1593.76] they would have been,
[1593.88 → 1594.04] you know,
[1594.04 → 1595.28] some significant percentage
[1595.28 → 1596.34] above beta test,
[1596.40 → 1596.52] right?
[1596.56 → 1596.72] Like,
[1596.78 → 1597.66] so like you said,
[1597.70 → 1597.92] you know,
[1598.00 → 1598.58] 5,
[1598.68 → 1599.92] 10% of the people got this.
[1600.00 → 1600.50] They would all have been like,
[1600.56 → 1600.70] nope,
[1600.78 → 1600.94] nope,
[1601.00 → 1601.18] nope,
[1601.22 → 1601.36] nope,
[1601.40 → 1601.56] nope.
[1601.68 → 1602.60] And then they would have like,
[1602.68 → 1602.86] you know,
[1602.86 → 1603.06] been like,
[1603.10 → 1603.28] okay,
[1603.36 → 1603.56] okay.
[1603.56 → 1606.58] So that's all.
[1606.74 → 1607.20] I do want to,
[1607.32 → 1607.58] can I,
[1607.68 → 1609.98] can I say one thing just about the testing part though?
[1610.96 → 1611.68] Is that okay?
[1612.18 → 1612.82] From before?
[1613.28 → 1613.64] Maybe.
[1613.98 → 1614.14] Sure.
[1614.20 → 1615.48] That's what the podcast is about.
[1615.62 → 1615.84] Exactly.
[1616.06 → 1616.74] I like this.
[1616.74 → 1617.22] I like this.
[1617.34 → 1617.92] Go for TJ.
[1618.32 → 1618.72] Um,
[1619.36 → 1621.46] my favourite project that I've ever worked on,
[1621.72 → 1622.16] Neovim,
[1622.30 → 1622.92] by the way.
[1623.86 → 1624.26] Um,
[1624.36 → 1625.60] can you go back to the grass?
[1625.72 → 1628.00] You were much more like better in the grass.
[1628.28 → 1628.64] Really?
[1628.84 → 1628.98] Okay.
[1628.98 → 1629.62] My phone,
[1629.82 → 1630.34] if I got it,
[1630.44 → 1630.72] the tower,
[1630.72 → 1632.10] I got a notification that said,
[1632.10 → 1635.14] your phone is overheating because I was in the sunshine.
[1635.22 → 1637.24] I was actually going to bring that up in the beginning.
[1638.64 → 1640.44] Like it literally said your phone is over.
[1640.44 → 1641.66] Your body's the one covering.
[1642.38 → 1642.74] Okay.
[1643.08 → 1643.30] All right.
[1643.30 → 1643.82] Sit over,
[1643.96 → 1645.16] create a shadow TJ.
[1645.38 → 1646.02] So they can't,
[1646.08 → 1647.14] you guys are in the shadows.
[1647.38 → 1647.74] Get your phone.
[1648.08 → 1649.96] You got to plank over your phone.
[1650.36 → 1650.46] Hey,
[1650.46 → 1650.98] what's up boys.
[1651.40 → 1651.58] Hey,
[1651.60 → 1651.72] yo,
[1651.72 → 1652.20] what's up boys.
[1652.40 → 1657.54] This is like getting into like TJ profile pic territory where it's like on the dating app.
[1657.54 → 1659.50] Can you tell us some of your pet peeves,
[1659.60 → 1659.84] TJ?
[1660.36 → 1661.98] Do you like long walks on the beach?
[1662.54 → 1662.98] I'm a
[1663.04 → 1664.82] I'm a long walks enjoyer.
[1665.20 → 1667.26] I'm really not a fan of short conversations.
[1667.26 → 1669.28] I want to really find out about the real you.
[1670.22 → 1670.62] Um,
[1670.78 → 1671.82] I don't know what else.
[1673.42 → 1675.64] I don't even know if any of my words are coming through.
[1675.88 → 1678.20] TJ is actually just describing himself right now.
[1678.60 → 1679.68] That's all TJ is doing.
[1680.24 → 1681.16] I love laughing.
[1681.52 → 1682.54] I love having fun.
[1682.66 → 1683.86] I like to make you laugh.
[1684.04 → 1685.10] This is just me to prime.
[1685.10 → 1686.68] This is my pitch for getting on the
[1686.68 → 1687.82] on the podcast.
[1687.82 → 1692.64] I'll make fun of trash.
[1693.44 → 1693.84] Yo,
[1694.14 → 1694.42] if,
[1694.50 → 1696.54] if there's a guy named trash on the podcast,
[1696.54 → 1698.02] I will make sure to make fun of him.
[1698.10 → 1699.10] Every episode.
[1699.32 → 1700.70] He uses one password.
[1700.80 → 1701.50] Are you joking?
[1703.76 → 1704.44] All right.
[1704.44 → 1704.76] All right.
[1704.76 → 1705.06] All right.
[1705.06 → 1705.30] All right.
[1705.30 → 1705.54] TJ,
[1705.64 → 1706.26] what's your take?
[1706.82 → 1709.76] My take is my favourite project that I've worked on.
[1709.96 → 1714.70] And like definitely the one with the most weird edge cases and probably users.
[1715.04 → 1715.56] Neo Vim.
[1716.06 → 1718.82] Like the test sweeper Neo Vim is amazing.
[1718.96 → 1719.94] We have tons of,
[1720.04 → 1722.34] we have different like styles of tests.
[1722.42 → 1724.08] We have different ways to run them.
[1724.12 → 1725.10] We have all this different stuff.
[1725.10 → 1728.26] Tons of work went into making it.
[1728.36 → 1734.38] And maybe that's just partially because Neo Vim is like trying to maintain compatibility with Vim on some stuff,
[1734.50 → 1735.52] like literally forever.
[1735.52 → 1735.86] Right.
[1735.90 → 1737.98] So there are some other requirements that are different,
[1737.98 → 1738.76] but man,
[1738.84 → 1743.16] every time I did a PR and a random test broke,
[1743.74 → 1744.94] it was my fault.
[1745.04 → 1746.56] It was not the other tests.
[1746.58 → 1747.94] It was not the snapshot tests.
[1747.94 → 1748.90] It was nothing else.
[1748.90 → 1749.22] Like,
[1749.48 → 1750.86] and like random stuff.
[1750.88 → 1751.12] I mean,
[1751.12 → 1753.80] maybe it's just because Neo Vim is also like a ancient C project.
[1753.94 → 1758.98] So you like change something and then a random global is destroyed.
[1759.28 → 1759.82] I don't know.
[1759.90 → 1760.12] You know,
[1760.12 → 1760.40] it's like,
[1760.44 → 1760.68] whatever,
[1760.76 → 1762.08] it's maybe not always the best,
[1762.16 → 1762.50] but like,
[1763.28 → 1763.66] so I don't,
[1763.76 → 1763.92] in,
[1763.92 → 1769.80] in my experience where people like actually cared about it and like cared to maintain snapshots and make those happen.
[1769.92 → 1772.24] Like no one's even getting paid to work on Neo Vim.
[1772.58 → 1773.28] You know what I'm saying?
[1773.28 → 1774.94] And like the snapshots were valuable.
[1774.94 → 1776.12] The unit tests are valuable.
[1776.12 → 1777.30] The functional tests were valuable.
[1777.30 → 1782.92] And I use them in a ton of different PRs and across like really large refactors,
[1782.98 → 1784.68] adding Lua to auto commands,
[1784.78 → 1789.00] like doing lots of different stuff where I had to change tons and tons of the code.
[1789.52 → 1792.30] I was just wrong every time until the test went green.
[1792.30 → 1798.60] I think that probably goes to show that tests are as valuable as the people who wrote them.
[1798.60 → 1800.74] I was literally going to say that.
[1801.06 → 1801.20] Yeah.
[1801.26 → 1802.80] That's what I've been waiting to say too,
[1802.88 → 1804.26] is I just wanted to say,
[1804.38 → 1805.34] but since I've been lagging,
[1805.36 → 1806.04] I didn't want to yell.
[1806.14 → 1807.80] I just wanted to yell skill issue to everything.
[1807.90 → 1808.78] Trash has been saying.
[1808.78 → 1811.00] I would,
[1811.00 → 1811.76] I would disagree.
[1812.08 → 1812.36] Actually,
[1812.52 → 1814.06] I will defend trash.
[1814.42 → 1814.86] Okay.
[1815.00 → 1815.44] Actually,
[1815.70 → 1816.64] Casey's smarter than you.
[1816.98 → 1817.98] Because here's the thing.
[1818.26 → 1818.96] That's true.
[1819.08 → 1819.54] Dang it.
[1820.48 → 1821.48] I suspect,
[1821.48 → 1825.90] I suspect that some of what you're seeing though,
[1825.90 → 1828.68] is not so much the skill of the people who did it,
[1828.74 → 1830.18] although they may have been very skilled.
[1830.68 → 1833.22] It's more just about when the tests were added.
[1833.68 → 1834.88] So at least for me,
[1834.88 → 1836.80] a lot of times what I'll do is I'll go,
[1837.02 → 1837.24] okay,
[1837.42 → 1837.60] if,
[1837.74 → 1838.38] if I like,
[1838.38 → 1841.22] let's say I have a bug that I actually work on for a day.
[1841.38 → 1841.74] Like,
[1841.80 → 1843.82] like this is because most bugs are like,
[1843.88 → 1844.24] oh yeah,
[1844.26 → 1844.86] I know what it is.
[1844.86 → 1845.60] And you just fix it.
[1845.60 → 1845.82] Right.
[1846.06 → 1847.14] But you get one of yours.
[1847.20 → 1847.42] Like,
[1847.80 → 1849.12] what the hell is happening?
[1849.24 → 1850.20] And you actually,
[1850.20 → 1852.96] it's like that once every few months when you're just like,
[1853.54 → 1853.88] okay,
[1853.88 → 1855.24] this is really weird.
[1855.24 → 1856.44] And I'm not sure what it is.
[1857.22 → 1858.50] When I find those,
[1858.58 → 1862.42] I typically try to add a test or assertions or whatever.
[1862.42 → 1865.02] I think would have caught it.
[1865.24 → 1865.60] Right.
[1865.64 → 1866.18] Because I'm like,
[1866.24 → 1866.50] okay,
[1866.52 → 1867.56] this one's nasty.
[1867.56 → 1869.22] And I wasn't expecting it.
[1869.44 → 1872.74] What can I add that will trip this kind of thing up?
[1872.74 → 1873.66] And I'll add it.
[1873.66 → 1879.42] And I suspect that much of what gets seen in like mature products like Neovim are just like,
[1879.88 → 1880.06] Hey,
[1880.12 → 1883.06] if you've got some post test discipline,
[1883.26 → 1884.92] like after we made the product,
[1884.94 → 1886.20] when we're finding bugs,
[1886.20 → 1887.90] we add the test that would have caught the bugs.
[1888.28 → 1894.92] Those are often very good because they come out of what are the things that are likely to break when we do stuff.
[1894.92 → 1896.96] And we put in a net there to catch them.
[1897.16 → 1899.18] And so those are like very good.
[1899.34 → 1901.12] And they're the opposite of TDD.
[1901.42 → 1902.06] They're like,
[1902.58 → 1902.84] Oh,
[1902.98 → 1903.56] they're TDD.
[1903.76 → 1905.42] They're test driven debugging.
[1906.64 → 1907.66] Maybe you could say,
[1907.88 → 1908.02] or,
[1908.12 → 1909.32] or something like that.
[1909.38 → 1909.52] But,
[1909.68 → 1909.92] but,
[1910.02 → 1910.48] so,
[1910.48 → 1912.98] so I do think there's something to that.
[1912.98 → 1914.68] But that that's a lot more,
[1914.80 → 1916.74] I had a couple other hot takes that I'll get to.
[1916.82 → 1917.52] I just want to leave it.
[1917.64 → 1919.56] I want to say that one based on what you said.
[1919.68 → 1920.86] I don't know if that's true about Neovim,
[1920.96 → 1922.20] but I might suspect it.
[1922.28 → 1922.38] Right.
[1922.62 → 1923.58] It definitely is.
[1923.64 → 1924.24] The thing though,
[1924.24 → 1926.00] that like I was more pushing back.
[1926.04 → 1926.32] I was like,
[1926.46 → 1929.84] I find the snapshot tests in Neovim invaluable.
[1929.84 → 1930.32] Like I,
[1930.54 → 1931.50] they're amazing.
[1931.50 → 1935.38] I find a bunch of these good end-to-end tests,
[1935.56 → 1936.28] truly end to end.
[1936.42 → 1939.76] Like literally it runs a test and does user.
[1940.24 → 1941.34] I don't know if I just dropped.
[1941.54 → 1942.84] It does like user input.
[1942.98 → 1944.12] And then asserts the outputs,
[1944.50 → 1944.70] right?
[1944.78 → 1946.20] Like though,
[1946.26 → 1948.00] I found those super valuable in Neovim.
[1948.28 → 1949.16] Probably just dropped.
[1949.64 → 1949.74] Yeah.
[1950.36 → 1951.02] I also,
[1951.16 → 1951.28] no,
[1951.32 → 1951.56] you didn't,
[1951.60 → 1952.04] you didn't drop.
[1952.10 → 1952.28] We said,
[1952.36 → 1952.92] we heard your point.
[1952.96 → 1955.90] I think also to put on top of it is thought about the
[1955.90 → 1960.62] the horizon of Neovim versus you starting up a new dev tool at work.
[1961.02 → 1961.66] And maybe,
[1961.84 → 1966.26] maybe there's something to be said about when are the goldens introduced during
[1966.26 → 1969.64] exploration phase or like Neovim is just not going to be changing.
[1969.80 → 1972.74] My assumption is that a lot of Neovim doesn't change.
[1972.74 → 1973.64] Super hard.
[1973.72 → 1974.14] It's not like,
[1974.20 → 1974.58] Hey guys,
[1974.58 → 1976.72] let's do a whole new data model today.
[1977.26 → 1977.60] Wrong.
[1978.22 → 1978.90] Changes all the time.
[1978.90 → 1979.56] All the ones.
[1979.66 → 1981.02] That's all the ones that ever,
[1981.18 → 1983.20] everything you guys have poo pooed on that.
[1983.20 → 1986.68] I found them the most valuable when I changed literally the entire data
[1986.68 → 1989.40] model and how all auto commands work all inside of Neovim.
[1989.40 → 1992.14] It was the most useful to have the snapshot tests.
[1992.14 → 1992.38] Then,
[1992.38 → 1992.88] I mean,
[1992.90 → 1995.88] your testing is going to depend greatly on what you're building.
[1996.52 → 1996.96] 100%.
[1996.96 → 1997.44] Sure.
[1997.66 → 1997.82] Yeah.
[1997.86 → 1997.96] Yeah.
[1997.96 → 1998.76] But I'm just saying like,
[1998.84 → 2000.48] we were fundamentally changing the data.
[2001.02 → 2001.38] Yeah.
[2001.38 → 2001.48] Yeah.
[2003.06 → 2003.86] I'm just saying.
[2004.18 → 2004.90] That's what happened.
[2005.62 → 2005.96] Yeah.
[2006.08 → 2007.70] I thought it was a pretty smart statement.
[2007.84 → 2008.32] Come on.
[2010.74 → 2011.68] You're really smart.
[2011.76 → 2014.16] I wouldn't poo poo that at all.
[2014.16 → 2014.40] I,
[2014.40 → 2016.88] you've noticed I have not poo pooed snapshot testing.
[2017.10 → 2017.32] True.
[2017.62 → 2018.26] Good job,
[2018.34 → 2018.58] Casey.
[2018.58 → 2019.56] I love you.
[2019.62 → 2020.72] You're smarter than trash.
[2023.78 → 2024.58] I love that.
[2024.70 → 2025.64] I'm not getting dunked on.
[2025.80 → 2030.28] Can we start rearranging the windows based on who Teen thinks is
[2030.28 → 2031.54] smartest at any given time.
[2031.54 → 2034.94] And I'm guessing that it has a very high correlation to who is
[2034.94 → 2035.76] agreeing with him.
[2036.10 → 2036.80] It's like,
[2036.86 → 2037.66] I'm getting that sense.
[2037.66 → 2039.18] I'll just always put trash at the end.
[2039.24 → 2039.54] It's fine.
[2039.58 → 2039.78] Casey.
[2039.78 → 2040.52] You don't have to worry.
[2040.90 → 2041.22] Today.
[2041.22 → 2043.86] I'm going to tweet that Casey protected me from Teen.
[2043.86 → 2044.34] Yes.
[2044.44 → 2046.82] This is a pinnacle moment of my career.
[2047.38 → 2049.64] I can't even see your guy's videos.
[2049.76 → 2051.46] So I have no idea what's happening.
[2051.58 → 2053.64] I'm talking to a black screen right now.
[2055.36 → 2058.16] I've been just cracking up at your feed this whole time.
[2058.22 → 2059.28] I just can't handle it.
[2059.28 → 2060.00] It's pretty good.
[2060.16 → 2061.02] It's very good.
[2061.10 → 2062.40] Like the result is,
[2062.40 → 2063.86] is top-notch of the feed.
[2064.46 → 2064.90] Unfortunately,
[2064.90 → 2066.88] I think this will be a stream only feature.
[2067.14 → 2069.60] I don't know if TJ will actually have this effect on the video
[2069.60 → 2071.08] because Riverside will be uploading it.
[2071.16 → 2071.68] That's true.
[2071.96 → 2072.40] Yeah,
[2072.50 → 2072.86] that's true.
[2072.86 → 2073.70] He'll still be in,
[2073.70 → 2074.22] in weird,
[2074.22 → 2078.68] like it is a profile is dating site profile pic phase,
[2078.80 → 2078.98] but,
[2078.98 → 2080.44] but it will be much smoother.
[2080.58 → 2080.72] Yeah.
[2081.30 → 2081.54] So,
[2081.74 → 2082.46] so anyway,
[2082.64 → 2083.34] I,
[2083.56 → 2084.78] I wanted to add a hot,
[2084.84 → 2085.08] I,
[2085.08 → 2086.92] I would agree that snapshot testing,
[2086.92 → 2087.66] it can be good.
[2087.72 → 2088.10] It depends.
[2088.16 → 2090.42] It just depends on whether those snapshots are going to be stable.
[2090.42 → 2090.68] I mean,
[2090.68 → 2091.60] that's the bottom line.
[2091.60 → 2092.58] If you have,
[2093.30 → 2093.82] if you're,
[2094.16 → 2103.92] I would imagine what prime and trash were talking about is if you're trying to snapshot testing at a level below something that's actually consistent across the refactor,
[2104.26 → 2105.70] obviously that's not going to work.
[2105.70 → 2106.00] Right?
[2106.00 → 2109.34] And so if your snapshot testing is like someone mentioned a parse tree.
[2109.66 → 2109.94] Well,
[2110.02 → 2112.94] if it's a parse of something that could be parsed different ways,
[2113.00 → 2115.38] depending on how you chose to implement that subsystem,
[2115.72 → 2116.92] those snapshots are useless.
[2117.16 → 2121.68] If the parse always has to be the same because it's like parsing for the C language specification,
[2121.68 → 2123.56] and it can't change because like,
[2123.62 → 2123.80] you know,
[2123.82 → 2124.76] it's hard coded.
[2124.90 → 2126.52] So if the thing's in C99 mode,
[2126.58 → 2128.36] then it had better produce the exact parse tree.
[2128.56 → 2130.06] That's a great snapshot test.
[2130.12 → 2130.28] Right?
[2130.44 → 2132.52] And so I think the difference boils down to those things.
[2132.62 → 2135.36] It has to be about something that actually is,
[2135.36 → 2136.96] you know,
[2136.98 → 2137.88] not going to change.
[2137.98 → 2138.92] I'd impotent to the
[2138.98 → 2140.32] to the release of the project.
[2140.44 → 2142.42] Otherwise it's a limited time test,
[2142.50 → 2143.34] but you know,
[2143.38 → 2144.42] that's just how it is.
[2145.08 → 2146.82] So probably also the scope of the breaking,
[2146.94 → 2147.14] right?
[2147.16 → 2150.66] If only 10% of your golden is invalid because you made this change,
[2150.66 → 2154.80] that's a lot different from a hundred percent of your goldens are invalid.
[2154.80 → 2158.48] And you have to like rework all of them because of big kind of refactors.
[2158.58 → 2159.38] That was my last,
[2159.52 → 2162.24] my last experiences that I had to do a bunch of testing against this,
[2162.24 → 2162.84] uh,
[2162.84 → 2167.28] games reporting thing at Netflix and to be able to do this auto doc and to be able
[2167.28 → 2167.56] to do it,
[2167.58 → 2170.50] I had to like to create the data model of the incoming events.
[2170.72 → 2173.94] And then they are changing the incoming events like once a week because it was
[2173.94 → 2175.02] still an exploration phase.
[2175.18 → 2175.96] So it was just like,
[2176.02 → 2176.22] well,
[2176.74 → 2178.62] not only is my input incorrect now,
[2178.70 → 2179.58] my output's incorrect.
[2179.58 → 2181.52] So I have to like change both sides.
[2181.62 → 2182.10] So I'm just like,
[2182.16 → 2183.86] I guess I'm just redoing all the things again.
[2183.96 → 2184.44] Here we go.
[2184.68 → 2187.92] And so then it just became super hard to know if I was actually right or if I
[2187.92 → 2188.58] was breaking things.
[2188.98 → 2190.32] So I think at the outset,
[2190.40 → 2191.40] I made it pretty clear.
[2191.42 → 2193.46] I don't like test different development as an idea.
[2193.46 → 2195.98] I don't like focusing the developer's attention on tests.
[2196.02 → 2198.88] I think they should understand tests and know how to deploy them smartly,
[2199.40 → 2200.48] but I don't think you're right.
[2200.90 → 2206.92] I do want to say there is a place where I do recommend literal test driven
[2206.92 → 2207.38] development.
[2207.38 → 2209.34] And it is as follows.
[2210.06 → 2216.64] That is if the programmer is finding that they are low productivity on a particular
[2216.64 → 2219.76] task and that task does not provide feedback.
[2219.76 → 2222.36] So for example,
[2222.36 → 2229.44] if you have to implement some low level feature component that has no visual output,
[2229.44 → 2231.02] no auditory output,
[2231.02 → 2232.52] no anything,
[2232.52 → 2237.02] it's just like an abstract thing that happens inside the computer.
[2237.02 → 2237.52] Right.
[2238.00 → 2239.80] Then sometimes programmers,
[2239.80 → 2243.16] like they get bored working on these sorts of things,
[2243.16 → 2250.02] but a lot of programmers will like focus on things like numbers that come out of a thing.
[2250.06 → 2250.78] Like if a thing,
[2251.02 → 2253.40] if you run a thing and the number like,
[2253.48 → 2253.82] you know,
[2254.00 → 2255.96] 37% pops out,
[2256.08 → 2261.24] suddenly the programmer's like super motivated to get it up to like 45% and 50%,
[2261.24 → 2261.82] right?
[2262.62 → 2263.88] So sometimes it's like,
[2263.96 → 2264.12] Oh,
[2264.20 → 2264.46] okay.
[2264.46 → 2266.12] If you can turn this problem,
[2266.12 → 2276.28] if you can make a test that turns whatever you're working on into something with a concrete output that you feel some reward about when it goes up or improves,
[2276.28 → 2280.16] that can be a valuable use of test driven development.
[2280.16 → 2281.98] And we do this in performance a lot.
[2282.12 → 2282.54] We'll put,
[2282.64 → 2288.04] make a little test around something that outputs things like how many cache misses did it have or how many,
[2288.04 → 2288.48] you know,
[2288.84 → 2289.14] uh,
[2289.14 → 2291.10] cycles did it take to complete or whatever.
[2291.36 → 2292.08] And it's like,
[2292.14 → 2292.36] Ooh,
[2292.56 → 2294.86] now I'm like trying to get that number down.
[2294.86 → 2299.90] And that's a lot more fun than I am just trying to make this system faster or whatever.
[2300.00 → 2302.42] So like a lot of times you can get a
[2302.52 → 2306.12] you can make it so that those things go together, and then you get the test.
[2306.12 → 2309.86] Or the good statistics gathering or whatever it is that you actually wanted anyway.
[2310.30 → 2314.50] And you get this motivation for the programmer and they all kind of work together in this nice way.
[2314.60 → 2315.92] So I just wanted to put that out.
[2315.96 → 2322.24] There's one place where I think it does kind of work to drive development by a test of some kind.
[2322.54 → 2325.88] First thing that comes to my mind is like code coverage reports.
[2326.74 → 2328.42] And you see that number really low.
[2328.80 → 2331.64] And I have the opposite reaction where I just don't care.
[2331.78 → 2332.40] And I want to quit.
[2332.40 → 2337.58] I don't think I've ever saw like a low code coverage report.
[2337.68 → 2338.14] And I was like,
[2338.28 → 2339.46] you know what?
[2339.92 → 2341.72] Today we're making that number higher.
[2341.88 → 2342.60] I'm kind of just like,
[2342.62 → 2342.94] guys,
[2343.04 → 2343.58] we suck.
[2343.82 → 2345.64] And I'm not going to help us get better.
[2346.18 → 2347.14] There's no way.
[2347.20 → 2347.48] No.
[2347.74 → 2348.20] All right.
[2348.72 → 2349.14] I mean,
[2349.14 → 2349.68] to be fair,
[2349.74 → 2352.42] if I go to a place that's like 100% code coverage,
[2352.42 → 2353.44] I also go,
[2353.64 → 2354.00] uh-oh.
[2354.70 → 2354.92] Right?
[2355.00 → 2358.96] Like I'm also kind of worried about the 100% code coverage as well.
[2359.16 → 2360.70] I'm not going to say the company I was at.
[2360.78 → 2361.48] I've been at many.
[2361.98 → 2362.32] Netflix.
[2362.32 → 2376.42] And there was a team that required 100% test coverage to the point where people were just like writing the most worthless tests just to get like this like PR bot to just shut up.
[2376.42 → 2382.42] And to make it even like funnier, there's like bugs every day, like in production.
[2382.58 → 2384.72] It's just like, I was just like, what's happening here?
[2384.92 → 2389.62] I don't know if anyone's ever experienced like 100% like test coverage quota by their team.
[2390.16 → 2390.56] Yes.
[2390.58 → 2392.08] I did it with Falk or when I was at Netflix.
[2392.20 → 2394.26] 100% code coverage bugs every day of my life.
[2394.52 → 2398.88] Oh, for Falk or, the one line production takedown.
[2402.56 → 2404.66] Wait, did you say Falk or?
[2405.22 → 2405.64] Uh-huh.
[2405.64 → 2408.24] Like the luck dragon from the never-ending story?
[2408.36 → 2408.64] Yeah.
[2410.00 → 2410.40] What?
[2410.96 → 2412.16] Why was it called that?
[2412.30 → 2413.10] You don't know what Falk or is, bro?
[2413.10 → 2413.98] Because it was named after the luck dragon.
[2413.98 → 2415.24] I do know what Falk or is.
[2415.26 → 2416.98] It's the luck dragon from the never-ending story.
[2417.24 → 2417.52] Yes.
[2417.60 → 2419.94] It was named after the luck dragon from the never-ending story.
[2420.52 → 2421.46] Tell the story, Prime.
[2421.84 → 2422.56] Tell the story.
[2422.68 → 2424.08] Tell it all, so Casey can hear it.
[2424.08 → 2424.80] And then we'll be done.
[2424.82 → 2424.84] All right.
[2424.84 → 2425.90] I'll do a quick one, Casey.
[2426.00 → 2426.56] Casey Snow.
[2426.56 → 2432.92] How it works is that you would provide effectively an array with keys in it as the path into your data model in the back end.
[2432.92 → 2435.54] So say you want videos, some ID, title.
[2435.64 → 2441.38] It would return to you the title in that kind of as a tree, videos, or as a graph, or maybe as a forest is a better way to say it.
[2441.62 → 2443.08] Videos, ID, title.
[2443.08 → 2447.44] So if you wanted, say, a list, I want list 0 through 10, title.
[2447.62 → 2452.98] It would go list 0 through 10, which would be IDs, which would then link to videos by ID, title.
[2453.08 → 2459.90] So it's kind of like a graph-like data structure that makes it so that if you make duplicate requests, it's able to go, oh, okay, I already have videos, whatever.
[2460.04 → 2461.44] I already have list item 0.
[2461.66 → 2464.06] I can kind of not request so much from the back end.
[2464.38 → 2468.84] The problem was that what happened if list 7 doesn't exist?
[2469.34 → 2469.90] You don't know.
[2470.06 → 2473.44] So we have to return something  to you that says it does not exist.
[2473.82 → 2476.88] So we return something called, like, it's a boxed value.
[2477.24 → 2478.66] It's an atom of undefined.
[2478.82 → 2482.26] It lets you know, hey, there is a value there, and the value there is nothing.
[2482.36 → 2483.44] You don't need to request it again.
[2483.48 → 2484.34] It's not going to be something.
[2484.82 → 2486.80] So we created something called materialize.
[2486.90 → 2489.90] On the back end, that means you need to materialize missing values.
[2490.04 → 2495.40] Well, what happens if you request lists 0 through 10,000, 0 through 10,000, 0 through 10,000, title?
[2495.40 → 2501.16] Well, you just created a gigantic number that were going to materialize everything for you.
[2501.52 → 2511.08] And so with one simple line of code, a while loop and bash, you can DOS, or at one point, 2016, you could have Dosed down and took down Netflix permanently.
[2511.22 → 2512.18] There was no rolling back.
[2512.44 → 2514.20] It was in production for, like, two years.
[2514.78 → 2519.72] You could do it for all endpoints, for all devices, for everything, and just it would never run again.
[2520.10 → 2520.60] And that's it.
[2520.60 → 2526.86] It was a simple while loop, and I wrote a lot of beautiful code about it, and I did a lot of beautiful stuff with it, and it was very nice code.
[2526.98 → 2531.82] And then I also discovered it and reported it, and then later on it got named the Repulsive Grizzly Attack.
[2533.12 → 2534.24] Repulsive Grizzly?
[2534.88 → 2535.24] Yeah.
[2536.76 → 2540.06] So has no one at Netflix watched The Never Ending Story?
[2540.18 → 2541.96] Shouldn't it be called The Gamers or something?
[2542.26 → 2543.26] Like, it's a movie.
[2543.36 → 2544.44] It's probably on Netflix.
[2544.44 → 2548.70] Okay, no, no, this wasn't some 9,000.
[2548.74 → 2556.56] It was a completely separate team that when they found out about it, they had to do a bunch of work, and it ended up being, you know, a fix on the Pool Gateway and all this kind of stuff.
[2556.58 → 2558.98] All right, because there are no Grizzly Bears in The Never Ending Story.
[2559.06 → 2561.98] I didn't read the original book because I think it's in German or something.
[2562.04 → 2562.38] I don't know.
[2563.04 → 2563.22] Yeah.
[2563.60 → 2572.84] Yeah, but the nice news is I originally didn't come up with the materialized idea, but I did do a lot of refactoring that while refactoring and recreating everything,
[2572.84 → 2575.02] I stopped and went, wait a second.
[2575.86 → 2577.02] Something seems funny here.
[2577.12 → 2583.72] So then I trashed staging for a day when no one could use staging for a day, and then that's when I realized we made a mistake.
[2585.40 → 2587.56] When I say we, I mean me.
[2587.90 → 2588.04] Yeah.
[2590.06 → 2590.90] And that's it.
[2591.08 → 2591.66] And he's off.
[2592.44 → 2597.38] He's like, I told my story, and I'm not participating in this podcast anymore.
[2597.90 → 2601.52] The transitions at the end of this podcast are just getting worse and worse.
[2601.52 → 2603.86] We just end stream, he walks off frame.
[2603.86 → 2604.68] We end stream?
[2605.06 → 2605.86] Look what's happening.
[2606.66 → 2608.58] All right, TJ, do you have anything you want to add to this all?
[2609.02 → 2610.42] He's phrasing my smile.
[2610.46 → 2611.14] Are we still live?
[2611.62 → 2612.00] We're still live?
[2612.52 → 2616.02] Dude, find a friend that smiles at you like TJ smiles at us.
[2616.40 → 2621.04] I think today's big takeaway is don't bring Trash Dev into a project that needs help.
[2621.28 → 2622.12] He'll just quit.
[2623.62 → 2624.06] Yeah.
[2624.60 → 2627.28] No, actually, I will help your product get better.
[2627.34 → 2627.68] Bye.
[2627.68 → 2631.18] You drive your code coverage metrics down to zero.
[2631.84 → 2631.96] Yeah.
[2632.36 → 2634.14] Code coverage is a lie anyway.
[2634.36 → 2635.22] Are we live?
[2635.56 → 2636.34] And then quit.
[2636.50 → 2637.50] Oh, TJ's back again.
[2639.18 → 2639.80] All right.
[2640.72 → 2641.12] Well.
[2641.36 → 2642.56] What is happening?
[2643.34 → 2643.90] Don't know.
[2644.24 → 2645.20] See you later.
[2647.60 → 2649.38] No blockers on my end.
[2649.38 → 2654.98] I think we had a really productive meeting today, everyone.
[2655.40 → 2655.60] Yeah.
[2655.74 → 2657.38] Everybody enjoy your weekend.
[2657.58 → 2658.86] Next quarter is going to be big.
[2659.36 → 2661.56] It's going to be the biggest quarter of our lifetime.
[2661.86 → 2662.24] Absolutely.
[2662.42 → 2663.54] We've got to hit our OKRs.
[2663.88 → 2664.10] Yep.
[2666.20 → 2667.24] Well, okay then.
[2668.94 → 2669.38] Bye.
[2669.38 → 2672.66] Gentlemen, another professional podcast from the stand-up.
[2673.32 → 2674.08] All right.
[2674.20 → 2675.54] I am ending it.
[2675.84 → 2676.10] All right.
[2676.12 → 2676.74] Hold on one second.
[2676.74 → 2678.20] Let me, I'm going to, I'm going to end the stream.
[2678.28 → 2679.94] Hey, thanks everybody for being around here.
[2680.84 → 2681.68] TJ is back.
[2681.88 → 2683.08] Big, whatever TJ is.
