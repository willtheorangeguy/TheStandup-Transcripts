[0.00 --> 1.50]  Today, we're talking robots, okay?
[1.88 --> 3.06]  And not just any robots.
[3.18 --> 5.24]  Robots with a massive exploit.
[5.58 --> 11.74]  An exploit so juicy and so hilarious that they just completely went dark, didn't talk to anybody.
[11.94 --> 13.42]  And we're going to find out all about it today.
[13.86 --> 16.18]  And so, Casey, why don't you give us a little bit of a walkthrough?
[16.22 --> 18.94]  Because you're the one that found this sweet, amazing article.
[19.34 --> 22.16]  And so why don't you kind of give us a bit of a walkthrough of what happened?
[22.56 --> 24.06]  And then we kind of can go from there.
[24.62 --> 26.84]  Yeah, and I'll be completely honest.
[26.94 --> 29.30]  This one was a bit perplexing to me.
[30.00 --> 34.06]  I don't work with robotics, so it's a little out of my comfort zone.
[34.86 --> 36.34]  But I saw it.
[36.46 --> 39.06]  It was actually a security research.
[39.28 --> 43.22]  You know how security research firms, they publish these white papers that are like,
[43.28 --> 47.10]  hey, we hacked the crap out of the Jeep Grand Cherokee or something, right?
[47.44 --> 49.36]  They publish these sorts of things all the time.
[49.86 --> 51.22]  And some of them are pretty severe.
[51.34 --> 52.00]  Some of them aren't.
[52.06 --> 56.06]  But it's basically the way security research people make a name for themselves, gain publicity.
[56.74 --> 59.12]  It's how they demonstrate that they actually know what they're doing.
[59.12 --> 64.14]  And you might want to hire them for whatever it is that you hire a security research firm for.
[64.96 --> 71.76]  And they published this white paper that was basically on, or tech report, probably a better term for it,
[72.04 --> 77.36]  on how they took this humanoid robot by a company called Unitree, which I guess is a Chinese company.
[77.36 --> 80.84]  And they did a security analysis on it.
[81.00 --> 85.18]  And one of the reasons that they did that is, I guess, normally, like, humanoid robots,
[85.88 --> 88.06]  there aren't that many people who sell humanoid robots.
[88.18 --> 94.36]  But the people who do, I guess, typically they're not sold as active, secure actors.
[94.36 --> 95.06]  They're actors.
[95.28 --> 99.48]  Meaning, they just come with, like, I think the default configuration,
[99.58 --> 103.42]  if you bought one as a consumer of humanoid robots for some reason,
[103.78 --> 107.62]  you would just get one that didn't really have any security protocols or connectivity or anything.
[107.68 --> 110.52]  You'd just have, like, the firmware and some stuff built in,
[110.54 --> 112.08]  and you were going to do whatever you were going to do with it.
[112.10 --> 113.96]  If you wanted to secure it, you'd secure it, whatever.
[113.96 --> 118.26]  But I take it these Unitree ones, they have a security subsystem.
[118.36 --> 119.76]  It's supposed to all be encrypted.
[119.98 --> 121.18]  It's supposed to be secure.
[121.34 --> 125.90]  So that's, like, a different, it's not common, I guess, for robots, was what I gathered from this.
[126.40 --> 128.60]  Which seems really, that seems really bizarre, by the way.
[128.64 --> 129.48]  Can we just stop on that?
[129.72 --> 133.40]  Look at all these engineers sitting at their neat little desks.
[133.96 --> 136.66]  It takes dirty work to keep a code base clean.
[137.16 --> 140.58]  Every day, sickos are out there committing unreviewed code.
[140.58 --> 144.12]  And when that happens, linters won't save you.
[144.46 --> 146.12]  You need someone like me.
[146.38 --> 147.26]  Let's go!
[148.36 --> 149.64]  Feature-free, scrumbag!
[149.80 --> 151.04]  Who are you calling scrumbag?
[151.22 --> 152.84]  What's this slop you're trying to push?
[153.16 --> 154.18]  Unnecessary comments?
[154.60 --> 155.58]  Global state?
[156.06 --> 157.08]  Nested ternaries?
[157.38 --> 158.46]  Oh, my bad.
[158.62 --> 159.96]  I didn't even read the code yet.
[160.18 --> 161.12]  You disgust me.
[161.34 --> 162.38]  Step away from the keyboard.
[162.48 --> 163.34]  Just let me explain.
[163.76 --> 164.38]  Is that a mouse?
[164.62 --> 165.60]  She's marching to prod!
[165.86 --> 167.52]  You have the right to remain silent.
[167.72 --> 170.32]  Anything you push to GitHub, a cannon will be used against you.
[170.32 --> 171.68]  You have the right to a debugger.
[172.02 --> 175.38]  But if you cannot afford one, a public stack trace will be made available to you.
[177.00 --> 180.48]  And one more code criminal off the streets where they belong.
[181.14 --> 181.46]  HR.
[184.42 --> 186.66]  Look, I didn't yet...
[186.66 --> 188.50]  I know I didn't review any of the code.
[188.78 --> 191.02]  But I was going to have CodeRabbit review it from the start.
[191.32 --> 194.56]  With one-click fixes and style enforcement, I don't need MergeCop.
[194.56 --> 200.28]  I would never merge Unreviewed code, but a first pass with CodeRabbit always makes things go faster.
[200.52 --> 202.94]  Actually, you can try it too at CodeRabbit.ai.
[204.24 --> 206.28]  Next week on MergeCop.
[206.44 --> 209.40]  The diffler's out there, and I'm going to be the one to deprecate them.
[209.40 --> 220.02]  How is there not security in an exceptionally high liability zone here?
[220.08 --> 228.92]  Because this is something with arms and legs and possibly LLMs wandering around in your house, around children, around construction workers, around whoever.
[229.04 --> 229.60]  Who knows?
[229.74 --> 230.54]  How is this not like...
[230.54 --> 237.60]  No, the default when they're selling it, I think, is to not these guys, but if it's in general.
[237.76 --> 249.54]  You're selling it, I think, to some manufacturing facility who has a fleet of embedded engineers who put their own thing on top of it to do stuff for your manufacturing system.
[249.54 --> 251.78]  Oh, so this is like the chrome of robots.
[252.08 --> 252.54]  Right.
[252.54 --> 261.18]  Like, it's not like it comes pre-programmed to then, like, I can build cardboard boxes or something like that.
[261.26 --> 267.24]  Like, it comes as, like, I can move arms and legs, you have to plug in and then tell me what to do, is my guess.
[267.32 --> 280.50]  I mean, that's generally, I feel like what you see for, like, a lot of embedded stuff here is, like, these companies have huge, like, embedded engineer teams who then write firmware and software
[280.50 --> 283.08]  and a bunch of stuff to make it work for your thing.
[283.90 --> 284.50]  Could be wrong.
[284.52 --> 292.50]  Yeah, that was my understanding as well, was that, like, normally, you know, because it's only, you know, previously it would be only a sophisticated consumer,
[292.80 --> 303.88]  like a factory or research team that would be buying one of these things, they don't come with any kind of, like, pre-configured, this is exactly how it will operate, literally.
[304.06 --> 305.80]  It's expected that you're going to go do that.
[306.16 --> 310.00]  And so you would secure it and you would run whatever you wanted to run on it and those sorts of things.
[310.52 --> 315.38]  And so I imagine that this is the sort of thing we're going to start seeing more of now, what happened with this unitary thing,
[315.84 --> 323.34]  because people are going to, with all the AI boom and all of this, the money in it, people are going to be trying to sell more and more of these to more and more people.
[323.34 --> 332.92]  Like, oh, you just buy the humanoid robot and you show it the task and the, you know, AI training system just, like, learns to do it and you don't have to be sophisticated, right?
[333.24 --> 334.62]  I mean, so I'm guessing, yeah.
[334.62 --> 338.02]  Yeah, this is basically, like, how IoT happened, right?
[338.06 --> 348.54]  It's, like, before you would have, like, some hardware supplier who gives you, like, a set of cameras and then you would be like, okay, we've got our own guys to maybe, like, build something or do.
[348.74 --> 351.84]  And then it's like, oh, sick, you want to buy 50 cameras?
[352.10 --> 353.48]  Cool, you just bought a bot, Nat.
[353.48 --> 358.56]  Like, you're about to get mined for your own hardware.
[359.28 --> 360.94]  So does that mean I can just buy a robot?
[360.94 --> 361.50]  Quite literally, I think that's what we're talking about.
[361.62 --> 362.26]  Yes, trash.
[362.28 --> 363.48]  I can literally just go buy a robot?
[363.90 --> 369.94]  Well, I mean, this is actually shocking to me because my understanding, I just assumed that if I do buy one, it's already going to be secure.
[370.02 --> 374.82]  I didn't realize it would actually be, like, some raw, like, interface for someone to build something on top of.
[375.22 --> 378.34]  So that's kind of scary, but I'm also, I kind of want to buy one.
[378.34 --> 385.78]  Well, that's what Unitree is ostensibly trying to solve, right, is they're saying, like, we will give you a humanoid robot that can do tasks.
[386.30 --> 386.76]  That's what I'm saying.
[386.88 --> 391.80]  So my first thought when I read this article is, like, if I hack someone else's robots, what would I do with them?
[392.56 --> 393.68]  And what was your answer?
[394.00 --> 394.82]  Yeah, what was your answer?
[394.98 --> 399.32]  Probably, like, the laundry, like, at my house and then, you know, in my car.
[399.58 --> 402.74]  Like, very, very applicable things to my life.
[402.92 --> 404.90]  Like, you know, clean my car.
[405.08 --> 405.70]  I don't know.
[406.04 --> 406.86]  Like, all those things.
[406.86 --> 419.02]  Everyone's robots are walking towards California and they all end up at Trash's house and they're all just doing, like, there's hundreds of robots, like, attempting to mow his lawn and they're fighting over the lawnmower or whatever.
[419.16 --> 420.72]  Yeah, like, it's time to do my fall garden.
[420.88 --> 424.42]  I need, like, somebody to go pull out all the current plants, put the new ones in.
[424.48 --> 428.62]  So I was, like, in my mind, I was, like, this would be amazing if I just could hack everybody's robot.
[428.84 --> 429.04]  Right.
[429.04 --> 432.60]  It's like, like, Trash is the world's worst supervillain.
[432.80 --> 437.76]  He, like, executes his master plan and the entire result is, like, a well-manicured lawn.
[437.92 --> 442.20]  It's like, and now my lawn is perfectly in mode.
[442.20 --> 444.86]  And when they're done, I put them back.
[445.24 --> 446.52]  So that's what I'm saying.
[446.52 --> 449.04]  That still makes you a bad guy, Trash.
[449.36 --> 450.38]  I gave it back, though.
[450.94 --> 452.38]  I'm, like, 50% bad.
[452.46 --> 453.26]  50% bad.
[453.62 --> 454.54]  Not 100%.
[454.54 --> 454.80]  Okay.
[455.36 --> 456.74]  Misdemeanor not felony bad.
[456.84 --> 457.20]  Yeah, yeah.
[457.56 --> 459.54]  You're, like, a loitering kind of bad guy.
[459.78 --> 461.06]  Not necessarily like manslaughter.
[461.42 --> 461.68]  Mm-hmm.
[461.80 --> 462.10]  Mm-hmm.
[462.32 --> 462.72]  Okay.
[463.10 --> 465.64]  By the way, Casey, we've massively interrupted you.
[466.00 --> 466.10]  Okay.
[466.20 --> 466.62]  That's all right.
[466.62 --> 469.22]  So that's what the podcast, that's why we do this.
[469.32 --> 471.20]  I know, but I want to hear more about the story.
[471.20 --> 471.64]  That's why I'm here.
[471.74 --> 472.38]  People are confused.
[472.56 --> 473.26]  What is the story?
[473.34 --> 473.92]  What happened?
[474.38 --> 480.08]  So what happened was these Unitree robots come sort of with pre-configured software, right?
[480.10 --> 481.36]  It's got a security suite.
[481.48 --> 482.52]  It's got all this sort of stuff.
[482.60 --> 487.46]  It's got protocols that are set up for doing, they have various ones we've never heard of.
[487.46 --> 490.32]  Like, I'd never heard of these protocols, but they're for these kind of robotic stuff.
[490.32 --> 497.78]  MQTT and DDS, these are things for sharing, like, the state of the robot or, like, the
[497.78 --> 501.42]  LiDAR sensing from the robot, the camera images from the robot, like, all these things, they
[501.42 --> 502.60]  have this stuff.
[503.88 --> 511.06]  And so, actually, there was more, like, the headline was something like, you know, wormable
[511.06 --> 513.98]  exploit allows an attacker to take over the robots.
[513.98 --> 515.64]  And that was true.
[515.84 --> 520.58]  But believe it or not, that's not even possibly the worst of it.
[520.66 --> 524.96]  Like, that is the worst of it, but there's even more worst of it, right?
[525.22 --> 529.78]  So the first problem is the security is absolutely horrific.
[530.28 --> 534.22]  Like, it's got so many problems with it.
[534.64 --> 539.30]  Like, for example, every robot uses the same private key for all the encryption.
[539.30 --> 545.14]  That private key is there's no initialization vector, so, and it's in, um, it's in electronic
[545.14 --> 546.04]  codebook mode.
[546.18 --> 551.24]  So it's basically just, like, every block that you send is just flat encrypted with that
[551.24 --> 551.92]  private key.
[552.06 --> 554.02]  And the private key is the same for all robots.
[554.20 --> 558.82]  So as soon as you ever can decrypt, like, one, or even if you want to replay attack, you
[558.82 --> 563.78]  can just send a block from your robot that you use to some other robot, and it will just
[563.78 --> 566.48]  do that thing because it's the same all the time, right?
[566.54 --> 567.32]  No initialization vector.
[567.32 --> 571.32]  And it was part of the password is literally unitry.
[572.20 --> 573.64]  The name of the company.
[574.06 --> 574.44]  The password.
[575.02 --> 577.64]  It is literally the admin-admin situation.
[577.92 --> 580.50]  It's WordPress 1999 going on in this robot.
[581.00 --> 587.44]  They had an LCG, like, they had a linear congruential generator step that is literally, it turned
[587.44 --> 590.38]  out to be RAND from the Linux.
[590.52 --> 594.42]  Like, it was literally Linux RAND, GLib C's RAND.
[594.42 --> 598.34]  So the parameters for the linear congruential generator, which is not, like, no one would
[598.34 --> 600.98]  ever use an LCG for a serious security thing as far as I know.
[601.08 --> 606.82]  But, like, if you were going to use one, you'd at least use different parameters than RAND,
[606.92 --> 608.76]  which everyone has access to the parameters.
[609.16 --> 609.88]  So there was that.
[609.88 --> 617.66]  The wireless setup, like, the actual thing where you try to connect to the wireless on the device,
[618.12 --> 622.86]  you could actually just insert commands into that because they were unescaped and unchecked.
[622.86 --> 628.70]  So you could actually get root access just by putting commands into the login for wireless.
[628.70 --> 632.92]  Like, it was just like, I was just, I was like, what is happening?
[633.28 --> 634.46]  It was so nuts.
[634.68 --> 637.70]  And all of that, all of that.
[638.98 --> 646.86]  And then it also turns out that it's by default configured to just send all its telemetry data
[646.86 --> 650.52]  to server, to hard-coded IP addresses in China while it's operating.
[651.94 --> 654.26]  Not, you don't have to exploit it for this.
[654.32 --> 655.32]  It just does that.
[655.44 --> 656.06]  That's for free.
[656.06 --> 658.92]  Can we say the other thing that's crazy about it?
[658.96 --> 660.38]  Well, first I have a question for Trash.
[660.82 --> 662.32]  And then I have the next thing.
[662.40 --> 666.40]  So, Trash, I was wondering, just, like, by any chance,
[666.94 --> 670.76]  did you happen to work on the password management system for this?
[670.88 --> 671.38]  I don't know.
[671.76 --> 675.10]  But literally, my other reaction was like, yeah, this is something I would do.
[675.42 --> 676.36]  Like, I would totally just get it.
[678.12 --> 679.10]  I'd be so screwed.
[679.40 --> 682.26]  I'd be just like with my robot one day and then it just starts, like, spanking me.
[682.48 --> 683.84]  One password's good enough for me, bro.
[683.90 --> 685.40]  It's good enough for my robots, too.
[685.40 --> 685.84]  Yeah.
[686.96 --> 689.84]  Also, one little fun fact we did leave out of that little description.
[690.02 --> 696.16]  As part of this whole thing, the security researchers who figured this all out reported this to Unitree,
[696.56 --> 698.64]  who effectively just went dead silent on them.
[699.14 --> 704.50]  And so how they responded was tweeting out the private keys to the robot on Twitter,
[705.16 --> 708.70]  formerly known as Twitter, formerly known as Twitter, the Everything application.
[708.70 --> 711.42]  They just tweeted out two private keys and that's that.
[711.48 --> 712.34]  So it's just, like, out there.
[712.48 --> 714.36]  Like, it's just for free.
[714.70 --> 719.40]  And then they just never responded to anything until, like, what, a week ago?
[719.70 --> 722.48]  They made a LinkedIn post and just said, hey, we're addressing things.
[723.34 --> 723.70]  And like that.
[723.70 --> 725.50]  Like, it is funny that it was on LinkedIn.
[725.64 --> 727.20]  I'm going to go ahead and assume that they're not really addressing anything.
[727.36 --> 727.58]  Yeah.
[727.58 --> 730.40]  The thing – well, there's a bunch of things.
[730.40 --> 742.00]  The other thing that's crazy that I think we didn't make super clear is – so this thing happens because of some, like, Bluetooth to Wi-Fi situation.
[742.00 --> 742.30]  Convenience.
[742.30 --> 743.62]  Setting up the robot with this.
[744.14 --> 758.84]  So because this is in this, like, Bluetooth wireless thing, if you infect one of them and then that robot gets next to another robot, you can make it do the same exploit.
[759.02 --> 762.26]  It's literally the first computer virus.
[762.60 --> 768.88]  It affects the other humanoid robots by contact, which is so funny.
[768.88 --> 769.40]  By proximity.
[769.40 --> 773.68]  It is, like, literally, like, stand six feet away or else your Bluetooth is going to get taken over.
[774.46 --> 774.98]  That's right.
[775.34 --> 777.30]  You need to social distance your robots.
[777.62 --> 777.88]  Yes.
[777.88 --> 780.02]  And the social distancing range is Bluetooth range.
[780.02 --> 781.72]  They have to be far and away apart from each other so that they can't get infected.
[781.94 --> 783.20]  If they put on masks, are they okay?
[783.76 --> 783.92]  Yeah.
[784.02 --> 784.34]  Are we good?
[784.56 --> 784.98]  That's good.
[786.40 --> 786.80]  Sorry.
[786.80 --> 808.20]  So the interesting thing about that, too, is it's just, like, it's a good reminder a little bit of we're entering a world now where the ability to exploit the things that we have is at an all-time high because software quality is, like, at, like, rock, rock, rock bottom.
[808.20 --> 817.60]  And the types of things we are building are starting to be able to do stuff like move between physical locations themselves.
[817.76 --> 818.90]  Things like drones.
[819.84 --> 821.48]  Things like humanoid robots.
[822.14 --> 826.98]  Things like cars that have, like, the ability to control their steering wheel and brakes, like, you know, self-driving.
[826.98 --> 831.82]  So we're getting to the point where, like, the computers aren't contained anymore.
[832.02 --> 834.06]  Like, Skynet is on the way, right?
[834.14 --> 843.18]  Like, the things can come after you literally or after each other in ways that was not previously on the roadmap, right?
[843.46 --> 845.84]  And we're not quite there yet.
[845.90 --> 855.04]  Like, there aren't enough things with this kind of autonomy yet, but we're pretty close, especially with self-driving cars and maybe with those, like, aero drone things.
[855.04 --> 856.44]  There's enough of them now.
[856.90 --> 860.84]  It's starting to feel, like, not fabulous, right?
[861.22 --> 868.06]  And I don't think there's a solution other than get your EMP devices ready, folks.
[868.32 --> 877.04]  So I've had this kind of, like, theory about how the world will end, and it's always been with robots, and it's always been with robots and exploits.
[877.12 --> 880.56]  Because this is, like, my idea is that we're going to invent robots one day that can fold our laundry.
[881.24 --> 882.66]  And then every person in the end.
[882.66 --> 883.18]  Trash is laundry.
[883.50 --> 883.70]  Right.
[883.80 --> 884.82]  Trash is laundry specifically.
[885.04 --> 889.10]  So then every person in a nation will have a robot that's just doing all the menial tasks.
[889.18 --> 894.36]  If you ever read Way of the Kings, Stormlight Archives, it'd be, like, the Parchment, right?
[894.70 --> 899.44]  There's Parchment everywhere throughout the entire, you know, land.
[899.88 --> 902.18]  And then someplace, China or whatever.
[902.32 --> 905.54]  They already have, it looks like, I mean, honestly, this unitry is so bad it looks like it's intentional.
[905.70 --> 906.84]  That's even what the article says.
[906.94 --> 909.00]  It's, like, it actually looks like it's intentional at this point.
[909.00 --> 909.32]  Yeah.
[909.32 --> 914.28]  That they have a back door that one day they can flip on, and then robots go into, like, not nice mode.
[914.78 --> 914.90]  Yeah.
[914.90 --> 915.48]  And hurt people.
[915.64 --> 920.78]  And then it's just, like, you have a robot within 15 feet of a person all throughout a country.
[920.78 --> 924.84]  You could actually have an entire country, theoretically in this universe, disappear.
[924.84 --> 931.70]  Like, every last person just, like, just disappear in a day, in, like, 30 minutes, which has just never really been feasible.
[932.14 --> 937.52]  And now we're starting to, like, at least in my personal sense, I just feel like I can see it actually possibly happening.
[937.52 --> 941.82]  Just maybe not intentionally, just by accident with how bad things are programmed.
[942.72 --> 944.24]  We're literally in a movie right now.
[944.78 --> 945.88]  That's literally what's happening.
[945.90 --> 947.32]  No, we're on a podcast, Trash.
[947.80 --> 948.16]  Okay.
[948.32 --> 949.18]  This is a podcast.
[950.34 --> 951.20]  Whatever, guys.
[951.22 --> 952.04]  You know what I'm saying.
[952.22 --> 953.66]  You know what I'm saying, okay?
[953.66 --> 962.16]  I also, like, I don't, I mean, I'll be completely honest, but, like, I also just don't really understand.
[963.10 --> 967.70]  I know why people do it, because they just want money.
[968.14 --> 973.78]  But, like, I actually don't understand from, like, a humanistic perspective.
[973.78 --> 984.48]  Like, I, there are things that I don't want to do in life, but most of those we now already have reasonable automation for.
[984.64 --> 988.36]  And, like, I just don't fundamentally mind doing my laundry.
[988.36 --> 1003.00]  So, if the question was, you can have a wormable robot army that could take over the world, or you could spend 15 minutes moving my clothes down to the washing machine, which already does the laundry for me.
[1003.06 --> 1004.20]  I just have to put it in.
[1004.76 --> 1006.92]  I'm just like, what is wrong with people?
[1007.06 --> 1011.66]  Like, what, can't you think of something better to do with your life than make this stuff?
[1011.66 --> 1013.04]  I just don't understand.
[1013.28 --> 1022.34]  Like, we're kind of at the point where the things that humans are doing, a lot of it is things that humans want to do or aren't that unhappy doing.
[1022.56 --> 1029.20]  It's not really like the days when we were doing backbreaking manual labor for, like, 12 or 14 hours a day.
[1029.20 --> 1037.24]  And it was like, oh, my God, like, being able to have something like an automated harvesting machine would be absolutely amazing and transform our lives in meaningful ways.
[1037.56 --> 1042.12]  Now it's like, hey, yeah, you didn't have to actually go to the restaurant.
[1042.30 --> 1047.64]  The automated drone delivery picked up your, like, Chinese food carton and brought it to your door.
[1047.70 --> 1055.44]  It's like, okay, yeah, maybe that's worth doing if you can absolutely guarantee that, like, we don't have Terminator as the future.
[1055.44 --> 1060.74]  But if you can't, like, I could go to the freaking store and get my own Chinese food.
[1060.86 --> 1062.60]  Like, what the hell is wrong with you people?
[1062.76 --> 1070.10]  So at some level, I feel like we're at this point where people are creating Skynet for no actual reason.
[1072.22 --> 1073.16]  That's pretty funny.
[1073.38 --> 1079.80]  The whole time I was listening to that, I was like, man, I would love not to do laundry.
[1080.38 --> 1080.78]  You are the problem.
[1080.78 --> 1082.08]  And I pick up Chinese food.
[1082.30 --> 1083.60]  I was like, Casey hates me.
[1083.60 --> 1085.64]  Oh, my Lord.
[1085.64 --> 1087.16]  Josh is like, don't say anything.
[1087.26 --> 1087.92]  Don't say anything.
[1088.06 --> 1088.88]  Don't stay in my lane.
[1088.88 --> 1090.52]  I was like, I would like that.
[1090.66 --> 1091.38]  I would like that.
[1091.56 --> 1092.12]  I would like it.
[1092.40 --> 1092.86]  I would like it.
[1092.86 --> 1093.48]  It's worth it.
[1093.74 --> 1094.12]  Worth it.
[1094.26 --> 1094.76]  I'm just kidding.
[1095.10 --> 1098.10]  Like, realistically, I would never, like, I don't do the smart home stuff.
[1098.16 --> 1099.44]  I don't do any of that.
[1099.64 --> 1102.28]  I mean, I do, like, have, like, a car that has, like, the Wi-Fi stuff.
[1102.28 --> 1108.40]  But, like, I don't want to, I don't know, ping an API across the world to, like, open my fridge or something.
[1108.56 --> 1109.60]  Like, that doesn't make any sense.
[1110.08 --> 1113.12]  So, if I may, like, let me just make sure I got this right.
[1113.12 --> 1121.94]  So, if the opening of Terminator was, like, the tank treads, rolls over the human skull, and it just crushes, right?
[1122.06 --> 1122.84]  Classic scene.
[1123.04 --> 1123.62]  Classic scene.
[1123.62 --> 1134.26]  And then, like, it's you kind of, like, over, like, you know, with some kind of, like, heavy weapon in your hands, like, pressed up against some, like, dirt bunker, right?
[1134.30 --> 1138.12]  And your face is all, like, half-blooded, and, like, you've seen all this stuff.
[1138.48 --> 1142.94]  And you're there, and you're like, man, war, this war against machines is brutal.
[1142.94 --> 1146.36]  But it was worth it for those five years of Chinese food.
[1147.70 --> 1151.38]  Is that basically, like, how the opening of Terminator goes in your world, Triathlon?
[1151.38 --> 1156.34]  No, but what'll be funny is, as I'm in the bunker, a robot comes up to me and, like, hands me some food.
[1156.84 --> 1160.22]  And then I continue shooting my blaster.
[1161.04 --> 1161.72]  Yeah, yeah.
[1162.04 --> 1165.52]  He's like, not all robots got infected by the Bluetooth virus, man.
[1165.58 --> 1167.98]  Some are still delivering Chinese food well.
[1167.98 --> 1175.56]  But the workaround, did the article say the workaround is, like, use some, like, isolated Wi-Fi, like, for now, to, like, get rid of that?
[1175.56 --> 1183.16]  The workaround, I mean, you can do a number of things, but if anyone comes close to it, within Bluetooth range, right?
[1183.92 --> 1187.60]  I mean, the workaround is run the exploit yourself and install better software.
[1188.22 --> 1188.76]  That's funny.
[1189.44 --> 1197.38]  So I'm going to be, I'm going to maybe put a little bit of water on your fiery speech there, Casey, in the sense that,
[1197.38 --> 1202.72]  I actually have a much more black-pilled viewpoint of success of software.
[1203.18 --> 1205.14]  Can you remind me which pills are which?
[1205.34 --> 1206.56]  So black pill means, like, hopeless.
[1207.66 --> 1209.70]  It's kind of like a hopeless view of software success.
[1210.18 --> 1212.64]  In the sense, it's like, even if you just look at Chad Jippity.
[1213.14 --> 1217.52]  Chad Jippity, if you got Sam Altman in front of Congress being like, I'm in it for the love of the game.
[1217.58 --> 1218.38]  We're curing cancer.
[1218.44 --> 1219.54]  We're taking it home, boys.
[1219.58 --> 1220.98]  We're going to make the world a better place.
[1221.56 --> 1227.08]  Fast forward two years later, they're like, dude, we got Sora TikTok, and we're now doing Erotica next, right?
[1227.08 --> 1231.72]  Like, it doesn't feel like software, like, goes to, like, these amazing heights.
[1231.72 --> 1236.22]  It always feels like it's just, like, what's the most disappointing level something can get to,
[1236.30 --> 1239.22]  and it's going to get right below that and be slightly more disappointing.
[1239.62 --> 1240.72]  Like, that's just what happens.
[1240.80 --> 1242.48]  And so it's like, oh, robots, they're coming.
[1242.86 --> 1246.20]  Yeah, in, like, 50 years they might be different, but today, for the next five years,
[1246.24 --> 1248.78]  they're just going to be really bad at everything they do.
[1248.78 --> 1253.76]  So the Black Pilger is basically like, look, there's not going to be Skynet,
[1253.88 --> 1256.38]  because these things will just start tripping over themselves,
[1256.56 --> 1257.90]  and they won't be able to shoot the gun.
[1258.02 --> 1259.94]  They'll try to shoot the gun, and they'll just fly backwards.
[1260.80 --> 1261.72]  It'll be more like this.
[1261.72 --> 1263.16]  You just think the incompetence will save us.
[1263.20 --> 1266.82]  Our own incompetence will both cause the robot uprising and stop it.
[1266.92 --> 1267.54]  It'll be like this.
[1267.60 --> 1270.34]  It'll be like, oh, man, dude, the robot uprising was going to happen,
[1270.34 --> 1274.86]  but then I forgot my password to my Google account because I lost my phone,
[1275.00 --> 1278.08]  so I, like, couldn't log in, and so then my robot couldn't turn on
[1278.08 --> 1279.16]  because I couldn't log into Google.
[1279.82 --> 1281.10]  I was just like, man.
[1281.84 --> 1282.30]  It was so close.
[1282.30 --> 1285.10]  It does feel that way a little bit with the AI stuff.
[1285.20 --> 1286.48]  They're like, you don't understand.
[1286.58 --> 1289.24]  It's going to write all the code in the world, and it's going to change everything.
[1289.28 --> 1290.26]  It's going to revolutionize the world.
[1290.26 --> 1295.16]  And then later on, they're like, so we need you to watch these ads
[1295.16 --> 1298.22]  that we're going to insert in between the responses.
[1298.22 --> 1300.66]  And you're just like, wait, what?
[1300.88 --> 1305.44]  Like, in what timeline did you need to do that if this stuff was that sophisticated?
[1305.72 --> 1309.82]  They're like, well, we just need a little more time to get there, I guess.
[1310.38 --> 1310.52]  Yeah.
[1310.62 --> 1313.72]  So anyways, I'm a little bit blackpilled on the success of software.
[1314.30 --> 1314.64]  Okay.
[1315.06 --> 1315.52]  Fair enough.
[1315.52 --> 1315.78]  You know.
[1316.12 --> 1316.84]  Totally reasonable.
[1317.08 --> 1319.30]  That's actually not horrible, I guess.
[1319.46 --> 1321.62]  It's not as bad as the robot uprising, for sure.
[1322.30 --> 1322.54]  Yeah.
[1322.94 --> 1323.50]  That's true.
[1324.30 --> 1326.82]  Are there a lot of people that have these robots to begin with?
[1327.14 --> 1327.90]  I've got three.
[1328.50 --> 1328.68]  Oh.
[1329.64 --> 1330.26]  No, I just.
[1330.48 --> 1331.74]  I was like, hold on.
[1331.84 --> 1332.46]  Give me one.
[1332.64 --> 1335.32]  They're just hugging each other right now, just huddled in the corner like I am legend.
[1335.74 --> 1336.62]  Like the vampire's like.
[1337.02 --> 1338.14]  He just pans his camera.
[1339.32 --> 1339.50]  Yeah.
[1339.92 --> 1341.84]  How do you guys think I have time for this podcast, bro?
[1341.94 --> 1344.30]  I'm laundry maxing right now with my robot.
[1349.08 --> 1350.36]  It's a real concern, okay?
[1350.82 --> 1351.04]  Yeah.
[1351.14 --> 1351.60]  Let's pile it up.
[1351.60 --> 1353.24]  They wrote this on the whiteboard behind me.
[1353.30 --> 1354.60]  Like, I'm not going to touch a whiteboard.
[1354.72 --> 1355.68]  A physical thing?
[1356.00 --> 1356.32]  Disgusting.
[1356.32 --> 1357.22]  I've got robots for that.
[1357.22 --> 1357.56]  I'm getting one.
[1357.68 --> 1358.24]  I'm getting one.
[1358.74 --> 1358.90]  Yeah.
[1358.90 --> 1360.02]  So what happens?
[1360.24 --> 1361.22]  Let's just pretend robots do come out.
[1361.22 --> 1367.28]  I like the idea that, like, the AI bro, like, bragging list keeps getting, like, reduced
[1367.28 --> 1372.50]  and stacked to, like, yo, man, if you're folding your shirts yourself, you're never going to
[1372.50 --> 1373.34]  get ahead in this world.
[1373.82 --> 1374.22]  Wait.
[1374.22 --> 1374.26]  Wait.
[1374.32 --> 1376.94]  How did we go from this to that?
[1377.20 --> 1383.60]  It'll be like the Sigma chat edits, and it's like, and the guy's like, folding your laundry
[1383.60 --> 1385.02]  takes 15 minutes every day.
[1385.14 --> 1385.98]  I don't do that.
[1386.12 --> 1386.98]  So you know what that means?
[1387.18 --> 1388.36]  15 times seven.
[1388.64 --> 1390.06]  That's 105.
[1390.60 --> 1392.16]  105 minutes a week times 50.
[1392.82 --> 1397.10]  5,217 minutes a year that I have that you don't have.
[1397.36 --> 1398.50]  You got to keep up with me.
[1398.50 --> 1399.38]  Was that an accurate number?
[1399.38 --> 1399.66]  Yes.
[1399.66 --> 1401.02]  Was that 5,000 number accurate?
[1401.80 --> 1402.62]  I don't know, Trash.
[1402.74 --> 1403.38]  I just was doing 50.
[1403.38 --> 1404.00]  Well, I believed you.
[1404.06 --> 1404.86]  I was like, oh, my God.
[1404.90 --> 1406.46]  His math is so hard right now.
[1407.12 --> 1407.44]  Trash.
[1407.44 --> 1409.52]  He said 105 times 50.
[1411.56 --> 1412.62]  What's 50 times?
[1412.74 --> 1412.96]  Okay.
[1413.00 --> 1413.34]  Never mind.
[1413.64 --> 1414.70]  We can just go on.
[1414.90 --> 1415.64]  Just go on.
[1415.70 --> 1417.10]  Are you still doing math in your head?
[1417.20 --> 1418.50]  We have calculators for that.
[1418.68 --> 1420.26]  All the math I did do in my head.
[1420.38 --> 1423.74]  I don't even know how much time I saved, but my calculator does.
[1423.98 --> 1428.18]  So I'm going to run my calculator, and after it's done telling me how much time I saved,
[1428.18 --> 1429.78]  I'm going to yell at you about it.
[1429.78 --> 1429.98]  Yeah.
[1430.04 --> 1430.60]  Shut up, Boomer.
[1431.14 --> 1433.78]  In this house, calculators do math.
[1433.78 --> 1434.14]  Yes.
[1434.40 --> 1434.76]  Yes.
[1434.76 --> 1436.84]  Alexa, what's 50 times whatever number he said?
[1439.74 --> 1440.72]  I'm going to go do.
[1440.72 --> 1442.54]  I'm ordering 12,000 bananas.
[1442.92 --> 1443.14]  No.
[1443.22 --> 1443.46]  No.
[1443.54 --> 1443.94]  Alexa.
[1444.12 --> 1444.42]  Stop.
[1444.60 --> 1444.84]  Stop.
[1445.00 --> 1445.14]  Stop.
[1447.26 --> 1448.24]  Hey, Siri.
[1448.66 --> 1450.02]  Let's get everybody's phone.
[1451.88 --> 1452.58]  Oh, man.
[1452.72 --> 1452.98]  Okay.
[1453.04 --> 1457.58]  So let's just pretend for a second that all these things actually end up coming true,
[1457.58 --> 1462.52]  and we kind of start living more and more towards the AI bro world where you're just
[1462.52 --> 1464.16]  letting AIs write all of your code.
[1464.36 --> 1466.20]  You got AIs folding all of your laundry.
[1467.02 --> 1467.22]  Yeah.
[1467.28 --> 1469.66]  What are you going to actually do in life?
[1470.74 --> 1471.04]  Yeah.
[1471.18 --> 1472.84]  I always want to ask the AI bros that.
[1473.62 --> 1476.30]  So when I have AI write my code, I have to do code review.
[1476.56 --> 1479.26]  So do we have to start doing laundry review with AI?
[1479.38 --> 1483.72]  Do I have to go back and make sure before we merge it into my drawers?
[1483.72 --> 1486.42]  I'm like, all right.
[1486.52 --> 1487.48]  I'm going to go check it out.
[1487.62 --> 1489.24]  I got to get GitHub Laundry Hub.
[1489.80 --> 1493.18]  Do you actually fold your shirts?
[1493.42 --> 1494.42]  Do you actually fold your shirts?
[1495.12 --> 1495.92]  This is what I do.
[1495.98 --> 1496.42]  Let me show you.
[1496.86 --> 1497.06]  Yeah.
[1497.08 --> 1497.72]  Let's see, Trash.
[1497.82 --> 1499.04]  I have like laundry behind me.
[1499.16 --> 1500.44]  That's my new robot.
[1500.72 --> 1501.14]  Don't worry.
[1501.22 --> 1501.84]  We can see it.
[1501.84 --> 1505.84]  I go like this, and then I just go like that, and then I just roll it up.
[1507.08 --> 1508.46]  You're a roller full-time.
[1508.58 --> 1509.06]  Full-time roller.
[1509.06 --> 1512.46]  And then I just have like a whole stack of them just like roll like scrolls in a library.
[1514.34 --> 1515.62]  Libraries don't have scrolls, Trash.
[1515.78 --> 1518.30]  Like maybe like a thousand years ago they had scrolls.
[1518.32 --> 1519.98]  Well, they used to, okay?
[1520.34 --> 1521.70]  They used to at one point in time.
[1521.70 --> 1523.08]  Well, if you go to a good library, they've got scrolls.
[1523.08 --> 1523.26]  Yeah.
[1523.28 --> 1524.46]  What kind of libraries are you going to?
[1524.46 --> 1525.82]  A crappy municipal library.
[1526.60 --> 1527.50]  You go to some stupid libraries.
[1527.50 --> 1532.24]  I go to the British Royal Library, and I read scrolls because I want the actual truth.
[1532.68 --> 1533.70]  If it's not on Popeye's.
[1533.70 --> 1534.56]  You guys are reading books?
[1534.56 --> 1535.48]  You're not living life.
[1535.48 --> 1541.22]  If you read a book that's printed on a printing press, you're just reading something that was
[1541.22 --> 1545.90]  written by someone who read a scroll at some point, and is regurgitating that to you,
[1546.14 --> 1550.00]  probably with a bunch of lies from the establishment baked into it.
[1550.16 --> 1550.42]  Yeah.
[1550.94 --> 1551.70]  Scrolls only.
[1551.98 --> 1553.12]  Everything came from scrolls.
[1553.36 --> 1553.86]  Changed my mind.
[1555.08 --> 1560.10]  That's like if you think software that's lasted a long time is more likely to keep being here tomorrow,
[1560.76 --> 1564.44]  scrolls that have been here a long time are more likely to be relevant tomorrow too.
[1564.44 --> 1568.20]  So it's kind of big brain strategy that trash only reads scrolls.
[1568.24 --> 1569.24]  I respect that trash.
[1569.46 --> 1570.14]  That's right.
[1570.46 --> 1570.68]  Yeah.
[1571.20 --> 1571.94]  Only scrolls.
[1571.94 --> 1572.68]  So question.
[1572.84 --> 1579.88]  Can we try to get Claude Fold as a sponsor to this, like the first like laundry based,
[1580.24 --> 1582.92]  like, like large LLM, large laundry model?
[1583.08 --> 1587.88]  Can we get the first large laundry model provider to like sponsor this podcast where we've been
[1587.88 --> 1589.42]  talking so positively about laundry?
[1589.42 --> 1595.74]  Uh, cause I feel like that's, that's where the money's going to be next, right?
[1595.76 --> 1598.90]  Like none of this, like a video generation or whatever it is.
[1598.90 --> 1600.18]  That's like, that's not interesting.
[1600.34 --> 1601.24]  It's, it's laundry, baby.
[1601.46 --> 1602.14]  Everyone's got it.
[1602.24 --> 1603.16]  Everyone needs to fold it.
[1603.98 --> 1604.60]  It's true.
[1605.32 --> 1605.66]  True.
[1605.76 --> 1608.00]  Not everyone has to write code, but everyone has to fold laundry.
[1608.36 --> 1609.52]  Prime asked a real question.
[1609.52 --> 1610.54]  So let's consider this.
[1610.60 --> 1613.20]  Let's try to, let's try to add some humanity back to this podcast.
[1613.42 --> 1613.68]  Sorry.
[1613.68 --> 1614.40]  Um, I'm ready.
[1614.56 --> 1617.60]  He asked a real question, which was like, what do you, and I do wonder this.
[1617.68 --> 1618.70]  I was like, what do you want to do?
[1618.72 --> 1620.02]  Especially when you're talking about it.
[1620.02 --> 1622.32]  You guys can, can explain this to me too.
[1622.62 --> 1625.30]  It's like, look, you guys were generating AI music.
[1625.30 --> 1628.92]  Like music is something that humans are supposed to do for themselves.
[1628.92 --> 1633.48]  You know, it's like part of like the human experience is to like make music and like sing
[1633.48 --> 1634.38]  and like play an instrument.
[1634.70 --> 1640.08]  And like a good question is like, it's feels kind of dehumanizing to have an AI do it.
[1640.08 --> 1645.34]  Whether you like the song that comes out of it or not, it's like, it feels a bit soulless.
[1646.12 --> 1646.48]  Comments?
[1647.22 --> 1648.06]  No, I agree with that.
[1648.52 --> 1649.38]  I agree with that.
[1650.10 --> 1650.34]  Okay.
[1650.70 --> 1652.68]  Casey, let me hit you with something just for a quick second.
[1652.74 --> 1653.22]  Hit me up.
[1653.72 --> 1656.58]  Uh, when you generate AI music, you know, it comes out.
[1657.52 --> 1658.54]  People's music.
[1658.54 --> 1658.90]  Yeah.
[1659.50 --> 1660.40]  Stolen music.
[1660.62 --> 1660.90]  Basically.
[1661.36 --> 1664.38]  Baby, baby powder covered slappers.
[1664.54 --> 1664.76]  Okay.
[1664.78 --> 1667.92]  We're talking about some of the finest music in the industry today.
[1668.52 --> 1669.46]  And you know why?
[1670.08 --> 1672.66]  Because modern music is soulless.
[1672.78 --> 1673.18]  Okay.
[1673.34 --> 1675.70]  And the AI can just regurgitate that stuff.
[1675.92 --> 1679.08]  So he's like, all right, you got four chords and just a snare drum.
[1679.50 --> 1680.22]  We got music.
[1680.32 --> 1680.54]  Okay.
[1680.60 --> 1682.18]  Throw a little female vocals on it.
[1683.00 --> 1683.44]  Boom.
[1684.58 --> 1685.28]  I think.
[1685.42 --> 1686.34]  So that might be.
[1686.60 --> 1688.00]  That would be something I'd point out.
[1688.12 --> 1688.24]  Right.
[1688.54 --> 1688.90]  Oh, go ahead.
[1688.96 --> 1689.44]  Sorry, Casey.
[1690.04 --> 1690.94]  That would be something I'd point out.
[1691.02 --> 1693.92]  It's like, it's happening at the worst time.
[1693.92 --> 1697.40]  Because basically what we're doing is we're pouring gasoline on a bad fire.
[1697.54 --> 1697.72]  Right.
[1697.72 --> 1702.68]  It's like, we already kind of had this place where like modern music distribution was increasingly
[1702.68 --> 1707.52]  becoming about like, you know, how do you just generate another version of the latest
[1707.52 --> 1708.90]  random pop song?
[1708.90 --> 1715.78]  And, and like, now it's like literally generate, not just generate by having some producers
[1715.78 --> 1717.88]  in a room who monkey with the like thing.
[1717.92 --> 1721.20]  But now it's like, we just need an AI that can generate that song again.
[1721.20 --> 1724.34]  Like, you know, did you, you know, did you ingest all the Taylor Swift songs?
[1724.38 --> 1726.78]  Just put out another one of those if you could, please.
[1726.78 --> 1731.58]  And we don't even, you know, we're not even going to have like people actually work on
[1731.58 --> 1731.94]  it anymore.
[1731.94 --> 1735.20]  And, and I do think like, that's kind of, I don't know.
[1735.28 --> 1739.28]  That's really unfortunate because I feel like we don't want to accelerate that trend, but
[1739.28 --> 1743.20]  we are sort of, or maybe, maybe trash.
[1743.36 --> 1745.36]  If you're right, what will happen is the opposite.
[1745.92 --> 1749.44]  Everyone in the world will just pump that stuff out and humans will become very bored
[1749.44 --> 1749.74]  of it.
[1749.74 --> 1754.44]  And then the actual value of music created by actual people will go up again.
[1754.54 --> 1755.38]  That could happen too.
[1755.42 --> 1755.70]  I guess.
[1755.76 --> 1756.16]  I don't know.
[1756.52 --> 1758.78]  I mean, all I do is listen to music from 20 years ago.
[1758.96 --> 1761.20]  Plus I don't even listen to anything in this.
[1761.46 --> 1763.40]  Except for you love French kiss and AI.
[1763.64 --> 1763.88]  Okay.
[1763.88 --> 1765.64]  That was one of the, that was a bopper.
[1766.54 --> 1767.64]  That is a good song.
[1768.28 --> 1774.84]  Um, the thing I would say for it though, is that I think, I don't know what the answer
[1774.84 --> 1778.52]  is to this, but I at least see like a parallel in that.
[1778.52 --> 1787.98]  Uh, computers are way better at chess than humans are, but like the, a mildly good computer
[1787.98 --> 1791.64]  chess engine can beat Magnus Carlson is my under standard.
[1792.04 --> 1792.96]  I'm sorry, Magnus.
[1792.96 --> 1796.24]  If you're out there listening to this pod and that's not true, I take it back.
[1796.30 --> 1800.94]  Uh, but definitely the best chess engines can still beat, uh, Magnus Carlson.
[1800.94 --> 1801.16]  Right.
[1801.22 --> 1804.78]  And like chess is more popular than ever.
[1805.40 --> 1805.96]  Right.
[1806.18 --> 1808.06]  Like it's literally more popular.
[1808.06 --> 1808.58]  What?
[1808.80 --> 1809.24]  Yeah.
[1809.24 --> 1809.80]  Mind us.
[1809.94 --> 1810.36]  It's the most popular it's ever been.
[1810.68 --> 1812.44]  No, it's by far the most popular it's ever been.
[1812.92 --> 1813.96]  Like you can look up anyone.
[1813.96 --> 1818.56]  People watch chess streams and they have like these like internet chess tournaments and there's
[1818.56 --> 1819.76]  all this, which was never possible.
[1820.12 --> 1820.82]  Uh, that's fair.
[1821.04 --> 1821.18]  Yeah.
[1821.30 --> 1821.50]  Yeah.
[1821.50 --> 1829.44]  So it's just, it's at least not like a, you know, sure thing that just cause a computer
[1829.44 --> 1834.84]  can do something better than people that then we're like done doing it as humans.
[1834.88 --> 1836.96]  Like we still like playing chess.
[1837.02 --> 1838.88]  We still like watching people play chess.
[1838.88 --> 1842.64]  We still like learning chess and learning it for ourselves.
[1842.64 --> 1848.04]  Even though like I could just look at stock fish every move and then I would play a perfect
[1848.04 --> 1852.94]  game, but that that's not like fun or enjoyable and there's no struggle or anything like that.
[1852.94 --> 1858.50]  So I, I think like maybe AI could be like, for me, it would be sick.
[1858.50 --> 1862.76]  Like as someone who only can play drums, if I was playing more drums, it would be sweet
[1862.76 --> 1868.06]  to make the rest of the pieces of a song and have AI play it and play drums along with it.
[1868.06 --> 1874.44]  Whereas I would never be able to like commission a bass player, a guitar player.
[1874.44 --> 1879.42]  And you know, like it'd be cooler to be part of a band, but like trash keeps, uh, not responding
[1879.42 --> 1880.14]  to my DMS.
[1880.54 --> 1882.48]  So that's like one.
[1882.66 --> 1883.94]  That's the best one I can do.
[1884.66 --> 1885.62]  Dude, next time.
[1885.70 --> 1887.48]  Wait, what have we got a whole band here?
[1887.48 --> 1888.64]  I can play keyboards.
[1889.22 --> 1890.06]  What have we got?
[1890.16 --> 1891.36]  I can play bass and guitar.
[1891.54 --> 1892.36]  I can play bass and guitar.
[1892.36 --> 1894.18]  Dude, we've got a band, man.
[1894.30 --> 1895.44]  We can play.
[1895.62 --> 1896.60]  I didn't say I'm good.
[1896.60 --> 1899.76]  Next time at the tower, there's a, there's a band.
[1900.68 --> 1902.62]  Dude, it would be pretty sweet to play some blues.
[1902.62 --> 1906.94]  Like if we just got down and did some, the blues songs got plankers taking our jobs.
[1906.94 --> 1907.70]  What's going on?
[1907.70 --> 1909.14]  Blues requires a lot of talent.
[1909.40 --> 1915.86]  I think we should do a live in-person stand-up one time at a place and we will close it with
[1915.86 --> 1916.88]  a live song.
[1917.48 --> 1919.62]  Yeah.
[1919.82 --> 1920.44]  I can play.
[1920.80 --> 1921.24]  I can do it.
[1921.24 --> 1926.26]  TJ's always, TJ has the same, uh, same desire that every pretty much high school boy has
[1926.26 --> 1927.96]  at some point, which is to be a famous musician.
[1927.96 --> 1930.36]  So if TJ could be on, like on stage right now.
[1930.36 --> 1930.88]  I was so close, guys.
[1931.02 --> 1934.02]  My band, Emergency Exits, we were so close.
[1936.02 --> 1937.42]  We almost made it.
[1938.20 --> 1938.50]  Okay.
[1939.26 --> 1940.18]  A.K.A.
[1940.32 --> 1941.16]  Sounds of Silver.
[1941.28 --> 1942.32]  We could never decide.
[1942.48 --> 1943.66]  Broke up the band after the name.
[1943.66 --> 1946.24]  It's a tough story, but well, you know, it's what it is.
[1946.24 --> 1946.74]  It is what it is.
[1946.90 --> 1949.50]  I did music for like three years touring and then.
[1950.54 --> 1951.06]  I'm worried.
[1951.54 --> 1951.76]  Yeah.
[1952.98 --> 1955.68]  I'm not going to tell you anything besides that, but.
[1955.84 --> 1957.98]  Oh, we can find it out.
[1958.12 --> 1958.40]  Trash.
[1958.40 --> 1958.62]  Yeah.
[1958.70 --> 1959.00]  We're going to.
[1959.08 --> 1959.12]  We're going to.
[1959.12 --> 1961.46]  If you find it out, please do not broadcast it.
[1961.68 --> 1962.34]  Oh, no.
[1964.38 --> 1964.74]  What?
[1965.16 --> 1965.80]  No, it was fun.
[1965.86 --> 1968.08]  I did like a Warped Tour and some other stuff.
[1968.16 --> 1968.72]  It was pretty fun.
[1968.86 --> 1970.74]  I was going to say you were in an emo band.
[1970.82 --> 1972.78]  And now that you say you did Warped Tour, dude, I was just like.
[1972.78 --> 1974.14]  I was 100% emo band.
[1974.14 --> 1974.24]  Bro.
[1974.46 --> 1975.38]  I was out there, dude.
[1975.40 --> 1976.44]  I had like snake bites.
[1976.44 --> 1977.10]  I just can imagine Trash doing this.
[1977.10 --> 1977.58]  I had like.
[1977.70 --> 1979.20]  I had my face was all pierced up.
[1979.26 --> 1980.66]  I had like the long hair like that.
[1981.14 --> 1983.16]  Dude, the stand up band is happening now.
[1983.16 --> 1984.00]  Trash, are you trolling me?
[1984.00 --> 1984.66]  It's happening.
[1985.38 --> 1985.72]  Hmm.
[1986.22 --> 1986.46]  Yeah.
[1986.46 --> 1987.48]  Oh, my trash.
[1987.58 --> 1987.72]  Okay.
[1987.78 --> 1989.54]  You have to send us some stuff offline.
[1989.68 --> 1989.94]  I promise.
[1990.12 --> 1990.98]  That's my previous life.
[1991.08 --> 1991.22]  Yeah.
[1991.36 --> 1991.78]  We won't.
[1991.86 --> 1992.58]  I want to see this.
[1992.58 --> 1993.16]  I have to see this.
[1993.16 --> 1993.88]  Because I just want to hear it.
[1994.18 --> 1994.70]  No, Trash.
[1994.74 --> 1995.90]  It is not your previous life.
[1995.94 --> 1996.84]  It's your current life.
[1996.86 --> 1998.40]  Because we are starting this band.
[1998.56 --> 1999.84]  We are going to play us online.
[1999.84 --> 2000.76]  It's going to be great.
[2001.06 --> 2001.70]  No way.
[2002.42 --> 2004.68]  I don't know why I even broadcasted that information.
[2004.70 --> 2006.74]  That's crazy that you told us and didn't last.
[2006.74 --> 2009.84]  I'm like real time regretting everything right now.
[2009.84 --> 2011.38]  I almost want to hang up.
[2011.52 --> 2012.44]  I want to hang up.
[2012.62 --> 2013.12]  I hate it.
[2013.54 --> 2013.96]  I'll be honest.
[2014.04 --> 2014.78]  Which one was worse?
[2014.78 --> 2018.70]  Was that realization that you just said that out loud or when you found out you were an
[2018.70 --> 2020.50]  Apple shill live on the podcast?
[2021.44 --> 2024.02]  I find out a lot of things about myself on this podcast.
[2024.70 --> 2026.72]  It's a soul searching experience.
[2029.14 --> 2029.54]  Yeah.
[2029.68 --> 2030.88]  I'm pretty sad about that.
[2030.90 --> 2033.00]  I'm glad that we have a future that is not very great.
[2033.20 --> 2034.86]  And I learned that Trash is a musician today.
[2034.90 --> 2035.66]  I'm very excited about this.
[2035.70 --> 2036.36]  We should do a band.
[2036.36 --> 2036.80]  A bad one.
[2037.46 --> 2040.98]  I actually kind of liked what Tiege just said.
[2040.98 --> 2043.56]  I feel like that's a pretty optimistic way of looking at it.
[2043.68 --> 2049.84]  And very, very like fitting with Tiege's personality, which was just like, look, maybe we're going
[2049.84 --> 2052.32]  to end up with a lot of things being like chess, but who cares?
[2052.32 --> 2053.92]  Because like humans can just do it.
[2053.98 --> 2054.88]  We're going to do it anyway.
[2055.74 --> 2056.40]  We are going to.
[2056.40 --> 2059.08]  Unless the machines get wormable exploits and kill us all.
[2059.14 --> 2059.92]  Yeah, that one.
[2060.26 --> 2060.58]  True.
[2060.70 --> 2061.96]  That one is the worry.
[2062.32 --> 2063.30]  That one's not.
[2063.42 --> 2063.96]  It's so good.
[2063.96 --> 2067.82]  I don't know if you guys ever feel this way.
[2068.12 --> 2071.22]  Like I sometimes feel like I have a German shepherd at home.
[2071.30 --> 2072.30]  She's like 60 pounds.
[2072.38 --> 2076.82]  She's not huge, but I'm like, she like plays next to my little kids.
[2076.82 --> 2078.98]  And I think like, holy cow, like that's kind of crazy.
[2078.98 --> 2084.14]  It's crazy that we like spent a lot of time fixing all the bugs in the dog coating.
[2084.14 --> 2085.94]  So now doggy, very nice.
[2085.94 --> 2091.26]  Like, you know, and my kids can jump on this dog and like pull her ears and everything.
[2091.26 --> 2094.54]  And she licks them instead of biting their face off.
[2094.62 --> 2095.68]  And you're like, that's really cool.
[2095.76 --> 2099.86]  I'm glad that I have German shepherd V 65,000.
[2102.26 --> 2102.66]  Yes.
[2103.54 --> 2109.44]  But it's like, are people I this makes like this article and just like thinking about it
[2109.44 --> 2114.50]  literally makes me think like, maybe I don't want robot version one, two, three, four, five,
[2114.54 --> 2116.64]  six, seven, eight, nine, 10, like in my house.
[2116.78 --> 2117.32]  You know what I'm saying?
[2117.32 --> 2118.88]  Like my kids.
[2119.30 --> 2121.02]  That's like freaky stuff, dude.
[2121.02 --> 2121.84]  It is kind of scary.
[2122.48 --> 2122.84]  Yes.
[2123.34 --> 2127.54]  Even if it doesn't get exploited, it's just like somebody wrote some bad code and it like
[2127.54 --> 2129.62]  steps down when it should have stepped over.
[2129.74 --> 2133.22]  And it's like humans are soft and squishy and robots are big and heavy.
[2133.60 --> 2134.04]  Right.
[2134.16 --> 2137.82]  There's like a, there's like, you know, you're, you're watching the change log every week
[2137.82 --> 2139.82]  and you see these like really disturbing things.
[2139.82 --> 2141.42]  It's like, Oh yeah.
[2141.48 --> 2147.76]  Patch resolved the problem where the robot would be standing over your bed, holding a knife at night.
[2147.76 --> 2151.14]  Uh, it was just misrecognizing that as tomatoes.
[2151.14 --> 2157.40]  Uh, and, uh, there were, you know, so, uh, sorry for everyone who got spooked out by that,
[2157.40 --> 2158.08]  but don't worry.
[2158.08 --> 2161.26]  We've like, uh, we fought, fixed that one should be rolling out.
[2161.26 --> 2162.78]  Uh, anything out yet.
[2162.78 --> 2169.28]  Uh, one thing we would suggest for the next two nights before it, uh, updates everywhere is just keep your bedroom doors close,
[2169.28 --> 2173.30]  preferably locked if they have the kind of handle, uh, that you can push down on.
[2173.46 --> 2174.74]  And we'll just leave it at that.
[2174.80 --> 2174.90]  Yeah.
[2174.90 --> 2175.82]  Just don't dress in red.
[2175.96 --> 2176.62]  You won't be mistaken.
[2176.82 --> 2177.58]  Yeah, exactly.
[2178.34 --> 2183.96]  If you have any small round red children, we would suggest keeping them out of the house.
[2184.56 --> 2184.96]  Yeah.
[2185.16 --> 2186.86]  That is so, that's such a good skit.
[2186.94 --> 2187.78]  Someone has to make that.
[2187.78 --> 2194.18]  I also think what's hilarious for this, like unitary one is it's like the patch notes still haven't dropped.
[2194.18 --> 2202.90]  The LinkedIn thing that they posted was like, Hey, we, we, we are about to roll out a patch that fixes most of these issues.
[2202.90 --> 2208.46]  If I recall, that was like the exact wording from the LinkedIn post, which is insane.
[2208.46 --> 2213.28]  Cause it's like, what do you mean one about to roll out?
[2213.46 --> 2213.90]  Right.
[2214.58 --> 2216.08]  We haven't rolled out the fix for this.
[2216.16 --> 2217.92]  And number two, what do you mean?
[2217.98 --> 2219.14]  Most of the issues.
[2219.40 --> 2219.68]  Yeah.
[2220.68 --> 2221.12]  Yeah.
[2221.64 --> 2222.94]  Like, like actual questions.
[2222.94 --> 2224.56]  Like for like these robots.
[2225.16 --> 2225.60]  Okay.
[2225.72 --> 2225.92]  Good.
[2226.10 --> 2226.32]  Sorry.
[2226.44 --> 2226.76]  Sorry.
[2226.86 --> 2227.58]  Just for TJ.
[2227.96 --> 2229.14]  Uh, exactly from LinkedIn.
[2229.30 --> 2233.34]  We immediately began addressing these concerns and have now completed the majority of the fixes.
[2235.08 --> 2235.52]  Majority.
[2235.84 --> 2236.24]  Yeah.
[2236.30 --> 2238.20]  That means over 50%, by the way.
[2238.20 --> 2239.32]  That's what majority means.
[2239.44 --> 2239.90]  Just so we're in it.
[2240.08 --> 2241.98]  Like 51% of the fixes.
[2242.16 --> 2242.84]  We've got those.
[2243.02 --> 2246.74]  They can only be hacked within 10 feet of each other now.
[2247.02 --> 2253.56]  Like, is there actual like, uh, consumers of this outside of like researchers just trying to break it and stuff?
[2253.72 --> 2255.76]  Like, I feel like I just don't know anybody.
[2256.10 --> 2257.06]  It's made to order.
[2257.26 --> 2259.02]  Like I can just go on there and order one right now.
[2259.20 --> 2260.06]  How much is a robot?
[2260.32 --> 2260.64]  $67,900.
[2262.16 --> 2262.80]  How much?
[2263.08 --> 2263.68]  Oh my God.
[2263.68 --> 2266.54]  $67,900 for a G1 robot.
[2266.54 --> 2268.42]  So there's like dozens of people.
[2268.42 --> 2275.04]  The scarier one though, Trash, was that a police department bought one of these for like the dog thing to test it out.
[2275.16 --> 2276.14]  Like they have a dog version.
[2276.14 --> 2276.54]  Oh, the dog.
[2276.60 --> 2277.46]  I've seen the dog ones.
[2277.46 --> 2278.16]  Yeah, yeah, yeah.
[2278.16 --> 2280.46]  Bro, the government's going to get these.
[2280.64 --> 2282.24]  And then what's going to happen then?
[2282.28 --> 2290.34]  It can like leak everything inside of the, like it can go inside of the police department and then, or it can go wherever the government owns it.
[2290.36 --> 2293.28]  And it's like, oh, we just accidentally hacked the entire police department.
[2293.28 --> 2296.98]  Or like we sent all of the audio visual data to our servers.
[2297.14 --> 2300.06]  Because like they have cameras and microphones and they can do.
[2300.76 --> 2304.34]  They're going to find Trash's arrest record for when he trashed the hotel room.
[2304.44 --> 2309.04]  That's where he got the name Trash probably when he was on tour with his band that we're not supposed to know about.
[2309.04 --> 2310.28]  The Leaky Faucets.
[2310.94 --> 2311.16]  Yeah.
[2311.70 --> 2312.76]  The Leaky Faucets.
[2313.32 --> 2314.26]  The Wet Bandits.
[2314.26 --> 2314.54]  Sick name, bro.
[2315.50 --> 2316.50]  That could be our band name.
[2316.86 --> 2317.18]  Uh-huh.
[2317.48 --> 2317.84]  Yeah.
[2317.84 --> 2321.98]  Can we put the Grammy award winning as part of the band title?
[2322.38 --> 2325.16]  Like the Grammy award winning stand up band.
[2325.52 --> 2327.60]  My grandma loved when I was in a band.
[2327.80 --> 2329.68]  So that's a Grammy award winning band.
[2329.72 --> 2330.96]  You don't have to use the term Grammy.
[2331.48 --> 2334.08]  We can just say award winning band.
[2334.20 --> 2336.04]  Because TJ, you just won an award.
[2336.12 --> 2336.86]  You have a trophy.
[2337.00 --> 2337.88]  I have a trophy.
[2338.34 --> 2338.96]  Award for what?
[2339.90 --> 2341.34]  I got a Netflix trophy.
[2341.34 --> 2341.72]  Love it.
[2342.12 --> 2342.60]  Love it.
[2342.92 --> 2344.32]  I want a hack day, loser.
[2344.34 --> 2344.96]  I got one right here.
[2346.34 --> 2346.90]  Love it.
[2347.84 --> 2348.92]  Right here.
[2350.70 --> 2352.26]  Award winning open source developer.
[2352.28 --> 2353.16]  Look at that.
[2354.02 --> 2354.84]  Look at that.
[2355.08 --> 2355.40]  Trash.
[2355.68 --> 2357.14]  Don't tell me that ain't award winning.
[2357.52 --> 2357.92]  Dang.
[2358.22 --> 2359.04]  Dang, Trash.
[2359.24 --> 2360.02]  Go break my tooth.
[2360.16 --> 2360.32]  I don't want to do that.
[2360.32 --> 2362.30]  What age group were you playing in?
[2363.68 --> 2365.72]  This is for breaking legs, buddy.
[2365.94 --> 2366.18]  Okay?
[2367.40 --> 2368.40]  Breaking legs award.
[2369.20 --> 2369.64]  Nice.
[2370.46 --> 2372.24]  14 plus breaking legs award.
[2374.26 --> 2374.80]  That's it.
[2374.90 --> 2376.34]  I'm scared of the robots.
[2376.56 --> 2377.34]  I would be worried.
[2377.84 --> 2379.42]  But I do kind of want to order one.
[2379.42 --> 2380.82]  I mean, what else is there to say?
[2381.02 --> 2381.68]  There's not a lot.
[2381.68 --> 2382.08]  We said it all.
[2382.28 --> 2382.92]  We said it all.
[2383.14 --> 2385.10]  Hopefully I'm dead before this apocalypse happens.
[2385.56 --> 2386.66]  I'm glad I'm old.
[2387.12 --> 2387.70]  I'm actually glad I'm old.
[2387.70 --> 2389.28]  Trash at the rate you're eating Doritos, bro.
[2390.90 --> 2391.54]  Hey, man.
[2391.58 --> 2392.60]  I'm working out, all right?
[2392.84 --> 2393.14]  Okay.
[2394.14 --> 2397.02]  Trash at the rate you're eating some pirate booties.
[2397.02 --> 2399.46]  I switched to pirate booties today.
[2400.24 --> 2400.32]  So.
[2401.08 --> 2401.66]  Just today?
[2402.00 --> 2403.12]  Health conscious reasons?
[2403.52 --> 2403.72]  Yeah.
[2403.78 --> 2406.64]  Well, I went to Disneyland with my kids.
[2406.72 --> 2408.00]  So I bought like a huge box of these.
[2408.34 --> 2409.54]  And then now they're in my office.
[2409.64 --> 2410.64]  So I'm just going to town.
[2410.72 --> 2411.64]  I can't stop myself.
[2412.20 --> 2413.40]  I can't stop myself.
[2413.50 --> 2413.98]  Sorry, kids.
[2414.02 --> 2414.76]  I'm eating your snacks.
[2415.54 --> 2416.72]  Where did Prime go?
[2416.90 --> 2418.24]  I just had to walk away for a second.
[2418.38 --> 2419.90]  I just can't even believe what I'm seeing right now.
[2420.00 --> 2420.54]  You literally.
[2420.74 --> 2422.40]  That was like you couldn't take it.
[2422.48 --> 2424.06]  You couldn't take the pirate bootie box.
[2424.22 --> 2429.24]  I just can't take the fact that he has a full ass pirate bootie box next to his desk.
[2429.40 --> 2432.82]  And then he also pulled up like multiple wrappers that are empty.
[2433.56 --> 2436.64]  And he argued with TJ about making health conscious decisions.
[2436.64 --> 2437.94]  Eat some protein is what he wants you to do.
[2438.04 --> 2438.42]  I'm hungry.
[2438.50 --> 2439.00]  I ate a bagel.
[2439.06 --> 2440.06]  It had lots of protein in it.
[2440.20 --> 2440.34]  Okay.
[2440.54 --> 2440.74]  Okay.
[2441.06 --> 2442.60]  Bagels are not a good source of protein.
[2442.60 --> 2443.14]  Did you have this?
[2443.24 --> 2443.70]  I'm going to.
[2443.76 --> 2444.40]  I'm going to.
[2444.40 --> 2446.16]  I'll eat like a steak or something later.
[2446.42 --> 2446.56]  Okay.
[2446.62 --> 2446.94]  All right.
[2446.98 --> 2447.28]  Okay.
[2447.36 --> 2447.68]  Okay.
[2447.74 --> 2449.00]  I'm going to work out today too.
[2449.06 --> 2449.80]  I'm going to work out again.
[2450.02 --> 2450.50]  Get this man some eggs.
[2450.92 --> 2451.38]  Yeah, I know.
[2452.08 --> 2452.72]  I'm going to work out again.
[2452.72 --> 2453.58]  Trash, I believe in you.
[2453.58 --> 2453.74]  I have to work out.
[2454.24 --> 2455.10]  I believe in you, Trash.
[2457.14 --> 2457.98]  I'm in shape, okay?
[2458.20 --> 2461.12]  Can I say something that doesn't hurt your feelings?
[2461.48 --> 2461.78]  Hopefully.
[2461.84 --> 2462.60]  It can't hurt my feelings.
[2463.28 --> 2465.44]  Trash, I really like it when you have glasses on.
[2466.44 --> 2467.54]  I have my contacts on.
[2467.54 --> 2468.42]  I know you had them on.
[2468.42 --> 2470.30]  You had them on your head for the first half of this podcast.
[2470.84 --> 2472.24]  I have my contacts in right now.
[2472.30 --> 2472.60]  I know.
[2472.68 --> 2473.80]  When you wear glasses, you just.
[2473.80 --> 2475.06]  You just look like trash.
[2475.12 --> 2477.26]  Now that you don't have your glasses in, it's like, I don't even know who you are.
[2477.36 --> 2478.08]  See, like, that's trash.
[2478.08 --> 2478.10]  I can't.
[2478.10 --> 2478.54]  I can't pull.
[2478.66 --> 2479.62]  I got contacts on.
[2479.68 --> 2480.20]  It hurts.
[2481.06 --> 2481.98]  Double vision.
[2482.22 --> 2482.90]  Is that how it works?
[2483.04 --> 2484.04]  You see two things now?
[2485.08 --> 2485.44]  I don't know.
[2485.44 --> 2486.20]  I just can't see nothing.
[2486.34 --> 2486.90]  You want me to see?
[2487.06 --> 2488.22]  Do you want me to rip out my contacts?
[2488.22 --> 2490.18]  I'll rip my contacts out right now and put them on.
[2490.26 --> 2490.88]  No, don't do it.
[2490.90 --> 2492.54]  Don't get the jelly in your eyeballs, Trash.
[2492.54 --> 2493.54]  Trash.
[2494.00 --> 2494.36]  Yeah.
[2494.40 --> 2499.60]  Those of you who are just joining us missed the part before the stream where I asked why
[2499.60 --> 2501.04]  Trash wasn't wearing glasses.
[2501.16 --> 2505.66]  And he was like, I don't want to get jelly in my eyeballs was the explanation.
[2505.80 --> 2506.58]  I was like, what?
[2506.66 --> 2509.38]  And he's like, well, I'm eating this bagel with jelly on it.
[2509.38 --> 2515.72]  And I'm like, so I guess he couldn't, you couldn't eat it without it coming up into your face like this?
[2515.72 --> 2516.54]  You don't understand.
[2516.84 --> 2520.18]  When you eat the bagel, you get jelly slime on your fingies.
[2520.40 --> 2522.62]  And it's not going to come off, but just the napkin.
[2522.66 --> 2523.46]  So you got to wash your hands.
[2523.82 --> 2526.32]  So now I got jelly slime in my eyeballs now.
[2526.44 --> 2527.22]  Thank you very much.
[2528.20 --> 2528.56]  True.
[2528.76 --> 2529.28]  Wait, hold on.
[2529.28 --> 2529.76]  Time out.
[2529.90 --> 2531.18]  How did you get in your eyeballs, though?
[2531.28 --> 2531.68]  Like, explain.
[2532.02 --> 2532.36]  I don't know.
[2532.62 --> 2532.70]  I don't know.
[2532.70 --> 2535.86]  You said all the steps and none of it involved putting your hands in your eyes.
[2535.96 --> 2537.36]  You're like, get some glasses.
[2537.48 --> 2539.06]  Would the glasses prevent that?
[2539.06 --> 2539.52]  Well, no.
[2539.58 --> 2540.56]  The glasses would prevent that.
[2540.82 --> 2542.02]  So I took the contact off.
[2542.10 --> 2546.70]  To get the contact on my eye, I got to squeeze my eyeball with two fingers and pull it off.
[2547.20 --> 2548.94]  And if there's jelly on these little thingies.
[2549.96 --> 2550.82]  That makes sense.
[2551.20 --> 2551.42]  Try it.
[2551.42 --> 2552.12]  It's going to get on my eye.
[2552.54 --> 2553.98]  It's a simple concept.
[2554.18 --> 2556.58]  50 times 105.
[2557.00 --> 2557.24]  Okay?
[2559.38 --> 2560.42]  You moron.
[2565.44 --> 2566.10]  1250, right?
[2566.16 --> 2566.64]  Is that the answer?
[2566.84 --> 2567.14]  50 times.
[2567.14 --> 2567.24]  No.
[2567.24 --> 2568.10]  Oh, dude.
[2568.18 --> 2569.32]  Just 100 times 50.
[2569.42 --> 2570.14]  You can do that.
[2570.24 --> 2571.32]  You at least know the magic category.
[2571.32 --> 2572.34]  I don't want to do it.
[2572.62 --> 2573.46]  I'm spoiled by AI.
[2573.46 --> 2577.28]  Are you still getting jelly all over your contact lenses and up in your eyeballs because
[2577.28 --> 2580.28]  you don't have an AI to remove your contact lenses for you?
[2580.44 --> 2581.58]  Well, I do.
[2581.76 --> 2587.02]  And I can see without having a giant purple haze over my eyes because I got jelly all up
[2587.02 --> 2587.40]  in there.
[2587.54 --> 2589.66]  And that's why I'm making bank.
[2589.66 --> 2592.96]  Every day you spend seven seconds taking out your glasses.
[2596.56 --> 2597.50]  It's a real problem.
[2597.70 --> 2598.66]  It's a real problem.
[2598.80 --> 2599.34]  You guys don't get it.
[2599.34 --> 2602.36]  You can wait 35 minutes for your AI robot to do this for you.
[2602.56 --> 2604.32]  But you don't have to lift a hand.
[2604.66 --> 2604.88]  Yeah.
[2605.42 --> 2605.84]  Come on.
[2605.84 --> 2607.04]  No more jelly for you.
[2607.14 --> 2608.92]  The robot's all jellied up now.
[2609.14 --> 2609.50]  Oh, man.
[2609.52 --> 2610.30]  It's a real problem.
[2610.56 --> 2611.36]  You guys don't get it.
[2611.36 --> 2611.64]  Jelly robot.
[2612.82 --> 2614.10]  Wait till you get jelly in your eyes.
[2614.14 --> 2614.66]  See how you feel.
[2615.88 --> 2616.66]  I trash.
[2616.66 --> 2617.40]  It makes sense to me.
[2617.46 --> 2618.32]  I'm with you on this one.
[2618.60 --> 2618.98]  I'm with you.
[2619.22 --> 2619.76]  I am right.
[2620.20 --> 2623.92]  Well, thank you, everybody, for joining us on this amazing stand-up today.
[2624.08 --> 2626.72]  We have with us, as always, TeejDV.
[2626.86 --> 2627.90]  I just want to code.
[2628.04 --> 2630.52]  We have TrashDev, Jelly in the eyeballs.
[2630.74 --> 2633.36]  And, of course, Casey, the actual engineer, Miratori.
[2634.10 --> 2636.24]  Casey, we can find you at ComputerEnhanced.com.
[2636.26 --> 2639.40]  If you actually want to learn how computers work, you should probably check that out and
[2639.40 --> 2642.86]  stop being such an idiot instead, being an amazing engineer.
[2642.98 --> 2643.18]  True.
[2643.66 --> 2644.02]  Trash.
[2644.14 --> 2646.24]  I don't know what Trash has to offer other than...
[2646.24 --> 2649.26]  Do you want to shout out a sponsor or something?
[2649.36 --> 2649.68]  What do you do?
[2649.70 --> 2651.08]  I'm just here for the lulz, everybody.
[2651.42 --> 2655.50]  Check out his x.com, Trash underscore Dev with two H's.
[2655.66 --> 2658.42]  That's the best place to find six-month-old Reddit memes.
[2658.78 --> 2659.90]  I need to change my name.
[2659.96 --> 2660.54]  That's what I need to do.
[2661.40 --> 2661.64]  True.
[2661.80 --> 2663.00]  What are you going to change your name to?
[2663.38 --> 2664.54]  Trash with three H's.
[2665.06 --> 2665.52]  Oh, yeah.
[2666.22 --> 2666.76]  Triple H.
[2666.84 --> 2667.32]  You know what I'm saying?
[2667.40 --> 2668.46]  Triple H, Trash.
[2668.48 --> 2669.54]  It works for Vin Diesel.
[2669.98 --> 2670.48]  You know what I'm saying?
[2670.48 --> 2676.98]  Of course, Teej D.V., the magnificent coder among us, who also dresses in Miami nice.
[2677.40 --> 2677.72]  I do.
[2677.80 --> 2679.60]  I try to represent for the pod.
[2679.68 --> 2680.00]  Stylish.
[2680.32 --> 2680.92]  It is pretty nice.
[2681.40 --> 2681.94]  Thank you.
[2682.32 --> 2682.56]  Thanks.
[2682.56 --> 2684.44]  And so today, that was the stand-up.
[2684.70 --> 2685.14]  The name.
[2686.30 --> 2687.30]  I don't have anything.
[2687.60 --> 2689.16]  I don't have like a run-on sense I can do.
[2689.32 --> 2689.72]  A gen.
[2689.72 --> 2691.52]  Boot up the day.
[2693.18 --> 2696.34]  Vibe code and errors on my screen.
[2697.70 --> 2699.34]  Terminal coffee.
[2700.18 --> 2701.12]  And here.
[2702.12 --> 2704.16]  Living the dream.
