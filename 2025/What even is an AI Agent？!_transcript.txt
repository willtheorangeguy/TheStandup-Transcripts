[0.00 --> 2.72]  Guys, have you guys checked out the hottest new site, Balls.yoga?
[4.22 --> 4.66]  What?
[4.88 --> 6.10]  Yeah, I have checked it out.
[6.28 --> 7.62]  Adam, check it out.
[7.80 --> 8.34]  Balls.yoga?
[8.98 --> 9.72]  Check it out.
[10.18 --> 11.54]  Oh my god, what is this?
[13.86 --> 16.04]  It's so hot right now. So hot.
[17.00 --> 18.08]  This is you guys?
[20.84 --> 23.30]  What in the world?
[23.56 --> 29.34]  I just sent in the chat, we made an ad for Bolt for their hackathon this month that we were doing.
[29.34 --> 34.48]  And it involved Prime being devastated that he was no longer able to make Balls.yoga,
[34.64 --> 40.76]  which we just casually mentioned in the ad, but then we actually made it so that it would be an Easter egg.
[40.90 --> 43.22]  Can you believe Balls.yoga was available to buy, though?
[44.00 --> 44.80]  Adam, are you okay?
[45.40 --> 46.84]  He's watching the ad.
[47.18 --> 47.44]  Yeah.
[48.70 --> 50.94]  Your face looks so disappointed.
[51.36 --> 52.80]  Oh, did it? I was just reading Twitter.
[52.94 --> 57.08]  I'm sorry, you guys sent me to Twitter and then I found that there's some stuff on Twitter.
[57.08 --> 59.28]  Ooh, the drama.
[61.20 --> 61.60]  Drama.
[62.26 --> 63.86]  I just want to read it so badly now.
[64.30 --> 65.48]  Let's just read it on stream.
[65.84 --> 67.80]  I don't know if it belongs on your podcast.
[68.06 --> 69.70]  I don't think that's necessarily where it goes.
[69.82 --> 70.84]  Bring it up.
[71.04 --> 73.16]  Can we give a proper intro to the episode before we start?
[73.26 --> 74.42]  Yeah, yeah, yeah, yeah, yeah, yeah.
[74.88 --> 78.96]  Yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah.
[78.96 --> 79.74]  Anyway, sorry.
[79.96 --> 80.40]  Go ahead, Prime.
[80.40 --> 85.48]  Hey, today we are having on what I would consider two experts, Adam and Dax.
[85.76 --> 88.46]  Adam is currently looking over, looking very disturbed.
[88.92 --> 89.70]  I'm so sorry.
[90.32 --> 91.44]  Josh, zoom in.
[91.92 --> 93.02]  Zoom in, Josh.
[93.02 --> 93.46]  Zoom in.
[94.12 --> 100.32]  But they have been building out something called OpenCode, which is going to be an agent for your terminal.
[100.52 --> 102.74]  And the experience looks immaculate.
[102.88 --> 104.46]  Adam, you've done a fantastic job.
[104.58 --> 105.70]  Dax, I don't know what you do.
[105.70 --> 108.62]  But it looks very, very, very good.
[108.94 --> 112.22]  And, of course, on this podcast, as always, is Teej.
[112.74 --> 113.14]  Teej.
[113.48 --> 116.40]  Hey, he might be Steve Jobs, Telescopic Johnson.
[116.52 --> 117.88]  I don't know what your full name is these days.
[117.94 --> 118.94]  You keep getting new ones.
[119.48 --> 122.72]  And so, yeah, today on The Stand-Up, we're going to be talking about how to build an agent.
[122.84 --> 129.08]  But not only that, some things about OpenCode itself, which hopefully you'll see a bunch of this on the stream coming up.
[129.08 --> 132.98]  Because this is really our kind of like our area that we all seem to enjoy.
[132.98 --> 137.16]  For whatever reason, all four people on this podcast use NeoVim, by the way.
[137.38 --> 138.02]  And so you can imagine.
[138.02 --> 139.30]  That's how we started our company.
[139.42 --> 141.22]  That's actually why we started our company.
[141.44 --> 143.96]  It's the first time someone got hired because of NeoVim.
[144.18 --> 146.32]  And he got two, a double, two for one.
[146.98 --> 154.24]  But the reality is that this type of agent is built for people who want, I assume, the more command line kind of experience.
[154.24 --> 158.16]  The ability to have the faster, more creamy experience that way.
[158.56 --> 161.10]  And so they're going to just kind of walk us through what it takes to actually build an agent.
[161.10 --> 164.46]  Because if you're not familiar, you probably read 1,000 AI articles at this point.
[164.50 --> 165.94]  That's like, yeah, I spent an afternoon.
[166.08 --> 166.70]  I built an agent.
[166.82 --> 167.16]  It's easy.
[167.24 --> 168.42]  You don't even need something like Cursor.
[168.48 --> 169.06]  It's so simple.
[169.38 --> 169.54]  Right?
[169.58 --> 171.44]  Like you read this thing over and over again.
[171.48 --> 173.10]  You're just like, well, then what are people working on?
[173.14 --> 174.26]  It has to be harder.
[174.26 --> 174.58]  Right?
[174.94 --> 179.46]  And so we would love to have someone on who's actually done it and can walk us through what it actually takes.
[179.46 --> 181.54]  Hackathon's over.
[181.94 --> 183.54]  But that doesn't mean the content is.
[183.96 --> 190.74]  Join us on July 26th at 10 a.m. PST on Prime Stream to live react to the award ceremony.
[191.14 --> 192.98]  See what everybody built and we'll see you there.
[194.62 --> 195.22]  It's okay.
[195.32 --> 196.26]  You've worked at Netflix.
[196.44 --> 197.96]  You have everything they want.
[198.36 --> 200.62]  Anyway, so that's been a little frustrating.
[200.62 --> 205.18]  But on the other hand, we're really excited about the direction things are going in.
[205.36 --> 211.30]  I think we've been, I think the genesis of this is like, there's been a lot of really cool tools out there.
[211.38 --> 216.52]  Like Cursor, a lot of people like, a lot of people use a bunch, but I don't want to give up NeoVim.
[216.64 --> 217.70]  Like I like working in the terminal.
[217.80 --> 218.84]  I don't want to switch my whole IDE.
[220.02 --> 224.64]  So we're excited about seeing, okay, what can we do for people like us?
[224.64 --> 230.96]  Like what's the best possible thing we can put together that's complimentary to whatever ID that you choose to use.
[233.48 --> 233.88]  Nice.
[234.02 --> 234.52]  Very exciting.
[234.52 --> 239.18]  Well, that's some good background info because we're going to be mentioning open code a bunch probably while we're talking about this.
[239.24 --> 245.08]  So that clears up where people should go when you guys are talking about that, at least.
[245.38 --> 247.94]  So let's get to, what is an agent, Dax?
[248.12 --> 248.98]  Everyone's been asking.
[250.30 --> 251.54]  I gotta be honest, I don't really know.
[253.10 --> 254.06]  Adam, do you want to take this?
[254.06 --> 256.82]  What's your concept of an agent?
[257.12 --> 259.76]  Well, I think the term is very overloaded, right?
[259.92 --> 262.96]  So outside of programming, it means a lot of things probably.
[263.50 --> 263.86]  Probably.
[264.22 --> 264.62]  Programming.
[265.12 --> 265.26]  Yeah.
[265.64 --> 266.22]  James Bond.
[266.88 --> 269.28]  I meant within the AI bubble.
[271.02 --> 279.66]  So I guess there's like, in the programming world, it's just this idea of calling an LLM, giving it a bunch of tools that are related to programming.
[279.66 --> 283.16]  So editing, reading files in your code base.
[283.80 --> 292.62]  And then just like looping and letting it keep calling these tools, making changes, and then coming back with some kind of response.
[292.62 --> 296.28]  That's kind of the basics, like the formula for an agent.
[296.28 --> 299.46]  If you look at, like, cursor has an agentic mode.
[300.12 --> 302.70]  But then there's other tools in the terminal, like cloud code.
[303.14 --> 307.26]  I think all the tools that fit into this category kind of have that backbone.
[307.26 --> 314.14]  And in particular, the looping is really what we like.
[314.78 --> 316.28]  The looping and the tools, right?
[316.38 --> 319.38]  I think, like, we can say agent equals LLM plus tools.
[319.50 --> 319.98]  Is that fine?
[320.06 --> 320.74]  Plus loops?
[320.74 --> 333.58]  Plus some sort of system prompt that keeps it into, like, there's some, I assume there's some sort of secret sauce to getting a good prompt that helps the agent understand that it needs to go through a bunch of files and kind of understand the code base.
[333.64 --> 334.92]  Is that what it is also?
[336.18 --> 337.58]  Or understand the task at hand?
[338.24 --> 338.38]  Yeah.
[338.44 --> 343.06]  And each of the models kind of like, there's, they respond differently to the system prompt.
[343.06 --> 347.68]  So there is, like, a bit of that, but it's not, like, a super sensitive secret.
[348.14 --> 351.60]  I mean, there's, you can kind of see all the system prompts out there.
[352.26 --> 358.14]  I don't really know that any tool can, like, differentiate that hard on those fronts.
[358.26 --> 362.34]  Like, the tools are pretty, like, set to the model at this point.
[362.70 --> 365.58]  Claude expects certain tools, at least today.
[365.68 --> 369.76]  Maybe someday all the models will be better at calling tools generically.
[369.76 --> 376.80]  But right now, like, it's really kind of like all these agents have the same set of tools, the same, roughly, system prompts.
[378.06 --> 385.26]  It's all the stuff around it that I think we're focused on, like, open code, having kind of, like, the share page.
[385.36 --> 388.84]  You can share sessions with people, and you can kind of see the full history of a session.
[390.34 --> 392.26]  And just having a really great TUI experience.
[392.46 --> 399.62]  We're going to build a mobile client, so you can kind of, like, step away from your machine and continue, you know, conversations while you're on the toilet or whatever.
[399.76 --> 409.10]  Yeah, I think, like, there's a lot of stuff around the actual agent that makes for a good experience in terms of programming with these things.
[409.50 --> 413.22]  And I think Dax and I have both done a lot of programming with these things, so we have a lot of opinions.
[414.18 --> 418.48]  Yeah, I think we're definitely, like, really firmly in the product zone.
[418.48 --> 426.16]  It's, like, less about pushing the LLM capabilities or, like, finding clever ways to use the LLM itself or making it perform better.
[426.30 --> 431.46]  There's some of that, but most of it is just packaging it in a way that's nice to use.
[431.46 --> 438.54]  And that's obviously very fun because when you're working on a product that you yourself use every day, you're just like, oh, I wish this was like this.
[438.60 --> 439.24]  I wish this was this.
[439.30 --> 439.96]  I wish this was easier.
[440.54 --> 442.58]  So, yeah, it's nice to be able to iterate on that.
[442.58 --> 458.84]  And then some of the mobile stuff, so I think one differentiator with us is we're really in on this idea of the agent running on your machine with access to your stuff because that's where you, presumably, your dev environment works the best.
[459.16 --> 460.42]  Presumably, you have everything set up.
[460.42 --> 474.24]  Some of these tools, like Codex or, like, DevIn, they work remotely and they run in the cloud, which can work, but then you need to, like, recreate your perfect environment in the cloud, which some companies are disciplined and have that, but not everyone does.
[474.26 --> 474.78]  Nix fixes this, right?
[474.88 --> 477.52]  Yes, Nix does fix it, but, you know, how many people use Nix?
[478.40 --> 478.76]  Seven.
[478.78 --> 481.20]  So until everyone's using Nix, several, yes.
[483.22 --> 486.44]  Realistically, practically, most people's workable dev environment is local.
[486.44 --> 488.74]  So we want to do stuff like, oh, we want to have a mobile app.
[488.74 --> 491.70]  That's just going to be connecting to a session.
[491.82 --> 494.82]  That's you leave your laptop running and you step away, go on a walk.
[494.88 --> 500.80]  You can, like, get notifications saying how the agent's done with this, give it feedback, but it's also just running on your laptop.
[500.80 --> 503.44]  So you don't have to go set up this crazy cloud thing.
[503.70 --> 513.38]  Have you successfully been able to actually, you know, do a day of prompting while out at the grocery store doing your own thing, just hitting some prompts from your mobile phone?
[514.50 --> 516.08]  No, we haven't built the mobile client yet.
[516.08 --> 518.82]  But it's something I desperately want.
[518.92 --> 520.68]  I don't care if anybody else uses it, to be honest.
[521.18 --> 523.28]  There's just so many times at this season of life.
[523.32 --> 524.10]  I'm 38 years old.
[524.14 --> 524.80]  I have two kids.
[525.16 --> 526.78]  I'm out of my office a lot.
[526.86 --> 529.22]  Like, I step out 15 times a day.
[529.22 --> 536.72]  And to be able to, like, go on a walk and then when it's done, get a notification, you know, it's doing its loop and it needs input.
[536.72 --> 541.66]  To be able to, like, continue that conversation without having to be sitting at my desk, it's just I want it very badly.
[541.90 --> 544.16]  And I think it turns out other people want it.
[544.66 --> 545.96]  We've seen some mentions on Twitter.
[546.28 --> 547.70]  Cursor's even designing a mobile app.
[547.70 --> 552.34]  So, yeah, it doesn't exist yet, but I'm very excited to have it.
[553.76 --> 554.16]  Okay.
[554.16 --> 568.40]  So then kind of walk us through what it takes to actually build an agent in some sort of real capacity, not just a weekend warrior project, but, like, why did it take you guys so long to release yours?
[568.46 --> 571.78]  Obviously, you put a lot of work into it, so it must be more than just a weekend project.
[572.74 --> 572.94]  Yeah.
[572.94 --> 578.28]  So I think one dynamic for us is we're not coupled to a single AI provider.
[578.46 --> 581.10]  So we support Anthropic, Google, OpenNet.
[581.12 --> 587.02]  We actually support, like, the full list of everything that's available because we're built on a library that covers most of them.
[587.38 --> 588.40]  What about, like, Llama?
[588.52 --> 589.32]  Can I run it locally?
[590.14 --> 590.36]  Yeah.
[590.44 --> 595.84]  So one of the – I haven't fully tested this out yet, but one of the providers – there's, like, provider support.
[595.92 --> 597.62]  One of the providers is for, like, a local model.
[597.62 --> 604.52]  So one, just testing this stuff across everything, seeing which models actually work well for this.
[604.60 --> 606.92]  The reality is, is right now very few perform well.
[607.46 --> 612.46]  We all use Anthropic and CloudSonic 4 as our default because it is the best.
[613.56 --> 616.70]  Well, some of us aren't poor and we use Opus, but sure.
[617.22 --> 618.22]  You can use Sonnet.
[618.28 --> 618.66]  That's fine.
[619.22 --> 620.56]  I use Sonnet because I'm not paying.
[620.56 --> 621.60]  I use Sonnet of all time.
[621.78 --> 622.64]  Holy cow.
[622.64 --> 627.96]  He's like, I need a mobile app because I'm going to be doing this while I'm eating vegan sushi.
[629.48 --> 631.88]  It's literally five times expensive, I think.
[632.20 --> 632.76]  So, yeah.
[633.44 --> 634.54]  It's quite a difference.
[635.02 --> 636.80]  I like it more because it's expensive.
[637.04 --> 637.88]  Like, that's my thing.
[638.02 --> 639.54]  I'm just going to expensive things.
[639.54 --> 640.42]  That is a very out of answer.
[640.42 --> 642.62]  It's like a Gucci bag or something, right?
[642.72 --> 644.64]  Like, I get the same code out.
[644.70 --> 645.62]  It doesn't matter at all.
[645.62 --> 648.74]  The models are all the same, but mine was made with Opus.
[648.86 --> 651.64]  I do have a quick question, Mr. Gucci over there.
[651.64 --> 653.80]  I noticed that you're not subbed on my channel.
[654.06 --> 656.90]  And so it's just like you're talking about spending all this money, but you don't even
[656.90 --> 658.14]  have $5 a month.
[658.32 --> 659.44]  $5 a month?
[660.28 --> 660.70]  Hang on.
[660.80 --> 661.06]  Hang on.
[661.10 --> 661.64]  How do I do it?
[661.70 --> 662.30]  How do I do it?
[662.82 --> 665.78]  $5 a month?
[667.14 --> 669.08]  I haven't been on Twitch in months.
[669.32 --> 669.92]  I swear to you.
[670.16 --> 674.68]  Oh, so before it wasn't even scheduled because you can set it up to auto renew, Adam.
[674.96 --> 675.08]  Wow.
[675.38 --> 676.50]  I think it was.
[676.54 --> 677.60]  It was at one time.
[677.82 --> 678.34]  Maybe it's a new.
[678.40 --> 679.82]  I got a new card, a new credit card.
[679.90 --> 681.18]  You know that happens and then it just.
[681.18 --> 681.82]  No, I know.
[681.96 --> 682.10]  It bounces.
[682.10 --> 682.62]  It's crazy.
[682.74 --> 685.28]  You guys make Adam do all the work and you make him pay you.
[686.20 --> 689.66]  He's getting the privilege of working with us, Dex.
[690.36 --> 690.72]  Dex.
[691.98 --> 692.48]  It's funny.
[692.58 --> 693.74]  I did see an ad a second ago.
[693.80 --> 695.16]  I've got Twitch chat up here.
[695.28 --> 696.50]  And I was like, why am I seeing an ad?
[696.56 --> 697.52]  What is this on Twitch?
[698.34 --> 698.92]  That's why.
[702.02 --> 703.62]  I'm so tilted right now.
[703.72 --> 704.32]  I just, I'm sorry.
[704.38 --> 705.16]  It's so hard to focus.
[705.16 --> 709.92]  I've seen like in Twitch chat, people are confused about the open code AI slash open code repo.
[709.92 --> 710.62]  It is super confusing.
[711.06 --> 712.62]  I'm so upset about this.
[712.66 --> 715.42]  It's so like frustrating and annoying.
[715.76 --> 718.70]  And I want to just like focus on our conversation, but it's just very annoying.
[719.00 --> 719.82]  Do you need a Snickers?
[720.40 --> 720.80]  Yeah.
[720.80 --> 724.54]  I don't think that's vegan friendly, TJ.
[724.54 --> 724.80]  I know.
[724.88 --> 725.86]  That's what he needs though.
[728.38 --> 728.70]  Okay.
[728.82 --> 729.70]  Well, all right.
[729.70 --> 731.62]  So, I mean, I want to keep going on this agent thing.
[731.70 --> 733.56]  So, you're just talking about integration and tools, all this.
[733.98 --> 741.34]  I would assume that do you have to, like, do you have to like bespokely craft every prompt to be able to use every tool?
[741.34 --> 743.56]  Or does it just simply kind of work out of the box?
[743.60 --> 746.96]  You're just like, hey, you should search for this thing now.
[746.96 --> 751.14]  Or does it tell it like, does it use reasoning in the sense that you're like, hey, what do you do?
[751.18 --> 752.20]  And it's like, this is what I should do.
[752.24 --> 753.64]  And you're like, okay, now follow step one.
[753.68 --> 754.72]  What do you do with follow step one?
[754.80 --> 756.72]  Like, how does it start using these tools?
[757.54 --> 763.32]  So, roughly what the model is good at is you give it a description of the tools and a list of tools and you give it a task.
[763.40 --> 764.58]  And it's very good at going in a loop.
[764.82 --> 766.52]  It's like, I'm going to figure out what to do.
[766.60 --> 768.72]  I'm going to tell you what tools to call, call them, give them the results.
[768.84 --> 769.74]  I'm going to like do that.
[769.74 --> 771.52]  So, it's at least a model where this works.
[771.80 --> 772.96]  That does work really well.
[773.20 --> 774.60]  There is optimization, though.
[774.64 --> 775.28]  There always is.
[775.60 --> 780.72]  So, the task tool descriptions, like the description of these task goals, like how do you describe it?
[781.82 --> 783.38]  Like, what's the schema for the input?
[783.52 --> 784.22]  Like, is that confusing?
[784.34 --> 785.70]  Does it get tripped up on things here and there?
[786.18 --> 792.32]  So, what we do is for, say, something like Anthropic, you know, they have their own version of this called Cloud Code.
[792.68 --> 794.64]  We just dump everything out from Cloud Code.
[794.64 --> 800.18]  And when you're using Anthropic, we use all the exact same task or the tool descriptions and stuff.
[801.26 --> 803.56]  So, on one hand, I'll say it does make a difference.
[803.56 --> 806.82]  If you just do a very naive approach, you're probably going to get worse results.
[807.60 --> 811.78]  I personally don't think it's like the thing that makes something 10x better.
[811.78 --> 821.54]  I think it's a thing that you can, like, kind of play with and optimize, but, and also, the end goal is, like, you don't really want it to have to be that precise because you can bring your own tools.
[822.12 --> 823.70]  You can say, here's a tool to access my database.
[823.82 --> 825.04]  Here's a tool to do XYZ things.
[825.14 --> 826.52]  It needs to be able to be flexible.
[827.30 --> 829.98]  So, we think it'll just kind of get better along those lines anyway.
[830.64 --> 834.54]  Can you give an example of, like, how you hooked it up to, like, LSP, for example?
[834.54 --> 841.66]  Because I feel like that will be, like, kind of illuminating, like, a particular example of how that, how it gets access to that.
[842.30 --> 844.70]  And how it even knows to call that also.
[845.60 --> 845.96]  Yep.
[846.18 --> 856.96]  So, with LSP, so we've experimented with a few different approaches to this, but the one that we're sticking with for now is whenever it makes an edit to the file, the response, we have a tool that's, like, the edit file tool.
[857.12 --> 861.96]  Send us, like, a patch or, like, a old string and new string in the file where we'll replace it.
[862.48 --> 863.36]  That's how it edits files.
[863.36 --> 869.92]  When it does that, the response to that tool will include any diagnostics that we found from LSP.
[870.20 --> 875.12]  So, if it's a TypeScript file where we have a TypeScript LSP running, we know that after this edit, there's these three errors.
[875.28 --> 876.24]  We say, here are the errors.
[876.36 --> 876.90]  Please fix.
[877.30 --> 879.98]  And you'll see it instantly respond with a fix.
[880.46 --> 890.38]  And this really helps hallucinations because when it, like, thinks that there's functions that don't exist on a library or any of those things, it corrects itself right away.
[890.38 --> 893.10]  And it's quite good at responding to that feedback.
[893.36 --> 898.40]  So, wait, so how does it kick all this stuff off?
[898.46 --> 901.20]  Because does that mean you actually run the LSPs yourself?
[901.20 --> 907.76]  Or do you, okay, so that means whenever I open a project, if I have open code plus Vim open, I might have two TypeScript servers.
[907.76 --> 911.74]  I may have two Go pleases or whatever they're called and all the other ones.
[911.84 --> 912.00]  Okay.
[912.72 --> 912.90]  Yeah.
[912.90 --> 917.14]  So, we originally were looking to see, can we, like, hijack any running ones?
[917.14 --> 922.38]  Because maybe you already have Vim open and you already have these LSPs configured, but you can't because they're standard input.
[922.70 --> 923.60]  Teej is big shaking.
[924.00 --> 924.82]  Big no.
[925.14 --> 926.90]  That's a big no for me, dog.
[927.16 --> 927.82]  That's a big no.
[927.82 --> 927.90]  Yeah.
[927.90 --> 927.98]  Yeah.
[928.10 --> 931.06]  So, we run our stuff in parallel.
[931.40 --> 932.66]  And there's also no configuration.
[932.90 --> 937.52]  Like, we ship out-of-the-box support for a bunch of things and everything just downloads and runs.
[937.82 --> 942.04]  Because you don't need, like, absolute precision for your exact LSB configuration that you like.
[942.52 --> 945.54]  It's more just giving the LLM something to work with.
[945.54 --> 952.48]  And then you said that's, like, at least for the way you guys have it, it's part of the edit file thing.
[952.56 --> 954.82]  So, it's like, okay, I know that I need to go and, like, edit.
[955.26 --> 958.04]  Does it also have any, like, move a file or delete file?
[958.12 --> 960.24]  Like, does it happen in every kind of, like, file?
[960.42 --> 964.52]  Because, like, I'm just interested to know how you put LSP into everything.
[964.84 --> 966.20]  Or is it just, like, edits?
[966.68 --> 967.50]  That's a good point.
[967.58 --> 971.84]  Like, we probably should give it information whenever it changes.
[972.24 --> 972.52]  All right.
[972.52 --> 973.46]  I'm making an issue right now.
[973.80 --> 974.20]  Well.
[974.20 --> 975.38]  And the right.
[975.54 --> 975.78]  Nice.
[976.04 --> 976.88]  Open source contributor.
[977.02 --> 977.56]  Let's go, TJ.
[978.48 --> 982.74]  Needs to do LSP diagnostics on file, add, delete.
[983.14 --> 983.34]  Boom.
[983.54 --> 984.70]  We do it on write.
[984.90 --> 988.04]  So, when you create a file, we do show the diagnostics to the tool.
[988.36 --> 989.90]  Or we return the diagnostics.
[990.12 --> 991.30]  So, edit and write.
[992.18 --> 993.14]  We're already returning them.
[993.32 --> 994.54]  I guess a move.
[994.66 --> 995.54]  I didn't, I don't know.
[995.64 --> 996.26]  We don't have a move file tool.
[996.26 --> 997.42]  Yeah, we don't often see.
[997.42 --> 1001.82]  I guess I haven't done much with it where it's running, like, a bash move command.
[1001.82 --> 1003.72]  But, yeah.
[1003.82 --> 1008.16]  I think we also considered, and we have this in there, which I've disabled for now.
[1008.54 --> 1010.28]  There's a tool that just returns diagnostics.
[1010.36 --> 1013.14]  So, it can choose, hey, I want to look at diagnostics right now.
[1013.20 --> 1014.04]  And it can query for them.
[1014.04 --> 1016.86]  And we have seen it use that a bunch.
[1017.00 --> 1018.28]  But it wasn't well tested.
[1018.36 --> 1019.52]  So, we're not shipping with that right now.
[1019.66 --> 1019.80]  Yeah.
[1019.92 --> 1024.92]  The models today, they're still very, like, tuned to call specific tools.
[1025.04 --> 1026.50]  Like, we've played with a lot of tools.
[1026.50 --> 1029.68]  And you can hand it a bunch of tools it's never seen before.
[1029.78 --> 1031.50]  And it just, it doesn't call them.
[1032.02 --> 1037.40]  There's something to being, like, the post-training process being catered to certain sets of tools.
[1037.40 --> 1041.68]  So, Anthropic is really a cloud for cloud 3.7 before that.
[1041.98 --> 1044.96]  Those models are the best at calling tools from a programming standpoint.
[1045.12 --> 1047.40]  They'll actually keep trying and going for it.
[1048.28 --> 1050.90]  Other models can be really smart, like Gemini 2.5.
[1050.98 --> 1053.54]  But it doesn't really, it doesn't call tools very eagerly.
[1053.90 --> 1060.46]  So, there is still, like, this phase we're in right now where you kind of have to, like, provide the set of tools that the model expects.
[1060.78 --> 1062.56]  I don't think that'll always be the case.
[1062.96 --> 1064.94]  But we've definitely given it a bunch of LSP tools.
[1064.94 --> 1069.60]  I've played with, you know, giving it go to definition and find references, things like that.
[1069.64 --> 1070.64]  And it just doesn't use them.
[1070.80 --> 1072.66]  I mean, you can get it to use them if you ask it to.
[1073.80 --> 1077.42]  But it doesn't, like, it doesn't default to kind of thinking that way.
[1077.78 --> 1078.78]  I think that'll change.
[1081.54 --> 1086.32]  So, like, how do you set it up in such a way to know to use that tool?
[1086.40 --> 1090.04]  Like, if you say, hey, use find references, how does it know when to use it?
[1090.04 --> 1097.28]  Or because isn't this kind of like a prompt skill issue going on here where it's just like you don't have a comprehensive enough system prompt for it to be able to follow?
[1098.04 --> 1099.28]  Is that what it is?
[1099.66 --> 1100.92]  I mean, it is a system prompt.
[1101.08 --> 1106.40]  That's if you look, like, at the Cloud Code system prompt, there's a lot of, like, specific tools called out.
[1106.40 --> 1110.38]  So, use the to-do tool to set up your plan before you start executing.
[1111.12 --> 1117.42]  That is how you kind of, like, massage the model into using tools that it maybe doesn't have any awareness of.
[1118.62 --> 1123.54]  It's just, yeah, there is kind of like a finite number of tools before you kind of hit diminishing returns today.
[1123.92 --> 1126.10]  It just doesn't take advantage of all of them.
[1126.22 --> 1128.90]  But it gets really good at using the handful that it uses.
[1129.72 --> 1131.40]  And I think it's in a good spot right now.
[1131.48 --> 1132.30]  I mean, it's very effective.
[1132.30 --> 1136.02]  I think these agents today are worth using and leveraging.
[1136.62 --> 1137.88]  But I do think it'll get better.
[1137.96 --> 1141.26]  I think more models will get better at calling tools and we'll have other options.
[1141.86 --> 1144.08]  So, I've never built a model.
[1144.22 --> 1146.06]  So, I just have kind of further questions.
[1146.22 --> 1147.00]  But here, Dax, why don't you go?
[1147.06 --> 1149.20]  Because then I just don't want to keep on asking questions about this.
[1149.32 --> 1150.44]  So, one last thing on that.
[1152.48 --> 1155.64]  I just totally blanked on what I was going to say.
[1156.06 --> 1156.60]  It's okay.
[1156.74 --> 1157.90]  Thanks for interrupting him.
[1157.90 --> 1158.78]  It's the name drop.
[1159.42 --> 1160.72]  I don't know if I interrupted him.
[1160.78 --> 1162.04]  We kind of, like, raced towards it.
[1162.04 --> 1164.58]  I mean, Adam is still so upset about Twitter right now.
[1164.72 --> 1165.42]  I remember.
[1165.56 --> 1165.94]  I remember.
[1167.36 --> 1167.86]  I'm going to go.
[1168.36 --> 1173.62]  So, one of the missing pieces here is you can add stuff to the system prompt and say,
[1173.84 --> 1174.64]  hey, use this tool.
[1175.48 --> 1178.22]  Dax, were you waiting for Cluely to load or something?
[1178.32 --> 1179.00]  What's going on?
[1179.14 --> 1180.04]  Yeah, it was buffering.
[1181.04 --> 1182.18]  I need my cheat sheet.
[1185.18 --> 1185.88]  One day.
[1185.88 --> 1193.70]  It's hard to tell right now whether when you're making something better, are you making something else worse?
[1193.82 --> 1195.86]  Because this LLM is such a black box.
[1195.92 --> 1198.22]  It's not like a deterministic system they can see the inside of.
[1198.80 --> 1207.20]  So, what is missing, and to me, the next major thing we work on is a set of consistent benchmarks that we can run whenever we make changes to system prompts.
[1207.74 --> 1210.16]  And these benchmarks are probably not going to be very quantitative.
[1210.54 --> 1214.18]  We're thinking that we're going to come up with a very real-world-looking code base.
[1214.60 --> 1216.86]  We'll have a bunch of, like, features that we needed to implement.
[1216.86 --> 1219.60]  And we'll have a bunch of standard prompts to have it do that.
[1220.44 --> 1226.10]  And we have this nice, like, way to see for anything we do, like, every single thing that happened diagnostics-wise.
[1227.28 --> 1232.56]  So, when we make a change, we can run it through this and see, like, the output and evaluate it somewhat qualitatively.
[1232.62 --> 1235.14]  So, it's still going to be a qualitative thing, like, did it get better or worse?
[1235.66 --> 1238.88]  But at least we have a consistent set of things we're running so we know.
[1239.58 --> 1240.84]  Right now, we're kind of flying in the dark.
[1240.84 --> 1245.60]  We're like, yeah, this made it better, but I don't know if, like, some other person is having a horrible experience because of this change.
[1245.60 --> 1249.94]  So, you're saying now you're doing not only vibe coding, but vibe testing, Dax?
[1250.94 --> 1253.26]  Vibe testing, vibe benchmarking.
[1253.46 --> 1253.66]  Yeah.
[1253.72 --> 1254.04]  Nice.
[1254.04 --> 1254.28]  In the world.
[1254.58 --> 1260.50]  It's really badly needed because there's so many benchmarks for the models, which everyone has opinions on.
[1260.94 --> 1262.02]  There's not really a benchmark.
[1262.14 --> 1262.32]  What are your opinions, Adam?
[1262.72 --> 1263.70]  Well, I don't know.
[1263.76 --> 1265.28]  They're kind of worthless, I guess.
[1266.28 --> 1266.92]  But why?
[1266.98 --> 1267.76]  Why are they worthless, Adam?
[1267.82 --> 1268.06]  Say why.
[1268.06 --> 1268.34]  Yeah, why?
[1268.34 --> 1269.24]  Why are the model?
[1269.56 --> 1270.98]  I mean, I have strong opinions.
[1271.16 --> 1275.34]  The model benchmarks, they just don't seem to correlate with, like, actual, real-world.
[1275.96 --> 1276.40]  But why?
[1276.66 --> 1277.58]  I mean, why?
[1277.72 --> 1278.34]  I don't know.
[1278.84 --> 1281.86]  I guess because they're training to, like, hit the benchmarks.
[1281.96 --> 1282.86]  Are you guys, like, quizzing me?
[1282.88 --> 1283.54]  What is going on here?
[1283.60 --> 1285.54]  No, I'm trying to get you to say.
[1285.54 --> 1287.22]  What's wrong with the ARC-AGI benchmarks, Adam?
[1287.78 --> 1289.52]  What's wrong with the ARC-AGI benchmarks?
[1290.02 --> 1292.72]  I'm trying to get you to say because they're all benchmarking Python.
[1293.52 --> 1294.84]  Oh, well, that's a thing, yeah.
[1295.54 --> 1302.50]  They're not all doing it, but the major, the SWE bench benchmark is literally just Python, which blew my mind when I learned that.
[1302.50 --> 1310.48]  But there's not, like, a benchmark today for, where there's, like, a dozen agentic coding assistants.
[1310.98 --> 1317.54]  And there's no benchmark that says, like, given the same prompts and the same code base, here's, like, it's part of it's, like, it's qualitative.
[1317.62 --> 1320.22]  But here's the one that did the best job.
[1320.28 --> 1321.06]  It did it the cheapest.
[1321.22 --> 1322.32]  It did it the most effectively.
[1323.70 --> 1327.88]  You had to have kind of, like, a grading system, and there'd have to be humans in that process.
[1327.88 --> 1331.66]  And speed's another factor, too, like, how fast did it even do this thing?
[1331.76 --> 1332.78]  Someone did this funny thing.
[1332.82 --> 1334.42]  Someone led me to something yesterday that was kind of interesting.
[1334.60 --> 1338.10]  They told the agent to, like, write a book.
[1338.20 --> 1339.52]  I can't remember exactly what it was.
[1339.56 --> 1342.80]  It was something where it would definitely, like, run in a loop for a long time.
[1343.50 --> 1346.32]  And he checked, like, how many steps did it do?
[1346.32 --> 1355.42]  I think the highest one, which was Claude, did 187 steps, like, to the LLM tool call, to the LLM tool call before it finally stopped.
[1356.08 --> 1359.00]  So that's a good way to, like, rank it, to see, like, which one's the most persistent.
[1359.18 --> 1361.38]  A lot of these models are not very, like, they give up very easily.
[1361.50 --> 1363.04]  They run into an issue and they just stop.
[1363.76 --> 1364.84]  Yeah, just like humans.
[1365.06 --> 1367.08]  AGI has really been achieved internally.
[1367.20 --> 1368.36]  Like, I'm giving up on this.
[1368.66 --> 1370.22]  They're going to just ask me again later.
[1370.26 --> 1370.78]  It's fine.
[1371.42 --> 1371.68]  Yeah.
[1372.34 --> 1372.82]  All right.
[1373.24 --> 1373.48]  All right.
[1373.48 --> 1374.54]  I got real questions here.
[1374.54 --> 1376.68]  I also agree RKGI sucks.
[1376.80 --> 1376.94]  Okay.
[1377.04 --> 1384.72]  But now that we got that out of the way, with that stated, so, like, how do you start a loop?
[1384.72 --> 1386.52]  And how do you determine that a loop's done?
[1386.68 --> 1390.16]  Like, because, like, I know you're going to say, here's what the user said.
[1390.40 --> 1395.22]  You have some sort of system prompt to say, hey, you can accomplish this task via these tools, whatever it says.
[1395.38 --> 1402.18]  How do you say, okay, I either re-prompt the system again to execute step one of a several instruction plan.
[1402.52 --> 1404.82]  Do you have to, like, manually parse it out?
[1404.92 --> 1409.84]  How do you, like, what's the interaction between the model and this to, like, start this looping process?
[1409.84 --> 1415.46]  Because that's what's kind of confusing to me since I've never actually built the agent itself is that I imagine that there's some –
[1415.46 --> 1415.48]  Yeah.
[1415.48 --> 1417.72]  You have to do some weird parsing goals.
[1417.88 --> 1422.70]  What's cool is you don't have to do anything because this is a responsibility of the model.
[1422.86 --> 1428.28]  So when you make a call to an LLM, it'll generate a bunch of text and it'll stop, right?
[1428.78 --> 1430.28]  There's reasons for why it stops.
[1430.36 --> 1434.08]  Sometimes it stops because, oh, I'm done generating text.
[1434.08 --> 1435.18]  I'm done with everything I need.
[1435.70 --> 1436.80]  So that's the SOP reason.
[1437.34 --> 1441.24]  But it could also stop because I can't continue until you execute these tools.
[1441.90 --> 1445.30]  So you don't have to figure out when to interrupt it and, like, do something else.
[1445.84 --> 1446.82]  It'll tell you.
[1446.82 --> 1450.92]  It'll stop and say, call these tools and then continue with the responses to the tools.
[1451.58 --> 1452.70]  That's baked into the models.
[1452.96 --> 1454.02]  So that part's pretty easy.
[1454.12 --> 1455.50]  It's, like, very easy to build, like, that loop.
[1456.82 --> 1458.16]  So that's not even a loop then?
[1459.72 --> 1461.60]  Where you keep asking until it's done.
[1461.60 --> 1467.62]  Eventually, it's like a wild true break if the SOP reason is done.
[1467.72 --> 1473.20]  It's part of the request that you literally send, like, to Claude is, like, yo, I have these tools available.
[1473.38 --> 1474.86]  They can do these different things.
[1475.08 --> 1479.06]  And then, like, Anthropic is the one, right?
[1479.18 --> 1483.88]  If I'm understanding, from what I've seen before, you literally send them the tool definitions.
[1484.22 --> 1486.34]  And then the model says, I'm going to run this thing.
[1486.42 --> 1487.24]  Then you're, like, cool.
[1487.28 --> 1488.24]  You said I'm going to run that thing.
[1488.34 --> 1489.22]  Do I run it?
[1489.54 --> 1490.72]  I send it back to Anthropic.
[1490.72 --> 1492.72]  And I said, just like you can do a conversation.
[1493.40 --> 1493.96]  Oh, okay.
[1493.98 --> 1497.52]  So it's not you going, if you were to execute, what would you do?
[1497.58 --> 1498.50]  And it's like, I would do these things.
[1498.52 --> 1500.16]  And you're like, okay, I'm going to post out all that things.
[1500.34 --> 1501.28]  I'm going to execute it.
[1501.36 --> 1503.78]  Then resend effectively the whole previous conversation.
[1504.22 --> 1504.72]  Plus the current one.
[1504.72 --> 1505.18]  That sounds hard.
[1505.20 --> 1505.92]  What's next, bro?
[1506.00 --> 1508.52]  Because that seems like it would just go, like, it would just do this forever.
[1508.52 --> 1509.88]  Because it always comes up with new stuff.
[1509.88 --> 1511.46]  Like you and Devin, basically.
[1511.98 --> 1512.30]  Exactly.
[1512.84 --> 1514.14]  Me and Devin are tight.
[1514.58 --> 1514.80]  Yeah.
[1517.80 --> 1518.16]  Yeah.
[1518.16 --> 1520.18]  So it's actually, it's very easy.
[1520.18 --> 1522.78]  That's why building, like, a basic prototype of an agent.
[1523.04 --> 1523.40]  Yeah.
[1523.40 --> 1524.22]  It's like a weekend.
[1524.98 --> 1525.66]  Weekend project.
[1526.32 --> 1526.68]  Yeah.
[1526.78 --> 1529.76]  Because you just would define, like, edit file as, like, a tool.
[1529.84 --> 1531.70]  And then you'd give that to the model.
[1531.70 --> 1536.10]  And then you'd define, like, some other simple ones that you would need to do stuff locally.
[1536.28 --> 1537.14]  Search for files.
[1537.26 --> 1537.56]  I don't know.
[1537.56 --> 1539.30]  I don't know what other ones are, like, the normal ones.
[1539.36 --> 1539.46]  Yeah.
[1540.16 --> 1540.60]  And that's it.
[1540.72 --> 1540.92]  Yeah, grip.
[1541.24 --> 1541.46]  Yeah.
[1541.54 --> 1541.70]  Yeah.
[1542.06 --> 1543.06]  Find, grip, set.
[1543.24 --> 1543.76]  It runs, grip.
[1543.76 --> 1544.20]  Yeah.
[1544.92 --> 1545.08]  Yeah.
[1545.14 --> 1548.30]  It's got a bash tool, like, where they can actually run bash commands.
[1549.22 --> 1550.26]  That one's always good.
[1550.38 --> 1552.50]  Because it's like, oh, I'll let you run any bash command.
[1552.58 --> 1553.62]  And then it just runs anything.
[1553.90 --> 1554.64]  That's a really smart move.
[1554.64 --> 1556.96]  That's actually my biggest worry is, like, how, okay.
[1557.00 --> 1559.24]  So how do you protect against destructive operations?
[1560.36 --> 1564.76]  Do you just simply say, hey, user, you must, like, approve of said operations?
[1564.76 --> 1568.52]  Because how do you know it's not going to, like, RMRF, root, no preserve?
[1568.96 --> 1570.46]  So there's a lot of different approaches here.
[1570.62 --> 1577.08]  Most of these agentic coding assistants have a permissions model where, basically, you know,
[1577.12 --> 1579.80]  certain tools have to be granted permission.
[1580.42 --> 1585.66]  Most of them also have, like, a full auto mode where you can bypass all those things if you know you're in a sandbox or whatever.
[1585.96 --> 1588.38]  And then there's, like, there's approaches with sandboxing.
[1588.38 --> 1594.88]  So, like, Codex CLI by OpenAI, they've got, they use, like, the Apple, I don't remember what, seatbelt?
[1595.56 --> 1597.28]  It's some kind of a sandboxing thing.
[1597.44 --> 1604.40]  Same with Linux has a sandboxing thing where it basically constrains it to work only in this directory, like, in the project directory.
[1605.14 --> 1607.18]  And then some network constraints as well.
[1608.14 --> 1611.80]  Yeah, some people have, some people run cloud code in a Docker container.
[1612.68 --> 1616.78]  Docker containers aren't, like, a perfect, like, security-wise, they're not, like, a perfect sandbox.
[1616.78 --> 1618.74]  But they're pretty good, practically speaking.
[1619.44 --> 1624.50]  We're not thinking about that stuff too much right now because we need to build something that's fun to use first.
[1625.12 --> 1628.18]  And then we'll figure out how to, like, layer in some of these sandboxing things.
[1629.28 --> 1629.72]  Sorry.
[1629.94 --> 1631.26]  That was just such a fun statement.
[1632.20 --> 1632.64]  Okay.
[1632.72 --> 1638.34]  So does that mean, are you saying that Windows was always right asking for permission for everything, including deleting files?
[1640.60 --> 1642.52]  That's what OpenCode does right now, right?
[1642.54 --> 1643.10]  So, yes.
[1643.56 --> 1644.88]  Yes, Windows was correct.
[1644.88 --> 1647.14]  Just say, yeah, Dax.
[1647.18 --> 1647.64]  You got it.
[1647.76 --> 1647.90]  Yeah.
[1648.00 --> 1649.14]  Dax, stop reading Twitter.
[1649.72 --> 1651.16]  I know you're upset.
[1651.84 --> 1653.90]  I know you guys are upset about this.
[1654.04 --> 1656.44]  I have so many questions.
[1656.54 --> 1661.00]  So I didn't even know that there was already this agentic loop, effectively, that exists.
[1662.16 --> 1663.44]  That's what's inside of Cursor.
[1664.26 --> 1664.60]  Well, yeah.
[1664.70 --> 1666.34]  I mean, I know that Cursor has it.
[1666.34 --> 1675.52]  But I thought that you wrote the loop, not that these models effectively can kind of break and say, hey, I need more information before continuing.
[1676.80 --> 1686.48]  I mean, you still do have a loop on your side because if it's a while loop, it's still a loop where you're having to keep calling the LLM with all the messages until it tells you to stop, basically.
[1686.48 --> 1686.92]  Yeah.
[1689.24 --> 1690.04]  Very exciting.
[1690.62 --> 1692.06]  And there's some tricks here, too, right?
[1692.14 --> 1696.10]  There's obviously a limited context window on a lot of these models.
[1696.70 --> 1698.26]  Sometimes they're pretty tight.
[1699.00 --> 1713.30]  So if that loop is going and the context window is starting to approach the limit, we will pause for a second, take the whole history, send it to LLM, ask it to summarize, and then we'll continue the loop just with a summary.
[1714.26 --> 1714.92]  Is that dangerous?
[1714.92 --> 1717.04]  In what way?
[1718.16 --> 1718.48]  I don't know.
[1718.62 --> 1725.22]  Well, I mean, dangerous in the sense that the moment you ask it to summarize, you do effectively a compression algorithm on top of it, a very lossy one.
[1725.86 --> 1727.34]  Like, how far does it get off?
[1727.34 --> 1727.56]  It's pretty effective.
[1727.56 --> 1728.56]  Do you get, like, warnings about it?
[1730.66 --> 1737.92]  Does OpenCode give you, like, a warning, like, hey, we have to do a lossy compression on your history, so therefore it may start going haywire?
[1737.92 --> 1747.86]  So we have that information to show you, but it works so well that, like, it's kind of, yeah, like, the experience feels like you have infinite context.
[1748.34 --> 1755.82]  Most of the tokens that it's taken up are like, here's the stack trace from one thing that I fixed eight minutes ago.
[1755.82 --> 1756.06]  Yeah.
[1756.28 --> 1762.80]  I mean, really, a better practice is just to keep creating new sessions and to not let any context window grow very far.
[1763.28 --> 1765.76]  Summary is, like, compacting it is basically doing that.
[1765.82 --> 1770.36]  It's basically forcing you to start a new session, but it's giving it a little bit of context, I guess, in the form of a summary.
[1770.36 --> 1778.64]  But it's generally, like, you don't want to keep a long context window filled up with a session that's, you know, 25 messages long.
[1778.72 --> 1781.30]  It's, like, it's getting less and less effective over time.
[1781.74 --> 1794.86]  Yeah, and most, I mean, if you think about, like, how much of the actual tokens you're typing in, telling it and giving it direction, it's very little compared to how much it's, like, getting from reading file or, like, a, oh, I'm going to change this file.
[1794.86 --> 1801.14]  It was 250 lines long, and I changed a bunch of the lines to a little, huge diff, tons of tokens.
[1801.34 --> 1802.42]  Oh, we don't need that now.
[1802.60 --> 1804.10]  That was an hour ago.
[1804.84 --> 1808.76]  Yeah, the effectiveness of the model is all tied to, like, signal to noise.
[1809.06 --> 1811.86]  How much signal can you give it without noise?
[1811.92 --> 1815.14]  And the longer your session goes, just obviously there's going to be more noise.
[1816.96 --> 1818.76]  Make a new session for different things.
[1819.08 --> 1820.56]  That's what we're saying, right?
[1820.60 --> 1822.66]  So if I'm going to do a new task, I should start a new session.
[1823.22 --> 1823.56]  Yep.
[1823.56 --> 1826.06]  And sometimes, yeah, sometimes you want to do things in parallel.
[1826.20 --> 1827.30]  It's another reason to start a new session.
[1827.44 --> 1829.90]  You, like, kick off one thing, new session, kick off another thing, new session.
[1830.86 --> 1835.30]  I found my brain can only handle so many of those, but people do like paralyzing a lot.
[1835.56 --> 1841.94]  So could you have an agent that spawns sessions so it is actually the compression algorithm for your brain?
[1841.94 --> 1842.56]  Sub-agents.
[1842.90 --> 1843.62]  It's all the rage.
[1843.98 --> 1845.26]  It's all the rage right now.
[1845.98 --> 1847.08]  Teej is on top of it.
[1847.38 --> 1847.90]  Oh, I know.
[1847.98 --> 1848.18]  I know.
[1848.28 --> 1850.00]  I know everything there is to know about agents.
[1850.12 --> 1851.04]  I came super prepared.
[1851.16 --> 1852.78]  I started drama on X.com.
[1852.78 --> 1853.90]  I've been reading the everything application.
[1853.90 --> 1856.82]  I've been reading false websites in the chat.
[1856.90 --> 1863.14]  I have 17 misinformation bots in the chat right now spreading fake news about open code.
[1865.78 --> 1866.30]  Nice.
[1867.00 --> 1869.64]  Sub-agents are an interesting concept.
[1869.64 --> 1872.90]  I think they should be used surgically.
[1873.40 --> 1880.28]  I think there's a trap of, like, having just sub-agents that are general purpose just to, like, parallelize work.
[1880.40 --> 1885.76]  Because we're not, like, open code, at least, is not intending to be an asynchronous agent.
[1885.76 --> 1887.78]  Like, you are in the loop on purpose.
[1887.78 --> 1893.94]  Like, we want you, as a programmer, able to interact with the agent and to steer it in the right directions.
[1894.28 --> 1899.12]  I think if you get into, like, eight sub-agents doing all the work, there's very little visibility into what's happening.
[1899.34 --> 1903.10]  You lose the permissions model, like, the ability to inspect what's going on.
[1903.16 --> 1907.16]  You just can't, like, your brain can't handle those eight sub-agents going in parallel.
[1907.16 --> 1909.68]  So now you've kind of got, like, a background agent, right?
[1909.72 --> 1911.36]  You've got Jules or whatever else.
[1912.36 --> 1919.08]  And that's a different thing than what we're trying to create, which is very much human in the loop, human guiding the agent.
[1919.18 --> 1924.46]  So I think sub-agents, like, using them, so there's a task agent in Cloud Code or a search agent.
[1924.46 --> 1930.78]  It basically is just a read-only agent that can search through files and limit the amount of context noise in your main context window.
[1930.88 --> 1931.84]  That one makes a lot of sense.
[1931.84 --> 1937.32]  I think, like, a code review or a planning agent that's a sub-agent, I think those can make sense.
[1937.68 --> 1943.08]  We're going to play with a lot of that stuff, but I think, like, just general purpose sub-agent that does everything,
[1943.22 --> 1946.70]  and then you're just trying to parallelize all the tasks, I don't know.
[1946.76 --> 1947.64]  I think that's kind of a trap.
[1948.40 --> 1952.98]  Can we get one that's like a Zoomer version of it so that then the rest of the time it responds like a Zoomer?
[1953.06 --> 1955.18]  I want Tanner in open code for me.
[1955.70 --> 1956.38]  You know what I'm saying?
[1956.38 --> 1962.12]  Like, I want to write my prompt, and then it turns it into Tanner, and Tanner reads everything off to me.
[1962.38 --> 1965.48]  Hey, guys, it's me, Tanner, here, just letting you know we're about to edit the files.
[1965.66 --> 1966.44]  Okay, sweet.
[1966.90 --> 1968.82]  That's what I think you guys are missing.
[1969.06 --> 1972.66]  Like, if you're going to differentiate on product, that's what you—oh, Prime, yours is way better.
[1973.14 --> 1973.84]  Yours is way better.
[1974.08 --> 1975.64]  I'm a way better Tanner dude.
[1976.56 --> 1978.12]  I don't know who Tanner is.
[1978.16 --> 1978.70]  I'm not going to lie.
[1978.88 --> 1980.28]  I was trying to laugh and pretend.
[1980.42 --> 1982.40]  It's an AI voice on Prime's channel.
[1982.80 --> 1983.52]  Oh, gotcha.
[1983.88 --> 1984.24]  Yeah, yeah, yeah.
[1985.14 --> 1986.48]  I'm outed as not watching Twitch.
[1986.56 --> 1987.12]  I'm sorry, guys.
[1987.20 --> 1987.92]  I love you guys.
[1988.04 --> 1988.60]  I don't watch Twitch.
[1988.60 --> 1988.62]  Don't worry.
[1988.68 --> 1990.20]  Someone gifted you a sub, loser.
[1990.40 --> 1990.66]  Yes.
[1991.58 --> 1993.70]  A cp variable would be the first thing.
[1994.80 --> 1996.12]  Adam, let me be honest.
[1996.20 --> 1999.90]  Let me be honest with you, and even though this is in public, I'm going to be very frank with you.
[2000.00 --> 2003.88]  If you were watching Twitch, I'd be really mad because I'd be wondering, what the heck?
[2003.92 --> 2005.56]  Who's working on Terminal.shop right now?
[2005.56 --> 2006.02]  Yeah, exactly.
[2006.44 --> 2006.80]  Really?
[2007.16 --> 2008.26]  I've got three jobs.
[2008.34 --> 2009.50]  I can't be watching Twitch.
[2009.50 --> 2012.20]  You do not have time to be watching Twitch, Adam.
[2012.20 --> 2015.04]  You need to be building Terminal.shop.
[2015.58 --> 2020.76]  And as your co-founder, I reject the notion of Adam on Twitch.
[2021.10 --> 2021.42]  Yes.
[2022.08 --> 2024.58]  If you knew who Tanner was, I'd be disappointed.
[2024.74 --> 2026.30]  It was a test all along.
[2028.04 --> 2028.34]  True.
[2028.44 --> 2030.94]  Really putting the individual, an individual contributor.
[2031.76 --> 2033.02]  Man, I love that line, though.
[2033.10 --> 2033.40]  That one.
[2033.84 --> 2034.46]  It was very good.
[2035.10 --> 2035.30]  Yeah.
[2036.30 --> 2039.98]  Adam's building open code so that he can have it work on Terminal.
[2039.98 --> 2041.22]  This is all like a straightforward plan.
[2041.38 --> 2042.60]  Oh, so we're investing.
[2043.08 --> 2043.98]  We're sharpening the axe.
[2044.44 --> 2044.80]  Nice.
[2045.18 --> 2047.12]  We're big fans of sharpening the axe around here, so.
[2047.20 --> 2047.46]  Yeah.
[2048.16 --> 2048.34]  Yeah.
[2048.66 --> 2049.54]  That's really smart.
[2050.14 --> 2053.26]  It's going to be so sharp when he's done with it in a few months.
[2053.50 --> 2054.92]  It's going to be so sharp.
[2055.90 --> 2056.56]  Oh, man.
[2057.00 --> 2057.32]  Okay.
[2057.40 --> 2059.72]  So, really, that's what it takes to build an agent.
[2059.80 --> 2065.04]  What is the part that you didn't realize was going to be the hardest when building an agent?
[2065.04 --> 2066.96]  What's the thing that caught you most off guard?
[2068.14 --> 2070.18]  You know, it's just like every product.
[2070.48 --> 2073.34]  The 80% is easy, and you get into all the edge cases.
[2073.58 --> 2078.80]  It's like, what happens when someone cancels the loop, and it's in the middle of a tool call?
[2078.96 --> 2080.02]  Is that handled gracefully?
[2080.60 --> 2083.40]  What happens when it hits the context window but didn't get a chance to summarize?
[2083.62 --> 2087.82]  There's just infinite of these weird cases, and it's multiplied by the fact that, again,
[2087.88 --> 2090.24]  these things are not very deterministic.
[2090.24 --> 2093.28]  So, discovering them is quite hard.
[2094.54 --> 2096.72]  But, yeah, I think for me, it's been all the edge cases.
[2096.90 --> 2098.50]  Adam's been mostly working on UI stuff.
[2099.06 --> 2102.82]  Yeah, the TUIs are just hard every time I work on a TUI.
[2103.26 --> 2107.64]  Would you say it's the way that Charm does the rendering that's hard,
[2107.94 --> 2113.60]  or is it the way that Charm takes over the open code repo and has to release it that's hard?
[2114.36 --> 2116.08]  Like, what would you say TUIs are hard?
[2117.00 --> 2118.76]  Charm's in both sides right now.
[2118.76 --> 2119.70]  That's what I'll say.
[2120.24 --> 2121.20]  It's multi-front.
[2121.54 --> 2122.40]  Multi-front attack.
[2122.40 --> 2124.66]  And TJ's like, that is not okay.
[2125.52 --> 2126.14]  All right.
[2126.76 --> 2127.70]  Do not associate.
[2127.92 --> 2129.40]  I could be literally anybody.
[2129.58 --> 2130.98]  It could be someone else over here.
[2131.24 --> 2133.58]  I am not part of this podcast at all.
[2133.60 --> 2134.52]  That's Miami, TJ.
[2135.00 --> 2135.92]  This is Miami, TJ.
[2135.98 --> 2137.42]  I'm missing your chain, Dex.
[2137.44 --> 2138.62]  That's what I need to complete it.
[2138.68 --> 2141.46]  It really changes the look of the turtleneck when you throw a chain on.
[2141.84 --> 2142.94]  It's so different.
[2143.38 --> 2145.78]  The turtleneck does become way, way different.
[2145.78 --> 2148.18]  Here's actually the tough.
[2148.30 --> 2150.78]  I have one tough question for Adam.
[2153.62 --> 2159.32]  Does watching Twitch make you not a vegan because you're consuming something made by animals?
[2160.62 --> 2161.12]  Aminals.
[2161.54 --> 2162.28]  I heard that.
[2162.28 --> 2166.66]  Wow.
[2167.46 --> 2169.24]  That was unexpected.
[2171.24 --> 2172.12]  I love it.
[2173.32 --> 2173.56]  Yeah.
[2173.66 --> 2177.18]  Does using electricity mean you're not a vegan because you're consuming gas or juice?
[2177.18 --> 2179.98]  You hate the environment.
[2180.66 --> 2181.96]  Adam, why'd you agree to come on?
[2182.02 --> 2182.56]  I was surprised.
[2182.88 --> 2183.24]  I don't know.
[2183.32 --> 2183.48]  Yeah.
[2184.16 --> 2184.42]  Okay.
[2184.62 --> 2185.02]  Okay.
[2185.46 --> 2185.78]  Okay.
[2185.82 --> 2190.20]  We could probably do one more real question, but is the Tui hard because of the way, because
[2190.20 --> 2194.58]  I know we've worked on Charm together and it has this thing where it has to render from
[2194.58 --> 2195.18]  top to bottom.
[2195.30 --> 2197.16]  So it makes like modals and various things difficult.
[2197.16 --> 2199.24]  Like, have you guys, because I know we talked about this.
[2199.24 --> 2205.72]  Were you considering actually still building like the non-top to bottom style rendering
[2205.72 --> 2207.80]  that is currently, is it Bubble Tea?
[2207.96 --> 2208.58]  Is that the name of it?
[2208.78 --> 2209.00]  Yeah.
[2209.00 --> 2212.46]  You're wanting to change it out to something that's more like you have a scene and you layer
[2212.46 --> 2212.68]  it?
[2213.12 --> 2214.46]  I like Bubble Tea.
[2214.84 --> 2215.28]  Yeah.
[2215.46 --> 2216.02]  It's very good.
[2216.36 --> 2217.60]  I've grown to really enjoy it.
[2217.72 --> 2219.88]  I enjoy Go more all the time.
[2220.18 --> 2221.76]  I kind of hated Go at first.
[2221.78 --> 2222.64]  Suck on it, Twitter.
[2223.18 --> 2223.88]  Suck on that.
[2224.54 --> 2226.60]  I'm actually enjoying Go quite a bit.
[2226.60 --> 2226.74]  It's okay.
[2227.40 --> 2229.12]  It's nothing about the actual like developer.
[2229.12 --> 2230.26]  You can learn to love anything.
[2230.76 --> 2231.30]  Yeah, you can learn.
[2231.38 --> 2231.74]  Yeah, sure.
[2232.06 --> 2236.36]  If we spent six months telling you you had to write something in this and that it was
[2236.36 --> 2238.08]  good, Adam, you would say Rust is good.
[2238.38 --> 2240.70]  Like, this is not a strong endorsement.
[2241.38 --> 2243.52]  Do not over-index on this.
[2243.52 --> 2249.02]  The thing that makes Tui hard is like coming from being a web developer, I can't like, there's
[2249.02 --> 2251.00]  so many more constraints and that's nice.
[2251.14 --> 2251.50]  Sure.
[2251.60 --> 2254.82]  In a lot of ways, like designing a Tui is kind of fun because you have all these constraints,
[2254.82 --> 2259.66]  but it also just sucks when I can't just like let the user do things you can just do on
[2259.66 --> 2262.06]  the web and vertical space is so constrained.
[2262.34 --> 2267.40]  Like you're so just like you're trying to like minimize absolutely every pixel.
[2267.52 --> 2268.92]  It's just, it's just stressful.
[2268.92 --> 2272.98]  It's just like getting all the little things right and making a good Tui experience just
[2272.98 --> 2275.36]  kind of like stretches all your brain cells.
[2275.44 --> 2276.02]  It just sucks.
[2276.36 --> 2277.48]  And overlays are hard.
[2278.42 --> 2279.04]  Overlays are hard.
[2279.10 --> 2279.22]  Yeah.
[2280.50 --> 2280.82]  Okay.
[2281.00 --> 2282.20]  See, TJ, that was a real question.
[2282.30 --> 2283.52]  TJ thought I was going to make another joke.
[2283.60 --> 2284.00]  I wasn't.
[2284.00 --> 2286.84]  And I was in there to actually, cause I'm actually curious about it because I wrote
[2286.84 --> 2291.42]  when I did, uh, when I did a flappy bird, I actually gave up using that and just wrote
[2291.42 --> 2296.40]  my own scene and did Z indexing because I wanted to be able to do layering and it's just,
[2296.48 --> 2300.70]  it's just easier, but then it takes care of all the colors and the spacing and how you
[2300.70 --> 2303.46]  do that is actually a pretty complicated subject at the end of the day.
[2304.58 --> 2304.94]  Yeah.
[2304.94 --> 2308.28]  I was just imagining you asking exactly the same question.
[2308.28 --> 2311.68]  Nah, that joke's only funny ones.
[2311.68 --> 2314.36]  Oh man.
[2315.18 --> 2315.44]  Okay.
[2315.48 --> 2318.38]  Well, anything else you guys want to let us know about agents or open code?
[2319.10 --> 2322.08]  We should, we have, we said on the podcast, it's SST slash open code.
[2322.22 --> 2323.52]  I've been pasting it in the chat.
[2323.58 --> 2323.84]  I know.
[2324.08 --> 2327.44]  Links will be in the description and even maybe in a pin comment.
[2327.44 --> 2328.38]  If you're lucky, Adam.
[2328.38 --> 2329.66]  Oh, that'd be amazing.
[2330.12 --> 2331.54]  S S T slash.
[2331.54 --> 2334.58]  I'm just already prepared for all the YouTube comments that are like, wait, it's not open
[2334.58 --> 2335.92]  code AI slash open code.
[2336.02 --> 2336.72]  That's not the one.
[2336.80 --> 2344.18]  Well, now that you said that you've just guaranteed 90% of the comments will be the wrong link.
[2344.26 --> 2344.74]  Adam.
[2345.80 --> 2346.48]  Thanks, Adam.
[2346.48 --> 2352.54]  So that's, so we, maybe we'll help you out.
[2352.58 --> 2356.26]  Maybe we'll cut that part from the final thing, but I will, I will post the links.
[2356.32 --> 2359.08]  I'll make sure the real links are there so that people can find it and test it out.
[2359.58 --> 2359.72]  Yeah.
[2359.76 --> 2360.14]  Thanks for asking.
[2360.14 --> 2365.42]  I still have no idea how to build an agent, but I really appreciate the talk.
[2365.52 --> 2366.36]  It makes me feel better.
[2368.78 --> 2369.36]  That's okay.
[2369.50 --> 2372.62]  We are going to ask open code to build us an agent next week.
[2374.36 --> 2374.72]  Yeah.
[2374.78 --> 2375.26]  There you go.
[2375.64 --> 2376.10]  Or later.
[2376.10 --> 2377.64]  It's going to write one loop.
[2378.28 --> 2378.40]  Yeah.
[2378.58 --> 2380.30]  It's, it'll be like, you'll just see it.
[2380.36 --> 2380.94]  It'll be super obvious.
[2381.10 --> 2382.88]  It's the same thing as sending completion requests.
[2383.00 --> 2384.52]  It's just tool requests.
[2384.64 --> 2385.06]  That's it.
[2385.78 --> 2386.14]  Okay.
[2386.24 --> 2388.08]  And then put it in a loop until it's done.
[2388.10 --> 2388.40]  Make it easy.
[2388.94 --> 2389.16]  Yeah.
[2389.64 --> 2389.94]  Okay.
[2389.94 --> 2390.16]  Cool.
[2390.36 --> 2390.76]  Okay.
[2390.84 --> 2391.06]  Okay.
[2391.08 --> 2391.30]  Okay.
[2391.94 --> 2392.20]  Okay.
[2392.30 --> 2393.04]  Well, thanks Dax.
[2393.10 --> 2393.66]  Thanks Adam.
[2394.02 --> 2395.58]  Thanks everyone for watching and listening.
[2396.38 --> 2397.94]  It's been another episode of the standup.
[2398.38 --> 2398.52]  Bye.
[2398.52 --> 2399.02]  Hopefully you enjoyed.
[2399.28 --> 2399.66]  Bye.
[2399.66 --> 2399.76]  Bye.
[2399.76 --> 2401.30]  Boot up the day.
[2402.96 --> 2403.80]  Vibe coping.
[2404.22 --> 2406.06]  Errors on my screen.
[2407.44 --> 2408.96]  Terminal coffee.
[2409.68 --> 2410.88]  In hand.
[2411.94 --> 2413.88]  Living the dream.
