[0.00 → 1.90] Hello everyone and welcome to the stand-up.
[2.04 → 3.26] I have to step away for a second.
[3.40 → 3.90] Shut up.
[4.08 → 5.60] Oh my god, dude.
[6.08 → 7.82] Classic prime moment, dude.
[8.02 → 8.22] Yep.
[9.06 → 9.82] Hey, hi.
[10.00 → 10.72] Hey, everybody.
[12.22 → 16.40] There is a very high chance I have no idea what we're talking about.
[16.96 → 19.18] There's a 100% chance I have no idea what we're talking about.
[19.18 → 21.88] The Google cloud service outage last week.
[22.34 → 23.38] Okay, so you do know.
[23.38 → 25.50] Which isn't really a security thing, but that's okay.
[25.92 → 26.18] Did you?
[26.30 → 28.24] Wait, you made a video on this.
[28.32 → 29.00] What are you talking about?
[29.00 → 29.04] I did.
[29.16 → 29.72] That doesn't mean anything.
[29.72 → 30.50] It's not security.
[30.90 → 32.12] I made a video on the switch.
[32.46 → 32.58] What?
[32.96 → 34.02] Yeah, it's not security.
[34.26 → 35.06] What's the security problem?
[35.06 → 35.90] Oh, I don't know what we're talking about.
[35.92 → 36.60] No one got hacked.
[36.60 → 37.94] Also, I did make a video on it.
[38.04 → 38.98] Just throwing that out there.
[39.04 → 41.52] Just, oh yeah, I made a little quick video on it, but I actually have no ghost.
[41.52 → 41.86] I got it.
[41.86 → 42.58] I'll carry it.
[42.64 → 43.10] It's all good.
[43.16 → 43.58] Let's do it.
[43.70 → 44.00] Let's go.
[44.06 → 44.30] We got it.
[44.30 → 44.80] We got this.
[44.80 → 45.60] We got this prime.
[46.22 → 47.44] Nothing could possibly go wrong.
[47.50 → 47.86] We're good.
[48.00 → 48.40] It's great.
[48.70 → 49.20] Step away.
[49.30 → 49.98] No problem.
[50.30 → 50.84] We got this.
[51.26 → 52.14] Go pee or something.
[52.52 → 52.68] Yeah.
[52.68 → 53.08] Okay.
[53.14 → 55.96] The reason why I got to be right back is I got to put a little bit of milk in my coffee
[55.96 → 60.70] because just a splash of milk with cacao is really delicious.
[60.82 → 62.32] I would love a coffee right now, actually.
[62.68 → 64.06] Oh, I'm on coffee so bad.
[64.46 → 64.90] Yeah.
[64.90 → 65.14] Yeah.
[65.14 → 65.54] Yeah.
[65.54 → 66.04] Yeah.
[66.04 → 66.24] Yeah.
[66.24 → 66.64] Yeah.
[66.64 → 67.04] Yeah.
[67.42 → 67.68] Yeah.
[67.68 → 68.00] Yeah.
[68.00 → 68.14] Yeah.
[68.14 → 68.50] Yeah.
[68.50 → 68.68] Yeah.
[68.68 → 69.00] Yeah.
[69.00 → 69.50] Yeah.
[69.50 → 77.92] Prime, I know that you're itching right now to do your signature opening to the extent
[77.92 → 79.50] that it exists for the podcast.
[79.94 → 85.04] I, the single greatest opener of all time for the standup, would love to start the opening.
[85.18 → 88.28] Hey, today we have a very special episode of the standup.
[88.28 → 91.82] We replaced TJ with, in fact, a smarter version of TJ.
[92.36 → 97.44] Low-level learnings, first appearance on the standup, security expert, probably Bellatrix
[97.44 → 98.56] expert as well.
[98.72 → 102.96] As always, we have Casey Moratoria and Trash Dev on here.
[103.28 → 109.06] Today we're going to be talking about a very large security incident and low-level learning.
[109.16 → 116.10] We brought him on due to all of his expertise, his good looks, his deep knowledge of C and
[116.10 → 117.50] null pointers and everything.
[117.64 → 119.64] And he's going to walk us through what's kind of happened.
[119.68 → 123.06] And we're going to talk about maybe the state of security and who knows where this is going
[123.06 → 123.34] to go.
[123.64 → 125.90] So, low-level, why don't you kick us off on this one?
[126.20 → 127.04] Let's do it, man.
[127.04 → 127.36] Yeah.
[127.54 → 133.68] So, I mean, it all goes back to 1972 when C, the programming language, was invented.
[134.24 → 137.68] And then 50 or so years later, we're still using it, which is kind of crazy.
[137.90 → 143.08] But yeah, man, last week, Google kind of took the internet offline for three hours.
[143.08 → 143.10] Oh, hold on.
[143.10 → 143.40] Time out.
[143.48 → 143.80] Time out.
[143.86 → 144.36] Yeah, yeah, yeah, yeah.
[144.36 → 147.68] You just started in 90, you started like 50 years ago and then went right up to last
[147.68 → 147.90] week.
[147.92 → 148.94] Like, what happened in between?
[149.34 → 150.70] Not a ton, honestly.
[151.02 → 151.78] Like, not a ton.
[151.90 → 154.66] Like, a couple new C standards came out and then now here we are.
[154.78 → 155.44] So that's about where it ends.
[155.44 → 156.08] People were born.
[156.08 → 157.42] Yeah, some people were born.
[158.38 → 159.92] But yeah, so Google took the internet out, man.
[159.96 → 161.34] And it's kind of crazy how they did it.
[162.12 → 166.40] It was like Thursday at like 1352 roughly Eastern time in the U.S.
[166.76 → 167.80] I have to convert that in my head.
[167.88 → 168.42] 1352?
[168.54 → 168.94] 152?
[169.16 → 169.18] Yeah.
[169.18 → 170.70] 1 p.m.
[170.70 → 171.64] He's a military boy.
[171.74 → 172.64] You just got to deal with it.
[172.72 → 173.42] 10 p.m.
[173.50 → 174.34] Pacific time.
[174.74 → 176.28] Well, I guess you route it to 2 o'clock, I guess.
[176.38 → 177.32] It's 52, but yeah.
[177.36 → 178.48] Internet went down for a little bit.
[178.86 → 182.04] And no one still to this day knows exactly what happened.
[182.18 → 186.44] But Google did put out a report that talks about what they did.
[186.44 → 192.92] The end result or the end reason was that Google published code that did not account for null
[192.92 → 193.34] pointers.
[193.94 → 198.70] And when a policy change went out that contained a null pointer in the policy change, it crashed
[198.70 → 200.84] the management plane of the Google Cloud.
[200.94 → 201.18] Period.
[201.26 → 201.62] Full stop.
[201.70 → 202.28] That's what happened.
[202.28 → 204.14] Absolutely nuts.
[204.44 → 204.66] Classic.
[204.66 → 205.50] Crazy stuff.
[205.66 → 206.70] Classic Google move.
[206.98 → 211.78] And the irony in all of this is that Google is a company that runs the OSS Fuzz Project,
[211.90 → 213.46] which is open source software fuzzing.
[213.56 → 220.00] So literally what they have is a data centre full of machines that fuzz open source software
[220.00 → 222.82] to find memory corruption vulnerabilities in them, right?
[222.86 → 225.18] This is a project Google has been sponsoring for a very long time.
[225.18 → 232.54] So the palpable irony in Google releasing software internally to their own management plane that
[232.54 → 236.84] had a memory issue and not like a heap overflow or a race condition, something a
[236.84 → 240.90] little harder to detect, something as simple that you could like lint with like a failing
[240.90 → 241.88] to check a null pointer.
[242.56 → 246.44] Crashing the Internet is just some of the craziest news I've seen in a very long time.
[246.84 → 248.56] Can you rewind a little bit?
[248.80 → 248.94] Yeah.
[248.96 → 251.74] You said two things that I think probably need a bit of explaining.
[251.74 → 255.32] One, maybe give like a quick overview of what a memory buzzer is.
[255.46 → 258.96] And then two, you said that nobody knows what happened, but Google released a port.
[259.04 → 261.22] Are you saying that Google knows what has happened?
[261.34 → 263.30] They're just not telling people what has happened.
[263.76 → 265.36] But now what happened?
[265.56 → 266.02] I don't know.
[266.12 → 267.76] Did you push on a Friday?
[268.04 → 268.36] Never.
[268.56 → 269.44] We're going to figure this out.
[269.72 → 271.26] How are we going to figure this out?
[271.50 → 272.28] That is your broad stone.
[273.02 → 273.56] Do you guys need the wheel?
[281.74 → 283.58] New Vim config.
[283.96 → 285.04] That makes sense.
[285.08 → 286.28] I'm going to spend a couple of hours with factory.
[286.52 → 287.18] I'll beat the plugins.
[291.04 → 292.52] Don't guess where your issues are.
[292.70 → 295.22] You can see exactly where they are happening with Sentry.
[295.52 → 298.82] Get all the context you need to debug any problem because code breaks.
[298.90 → 300.82] So fix it faster with Sentry.
[302.16 → 306.52] Operationally internal to Google, we do not know how that code got out, right?
[306.52 → 312.48] Like, was the code pushed through CCD and, like, it failed the test, and they just said roll with it?
[313.16 → 315.66] Was the code vibe coded and no one really checked?
[315.74 → 321.32] Like, there's a lot of, like, weird if ANDs that could be happening with that code that caused it to get published in the state that it was.
[321.40 → 322.00] That's a little weird.
[322.10 → 323.70] That's what I mean by, like, no one knows what happened.
[324.04 → 325.28] We know that there was a null pointer.
[325.38 → 327.34] We know that that was the reason why it crashed.
[327.98 → 330.54] But how that code got released is still kind of, like, ambiguous.
[331.04 → 334.30] And then Casey and I were talking previously about, like, when CrowdStrike had their incident.
[334.64 → 334.86] Right.
[334.86 → 338.62] They released, like, a 50-page report that said, like, hey, here is exactly what happened.
[338.98 → 340.18] Here is why the code went out.
[340.28 → 342.28] You know, sorry, it won't happen again.
[342.42 → 342.86] Ada, Ada, Ada.
[343.00 → 344.12] Google has not done that yet.
[344.48 → 347.80] And amusingly, these two exploits were, exploits is the wrong term.
[347.86 → 347.98] Sorry.
[348.08 → 349.98] These two, like, they're just crashes.
[350.16 → 351.92] Like, nobody exploited anything, right?
[352.24 → 352.38] Right.
[352.78 → 355.10] But they're actually kind of similar.
[355.54 → 362.18] The CrowdStrike one and the Google one were both, like, we have some config stuff that can happen, essentially.
[362.18 → 369.54] Like, there's some kind of, like, code that's being driven off of, like, some data that goes into the code that tells it, like, what it should do.
[369.62 → 369.82] Right.
[369.82 → 381.44] And in the CrowdStrike case, that was the problem is that, you know, the in-production was the first time it got fed the correct data, like, to make the bad case happen.
[382.02 → 383.60] And the same was true of Google, apparently.
[383.72 → 387.48] It's, like, basically this code, it will only hit its null pointer case.
[387.56 → 389.82] I mean, trying to read between the lines of the thing that they published.
[389.82 → 391.78] Because, again, they didn't show the code like CrowdStrike did.
[391.92 → 398.04] But it only gets to the null pointer case, apparently, if you pass it a certain configuration for the quota system.
[398.20 → 401.92] Like, it was in the like, thing that's trying to check quotas or this sort of thing.
[401.92 → 404.86] So it's the same exact kind of pathologies.
[405.04 → 413.92] Like, there's a type of data that if you fed it to this thing, it doesn't do the right, like, checking of that data to make sure that it won't go into some bad code path.
[414.38 → 415.78] And off you go.
[415.92 → 421.80] And so they're kind of actually somewhat similar, at least from what Google actually said, which, again, they didn't include the code.
[421.92 → 423.08] So it's, like, who knows?
[423.20 → 424.84] They didn't even say what language it was in, correct?
[425.70 → 426.28] They didn't.
[426.34 → 428.98] They said null pointer, but that could be C, C++, whatever.
[429.26 → 429.70] Or Go.
[430.10 → 431.76] Go has null pointers, I think, too, right?
[432.02 → 432.18] Yeah.
[432.60 → 433.20] Yes, they do.
[433.64 → 434.36] So famously.
[434.72 → 435.26] Hold on, time out.
[435.30 → 436.82] Did we explain what a memory buzzer is?
[436.96 → 438.06] Yeah, I can talk about that.
[438.28 → 441.56] So basically, a memory buzzer, it's basically a picture.
[441.68 → 445.08] It's like a unit test where you're trying to get as much code coverage as possible.
[445.08 → 455.54] But instead of, like, traversing down paths with, like, the sane data shape, you're literally mutating the data to try to find edge cases in your code that are not accounted for in testing.
[455.98 → 465.22] So, like, if I have an HTTP buzzer, my initial corpus, my first seed is going to be HTTP, you know, like a get request, right?
[465.22 → 468.22] And what the buzzer will do is it'll pick a random byte in that packet.
[468.92 → 470.36] It'll mutate it by, like, flipping a bit.
[470.48 → 472.44] It'll, like, make an integer, a negative integer.
[472.60 → 473.52] It'll do some mutation.
[473.52 → 479.68] And then it'll run that request on the service and see, hey, does that input generate new coverage?
[479.68 → 485.04] If it does, okay, that is a new piece we have to add to the corpus to future mutate to find new code paths.
[485.06 → 489.06] And you do that trying to enumerate the entire code base from a coverage perspective.
[489.62 → 499.20] And so what a memory buzzer would have done if they had fuzzed this software, and, again, like, this is the science behind getting coverage in fuzzing is, like, cutting-edge technology right now.
[499.26 → 501.74] No one has it, like, figured out, but Google is very good at it.
[501.74 → 507.64] But a buzzer would have very quickly found, like, oh, if this field is zero, it crashes the program, right?
[507.64 → 511.52] So it kind of implies that the software was not fuzzed, at least long at all.
[511.94 → 515.04] To Casey's point, this code had actually been public or not public.
[515.10 → 518.92] It had been released since, like, May of this year, like, May 29th, I think.
[519.24 → 526.08] And because they had never pushed a policy change that exercised this code path, it just never was seen to crash.
[526.32 → 528.70] So either they didn't test it, they didn't fuzz it.
[528.70 → 532.70] Nothing really was done to, like, try to exercise this code until it got hit on June 12th.
[533.50 → 546.42] And it sounded like, too, that the fuzzing would not have had to have been very complicated because the way they made it sound, anyway, in the very terse description, was that, like, the kind of thing that would crash this was just something with some missing fields.
[546.74 → 548.58] They just used the phrase missing fields.
[548.58 → 554.58] So, you know, a basic fuzz tester would probably try a bunch of different field combinations with some missing.
[554.82 → 557.06] Like, that's not a weird thing to have fuzzed.
[557.30 → 559.28] And apparently that was not done, I guess.
[559.36 → 561.40] But again, because there's so little information, who knows?
[561.48 → 566.16] Maybe it was a very strange, like, really unusual combination of missing fields that no one thought to try.
[566.24 → 566.80] Who knows?
[566.80 → 567.20] Yeah.
[567.40 → 569.42] What I would imagine is that, again, all speculation.
[569.58 → 570.10] I don't work at Google.
[570.22 → 570.70] I have no idea.
[571.28 → 576.40] It is likely they're passing around either a JSON blob or a YAML file.
[576.82 → 587.06] And then, like, if you use some YAML object that exists but a subfield in that YAML object does not exist, that will populate a null pointer that then gets read.
[587.06 → 593.30] And the problem with that is, like, fuzzing binary data is very easy because, like I said, you flip a bit.
[593.60 → 596.22] You make an integer sign or something like that.
[596.60 → 602.82] Fuzzing data with a sane grammar, like JavaScript, for example, or YAML, much more complicated.
[603.02 → 614.16] So it just – the fact that it was not fuzzed implies that it was some, like, human-readable grammar and, like, a config spec that just didn't get tested, which is, again, for Google, it's just crazy.
[614.16 → 616.76] But also, I could totally see why that would happen operationally.
[617.06 → 620.68] So I have a question.
[620.96 → 621.42] Yeah, what's up?
[621.74 → 627.82] So I don't know much about the outage because I was at a conference, so I didn't really see the internet go out if it actually did at all.
[628.20 → 631.82] So when you say they crashed the internet, to me, that just sounds like a really bold claim.
[632.10 → 637.30] Like, when we say they crashed the internet, like, what is, like, the impact here?
[637.48 → 640.60] And, like, what was the collateral – like, what happened exactly?
[640.60 → 654.70] Yeah, so basically, when this outage happened, what really ended up occurring was that the binary that was responsible for doing quota and authority checks or, like, authorization checks on requests, like, crashed in all regions of the world, right?
[655.00 → 659.88] So basically, any call to a Google Cloud Platform API would just 503.
[659.88 → 661.14] Like, you could not do anything.
[661.26 → 664.64] So if you're – like, my course website, not a plug, this is, like, real life.
[665.52 → 666.70] What's the course website again?
[666.88 → 667.72] Low-level academy.
[667.90 → 669.04] If you want to learn C, Ross, whatever.
[669.38 → 670.24] Yeah, just cheeky little plug.
[670.26 → 670.98] Clubs are allowed here.
[671.08 → 671.74] Low-level academy.
[671.82 → 672.28] Clubs are allowed.
[672.28 → 677.34] No, but the reason why I'm saying this is that I depend – I depend on Google OAuth, right?
[677.42 → 681.28] And so every time my site receives a 503 from an API, I get an email.
[681.72 → 690.04] And so during this outage, because the OAuth provider was returning 503s, I got, like, 120 emails in 30 minutes being, like, you know, the internet's down.
[690.04 → 705.14] So the issue was every – like, basically every site on the internet now depends on Google in some form or fashion through OAuth, OAuth, through the actual, like, compute providers, a bunch of other stuff that I don't use or don't care to use.
[705.22 → 713.14] But basically, because Google in its entirety went down, it kind of, like, brought the internet down with it, which is very, like, counterintuitive to, like, the design of the internet.
[713.26 → 718.58] It's meant to be, like, a decentralized mesh of nodes that if one goes down, routing exists, and you can kind of route around it.
[718.58 → 730.00] But it kind of just goes to show that we have this really weird dependence on, like, single points of failure in modern cloud architecture, which is kind of scary, I think, from a, you know, a cyberattack perspective, right?
[730.02 → 738.48] It's kind of like how when Dan went down, or Dan, however you want to pronounce it, in 2016, like, again, DNS, core protocol to the internet, there was, like, one major provider that went down because of a botnet.
[738.62 → 741.14] And when that went down, it took the whole internet down with it, so.
[741.86 → 742.76] Cyberdyne, did you say?
[743.14 → 744.40] No, just Dan, D-Y-N.
[744.50 → 745.46] Okay, okay, okay.
[745.46 → 746.54] Yeah, sorry, cyberattack.
[746.70 → 747.84] The provider is called Dan.
[747.84 → 749.76] I don't know if it's Dan or Dan.
[749.76 → 750.74] It's a Terminator joke.
[750.96 → 752.68] He's going Skynet on us.
[752.92 → 753.72] Sorry, sorry.
[754.04 → 755.98] I'm a little too young for Terminator, I think.
[756.06 → 756.46] I'm 30.
[756.56 → 757.02] No way.
[757.56 → 757.84] Yeah.
[758.04 → 759.24] Shut up, you're not too young for Terminator.
[759.26 → 760.84] You're supposed to pass already dead.
[760.94 → 762.80] Wait, what was the first, when did the first Terminator come out?
[763.14 → 764.24] Like, 78, I think.
[764.32 → 764.98] Oh, was it that old?
[765.10 → 767.32] No, 80, 81 or two.
[767.34 → 767.90] I thought it was 80s.
[768.92 → 769.62] Terminator 1?
[769.80 → 770.44] Nah, I don't think so.
[770.54 → 770.98] I think I'm right.
[770.98 → 772.02] Was it late 70s?
[772.02 → 772.66] No, he wasn't.
[772.66 → 773.82] Terminator 2 is the best Terminator.
[773.82 → 775.00] Okay, 84, you're right, it's 84.
[775.00 → 777.24] It's a little older.
[778.04 → 780.26] The problem is, you can name any movie.
[780.72 → 782.32] I probably haven't seen it.
[782.44 → 783.80] Do you just name it like movies?
[784.32 → 784.76] Lord of the Rings?
[784.92 → 785.60] Okay, those I've seen.
[786.30 → 787.48] Oh, got him.
[788.06 → 788.98] But I'm a nerd.
[789.12 → 789.86] Any other movie.
[789.98 → 790.16] Fine.
[791.00 → 792.34] Really, just any other movie?
[794.04 → 794.88] Star Wars.
[795.40 → 796.02] Star Wars.
[796.02 → 796.30] Gladiator.
[797.58 → 798.22] Fine, Star Wars.
[798.30 → 799.04] Those are the only two.
[799.04 → 799.60] Other than that.
[800.90 → 801.98] You guys are bad.
[802.42 → 802.96] That was it.
[803.52 → 803.88] Love it.
[804.36 → 806.34] Anyway, I guess we could just move on, Mr.
[806.40 → 808.56] I've never seen any movies except for all the ones we named.
[809.20 → 809.60] Exactly.
[809.86 → 810.46] Of the two?
[810.60 → 810.82] Yeah.
[812.10 → 815.60] Before, before, maybe we should just stay off-topic.
[815.72 → 818.04] I was going to bring us back on, but this is kind of good.
[818.40 → 819.40] Name a third movie.
[819.52 → 820.54] Someone name a third movie.
[820.76 → 821.94] I went with Gladiator.
[822.38 → 823.18] I have not seen that.
[823.66 → 824.54] Yeah, that's a little more.
[824.54 → 825.46] Saving Private Ryan.
[826.02 → 828.04] No, first off, Gladiator is not rare.
[828.16 → 830.10] Wait, wait, okay, whoa, whoa, whoa, whoa, whoa, whoa, stop.
[830.10 → 831.66] Gladiator is one of the best movies ever.
[831.92 → 832.18] Really?
[832.18 → 832.62] Stop and stop.
[832.84 → 835.42] How did you only see half of Saving Private Ryan?
[835.42 → 836.16] Can I tell you why?
[836.26 → 836.78] Can I tell you why?
[836.90 → 837.20] Yes, please.
[837.24 → 839.28] When I was growing up, big paintball kid.
[839.32 → 840.26] We loved to play paintball.
[840.36 → 842.54] We would go drive an hour south to go play paintball.
[842.64 → 844.94] It's called Cousins Paintball in Tom's River, New Jersey.
[845.24 → 850.18] And every time we went, we would hype ourselves up by watching the Normandy invasion scene.
[850.28 → 852.50] We would get like an hour into the movie.
[852.50 → 853.12] That is very sick.
[853.12 → 854.00] And then we would be done.
[854.16 → 854.46] Yeah, dude.
[854.68 → 855.24] That's what we did.
[855.92 → 857.24] That is dark.
[857.60 → 859.84] Dude, I mean, that's what we would do.
[860.04 → 861.56] Dude, we were like 12-year-old kids, man.
[861.58 → 862.60] We had to get hyped up somehow.
[862.90 → 865.90] And that's how I knew I would have a job in security someday.
[865.90 → 866.20] There's literally people getting blown up.
[867.08 → 867.36] What?
[868.42 → 870.38] We were going to war with paintball, man.
[870.46 → 871.18] Oh, yeah, we were teenagers.
[871.34 → 872.16] So, I mean, like, give me a break.
[872.22 → 873.66] But, yeah, so that's why I've only seen half of it.
[873.66 → 876.32] Because we would get into the Normandy invasion scene, get like an hour into the movie,
[876.40 → 876.94] and then it'd be over.
[877.06 → 877.92] And we'd be there.
[878.66 → 880.70] He's like, I still don't know what happened in World War II.
[880.80 → 881.20] Who won?
[881.30 → 881.96] Yeah, I mean, did we win?
[882.06 → 882.72] Shit, I have no idea.
[882.92 → 884.20] It looked pretty bad from that.
[884.36 → 884.68] I didn't even know.
[884.68 → 885.64] We probably were going to.
[885.74 → 885.92] No spoilers.
[886.00 → 886.70] No spoilers, please.
[887.02 → 887.60] Yeah, no spoilers.
[887.70 → 890.06] And apparently, like, Oppenheimer, we had like a big bomb or something.
[890.16 → 890.72] That's crazy, too.
[890.74 → 891.68] Yeah, when did that even happen?
[891.76 → 892.24] Who knows?
[892.24 → 892.32] I know.
[892.44 → 893.24] It's confusing.
[893.50 → 894.02] Very confusing.
[894.14 → 894.28] All right.
[894.40 → 896.62] Well, let's get back on topic here.
[896.86 → 904.80] Okay, so philosophically, are you saying that all those times I've been told that rolling my
[904.80 → 910.92] own auth is for losers and people who want security issues may not have been correct?
[911.16 → 911.64] Is that true?
[911.70 → 912.32] Is that what you're saying?
[912.68 → 913.30] Low-level learning?
[913.46 → 914.76] Chief expertise of security?
[915.40 → 917.84] I mean, chief expertise in cloud, incorrect.
[918.14 → 918.58] No.
[918.96 → 920.00] But yeah, I don't.
[920.50 → 921.38] It's tough, right?
[921.38 → 926.78] It's just everything you do anywhere, including in programming, including in, like, system
[926.78 → 929.12] architecture, is a choice in risk.
[929.20 → 929.94] And what is risk?
[930.22 → 934.34] It's the probability that a thing will occur, and if it occurs, what happens, right?
[934.34 → 935.08] How bad is it?
[935.42 → 940.44] The probability that Google Cloud goes down all the time is fairly low, so not impossible,
[940.70 → 941.90] but, like, you know, it could happen.
[942.24 → 945.30] So I don't think it's bad if you use Google Auth.
[945.44 → 946.52] There's nothing wrong with that.
[946.56 → 948.12] But you have to consider that in your calculus.
[948.12 → 951.10] Like, well, you know, how mission-critical is my software?
[951.26 → 955.82] If Google goes down, which it definitely could, are people going to get hurt kind of thing?
[955.86 → 960.02] Like, maybe medical providers shouldn't be using Cloud Auth for their stuff if it's,
[960.06 → 962.10] you know, a complete necessity that they get into it.
[962.38 → 963.96] So I don't think it's bad to roll your own auth.
[964.00 → 967.22] I just think you have to do the math on what makes sense for your application, you know?
[967.88 → 974.00] It's kind of rough, too, I think, like, at least from a user's perspective.
[974.00 → 978.08] Or, I mean, for when I say user, I mean someone who uses, like, cloud services.
[978.78 → 984.22] It's a bit tough, too, because one of the things that seemed to get exposed by this particular crash,
[984.26 → 987.40] at least when I was kind of looking at people's reports on it,
[987.76 → 994.76] was that a lot of people didn't seem to know or maybe could not have known
[994.76 → 998.60] that they were relying on someone who was relying on Google.
[998.60 → 1003.12] So I could even imagine somebody was like, oh, don't worry, we, like,
[1003.24 → 1006.86] use two different storage providers or two different auth providers,
[1007.00 → 1012.88] not realizing that actually they will both go down if Google's quota server goes down, right?
[1013.22 → 1015.78] And so on of the things that kind of occurred to me during this crash,
[1015.90 → 1018.94] not being a security professional, so I don't really have to think about this for my job,
[1019.02 → 1022.38] but it just was kind of floating around in my head, was I was like, you know,
[1022.44 → 1026.32] it probably should be a requirement somewhere for these kinds of services
[1026.32 → 1032.80] that you get the diagram, where it's like, what are all the things that you actually call out to?
[1033.00 → 1036.68] So that I can look, and if I want to do a redundant thing,
[1037.00 → 1040.04] I know that I need something where the Venn diagrams don't overlap.
[1040.04 → 1042.66] Because if at the end of the day all these people call AWS,
[1043.40 → 1045.00] then really I have no redundancy at all.
[1045.08 → 1048.02] Because as soon as AWS goes down, all my stuff goes down or whatever, right?
[1048.38 → 1050.86] And I realize no one's probably thinking that way.
[1051.04 → 1055.18] Like, people, like, the web is not really about uptime, it doesn't seem.
[1055.18 → 1058.34] But, like, let's suppose you were, it would be interesting to be able to get that
[1058.34 → 1063.26] so that you could just kind of know, okay, if I use this and this, they're fairly disparate.
[1063.36 → 1066.02] Whereas if I use this and this, they share a bunch of services,
[1066.02 → 1068.86] so there's probably no point because I'm not really getting any redundancy.
[1068.96 → 1070.04] Does that make sense what I'm saying?
[1070.08 → 1071.10] Yeah, it makes sense.
[1071.42 → 1074.88] But I do want to throw something in here really quickly before an actual expert speaks.
[1075.32 → 1078.74] Is that, Casey, it sounds like you're getting dangerously close to us drawing UML,
[1079.26 → 1083.28] which just generally speaking here at the startup, we're very against UML.
[1083.28 → 1086.90] So that already sounds like, hey, we just need, like, a universal language for modelling
[1086.90 → 1088.60] all the services and their dependencies.
[1089.14 → 1090.18] You want Grady Booch on here?
[1090.24 → 1091.64] You got to Book it up.
[1091.78 → 1094.18] I don't want Book on here talking about it.
[1094.18 → 1095.00] Book is coming on.
[1095.22 → 1096.28] I'm going to call him up.
[1096.34 → 1098.98] I don't know him, but I'll, you know, call him up randomly.
[1099.52 → 1100.16] Hey, Grady.
[1100.62 → 1101.88] What's going on, man?
[1102.08 → 1106.34] You don't know me, but I got this podcast that no one wants you on, apparently.
[1106.52 → 1107.12] Could you come on?
[1107.42 → 1107.58] Yeah.
[1107.58 → 1112.66] Okay, well, no, I'm not talking about a UML diagram, but I guess I am sort of scarily
[1112.66 → 1114.84] talking about maybe, like, what do they call this?
[1115.06 → 1116.90] A systems architect diagram?
[1117.06 → 1117.56] What do they call it?
[1117.68 → 1120.72] That little thing where they draw a bunch of little cloud shapes, and then they write
[1120.72 → 1122.30] a name in it, and then there are arrows.
[1122.96 → 1126.16] I mean, I don't actually need that, because I just need the list, right?
[1126.20 → 1130.26] I just need to know, like, what main services, you know, are you depending on or something
[1130.26 → 1130.72] like that.
[1130.72 → 1135.54] But I do think that would be interesting to know just from an architecture standpoint,
[1135.70 → 1140.68] because it's like, if you're thinking of this service as just an endpoint you connect
[1140.68 → 1144.10] to, and so you're just thinking, what is the chances that that goes down?
[1144.66 → 1149.40] You may not realize that really that and some other thing, they will go down at the same
[1149.40 → 1152.42] time if this other third service they both depend on goes down.
[1152.84 → 1157.12] And that's, like, to the point Low Level was just saying about, like, calculating that
[1157.12 → 1157.44] risk.
[1157.74 → 1160.32] That's an important part of the risk calculation, right?
[1160.32 → 1164.06] You have to know which things are independent, because, like, the chance that Amazon and
[1164.06 → 1166.44] Google have an outage on the same day is pretty low.
[1166.64 → 1170.46] But if actually they're secretly both using each other's stuff, it's very high.
[1170.54 → 1172.40] And you need to know the difference between those two things.
[1172.46 → 1172.80] That's all.
[1173.24 → 1173.38] Yeah.
[1173.48 → 1177.20] I mean, you saw that when, like, as a result of this, Google had an outage, but it also
[1177.20 → 1178.98] caused Cloudflare services to go down.
[1179.16 → 1180.12] I was just about to ask this.
[1180.16 → 1180.82] How did that happen?
[1180.90 → 1181.40] What was this?
[1181.44 → 1185.48] Because I just, I was, I guess I was a bit shocked when Cloudflare was reporting things going
[1185.48 → 1188.68] down afterwards, because I heard this was, like, a Google-related thing.
[1188.88 → 1189.14] Yeah.
[1189.14 → 1193.98] And so I was very confused as to how the other services went down.
[1194.30 → 1198.92] They have this worker service thing they do, and it relied on Google Cloud, apparently.
[1199.76 → 1201.06] Oh, were they actually related?
[1201.62 → 1203.20] Yes, I believe that was the case.
[1203.46 → 1203.92] I thought it was.
[1203.96 → 1206.28] So that's the only outage I heard of was the Cloudflare one.
[1206.36 → 1208.36] So I didn't realize they were kind of, like, one and the same.
[1208.36 → 1208.84] I think they are.
[1208.84 → 1211.98] Which is hilarious, because at the conference, we were at a Cloudflare booth, and we were,
[1212.06 → 1213.14] like, showing them the status.
[1214.06 → 1214.98] Like, hey, you guys are down.
[1215.10 → 1217.06] And we just, like, dropped the bomb on them.
[1217.06 → 1221.46] At Render ATL, you were literally walking up to people who were sweating bullets.
[1221.60 → 1223.42] I think Hacksaw did it.
[1224.34 → 1225.04] You're damn.
[1226.14 → 1228.76] Hey, man, your entire service is down.
[1228.84 → 1229.70] Have a nice conference.
[1230.44 → 1232.90] Sorry, I'm looking at the report by Cloudflare.
[1233.42 → 1236.04] Cloudflare's report went a lot more in detail, too, than Google's did.
[1236.04 → 1239.18] So it looks like, yeah, Casey said workers, as well as, so what is it?
[1239.58 → 1246.94] Workers, warp, access gateway, images, stream, workers' AI, turnstile, auto-rag, I don't know what that is, and Era.
[1247.20 → 1253.82] So there's, like, a ton of services are downstream dependent on Google at what you would call, you know, a CSP, right?
[1253.82 → 1254.52] A cloud service provider.
[1254.70 → 1262.74] Which is just, again, to Casey's point, like, you can't make a sane risk calculus if you don't know, like, the probability and the outcomes of things happening.
[1262.74 → 1270.14] So, like, if Google is, like, the core, call it centre of gravity, right, of all of these things, if it goes away, what happens?
[1270.30 → 1275.10] You know, because you're not exposed to that, you can't make a good call off of that.
[1275.28 → 1277.38] I have a question for you, Low Level.
[1277.66 → 1277.98] What's up?
[1278.34 → 1279.48] So, obviously, like—
[1279.48 → 1280.88] You say your question, Trash.
[1281.10 → 1282.54] I'm going to say my question, all right?
[1282.54 → 1282.84] You ready?
[1283.04 → 1283.72] Three, two, one.
[1285.00 → 1285.40] Hold on.
[1286.12 → 1286.48] Articulating.
[1286.76 → 1287.08] Articulate.
[1287.22 → 1287.38] Okay.
[1287.68 → 1289.84] So, let's picture, like, a big company.
[1290.28 → 1290.46] Yeah.
[1290.46 → 1291.64] Like Amazon or something.
[1292.06 → 1292.20] Yeah.
[1292.74 → 1293.04] Yeah.
[1294.22 → 1295.78] Let's say you were, like, Netflix.
[1296.04 → 1297.62] Let's say you should pick a random company.
[1297.78 → 1298.94] It's, like, Netflix, let's say.
[1298.94 → 1302.08] I was thinking about this question for, like, 10 minutes, and it's just, like, okay, okay, okay, okay.
[1302.48 → 1306.20] Let's just picture I'm, like, Mr. Amazon, and I have a big company.
[1306.34 → 1307.34] It's so many teams.
[1307.38 → 1314.28] It's hard for me to find, like, which team is, like, is actually dependent on something that could actually, like—like, the dependency waterfall, right?
[1314.28 → 1323.04] Like, how do I—like, when you're consulting or have you seen this in practice, like, how do companies approach this, like, to know that you're, like, the single domino?
[1323.12 → 1326.18] Like, if you fall, we're all, like, fucked, right?
[1326.28 → 1326.84] Like—
[1326.84 → 1327.02] Yeah.
[1327.02 → 1333.68] Because it seems like when things like this happen, it's clearly, like, not in anyone's, like, peripheral, right?
[1333.76 → 1334.22] I don't know.
[1334.28 → 1334.42] Yeah.
[1334.42 → 1336.50] I'm going to say I don't have a good answer to this.
[1337.42 → 1346.42] I've worked at big places, and I've worked at small places, and inevitably what happens at companies that get big is their knowledge management solutions begin to suck very bad.
[1346.92 → 1355.24] And people in what you would call, like, principal engineering positions know less and less about, like, the actual principal engineering concepts of the architecture.
[1356.10 → 1362.10] And so at the end of the day, like, nobody probably knows the totality of, like, what you depend on.
[1362.18 → 1363.54] And I'm not sure if there is a good answer.
[1363.54 → 1373.38] I mean, I think the real answer is, like, you have to have a single guy that probably knows the entire setup and have, like, a good place that everyone can go reference and see, like, kind of what Casey said, like, the UML diagram of the architecture, right?
[1373.40 → 1375.48] Like, hey, we depend on Google here, here, here.
[1375.54 → 1377.40] If it goes down, we can make this risk calculus.
[1377.94 → 1379.54] But there really isn't a good answer to this.
[1379.58 → 1383.18] It's probably why this—not that it keeps happening, but, like, that this is able to happen.
[1383.24 → 1387.12] Because no one's really aware how it all kind of glues together.
[1387.34 → 1391.64] It's hard, especially at a company as big as Amazon or Netflix, potentially.
[1391.64 → 1394.34] Just pick a random company.
[1394.80 → 1396.52] A random—just completely random.
[1397.18 → 1398.78] So question for Prime.
[1398.88 → 1400.22] So obviously we have, like, Chaos Monkey.
[1400.34 → 1402.38] Is Chaos Monkey kind of, like, in the same spirit of—
[1402.38 → 1404.14] I don't really know what it does at a low level.
[1404.60 → 1407.00] I'll tell you what, Chaos Monkey, Chaos Kong, and Chaos Gorilla.
[1407.18 → 1408.52] Or Chaos Gorilla, Chaos Kong.
[1408.58 → 1409.42] So we have three of them in Netflix.
[1409.42 → 1411.36] I had no idea there was three of them.
[1411.64 → 1411.74] What?
[1412.44 → 1413.90] I got to tell you about Netflix.
[1414.02 → 1414.94] That's who work there, and I don't.
[1414.94 → 1422.38] So at—so Chaos Monkey, what it would do is actually target an individual instance on Amazon, and it would kill that individual instance.
[1422.90 → 1433.82] And so that way it's kind of to prevent any sort of, like, stateful operations between two separate services where I'm caching—like, I'm doing some sort of extracurricular caching and creating some sort of weird state dependency.
[1433.82 → 1439.22] It will start just randomly killing services, and that runs in production every single day, as far as I know, at Netflix.
[1439.80 → 1443.84] Chaos Kong or Chaos Gorilla will take down an entire service.
[1443.94 → 1445.96] That's why we have something called Blue Services at Netflix.
[1446.08 → 1451.18] So if you look into Blue Services, that's, like, how we do a lot of default responses and things like that.
[1451.20 → 1454.40] So if a service goes down, you're able to have some form of data coming up.
[1454.46 → 1455.70] That's why we have a default Lollop.
[1455.70 → 1463.30] Because if you can't reach GPS or map or, you know, all the things that go into creating, there's, like, Pitcher.
[1463.48 → 1464.08] There's Rex.
[1464.18 → 1465.80] There's all those services all together.
[1465.88 → 1472.20] If one of them goes down, then you get what is the default Lollop, which is, like, the latest known, highest-ranking videos that will all come down.
[1472.28 → 1475.80] So you'll get, like, Stranger Things right off the rip, even if you've seen it, and there's no new episode.
[1475.80 → 1483.76] Just to translate this for Prime, using knowledge I gained from Prime Stream, they used the word Lollop to mean list of movies, I believe.
[1483.90 → 1485.08] I didn't know that for the longest time.
[1485.08 → 1491.82] Yes, but now we technically are a Lollop, which is a list of recommendation objects for movie objects.
[1491.92 → 1492.28] Okay.
[1492.52 → 1492.84] That's Lollop.
[1492.84 → 1493.50] And it's a new one.
[1493.52 → 1494.38] I can explain that for another one.
[1494.46 → 1496.18] I actually was the first person to implement that.
[1496.42 → 1498.74] It was very tricks, but we got it done.
[1499.10 → 1503.32] Anyway, so with all that, then Chaos Kong, which are you will see emails about that.
[1503.32 → 1506.34] So if you just search in your email Chaos Kong, it usually runs on a Wednesday.
[1507.04 → 1511.42] And what will end up happening is that we'll actually take down an entire region.
[1511.86 → 1513.16] So not just a specific service.
[1513.16 → 1520.42] This will actually take down U.S. East 1 or U.S. East 2 or West 1 or somewhere in EU, and it will be run in production.
[1521.20 → 1526.74] And usually it's for like one or two hours to make sure that if some region goes down, Netflix continues to operate correctly.
[1526.84 → 1527.76] So those are the three levels.
[1527.76 → 1539.00] And so this doesn't help because the problem is that if every single one of these services has some sort of dependency, say, on Google, you can't take down a region to test this because you don't take down a region.
[1539.10 → 1543.74] You're taking down an external service, which would crash every single subservice, which would take down all regions.
[1544.20 → 1544.26] Right.
[1544.26 → 1546.06] And so there is no overflow mechanics.
[1546.30 → 1559.26] So very interesting thing to do a Chaos Monkey with, which is to kill that service or a Chaos Kong, at least, would be to kill that entire service for a moment and see how does your system handle, say, a Google going down or a something.
[1559.94 → 1567.68] But then you don't also know, like you said, like no one would know that Cloudflare was going to get taken down because Google didn't access to a nil pointer.
[1567.68 → 1568.88] I have an idea.
[1569.28 → 1569.48] Yeah.
[1569.80 → 1570.70] I have a great idea.
[1570.78 → 1572.22] You guys can have this for free at Netflix.
[1572.54 → 1573.54] I'm just giving this to you.
[1573.60 → 1574.48] I'm giving this one to you.
[1574.60 → 1575.64] I think he's on the same page as me.
[1575.68 → 1576.54] I'm curious what this is.
[1576.72 → 1576.94] Okay.
[1577.44 → 1578.42] I'm not on the same page.
[1578.48 → 1578.82] What's happening?
[1579.04 → 1579.68] So here's what you do.
[1580.66 → 1586.88] Because obviously you do have a problem because Netflix is like the whole point of the service is I'm supposed to be able to play movies.
[1586.98 → 1589.98] I'm supposed to be able to stream movies at home or wherever on my devices.
[1590.66 → 1592.70] And you get in this situation.
[1593.04 → 1593.92] Google Cloud goes down.
[1594.00 → 1594.72] Amazon goes down.
[1594.72 → 1595.04] Whatever.
[1595.04 → 1599.26] Whoever's storing the data goes down, I can't get the movie.
[1599.32 → 1600.02] So here's what you do.
[1600.88 → 1606.44] You get a really, and I mean blocky, compressed version of Baby Shark.
[1606.66 → 1609.70] So we're packing this thing into like a megabyte, right?
[1610.10 → 1610.38] Okay.
[1610.52 → 1618.24] And every single server node you have, no matter what it's running, keeps that one megabyte in memory.
[1618.24 → 1628.42] So that if everything goes down, Netflix will just stream Baby Shark to everyone so that at least something is playing during an outage.
[1628.58 → 1632.24] And then you can just be like, you can make up something about what happened.
[1632.32 → 1633.00] You're like, oh, sorry.
[1633.12 → 1635.38] You know, like our recommendation service is a little on the fritz.
[1635.46 → 1637.72] So it just decided that everyone wanted to watch Baby Shark.
[1637.72 → 1640.36] And then it will seem like you just have like infinite uptime.
[1640.68 → 1641.22] There you go.
[1641.42 → 1642.80] Can I tell you a fun side story?
[1642.86 → 1644.08] This is just reminding me of a side story.
[1644.34 → 1648.48] I tried to convince our marketing wing to do something kind of similar.
[1648.82 → 1649.26] Oh, really?
[1649.26 → 1650.14] In a similar vein.
[1650.24 → 1652.14] So effectively, they did this once.
[1652.20 → 1655.12] So if you look back in the day, this must be 2016, 2015.
[1655.50 → 1659.94] We actually leaked, I think, the second season of House of Cards early.
[1660.42 → 1660.78] Okay.
[1660.92 → 1662.72] And everybody was like, oh, my gosh, House of Cards.
[1662.94 → 1665.78] And then you got like for 30 minutes, it was up and people could go watch it.
[1665.80 → 1668.14] So we actually like had content that we shouldn't have had leaked.
[1668.64 → 1672.14] And so then there's all these articles written, all this hype built and all this.
[1672.52 → 1677.16] And so I actually want to – I know this is not actually related at all to your idea.
[1677.26 → 1678.42] It just reminds me of it.
[1678.42 → 1689.70] I actually – I tried to convince Netflix to leak shows more regularly just for like a half an hour because then you get all these articles written and everyone gets super hyped up.
[1689.70 → 1691.50] And it's like such a sweet way to mess with people.
[1691.66 → 1693.12] And it looks like it's an accident.
[1693.32 → 1697.80] And so you can have this whole idea of like accidental content and just be like, oh, our fault.
[1697.86 → 1699.30] You know, I didn't mean to do that one.
[1699.74 → 1702.26] And then publish like a fake apology every time.
[1702.36 → 1702.72] Right?
[1702.76 → 1706.60] It's like making up service names like our Gorgonzola service failed.
[1706.60 → 1709.86] And then they're just like they don't actually exist internally.
[1710.58 → 1710.94] Great.
[1711.14 → 1712.50] Love Galactic us.
[1712.88 → 1713.16] Sorry.
[1713.50 → 1717.48] Low level, you wanted to say something that was not my ridiculous baby shark joke.
[1717.48 → 1720.10] It sounded like you were going down the path that I was going to go down.
[1720.34 → 1720.72] But you didn't.
[1720.78 → 1721.02] It's okay.
[1721.06 → 1722.62] You went down a completely different path.
[1722.74 → 1722.94] Yeah.
[1723.06 → 1726.26] I propose chaos skiing.
[1726.40 → 1726.68] Hear me out.
[1726.92 → 1727.10] Okay.
[1727.10 → 1729.32] What you do is you – this is actually real.
[1729.48 → 1736.26] Like what you could do is you could create like basically a firewall red button layer in between a cloud service provider and like whatever service it is.
[1736.30 → 1738.30] So just like you're doing like chaos dong.
[1738.38 → 1738.68] What are they called?
[1738.76 → 1739.12] Chaos Kong.
[1739.64 → 1742.02] You know, chaos Kong attacks at Netflix.
[1742.02 → 1754.78] You could also do – and then like if it's a regional cloud-based thing, it would be chaos Kong dong or chaos, you know, if it's just for, you know, a small little service, chaos monkey dong.
[1755.04 → 1760.86] But all you're doing is you're red buttoning the cloud firewall to see like if Google goes away, what happens, right?
[1761.52 → 1763.92] My rate is roughly $1,200 an hour.
[1764.10 → 1765.42] That will be $120.
[1765.80 → 1766.98] You can bill it to Netflix trash.
[1766.98 → 1768.30] I'll give you my answer.
[1768.96 → 1780.26] Obviously, the only problem with that notion is that there's all those third-party ones like the cloud flare one that leaves your cloud or leaves your private network that you can control your whatever, however you're controlling the traffic through your private network.
[1780.68 → 1782.36] You wouldn't be able to control that.
[1782.50 → 1786.72] And so they would still remain up, which would hide where the problems were actually at.
[1786.84 → 1790.04] This is like the sole problem, which is the internet is supposed to be distributed.
[1790.20 → 1791.68] It's supposed to be the people-owned thing.
[1791.68 → 1797.06] But the reality is that the internet is largely power accumulated.
[1797.64 → 1798.36] You know, you only have a couple services.
[1798.36 → 1798.60] I'm sorry.
[1798.68 → 1799.36] I think I lost you there.
[1799.60 → 1801.16] Can you explain why that wouldn't work again one more time?
[1801.34 → 1802.14] So you're saying –
[1802.14 → 1802.16] Okay.
[1802.24 → 1802.72] So let's see.
[1802.76 → 1803.60] I have three services.
[1803.76 → 1810.16] I have Google Login and I have Cloudflare AutoRag, which I assume is something to do with AI.
[1810.68 → 1817.06] You would program in your little cluster of machines that any request going out to Google automatically explodes.
[1817.42 → 1818.62] It's not a cluster of machines.
[1818.76 → 1820.34] It's called Donkey Kong or something.
[1820.42 → 1821.28] I don't remember what he called it.
[1821.28 → 1822.78] It was like Dong Sh long or whatever.
[1822.78 → 1823.10] But I'm describing the actual architecture.
[1823.36 → 1824.46] Donkey Kong Sh long.
[1824.68 → 1825.12] Yeah, that.
[1825.46 → 1832.44] When that thing's on, it takes the cluster of machines and says, okay, any network traffic that matches this regex, which, of course, don't do that.
[1832.48 → 1833.88] But let's just pretend you do it this way.
[1834.16 → 1834.92] Match this regex.
[1834.96 → 1836.24] We just return an auto 500.
[1836.74 → 1838.38] Okay, that works on the Google sign-in.
[1838.44 → 1839.22] We fix the problem.
[1839.58 → 1848.94] But the Cloudflare request to AutoRag, you don't solve because that request to Google happens outside your purview to, like, effect.
[1849.50 → 1851.16] And so that's where this big problem is, is that you can't actually simulate it.
[1851.16 → 1852.52] You basically need a black hat team.
[1852.86 → 1856.72] You need a black hat team to go actually crash Google and see what happens for the day.
[1857.02 → 1860.76] And that's the only way to actually implement Donkey Kong Sh long or whatever it's called.
[1861.12 → 1861.78] It's crazy.
[1862.44 → 1864.94] We'll have just been here for 20 minutes in case he's saying Sh long and Dong true.
[1864.94 → 1867.42] I mean, couldn't you also catch this, too?
[1867.56 → 1873.20] So I'm saying, like, basically any external dependency you guard with a red button that you can test, right?
[1873.26 → 1874.42] Because then, like, then you could test.
[1874.62 → 1880.12] It's not so much like that you're depending on that to tell you when Google or Cloudflare or whatever goes down.
[1880.20 → 1885.12] It's more like you're able to test, like, hey, from a risk calculus perspective, if Cloudflare.
[1885.20 → 1886.76] Oh, but you're saying you don't know the dependency, I guess.
[1886.96 → 1887.54] That's the problem.
[1887.62 → 1889.08] It's the same problem I was talking about originally.
[1889.08 → 1896.30] It's just like if you don't – if this isn't – or worse yet, I guess if you combine the two problems that we've talked about, it gets even worse.
[1896.48 → 1899.18] Because, like, I'm saying, like, oh, it would be nice if they said what they depend on.
[1899.52 → 1906.40] But what you were saying at a level is that, like, it's unclear that anyone at the company may even know the answer to that question always.
[1906.40 → 1912.42] Like, dude forgot that, oh, we actually do call, like, the Google service in this one place.
[1912.42 → 1913.62] And we forgot about that.
[1913.64 → 1914.58] And we didn't put it on the diagram.
[1914.68 → 1916.68] And so then we went down because, you know, blah, blah, blah.
[1916.68 → 1923.80] So I guess it's, like, what I'm saying is just an observation of, like, this increases – this decreases your ability to analyze your risk.
[1923.90 → 1925.42] And there may be nothing you can do about it.
[1925.80 → 1925.92] Yeah.
[1925.96 → 1927.04] I think I'm on that team.
[1927.24 → 1929.44] I think I'm literally in the team of, like, that's just how it is.
[1929.70 → 1930.34] Figure it out.
[1930.52 → 1931.18] Like, you know what I mean?
[1931.36 → 1933.52] It's like either roll your own everything or forget it.
[1933.68 → 1934.72] I mean, do companies do that?
[1934.76 → 1936.48] Do people just, like, I just don't want any dependencies?
[1936.88 → 1937.86] I'm so happy you said that.
[1938.04 → 1938.32] Trash.
[1938.40 → 1946.24] I'm so happy you said that because that's the next thing I wanted to talk about, which was my happiest part about this whole thing is knowing the level of tweets.
[1946.24 → 1950.22] That were going to happen from DHH right after this thing started going down.
[1950.36 → 1951.50] I was so stoked.
[1951.60 → 1952.78] I'm like, here comes DHH.
[1953.12 → 1954.70] He's going to be coming in hard.
[1954.78 → 1957.16] He's going to be, like, on-prem solutions.
[1957.52 → 1957.84] Exactly.
[1958.52 → 1961.28] At what point did we just have it all under our own rules?
[1961.28 → 1962.54] He was living the dream life.
[1962.62 → 1964.34] They're like, oh, it went down.
[1964.50 → 1966.14] Oh, I didn't know that.
[1966.16 → 1966.94] Was he tweeting a lot?
[1967.04 → 1967.44] I didn't see.
[1968.26 → 1968.94] Was he going nuts?
[1969.44 → 1969.86] Oh, yeah.
[1969.90 → 1976.84] He said there was even – I saw more tweets about people getting worried about DHH tweeting than DHH tweeting.
[1977.20 → 1978.92] But there were several of them.
[1979.14 → 1979.64] That's awesome.
[1979.64 → 1980.44] And this is, like, my favourite.
[1980.54 → 1986.92] That's my favourite aspect of the whole thing is that someone who has been right this whole time who everyone makes fun of,
[1986.92 → 1990.80] and then the thing happens that he talks about, and they're all like, oh, great.
[1991.40 → 1993.16] He's going to be insufferable now.
[1993.24 → 1996.44] It's just like – or he's just going to be right, and he told you so.
[1997.52 → 1997.96] Mm-hmm.
[1998.10 → 1998.50] Mm-hmm.
[1999.22 → 1999.58] MWh.
[2000.58 → 2000.82] Okay.
[2000.88 → 2001.50] No one else noticed?
[2001.68 → 2001.92] Whatever.
[2002.34 → 2004.32] I thought it was fantastic.
[2004.62 → 2005.74] We don't need to discuss that part.
[2007.04 → 2008.64] I was living real life touching grass.
[2008.72 → 2009.26] I missed it all.
[2009.26 → 2009.58] All right.
[2009.62 → 2016.52] So something funny happened to me is that I was streaming during that day, and I got done – my stream,
[2016.52 → 2022.34] I ended at, like, I think it was the hour that Cloudflare went down,
[2022.44 → 2024.74] and then I had a bunch of programming that I had to do,
[2024.90 → 2028.92] and I just proceeded to program until, like, 3 or 4 in the afternoon, open up Twitter,
[2028.98 → 2030.68] and everyone's just like, oh, I can't work.
[2030.78 → 2031.56] The life's ruining.
[2031.66 → 2032.30] The Internet's down.
[2032.52 → 2034.56] I had no idea the Internet even went down.
[2034.84 → 2037.42] I was just in my own little world with my headphones on,
[2037.50 → 2040.94] and I missed the entire, like, experience of the Internet exploding.
[2041.72 → 2043.26] Yeah, I literally had no idea either.
[2043.26 → 2044.04] I lost out, yeah.
[2044.04 → 2047.44] I don't actually know, like, what exactly went down, like, in my own.
[2047.52 → 2048.66] Like, what do I use every day that went down?
[2048.66 → 2049.02] Everything.
[2049.28 → 2049.94] Everything went down.
[2049.96 → 2055.14] Like, I remember, like, people couldn't – like, on our Discord, people couldn't upload images.
[2055.76 → 2056.66] Could Tesla start?
[2056.74 → 2057.42] Could you drive a Tesla?
[2058.00 → 2058.88] I don't have a Tesla.
[2059.26 → 2064.18] I refuse to use a computer that is connected to an Internet – a car that is connected to the Internet.
[2064.32 → 2065.26] I think that's absolutely ludicrous.
[2065.28 → 2067.28] I was like, Casey, you're on a computer that's connected to the Internet, buddy.
[2067.32 → 2068.60] Casey, I used to have that mentality.
[2068.60 → 2073.42] I used to, like, refuse to do smart thermostats, smart cars, and then I just gave up.
[2073.50 → 2074.42] I was like, nah, whatever.
[2074.68 → 2075.02] Don't do it.
[2075.26 → 2075.46] Don't do it, man.
[2075.46 → 2076.74] If they're going to kill me, they're going to kill me.
[2076.78 → 2077.22] You know what I mean?
[2077.22 → 2077.54] No, no.
[2077.74 → 2078.80] I know what happened.
[2079.16 → 2081.06] Your wife bought that Wi-Fi lamp.
[2081.26 → 2084.08] You uploaded a picture of it, and after that, you're just like –
[2084.08 → 2084.52] GG.
[2084.96 → 2085.20] GG.
[2085.20 → 2086.70] My wife – love her to death.
[2086.74 → 2087.46] She's actually in the other room.
[2087.50 → 2088.82] She might walk in here while I'm making fun of her.
[2089.30 → 2097.16] She bought a lamp that was, like, IoT, and to turn on the lamp, you had to download an app that connected to the lamp over Bluetooth.
[2097.40 → 2097.84] Hold on.
[2098.16 → 2105.44] And then you had to put your Wi-Fi password into the lamp for it to connect to the Internet to upload its firmware, and then you could turn the lamp on.
[2105.62 → 2106.02] Exactly.
[2106.48 → 2106.68] Yeah.
[2106.68 → 2108.70] And then it bricked itself somehow, and it's useless.
[2111.60 → 2112.68] It's crazy, man.
[2112.78 → 2117.32] So ever since then – oh, and also, I had to punch a hole through my firewall for it to work.
[2117.32 → 2125.68] I had to make a separate VLAN on my network, and on that network, I had to basically allow – I block, like, traffic by country.
[2125.84 → 2130.44] I had to allow a different country into my network for that lamp to work, which is pretty insane.
[2130.44 → 2130.66] This is what country.
[2130.80 → 2131.32] Was it Russia?
[2131.82 → 2132.54] What country?
[2133.46 → 2133.62] China.
[2133.62 → 2134.06] China, yeah.
[2134.06 → 2135.70] I had to allow Chinese traffic to my network.
[2136.10 → 2136.90] Never heard of them, yeah, yeah.
[2136.90 → 2140.44] I love that you allowed China in from a Wi-Fi lamp that uploads passwords.
[2140.58 → 2142.10] That definitely wasn't –
[2142.10 → 2143.20] Worth it.
[2143.92 → 2144.96] Needed the lamp, baby.
[2145.42 → 2145.92] Needed the lamp.
[2145.94 → 2147.10] Did it at least change colours?
[2147.10 → 2147.66] Was it, like, a human?
[2147.66 → 2147.94] Oh, yeah.
[2148.02 → 2148.42] It was cool.
[2148.62 → 2148.94] Perfect.
[2149.26 → 2149.50] Perfect.
[2149.60 → 2149.88] Worth it.
[2149.96 → 2152.46] It also had a timer in it that when you, like, oh, it's 630.
[2152.68 → 2153.74] Sunrise is at 645.
[2153.90 → 2156.12] It'll slowly bring the room up to light.
[2156.20 → 2158.04] It'll be, like – and it makes, like, bird noises.
[2158.14 → 2158.92] It's, like, kind of rad lamp.
[2158.92 → 2160.38] I actually have a clock that does that.
[2160.40 → 2161.74] Yeah, but it broke, so, yeah.
[2161.90 → 2162.12] Whatever.
[2162.20 → 2164.58] I love how, like, no one can program without the internet.
[2164.66 → 2167.24] Like, nothing you just said requires the internet at all.
[2167.38 → 2168.48] But they're like, you know what?
[2168.74 → 2170.62] We need this lamp to connect to China.
[2171.08 → 2171.84] Remember that?
[2172.20 → 2175.78] The only way we can be sunrise in America is a server in China.
[2175.78 → 2176.02] China.
[2176.18 → 2176.68] That's right.
[2176.68 → 2179.18] That's a new rattle, right?
[2179.58 → 2182.80] We need a convenient way to ask you for your Wi-Fi plaintext password.
[2183.12 → 2184.88] But, like, you know, let that be what it is.
[2185.08 → 2185.78] Yeah, man, it's crazy.
[2185.88 → 2186.68] Like, GPS exists.
[2186.80 → 2187.84] GPS has a time source.
[2187.96 → 2189.08] Just use that.
[2189.16 → 2190.52] I don't know why it needed Wi-Fi access.
[2190.62 → 2193.56] Yeah, honestly, peak tech was the clap-on, clap-off lights.
[2193.74 → 2194.68] Dude, bring it back.
[2195.14 → 2196.00] Remember those commercials?
[2196.28 → 2196.58] Everybody?
[2196.74 → 2197.14] Old people?
[2197.48 → 2198.12] They're all getting out of bed.
[2198.20 → 2200.02] They're like, going to go back to sleep.
[2200.26 → 2201.84] That was peak technology.
[2202.18 → 2202.56] Yeah, dude.
[2202.66 → 2203.10] So good.
[2203.10 → 2208.28] I will say the fact that we have to sign in to something to use it, for me personally,
[2208.28 → 2211.52] is single-handedly the most frustrating aspect of modern life.
[2212.02 → 2215.90] Like, anything that I purchase that requires that, I want to throw it out the window.
[2216.00 → 2220.72] And I recently got an automated dog food feeder for my dog.
[2220.72 → 2222.32] And get this.
[2222.40 → 2225.08] I want you to just sit down and listen to this.
[2226.26 → 2227.74] There's no internet to it.
[2228.04 → 2229.70] There's no Bluetooth to it.
[2230.30 → 2234.08] It has a record button, so you can just be like, hey, dog, it's time to eat.
[2234.48 → 2234.58] Yep.
[2234.64 → 2239.68] It records your voice up to 10 seconds, and you can have up to four feeding sessions a day.
[2241.90 → 2242.70] That's pretty cool.
[2243.02 → 2243.60] We have this.
[2243.90 → 2244.30] Automated.
[2244.30 → 2247.18] We have basic technology.
[2247.40 → 2248.24] It exists.
[2248.90 → 2249.98] We have this as well.
[2250.22 → 2251.68] We have this for our cats.
[2252.38 → 2257.10] It says, bon appétit, tiny puss, every time it puts the little stuff up.
[2257.10 → 2257.28] Let's go.
[2257.92 → 2258.36] What?
[2258.80 → 2259.00] Yeah.
[2259.10 → 2259.60] That's awesome.
[2260.20 → 2260.48] It does.
[2260.48 → 2262.64] Is it, like, in your voice?
[2262.74 → 2263.54] Or is it like a song?
[2263.54 → 2263.78] Yeah, yeah, yeah.
[2263.78 → 2265.34] We recorded that.
[2265.64 → 2265.74] Nice.
[2265.74 → 2266.14] I love that.
[2266.14 → 2267.68] It's like, bon appétit, tiny puss.
[2268.22 → 2269.42] Is that how you say it?
[2269.50 → 2269.78] So it again?
[2270.42 → 2272.10] Bon appétit, tiny puss.
[2272.10 → 2274.54] And then all the stuff, the food comes out.
[2274.54 → 2275.62] He's Mario all of a sudden.
[2275.80 → 2276.42] Tiny puss.
[2277.46 → 2277.86] Yes.
[2278.56 → 2285.30] And this is the best part about this is you have to remember, this is an automated feeder,
[2285.54 → 2289.16] and there's two of them because we have two cats, and there's one for each cat.
[2289.68 → 2295.70] And these feeders go off, you know, four times a day or something.
[2295.70 → 2299.64] So if there are guests over, right, it's just like, oh, hey, how's it going?
[2299.74 → 2302.24] And then, like, in the background, it's like, bon appétit, tiny puss.
[2303.24 → 2305.08] And they're just like, ah, it's just a cat feeder.
[2305.08 → 2305.88] Don't worry about it.
[2306.78 → 2307.14] Yeah.
[2307.44 → 2308.12] That's awesome.
[2308.36 → 2309.06] It's pretty awesome.
[2309.06 → 2309.08] It's really cool.
[2309.08 → 2310.40] It's totally normal, bro.
[2310.60 → 2311.86] It's just a cat feeder, okay?
[2311.86 → 2312.10] Don't worry about it.
[2312.10 → 2312.96] I've been weird about it.
[2313.12 → 2315.92] But, okay, so this cloud thing.
[2316.00 → 2316.84] We've got to get back to the cloud thing.
[2316.84 → 2318.22] Like, hey, just kind of thing.
[2318.40 → 2320.18] All right, we're just blowing past that.
[2320.18 → 2323.44] I've never heard anyone call a cat a tiny puss before.
[2323.44 → 2327.90] Oh, dude, I love using the word.
[2328.54 → 2332.96] I totally abuse that so much all the time.
[2332.96 → 2334.36] You abuse the puss?
[2334.68 → 2335.16] Oh, yeah.
[2336.06 → 2337.66] What is happening right now?
[2337.66 → 2338.04] Yeah, yeah.
[2338.20 → 2340.42] I mean, in exactly the way you're doing now.
[2340.66 → 2342.44] Like, I love double entendre.
[2342.52 → 2343.26] What can I say?
[2343.70 → 2345.12] It's always good.
[2345.68 → 2350.46] Like, I always like when you can accidentally, accidentally make it sound dirty.
[2350.70 → 2351.92] I'm going to like it.
[2352.04 → 2352.74] I'm going to like that.
[2352.74 → 2353.34] Mm-hmm.
[2353.48 → 2356.30] I swear TJ leaves for one stream.
[2356.98 → 2357.44] Just one stand-up.
[2357.44 → 2358.54] Oh, God, you're right.
[2358.64 → 2359.90] He would love this.
[2360.16 → 2360.34] Yeah.
[2360.48 → 2361.58] I don't know if he would love it.
[2361.58 → 2365.82] I don't know if he would love it, but he'd probably shut it down real quick.
[2366.22 → 2367.50] We would have been on a different topic.
[2367.70 → 2369.86] Family-friendly podcast, guys.
[2370.44 → 2371.48] I'm from New Jersey.
[2371.66 → 2372.94] I can't help myself.
[2373.02 → 2373.86] I'm sorry, okay?
[2373.98 → 2374.16] Listen.
[2374.24 → 2374.60] All right.
[2375.00 → 2377.86] Well, anyway, what were you going to say about some stupid cloud?
[2377.86 → 2381.42] Honestly, I have no idea at this point.
[2381.42 → 2382.84] I just want to say that.
[2382.84 → 2383.00] Okay.
[2383.24 → 2383.66] All right.
[2383.82 → 2386.30] Just, I guess, okay, so low-level learning.
[2386.56 → 2390.24] We had a thing where you weren't allowed to plug in devices on the Netflix network.
[2390.58 → 2390.76] Yeah.
[2391.50 → 2392.86] Why are you giving up?
[2393.32 → 2399.72] Why not just not have, like, do you really need sunset lamp, or can you just turn on the lamp?
[2399.90 → 2403.56] So my thing is like, how do I say this?
[2404.46 → 2412.78] I, for a long time, lived a very paranoid life where I wouldn't do certain things, and I wouldn't use modern comforts out of fear of being targeted.
[2413.04 → 2414.82] Hit me a modern comfort that you wouldn't use.
[2414.92 → 2416.46] Like, something to help us understand that.
[2416.46 → 2418.60] No, literally, like, a smart thermostat, I refused.
[2418.84 → 2426.18] And, like, me 10 years ago would not have driven a Tesla because, like, oh, it's, you know, lithium-ion batteries attached to a computer on the internet, and they could blow it up, right?
[2426.22 → 2428.14] Like, that crap used to be what I would say.
[2428.52 → 2432.94] But then I realized, if you're being targeted, they're going to get you, dude.
[2433.14 → 2434.02] It doesn't matter.
[2434.20 → 2435.74] That's literally my way of life.
[2436.02 → 2436.24] Yeah.
[2436.36 → 2436.66] What?
[2436.96 → 2437.18] What?
[2437.74 → 2438.88] This is a one password.
[2439.16 → 2440.14] One password, bro.
[2440.24 → 2440.94] Yeah, yeah, yeah.
[2440.94 → 2444.72] I have faith in humanity until it turns on me.
[2444.72 → 2450.32] So, like, if I go to, like, a public space, I'll just literally leave my wallet just standing or sitting right there.
[2450.34 → 2450.78] That's crazy.
[2450.98 → 2451.46] Hold on.
[2451.66 → 2451.94] Stop.
[2452.12 → 2452.28] Wait.
[2452.38 → 2452.88] Okay, so, like.
[2452.88 → 2454.42] I'll literally just put my wallet, like, right there and open.
[2454.50 → 2455.72] Like, I'm just, like, no one's going to steal it.
[2455.74 → 2456.64] Like, I have faith in you, man.
[2456.94 → 2457.90] So far, hasn't yet.
[2457.96 → 2458.44] Oh, my goodness.
[2458.64 → 2459.68] Just jinxed myself.
[2460.18 → 2461.30] But, like, I leave my stuff.
[2461.38 → 2464.04] Like, this is, like, at, like, gyms that I go to, like, where I kind of know everybody.
[2464.20 → 2467.78] But, like, I have faith in humanity to where, like, if they're going to get me, they're going to get me.
[2467.78 → 2469.90] If they want to get my wallet, they'll just break into my locker.
[2469.90 → 2471.78] Time on, time on, time on.
[2471.92 → 2474.34] I just, I'm speechless.
[2475.08 → 2476.46] Like, there's a difference.
[2476.92 → 2477.28] What?
[2478.42 → 2481.20] I just leave my wallet out because if they're going to get me.
[2481.32 → 2485.42] First off, there is a shadowy cabal that's going to get somebody for a very specific reason.
[2485.90 → 2489.48] Leaving your wallet out for anybody to steal is not smart.
[2490.06 → 2490.74] Okay, okay, okay.
[2490.74 → 2491.50] Here's a better example.
[2491.64 → 2493.94] Sometimes I don't lock the door to my house.
[2493.94 → 2498.88] Like, if they're going to get me, they're going to just break the window, kick the door down.
[2498.88 → 2499.88] Like, my life's very-
[2499.88 → 2500.46] Yeah, but you live in California, though.
[2500.64 → 2501.06] That's different.
[2501.50 → 2502.52] Yeah, that's what you guys do out there.
[2502.52 → 2504.24] I mean, I did it on the East Coast, too.
[2504.42 → 2504.70] You know?
[2504.86 → 2506.26] Just leave your keys in the car.
[2506.88 → 2510.20] All I'm saying is if they're going to get me, they're going to get me, I'm just going to live my life.
[2510.54 → 2511.82] No, but that's where I'm at, right?
[2511.88 → 2513.50] It's like, back to your question, Prime.
[2513.74 → 2516.78] Like, a corporate network has more to lose, right?
[2516.82 → 2519.26] So, like, maybe there should be rules in place to not plug in random crap.
[2519.26 → 2521.34] But, like, at my house, like, I'm going to do my best.
[2521.42 → 2525.78] I'm not going to go on freaking Teems and buy a router from Teems for $14 and then, like, be surprised when I get hacked.
[2525.78 → 2529.48] I'm not going to do that, but I'm also, like, I'm going to use the internet lamp.
[2529.58 → 2530.06] You know what I mean?
[2530.12 → 2531.12] Like, I'm just kind of just whatever.
[2531.64 → 2534.42] I'm over the paranoia, just for myself personally.
[2534.70 → 2536.80] Have good hygiene.
[2537.06 → 2537.86] Like, use, like, shower.
[2538.00 → 2540.10] No, but, like, use a password manager, right?
[2540.10 → 2540.78] Do all that stuff.
[2540.90 → 2542.52] Like, VPNs when appropriate.
[2542.78 → 2545.98] But, I mean, like, I'm not going to, like, not use certain technologies out of fear anymore.
[2546.12 → 2547.88] Just how I've decided to do.
[2547.88 → 2548.64] That's a pain of an ass.
[2548.82 → 2555.92] Like, to have to sign in via Bluetooth, send a password so it can sign in to your network just to turn on a lamp.
[2556.08 → 2558.40] Like, that's not even about getting hacked.
[2558.48 → 2559.68] That's just an ass pain.
[2559.90 → 2561.90] I don't want to use that product, like, ever.
[2562.22 → 2566.78] I don't care how great the sunrise and bird calls are and how, oh, did you hear that?
[2566.96 → 2570.22] That's actually a southwest loop that's specific to a region.
[2570.36 → 2571.80] Like, I don't even care.
[2572.02 → 2576.06] Like, there's no money you can pay me to sign in to a lamp to make it turn on.
[2576.50 → 2578.02] That one's, like, the far end of the spectrum.
[2578.12 → 2578.46] I agree.
[2578.68 → 2579.24] But, like, you know.
[2579.24 → 2580.36] That's the counterpoint, though.
[2580.44 → 2581.70] That is the legitimate counterpoint.
[2581.76 → 2583.52] Because it's, like, what you're saying makes total sense.
[2583.60 → 2592.68] Like, if your threat model for why your stuff in your house isn't going to work is that, like, you know, some government security agency is going to target you.
[2592.68 → 2593.42] It's, like, forget it.
[2593.44 → 2595.24] Because they'll just come to your house with guns and take you.
[2595.44 → 2597.52] They don't need to hack your lamp.
[2597.64 → 2598.78] It's not necessary, right?
[2598.78 → 2608.82] But the in your sentence could just as easily just be incompetent people at the actual manufacturer who cannot get the freaking lamp working.
[2608.92 → 2610.38] And that's why I don't buy any of these things.
[2610.46 → 2617.18] Like, I know that if I bought a Nest thermostat, I guarantee you the temperature in my house would be random all the time.
[2617.42 → 2622.26] And that is because I also seem to have uniquely bad luck with this sort of thing.
[2622.44 → 2624.78] So, you know, all the people who are, like, what are you talking about?
[2624.82 → 2626.28] My Linux install worked the first time, right?
[2626.28 → 2630.28] It's, like, for me, it's always, like, I will always hit the weird case for some reason.
[2630.90 → 2635.00] So, if, you know, if I bought a Tesla, it would – the software would never be working.
[2635.12 → 2637.08] It would be – and, in fact, a friend of mine actually had this.
[2637.14 → 2638.50] He had a Tesla pretty early.
[2638.86 → 2640.28] And he had so many hilarious stories.
[2640.38 → 2643.80] He's, like, yeah, the air conditioning just stopped working for several weeks because of some software update.
[2643.92 → 2645.34] But then it's sort of working again now.
[2645.44 → 2653.38] And he's, like, oh, the sunroof stopped working because they updated the software, and they changed – I guess new models have that plugged into a different physical port.
[2653.38 → 2656.14] And they stopped sending the things out, the old port.
[2656.22 → 2657.96] So, now his sunroof is just closed permanently.
[2658.38 → 2661.96] Like, all of a sudden, I'm, like, yes, that is what would have happened to me if I had bought a Tesla.
[2662.00 → 2662.78] I don't want any of that.
[2662.92 → 2665.66] I just want to know that, like, the sunroof is on a motor.
[2665.84 → 2668.02] And unless the motor dies, it will open, right?
[2668.30 → 2669.56] Because it's less failure points.
[2669.88 → 2673.50] I will say, like, I don't like being on the cutting edge of new technology.
[2673.62 → 2675.16] So, like, I own a Tesla, for example, right?
[2675.52 → 2678.64] And to that point, I recently went to go drive somewhere.
[2678.78 → 2679.62] I sat in my car.
[2679.76 → 2682.90] And then on the Tesla, it said there has been an electrical failure.
[2683.08 → 2683.56] Call Tesla.
[2683.84 → 2684.96] And I'm, like, what the hell is that?
[2685.12 → 2689.02] And so what I had to do is have them tow the Tesla 45 minutes away and fork out $5,000.
[2689.44 → 2691.22] And because it's Tesla, it's proprietary.
[2691.60 → 2692.96] So they can't tell me what happened.
[2693.04 → 2694.58] They're just, like, yep, sorry, we fixed it.
[2694.62 → 2695.00] Here you go.
[2695.06 → 2695.48] Give me your money.
[2695.48 → 2699.50] And so I feel you in terms of the ease of use on technology.
[2700.94 → 2704.36] Things that are well-solved problems, I will use newer technology.
[2704.60 → 2706.60] But, like, electric cars, I have a Tesla.
[2706.68 → 2708.52] I'm probably going to get rid of it for that reason.
[2708.62 → 2714.34] I don't like effectively being the market test monkey, right, for these bigger companies.
[2714.86 → 2717.06] And they're not serious about fault tolerance.
[2717.24 → 2717.68] Like, that's the thing.
[2717.74 → 2718.66] It's, like, this car was not.
[2718.72 → 2721.22] I mean, maybe the brakes were, which is good.
[2721.34 → 2725.10] But, like, the actual ability to drive the car was not, as far as I can tell, right?
[2725.10 → 2726.36] And use the features of the car.
[2726.62 → 2731.84] Yeah, I would imagine, like, internally there's, like, some real-time hard system for braking and stuff.
[2732.14 → 2734.66] But, like, the UX of turning on the car.
[2735.10 → 2735.82] Not so much.
[2735.92 → 2736.38] Maybe not.
[2736.50 → 2736.66] Yeah.
[2737.10 → 2738.20] All I really want.
[2738.70 → 2739.70] Sorry, you go trash.
[2739.96 → 2740.56] No, I was going to say.
[2740.62 → 2741.40] You just go, okay?
[2742.20 → 2743.14] Prime is so mad.
[2743.20 → 2743.80] What is happening right now?
[2743.80 → 2744.44] I don't know.
[2744.64 → 2745.96] He's melting down.
[2746.06 → 2746.72] He's not mad.
[2746.84 → 2747.20] He's melting.
[2747.20 → 2748.96] He's, like, so disappointed in us.
[2749.08 → 2750.56] I just want to get this off my chest.
[2750.68 → 2752.42] So disappointed in us right now.
[2752.70 → 2753.50] All I want.
[2753.50 → 2755.66] I don't really care about smart houses or anything.
[2755.76 → 2760.96] All I want is the fridge that has the clear door so I can just look inside of it without opening the door.
[2761.56 → 2762.18] That's all I want.
[2762.58 → 2763.36] That's all I require.
[2763.36 → 2764.42] You can just buy a glass door?
[2764.78 → 2765.40] Is that what you're asking?
[2765.40 → 2768.84] You know, the fridge is where you can see before you open the door.
[2768.92 → 2769.60] That's all I want.
[2769.90 → 2770.40] They have that.
[2770.48 → 2770.98] You can buy that.
[2771.06 → 2771.48] I know.
[2771.74 → 2773.22] But it's just glass.
[2773.22 → 2775.62] Why don't you just get triple-pane glass or something?
[2775.78 → 2781.86] Like, why do we have to have technology that involves a camera when we already have something you can see through called glass?
[2781.86 → 2783.04] Well, no, that's what I'm saying.
[2783.10 → 2785.16] I just want a simple glass door.
[2785.16 → 2786.02] He wants the glass one.
[2786.06 → 2786.82] He's agreeing with you, Prime.
[2786.82 → 2787.72] I don't want the technology.
[2787.96 → 2789.50] This isn't even about technology anymore.
[2789.50 → 2790.26] I just want a free glass.
[2790.26 → 2791.24] I'm on his side.
[2791.60 → 2792.76] I'm on your side, Prime.
[2793.30 → 2793.88] Thank you.
[2793.94 → 2798.86] Because when I hear everyone like, oh, the Nest thermostat is good, I'm like, bitch, it is worse.
[2798.86 → 2804.14] The time I set my AC to 69, and I never set it again.
[2804.36 → 2805.08] Same here.
[2805.08 → 2810.46] Next month, what the hell do you need a smart temperature setter?
[2810.56 → 2811.18] Can I tell you?
[2811.40 → 2811.64] Okay.
[2811.86 → 2813.26] Hit us up with it.
[2813.60 → 2816.40] This is the most American thing you're ever going to hear, but here.
[2816.64 → 2817.72] I'm laying in bed.
[2818.14 → 2818.84] It's 930.
[2819.00 → 2819.52] Super American.
[2819.66 → 2820.86] My son, two years old, is asleep.
[2820.94 → 2824.88] I can see on the baby monitor that his room is a piping hot 74.
[2825.38 → 2825.68] Okay.
[2826.00 → 2826.88] I don't want to get up.
[2826.96 → 2827.42] I'm in bed.
[2827.48 → 2828.06] I brush my teeth.
[2828.12 → 2828.82] My Invisalign is in.
[2828.84 → 2829.28] You know what I do?
[2829.30 → 2830.08] I go to my phone.
[2830.08 → 2833.78] I can change the temperature in the house from my bed.
[2833.88 → 2834.90] I don't have to get up, baby.
[2835.20 → 2836.08] You can try.
[2836.18 → 2838.76] You can try to change the temperature and everything.
[2839.02 → 2840.18] I have two beds going.
[2840.30 → 2840.64] I'm set.
[2841.30 → 2844.56] I turned off the camera and only listened to audio.
[2845.98 → 2849.20] And for most of our kids' childhood, I didn't even have one of those.
[2849.36 → 2853.72] I slept near enough that I could hear them cry if they got really ornery, and that's it.
[2853.74 → 2856.36] Because you don't need to listen to everything.
[2856.84 → 2857.92] Probably good practice in this podcast.
[2857.92 → 2860.96] If you're in your life with this shit, just stop it.
[2861.02 → 2862.64] You don't need to do it at 74.
[2862.82 → 2863.48] It gets sucks.
[2863.64 → 2865.50] But that's totally normal temperature.
[2865.50 → 2868.86] But the moral of the story is I changed that shit for my phone, dude.
[2868.90 → 2869.42] It was great.
[2869.50 → 2870.18] I don't have to get up.
[2870.34 → 2871.28] So that's why I used it.
[2871.28 → 2872.38] That's not the moral of the story.
[2873.44 → 2874.72] Prime, just more heated now.
[2875.70 → 2876.46] Wait, so I saw in chat, Prime.
[2876.46 → 2879.22] And then the Google Cloud went down, and my baby froze to death.
[2879.34 → 2883.58] But you know that one day that I could change the temperature from bed, it was all worth it, right?
[2884.72 → 2887.90] Google Log just stopped working, so I couldn't show up.
[2887.92 → 2890.08] My house is 89 today in the summer.
[2891.10 → 2892.26] Prime, are you mad because you bought a Tesla?
[2893.70 → 2893.96] Me?
[2894.10 → 2895.04] No, I never bought a Tesla.
[2895.28 → 2896.58] Oh, Beacon said you bought a Tesla.
[2896.70 → 2896.96] That's why.
[2896.98 → 2902.94] I have a 2006 what's called Chevy flatbed pickup that has manual window rolls.
[2902.94 → 2909.04] Dude, when I met up with Prime and Teen in LA, they saw my car, and Prime was so disappointed.
[2909.40 → 2914.14] And he was like, you need to get your priorities straight in life.
[2914.38 → 2915.56] What was the car?
[2915.90 → 2916.92] I have a Porsche.
[2916.92 → 2922.10] And he just looked at the ground and was like, damn it, trash.
[2922.10 → 2923.36] Get your life on track.
[2923.74 → 2925.10] It was so fun.
[2925.68 → 2926.64] I felt so bad.
[2926.76 → 2929.02] I was like, all right, I guess I'll just drive home now.
[2929.28 → 2930.92] And it just drove home in shape.
[2931.74 → 2933.20] Let the man have his Porsche.
[2933.34 → 2934.22] All right, my bad, dude.
[2934.70 → 2935.96] That is a crazy message.
[2936.10 → 2936.52] Holy shit.
[2936.58 → 2939.32] We lost the baby because it had an upstream dep on GCP.
[2939.62 → 2940.16] Yeah, yeah.
[2940.88 → 2941.32] Dude.
[2941.32 → 2946.38] Dude, but that's like actually, okay, that is like the world we live in now.
[2946.50 → 2950.88] We live in a world where computers have crashed planes into the ground and everyone died.
[2951.12 → 2952.24] That's not like fictional.
[2952.36 → 2952.48] That's true.
[2952.66 → 2953.46] That's terrifying.
[2953.58 → 2954.44] I was just like, sorry.
[2954.92 → 2955.72] It really is.
[2955.78 → 2962.30] People underestimate the risks from actually increasingly putting technology in places where they could have bad results.
[2962.42 → 2965.54] I agree the baby froze to death is probably an exaggeration in this case.
[2965.54 → 2968.96] But things like that are not far, right?
[2968.96 → 2972.16] And it doesn't have to be about security exploits.
[2972.24 → 2973.90] It can just be incompetence.
[2974.02 → 2974.88] That's the scary part.
[2975.14 → 2978.24] You guys have heard of the Toyota 2009 case, right?
[2979.32 → 2979.56] Yes.
[2979.80 → 2981.70] Was this the Prius acceleration case?
[2981.70 → 2983.14] I was like, what, 16 years ago?
[2983.20 → 2983.94] I don't know.
[2984.14 → 2985.60] So I don't know if it was just Prius, Casey.
[2985.74 → 2986.94] I think it was a lot of Camry, too.
[2987.02 → 2991.74] But basically, the way the ECU worked on Toyota is it had an RTS in it.
[2991.74 → 2995.88] And inside RTS is you have the thread control block for all the threads that run on the RTS.
[2996.06 → 2997.20] Time out, time out, RTS.
[2997.20 → 2998.74] The real-time operating system.
[2998.74 → 2999.98] The electrical control unit, real-time operating system.
[2999.98 → 3000.18] Sorry.
[3000.34 → 3000.76] Okay, okay.
[3000.76 → 3001.62] Got it, got it, got it.
[3001.86 → 3002.72] Real-time operating system.
[3002.82 → 3014.44] But basically, the way that it was designed, if a single bit got flipped in the TCB, the task that ran the accelerator would not properly halt.
[3014.44 → 3018.24] So, like, the cars were literally just randomly flooring it.
[3018.30 → 3020.96] And there was no way to stop it because of the way that they wrote the braking logic.
[3021.06 → 3022.46] Because it was a fly-by-wire braking.
[3022.56 → 3023.84] It wouldn't actually actuate the brakes.
[3023.84 → 3035.90] So, people from, like, 2009 to 2012, I think, were, like, just randomly getting caught doing, like, 120 miles an hour and flying into a brick wall because the ECU was, like, crashing non-gracefully.
[3036.14 → 3038.34] I didn't know that they ever root-caused that.
[3038.46 → 3041.86] That's always—they actually found—they actually did—oh, I shouldn't say root-caused it.
[3041.96 → 3044.60] I didn't know they ever published what it actually was.
[3044.60 → 3053.54] So, it was closed privately, but Michael Barr, who was the consultant that was doing the analysis, has published some of his slides of his findings.
[3053.68 → 3055.60] I think a lot of it is still under NDA with Toyota.
[3055.82 → 3061.28] But he basically, like, published what he thought it was before it went public, public internal, right?
[3061.58 → 3063.94] And he said, basically, yeah, like, this thing is a landmine.
[3064.06 → 3068.54] If a bit flips here, here, here, or here, the ECU will just run on forever in undefined behaviour.
[3068.68 → 3071.12] And that includes, like, oops, the brakes don't work.
[3072.04 → 3072.32] Wow.
[3072.32 → 3072.72] Wow.
[3073.02 → 3078.34] Just recently, like, just this year or maybe last year, Tesla had it where there was some sort of fire that happened,
[3078.72 → 3082.52] and people couldn't unlock the door because there was a power failure in the Tesla.
[3082.68 → 3085.58] And it just, like, the door shut, and the people burned to death inside their own car.
[3086.06 → 3087.26] Fail open is very important.
[3087.54 → 3094.24] In fact, in fact, we can tie this back here at the—because we are at our hour mark, I think, or getting close to it.
[3094.36 → 3096.50] We can tie this back to the original topic of the day.
[3096.50 → 3103.82] One of the things that Google included in their, like, mea culpa, we took down the entire internet.
[3103.92 → 3104.58] Sorry about that.
[3104.68 → 3105.16] Our bad.
[3105.64 → 3111.08] Was at the end, they were like, what are the, you know, they're like, what are the steps we're going to take to try and improve our process, you know?
[3111.08 → 3115.60] And one of the things they listed was this service should have failed open.
[3116.14 → 3124.68] Like, instead of the default for when the quota system goes down being denied everything, maybe it's just approved everything, so the services can keep running.
[3124.92 → 3133.12] I don't know how that necessarily—but maybe you could do something more cabined where it's, like, approve any reasonable—like, approve anything that doesn't allocate news—too much new space.
[3133.12 → 3140.78] I don't know what they meant by that exactly, but they were like, try to make these things fail open so that it won't just take down the internet if, like, the quota check fails.
[3140.98 → 3145.96] That was what I assumed that they meant, but I don't really know because, again, it was a very terse statement.
[3146.30 → 3147.78] And I only read it for this podcast, right?
[3147.82 → 3151.40] I wasn't, like—I don't study this stuff, so I'm not sure.
[3151.58 → 3154.14] But so fail open is a pretty important principle.
[3154.32 → 3156.62] Like, should something fail closed or should something fail open?
[3156.62 → 3169.04] And if you have, like, door locks on a car, ideally, if there could be people inside, you always want it to fail open so that there's no way for, like, a car computer system to fail and then trap the people on the inside.
[3169.20 → 3173.34] You want to fail if, you know, if the system for locking goes down, you want it to be open, right?
[3173.40 → 3175.92] Because worst case, people steal your car or something like that.
[3176.04 → 3177.38] That's a lot better than burning alive.
[3177.86 → 3178.82] I was thinking about that.
[3179.14 → 3179.48] Oh, sorry.
[3179.72 → 3180.04] You can go.
[3180.04 → 3180.22] Okay.
[3180.32 → 3182.48] So it is tough from, like, I think, a design perspective.
[3182.74 → 3182.96] It is.
[3182.96 → 3188.50] Because the control plane software that crashed was the authorization software, it's like, I agree with you.
[3188.50 → 3189.24] It should fail open.
[3189.32 → 3193.58] But, like, to your point, what does fail open mean in an authorization case, right?
[3193.62 → 3196.24] You can't just be like, yeah, go do it, whatever, because that's bad.
[3196.24 → 3199.26] But inversely, denying everything killed the internet for a minute.
[3199.32 → 3199.86] So what do you do?
[3199.92 → 3200.22] It's tough.
[3200.72 → 3201.02] Prime, go ahead.
[3201.56 → 3207.94] I was about to say, you know, this fail open thing that also, like, there's—you also have a problem with this even with just the physical reality.
[3207.94 → 3212.68] Remember how Tesla was claiming that they're—whether it actually is bulletproof, their windows were bulletproof?
[3212.96 → 3216.34] What happens when you drive a Cybertruck into a pond, and you need to break out of the window?
[3217.84 → 3218.86] I actually have a keychain.
[3219.06 → 3219.22] Right.
[3219.32 → 3220.18] Yeah, yeah, yeah.
[3220.18 → 3222.14] I have a key utility that breaks windows.
[3222.24 → 3226.08] But normal windows, they just—you hit it once, and they explode into a thousand little pieces.
[3226.40 → 3229.84] What do you do when you hit it, and it just goes—and you're like, oh!
[3230.02 → 3230.16] Yeah.
[3231.04 → 3231.70] Oh, yeah, yeah, yeah.
[3232.24 → 3233.52] Well, this is like the locks, right?
[3233.52 → 3241.66] It's like one of the reasons that you want a lock to always be possible to do physically, if you could, right, is for this reason.
[3241.66 → 3252.70] It's because if you think about what fail open means, well, if a mechanical element has to push the lock up and down, and it's not accessible to humans, it's almost impossible to build a fail open version of that.
[3252.70 → 3255.88] Because if the electrical system fails, the locks cannot actuate.
[3256.08 → 3258.10] So there's really no fail open possibility.
[3258.46 → 3258.50] Right.
[3258.54 → 3268.40] So, like, again, like just smart mechanical design is like your car should have a way that you, with your hand, can unlock the door from the inside if you needed to, right?
[3268.40 → 3272.18] And, like, anything short of that is just kind of bad safety design, right?
[3272.20 → 3274.94] And the same is true for internet services to the extent that you can do them.
[3275.22 → 3277.08] You want to be thinking about that the same way.
[3277.26 → 3280.12] It doesn't quite analogize exactly, but it's similar, right?
[3280.56 → 3287.44] That is interesting because, like, the Tesla—you know, you have—the way that the doors work is you have a button that you push that electrically pulls the window down and opens the door for you.
[3287.56 → 3292.50] But there is a physical—I'm pretty sure it's pure mechanical knob where you can rip that, and it pops the door open.
[3292.56 → 3296.84] It's bad for the windows, obviously, but that's the fail open scenario is, like, you know, you are in a lake.
[3296.84 → 3299.54] The electronics are dead. Pull this lever. The door will open.
[3299.62 → 3305.94] So I'm interested in that case if they, like, if they knew that, if it was a rental, maybe that version didn't have that model.
[3306.02 → 3307.94] Maybe it's not mechanical, and it just broke. I'm not sure.
[3308.16 → 3310.10] Yeah, like, how did they burn to death without being able to do that?
[3310.52 → 3310.62] Yeah.
[3310.82 → 3313.48] I don't know. That's just the things that I heard.
[3313.62 → 3315.70] I don't know how it exactly works. I didn't do any research.
[3315.80 → 3321.12] Window-wise, it's worse because, like, to your point, like, you can't open the door if you fall into a lake because the water pressure is too high.
[3321.18 → 3321.28] Right.
[3321.28 → 3324.56] So you need to be able to open the window, and in that case, I don't know what their answer is to that.
[3324.56 → 3325.94] Break it, I guess, or I don't know.
[3326.84 → 3327.98] That's a terrifying scenario.
[3328.36 → 3329.02] It is terrifying.
[3329.62 → 3329.90] Nope.
[3330.44 → 3331.44] Prime, I know you love Rust.
[3332.16 → 3332.52] Yeah.
[3333.08 → 3333.94] Yeah, I do love Rust.
[3333.94 → 3339.24] Do you think that the GCP outage would have happened had this binary been written Rust?
[3340.24 → 3341.82] You know, that's actually a perfect question.
[3341.82 → 3347.86] I think that we would have still had some sort of weird state because at the end of the day, how do you have a state?
[3347.98 → 3350.10] Let's just say the YAML file produces something incorrectly.
[3350.74 → 3357.58] What happens to a GCP service if they update the policy and there's nothing there in a thing that's supposed to be there?
[3357.58 → 3358.18] Right.
[3358.24 → 3361.52] Like, someone would have probably programmed the positive case, and then what happens at the negative case?
[3361.56 → 3362.52] It just wouldn't deploy.
[3362.66 → 3363.94] Like, all things would stop anyway.
[3364.36 → 3364.48] Right.
[3364.48 → 3370.90] I'm not really sure, like, how this could have saved it much other than you would have had a pre-planned, hey, it's going to explode.
[3370.98 → 3374.44] Maybe you could have identified it earlier, and maybe the outage would have been less.
[3374.44 → 3384.60] I mean, I'm all for the idea of unique pointer slash smart pointers where you can't access things without some sort of, like, hey, yeah, this thing's not nil.
[3385.16 → 3386.62] Like, I like monads?
[3386.74 → 3387.80] Yeah, dude, get me in.
[3388.00 → 3389.88] Yeah, let me have a piece of that monad.
[3390.60 → 3391.60] I'm all about that.
[3391.72 → 3393.62] But at the same time, I don't know.
[3393.74 → 3402.10] Because the real question, I guess the question I'd have to follow up with is that it's not whether Rust would have made this possible or not possible.
[3402.10 → 3409.08] It is, if it were written in Rust, would this software ever have existed beyond somebody's idea or not?
[3409.18 → 3412.52] And that's really the question I have to ask is, can it actually exist in production?
[3412.72 → 3413.70] I'm not too sure.
[3414.06 → 3414.28] Right.
[3414.76 → 3418.66] We don't have any security exploits in Rust because the software did not get written.
[3419.00 → 3419.94] Right, because it never got shipped.
[3420.22 → 3421.00] It's never in production.
[3422.00 → 3422.74] Yeah, that's the thing, right?
[3423.02 → 3427.22] So whenever I do videos, I say at the end of the video about, like, memory exploits, like, would Rust have saved this?
[3427.28 → 3430.48] I think the answer to this one is sort of, right?
[3430.48 → 3438.82] Like, because it wasn't, like, necessarily, like, a memory corruption vulnerability or a memory corruption issue, it was more just, like, you dereferenced a bad address.
[3439.24 → 3442.06] I think the Rust programming model would have helped with it.
[3442.18 → 3445.50] But, like, you can do an unwrap on an option that's none, right?
[3445.60 → 3446.68] And then, like, you crash.
[3446.76 → 3455.94] So it's, like, there are still human factors in the code that could have caused it to be the same DOS condition if, you know, the ha-ha object in the YAML file wasn't there, right?
[3455.94 → 3458.44] But they would have made it, I think, less...
[3458.44 → 3458.92] What's that?
[3459.22 → 3460.48] They would have had an expert, right?
[3460.86 → 3466.00] Like, because they had been, like, you cannot have a license or whatever it was without these fields.
[3466.06 → 3468.84] And they probably would have just expected, which would have caused...
[3468.84 → 3473.10] It's, like, no different from a nil pointer crash because you wouldn't have known about it until runtime.
[3473.28 → 3474.72] So I assume it's the same thing.
[3474.76 → 3476.10] I don't think Rust would have helped at all here.
[3476.10 → 3476.84] Yeah, I agree.
[3476.84 → 3485.20] It would have been nice if they had said what language it was written in, showed us a little bit of the code, like, told us if this was Gemini, right?
[3485.20 → 3489.64] This could have been, like, somebody vibe-coded this and, like, hey, man, I'm pretty sure the AI said it was great.
[3489.98 → 3491.64] You know, like, but there was no information.
[3491.64 → 3494.06] So we don't really know, like, human factors-wise.
[3494.18 → 3498.26] We have no idea what happened here, really, because they were very, very, like...
[3498.26 → 3499.98] It was actually written in Rust, is my guess.
[3500.08 → 3503.22] And they actually don't want to release that information that it was written in Rust.
[3503.40 → 3503.90] By Gemini.
[3503.90 → 3505.56] It was written in Rust by Gemini.
[3505.56 → 3510.62] As part of the greater agenda of the Rust Industrial Complex, your sheep will need to wake up!
[3514.22 → 3515.22] Put up the board.
[3515.26 → 3519.44] Where's the board with all the connections between the Rust Foundation and the...
[3519.44 → 3520.50] Like, where is your diagram?
[3521.00 → 3523.20] We need the little conspiracy diagram.
[3524.72 → 3525.10] All right.
[3525.76 → 3526.54] Are we done?
[3526.94 → 3527.40] Are we done?
[3527.48 → 3528.26] Have we wrapped?
[3528.86 → 3529.88] I think we're wrapped, right?
[3529.88 → 3531.48] We've got tons of great content in here.
[3532.02 → 3533.54] No one could be unhappy with that.
[3533.54 → 3535.12] No one could be unhappy with that episode.
[3535.12 → 3536.24] Chad, you just...
[3536.24 → 3537.62] That was a golden episode.
[3537.78 → 3538.84] What more do you want from us?
[3539.98 → 3540.66] Low level.
[3540.82 → 3541.70] Low level, everybody.
[3541.84 → 3543.38] Loot up the day.
[3545.08 → 3548.14] Vibe cult and errors on my screen.
[3550.02 → 3551.06] Terminal coffee.
[3552.06 → 3552.96] And hand.
[3553.96 → 3555.94] Living the dream.
[3555.94 → 3558.52] Harm.
[3558.52 → 3571.58] Let's go.
[3575.70 → 3576.22] What are you doing?
