[0.00 → 6.06] This is the episode though where Casey's going to find out that like he's been calling all three of us web developers
[6.06 → 10.12] But Trash is the only one who actually knows how to develop for the web
[10.12 → 14.38] I mean you can use TypeScript on the server
[14.38 → 19.58] Okay, so Trash is a web developer and you guys are web developers is what you're saying
[19.58 → 20.36] Yes, thank you
[20.36 → 26.00] I'm just a Norrie but everyone's so bad at their craft that I just rise to the top
[26.00 → 34.24] Which is hilarious you can just be like normal and that's like perfect
[34.24 → 38.40] Nice then they give you talks at render ATL
[38.40 → 42.46] Exactly they're like this guy's a genius I'm like oh look I just know the basic
[42.46 → 43.10] Oh hey prom
[43.10 → 45.38] Oh howdy Moody
[45.38 → 47.12] Hello
[47.12 → 49.56] Are you ready for some TypeScript Prime?
[49.56 → 50.74] I am so ready for TypeScript
[50.74 → 54.62] Yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah yeah
[54.62 → 56.08] Anyway sorry
[56.08 → 59.00] Alright hey I'm going to do the introduction right now okay
[59.00 → 59.78] Okay
[59.78 → 60.52] I'm low-key freaking out
[60.52 → 61.00] Okay, okay
[61.00 → 61.90] Hey
[61.90 → 63.30] You got this Trash
[63.30 → 63.86] You got this
[63.86 → 64.46] You're the man
[64.46 → 65.28] I'm so ready for this
[65.28 → 66.26] Trash you are awesome
[66.26 → 66.80] You got this
[66.80 → 68.90] I'm free sawing this okay this isn't going to be
[68.90 → 69.50] Trash
[69.50 → 69.90] Alright
[69.90 → 70.70] Just go
[70.70 → 71.08] Here we go
[71.08 → 73.96] Today's let's see today's stand-up is a special one
[73.96 → 77.54] We have with us a legendary engineer Chris Bautista
[77.54 → 79.48] You probably know better as Trash Dev
[79.48 → 84.48] Going to give us an amazing presentation about TypeScript build system speed performance
[84.48 → 85.74] Usability
[85.74 → 87.32] All the good stuff
[87.32 → 88.32] Trash
[88.32 → 91.16] Unironically drinks from a mason jar just like me
[91.16 → 91.96] So good job Trash
[91.96 → 92.74] Really appreciate that
[92.74 → 93.42] Hey cheers buddy
[93.42 → 96.66] But second off he's actually a very talented engineer
[96.66 → 99.50] And if I were to have TypeScript problems
[99.50 → 101.96] There's the first person I would call would be Trash
[101.96 → 103.54] He's actually quite excellent
[103.54 → 104.92] So I'm very excited about this talk
[104.92 → 110.00] And I'm even more excited about Casey being confused by the fact
[110.00 → 111.46] That there is JavaScript
[111.46 → 112.74] That's not JavaScript
[112.74 → 113.56] That can't run
[113.56 → 115.58] That takes a long time to make into JavaScript
[115.58 → 116.44] And I'm just
[116.44 → 117.06] This is just
[117.06 → 118.82] I'm very excited about this whole thing
[118.82 → 119.88] So this is going to be excellent
[119.88 → 121.00] So Trash
[121.00 → 122.70] Could you please take it away for us?
[122.70 → 125.18] So this is how I'm going to approach this
[125.18 → 127.86] Because I want to get through like
[127.86 → 130.88] The less interesting parts I feel like in my opinion
[130.88 → 133.38] And get to the stuff that I think Casey will get interested in
[133.38 → 135.64] So I'm going to pick pieces of my presentation
[135.64 → 138.08] To show you just some weird quirks that happen in TypeScript
[138.08 → 141.40] And then we'll kind of like go into the more in-depth stuff
[141.40 → 142.34] And kind of just like
[142.34 → 144.40] We'll probably just end up freestyling at that point
[144.40 → 145.92] And this is also weird for me
[145.92 → 147.16] Because I only have one monitor
[147.16 → 148.58] So I have to like
[148.58 → 149.94] You're basically going to see me like
[149.94 → 151.16] Finagling all this stuff live
[151.16 → 152.84] So Josh or whoever's going to edit this
[152.84 → 154.10] Can edit it
[154.10 → 154.68] So
[154.68 → 157.42] So first things first is like
[157.42 → 159.76] TypeScript is an interesting language
[159.76 → 160.20] Where
[160.20 → 162.34] In my opinion
[162.34 → 164.72] There's like a spectrum of like
[164.72 → 165.86] Skill level
[165.86 → 167.16] I don't want to say skill level
[167.16 → 169.02] But just like familiarity with the
[169.02 → 170.40] With the language
[170.40 → 172.10] And I feel like most people
[172.10 → 173.50] Don't take the time
[173.50 → 175.50] To actually jump over that hurdle
[175.50 → 176.56] And get to the more advanced stuff
[176.56 → 177.86] Not because it's their fault
[177.86 → 178.54] But more of like
[178.54 → 179.98] The work that they're doing
[179.98 → 181.46] Doesn't really actually call for it
[181.46 → 182.88] So like the talk I'm doing
[182.88 → 184.04] It's very high level
[184.04 → 185.80] Because I think most people
[185.80 → 187.10] Fall into that kind of bucket
[187.10 → 188.74] But then there are pieces of my talk
[188.74 → 189.92] That I kind of skim over
[189.92 → 191.80] Because I don't want your eyes to glaze over
[191.80 → 192.92] During a presentation, right?
[193.42 → 194.78] And I was also at the end of the conference
[194.78 → 195.88] Trash, can I interrupt one second?
[196.56 → 196.94] Yeah, yeah, yeah
[196.94 → 198.34] What is the title of your talk?
[198.44 → 200.22] It is called WTF TypeScript
[200.22 → 201.20] Literally
[201.20 → 204.16] Dude, I had some bomb-ass memes
[204.16 → 205.08] During this presentation
[205.08 → 206.66] That I was so terrified
[206.66 → 207.96] That weren't going to land
[207.96 → 209.20] But thankfully
[209.20 → 210.98] Everyone started laughing
[210.98 → 211.88] And I just like
[211.88 → 213.20] Then all my like nervousness went away
[213.20 → 214.40] I like called it out in the beginning
[214.40 → 215.38] I was like
[215.38 → 217.14] Guys, I'm like freaking out right now
[217.14 → 219.42] And I was doing a sound check
[219.42 → 220.60] The MC was introducing me
[220.60 → 221.26] And I had a
[221.26 → 223.24] Like a remote mic on my shirt
[223.24 → 225.10] And when I was sound checking
[225.10 → 226.06] My mic wasn't that loud
[226.06 → 228.02] So while the MC was introducing me
[228.02 → 229.52] I went skirt into the mic
[229.52 → 231.60] And it is just like filled up the stadium
[231.60 → 232.56] Not the stadium
[232.56 → 233.32] I filled up the room
[233.32 → 234.48] And everyone just like looked at me
[234.48 → 235.58] And I just like froze in terror
[235.58 → 236.52] It was like the worst thing ever
[236.52 → 237.64] But anyway
[237.64 → 239.32] Skirt
[239.32 → 240.84] Did you find the errors?
[241.08 → 242.06] I don't even know what they look
[242.06 → 243.58] What do they even look like?
[243.80 → 244.86] They're in the phone
[244.86 → 246.72] In the phone?
[246.98 → 248.80] Yeah, they're definitely in there
[248.80 → 250.52] I just don't know how we labelled them
[250.52 → 251.88] I got it, don't worry
[251.88 → 253.50] You have to figure it out
[253.50 → 255.44] We're running out of time, Prime
[255.44 → 256.64] You have to find them
[256.64 → 258.08] And meet me at the stand-up
[258.08 → 258.74] Roger
[258.74 → 262.98] They're in the phone
[262.98 → 265.58] It's so simple
[265.58 → 269.62] Get all the context you need
[269.62 → 270.52] To debug your problem
[270.52 → 271.64] Because code breaks
[271.64 → 273.40] So fix it faster with Sentry
[273.40 → 279.44] Alright, I want to show Casey
[279.44 → 280.64] Excess property checks
[280.64 → 281.80] Oh no, on this screen
[281.80 → 283.20] It kind of like makes things crap
[283.20 → 283.76] But it's fine
[283.76 → 285.16] So excess property checks
[285.16 → 285.86] So check this out
[285.86 → 287.88] So this is a type
[287.88 → 289.48] So you've never seen TypeScript before
[289.48 → 290.62] I've never
[290.62 → 291.20] Okay
[291.20 → 293.72] So the function looks like JavaScript to you
[293.72 → 295.10] The only difference between like JavaScript
[295.10 → 296.70] And TypeScript in my opinion
[296.70 → 298.28] You see these little colons here
[298.28 → 299.42] And that's your type afterwards
[299.42 → 301.50] And then the type definition is at the top
[301.50 → 302.96] Hopefully that's pretty obvious, right?
[303.02 → 303.92] So you have type person
[303.92 → 305.94] It's an object-like structure
[305.94 → 306.94] And has two properties
[306.94 → 308.46] First name of type string
[308.46 → 309.34] Age of type number
[309.34 → 311.58] And then this function
[311.58 → 313.60] Obviously will take its own parameter
[313.60 → 314.58] And it's a type person
[314.58 → 317.60] So the interesting part with TypeScript is
[317.60 → 319.20] Okay, if we call it like this
[319.20 → 320.54] This looks normal, right?
[320.62 → 322.06] This doesn't error out
[322.06 → 323.86] Business as usual
[323.86 → 325.76] If you actually work in the TypeScript ecosystem
[325.76 → 327.98] If you pass in an extra property
[327.98 → 330.70] It's going to actually break with extra prop
[330.70 → 332.30] So hopefully this all makes sense
[332.30 → 334.12] Like this is actually like aligning with most
[334.12 → 336.68] Most web developers' mental model
[336.68 → 338.44] But what's interesting here is
[338.44 → 340.10] If you extract this object
[340.10 → 341.34] The type error goes away
[341.34 → 342.08] Right?
[342.18 → 343.32] Which isn't the biggest deal
[343.32 → 344.52] So the difference here is like
[344.52 → 345.42] TypeScript is structural
[345.42 → 348.06] So as long as it satisfies the contract
[348.06 → 349.12] Of first name and age
[349.12 → 350.12] TypeScript's like
[350.12 → 351.26] Cool, I don't care
[351.26 → 352.60] We have those two properties
[352.60 → 353.96] I don't care about the rest
[353.96 → 354.46] Right?
[355.08 → 356.40] Which may not be what you want
[356.40 → 358.12] So if you actually want that behaviour
[358.12 → 359.74] Of like getting that error
[359.74 → 360.88] That we saw in the previous slide
[360.88 → 362.76] You have to explicitly type it
[362.76 → 363.66] Right?
[364.24 → 365.48] So this kind of makes sense
[365.48 → 366.38] Has an extra prop
[366.38 → 366.80] It breaks
[366.80 → 368.18] But if you're just like
[368.18 → 369.92] Really want to add this extra property
[369.92 → 372.02] You can literally just
[372.02 → 373.76] Spread an object into this
[373.76 → 374.84] And then the type error goes away
[374.84 → 376.94] So that's literally
[376.94 → 378.88] The first WTF of TypeScript
[378.88 → 379.54] Right?
[379.68 → 381.14] So this actually blew people's minds
[381.14 → 381.44] They're like
[381.44 → 381.74] What?
[381.80 → 382.54] I didn't know you can do this
[382.54 → 384.02] Honestly, like pragmatically
[384.02 → 385.50] You probably would never do this
[385.50 → 387.08] Most people won't even
[387.08 → 387.68] Except people do
[387.68 → 389.34] Yeah, exactly
[389.34 → 389.92] Exactly
[389.92 → 391.44] So why does that work?
[391.44 → 392.32] You have somebody told to hold it around
[392.32 → 393.58] Because I thought spreading
[393.58 → 394.80] Like TypeScript was able to
[394.80 → 395.78] Trace the types through
[395.78 → 397.24] And the properties that you get
[397.24 → 398.44] Why does that work?
[398.46 → 399.84] So I don't know the technical reasons
[399.84 → 400.98] But I just don't think
[400.98 → 402.66] TypeScript can actually follow it
[402.66 → 403.50] Right?
[403.72 → 404.76] I just think it just sees
[404.76 → 405.72] The first two properties
[405.72 → 407.18] And then it just can't
[407.18 → 408.50] I think it's like the same scenario
[408.50 → 409.84] Where you extract it like this
[409.84 → 411.72] It doesn't know what's in there
[411.72 → 412.26] And it kind of just
[412.26 → 413.52] Treats everything in this object
[413.52 → 414.84] As an excess property
[414.84 → 416.26] At this point
[416.26 → 417.14] So I don't know
[417.14 → 417.70] I don't know like
[417.70 → 418.66] The actual technical reasons
[418.66 → 419.62] If you go into the compiler
[419.62 → 421.08] I'm sure some like
[421.08 → 422.18] Team member can tell you why
[422.18 → 423.50] I just know if you do this
[423.50 → 424.36] It makes it go away
[424.36 → 425.20] And I've seen this actually
[425.20 → 425.90] Like in some way
[425.90 → 427.04] So why wouldn't you just use
[427.04 → 428.20] A Tagore at this point?
[429.80 → 430.78] Or an as person
[430.78 → 431.84] Well Tagore just opens up
[431.84 → 432.48] A whole other
[432.48 → 434.56] Opens up a whole other thing
[434.56 → 435.46] Of like candle worms
[435.46 → 436.38] Usually what people do
[436.38 → 437.60] Is they'll opt for this
[437.60 → 438.36] They just want to
[438.36 → 439.32] Explicitly talk about it
[439.32 → 439.64] Okay
[439.64 → 441.46] Because at the end of the day
[441.46 → 442.12] As long as you have
[442.12 → 442.88] First name and age
[442.88 → 443.74] It doesn't actually matter
[443.74 → 444.64] Like your code is only
[444.64 → 445.58] Typically going to look
[445.58 → 446.46] For those two properties
[446.46 → 447.50] Unless you have like
[447.50 → 448.12] Some validator
[448.12 → 448.80] That's actually like
[448.80 → 449.56] Enumerating
[449.56 → 451.16] The properties of the object
[451.16 → 452.38] It could actually break stuff
[452.38 → 453.64] But more times than not
[453.64 → 454.72] This would usually be fine
[454.72 → 455.52] So this
[455.52 → 456.76] Trash I got a question
[456.76 → 457.86] Yeah yeah yeah
[457.86 → 459.58] If this
[459.58 → 460.52] If this behaviour
[460.52 → 461.38] Didn't exist
[461.38 → 462.04] Wouldn't like
[462.04 → 463.58] Everybody's strategy
[463.58 → 464.68] For passing around
[464.68 → 466.02] Properties in React
[466.02 → 466.66] Just like
[466.66 → 468.16] Completely get demolished
[468.16 → 469.56] Right?
[469.66 → 470.00] Isn't this what
[470.00 → 470.72] Everybody does
[470.72 → 471.34] Is like you've got
[471.34 → 472.10] Some big object
[472.10 → 473.02] With a bunch of context
[473.02 → 474.30] Everybody just spreads it
[474.30 → 475.10] All the way down
[475.10 → 475.60] Right?
[475.68 → 476.00] Do they not?
[476.00 → 476.46] Yeah that's like
[476.46 → 477.48] A whole other conversation
[477.48 → 478.18] Of just like
[478.18 → 479.24] Dumping bags
[479.24 → 480.28] Into like
[480.28 → 480.90] Other functions
[480.90 → 481.60] And you have no idea
[481.60 → 482.14] What's in there
[482.14 → 483.30] This is a problem
[483.30 → 484.12] I don't know
[484.12 → 485.70] Like the exact React types
[485.70 → 486.88] But I know the practice
[486.88 → 487.44] Of just like
[487.44 → 488.96] Taking a bag of anything
[488.96 → 490.00] And just passing it down
[490.00 → 490.70] Is a thing
[490.70 → 491.26] Yeah you're just like
[491.26 → 492.28] We just pass
[492.28 → 492.90] We just keep
[492.90 → 493.54] All the way down
[493.54 → 494.64] Somebody uses it
[494.64 → 495.50] It's actually
[495.50 → 496.44] A real big problem
[496.44 → 497.32] And I've experienced
[497.32 → 498.10] This pain firsthand
[498.10 → 499.12] And I actually hate it
[499.12 → 500.00] I don't think it actually
[500.00 → 500.60] At the type level
[500.60 → 501.18] Catches it
[501.18 → 502.26] Because I've been in code bases
[502.26 → 502.86] Where we're just like
[502.86 → 503.38] I don't even know
[503.38 → 503.80] What's in here
[503.80 → 505.00] But I'm just going to spread it
[505.00 → 506.26] I'm just going to spread it down
[506.26 → 508.46] And drill it to the core of the earth
[508.46 → 509.34] Because I have no idea
[509.34 → 509.86] So yeah
[509.86 → 510.18] I don't know
[510.18 → 510.72] At the type level
[510.72 → 511.32] I'm not too familiar
[511.32 → 512.32] With like the React types
[512.32 → 513.20] In depth
[513.20 → 514.22] But potentially
[514.22 → 514.64] Right?
[514.70 → 515.60] Casey just so you know
[515.60 → 517.60] When someone spreads
[517.60 → 519.36] It's actually taking
[519.36 → 520.16] That object
[520.16 → 520.88] And copying it
[520.88 → 521.82] Key and value in
[521.82 → 523.64] Not doing a deep copy
[523.64 → 524.54] Just a shallow copy
[524.54 → 525.18] Of key and value
[525.18 → 526.32] Which means that
[526.32 → 527.90] Every time React renders
[527.90 → 528.92] Every single component
[528.92 → 530.94] Recopies the same object
[530.94 → 532.36] Through all the way down
[532.36 → 532.76] So if you have
[532.76 → 533.48] Thousands of components
[533.48 → 534.12] You create thousands
[534.12 → 535.40] Of copies of objects
[535.40 → 536.18] Every single time
[536.18 → 537.96] Just so you understand
[537.96 → 538.60] Because I feel like
[538.60 → 539.20] This would be kind of
[539.20 → 539.76] Like a fun
[539.76 → 541.48] Like illuminating fact
[541.48 → 542.02] For you
[542.02 → 544.08] Actually Trashed
[544.08 → 545.22] I mean this is going to be
[545.22 → 545.78] One of those things
[545.78 → 546.70] Because since we're
[546.70 → 547.62] All actually interested
[547.62 → 548.02] In this
[548.02 → 548.98] Like this is going to be
[548.98 → 550.06] Like one slide
[550.06 → 550.80] Per podcast
[550.80 → 551.94] That was perfectly fine
[551.94 → 553.28] And six weeks from now
[553.28 → 554.00] We'll have gotten
[554.00 → 554.72] Through the presentation
[554.72 → 556.42] Sorry
[556.42 → 557.70] Just for my benefit
[557.70 → 558.14] So
[558.14 → 559.98] Can you go back
[559.98 → 560.64] To the thing
[560.64 → 561.50] Where you called the function
[561.50 → 562.36] And you got the error
[562.36 → 563.28] In the first place
[563.28 → 565.36] Sorry
[565.36 → 566.48] I'm not supposed to
[566.48 → 566.90] Go backwards
[566.90 → 567.52] In this one
[567.52 → 568.08] Oh I'm sorry
[568.08 → 568.34] Okay
[568.34 → 568.84] Well I just
[568.84 → 569.26] I was curious
[569.26 → 570.08] So
[570.08 → 571.02] Never go back
[571.02 → 572.74] So I'm just wondering
[572.74 → 574.12] Compiler wise
[574.12 → 575.86] Why does it see a difference
[575.86 → 576.88] Between these two things
[576.88 → 577.86] Because to me
[577.86 → 578.64] When I look at that
[578.64 → 578.98] I'm like
[578.98 → 579.28] Okay
[579.28 → 580.76] What that would normally do
[580.76 → 581.42] Is first it would
[581.42 → 582.74] Evaluate to an object
[582.74 → 583.94] That object should be
[583.94 → 585.22] The same as the person
[585.22 → 586.06] Object you were creating
[586.06 → 586.48] Before
[586.48 → 587.30] Because it has exactly
[587.30 → 588.04] The same members
[588.04 → 589.56] In exactly the same order
[589.56 → 591.52] Written exactly the same way
[591.52 → 592.24] So
[592.24 → 593.68] There's just
[593.68 → 595.56] There's a special case
[595.56 → 596.84] In TypeScript
[596.84 → 598.02] For if you're constructing
[598.02 → 598.78] An object
[598.78 → 600.34] Only inside
[600.34 → 602.08] The call to a function
[602.08 → 603.42] And in that case
[603.42 → 604.06] It will check
[604.06 → 604.98] Yeah
[604.98 → 605.72] So the compiler
[605.72 → 606.12] Will treat
[606.12 → 607.06] Inline
[607.06 → 608.28] Objects
[608.28 → 608.94] This way
[608.94 → 610.12] But outside
[610.12 → 610.86] It won't do it
[610.86 → 611.76] And so
[611.76 → 612.22] I don't know
[612.22 → 612.86] Like the exact
[612.86 → 613.72] Like specifications
[613.72 → 614.24] On why
[614.24 → 615.02] But this is like
[615.02 → 615.46] The behaviour
[615.46 → 615.86] That everyone
[615.86 → 616.42] Has kind of been
[616.42 → 617.22] Like accustomed to
[617.22 → 618.70] So that kind of suggests
[618.70 → 620.00] This is very intentional
[620.00 → 620.40] Right
[620.40 → 621.28] Because that means
[621.28 → 622.00] They probably
[622.00 → 623.00] Special case this
[623.00 → 623.40] And said
[623.40 → 623.84] Oh
[623.84 → 624.88] Like if this is
[624.88 → 625.80] If this object
[625.80 → 626.52] Has a property
[626.52 → 627.50] That isn't used
[627.50 → 628.68] Because the only place
[628.68 → 629.26] That it actually
[629.26 → 629.80] Would go
[629.80 → 630.36] Is some place
[630.36 → 631.04] Where it's not used
[631.04 → 631.76] We'll give you
[631.76 → 632.62] An error about that
[632.62 → 633.86] But if you have
[633.86 → 634.74] A regular object
[634.74 → 635.74] And you could pass it
[635.74 → 636.20] To a function
[636.20 → 636.88] That would work
[636.88 → 637.38] We're going to make
[637.38 → 637.82] That work
[637.82 → 638.12] So that
[638.12 → 639.02] It kind of feels
[639.02 → 639.66] Like that must be
[639.66 → 640.26] Intentional
[640.26 → 640.68] It's called
[640.68 → 641.34] Duck typing
[641.34 → 641.64] Right
[641.64 → 642.52] They have a term
[642.52 → 642.84] For that
[642.84 → 643.00] Right
[643.00 → 643.40] Exactly
[643.40 → 643.92] If you think about
[643.92 → 644.20] How just
[644.20 → 645.08] JavaScript works
[645.08 → 645.76] It doesn't care
[645.76 → 646.26] About any of this
[646.26 → 646.94] You can pass anything
[646.94 → 647.24] Right
[647.24 → 648.20] Like you said
[648.20 → 648.84] With duck typing
[648.84 → 650.42] I mean
[650.42 → 651.64] Like you said
[651.64 → 652.26] With duck typing
[652.26 → 652.90] If it just has
[652.90 → 653.42] These properties
[653.42 → 654.06] It must be
[654.06 → 654.84] It must be
[654.84 → 655.04] A duck
[655.04 → 656.56] And this is not
[656.56 → 657.36] Necessarily a bad thing
[657.36 → 657.62] TJ
[657.62 → 658.52] Like duck typing
[658.52 → 659.58] Is a feature
[659.58 → 660.00] Right
[660.00 → 660.74] It's a thing
[660.74 → 661.48] And so
[661.48 → 662.06] You know
[662.06 → 662.58] When you're making
[662.58 → 663.02] A language
[663.02 → 663.60] Like they were
[663.60 → 664.10] With TypeScript
[664.10 → 665.06] They have to decide
[665.06 → 666.18] What's the default
[666.18 → 666.64] Behaviour
[666.64 → 667.30] And maybe
[667.30 → 668.14] Like their thing
[668.14 → 668.48] Was like
[668.48 → 669.00] Okay we're going
[669.00 → 669.30] To decide
[669.30 → 669.82] The default
[669.82 → 670.20] Behaviour
[670.20 → 671.06] Is duck typing
[671.06 → 672.56] And if we
[672.56 → 673.32] Detect somewhere
[673.32 → 674.16] Where it's clear
[674.16 → 674.78] That you probably
[674.78 → 675.86] Didn't actually
[675.86 → 676.48] Want that
[676.48 → 677.12] Then we'll err
[677.12 → 677.82] Like in this case
[677.82 → 679.10] Because there's no way
[679.10 → 680.52] Extra prop can be used here
[680.52 → 681.90] It's only going
[681.90 → 682.68] Towards a function
[682.68 → 683.16] That right
[683.16 → 684.90] So you know
[684.90 → 685.70] I'll be honest
[685.70 → 686.94] I'm
[686.94 → 689.56] I know people
[689.56 → 690.58] Probably expected me
[690.58 → 691.54] To think that
[691.54 → 692.70] That everything sucks
[692.70 → 693.48] But looking at this
[693.48 → 693.84] I'm like
[693.84 → 695.18] That sounds like
[695.18 → 696.28] An adult design this
[696.28 → 698.22] Just to be honest
[698.22 → 698.88] That seems like
[698.88 → 699.64] An adult design this
[699.64 → 699.96] To me
[699.96 → 700.74] Yeah I mean
[700.74 → 701.12] Like just
[701.12 → 702.12] Imagine just trying
[702.12 → 702.96] To type a dynamic
[702.96 → 703.80] Language like
[703.80 → 704.32] JavaScript
[704.32 → 705.12] Like it's never
[705.12 → 705.84] Going to be perfect
[705.84 → 706.20] Right
[706.20 → 706.80] So you can always
[706.80 → 707.44] Get as close
[707.44 → 708.04] As you want
[708.04 → 708.76] And then you
[708.76 → 709.08] Kind of make
[709.08 → 709.52] These arbitrary
[709.52 → 710.56] Decisions on
[710.56 → 711.00] Like how you
[711.00 → 711.42] Want like
[711.42 → 712.22] This experience
[712.22 → 712.60] To be
[712.60 → 713.42] So Casey's
[713.42 → 714.20] Thumbs up so far
[714.20 → 714.96] Sorry guys
[714.96 → 715.46] I'm up
[715.46 → 716.76] I'm thumbs up
[716.76 → 717.84] So far
[717.84 → 718.44] Can I ask
[718.44 → 718.66] Casey
[718.66 → 719.14] Do you think
[719.14 → 719.46] It's
[719.46 → 719.92] Is it
[719.92 → 720.74] Do you like
[720.74 → 721.06] That
[721.06 → 722.14] Because I agree
[722.14 → 723.04] I like this one
[723.04 → 723.92] Where it says
[723.92 → 724.68] Yo you passed
[724.68 → 725.26] An extra prop
[725.26 → 725.86] You shouldn't do
[725.86 → 726.12] This
[726.12 → 727.24] But do you like
[727.24 → 728.00] Being able
[728.00 → 729.78] To do the next
[729.78 → 730.74] Phase where it's
[730.74 → 731.54] Like oh I just
[731.54 → 732.48] Put I just have
[732.48 → 733.18] An object and I
[733.18 → 733.82] Pass it in as
[733.82 → 734.58] Extra properties
[734.58 → 735.04] Because that
[735.04 → 735.50] Like
[735.50 → 735.80] Yes
[735.80 → 736.74] Okay
[736.74 → 737.26] Alright cool
[737.26 → 737.84] Just making sure
[737.84 → 738.60] Like I said
[738.60 → 739.14] It's so
[739.14 → 739.66] Duck
[739.66 → 740.44] I actually like
[740.44 → 741.02] Duck typing
[741.02 → 742.62] If I ask for it
[742.62 → 743.26] Right so like
[743.26 → 744.18] I would prefer
[744.18 → 745.10] That more languages
[745.10 → 745.70] Have the ability
[745.70 → 746.04] To do duck
[746.04 → 746.74] Like for example
[746.74 → 747.90] You can think
[747.90 → 749.68] Of C++ templates
[749.68 → 750.88] As supporting
[750.88 → 751.58] Duck typing
[751.58 → 752.42] Because if you
[752.42 → 753.46] Pass something
[753.46 → 754.58] Pass I mean
[754.58 → 754.92] If you
[754.92 → 755.86] If you instantiate
[755.86 → 756.26] A template
[756.26 → 757.12] And you have
[757.12 → 757.54] A parameter
[757.54 → 758.72] That has
[758.72 → 759.34] The necessary
[759.34 → 760.44] Things but also
[760.44 → 760.86] A bunch of
[760.86 → 761.54] Other things
[761.54 → 763.02] It will work
[763.02 → 763.70] Right because
[763.70 → 764.32] It's what it's
[764.32 → 764.84] Doing is it's
[764.84 → 765.26] Going to create
[765.26 → 765.88] Code that works
[765.88 → 766.24] For anything
[766.24 → 766.98] That supports
[766.98 → 767.80] That feature
[767.80 → 768.38] At a minimum
[768.38 → 769.06] It's not going
[769.06 → 769.54] To say you
[769.54 → 770.04] Can't have
[770.04 → 770.62] These other things
[770.62 → 771.52] And to me
[771.52 → 772.08] That's actually
[772.08 → 772.68] Better because
[772.68 → 773.26] It gets me
[773.26 → 774.28] More code leverage
[774.28 → 774.84] It means I can
[774.84 → 775.94] Use more functions
[775.94 → 777.28] On more types
[777.28 → 778.52] As opposed to
[778.52 → 779.42] The opposite
[779.42 → 780.10] Which is when
[780.10 → 780.70] You try to do
[780.70 → 781.70] The object-oriented
[781.70 → 782.48] Like very
[782.48 → 783.34] Procrustean
[783.34 → 784.16] Like type
[784.16 → 784.78] Hierarchy thing
[784.78 → 785.10] And make it
[785.10 → 785.68] It's like we
[785.68 → 786.22] Only
[786.22 → 787.30] Everything has
[787.30 → 787.72] To be the
[787.72 → 788.40] Minimum set
[788.40 → 788.94] And functions
[788.94 → 790.00] Can only work
[790.00 → 790.78] On exactly
[790.78 → 791.42] The things we
[791.42 → 791.70] Said
[791.70 → 791.94] Right
[791.94 → 792.78] That really
[792.78 → 793.66] Handcuffs you
[793.66 → 794.24] Right so
[794.24 → 794.78] To me
[794.78 → 795.32] Duck typing
[795.32 → 795.78] Is great
[795.78 → 796.76] Would I have
[796.76 → 797.32] Wanted it in
[797.32 → 798.12] An ideal world
[798.12 → 798.80] Perhaps to be
[798.80 → 799.48] More explicit
[799.48 → 800.24] Like I say
[800.24 → 800.70] If I want
[800.70 → 801.06] Duck type
[801.06 → 801.32] Or not
[801.32 → 802.14] Maybe
[802.14 → 803.16] But again
[803.16 → 804.40] In the context
[804.40 → 805.50] Of a JavaScript
[805.50 → 806.36] Front end
[806.36 → 806.94] Which is what
[806.94 → 807.36] Type script
[807.36 → 807.76] Is
[807.76 → 808.76] I think this
[808.76 → 809.62] Is a reasonable
[809.62 → 810.56] Choice for a
[810.56 → 811.02] Language designer
[811.02 → 811.62] To make
[811.62 → 812.86] Because most
[812.86 → 813.74] Of the existing
[813.74 → 814.86] JavaScript ecosystem
[814.86 → 815.56] Is being
[815.56 → 816.08] Duck typed
[816.08 → 816.78] By default
[816.78 → 817.42] So if you
[817.42 → 818.00] Make it really
[818.00 → 819.12] Onerous and
[819.12 → 820.14] Annoying for the
[820.14 → 820.96] Person writing
[820.96 → 821.40] The code
[821.40 → 822.12] To constantly
[822.12 → 822.48] Be saying
[822.48 → 823.16] Duck type
[823.16 → 823.58] Duck type
[823.58 → 824.02] Duck type
[824.02 → 824.44] Duck type
[824.44 → 824.88] Duck type
[824.88 → 825.62] That's going to be
[825.62 → 825.86] Annoying
[825.86 → 826.44] So again
[826.44 → 827.44] Seems like
[827.44 → 827.98] Adult design
[827.98 → 828.36] To me
[828.36 → 829.44] So I'm
[829.44 → 829.88] Thumbs up
[829.88 → 830.40] On everything
[830.40 → 830.76] You showed
[830.76 → 831.08] So far
[831.08 → 831.42] Can I ask
[831.42 → 831.74] A quick
[831.74 → 832.06] Question
[832.06 → 832.48] This is just
[832.48 → 832.76] A general
[832.76 → 833.08] Question
[833.08 → 834.00] Is there
[834.00 → 834.44] A specific
[834.44 → 834.70] DIF
[834.70 → 835.46] In my head
[835.46 → 836.16] The duck
[836.16 → 836.46] Typing
[836.46 → 836.86] Versus
[836.86 → 837.72] Structural
[837.72 → 838.06] Typing
[838.06 → 838.46] Is structural
[838.46 → 838.78] Typing
[838.78 → 839.16] About the
[839.16 → 839.70] Properties
[839.70 → 841.08] And the
[841.08 → 841.68] Available
[841.68 → 842.16] Functions
[842.16 → 842.46] Whereas
[842.46 → 843.44] Duck typing
[843.44 → 844.04] Is only about
[844.04 → 844.62] The functions
[844.62 → 845.96] Is there
[845.96 → 846.28] Like a
[846.28 → 846.54] Difference
[846.54 → 846.90] I'm not
[846.90 → 847.46] Actually
[847.46 → 847.98] Sure
[847.98 → 848.32] If there's
[848.32 → 848.54] Actually
[848.54 → 848.92] A difference
[848.92 → 849.28] Or is
[849.28 → 849.74] Duck typing
[849.74 → 850.18] Like the
[850.18 → 851.78] Local
[851.78 → 852.18] Or the
[852.18 → 852.56] Colloquial
[852.56 → 852.90] Version
[852.90 → 853.36] Of
[853.36 → 853.90] Structural
[853.90 → 854.26] Typing
[854.26 → 855.56] I don't
[855.86 → 856.10] I know
[856.10 → 856.46] The term
[856.46 → 856.96] Structural
[856.96 → 857.36] Typing
[857.36 → 857.86] But duck
[857.86 → 858.24] Typing
[858.24 → 858.70] Literally
[858.70 → 859.28] Just comes
[859.28 → 859.58] From the
[859.58 → 859.90] Phrase
[859.90 → 860.48] If it
[860.48 → 861.04] Looks like
[861.04 → 861.40] A duck
[861.40 → 861.82] And quacks
[861.82 → 862.30] Like a duck
[862.30 → 862.62] That it's
[862.62 → 862.92] A duck
[862.92 → 863.58] So literally
[863.58 → 863.98] It's just
[863.98 → 864.36] Like if
[864.36 → 864.78] This thing
[864.78 → 865.22] Can do
[865.22 → 865.88] What I
[865.88 → 866.18] Need
[866.18 → 866.98] Whether that's
[866.98 → 867.22] Member
[867.22 → 867.72] Functions
[867.72 → 868.40] Or having
[868.40 → 868.84] Particular
[868.84 → 869.48] Data items
[869.48 → 869.90] Or whatever
[869.90 → 870.34] It is
[870.34 → 871.48] Then I
[871.48 → 872.10] Consider it
[872.10 → 872.64] To be
[872.64 → 873.30] The type
[873.30 → 873.78] I needed
[873.78 → 874.34] For all
[874.34 → 874.62] Intents
[874.62 → 875.08] And purposes
[875.08 → 875.64] And I'm
[875.64 → 876.10] Not going
[876.10 → 876.56] To inquire
[876.56 → 877.00] Further
[877.00 → 877.82] To see
[877.82 → 878.12] Whether
[878.12 → 879.22] It actually
[879.22 → 879.86] Is
[879.86 → 880.98] A exact
[880.98 → 881.34] Copy
[881.34 → 881.60] Of that
[881.60 → 881.80] Type
[881.80 → 882.04] I'm
[882.04 → 882.34] Just going
[882.34 → 882.66] To say
[882.66 → 883.22] Does it
[883.22 → 883.88] Have similar
[883.88 → 884.32] Things to
[884.32 → 884.74] That type
[884.74 → 885.08] That will
[885.08 → 885.40] Work
[885.40 → 885.76] Right
[885.76 → 887.14] I don't
[887.14 → 887.24] Know
[887.24 → 887.60] What is
[887.60 → 887.98] Structural
[887.98 → 888.16] Typing
[888.16 → 888.36] So I
[888.36 → 888.44] Don't
[888.44 → 888.78] Know that
[888.78 → 889.08] Term
[889.08 → 889.28] So
[889.28 → 889.64] Structural
[889.64 → 889.88] Typing
[889.88 → 890.18] Just think
[890.18 → 890.36] About
[890.36 → 890.82] Legos
[890.82 → 891.08] Right
[891.08 → 891.42] So if
[891.42 → 891.62] They have
[891.62 → 891.96] The same
[891.96 → 892.34] Shape
[892.34 → 893.54] They're probably
[893.54 → 893.98] The same
[893.98 → 894.34] Thing
[894.34 → 894.58] Right
[894.58 → 894.86] So like
[894.86 → 895.06] In this
[895.06 → 895.38] Case
[895.38 → 895.76] They're the
[895.76 → 896.08] Same
[896.08 → 896.62] Basically
[896.62 → 896.98] Like
[896.98 → 897.48] Structural
[897.48 → 898.16] Subtyping
[898.16 → 898.64] I think
[898.64 → 899.14] Is the
[899.14 → 899.62] Functional
[899.62 → 900.26] Programmer
[900.26 → 900.56] Way
[900.56 → 901.00] To say
[901.00 → 901.34] Duck
[901.34 → 901.70] That's
[901.70 → 902.82] Where I
[902.82 → 903.04] Was having
[903.04 → 903.20] This
[903.20 → 903.80] Impedance
[903.80 → 904.20] Mismatch
[904.20 → 904.56] I knew
[904.56 → 905.22] In my
[905.22 → 905.42] Head
[905.42 → 905.52] They're
[905.52 → 905.80] The same
[905.80 → 905.98] Thing
[905.98 → 906.14] But I'm
[906.14 → 906.24] Like
[906.24 → 906.72] What's
[906.72 → 907.08] The difference
[907.08 → 907.50] There has
[907.50 → 907.64] To be
[907.64 → 907.94] A difference
[907.94 → 908.34] But okay
[908.34 → 909.30] Well if it
[909.30 → 909.66] Comes from
[909.66 → 910.08] Functional
[910.08 → 910.72] Programming
[910.72 → 911.52] They're definitely
[911.52 → 912.14] Not the same
[912.14 → 912.46] Thing
[912.46 → 913.32] And somebody
[913.32 → 913.72] Will be
[913.72 → 914.08] In the
[914.08 → 914.42] Comments
[914.42 → 914.66] Going
[914.66 → 915.46] I can't
[915.46 → 915.70] Believe
[915.70 → 916.22] They called
[916.22 → 916.72] Structural
[916.72 → 917.08] Typing
[917.08 → 917.34] Duck
[917.34 → 917.80] Typing
[917.80 → 918.42] And then
[918.42 → 919.42] 20 paragraphs
[919.42 → 919.82] Later
[919.82 → 920.28] There will be
[920.28 → 920.98] This minor
[920.98 → 921.68] Tiny little
[921.68 → 922.20] Difference
[922.20 → 923.04] That no one
[923.04 → 923.66] Cares about
[923.66 → 924.98] But yes
[924.98 → 925.50] They probably
[925.50 → 926.06] Are the same
[926.06 → 926.34] Then
[926.34 → 927.28] So we'll
[927.28 → 927.58] Get them
[927.58 → 927.92] We'll get
[927.92 → 928.22] You guys
[928.22 → 928.68] In the next
[928.68 → 928.98] Episode
[928.98 → 929.44] We'll have
[929.44 → 929.90] The answer
[929.90 → 930.40] Solved
[930.40 → 930.92] I'm not
[930.92 → 931.34] Going to look
[931.34 → 931.56] It up
[935.52 → 935.76] All right
[935.76 → 936.40] So 20 minutes
[936.40 → 936.96] Later we got
[936.96 → 937.64] Past the first
[937.64 → 938.04] Yeah
[938.04 → 939.00] First section
[939.00 → 940.06] So we'll see
[940.06 → 940.82] How far we get
[940.82 → 941.08] To this
[941.08 → 941.58] This is actually
[941.58 → 941.86] Okay
[941.86 → 942.96] Let's keep going
[942.96 → 943.28] Okay
[943.28 → 944.08] Ends
[944.08 → 945.10] I'm assuming
[945.10 → 945.92] Ends
[945.92 → 946.26] Okay
[946.26 → 946.76] This is an
[946.76 → 947.42] Interesting example
[947.42 → 948.34] I wouldn't say
[948.34 → 948.66] It's the most
[948.66 → 949.40] Interesting one
[949.40 → 950.50] But I think
[950.50 → 951.22] It's pretty
[951.22 → 951.78] Pretty cool
[951.78 → 953.02] So let's look
[953.02 → 953.68] At ends
[953.68 → 954.26] Colours
[954.26 → 954.90] They just have
[954.90 → 955.46] String values
[955.46 → 955.82] So green
[955.82 → 956.28] Orange red
[956.28 → 956.90] Nothing
[956.90 → 957.48] Particularly
[957.48 → 958.26] Interesting here
[958.26 → 959.22] But we want
[959.22 → 959.94] To use this
[959.94 → 960.76] Enum
[960.76 → 961.58] In a function
[961.58 → 962.16] So we'll just
[962.16 → 962.46] Have some
[962.46 → 962.82] Placeholder
[962.82 → 963.24] Function
[963.24 → 963.70] Is the best
[963.70 → 963.98] Colour
[963.98 → 964.96] Its parameter
[964.96 → 965.50] Is going to be
[965.50 → 966.20] Of type colours
[966.20 → 966.98] That makes sense
[966.98 → 967.28] Right
[967.28 → 969.08] Oh sorry
[969.08 → 969.80] I bet you're asking
[969.80 → 971.78] Green is the best
[971.78 → 971.90] I was like
[971.90 → 972.56] How did you know
[972.56 → 974.70] So if we call
[974.70 → 975.08] Like this
[975.08 → 975.66] Colours. Green
[975.66 → 976.26] This makes sense
[976.26 → 976.38] Right
[976.38 → 976.90] It shouldn't look
[976.90 → 978.60] Surprising to anybody
[978.60 → 979.58] That's used
[979.58 → 980.12] TypeScript
[980.12 → 980.94] Or just coding
[980.94 → 981.28] In general
[981.28 → 981.82] I feel like
[981.82 → 983.56] But if you call
[983.56 → 984.28] It as its actual
[984.28 → 984.74] Value
[984.74 → 986.00] It's going to
[986.00 → 986.32] Break
[986.32 → 987.00] So if you see
[987.00 → 987.68] Here we're calling
[987.68 → 987.96] It with a
[987.96 → 988.32] String value
[988.32 → 988.72] Green
[988.72 → 989.64] But if I
[989.64 → 990.28] Console log
[990.28 → 991.06] Colours. Green
[991.06 → 992.66] It fails
[992.66 → 993.16] Even though the
[993.16 → 993.88] Values match
[993.88 → 994.24] Right
[994.24 → 994.94] And this isn't
[994.94 → 995.54] The biggest deal
[995.54 → 996.36] The biggest
[996.36 → 996.96] Annoyance
[996.96 → 997.32] I think
[997.32 → 998.18] I experience
[998.18 → 998.64] Personally
[998.64 → 999.26] And other
[999.26 → 999.74] Developers
[999.74 → 1000.60] Is when I
[1000.60 → 1000.88] Call this
[1000.88 → 1001.24] Function
[1001.24 → 1001.96] I now have
[1001.96 → 1002.54] To import
[1002.54 → 1003.16] This enum
[1003.16 → 1004.68] Just so I
[1004.68 → 1005.22] Can call it
[1005.22 → 1005.80] Even though
[1005.80 → 1006.20] If I know
[1006.20 → 1006.56] The values
[1006.56 → 1006.86] I can't
[1006.86 → 1007.16] Just call it
[1007.16 → 1007.42] With green
[1007.42 → 1007.86] Orange red
[1007.86 → 1008.58] So with
[1008.58 → 1009.12] Auto importing
[1009.12 → 1009.84] Not the biggest
[1009.84 → 1010.20] Deal
[1010.20 → 1010.92] But where
[1010.92 → 1011.20] This is
[1011.20 → 1011.62] Interesting
[1011.62 → 1012.38] Is going to
[1012.38 → 1012.68] Be in my
[1012.68 → 1013.26] Next example
[1013.26 → 1013.64] So right
[1013.64 → 1013.84] Now
[1013.84 → 1014.42] Any questions
[1014.42 → 1014.86] Like this
[1014.86 → 1015.10] All
[1015.10 → 1015.80] Does this
[1015.80 → 1016.74] All make
[1016.74 → 1017.00] Sense
[1017.00 → 1017.56] I can't
[1017.56 → 1017.66] Say
[1017.66 → 1017.98] Good so
[1017.98 → 1018.26] Far
[1018.26 → 1020.02] Trash
[1020.02 → 1020.60] Alright
[1020.60 → 1021.34] So let's
[1021.34 → 1021.96] Talk about
[1021.96 → 1022.46] Ends
[1022.46 → 1023.24] With number
[1023.24 → 1023.84] Values
[1023.84 → 1024.58] So we're
[1024.58 → 1024.68] Going to
[1024.68 → 1025.04] Have like
[1025.04 → 1025.30] Pending
[1025.30 → 1025.68] Decline
[1025.68 → 1026.16] Approved
[1026.16 → 1027.02] 012
[1027.02 → 1027.78] We're going
[1027.78 → 1028.02] To call
[1028.02 → 1028.32] It again
[1028.32 → 1028.60] Just like
[1028.60 → 1028.82] We did
[1028.82 → 1028.98] In the
[1028.98 → 1029.22] Previous
[1029.22 → 1029.78] Example
[1029.78 → 1030.76] Stats
[1030.76 → 1031.30] Decline
[1031.30 → 1031.90] You know
[1031.90 → 1032.70] Makes sense
[1032.70 → 1033.20] Makes perfect
[1033.20 → 1033.50] Sense
[1033.50 → 1033.84] But if
[1033.84 → 1034.12] I call
[1034.12 → 1034.32] It with
[1034.32 → 1034.46] This
[1034.46 → 1035.24] Corresponding
[1035.24 → 1035.68] Value
[1035.68 → 1036.76] We don't
[1036.76 → 1037.12] Get that
[1037.12 → 1037.62] Type error
[1037.62 → 1038.82] So it
[1038.82 → 1039.16] Looks like
[1039.16 → 1039.48] I love
[1039.48 → 1039.74] C
[1039.74 → 1042.36] So yeah
[1042.36 → 1043.32] It works
[1043.32 → 1044.44] Here but it
[1044.44 → 1044.82] Doesn't work
[1044.82 → 1045.02] In the
[1045.02 → 1045.30] String
[1045.30 → 1045.66] In the
[1045.66 → 1046.28] String case
[1046.28 → 1047.00] What happens
[1047.00 → 1047.32] If you
[1047.32 → 1047.76] Passed
[1047.76 → 1048.06] Three
[1048.06 → 1050.12] I don't
[1050.12 → 1050.44] Actually
[1050.44 → 1050.82] I'll
[1050.82 → 1051.14] Type it
[1051.14 → 1051.74] I'll
[1051.74 → 1052.06] Type it
[1052.06 → 1052.58] I'm
[1052.58 → 1052.90] Pretty
[1052.90 → 1053.38] I'm
[1053.38 → 1053.58] Pretty
[1053.58 → 1053.90] Sure
[1053.90 → 1054.16] It's
[1054.16 → 1054.40] Going to
[1054.40 → 1054.64] Work
[1054.64 → 1054.84] Because
[1054.84 → 1054.98] There's
[1054.98 → 1055.14] Going to
[1055.14 → 1055.30] Be a
[1055.30 → 1055.44] Type
[1055.44 → 1055.66] Number
[1055.66 → 1056.02] But I
[1056.02 → 1056.26] Can
[1056.26 → 1057.66] Type it
[1057.66 → 1057.78] Out
[1057.78 → 1058.06] I'm
[1058.06 → 1058.20] Doing
[1058.20 → 1058.32] It
[1058.32 → 1058.48] Right
[1058.48 → 1058.74] Now
[1058.74 → 1060.08] Do
[1060.08 → 1060.32] Real
[1060.32 → 1060.62] Quick
[1060.62 → 1061.40] Oh
[1061.40 → 1061.78] Boy
[1061.78 → 1062.88] I
[1063.50 → 1064.56] Right
[1064.56 → 1064.78] Now
[1064.78 → 1065.18] It says
[1065.18 → 1065.80] Argument
[1065.80 → 1065.92] Of
[1065.92 → 1066.14] Type
[1066.14 → 1066.36] Three
[1066.36 → 1066.52] Is
[1066.52 → 1066.68] Not
[1066.68 → 1067.04] Assignable
[1067.04 → 1067.18] To
[1067.18 → 1067.60] Parameter
[1067.60 → 1067.78] Type
[1067.78 → 1068.00] Status
[1068.00 → 1068.60] It
[1068.60 → 1069.40] Doesn't
[1069.40 → 1069.60] Allow
[1069.60 → 1069.92] Three
[1069.92 → 1070.48] So it
[1070.48 → 1070.74] Does
[1070.74 → 1071.10] Actually
[1071.10 → 1072.20] Look
[1072.20 → 1072.50] For the
[1072.50 → 1072.90] Numbers
[1072.90 → 1074.64] So it's
[1074.64 → 1074.78] Like
[1074.78 → 1075.14] Half
[1075.14 → 1075.34] C
[1075.34 → 1077.90] Half
[1077.90 → 1078.08] C
[1078.08 → 1078.54] Exactly
[1078.54 → 1079.34] So this
[1079.34 → 1079.56] One's
[1079.56 → 1079.74] Like
[1079.74 → 1080.16] Interesting
[1080.16 → 1080.48] Like
[1080.48 → 1080.60] It's
[1080.60 → 1080.72] Not
[1080.72 → 1080.98] Something
[1080.98 → 1081.52] I
[1081.52 → 1081.68] Don't
[1081.68 → 1081.92] Think
[1081.92 → 1082.30] Anyone's
[1082.30 → 1082.48] Going to
[1082.48 → 1082.78] Actually
[1082.78 → 1083.34] Encounter
[1083.34 → 1084.28] Like
[1084.28 → 1084.62] Day
[1084.62 → 1084.76] To
[1084.76 → 1085.04] Day
[1085.04 → 1085.66] But
[1085.66 → 1085.74] It
[1085.74 → 1085.84] Was
[1085.84 → 1086.04] An
[1086.04 → 1086.32] Interesting
[1086.32 → 1086.66] Case
[1086.66 → 1086.86] On
[1086.86 → 1087.08] Like
[1087.08 → 1087.28] It's
[1087.28 → 1087.68] Behaviour
[1087.68 → 1088.06] So I
[1088.06 → 1088.42] Included
[1088.42 → 1088.74] It
[1088.74 → 1089.86] That
[1089.86 → 1090.14] Feels
[1090.14 → 1090.34] Like
[1090.34 → 1090.48] It
[1093.50 → 1094.06] That I
[1094.06 → 1094.26] Don't
[1094.26 → 1094.78] Remember
[1094.78 → 1095.80] Oh
[1095.80 → 1096.38] Don't
[1096.38 → 1096.72] Remember
[1096.72 → 1096.96] But
[1096.96 → 1097.12] There
[1097.12 → 1097.60] Are
[1097.60 → 1098.16] Reasons
[1098.16 → 1098.56] But
[1098.56 → 1098.86] Reasons
[1098.86 → 1099.02] That
[1099.02 → 1099.14] You
[1099.14 → 1099.32] Don't
[1099.32 → 1099.50] Ever
[1099.50 → 1099.82] Probably
[1099.82 → 1100.10] Care
[1100.10 → 1100.40] About
[1100.40 → 1101.70] But
[1101.70 → 1101.86] Now
[1101.86 → 1102.00] I'm
[1102.00 → 1102.14] Going to
[1102.14 → 1102.30] Look
[1102.30 → 1102.46] I
[1102.46 → 1102.66] Got to
[1102.66 → 1102.92] Remember
[1102.92 → 1103.30] Like
[1103.30 → 1103.48] When I
[1103.48 → 1103.56] Was
[1103.56 → 1103.72] Making
[1103.72 → 1103.90] This
[1103.90 → 1104.10] Talk
[1104.10 → 1104.18] I
[1123.50 → 1125.48] It
[1125.48 → 1125.68] Inline
[1125.68 → 1126.36] It
[1126.36 → 1126.40] It
[1126.40 → 1126.64] Looks
[1126.64 → 1126.82] Like
[1126.82 → 1126.92] A
[1126.92 → 1127.12] Heap
[1127.12 → 1127.32] Item
[1127.32 → 1127.42] But
[1127.42 → 1127.52] It
[1127.52 → 1127.80] Is
[1127.80 → 1127.92] A
[1127.92 → 1128.22] Tag
[1128.22 → 1128.56] To
[1128.56 → 1128.76] Say
[1128.76 → 1128.96] Hey
[1128.96 → 1129.10] This
[1129.10 → 1129.12] Is
[1129.12 → 1129.34] Actually
[1129.34 → 1129.44] An
[1129.44 → 1129.70] Inline
[1129.70 → 1129.98] Number
[1129.98 → 1130.58] So I
[1130.58 → 1130.74] Wonder
[1130.74 → 1130.86] If
[1130.86 → 1131.00] This
[1131.00 → 1131.26] Works
[1131.26 → 1131.46] With
[1131.46 → 1131.88] Numbers
[1131.88 → 1132.32] Above
[1132.32 → 1132.56] 2
[1132.56 → 1132.68] To
[1132.68 → 1133.56] To
[1133.56 → 1133.76] The
[1133.76 → 1134.04] 32
[1134.04 → 1134.64] Does
[1134.64 → 1134.82] That
[1134.82 → 1135.16] Break
[1135.16 → 1135.34] The
[1135.34 → 1135.48] Whole
[1135.48 → 1135.78] Reference
[1135.78 → 1136.00] Because
[1136.00 → 1136.12] Then
[1136.12 → 1136.18] It
[1136.18 → 1136.40] Becomes
[1136.40 → 1136.54] A
[1136.54 → 1136.74] Box
[1136.74 → 1137.00] Value
[1137.00 → 1137.16] It's
[1137.16 → 1137.26] No
[1137.26 → 1137.48] Longer
[1137.48 → 1137.58] A
[1137.58 → 1137.74] Small
[1137.74 → 1137.98] Number
[1137.98 → 1138.80] Potentially
[1138.80 → 1139.00] I
[1139.00 → 1139.12] Know
[1139.12 → 1139.32] There's
[1139.32 → 1139.52] A
[1139.52 → 1140.10] Limitation
[1140.10 → 1140.42] On
[1140.42 → 1141.48] What
[1141.48 → 1141.74] Numbers
[1141.74 → 1141.86] You
[1141.86 → 1141.98] Can
[1141.98 → 1142.20] Use
[1142.20 → 1142.66] As
[1142.66 → 1142.98] But
[1142.98 → 1143.32] TypeScript
[1143.32 → 1143.48] Is
[1143.48 → 1144.02] Compiled
[1144.02 → 1144.28] So
[1144.28 → 1144.44] It
[1144.44 → 1144.66] Wouldn't
[1144.66 → 1144.92] Care
[1144.92 → 1145.10] It
[1145.10 → 1145.30] Doesn't
[1145.30 → 1145.54] Matter
[1145.54 → 1145.76] What
[1145.76 → 1146.02] The
[1146.02 → 1147.14] Runtime
[1147.14 → 1147.38] Engine
[1147.38 → 1147.74] Uses
[1147.74 → 1148.02] Right
[1148.02 → 1150.06] I
[1150.06 → 1150.18] Think
[1150.18 → 1150.38] There's
[1150.38 → 1150.50] Stuff
[1150.50 → 1151.32] Built
[1151.32 → 1151.80] Into
[1151.80 → 1152.08] The
[1152.08 → 1152.54] Compiler
[1152.54 → 1152.74] That
[1152.74 → 1152.88] Will
[1152.88 → 1153.22] Right
[1153.22 → 1154.86] I'm
[1154.86 → 1155.24] Serious
[1155.24 → 1155.48] Right
[1155.48 → 1155.68] Like
[1155.68 → 1155.86] This
[1155.86 → 1156.00] Is
[1156.00 → 1156.12] A
[1156.12 → 1156.86] Compiled
[1156.86 → 1157.18] This
[1157.18 → 1157.30] Is
[1157.30 → 1157.40] A
[1157.40 → 1157.68] Compile
[1157.68 → 1157.92] Time
[1157.92 → 1158.20] Error
[1158.20 → 1158.44] Right
[1158.44 → 1158.64] Like
[1158.64 → 1159.00] This
[1159.00 → 1159.06] Is
[1159.06 → 1159.18] Not
[1159.18 → 1159.30] A
[1159.30 → 1159.64] Runtime
[1159.64 → 1159.78] Error
[1159.78 → 1159.88] It's
[1159.88 → 1160.10] Compile
[1160.10 → 1160.26] Time
[1160.26 → 1160.40] Error
[1160.40 → 1160.66] Right
[1160.66 → 1161.76] Yeah
[1161.76 → 1162.42] So
[1162.42 → 1162.54] It
[1162.54 → 1162.70] Doesn't
[1162.70 → 1162.92] Matter
[1162.92 → 1163.60] What
[1163.60 → 1163.94] V8
[1163.94 → 1164.18] Does
[1164.18 → 1164.30] Is
[1164.30 → 1164.66] Irrelevant
[1164.66 → 1165.20] This
[1165.20 → 1165.40] Is
[1172.98 → 1173.38] So
[1173.38 → 1173.66] It
[1173.66 → 1174.08] Knows
[1174.08 → 1174.26] That
[1174.26 → 1174.42] You're
[1174.42 → 1174.92] Passing
[1174.92 → 1175.50] One
[1175.50 → 1175.98] Which
[1175.98 → 1176.30] Is
[1176.30 → 1176.62] A
[1176.62 → 1177.22] Constant
[1177.22 → 1177.56] A
[1177.56 → 1177.96] Numerical
[1177.96 → 1178.38] Constant
[1178.38 → 1178.92] To
[1178.92 → 1179.22] Something
[1179.22 → 1179.44] That
[1179.44 → 1179.88] Requires
[1179.88 → 1180.20] Status
[1180.20 → 1180.40] So
[1180.40 → 1181.04] Somebody
[1181.04 → 1182.00] Like
[1182.00 → 1182.52] Somebody
[1182.52 → 1182.90] In
[1182.90 → 1183.04] The
[1183.04 → 1183.54] Compiler
[1183.54 → 1184.30] Said
[1184.30 → 1184.50] That
[1184.50 → 1184.68] Was
[1184.68 → 1185.00] Okay
[1185.00 → 1185.82] They
[1185.82 → 1186.24] Must
[1186.24 → 1186.36] Have
[1186.36 → 1186.50] Had
[1186.50 → 1186.62] A
[1186.62 → 1186.84] Reason
[1186.84 → 1187.06] For
[1187.06 → 1187.28] That
[1187.28 → 1187.46] I
[1187.46 → 1188.00] Think
[1188.00 → 1188.72] Because
[1188.72 → 1189.88] That
[1189.88 → 1190.02] Would
[1190.02 → 1190.10] Be
[1190.10 → 1190.22] A
[1190.22 → 1190.36] Pretty
[1190.36 → 1190.60] Straight
[1190.60 → 1190.92] Forward
[1190.92 → 1191.22] Bug
[1191.22 → 1191.38] To
[1191.38 → 1191.58] Fix
[1191.58 → 1191.72] If
[1191.72 → 1191.78] It
[1191.78 → 1191.90] Was
[1191.90 → 1192.38] Accidental
[1192.38 → 1193.00] So
[1193.00 → 1193.26] I
[1193.26 → 1193.96] Really
[1193.96 → 1194.18] Would
[1194.18 → 1194.34] Like
[1194.34 → 1194.46] To
[1194.46 → 1194.58] Know
[1194.58 → 1194.76] What
[1194.76 → 1194.94] The
[1194.94 → 1195.44] Rational
[1195.44 → 1195.76] Was
[1195.76 → 1195.98] Because
[1195.98 → 1196.26] Those
[1196.26 → 1196.46] Two
[1196.46 → 1196.70] Things
[1196.70 → 1196.90] Are
[1202.98 → 1203.36] I'm
[1203.36 → 1203.52] Pretty
[1203.52 → 1203.64] Sure
[1203.64 → 1203.78] Just
[1203.78 → 1203.92] Like
[1203.92 → 1204.02] An
[1204.02 → 1204.60] Explicit
[1204.60 → 1205.00] From
[1205.00 → 1205.12] When
[1205.12 → 1205.56] I'm
[1205.56 → 1205.72] Trying
[1205.72 → 1205.80] To
[1205.80 → 1206.06] Recall
[1206.06 → 1206.22] What
[1206.22 → 1206.28] I
[1206.28 → 1206.54] Remember
[1206.54 → 1206.72] But
[1206.72 → 1206.82] I
[1206.82 → 1206.98] Think
[1206.98 → 1207.14] There's
[1207.14 → 1207.30] An
[1207.30 → 1207.66] Explicit
[1207.66 → 1208.02] Decision
[1208.02 → 1208.30] Here
[1208.30 → 1208.88] Yeah
[1208.88 → 1209.52] We'll
[1209.52 → 1209.78] Find
[1209.78 → 1210.04] Out
[1210.04 → 1211.52] It's
[1211.52 → 1211.68] Easy
[1211.68 → 1211.84] To
[1211.84 → 1212.60] Find
[1212.60 → 1212.84] Out
[1212.84 → 1213.08] For
[1213.08 → 1213.32] Sure
[1213.32 → 1213.62] Yeah
[1213.62 → 1214.14] That's
[1214.14 → 1214.44] Point
[1214.44 → 1214.68] Number
[1214.68 → 1214.96] Two
[1214.96 → 1215.12] In
[1215.12 → 1215.20] The
[1215.20 → 1215.42] YouTube
[1215.42 → 1215.82] Comments
[1215.82 → 1215.96] We'll
[1215.96 → 1216.06] Be
[1216.06 → 1216.28] Looking
[1216.28 → 1216.62] For
[1216.62 → 1216.98] Yeah
[1216.98 → 1217.86] Can
[1217.86 → 1218.06] Someone
[1218.06 → 1218.28] Leave
[1218.28 → 1218.40] A
[1218.40 → 1218.64] YouTube
[1218.64 → 1218.98] Comment
[1218.98 → 1219.14] And
[1219.14 → 1219.26] Let
[1219.26 → 1219.38] Us
[1232.98 → 1233.08] That
[1233.08 → 1233.38] Access
[1233.38 → 1233.74] It's
[1233.74 → 1233.86] Not
[1233.86 → 1234.22] Surface
[1234.22 → 1234.42] To
[1234.42 → 1234.60] You
[1234.60 → 1234.90] In
[1234.90 → 1235.26] JavaScript
[1235.26 → 1236.22] So
[1236.22 → 1236.84] It
[1236.84 → 1237.16] Can't
[1237.16 → 1237.30] Be
[1237.30 → 1237.58] Based
[1237.58 → 1237.72] On
[1237.72 → 1237.88] That
[1237.88 → 1238.08] It's
[1238.08 → 1238.26] Based
[1238.26 → 1238.40] On
[1238.40 → 1238.62] Someone
[1238.62 → 1238.80] Made
[1238.80 → 1238.94] The
[1238.94 → 1239.34] Intentional
[1239.34 → 1239.62] Design
[1239.62 → 1239.94] Decision
[1239.94 → 1240.10] That
[1240.10 → 1240.50] Numbers
[1240.50 → 1241.10] Can
[1241.10 → 1241.22] Be
[1241.22 → 1241.44] Raw
[1241.44 → 1241.82] Dogged
[1241.82 → 1242.08] And
[1242.08 → 1242.44] Strings
[1242.44 → 1242.78] Cannot
[1242.78 → 1243.42] Yeah
[1243.42 → 1244.28] And
[1244.28 → 1244.40] They
[1244.40 → 1244.60] Are
[1244.60 → 1245.04] Checking
[1245.04 → 1245.30] Like
[1245.30 → 1245.60] They
[1245.60 → 1246.18] Like
[1246.18 → 1246.48] Three
[1246.48 → 1246.72] Didn't
[1246.72 → 1247.02] Work
[1247.02 → 1247.34] So
[1247.34 → 1247.60] It's
[1247.60 → 1247.86] Not
[1247.86 → 1248.18] Like
[1248.18 → 1248.44] It's
[1248.44 → 1248.64] Just
[1248.64 → 1248.86] Like
[1248.86 → 1249.04] I
[1249.04 → 1249.16] Don't
[1249.16 → 1249.30] Know
[1249.30 → 1249.44] We're
[1249.44 → 1249.58] Just
[1249.58 → 1249.70] Going
[1249.70 → 1249.76] To
[1249.76 → 1250.12] It's
[1250.12 → 1250.24] Like
[1250.24 → 1250.42] No
[1250.42 → 1250.68] In
[1250.68 → 1250.78] The
[1250.78 → 1251.10] Compiler
[1251.10 → 1251.28] It
[1251.28 → 1251.50] Knows
[1251.50 → 1251.96] So
[1251.96 → 1252.24] This
[1252.24 → 1252.40] Was
[1252.40 → 1252.92] Intentional
[1252.92 → 1253.08] And
[1253.08 → 1253.28] I'd
[1253.28 → 1253.38] Love
[1253.38 → 1253.50] To
[1253.50 → 1253.62] Know
[1253.62 → 1253.86] Why
[1253.86 → 1254.08] Yeah
[1254.08 → 1254.18] I'd
[1254.18 → 1254.22] Be
[1254.22 → 1254.42] Interested
[1254.42 → 1254.52] To
[1254.52 → 1254.72] Know
[1254.72 → 1255.56] There
[1255.56 → 1255.70] Might
[1255.70 → 1255.82] Be
[1255.82 → 1255.92] A
[1255.92 → 1256.56] Very
[1256.56 → 1256.76] Good
[1256.76 → 1257.04] Reason
[1257.04 → 1257.26] Like
[1257.26 → 1257.44] Oh
[1257.44 → 1257.66] Yeah
[1257.66 → 1258.00] Because
[1258.00 → 1258.24] Of
[1258.24 → 1258.58] Like
[1258.58 → 1258.68] I
[1258.68 → 1258.86] Said
[1258.86 → 1259.60] I
[1259.60 → 1260.10] I
[1260.10 → 1260.48] Want
[1260.48 → 1260.60] To
[1260.60 → 1260.76] Say
[1260.76 → 1263.14] That
[1263.14 → 1263.36] I
[1263.36 → 1263.92] Remember
[1263.92 → 1264.20] The
[1264.20 → 1264.56] Dude
[1264.56 → 1264.88] Who
[1264.88 → 1265.18] Made
[1265.18 → 1265.38] The
[1265.38 → 1265.88] TypeScript
[1265.88 → 1266.38] Compiler
[1266.38 → 1266.54] In
[1266.54 → 1266.64] The
[1266.64 → 1266.88] First
[1266.88 → 1267.18] Place
[1267.18 → 1267.32] Or
[1267.32 → 1267.42] One
[1267.42 → 1267.50] Of
[1267.50 → 1267.56] The
[1267.56 → 1268.08] Dudes
[1268.08 → 1269.06] I
[1269.06 → 1269.34] Want
[1269.34 → 1269.44] To
[1269.44 → 1269.70] Say
[1269.70 → 1269.86] That
[1269.86 → 1269.96] He
[1269.96 → 1270.08] Was
[1270.08 → 1270.20] A
[1270.20 → 1270.40] Friend
[1270.40 → 1270.54] Of
[1270.54 → 1270.74] Dave
[1270.74 → 1271.20] Stafford
[1271.20 → 1271.32] So
[1271.32 → 1271.42] I
[1271.42 → 1271.56] Had
[1271.56 → 1271.80] Lunch
[1281.50 → 1281.80] Before
[1281.80 → 1282.22] Chrome
[1282.22 → 1282.42] For
[1282.42 → 1282.68] These
[1282.68 → 1282.88] Things
[1282.88 → 1283.30] The
[1283.30 → 1283.68] Original
[1283.68 → 1284.52] JavaScript
[1284.52 → 1287.32] Runtime
[1287.32 → 1287.70] Engine
[1287.70 → 1288.30] For
[1288.30 → 1288.96] IE
[1288.96 → 1289.12] When
[1289.12 → 1289.24] It
[1289.24 → 1289.56] First
[1289.56 → 1289.82] Got
[1289.82 → 1290.14] That
[1290.14 → 1290.54] And
[1290.54 → 1290.64] It
[1290.64 → 1290.76] Was
[1290.76 → 1291.62] Better
[1291.62 → 1291.84] Than
[1291.84 → 1292.14] Everyone
[1292.14 → 1292.40] Else
[1292.40 → 1292.50] It
[1292.50 → 1292.60] Was
[1292.60 → 1292.96] Way
[1292.96 → 1293.22] Better
[1293.22 → 1293.44] Than
[1293.44 → 1294.04] Netscape's
[1294.04 → 1294.16] Or
[1294.16 → 1294.40] Whatever
[1294.40 → 1294.68] Right
[1294.68 → 1295.24] So
[1295.24 → 1296.28] I'm
[1296.28 → 1296.82] Not
[1296.82 → 1297.06] Coming
[1297.06 → 1297.24] Into
[1297.24 → 1297.40] This
[1297.40 → 1297.50] With
[1297.50 → 1297.58] A
[1297.58 → 1297.92] Mentality
[1297.92 → 1298.14] That
[1298.14 → 1298.32] This
[1298.32 → 1298.50] Was
[1298.50 → 1298.74] Just
[1298.74 → 1299.00] Like
[1299.00 → 1299.18] A
[1299.18 → 1299.38] Bunch
[1299.38 → 1299.52] Of
[1299.52 → 1299.90] Toddlers
[1299.90 → 1300.10] And
[1300.10 → 1300.42] Diapers
[1300.42 → 1300.72] Running
[1300.72 → 1301.02] Around
[1301.02 → 1301.28] Going
[1301.28 → 1301.50] Like
[1301.50 → 1301.94] Wooloo
[1301.94 → 1302.20] Right
[1302.20 → 1302.38] I
[1302.38 → 1302.64] Think
[1302.64 → 1302.96] Like
[1302.96 → 1303.52] I'm
[1303.52 → 1304.16] Gonna
[1304.16 → 1304.60] Give
[1304.60 → 1304.72] Them
[1304.72 → 1304.82] The
[1304.82 → 1305.12] Of
[1305.12 → 1305.14] The
[1311.50 → 1312.08] That's
[1312.08 → 1312.38] Also
[1312.38 → 1312.56] The
[1312.56 → 1312.76] Best
[1312.76 → 1312.92] Way
[1312.92 → 1313.04] To
[1313.04 → 1313.20] Get
[1313.20 → 1313.32] A
[1313.32 → 1313.56] YouTube
[1313.56 → 1314.00] Comment
[1314.00 → 1314.32] Because
[1314.32 → 1314.50] They'll
[1314.50 → 1314.68] Say
[1314.68 → 1315.32] Actually
[1315.32 → 1315.76] TJ's
[1315.76 → 1315.86] An
[1315.86 → 1316.26] Idiot
[1316.26 → 1316.76] Here's
[1316.76 → 1316.88] What
[1316.88 → 1316.96] It
[1316.96 → 1317.08] Is
[1317.08 → 1317.18] So
[1317.18 → 1317.38] Here's
[1317.38 → 1317.54] My
[1317.54 → 1317.86] Guess
[1317.86 → 1319.22] I
[1319.22 → 1319.62] Actually
[1319.62 → 1319.80] Think
[1319.80 → 1319.92] It
[1319.92 → 1320.16] Has
[1320.16 → 1320.40] Something
[1320.40 → 1320.92] Possibly
[1320.92 → 1321.10] To
[1321.10 → 1321.24] Do
[1321.24 → 1321.40] With
[1321.40 → 1321.56] What
[1321.56 → 1321.88] You're
[1321.88 → 1322.28] Saying
[1322.28 → 1322.60] Prime
[1322.60 → 1323.08] Is
[1323.08 → 1323.20] I
[1323.20 → 1323.34] Do
[1323.34 → 1323.56] Wonder
[1323.56 → 1323.74] If
[1323.74 → 1324.00] There's
[1324.00 → 1324.22] A
[1324.22 → 1324.40] Few
[1324.40 → 1325.40] Comparisons
[1325.40 → 1325.80] Or
[1325.80 → 1326.54] Operations
[1326.54 → 1327.38] That
[1327.38 → 1327.58] Would
[1327.58 → 1327.94] Work
[1327.94 → 1328.14] For
[1328.14 → 1328.76] Numbers
[1328.76 → 1329.12] To
[1329.12 → 1329.38] Check
[1329.38 → 1329.54] A
[1329.54 → 1329.98] Quality
[1329.98 → 1330.26] That
[1330.26 → 1330.60] Don't
[1330.60 → 1330.84] Work
[1330.84 → 1331.02] For
[1331.02 → 1331.58] Strings
[1331.58 → 1332.62] Where
[1332.62 → 1333.38] If
[1333.38 → 1333.58] You're
[1333.58 → 1333.96] Not
[1333.96 → 1334.40] Holding
[1341.50 → 1343.82] Are
[1343.82 → 1344.02] There
[1344.02 → 1344.32] Some
[1344.32 → 1344.82] Operations
[1344.82 → 1345.04] That
[1345.04 → 1345.18] Get
[1345.18 → 1345.30] You
[1345.30 → 1345.80] Different
[1345.80 → 1346.54] Results
[1346.54 → 1346.90] That's
[1346.90 → 1347.04] My
[1347.04 → 1347.30] Guess
[1347.30 → 1347.82] Maps
[1347.82 → 1348.02] I
[1348.02 → 1350.18] Think
[1350.18 → 1350.30] You
[1350.30 → 1350.42] Can
[1350.42 → 1350.56] Use
[1350.56 → 1350.82] Map
[1350.82 → 1350.98] And
[1350.98 → 1351.12] Set
[1351.12 → 1351.36] To
[1351.36 → 1351.54] Do
[1351.54 → 1353.40] To
[1353.40 → 1353.68] Do
[1353.68 → 1355.54] To
[1355.54 → 1355.84] Do
[1355.84 → 1356.12] To
[1356.12 → 1357.94] To
[1357.94 → 1360.08] Do
[1360.08 → 1360.64] To
[1360.64 → 1361.12] Do
[1361.12 → 1361.86] To
[1361.86 → 1362.00] Do
[1362.00 → 1362.14] That
[1362.14 → 1362.34] With
[1362.34 → 1362.70] Enum
[1362.70 → 1362.88] So
[1362.88 → 1363.00] I
[1363.00 → 1363.74] Would
[1363.74 → 1363.86] Be
[1363.86 → 1364.00] A
[1364.00 → 1364.36] Surprise
[1364.36 → 1364.56] To
[1364.56 → 1364.68] Me
[1364.68 → 1364.84] To
[1364.84 → 1364.96] Know
[1364.96 → 1365.12] That
[1365.12 → 1365.20] You
[1365.20 → 1365.32] Can
[1365.32 → 1365.50] Do
[1365.50 → 1366.04] To
[1366.04 → 1366.06] Do
[1366.06 → 1366.22] To
[1366.22 → 1367.08] Do
[1367.08 → 1367.98] Anything
[1367.98 → 1368.72] In
[1368.72 → 1369.12] JavaScript
[1369.12 → 1369.92] Other
[1369.92 → 1370.08] Than
[1370.08 → 1370.58] Potentially
[1370.58 → 1371.16] Maps
[1371.16 → 1373.04] That's
[1373.04 → 1373.16] My
[1373.16 → 1373.44] Guess
[1373.44 → 1373.78] That's
[1373.78 → 1373.82] A
[1373.82 → 1373.92] Good
[1373.92 → 1374.10] Guess
[1374.10 → 1374.28] It's
[1374.28 → 1374.36] A
[1374.36 → 1374.52] Really
[1374.52 → 1374.68] Good
[1374.68 → 1374.92] Guess
[1374.92 → 1376.24] So
[1376.24 → 1376.38] Let
[1376.38 → 1376.46] Me
[1376.46 → 1376.66] Show
[1376.66 → 1376.74] You
[1376.74 → 1376.88] The
[1376.88 → 1377.40] Alternative
[1377.40 → 1377.58] To
[1377.58 → 1377.84] Ends
[1377.84 → 1378.00] That
[1378.00 → 1378.24] People
[1378.24 → 1378.96] Started
[1378.96 → 1379.28] Doing
[1379.28 → 1379.68] Instead
[1379.68 → 1380.46] Oh
[1380.46 → 1381.14] Oh
[1381.14 → 1381.36] No
[1381.36 → 1381.88] Are
[1381.88 → 1382.04] We
[1382.04 → 1382.20] Going
[1382.20 → 1382.38] Off
[1382.38 → 1382.58] Script
[1382.58 → 1382.78] Here
[1382.78 → 1382.86] Are
[1382.86 → 1382.94] We
[1382.94 → 1383.08] Going
[1383.08 → 1383.26] Off
[1383.26 → 1383.50] Script
[1383.50 → 1383.80] No
[1383.80 → 1383.96] Can
[1383.96 → 1384.04] You
[1384.04 → 1384.16] See
[1384.16 → 1384.30] My
[1384.30 → 1384.58] Screen
[1384.58 → 1384.94] Yes
[1384.94 → 1385.10] I
[1385.10 → 1385.20] Can
[1385.20 → 1385.66] On
[1385.66 → 1386.00] Script
[1386.00 → 1386.48] Holy
[1386.48 → 1386.78] Cow
[1386.78 → 1387.08] Nice
[1387.08 → 1387.46] Trash
[1387.46 → 1387.86] Well
[1387.86 → 1388.02] I
[1388.02 → 1388.16] Didn't
[1388.16 → 1388.28] Do
[1388.28 → 1388.42] This
[1388.42 → 1388.56] During
[1388.56 → 1388.72] My
[1388.72 → 1388.98] Talk
[1388.98 → 1389.16] I'm
[1389.16 → 1389.24] Going
[1389.24 → 1389.38] Do
[1389.38 → 1389.48] It
[1389.48 → 1389.70] Here
[1389.70 → 1390.66] So
[1390.66 → 1392.00] People
[1392.00 → 1392.40] Stop
[1392.40 → 1392.72] Doing
[1392.72 → 1393.32] Ends
[1393.32 → 1393.54] And
[1393.54 → 1393.68] They
[1393.68 → 1394.00] Favour
[1394.00 → 1394.46] This
[1394.46 → 1394.76] Stuff
[1394.76 → 1394.90] Right
[1394.90 → 1395.00] Here
[1395.00 → 1395.12] So
[1395.12 → 1395.24] This
[1395.24 → 1395.34] Is
[1395.34 → 1396.10] You
[1396.10 → 1397.50] Defining
[1397.50 → 1398.16] JavaScript
[1398.16 → 1399.10] At
[1399.10 → 1399.26] This
[1399.26 → 1399.52] Point
[1399.52 → 1399.74] But
[1399.74 → 1399.96] You
[1399.96 → 1400.16] Add
[1400.16 → 1400.56] As
[1400.56 → 1400.90] Coast
[1400.90 → 1401.12] Here
[1401.12 → 1402.00] Which
[1402.00 → 1402.12] Is
[1402.12 → 1402.42] Kind
[1402.42 → 1402.58] Of
[1402.58 → 1403.06] Like
[1403.06 → 1403.66] Object
[1403.66 → 1404.24] Freeze
[1404.24 → 1404.86] Freezing
[1404.86 → 1405.00] The
[1405.00 → 1405.28] Object
[1405.28 → 1405.46] But
[1405.46 → 1405.58] At
[1405.58 → 1405.68] The
[1405.68 → 1405.88] Type
[1405.88 → 1406.14] Level
[1406.14 → 1407.00] So
[1407.00 → 1407.20] Instead
[1407.20 → 1407.30] Of
[1407.30 → 1407.46] Doing
[1407.46 → 1407.78] Ends
[1407.78 → 1408.06] People
[1408.06 → 1408.48] Actually
[1408.48 → 1408.70] Do
[1408.70 → 1409.14] This
[1409.14 → 1410.10] Convert
[1410.10 → 1410.60] That
[1410.60 → 1411.72] Into
[1411.72 → 1411.92] A
[1411.92 → 1412.26] Type
[1412.26 → 1413.88] And
[1413.88 → 1414.24] Then
[1414.24 → 1414.98] This
[1414.98 → 1415.08] Is
[1415.08 → 1415.24] Kind
[1415.24 → 1415.30] Of
[1415.30 → 1415.44] Getting
[1415.44 → 1415.64] Into
[1415.64 → 1415.78] The
[1415.78 → 1416.00] Weeds
[1416.00 → 1416.12] Like
[1416.12 → 1416.24] You're
[1416.24 → 1416.40] Probably
[1416.40 → 1416.50] Just
[1416.50 → 1416.58] Going
[1416.58 → 1416.60] To
[1416.60 → 1416.86] What
[1416.86 → 1416.96] The
[1416.96 → 1417.08] Hell
[1417.08 → 1417.20] Is
[1417.20 → 1417.56] Happening
[1417.56 → 1418.18] But
[1418.18 → 1418.34] The
[1418.34 → 1418.76] Experience
[1418.76 → 1419.14] Now
[1419.14 → 1419.54] Is
[1419.54 → 1420.08] I
[1420.08 → 1420.20] Don't
[1420.20 → 1420.32] Have
[1420.32 → 1420.42] To
[1420.42 → 1420.64] Import
[1420.64 → 1420.76] An
[1420.76 → 1421.12] Enum
[1421.12 → 1421.48] I
[1421.48 → 1422.98] Can
[1422.98 → 1423.68] Now
[1423.68 → 1423.88] See
[1423.88 → 1424.02] All
[1424.02 → 1424.12] The
[1424.12 → 1424.44] Values
[1424.44 → 1424.58] That
[1424.58 → 1424.68] Are
[1424.68 → 1425.08] Valid
[1425.08 → 1425.56] Right
[1425.56 → 1426.00] So
[1426.00 → 1426.20] This
[1426.20 → 1426.32] Is
[1426.32 → 1426.44] What
[1426.44 → 1426.64] People
[1426.64 → 1426.86] Like
[1426.86 → 1426.98] To
[1426.98 → 1427.14] Do
[1427.14 → 1427.54] Because
[1427.54 → 1427.84] At
[1427.84 → 1427.94] The
[1427.94 → 1428.66] The
[1428.66 → 1429.06] Ends
[1429.06 → 1429.86] Actually
[1429.86 → 1430.18] Turned
[1430.18 → 1430.30] Into
[1430.30 → 1430.68] Runtime
[1430.68 → 1430.98] Code
[1430.98 → 1431.86] Which
[1431.86 → 1431.98] Is
[1431.98 → 1432.24] Actually
[1432.24 → 1432.50] One
[1432.50 → 1432.60] Of
[1432.60 → 1432.72] The
[1432.72 → 1433.02] Things
[1433.02 → 1433.24] That
[1433.24 → 1433.46] Like
[1433.46 → 1433.64] I
[1433.64 → 1434.08] Believe
[1434.08 → 1435.02] The
[1435.02 → 1435.30] TypeScript
[1435.30 → 1435.58] Team
[1435.58 → 1435.80] Kind
[1435.80 → 1435.90] Of
[1435.90 → 1436.28] Regrets
[1436.28 → 1436.48] Is
[1436.48 → 1436.72] Using
[1436.72 → 1437.08] Ends
[1437.08 → 1437.28] Like
[1437.28 → 1437.46] There's
[1437.46 → 1437.70] Actually
[1437.70 → 1437.90] Like
[1437.90 → 1438.02] A
[1438.02 → 1438.36] Rule
[1438.36 → 1439.04] In
[1439.04 → 1439.36] TypeScript
[1439.36 → 1439.58] Now
[1439.58 → 1439.74] If
[1439.74 → 1439.86] You're
[1439.86 → 1440.36] Doing
[1440.36 → 1440.74] TypeScript
[1440.74 → 1440.94] In
[1440.94 → 1441.16] Node
[1441.16 → 1441.38] To
[1441.38 → 1441.80] Actually
[1441.80 → 1442.40] Not
[1442.40 → 1442.62] Allow
[1442.62 → 1442.72] You
[1458.66 → 1458.96] I
[1458.96 → 1459.16] Know
[1459.16 → 1459.36] So
[1459.36 → 1459.60] Here
[1459.60 → 1459.80] We're
[1459.80 → 1460.14] Basically
[1460.14 → 1460.52] This
[1460.52 → 1460.68] Is
[1460.68 → 1461.02] Where
[1461.02 → 1461.84] We
[1461.84 → 1462.40] Intersect
[1462.40 → 1462.64] Okay
[1462.64 → 1463.12] Let me
[1463.12 → 1463.30] Back
[1463.30 → 1463.48] Up
[1463.48 → 1463.60] So
[1463.60 → 1464.06] TypeScript
[1464.06 → 1464.64] Which
[1464.64 → 1464.90] People
[1464.90 → 1465.34] Always
[1465.34 → 1466.08] Mess
[1466.08 → 1466.26] This
[1466.26 → 1466.46] Up
[1466.46 → 1466.64] Is
[1466.64 → 1467.12] Strictly
[1467.12 → 1467.34] At
[1467.34 → 1467.46] The
[1467.46 → 1467.70] Type
[1467.70 → 1468.04] Level
[1468.04 → 1468.74] And
[1468.74 → 1469.12] JavaScript
[1469.12 → 1469.42] Is
[1469.42 → 1469.56] At
[1469.56 → 1469.68] The
[1469.68 → 1470.02] Runtime
[1470.02 → 1470.24] Level
[1470.24 → 1470.46] Like
[1470.46 → 1470.58] They
[1470.58 → 1470.82] Don't
[1470.82 → 1471.28] Intersect
[1471.28 → 1471.62] The
[1471.62 → 1471.86] Place
[1471.86 → 1472.00] Where
[1472.00 → 1472.14] They
[1472.14 → 1472.42] Can
[1472.42 → 1472.90] Actually
[1472.90 → 1473.16] Kind
[1473.16 → 1473.22] Of
[1473.22 → 1473.66] Intersect
[1473.66 → 1474.14] Is
[1474.14 → 1474.30] This
[1474.30 → 1474.54] Line
[1474.54 → 1474.72] Right
[1474.72 → 1474.92] Here
[1474.92 → 1475.04] Is
[1475.04 → 1475.14] Where
[1475.14 → 1475.26] You
[1475.26 → 1475.44] Do
[1475.44 → 1475.80] Type
[1475.80 → 1476.14] Of
[1476.14 → 1476.86] Foo
[1476.86 → 1477.10] Where
[1477.10 → 1477.28] This
[1477.28 → 1477.40] Is
[1477.40 → 1477.82] Actually
[1477.82 → 1478.44] Referencing
[1478.44 → 1479.22] Some
[1479.22 → 1479.62] Runtime
[1479.62 → 1479.92] Code
[1488.66 → 1488.90] Now
[1488.90 → 1489.06] You're
[1489.06 → 1489.42] Officially
[1489.42 → 1489.62] In
[1489.62 → 1489.74] The
[1489.74 → 1489.94] Type
[1489.94 → 1490.28] World
[1490.28 → 1490.98] Right
[1490.98 → 1491.46] So
[1491.46 → 1491.70] We've
[1491.70 → 1492.20] Officially
[1492.20 → 1492.94] Turned
[1492.94 → 1493.28] This
[1493.28 → 1493.98] Into
[1493.98 → 1494.38] Bar
[1494.38 → 1495.30] And
[1495.30 → 1495.64] Now
[1495.64 → 1495.84] We
[1495.84 → 1495.96] Can
[1495.96 → 1496.10] See
[1496.10 → 1496.24] The
[1496.24 → 1496.46] Type
[1496.46 → 1496.60] Here
[1496.60 → 1496.82] Like
[1496.82 → 1497.22] Read
[1497.22 → 1497.42] Only
[1497.42 → 1497.90] Failed
[1497.90 → 1498.36] And
[1498.36 → 1498.46] We
[1498.46 → 1498.60] See
[1498.60 → 1498.74] It's
[1498.74 → 1498.92] Read
[1498.92 → 1499.28] Only
[1499.28 → 1499.84] Because
[1499.84 → 1500.56] This
[1500.56 → 1500.78] As
[1500.78 → 1501.08] Cons
[1501.08 → 1501.30] Because
[1501.30 → 1501.42] It
[1501.42 → 1501.76] Behaves
[1501.76 → 1501.90] Of
[1501.90 → 1502.10] Like
[1502.10 → 1502.74] Freezing
[1502.74 → 1503.04] Something
[1503.04 → 1503.22] At
[1503.22 → 1503.34] The
[1503.34 → 1503.54] Type
[1503.54 → 1503.84] Level
[1503.84 → 1504.76] So
[1504.76 → 1504.88] What
[1504.88 → 1505.00] We
[1505.00 → 1505.16] Do
[1505.16 → 1505.46] Now
[1505.46 → 1505.72] Is
[1505.72 → 1505.86] We
[1505.86 → 1505.98] Can
[1505.98 → 1506.14] Get
[1506.14 → 1506.24] All
[1506.24 → 1506.36] The
[1506.36 → 1506.68] Keys
[1506.68 → 1506.96] It's
[1506.96 → 1507.30] An
[1507.30 → 1507.60] Object
[1507.60 → 1507.94] Right
[1507.94 → 1508.10] So
[1508.10 → 1508.20] We
[1508.20 → 1508.32] Get
[1508.32 → 1508.44] The
[1508.44 → 1508.78] Keys
[1508.86 → 1509.30] We
[1509.30 → 1509.46] Now
[1509.46 → 1509.58] See
[1509.58 → 1510.06] That's
[1510.06 → 1510.20] My
[1510.20 → 1510.70] Dog's
[1510.70 → 1511.12] Favourite
[1511.12 → 1511.58] Type
[1511.58 → 1512.84] What
[1512.84 → 1513.58] Barbies
[1513.58 → 1514.16] Oh
[1514.16 → 1514.34] My
[1514.34 → 1514.64] God
[1514.64 → 1515.06] Stop
[1515.06 → 1518.14] You
[1518.14 → 1518.38] Are
[1518.38 → 1518.60] The
[1518.60 → 1519.08] Worst
[1519.08 → 1520.54] Is
[1520.54 → 1520.68] That
[1520.68 → 1520.84] An
[1520.84 → 1521.18] Actual
[1521.18 → 1521.56] Brand
[1521.56 → 1521.76] Is
[1521.76 → 1521.86] That
[1521.86 → 1522.28] No
[1522.28 → 1523.06] Barbies
[1523.06 → 1523.70] I'll
[1523.70 → 1523.88] Be
[1523.88 → 1524.44] Yeah
[1524.44 → 1525.50] I
[1525.50 → 1525.86] Thought
[1525.86 → 1526.02] It
[1526.02 → 1526.72] Was
[1526.72 → 1526.84] Like
[1526.84 → 1526.94] A
[1526.94 → 1527.20] Brand
[1527.20 → 1527.78] Chewy
[1527.78 → 1528.02] Or
[1528.02 → 1528.32] Something
[1528.32 → 1528.64] Okay
[1528.64 → 1528.90] Okay
[1528.90 → 1529.36] The
[1529.36 → 1530.68] Intersection
[1530.68 → 1530.94] Of
[1530.94 → 1531.28] Dad
[1531.28 → 1531.74] Jokes
[1531.74 → 1532.04] And
[1532.04 → 1532.82] Programming
[1532.82 → 1533.38] Is
[1533.38 → 1533.82] TJ
[1533.82 → 1535.32] I
[1535.32 → 1535.60] Only
[1535.60 → 1535.96] Wanted
[1535.96 → 1536.06] To
[1536.06 → 1536.20] Go
[1536.20 → 1536.52] Line
[1536.52 → 1536.70] By
[1536.70 → 1537.12] Line
[1537.12 → 1537.34] Through
[1537.34 → 1537.54] This
[1537.54 → 1537.76] Because
[1537.76 → 1537.96] I
[1537.96 → 1538.48] Had
[1538.48 → 1538.66] That
[1538.66 → 1538.88] Joke
[1538.88 → 1539.22] As
[1539.22 → 1539.56] Soon
[1539.56 → 1539.72] As
[1539.72 → 1539.84] I
[1539.84 → 1540.14] Saw
[1540.14 → 1540.40] You
[1540.40 → 1540.64] Bring
[1540.64 → 1540.80] This
[1540.80 → 1541.08] Out
[1541.08 → 1541.46] I
[1541.46 → 1542.44] Am
[1542.44 → 1543.06] Not
[1543.06 → 1543.40] Gonna
[1543.40 → 1543.74] Let
[1543.74 → 1544.22] This
[1544.22 → 1544.94] Joke
[1544.94 → 1545.34] Pass
[1545.34 → 1545.60] I
[1545.60 → 1545.78] Am
[1545.78 → 1546.18] Gonna
[1546.18 → 1546.44] Get
[1546.44 → 1546.60] A
[1546.60 → 1546.94] Chance
[1546.94 → 1547.12] To
[1547.12 → 1547.36] Drop
[1547.36 → 1547.62] This
[1547.62 → 1547.92] Joke
[1547.92 → 1548.48] Let
[1548.48 → 1548.76] Let
[1548.76 → 1548.78] Let
[1548.78 → 1549.26] Let
[1549.26 → 1549.32] Let
[1549.32 → 1549.34] Let
[1549.34 → 1549.36] Let
[1549.36 → 1549.38] Let
[1549.38 → 1549.68] Let
[1549.68 → 1549.90] Let
[1549.90 → 1549.98] Let
[1549.98 → 1550.06] Let
[1550.06 → 1550.24] Let
[1550.24 → 1550.40] Let
[1550.40 → 1550.78] Let
[1550.78 → 1551.40] Let
[1551.40 → 1551.94] Let
[1551.94 → 1551.98] Let
[1551.98 → 1552.28] Let
[1552.28 → 1562.56] Let
[1562.56 → 1563.06] Let
[1563.06 → 1563.40] Let
[1563.40 → 1563.92] Let
[1563.92 → 1564.06] Let
[1564.06 → 1564.14] Let
[1564.14 → 1564.40] Let
[1564.40 → 1564.56] Let
[1564.56 → 1564.94] Let
[1564.94 → 1565.88] Let
[1565.88 → 1566.34] Let
[1566.34 → 1596.34] 
[1596.34 → 1607.62] Come
[1607.88 → 1608.26] dividend
[1608.26 → 1609.76] Is Dax at your house?
[1610.00 → 1611.00] Did you have Dax over?
[1611.16 → 1613.14] I got Dax's people over right now.
[1613.66 → 1614.26] Oh, no.
[1614.38 → 1615.90] If I keep talking, does it go away?
[1616.02 → 1617.06] Like, if I just keep saying, hey.
[1617.06 → 1620.36] No, but just keep talking and pretend like it's not far in.
[1620.36 → 1620.54] Okay, okay.
[1620.60 → 1622.14] Anyway, well, I just want to show you this real quick.
[1622.28 → 1626.46] So, again, here are the keys of that structure, that object-like structure at the top.
[1626.80 → 1627.48] Feeling the success.
[1627.62 → 1630.28] If we want the values, we would just do it like this.
[1630.32 → 1632.02] It looks like JavaScript, to be honest, right?
[1632.06 → 1635.10] Like, this is kind of like how you access objects with their keys, right?
[1635.76 → 1636.64] And you get their values.
[1636.64 → 1640.78] So, now, if we did Barbies, based on Teen's joke, right?
[1641.10 → 1644.30] We now see we get the autocomplete of this.
[1644.40 → 1644.90] Failed in success.
[1645.14 → 1649.00] And if we do bar values, we can now see we get the autocomplete.
[1649.14 → 1652.80] So, this is like an alternative way to ends, which people actually like doing instead.
[1653.56 → 1658.80] Like I said, the other quirk is like with now node, they have like this new, like, strip.
[1658.94 → 1659.82] I forget the name of it.
[1659.84 → 1662.78] But basically, they don't want you using ends in node in TypeScript.
[1663.54 → 1665.56] I feel like I missed something here.
[1665.56 → 1670.22] Just so that we make sure that we get through a maximum of two slides per hour.
[1671.62 → 1675.92] So, I see what you're doing here or whatever this is.
[1675.92 → 1679.12] I understand the example that you showed here.
[1679.54 → 1683.38] But what I must have missed somewhere in between this is why.
[1683.38 → 1686.84] So, what was wrong with the enum version?
[1687.20 → 1697.38] And also, so like, at least for me, what I would have wanted as a programmer when I was initially creating an enum is I wanted to see...
[1697.38 → 1704.06] This is probably because I'm coming from a background of programming languages with ends that maybe work a little differently.
[1704.06 → 1709.28] But what I wanted to see was X parentheses success, no quotes around it.
[1709.40 → 1713.36] Because to me as a programmer, that lets me know, oh, this isn't a string.
[1713.52 → 1714.06] It's an exuberant.
[1714.92 → 1719.22] So, this actually looks more confusing to the user to me.
[1719.36 → 1721.58] So, this looks worse than the enum case to me.
[1721.72 → 1724.10] And yet you're saying people go out of their way to do it this way.
[1724.50 → 1724.86] Why?
[1724.96 → 1727.96] What was wrong with the enum version that makes them want to do this?
[1728.10 → 1730.70] I think this is more up for...
[1730.70 → 1732.50] I think it's kind of subjective in my opinion.
[1732.58 → 1736.02] So, I'll tell you why I've seen people use it and why sometimes I use it.
[1736.48 → 1740.74] One, because it's no mystery on what's actually being compiled to.
[1740.82 → 1743.74] So, like, if you did an enum, you don't even know what that looks like at runtime, right?
[1743.76 → 1744.92] Because it's all compiled down.
[1745.32 → 1749.52] So, at least here, I can actually see what the Java output is going to be.
[1749.90 → 1750.68] So, that's like one reason.
[1750.76 → 1752.98] So, I can see the runtime code next to my types.
[1752.98 → 1754.42] It's not hidden behind the compiler.
[1755.62 → 1758.64] Oh, like they don't want to see 0, 1, 2, 3 is what you're saying.
[1758.80 → 1759.80] Yeah, yeah, yeah.
[1760.18 → 1760.54] Okay.
[1761.00 → 1761.32] Exactly.
[1761.44 → 1767.04] And then also, the other thing where you have to actually import, like if this was enum foo,
[1767.16 → 1769.30] I would have to do something like...
[1769.30 → 1771.48] I'll do Vim mode broken the playground.
[1771.88 → 1772.60] Oh, my goodness.
[1772.78 → 1773.54] Let me refresh it.
[1774.62 → 1775.52] I can't do this.
[1776.72 → 1777.28] Oh, man.
[1777.32 → 1778.00] This thing sucks.
[1778.12 → 1778.30] Okay.
[1778.36 → 1778.72] Anyway.
[1778.96 → 1781.72] So, what you would normally do, you would do like foo. Failed, right?
[1781.72 → 1784.42] And you would have to like import that.
[1784.90 → 1786.20] Here, you could...
[1786.20 → 1787.04] You would actually...
[1787.04 → 1790.70] Since you are familiar with the values, you could just do something like this and get
[1790.70 → 1791.50] everything right here.
[1791.90 → 1792.32] So, it's like...
[1792.32 → 1793.46] That's more of a DX thing.
[1793.58 → 1794.86] I don't think it's like the biggest gain.
[1795.02 → 1795.50] Well...
[1795.50 → 1798.56] But I personally think people do it because of this.
[1798.68 → 1800.58] And someone in the comments can tell you otherwise.
[1800.82 → 1801.18] Okay.
[1801.18 → 1803.90] But I think this is like the biggest win is actually seeing what the runtime code is.
[1803.90 → 1805.26] I'm starting to understand.
[1805.72 → 1806.62] I see.
[1807.14 → 1810.00] I think Casey and you are talking about two different things too, right?
[1810.08 → 1812.38] Because Casey's used to see that where they're actually...
[1812.38 → 1812.88] That answered my question.
[1812.88 → 1813.78] They're like identifiers.
[1814.52 → 1816.84] Enumerations become identifiers for you to know about.
[1816.94 → 1819.96] Whereas in this world, you're actually having...
[1819.96 → 1820.72] It's not that.
[1820.76 → 1823.42] It's like these ethereal things that you actually reference with strings.
[1824.38 → 1824.74] Yeah.
[1824.82 → 1826.12] Let me show you another big foot.
[1826.12 → 1827.60] TJ has a thingy.
[1828.36 → 1828.72] Oh, yeah.
[1828.78 → 1829.00] Go ahead.
[1829.08 → 1829.10] Go ahead.
[1829.10 → 1829.32] Yeah.
[1829.32 → 1829.94] So, yeah.
[1829.96 → 1830.70] He can't see me.
[1830.78 → 1831.68] So, that's okay, Trash.
[1832.12 → 1833.60] I do think the...
[1833.60 → 1834.10] CM Griffin.
[1834.24 → 1835.48] Shout out CM Griffin in the chat.
[1835.62 → 1837.22] And I think this is the other main reason.
[1837.34 → 1839.86] Is if you have to import...
[1839.86 → 1841.88] Like, you got to remember as well, Casey, right?
[1841.92 → 1844.70] Like, people are not just shipping one blob of stuff sometimes.
[1844.78 → 1847.18] Sometimes this makes for, like, they are shipping one blob.
[1847.28 → 1848.78] They're shipping it to the front end.
[1848.80 → 1850.30] So, this could mean, like...
[1850.30 → 1851.46] Oh, you have an enum.
[1851.54 → 1852.88] You want to use it in your code.
[1852.88 → 1853.16] Okay.
[1853.28 → 1855.56] Now, I import this package.
[1855.96 → 1857.60] And now, all of a sudden, I, like...
[1857.60 → 1859.18] I'm going to balloon the size.
[1859.32 → 1860.38] Of my JS bundle.
[1860.54 → 1863.02] Normally, people like that kind of thing happening.
[1863.12 → 1866.28] But, like, in the web world, it's kind of a net negative to balloon your bundle.
[1866.86 → 1868.98] So, they're trying not to have that happen.
[1869.08 → 1872.76] So, if you can just do a string directly, you can avoid, like, that scenario.
[1873.76 → 1874.36] Oh, sorry.
[1874.44 → 1875.00] I was going to say...
[1875.00 → 1879.62] Like, if I had to summarize my understanding of it now, just having only seen this much,
[1879.84 → 1887.70] I guess I would say the problem is that JavaScript, the runtime layer, is basically forcing you to do one of two things.
[1887.70 → 1897.58] Either you can use some kind of constant that already exists in JavaScript, which is either going to have to be a string or a number, right?
[1897.58 → 1897.62] Right.
[1898.24 → 1909.20] And if you choose number, then anyone who's calling this who's not using TypeScript is just going to see, like, three as the parameter, which is not what you want.
[1909.26 → 1911.24] You wanted something that they could actually read.
[1911.24 → 1911.42] Yes.
[1911.42 → 1923.32] So, you have to pick string because it's your only other option for a constant unless you were going to literally import an object whose references you could compare, which is what you don't want to do.
[1923.40 → 1927.10] Is that a fairly reasonable summary for, like, why it's, like, okay?
[1927.48 → 1932.60] Because otherwise, it would just all be numbers in the code and people don't want that because it can't be read in JavaScript.
[1932.88 → 1934.86] So, it doesn't allow you to do, like, pound defines or anything.
[1934.86 → 1935.16] Correct.
[1935.42 → 1935.62] Right.
[1936.64 → 1942.56] So, here's one more interesting thing is, like, so ends will automatically assign number values to them.
[1942.96 → 1944.56] So, like, red and green, zero and one.
[1944.86 → 1945.02] Yeah.
[1945.12 → 1955.40] So, if you define your ends like that and then in your runtime code you're depending on that order, you could easily break all your code by rearranging the order of your values.
[1955.44 → 1956.02] Does that make sense?
[1956.84 → 1957.02] Yeah.
[1957.06 → 1959.92] Well, that's kind of normal for ends in general.
[1959.92 → 1960.28] Yeah.
[1960.56 → 1962.48] So, that's, like, a foot gun that people don't understand.
[1962.68 → 1966.36] So, people, like, if you actually need to depend on values, you need to explicitly define them.
[1966.78 → 1966.98] Got it.
[1966.98 → 1968.48] Otherwise, they get implicit values.
[1968.58 → 1971.74] And if you're depending on those implicit values, you can easily just, like, mess up the logic.
[1971.86 → 1979.22] Like, they save something to disk and reread it, and they think that because it's named the same thing, it will still be equivalent, but it's not because we changed the order.
[1979.40 → 1979.42] Exactly.
[1979.42 → 1980.48] Because green would be zero.
[1980.74 → 1980.88] Yeah.
[1980.90 → 1982.06] But it was one before.
[1982.58 → 1982.88] Got it.
[1982.88 → 1983.12] You know what I mean?
[1983.12 → 1989.92] Nothing I've seen, like, too much in practice, like, on my end professionally, but I can definitely see someone, like, doing that.
[1989.92 → 1990.06] Got it.
[1991.50 → 1997.58] Especially since a bunch of the functions for numbers will accept just a raw number, right?
[1997.64 → 1998.78] We saw that earlier.
[1999.08 → 1999.88] We saw that happen, yeah.
[2000.40 → 2002.18] So, it's like, that won't give you an error.
[2002.52 → 2005.24] That does seem like a recipe for disaster.
[2005.58 → 2005.84] Right.
[2005.90 → 2006.22] Love it.
[2006.68 → 2007.90] Learning a lot today.
[2008.00 → 2008.64] Loved Galactic.
[2009.52 → 2009.76] Right.
[2009.76 → 2014.88] So, here's another quirk that I think is very popular in the ecosystem that people, like, experience day to day.
[2015.38 → 2020.44] So, like, if we use, like, a filter function of Boolean, that's just, like, a fancy way of just filtering out false values.
[2020.88 → 2022.78] So, like, in this array, we have one undefined three.
[2023.08 → 2025.08] The false value is going to be undefined here.
[2025.24 → 2027.34] So, at runtime, if we log this, we get one and three.
[2028.36 → 2035.34] So, by looking at that output, we would expect, since it behaves this at runtime, that it would give us a type of, like, a number array, right?
[2035.96 → 2041.22] But what actually happens is we get number or undefined because it's not able to narrow that.
[2041.22 → 2045.98] So, like, the implication here is, like, there are workarounds with, like, things like flat map and, like, type guards.
[2046.56 → 2055.84] But even though you know for a fact that runtime, you're never going to get undefined, you don't have to, like, program defensively against this case because TypeScript will give you, like, those, like, red squiggles.
[2055.94 → 2057.28] Because it's, like, there could be an undefined here.
[2057.62 → 2058.72] So, that's the annoying part.
[2059.40 → 2063.12] And this next thing, this one hit hard during the live thing.
[2063.24 → 2064.04] So, I had, like, this thing here.
[2064.08 → 2064.80] This is Matt Po cock.
[2065.08 → 2069.44] He's, like, a big person in the TypeScript community.
[2069.78 → 2070.88] Dude, everyone laughed so hard.
[2070.94 → 2071.96] I was, like, I was so happy.
[2072.06 → 2075.86] I was, like, man, I'm really – before I hit the button, I was, like, please let everyone laugh.
[2076.26 → 2077.36] But, anyway, so this is Matt Po cock.
[2077.50 → 2079.40] He built a library called TS Reset.
[2079.70 → 2083.38] And it will basically reset, like, these weird quirks that kind of go against your mental model.
[2083.78 → 2086.46] So, if you use this library, it's kind of like a CSS Reset.
[2086.66 → 2088.48] But at the type level or TypeScript.
[2088.70 → 2091.96] So, it would actually give you number array versus number undefined.
[2092.26 → 2094.30] And there are a bunch of other cases this library accounts for.
[2094.84 → 2098.14] But, like, looking at this, though, like, this is kind of annoying.
[2098.24 → 2102.14] And it's, like, a common thing people work around in their code bases.
[2103.08 → 2104.58] So, I don't know if there are any comments here.
[2104.70 → 2106.68] Not, like, again, like, nothing too, too crazy.
[2106.82 → 2108.48] But it is, like, really, really annoying.
[2108.88 → 2109.72] It makes perfect sense.
[2109.72 → 2120.94] I mean, you know, because it's, like, unless you special case filter, and you basically say, all right, instead of treating filter as just a function that operates on an array,
[2121.18 → 2129.98] I now have to treat it as a special case where I know that it happens to remove things of a certain type from this array.
[2129.98 → 2137.14] Therefore, I should mutate the actual type of the array that it returns to be different from the type of the array that it takes.
[2137.20 → 2140.34] Which would be a very unusual thing for a compiler to do.
[2140.64 → 2142.86] So, it makes perfect sense why they did it this way.
[2142.98 → 2146.24] I can also understand why people get confused when they do it.
[2146.50 → 2146.52] Yeah.
[2146.52 → 2147.38] But it makes perfect sense.
[2147.38 → 2151.98] I think the course of, like, the workarounds, like, it just gets verbose, like, having to do, like, a type guard or...
[2151.98 → 2152.98] There are some oddities to this.
[2152.98 → 2154.26] It just kind of goes against your mental model.
[2154.26 → 2161.20] So, the big thing is you can actually throw a generic on filter, but Boolean is a constructor.
[2161.46 → 2164.54] So, it doesn't really understand that Boolean is also a function.
[2164.66 → 2166.04] You can treat Boolean as a function.
[2166.56 → 2171.58] And so, it kind of blows up, and Boolean just returns, you know, it returns the positive case.
[2171.76 → 2173.26] So, it has a really...
[2173.80 → 2176.18] It has this hard time mapping through things.
[2176.18 → 2179.42] And so, it looks like it's...
[2179.42 → 2179.98] It just...
[2179.98 → 2181.02] It can't do it...
[2181.02 → 2184.88] So, you can't use generics and a Boolean thing because the constructor returns not that.
[2184.98 → 2186.12] And so, filter kind of explodes.
[2186.92 → 2189.46] You could imagine something even more ridiculous, right?
[2189.56 → 2193.18] Like, if just to illustrate how odd this kind of case is, right?
[2193.62 → 2199.80] Is, like, let's suppose that you imagine something where you're like, we have a typed array.
[2200.00 → 2202.22] And you're like, what type of stuff does this have in it?
[2202.22 → 2207.76] It's like, oh, you know, like, imagine you distinguish between integers and floating point values.
[2207.80 → 2211.78] So, numbers like 1, 2, 3, 4, 5 versus 3.213, 4, 5, right?
[2212.48 → 2215.40] And you can create one of these, and it has a mixed set.
[2215.40 → 2218.08] So, it's got 1 and 1.5 in it, right?
[2218.48 → 2225.30] And then you have some mathematical function, or something like this, that goes through and rounds all the values.
[2225.30 → 2232.84] Like, you wouldn't intuitively expect the compiler to now change the type of the thing that you were, right?
[2232.86 → 2238.72] Because it's just something that happened to end up being true after some operations occurred on this thing.
[2239.10 → 2240.80] And that's sort of what's happening here.
[2240.80 → 2245.14] And, you know, when we're in C or C++, something like that, it's very rigidly typed.
[2245.32 → 2251.58] And, like, everything has a specific storage type as well, as opposed to sort of this generic storage type like JavaScript uses.
[2252.06 → 2254.78] Then it's very hard to get this kind of corner cases.
[2254.78 → 2261.98] Because, look, if you had storage for a double, then you're always going to think of that as a double no matter what value it takes, right?
[2262.36 → 2268.20] And so you don't expect it to be able to handle anything like this because there's nothing like this that can happen.
[2268.20 → 2282.42] But when you're in a very flexible language where the type of things can kind of mutate all the time, I feel like that creates real difficulties for the compiler vendor who wants to try and make it appear as if these things are more rigidly typed.
[2282.64 → 2284.72] So this, to me, makes perfect sense.
[2285.04 → 2287.12] And, like, I can totally see why people are confused.
[2287.24 → 2291.70] But, like, yeah, that's exactly what I would expect it to do, too, is the weird behaviour.
[2291.80 → 2293.58] Because that's just like, yeah, what else do you do?
[2293.58 → 2303.62] Except special case or, like, that dude did make libraries to try and, like, special case all the things that might trip you up and try to fix them, like, ad hoc, basically, you know?
[2303.70 → 2304.64] So this seems fine.
[2305.08 → 2305.38] I'm down.
[2305.38 → 2309.78] So, Casey, something that might blow your mind is if you redo this, you put a generic on filter with number.
[2310.00 → 2315.58] So it's like, hey, I'll return a type number and then pass in a function that checks for it to not be undefined.
[2315.58 → 2323.54] Because the thing that got passed in was of type number and undefined or, like, or undefined as an array of one of those two possibilities.
[2323.54 → 2326.82] And your filter function filters out specifically undefined.
[2327.14 → 2331.08] It's able then to infer that the thing coming out is only numbers.
[2331.94 → 2332.34] Okay.
[2332.42 → 2334.64] So it was trying a little bit.
[2334.64 → 2336.24] It's like shockingly advanced kind of type checking in there.
[2336.66 → 2336.88] Yeah.
[2337.38 → 2340.26] So, you know, I mean, this is, like I said, I just, I can totally see this.
[2340.34 → 2342.60] It's just like, look, there are probably a bunch of cases like that.
[2342.60 → 2343.68] They caught some of them.
[2343.74 → 2345.30] They didn't catch others, you know?
[2345.54 → 2346.14] And so, yeah.
[2346.24 → 2349.72] So good on them for catching any, honestly, I think.
[2350.36 → 2350.76] Yeah.
[2350.84 → 2351.24] All right.
[2352.00 → 2352.88] Ready for more.
[2353.06 → 2353.36] Hold on.
[2353.40 → 2353.76] Let me see.
[2353.86 → 2354.10] Yeah.
[2354.22 → 2357.34] We're moving so slow that I'm going to have to, like, pick another one.
[2358.62 → 2359.02] Okay.
[2359.24 → 2360.16] This one's interesting.
[2360.74 → 2361.18] All right.
[2361.18 → 2368.56] So at the type level, we're going to have empty braces versus object versus lowercase object.
[2368.68 → 2370.50] And honestly, this literally trips up everybody.
[2370.50 → 2377.68] I don't think it's, like, as much of a common case anymore because people just, like, explicitly type with, like, a name or something.
[2378.42 → 2382.88] But, like, when you look at this, you kind of expect all three of those to be very similar, right?
[2383.14 → 2385.84] At least that's, like, how I react when I see something like this.
[2386.46 → 2391.28] So if we look at how TypeScript responds, so we'll just have two variables here.
[2391.36 → 2396.46] We have foo and one with lowercase object, one with empty braces, right?
[2396.46 → 2402.70] So if we do the one on the left, this one is going to – this one actually aligns with most people's mental models.
[2402.78 → 2405.46] It's going to have an object and an array, right?
[2405.46 → 2406.30] Those are both objects.
[2406.56 → 2410.72] But any primitive value will not be accepted.
[2410.88 → 2412.72] It's, you know, Booleans, null-defined strings.
[2413.12 → 2414.22] So this makes sense.
[2414.84 → 2419.30] But what's interesting, like, if people are familiar with JavaScript, empty braces represent an object, right?
[2419.30 → 2423.48] I think, like, most people would probably think it would behave the same way.
[2423.74 → 2431.18] But the interesting part is that it accepts literally everything but null or undefined.
[2431.44 → 2433.72] And that's not very intuitive when you kind of look at this.
[2433.84 → 2443.24] I actually see a lot of code bases where people just say, like, something extends empty object when they actually mean they just want something to be, like, of an object-like structure.
[2443.24 → 2448.94] But what's happening is you're literally doing numbers, Booleans, and objects, right?
[2448.98 → 2451.72] So you end up allowing way more than you want.
[2452.12 → 2459.36] So this is something that, like – this is actually a huge problem I've seen pretty much in every company I've ever been in doing this kind of syntax.
[2460.48 → 2462.30] So that's the interesting part.
[2462.46 → 2466.94] Why isn't it just only – why isn't foo just, like, only an empty object?
[2467.06 → 2472.62] Is there some sort of, like, writing about why it – like – because if you did squirrel brace, but you put one key in it,
[2472.62 → 2474.20] then it's structurally that one key.
[2474.32 → 2476.02] But once you remove it, it becomes everything.
[2476.16 → 2478.46] Why isn't it just, like, it only allows for empty objects?
[2480.04 → 2480.62] I don't know.
[2480.70 → 2482.96] You're asking the wrong – we have to look at the compiler code on that one.
[2483.02 → 2483.50] I don't know.
[2483.56 → 2485.52] I just know, like, what the like, result is.
[2486.50 → 2488.20] But, yeah, this is kind of weird.
[2488.20 → 2493.06] And I always found that to be a foot gun because, like, at face value, these all kind of look the same.
[2493.92 → 2494.18] But, yeah.
[2494.50 → 2494.96] I don't know.
[2495.06 → 2497.24] I would have to look at the compiler code and see, like, exactly why.
[2497.30 → 2502.56] Or maybe someone in the YouTube comments can explain – who's on the TypeScript team could, like, explain that.
[2502.62 → 2506.32] So this is, like, a perfect episode to be mansplained in the comments.
[2506.44 → 2506.90] Right, right.
[2507.66 → 2512.88] What's weird about it to me is more that it does – that it doesn't accept null and undefined.
[2512.88 → 2522.10] Because otherwise I'd be like, oh, well, maybe they just decided that open brace, closed brace is the shorthand for I don't know what this thing is yet.
[2522.24 → 2527.54] Like, it's just, like, I'm not – I'm just, like, telling you that this variable will exist, but I'm not going to say what it is yet.
[2527.94 → 2530.98] Which, you know, we do in other languages for sure.
[2532.36 → 2543.74] And so – but the fact that you can't make it be null or undefined makes it seem like it's, like, okay, well, we do want to say something about it, but we just don't want to say that much.
[2543.84 → 2546.60] And it's, like, what is the use case for that exactly?
[2546.78 → 2548.52] Like, why do we need that?
[2548.56 → 2550.46] So I would be interested to hear, you know.
[2550.46 → 2552.14] So we have a type for, like, the case you mentioned.
[2552.30 → 2553.24] It's called type unknown.
[2553.42 → 2554.24] It's a built-in type.
[2554.36 → 2556.14] And that's, like, if you literally don't know what it is.
[2556.20 → 2556.46] Yeah.
[2556.58 → 2561.46] And then you basically have to, like, validate at runtime what it is because we just don't know.
[2561.46 → 2564.94] We don't want you to just be, like, accessing an object if it's not an object or something.
[2565.16 → 2567.62] And this is definitely not that because you can't make it be null.
[2567.72 → 2569.96] Like, you can't decide that it's, oh, it's just not anything, right?
[2570.08 → 2570.26] You know.
[2570.36 → 2571.80] So I don't really know.
[2571.86 → 2572.60] This is pretty interesting.
[2572.98 → 2574.60] I'll be interested to see the YouTube comment on that.
[2574.96 → 2578.62] We did get one comment in chat, which does seem at least plausible.
[2578.62 → 2581.16] Thanks, Spion669.
[2581.88 → 2585.28] Null an undefined throw when you attempt property access.
[2585.48 → 2586.30] So that's what I was wondering.
[2586.74 → 2589.62] Because I think you can do, like, 42.length, right?
[2590.14 → 2593.74] Or not length, probably, but, like, 42.2 string, right?
[2593.84 → 2593.98] Right.
[2594.02 → 2594.66] Or something like that?
[2594.98 → 2597.10] Oh, because structurally it's an object still.
[2597.36 → 2600.00] Oh, its prototype is still an object at the tip pity-toff.
[2600.00 → 2600.18] Yeah.
[2600.72 → 2601.06] Okay.
[2601.56 → 2601.78] Right?
[2601.82 → 2602.22] Is that it?
[2602.28 → 2602.62] I can buy that.
[2602.74 → 2603.70] I don't know if that is.
[2603.70 → 2604.34] I can buy that.
[2604.40 → 2605.96] I don't know if that's right, but I can buy it.
[2606.44 → 2606.86] I buy it.
[2606.86 → 2607.46] I don't buy it.
[2607.46 → 2610.68] No, it's only worth what you'll pay for it, Trash.
[2611.66 → 2612.50] It seems plausible.
[2612.64 → 2613.92] Let me ask my man Claude.
[2614.12 → 2614.86] Let's see if he agrees with that.
[2614.86 → 2617.80] Because I would assume I love Squirrel Grace.
[2618.36 → 2618.98] Would be true.
[2618.98 → 2622.62] So far, this one is the first one that really does seem to earn a WTF.
[2623.22 → 2623.58] Legit.
[2623.78 → 2625.72] Like, no, like, I don't know, man.
[2625.88 → 2626.82] Like, WTF.
[2626.82 → 2629.38] Like, if you see this in code, like, probably just be like, don't do this.
[2629.44 → 2629.70] Okay.
[2629.90 → 2630.12] Yeah.
[2630.26 → 2631.14] Have, like, a good reasoning.
[2631.46 → 2631.68] All right.
[2631.70 → 2632.04] I don't know.
[2632.82 → 2633.14] Okay.
[2633.28 → 2633.60] Hold on.
[2633.64 → 2633.96] Let me see.
[2634.02 → 2634.46] Where are we at?
[2634.46 → 2636.04] I know we're getting short on time here.
[2636.04 → 2637.36] I want to...
[2637.36 → 2638.86] We're never short on time for you, brother.
[2639.00 → 2640.28] Like, take as much time as you want.
[2640.28 → 2640.40] I know.
[2640.64 → 2641.08] It's true.
[2641.08 → 2641.12] It's true.
[2641.22 → 2643.18] This is one thing I wanted to show Casey.
[2643.36 → 2646.20] So this isn't actually, like, weird type stuff.
[2646.40 → 2649.36] But this is a doom and type script that my friend Dimitri did.
[2649.72 → 2649.94] Okay.
[2649.94 → 2652.48] So this is what it took for him.
[2653.12 → 2654.00] You're going to see what...
[2654.00 → 2654.48] I mean, I'm not sure.
[2654.48 → 2655.82] Are you familiar with this or no?
[2656.04 → 2656.78] He doesn't know.
[2656.92 → 2657.38] He doesn't know.
[2657.72 → 2658.06] Okay.
[2658.12 → 2658.68] This is perfect.
[2659.32 → 2660.10] Trillion lines?
[2660.22 → 2665.26] So with three and a half trillion lines of code, which is about 177 terabytes, with 12
[2665.26 → 2670.94] days of running said code through a type checker and just being, like, mentally ill, this is
[2670.94 → 2672.66] what you're going to get in type script.
[2672.66 → 2678.32] You're going to get the first frame of doom rendered in type script.
[2678.82 → 2680.66] So this is someone doing...
[2680.66 → 2680.98] In type script types.
[2681.30 → 2681.62] Types.
[2681.62 → 2681.84] Yeah.
[2682.10 → 2682.80] Strictly through types.
[2683.38 → 2683.74] I see.
[2683.84 → 2687.88] So this is someone who basically said, look, is type script's compiler Turing complete?
[2688.12 → 2688.80] And the answer was yes.
[2688.80 → 2689.24] Exactly.
[2689.40 → 2689.80] Literally.
[2690.00 → 2690.54] Yeah, exactly.
[2690.76 → 2691.34] And they were like...
[2691.34 → 2695.72] The funny thing is at render, someone was doing type script is Turing complete, like,
[2695.72 → 2696.96] a couple of hours before mine.
[2697.36 → 2699.22] And we both referenced this.
[2699.34 → 2700.12] I was like, duh.
[2700.48 → 2701.22] Like, fell to my knees.
[2701.28 → 2701.62] No, I'm just kidding.
[2701.62 → 2703.08] But I was just like, oh, man.
[2703.36 → 2704.80] Oh, I'm a fraud.
[2705.34 → 2705.94] I'm a fraud.
[2706.12 → 2708.88] Dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun-dun.
[2708.88 → 2713.20] And last thing, last thing, and I kind of want to show you something else after this, is you can do math in
[2713.20 → 2714.56] TypeScript, right?
[2714.58 → 2719.00] So if we see, like, type foo, some, we pass in 1321, we get 34 because math, right?
[2719.84 → 2724.74] What I really wanted to show, like, the audience was, like, what does the resulting type look
[2724.74 → 2725.06] like?
[2725.18 → 2727.04] And this is how you accomplish this.
[2727.72 → 2729.62] So this is one of the cleaner implementations.
[2730.40 → 2731.60] Shout out Team Chong.
[2731.66 → 2733.68] I think he's, like, very popular in the open source community.
[2734.84 → 2736.54] So this is, like, and it's going to scroll.
[2737.66 → 2738.82] So you go like this.
[2739.86 → 2744.72] And this is what you get if you want to implement some in TypeScript.
[2745.38 → 2746.66] Ideally, no one does this.
[2746.72 → 2749.50] Like, it's more just, like, pushing the limits of TypeScript, seeing what is possible.
[2749.62 → 2751.84] Like, people have done, like, Mobile Soar and all this stuff.
[2752.56 → 2755.64] But it's just, like, crazy what you can do in the type system.
[2755.64 → 2759.88] So, like, I got really addicted to type challenges, which is, like, basically leak code for types.
[2760.32 → 2764.16] So, like, I absolutely just, like, I got tired of, like, I never was, like, a big leak code person.
[2764.44 → 2766.44] But I did do it because, like, if I was interviewing.
[2766.44 → 2772.86] But when I found out about, like, type challenges where you can basically do type challenges like this, I got, like, addicted for, like, a year.
[2773.26 → 2777.54] And I just, like, went through, like, almost, like, not, like, all of them because they get, like, pretty big brain.
[2778.06 → 2779.74] But I did, like, 100 plus.
[2779.74 → 2782.50] And I just got, this is, like, what kind of unlocked TypeScript for me.
[2782.56 → 2791.90] I was very much, like, a, I would say just a normal application developer using TypeScript, you know, just doing type, like, basic type declarations.
[2792.26 → 2798.58] But then once I started doing these, like, challenges, like, I just completely unlocked, like, a different, like, avenue in my brain.
[2798.66 → 2801.74] I was able to just do, like, gnarly stuff at the type level.
[2801.74 → 2805.26] And it was very helpful because I was helping with, like, libraries at work.
[2805.70 → 2806.48] I write libraries.
[2807.20 → 2815.54] And doing this allows me to, like, give the, quote, unquote, the best developer experience to, like, my consumers, right?
[2816.14 → 2818.46] You don't have to do stuff, like, exactly at this level.
[2818.74 → 2822.34] But you do, like, pretty insane stuff that looks like spaghetti code, and you can't read.
[2822.98 → 2828.66] So there's one thing that I think Casey's going to appreciate, which I glossed over in this.
[2828.72 → 2830.22] And this is TypeScript performance.
[2830.22 → 2832.68] So, sure, you see all this code.
[2834.34 → 2839.68] But this is a very real scenario that I'm experiencing now as we speak.
[2840.22 → 2844.78] Let's imagine we have a huge monorepo that has tons of contributors.
[2846.60 → 2848.74] You have potentially some code gen.
[2848.96 → 2851.06] You have a lot of, like, user-generated types.
[2851.82 → 2856.22] But now when you're doing your, when you're working on code base, right?
[2856.30 → 2858.32] So this is me working in my code base.
[2858.32 → 2864.14] Let's imagine this auto-suggestion taking, like, 10 seconds to appear.
[2864.78 → 2865.32] Oh.
[2865.64 → 2866.00] Right?
[2866.28 → 2874.18] Or let's imagine your build taking tens of, like, you know, like 15 plus minutes to just compile types, right?
[2874.20 → 2875.44] And that's, like, a very real scenario.
[2875.44 → 2881.76] And it's a scale not many people hit depending on, like, I don't know, the work they're doing.
[2881.76 → 2887.94] So being able to fix these performance bottlenecks is actually, like, black magic.
[2888.48 → 2891.90] I think there's maybe, I'm just going to, this is just my general observation.
[2892.02 → 2898.10] But I think there's maybe, like, I can count on my hands how many people actually know that are probably not on the like, actual core team.
[2898.10 → 2905.96] That could actually help you debug your, like, your performance and try to kind of help, like, build this.
[2906.38 → 2910.66] So what they give you is with, like, not really much documentation, you get something, like, you get, like, a tracer.
[2911.08 → 2913.24] And you get these graphs, which I'm sure you're familiar with.
[2913.66 → 2913.74] Yep.
[2913.74 → 2920.20] So what I do is I run this, and then I try my best to, like, figure out where the bottlenecks are.
[2920.40 → 2925.14] But then even when I find out what they are, it's hard to tell why it's behaving this way.
[2925.14 → 2931.14] Because when you're looking at types, you need to understand really in depth, like, you know, which types do lazy evaluation?
[2931.30 → 2932.18] Can I make this lazy?
[2933.32 → 2935.42] How does the caching work at the type level?
[2935.60 → 2941.30] Like, if I do this kind of type, is it going to cache to where, you know, I can reuse that and things are performant?
[2941.30 → 2945.64] So you have to, like, really dig super deep into these, like, really obscure things.
[2945.64 → 2947.00] And they're not documented.
[2947.50 → 2951.64] There's literally nothing really on the internet that can help you get through this.
[2952.80 → 2955.46] So this is, like, my biggest WTF right now.
[2955.56 → 2959.66] Because I asked for help on Twitter because I was, like, literally, like, at, like, my rope's end.
[2960.08 → 2962.06] And luckily some people, like, reached out to me.
[2962.16 → 2966.36] But even then it's just, like, I don't know, maybe it's, like, kind of, like, guessing at its best.
[2966.36 → 2971.84] So I'm hoping, like, eventually, like, with TS Go, we're going to use that.
[2971.94 → 2973.66] And that's going to hopefully speed up things.
[2973.88 → 2981.32] Because with Go, it's going to be significantly, I think it's, like, a 10 times performance gain, potentially, depending on how your code is written, I guess.
[2982.12 → 2983.32] Or how your code base looks.
[2983.74 → 2986.10] So this is, like, one of the big things I thought you would appreciate.
[2986.24 → 2990.96] It's just, like, I don't know how it's, like, debugging performance in some of your ecosystems.
[2990.96 → 2994.94] Where it's kind of just black magic, and you're kind of just, like, you just kind of F around and find out.
[2995.04 → 2996.54] Because that's basically what I'm doing now.
[2996.92 → 2998.50] It's, like, well, this type looks gnarly.
[2998.94 → 3005.32] Let me just, like, try different things and then run it again and see if it just got better by, like, 50 milliseconds.
[3005.54 → 3007.04] And that's basically my life right now.
[3007.48 → 3014.18] Well, a lot of times what we'll do in this kind of circumstances when we have, like, it's, like, black box performance optimization, right?
[3014.18 → 3024.12] Where you're, like, okay, I need this thing to go faster, but I have either no or very limited ability to get diagnostics from inside the box, right?
[3024.20 → 3027.10] Like, so, you know, you've got a flame graph here, but I'm imagining.
[3027.48 → 3032.16] So I'm kind of implicit in what you were saying, or at least I assumed based on what you were saying.
[3032.58 → 3038.78] If I were to hover over the parts of this flame graph, it's going to tell me, like, what function the TypeScript compiler was in.
[3038.82 → 3041.16] But it's not going to tell me, like, on behalf of whom.
[3041.16 → 3048.40] So it's not going to say, like, it's because I was compiling this type or because I was compiling this dispatch, I'm assuming.
[3048.88 → 3054.48] So what is going to happen is it's going to, this one's not showing you exactly, but it's going to give you some line numbers.
[3054.74 → 3062.66] So you're actually going to have to look at the AST version of your TypeScript code to map, like, the position to, like, your actual code.
[3062.76 → 3063.96] That's kind of handy, though.
[3064.24 → 3064.70] Yeah, yeah.
[3064.70 → 3068.16] So, like, so you have to basically look at the Acts.
[3068.16 → 3071.18] Even then, it doesn't even map one-to-one, usually, from my experience.
[3071.20 → 3072.00] Of course, yeah.
[3072.16 → 3073.10] It couldn't, right?
[3073.30 → 3073.62] Exactly.
[3073.80 → 3083.88] But even then, once you kind of figure out where it is, you have a whole other can of worms on, like, now you have to understand at the compiler level how these types are handled.
[3084.44 → 3087.28] And, like, why is this being slow versus, like, potentially another avenue?
[3087.28 → 3093.40] And those things are, like, not really said at all that I realized doing now that I'm, like, in this world.
[3094.20 → 3099.62] So this is, like, it's not something that many people can relate to until you have to do it, if that makes sense.
[3099.86 → 3100.00] Isn't this?
[3100.16 → 3106.46] And what size are we talking about here in terms of, like, I mean, because I'm guessing there is basically an interplay here.
[3106.56 → 3112.08] There's the size of the code base, but then there's also, like, the level of complexity of type things you're doing.
[3112.08 → 3119.02] So I'm imagining, like, that thing you showed before that was using, like, a number of parameters crackers at the bottom.
[3119.26 → 3119.78] I've seen those.
[3119.88 → 3125.76] They're used in C and C++ as well to make macros that take different numbers of arguments, for example.
[3127.22 → 3132.12] So I'm guessing that also it depends on how much of that kind of stuff you're doing.
[3132.20 → 3141.18] Like, if the compiler is having to churn through lots of transformations that you've told it to do, like, using that kind of type metaprogramming, basically, I'll call it for now.
[3142.08 → 3145.66] So is it basically, like, an interplay of those two things?
[3145.72 → 3149.36] Like, how much type metaprogramming do you have plus how big is the code base?
[3149.40 → 3150.88] So, like, how much are we asking it to do?
[3151.08 → 3157.78] There's, like, some weird fuzzy function of, like, if you hit too much of both of those, then you're in no man's land or?
[3158.20 → 3158.60] Exactly.
[3158.80 → 3163.56] So, like, in my experience, what I've learned so far is our problem is kind of unique.
[3163.56 → 3168.30] It's just literally the sheer number of explicit types because we use Code Gen to generate some stuff.
[3168.92 → 3172.26] But also, it's also, like you said, like, inference.
[3172.60 → 3178.50] Like, if we're having TypeScript try to figure it out, when you do that, it really bogs down TypeScript.
[3178.50 → 3183.52] So what you typically have to do is be very explicit with your types and just be, like, this is what it outputs.
[3183.64 → 3186.02] You don't need to figure it out on your own.
[3186.20 → 3189.22] Let me explicitly type the return type of this function.
[3189.66 → 3192.86] And TypeScript, like, okay, now I don't have to go in and analyze everything.
[3193.02 → 3197.36] Oh, this is going to output, like, an object with, like, these objects or these properties.
[3197.68 → 3199.22] Let me just give you an explicit type.
[3199.64 → 3200.94] And you have to kind of, like, cast.
[3201.06 → 3202.52] You do, like, as and stuff.
[3202.58 → 3203.58] And that kind of helps as well.
[3203.58 → 3207.94] But it's kind of just, like, yeah, there's, like, a lot of different quirks you can do.
[3208.12 → 3216.38] So TypeScript has the functional programming, the classic functional programming compiler problem where it's, like, a bad exponential.
[3216.76 → 3223.04] Because since you don't ever have to say what the types are of functions, it's just implied based on what the function does.
[3223.18 → 3226.96] Then if a function calls another function, calls another function, calls another function, and so on,
[3227.06 → 3232.30] you end up with this permutation of it having to, like, solve the whole chain and see, like, what would it actually be?
[3232.30 → 3233.70] TypeScript has this as well?
[3235.08 → 3236.40] So, yes.
[3236.44 → 3236.76] Okay.
[3237.06 → 3237.96] But so check this out.
[3238.02 → 3239.88] Here's, like, another thing, even outside of this.
[3239.94 → 3242.76] So let's just assume I have a type file that's, like, 60 legs big.
[3243.12 → 3244.30] Like, that's huge, right?
[3244.60 → 3244.80] Okay.
[3244.80 → 3245.58] Of just TypeScript types.
[3245.80 → 3245.94] Yeah.
[3247.24 → 3257.16] What you now need to do is you now need to slice and dice this file and have it only pertain to, like, the specific pieces of the code base that actually care about it.
[3257.16 → 3265.54] So right now, especially most people in chat probably, they probably have just, like, one big, like, file, or they have some files and they kind of just build their whole project at one time.
[3266.52 → 3273.46] But when you hit this certain kind of scale, you kind of have to slice and dice your project to only care about specific things.
[3273.46 → 3282.98] So you're not so you can, like, you basically have, like, a bunch of different processes that take, like, five seconds versus one process that takes, like, 10 minutes or something.
[3283.16 → 3283.40] I see.
[3283.40 → 3283.96] If that makes sense.
[3284.16 → 3284.42] Okay.
[3284.42 → 3291.86] So, like, in the thing with TypeScript, they basically, like, will statically just crawl your imports and look at every file.
[3292.26 → 3299.40] So, like, if you had one file that was importing, like, 10 files, TypeScript, the compiler will go and go span out to those 10 files.
[3299.56 → 3302.08] And then those 10 files are most definitely importing something.
[3302.34 → 3302.54] Right.
[3302.66 → 3304.54] So then you just end up with this huge problem.
[3304.60 → 3313.02] So you have to be very, like, surgical with, like, how you're splitting everything up because you don't want that to, like, leak in places as you need to.
[3313.02 → 3316.90] So, like, in my, so right now I'm kind of in hell because we have such a big code base.
[3316.96 → 3322.78] I have to figure out where all these little spider webs kind of span out to and kind of try to keep them in their lane.
[3323.18 → 3323.30] Yep.
[3323.60 → 3326.88] So we're kind of hoping, like, TOGO is going to save us in some aspects.
[3326.92 → 3334.86] But at the same time, like, what happens is when you hit this scale, you have to be very intentional with how you format your code base.
[3334.88 → 3337.54] Because most people are just like, ugh, glob the whole thing.
[3337.62 → 3338.04] Let's go.
[3338.18 → 3338.40] Build.
[3338.46 → 3339.34] Takes five seconds.
[3339.34 → 3342.14] Because my code base is, like, maybe 50 files.
[3342.14 → 3343.86] But, yeah, not the case for me.
[3343.96 → 3345.60] And I'm, like, feeling that pain so hard.
[3345.62 → 3346.14] You guys reinvented.
[3346.92 → 3353.90] The TypeScript world has reinvented the bad C, C++ compilation situation where you end up having to build all these modules.
[3354.82 → 3355.50] Oh, my God.
[3355.92 → 3356.92] This is crazy.
[3357.16 → 3359.16] I mean, very few projects get this big.
[3359.22 → 3363.60] So, like, to be fair, I mean, Netflix is one of the very few companies that are operating on this level.
[3363.60 → 3367.92] Do the LSP still crash pretty regularly?
[3369.26 → 3372.42] Because, like, I couldn't get TS Server to work for, like, a year straight.
[3372.90 → 3374.10] And I was just like, forget this.
[3374.24 → 3374.56] I had a slide.
[3375.24 → 3376.74] I skipped over a slide.
[3376.86 → 3380.44] But it was like, is this a TypeScript error or is my server dead?
[3382.38 → 3383.50] Let's just restart.
[3383.60 → 3385.28] Let's just restart to be sure.
[3385.38 → 3388.26] Like, I'm at the point where, like, I'm just like, is that an error?
[3388.72 → 3391.54] Let's just give that boy a restart and see what happens.
[3391.76 → 3394.28] And that's, like, the classic TypeScript experience, to be honest.
[3394.94 → 3397.10] Especially, like, when you, like, get into bigger code bases.
[3397.22 → 3399.00] But, man, it is rough.
[3399.36 → 3399.60] Question.
[3399.86 → 3406.60] Is there, like, a practical kind of set of tools you can give developers to help this problem not scale as fast?
[3406.64 → 3409.00] Like, I hate ESLint, generally speaking.
[3409.32 → 3413.10] Can you throw in some TSLint that's like, hey, you didn't explicitly type your return function.
[3413.54 → 3414.64] You must return.
[3414.76 → 3416.02] You must do that.
[3416.02 → 3420.86] Like, has there been a change where people are actually doing that at Netflix?
[3420.98 → 3422.84] Or is it still kind of like you don't have to do that?
[3424.26 → 3426.34] I don't think you do it until it's a problem.
[3426.96 → 3428.26] I think that's kind of what happens.
[3428.68 → 3430.28] I think, I mean, that's not unique to us.
[3430.30 → 3431.52] It's like everybody, right?
[3431.60 → 3432.72] It's not a problem until it is.
[3433.08 → 3433.86] You ignore it.
[3433.94 → 3437.74] And then once it's a thing, you're like, oh, man, I'm done messed up.
[3438.08 → 3438.68] But I've definitely, like.
[3438.68 → 3440.00] That's a very human experience.
[3440.04 → 3440.28] Yes.
[3440.28 → 3440.60] Yes.
[3440.94 → 3441.30] Yeah.
[3441.52 → 3442.44] Yeah, exactly.
[3442.44 → 3445.76] So, like, I'm kind of, like, slowly trying to tell people what we're experiencing.
[3446.40 → 3448.20] Like, be like, you know, just be careful.
[3448.40 → 3449.34] Be careful out there.
[3450.30 → 3450.56] But, yeah.
[3450.98 → 3456.44] It sucks because, like, like you said, like Netflix has such a unique scale that we now
[3456.44 → 3458.64] have to just care about things that no one cares about.
[3459.28 → 3460.42] It's like, ugh.
[3461.02 → 3464.18] But, you know, that's how it goes sometimes.
[3464.60 → 3464.86] But, yeah.
[3465.54 → 3466.32] That's all I got.
[3466.58 → 3467.22] That's all I got.
[3467.22 → 3469.04] Thanks, Trash.
[3471.78 → 3474.22] I mean, we weren't, like, on the script as my talk, but, dude.
[3474.74 → 3477.02] So, just to, like, backtrack to my talk.
[3477.26 → 3479.20] Like, this was my first big conference talk.
[3480.18 → 3482.04] And it was at the end of the conference.
[3482.12 → 3483.20] So, it was, like, three-day conference.
[3483.60 → 3485.68] I was at the last day, almost at the very end.
[3486.14 → 3488.12] And I was, like, terrified no one was going to come.
[3488.24 → 3490.98] But it turned out, dude, I had, like, a packed-out room.
[3491.08 → 3492.18] People were laughing at my jokes.
[3492.18 → 3492.46] Nice.
[3492.46 → 3493.84] I felt, like, so relieved.
[3493.84 → 3497.32] But beforehand, I was, like, doing stretches on stage, just trying to calm down.
[3497.72 → 3499.58] And, like, I tried to, like, meditate.
[3499.92 → 3502.00] I, like, just sat there and took, like, 10 deep breaths.
[3502.08 → 3502.58] I was, like, oh.
[3502.58 → 3505.66] Did you go to the bathroom stall and stand huge?
[3506.36 → 3507.42] Increase testosterone?
[3507.92 → 3510.48] Do all the like, power stances?
[3510.48 → 3514.28] I drank, like, 50 bottles of water on stage before my talk.
[3514.32 → 3515.42] And I had to pee so bad.
[3515.46 → 3516.00] Oh, no.
[3516.60 → 3517.92] Classic talk mistake.
[3517.92 → 3522.72] One thing I'll say is, like, I used to, like, this was probably, like, my first conference
[3522.72 → 3523.60] that was, like, multi-day.
[3523.76 → 3524.80] Like, I've been to React Miami.
[3525.52 → 3528.04] I don't think that's as big as, like, the one I went to.
[3528.36 → 3531.22] But, like, the I don't know, like, the support.
[3531.28 → 3533.98] I never felt, like, the support from, like, speaking at a conference before.
[3534.16 → 3536.12] Because usually I did, like, virtual ones because of COVID.
[3536.84 → 3538.70] And, man, it was, like, pretty eye-opening.
[3538.80 → 3544.30] Like, you know, some of the people you see online, you know, very super nice in person.
[3544.30 → 3547.56] Like, kind of just changed my perspective on the whole thing of just, like, the community,
[3547.56 → 3551.58] like, of, like, conference speakers and people that tend to go to conferences regularly.
[3552.00 → 3553.12] Kind of just, like, changed my mind.
[3553.20 → 3558.24] Like, not really about those people specifically, but more of, like, the surrounding community.
[3558.32 → 3559.10] So it was pretty nice.
[3559.16 → 3562.02] I don't know if I'll ever do it again because it was very stressful.
[3562.14 → 3564.64] Like, this was actually pretty stressful for me to do on this podcast.
[3566.00 → 3568.28] You crushed it, Trash.
[3568.60 → 3571.20] Yeah, it was nice because there was a lot of back-and-forth banter.
[3571.20 → 3572.88] So that made it, like, all worth it.
[3573.58 → 3574.92] That made it all worth it.
[3575.02 → 3575.56] I love that.
[3575.56 → 3582.22] I actually think this was really awesome because, you know, this is one of those things where,
[3582.44 → 3584.94] unless if you used it, you just don't know about any of them.
[3584.98 → 3588.82] And I think a lot of people are actually pretty surprised about what's done.
[3589.08 → 3594.72] I am going to say you didn't bring up my most hated feature of them all, which is—
[3594.72 → 3595.98] Oh, not this one again, dude.
[3596.06 → 3596.56] What is your hate?
[3596.56 → 3598.78] Literally, just go back and watch the stream, Vox.
[3598.78 → 3601.90] If you randomly go inside of it, you'll probably run into complaining about this.
[3601.90 → 3605.42] You can have—so you know how you did kind of briefly kind of get close to it?
[3605.42 → 3607.80] You know how you had number and or undefined?
[3608.80 → 3609.18] Yeah, yeah.
[3609.18 → 3610.36] Let me switch my camera so you can go over there.
[3610.36 → 3611.82] No, you're on full mode right now.
[3611.86 → 3612.58] You're full screened.
[3612.64 → 3613.38] We're not changing it.
[3613.46 → 3614.32] Oh, big trash.
[3614.44 → 3614.90] Big trash.
[3615.12 → 3619.50] You know how you can have, like, a number or undefined, or you can do number or string that's an array?
[3620.68 → 3622.04] Oh, I've seen you talk about this before.
[3622.04 → 3625.04] You can pass that into a function that only accepts string arrays.
[3625.18 → 3625.76] Yeah, yeah.
[3626.42 → 3628.28] I saw you talk about that.
[3628.36 → 3631.06] Trash, pull it up on the TypeScript Playground thing and we'll show Casey.
[3631.34 → 3632.06] Yeah, pull it up here.
[3632.08 → 3633.76] I can send you a code example if you need me to.
[3634.18 → 3635.34] This just blows—
[3635.34 → 3636.58] Just give me some pasta.
[3636.66 → 3637.26] Yeah, yeah, yeah.
[3637.26 → 3637.42] Here.
[3637.42 → 3641.20] I find this to be such a funny thing.
[3641.36 → 3642.52] Prime's cooking the pasta.
[3642.90 → 3644.74] He's boiling the water.
[3645.44 → 3646.20] He's in the kitchen.
[3646.36 → 3647.86] He's cooking up some taste of pasta.
[3648.70 → 3649.54] Salt the taste.
[3649.62 → 3650.68] Why do you share your screen?
[3650.86 → 3654.36] Just because I don't have it set up, and so we're not going to do it.
[3654.90 → 3655.54] All right.
[3655.94 → 3659.58] Trash, this is your presentation, even if it's Prime's example, okay?
[3660.06 → 3663.00] I don't remember the example exactly, but I remember watching his stream where he's like,
[3663.00 → 3664.04] What is this?
[3664.42 → 3666.02] And I feel like he's brought it up like 10 times.
[3666.02 → 3666.90] Just because I—
[3666.90 → 3668.32] That's what I'm saying, Trash.
[3668.40 → 3669.64] That's exactly what I'm saying.
[3669.80 → 3671.40] I've read it 100 times.
[3671.46 → 3673.62] If he's already at TypeScript, he brings it up, literally.
[3674.02 → 3676.50] Yeah, he's like, oh, are we talking things I hate about TypeScript?
[3676.62 → 3677.30] Oh, I've got one.
[3677.38 → 3678.02] In the back pocket.
[3678.96 → 3683.12] If they fix this in the compiler, Prime is done for.
[3683.84 → 3685.40] Right, that's the end of his streaming career.
[3685.56 → 3685.96] That's it.
[3685.96 → 3688.20] It's like there's no go-to anymore.
[3688.32 → 3688.96] There's no go-to.
[3689.04 → 3692.26] They can't fix this because it's not a thing.
[3693.00 → 3693.60] Right?
[3693.76 → 3694.74] Oh, that's what you think.
[3695.08 → 3697.40] It's a—I ran into this with logging.
[3697.52 → 3701.62] So when I was doing a bunch of logging, this is what got me, was during a logging day,
[3701.70 → 3706.64] working through a bunch of logging, and then it just—I just got—I just got really sad.
[3706.92 → 3707.20] You know?
[3708.82 → 3709.70] Here you go, Trash.
[3709.74 → 3711.04] I'm not sure how to send this to you.
[3711.54 → 3713.62] So I'm going to send it to you via Twitter DMs.
[3715.28 → 3715.60] Whoa.
[3716.42 → 3717.32] Send it to me on display.
[3717.32 → 3717.84] I don't know.
[3717.90 → 3718.46] Are we friends?
[3718.80 → 3719.64] Oh, we are friends.
[3719.70 → 3720.28] We are friends.
[3720.56 → 3721.08] Make a guest.
[3721.08 → 3722.90] I know, but then I have to go to guesting, and then I have—
[3722.90 → 3724.24] We have like five places where we're talking with them.
[3724.24 → 3725.92] You can also just post in the stand-up.
[3725.92 → 3728.06] Yeah, I'll post in the stand-up.
[3728.24 → 3728.84] There we go.
[3728.90 → 3729.86] My Discord is updating.
[3729.98 → 3731.08] It's going to take forever.
[3731.82 → 3732.90] They're compiling types.
[3733.30 → 3736.84] Also remind me to close Discord before I share my screen.
[3737.38 → 3737.62] Smart.
[3737.62 → 3739.94] I am notorious for leaking everything in existence.
[3739.94 → 3740.46] I am too.
[3740.50 → 3741.94] Discord probably was watching this.
[3742.08 → 3745.58] They probably just updated all their TypeScript to fix the problems you were saying, so they
[3745.58 → 3746.24] had to just update.
[3746.54 → 3747.16] We're on it.
[3747.20 → 3748.82] They're watching it right now, just like furious.
[3748.82 → 3749.50] Yeah, that's what I'm saying.
[3749.58 → 3751.48] They're like, oh my goodness, he's so right about ends.
[3751.58 → 3752.38] Get those out of here.
[3752.58 → 3756.40] Dude, they have been around for so long, ends.
[3756.58 → 3760.72] And the worst part is that when you do—when you first start off on TypeScript, your first
[3760.72 → 3764.18] thought is, ends are the right choice because this is what I want.
[3764.32 → 3767.44] And it takes you forever to discover you've been using them wrong.
[3767.62 → 3770.44] I feel like that is by far one of the biggest WTFs of all time.
[3770.70 → 3771.02] All right.
[3771.04 → 3771.86] What are we looking at here?
[3771.96 → 3772.90] I actually don't remember—
[3772.90 → 3773.60] Okay, just look at it.
[3773.66 → 3774.30] What is food?
[3774.36 → 3775.02] Now that I'm looking at it.
[3776.82 → 3778.18] Okay, what is bar take in?
[3778.18 → 3782.30] A number or string.
[3783.12 → 3784.44] Yeah, and what do you pass into bar?
[3785.62 → 3786.40] A string array.
[3786.58 → 3787.90] And what does bar do to the array?
[3788.14 → 3788.88] Pushes a number.
[3789.10 → 3789.84] Oh, that's right.
[3789.84 → 3792.24] Yeah, it totally—it could screw you.
[3793.20 → 3796.32] Trash, show us the type of bar afterwards.
[3796.40 → 3799.68] Yeah, what's the type of—or what's the type of foo afterwards?
[3799.78 → 3801.76] I mean, the result of bar foo, you know?
[3801.76 → 3804.18] Well, you don't assign anything.
[3806.04 → 3806.66] Oh, shoot.
[3806.76 → 3808.78] Right, so it's still just string array the whole time.
[3808.86 → 3809.50] Yeah, it's just string array.
[3810.00 → 3814.14] And that—yeah, well, foo doesn't—it doesn't return anything.
[3815.24 → 3815.80] Oh, sorry.
[3815.80 → 3817.18] Yeah, yeah, you can just look at foo, though.
[3817.28 → 3818.06] Like, what is foo?
[3818.18 → 3821.14] Foo should be a set of strings, because then you afterwards could have a function that,
[3821.14 → 3827.02] say, calls contains or includes or whatever it is on the array, and the array now has
[3827.02 → 3830.64] something that doesn't contain that function and will explode and will fly under the radar.
[3833.14 → 3834.38] So this has happened to you?
[3834.50 → 3837.48] Yeah, yeah, it happened to me on Netflix when doing the gaming stuff for logging.
[3837.94 → 3842.66] Because we have, like—we had such a crazy logging thing that if you look on my GitHub,
[3842.78 → 3848.48] there's a project called Undefined, where I take, like, one million query results from
[3848.48 → 3848.82] Congo.
[3848.92 → 3850.62] This is back when we had Congo running all gaming.
[3851.14 → 3856.56] It took a million query results from Congo, converted all of those into types, and then
[3856.56 → 3858.28] figured out all the unions to reduce all the types.
[3858.34 → 3861.78] So we had so many different types that some of the types were kind of goofy.
[3862.28 → 3865.86] So you had to, like—you knew you were going to be this collection of various unions.
[3866.18 → 3870.14] And so I'd do something to the union or have functions that take in subsets of the unions,
[3870.32 → 3872.86] not realizing it was actually even a stricter subset.
[3873.26 → 3875.68] And then would—you know, it was just very, very difficult.
[3875.86 → 3877.46] And obviously, this was a problem of my own make.
[3877.46 → 3877.48] So what did you do here?
[3877.58 → 3880.12] Are you just—did you end up just programming defensively?
[3880.34 → 3880.96] Everything, yeah, yeah.
[3880.96 → 3882.80] You just have to—you just had to be—
[3882.80 → 3885.08] Can I ask a remedial question here?
[3885.50 → 3885.72] Yeah.
[3887.38 → 3890.42] What is coast doing there?
[3890.48 → 3893.28] Because you're pushing something onto it, so it's obviously not coast.
[3893.88 → 3898.26] Casey, you just hit the funniest argument of all time in JavaScript.
[3898.44 → 3899.52] Welcome to JavaScript, buddy.
[3899.68 → 3899.98] Yeah.
[3900.26 → 3900.52] Yeah.
[3900.52 → 3904.56] That's why I said remedial, because I'm like, I'm sure this is something that's come up before.
[3904.74 → 3906.18] But, like, what—so what's the deal?
[3906.64 → 3911.40] You just can't change, like, it's reference, but you can change—you can mutate it directly.
[3911.94 → 3912.08] Right?
[3912.70 → 3919.04] So there is there—is there any way—is there any actual con—like, saying that the contents are coast,
[3919.10 → 3921.46] or can you only coast just the reference?
[3922.08 → 3923.16] At the JavaScript level, right?
[3923.16 → 3926.46] JavaScript, if you want it to be, like, purely frozen, you can do object.freeze.
[3926.66 → 3928.68] And if you want to do it at the type level, you can do, like, as coast.
[3928.80 → 3930.28] Can you do object. Freeze on an array?
[3932.22 → 3932.78] Pretty sure.
[3933.68 → 3936.26] I don't—I haven't used object. Freeze in, like, forever.
[3937.40 → 3940.66] And—and that would mean that now it would be an error.
[3940.74 → 3942.64] If anyone tries to push, it'll just be like, you can't.
[3942.64 → 3943.04] There you go.
[3943.50 → 3943.70] Yeah.
[3943.70 → 3949.16] But you can still push a frozen array into a function that mutates it.
[3950.28 → 3952.28] Well, I guess not.
[3953.58 → 3953.88] So—
[3953.88 → 3955.12] Wait, does this return something?
[3955.24 → 3956.00] I haven't used freeze in the mall.
[3956.04 → 3956.90] Does this actually return something?
[3957.66 → 3958.66] It returns a new one, I think.
[3958.66 → 3959.60] Yeah, it turns a read-only one.
[3959.70 → 3960.14] There you go.
[3962.20 → 3964.34] Okay, so A is the thing we can't push.
[3964.52 → 3965.04] There you go.
[3965.10 → 3966.34] Yeah, can you pass A in the bar?
[3966.34 → 3967.14] And, like, what's the error?
[3967.24 → 3967.98] What does the error say?
[3968.22 → 3969.30] Just so I can see.
[3971.04 → 3973.24] Does not exist on read-only string.
[3973.24 → 3974.76] Can you push A into bar?
[3974.82 → 3975.86] Or can you put A into bar?
[3975.94 → 3977.50] I can't remember if that's a thing you can do.
[3979.06 → 3979.96] Can I put A into bar?
[3979.96 → 3981.20] Can you call bar with A?
[3981.38 → 3981.76] I can't.
[3981.90 → 3984.16] No, just call A or call bar with A.
[3985.52 → 3986.42] Okay, nice, nice.
[3986.48 → 3988.34] Okay, so the read-only does go that direction.
[3988.46 → 3988.70] Perfect.
[3990.14 → 3992.14] Okay, so you can coast.
[3992.14 → 3993.82] It's just it's not that particular.
[3994.10 → 3996.56] It's not that particular syntax, but—
[3996.56 → 3997.28] That works.
[3997.62 → 3998.62] There is a question.
[3999.84 → 4000.86] That works.
[4001.74 → 4002.86] WTF, that works.
[4002.86 → 4003.36] I don't know.
[4004.32 → 4006.86] I actually didn't think that was going to work, but—
[4006.86 → 4008.64] Hold on, Trash.
[4008.84 → 4011.68] Was the LSP broken, or was it an actual error?
[4012.48 → 4014.08] I already saw you.
[4014.66 → 4015.26] Run it back.
[4015.32 → 4015.66] Run it back.
[4015.70 → 4016.40] I know, exactly.
[4016.52 → 4017.48] Let me refresh the browser.
[4017.64 → 4018.42] I don't actually know.
[4019.70 → 4021.00] Oh, dude, we just lost it.
[4021.02 → 4021.82] Okay, it's gone forever.
[4021.88 → 4022.64] I'm not typing that again.
[4023.44 → 4024.12] Yeah, for real.
[4024.54 → 4026.12] So, can I ask another question here?
[4026.12 → 4026.52] Sure.
[4026.52 → 4032.12] So, I'm assuming that this is not really—like, I'm assuming that this example is—
[4032.78 → 4032.96] It's rare.
[4034.20 → 4038.24] Well, I was going to say, it doesn't even need to have as many moving parts, right?
[4038.30 → 4040.24] Because, like, maybe it does.
[4040.92 → 4047.52] So, before you had a way of typing things, like, so, can you put number or string up in
[4047.52 → 4048.28] the original definition?
[4048.44 → 4051.72] So, it's coast foo colon number or string, and then the thing?
[4053.48 → 4054.08] As well?
[4055.40 → 4056.82] So, you want me to do this, right?
[4057.04 → 4057.88] No, I was just curious.
[4057.98 → 4059.30] So, we can say whichever types we want.
[4059.38 → 4059.76] So, okay.
[4059.86 → 4061.16] So, my question is—no, sorry.
[4061.36 → 4063.14] You don't have to—no, you don't have to do that.
[4063.44 → 4064.04] Oh, okay.
[4064.04 → 4069.76] So, would the push work even before you passed it to a thing?
[4069.86 → 4075.92] So, if you said coast foo string, and you pushed three, just with it in full sight of
[4075.92 → 4078.66] the fact that it was only supposed to be strings, what would happen?
[4080.52 → 4082.54] So, you're saying, can I do foo push one?
[4083.00 → 4083.22] Yeah.
[4083.58 → 4084.86] Oh, that should definitely work.
[4084.94 → 4085.66] That should definitely break.
[4086.90 → 4087.20] Yeah.
[4089.16 → 4090.24] Very interesting.
[4090.66 → 4090.84] Yeah.
[4091.64 → 4092.60] Very interesting.
[4094.04 → 4094.62] All right.
[4094.78 → 4097.40] Yeah, the problem is it just can't narrow it down.
[4097.72 → 4098.02] Yeah.
[4098.70 → 4100.58] It's like rectangles and squares, right?
[4100.86 → 4104.62] Foos a square, number—bar takes in a rectangle.
[4106.78 → 4109.82] This, to me, seems like a legit compiler bug.
[4109.86 → 4110.38] It's not.
[4110.46 → 4115.68] To me, because—but it does seem like one, because in this case, if what we're basically
[4115.68 → 4119.94] saying—because in order for this to make any sense logically, right, what we're saying
[4119.94 → 4123.52] here is that the or is not a type definition.
[4123.52 → 4129.42] Meaning it's not saying that I only accept number or string types, which is, A, probably
[4129.42 → 4132.30] what it should have been based on how it's compiling.
[4132.30 → 4139.58] So, it's compiling this as if what you said was, I will take only things that support number
[4139.58 → 4144.64] and string, not either or, but, you know, it can support both.
[4145.00 → 4149.34] But then what it's doing is it's actually accepting either.
[4149.34 → 4153.22] So, it's compiling as if it's and accepting as if it's or.
[4153.36 → 4154.84] That just seems like a straight-up bug.
[4155.12 → 4158.04] So, I'd love to see someone justify that, because I don't buy that.
[4158.30 → 4159.82] There are two ways you could have made this work.
[4159.92 → 4163.40] One is the first way, which is your say, that's an actual requirement.
[4163.60 → 4167.16] So, if you tried to pass the string one, it would just error and say, no, I only accept
[4167.16 → 4168.44] number or string types.
[4169.24 → 4174.94] And then the other one would be, when you actually make the call, if it actually was supposed
[4174.94 → 4179.12] to be more like a template where it says, I'll accept either or of these, then it should
[4179.12 → 4186.88] have done a compilation error check on that function as if it had just said type of string,
[4187.14 → 4191.10] which it definitely didn't do, because it would have given you an error on the push.
[4191.76 → 4192.12] Right?
[4192.56 → 4194.98] So, I'm saying, I'm calling this a bug.
[4196.00 → 4197.36] This is a bug.
[4198.12 → 4201.58] YouTube comments, I will fight you next time on this.
[4201.78 → 4202.98] This is a bug.
[4202.98 → 4207.84] You should have picked one or the other to do, and if you did neither, then it's a bug.
[4207.86 → 4208.82] Hey, guess what, TJ?
[4209.16 → 4210.94] I told you it was a good piece of content.
[4211.12 → 4214.68] TJ's over there being all upset at me for bringing up my favourite thing, being like,
[4214.72 → 4216.92] oh, here's Prime bringing up his classic thing.
[4217.18 → 4219.64] This is great, because I knew Casey would be like, what?
[4219.76 → 4220.54] I don't get this.
[4220.62 → 4221.70] What the heck's happening here?
[4221.72 → 4223.72] I'm right there with you.
[4223.90 → 4227.74] Because there were two ways you could have done this correctly, and they chose neither.
[4227.74 → 4233.48] So, I would be impressed if someone in the YouTube comments can convince me that this
[4233.48 → 4236.24] is not just a bad design.
[4236.66 → 4238.92] That this is not just a bug in the way you've defined the way.
[4238.96 → 4239.82] This is just a bug.
[4240.70 → 4245.74] Here's why they can't fix it, is because it would make JavaScript...
[4245.74 → 4250.18] That it would just break everything that they've already done in JavaScript world.
[4250.36 → 4251.38] That's the main reason.
[4251.38 → 4252.34] That's a good answer, by the way.
[4252.36 → 4257.74] It's that they had to make TypeScript incrementally adoptable for JavaScript, and that's...
[4257.74 → 4259.10] I don't see why...
[4259.10 → 4261.64] I don't see that explanation being valid here.
[4261.80 → 4263.70] It doesn't look so...
[4263.70 → 4268.58] So, in this case, the main problem is that there's no way to say whether something is going...
[4268.58 → 4273.68] There's no mutability access in the type system for TypeScript, right?
[4273.68 → 4275.68] So, there's no way to say...
[4276.32 → 4278.76] Well, there is, but not when you're writing it this way.
[4278.84 → 4282.76] There's no way to tell you, actually, I'm going to mutate the array that I'm passing.
[4283.38 → 4289.38] So, in a normal case, what you're saying is if this function takes numbers or string arrays,
[4289.98 → 4290.62] that's fine.
[4291.04 → 4293.00] It does successfully handle that case.
[4293.08 → 4298.08] That function does not break any promises of its function signature or its return type.
[4298.08 → 4309.36] The problem is there's a separate axis of it has mutated that array to now basically upgrade or, like, mutate the type itself.
[4309.48 → 4313.62] It now took something that was, you know, possibly a number array or a string array
[4313.62 → 4316.80] and turned it into either a number array or number or string array.
[4317.24 → 4319.28] But that's not tracked in the type system at all.
[4319.36 → 4320.44] I don't know why, Trash.
[4321.12 → 4321.92] Hold on, I'm coming back.
[4321.96 → 4322.42] I know, don't worry.
[4322.50 → 4325.20] I've switched the grid, so at least we don't have that as a full thing.
[4325.20 → 4326.06] But this is good.
[4326.12 → 4326.52] This is great.
[4326.70 → 4331.18] No, but, like, I went through the different cases and I had, and Trash typed them in.
[4331.42 → 4338.90] We saw, literally, that the compiler can go, oh, if I have something that's declared as only a string,
[4339.20 → 4342.66] as only an array of strings, and I try to push one, it will error, right?
[4342.98 → 4349.30] Now, what that says to me is that it actually was, it has the logic for looking at push and saying,
[4349.38 → 4350.44] if it's a string, I can't do it.
[4350.44 → 4358.00] So when you called, when someone called that function, and you said you passed a string,
[4358.20 → 4363.74] what it should have done is do the type checking on that function at that time,
[4363.86 → 4366.04] at the dispatch point, right?
[4366.08 → 4367.84] This is how template compiling works in C.
[4368.00 → 4376.10] At the dispatch point to go, could I actually have this function evaluate with this type?
[4376.10 → 4379.90] And the answer is clearly no, even if they run the code they already have in the compiler
[4379.90 → 4382.54] because we saw it error on the push code.
[4382.68 → 4384.42] So this is a bug in the compiler.
[4384.56 → 4387.94] It should have done that type checking, and it should have done, like, again,
[4388.12 → 4391.02] this is my first time seeing type strips, so maybe I'm missing something.
[4391.12 → 4393.24] But, like, no, from what I saw, this is a bug.
[4393.36 → 4397.38] This is a bug that should have been fixed because you should have done at the dispatch point
[4397.38 → 4400.50] and you should have gone, I'm instantiating one of string.
[4400.90 → 4405.48] I'm effectively instantiating your version of this function call that would be used for string.
[4405.48 → 4407.54] And I don't have to actually instantiate a new version of the function.
[4407.72 → 4410.78] I just have to do the type checking for that function, and it didn't do that.
[4411.20 → 4411.84] It should have done that.
[4412.68 → 4414.00] So fight me, YouTube.
[4415.02 → 4418.28] I would love nothing more than this bug getting fixed
[4418.28 → 4422.94] and never have to hear Prime talk about this on another podcast or stream or video again.
[4423.22 → 4425.22] So you're preaching to the choir big time.
[4425.40 → 4429.32] If there's a way that this can get fixed, I will be so happy.
[4429.44 → 4431.58] I will stand TypeScript for months.
[4431.72 → 4433.54] I will say it's a great programming language.
[4433.54 → 4436.56] TJ's positivity arc is already in there.
[4436.88 → 4437.90] It's already gone.
[4438.00 → 4441.98] Let me just illustrate, just to be clear, what I'm talking about.
[4442.06 → 4444.40] I'm trying to make a mental model of the compiler in my head, right?
[4444.74 → 4444.98] Yep.
[4445.10 → 4449.10] So when I define a function, right, I'm going to have a function,
[4449.60 → 4454.12] and 99% of the time that function is going to have an explicit type, let's say.
[4454.12 → 4457.62] So it's going to say, like he had before, I take person.
[4457.76 → 4459.18] I take type person, right?
[4459.50 → 4459.68] Yep.
[4459.94 → 4465.36] And so in that case, you can just type check the function at the time when you're actually just looking at the function.
[4465.76 → 4468.92] In other words, there's only one type check that only has to happen for this,
[4469.02 → 4471.52] and that is the type check for the type that it said it took.
[4471.52 → 4476.94] But as soon as you have an or in there, then what the compiler should have done is it should have said,
[4477.10 → 4481.40] okay, I don't know how this will be called yet, right?
[4481.58 → 4488.34] Because now one option is we could type check all permutations, string, number, and string or number.
[4488.48 → 4492.44] But the problem is as you add more of those, you could get into a thing where it's like,
[4492.52 → 4495.94] okay, we're in factorial land, and then your compile time blows up.
[4495.98 → 4496.52] So you wouldn't do that.
[4496.92 → 4500.42] All you would do is say, okay, I'm going to defer type checking of this function.
[4500.66 → 4503.08] I'm going to defer it until it's called, right?
[4503.12 → 4503.86] That's what you would do.
[4504.34 → 4508.84] You could still run a type check on it if you just want to run a type check to see if it ever could do it, right?
[4508.88 → 4513.06] Meaning if you could do the inclusive type check of like all possible things if you want to.
[4513.34 → 4514.30] You could do that if you want to.
[4514.36 → 4514.88] I don't care.
[4514.88 → 4518.60] But point being, we should put it to the side and say, okay, here's the like effectively like it's a template.
[4518.86 → 4522.84] Here's all the things that could have been called as we're just going to remember those, right?
[4522.84 → 4527.36] Then as it goes through call points, what the compiler should do is look at the call point.
[4527.62 → 4534.44] It should go, okay, do I have a cached type check for this type signature that I'm about to dispatch, right?
[4534.44 → 4541.56] If the answer is yes, then I don't need to do anything because I've already outputted the errors or not any errors if it was correct.
[4541.78 → 4547.80] If I don't have a cached version of that type combination that is passing in, I need to do the type check now.
[4547.98 → 4549.40] I do that type check.
[4549.50 → 4553.08] And if it's an error, I put the error on the dispatch point, right?
[4553.22 → 4558.22] And I say invocation of this would have created an error at this line in the function.
[4558.22 → 4563.00] Meaning the push would fail because it's pushing an integer and I only had a string array, right?
[4563.00 → 4564.78] That is what the compiler should have done.
[4564.88 → 4567.88] You would then put that in the cache so you'd never do it again.
[4567.96 → 4569.80] So it's not a performance penalty to do this, right?
[4570.36 → 4571.56] But that's how you would do it.
[4571.94 → 4574.98] And so if they're not doing that, I would argue that's a bug.
[4575.06 → 4585.62] And someone would have to explain to me why that compilation process I just described somehow creates some unworkable situation that simply won't allow us to create JavaScript anymore.
[4585.74 → 4589.96] Like you were saying, like if there's – I'm totally willing to believe there's something I don't know that's that.
[4589.96 → 4593.64] But of the things I've been shown, there's no reason that compilation model wouldn't work.
[4593.72 → 4598.84] So I would consider it a bug until someone explains to me what the secret thing is that makes this not possible.
[4598.92 → 4599.40] Does that make sense?
[4600.42 → 4602.78] Well, the code still runs.
[4603.92 → 4608.10] It's that TypeScript now lies about its types, right?
[4608.16 → 4614.80] That would be the – so I'm okay with saying it's a bug in the sense like the TypeScript compiler, right?
[4614.80 → 4622.00] It needs to either update its type or say, hey, this type is actually like becomes expanded afterwards.
[4622.40 → 4623.84] No, it doesn't need to do that at all.
[4623.98 → 4625.48] It just needs to output the error.
[4626.34 → 4632.52] Yeah, it would be fine in the case where we're explicitly typing it with saying string like array at the beginning.
[4632.52 → 4639.94] But like I'm saying, TypeScript's design is not like – has to have been from the start.
[4640.12 → 4644.68] And maybe like they could really TypeScript 6.0 and change their mind about it because now it's a very different situation.
[4644.92 → 4651.56] Was like code that runs in JavaScript, like they want it to still kind of be able to run in TypeScript land, right?
[4651.62 → 4652.36] But it will.
[4652.46 → 4653.02] It's still an array.
[4653.42 → 4653.88] But it will.
[4653.88 → 4668.68] Everything I just said, like literally nothing happens to the TypeScript compiler at all except that if you pass something that wasn't a type that could make this function compile normally, then it will produce the error, right?
[4669.36 → 4676.02] So it's literally just asking for that error to be produced when you use a dispatch that would have been illegal.
[4676.52 → 4678.18] It's not asking to mutate any types.
[4678.26 → 4678.88] Yeah, but it's not.
[4678.88 → 4681.34] I think like dispatch is probably – I don't know.
[4681.34 → 4682.94] I think like – I don't know.
[4683.00 → 4685.22] Maybe like in this case they could solve this one.
[4685.60 → 4694.20] But I don't think like exhaustively they can solve this like problem because sometimes this works.
[4694.38 → 4700.02] Like if they didn't – if they didn't – they would have to then – okay, sorry.
[4700.88 → 4705.30] There's nothing in the Type like for the function.
[4705.60 → 4709.54] There's nothing in the Type for the function that says it mutates this.
[4709.54 → 4721.02] So if you're like it needs to get expanded out like a template, and then they could check everything if it works, that would like – Trash is saying TypeScript compiler doesn't scale for them.
[4721.36 → 4729.18] Like I promise you it is doing a lot of things to avoid getting to like anywhere close to the situation where you're talking about right now.
[4729.18 → 4734.50] It is not a tenable option for them to like to make it look or act like a template.
[4734.68 → 4740.02] Like if it says it takes these things in as the type, then like that's what it has.
[4740.34 → 4742.32] I don't know if that makes sense or not.
[4742.32 → 4745.96] I mean it kind of does.
[4746.04 → 4756.34] But I mean I'm just saying that the – in the worst case scenario, then really all you're going to get is a few more compiles of this.
[4756.94 → 4757.84] I mean – okay.
[4758.06 → 4767.16] So I guess what I would say is it sounds to me like TypeScript already is not providing a – some kind of guarantee on compile time.
[4767.16 → 4768.36] There's no generics.
[4768.58 → 4772.02] The thing you're thinking of is you have this like generic picture in your head that doesn't exist.
[4772.16 → 4773.78] There's only one function that ever exists.
[4774.48 → 4779.12] And so it doesn't actually have a string version of the string number or a number version of the string number.
[4779.76 → 4780.42] It just –
[4780.42 → 4782.92] But it's not – I'm not asking it for it to change the code.
[4783.04 → 4785.16] I'm just saying it could just run the type check.
[4786.18 → 4787.16] It just has to run the type check.
[4787.16 → 4788.48] I see what you're saying, Casey.
[4788.64 → 4795.32] Like I get what you're saying because you're saying like if this was – if we imagined this more like how templates work in the sense that like it's duct typing.
[4795.32 → 4800.80] I want to see does this work for a number array, does this work for a string array, or does this work for a number or string array.
[4801.22 → 4809.64] Like I get what you're saying there, and you're saying, hey, if you passed in a pure string array, this should error because we're now going to push a number into it.
[4809.72 → 4811.42] And now you're lying about the type.
[4811.56 → 4811.68] Yeah.
[4811.80 → 4813.66] The type expanded effectively internally.
[4815.32 → 4815.68] Yes.
[4815.68 → 4818.32] Well, I'm not really saying that explicitly.
[4818.32 → 4825.36] All I'm trying to say is the existing compiler that they have already done this error checking.
[4826.18 → 4835.08] So another way to say this would be let's suppose that what you were saying was a legitimate defence of this behaviour.
[4835.24 → 4846.84] If that was the case, then the.push1 that Trash put in should have worked because your argument here, right, is that, well, I don't want to handle expanding types.
[4846.84 → 4849.42] I just want to go like, okay, if it was in JavaScript, it should work.
[4849.54 → 4851.74] So the push one should have worked everywhere.
[4852.04 → 4866.78] But the fact that the push one didn't work on something that it knew was a string is misleading to the programmer because now it's telling the programmer that what this thing does is it type checks the type you have against the functions that you're calling on that type.
[4866.78 → 4878.64] And then when a programmer goes and passes a string type to this function, they very clearly would expect that function to run the type check, which would have.push1 fail.
[4878.82 → 4881.66] Because there isn't any additional analysis that it needs to do.
[4881.74 → 4886.00] It's the exact same analysis it was already doing on the push one before.
[4886.00 → 4889.96] So what I'm saying is literally they don't even have to do any new work.
[4890.06 → 4891.92] They don't have to check any different types, nothing.
[4892.18 → 4905.32] All they have to do is when they have their or operator for types, they just have to remember, okay, I should store the fact that I haven't type checked this function completely yet.
[4905.54 → 4906.04] That's it.
[4906.30 → 4909.06] So I'll do one type check on it, which is the one I'm already doing.
[4909.06 → 4909.64] You can do it.
[4909.76 → 4915.90] The compiler stays the same currently, but I record a little thing into my table of, because, you know, it's got a table of functions and their types.
[4915.98 → 4918.68] That's the only way it can do any of the rest of the type checking it's about to do.
[4918.92 → 4920.04] So I have a table of functions and their types.
[4920.34 → 4924.74] Every time I see someone call one, what I should do is rerun the type checker.
[4924.90 → 4928.14] Now, if you're worried about compile time, you could have a flag to turn this off.
[4928.14 → 4930.80] If you're like, don't check my dispatches, right?
[4930.84 → 4932.32] You could do that if that's what you want.
[4932.32 → 4940.00] But presumably the only reason people are adding all the compile time overhead of TypeScript in the first place is because they wanted the type checking.
[4940.36 → 4948.46] So what you should at least do is have a thing that every time you have a dispatch, you go and look, have I type checked this version of the dispatch?
[4948.70 → 4951.06] And if you haven't, you just call the type checker.
[4951.62 → 4953.08] It will literally just work.
[4953.08 → 4958.36] Like, that's all you need to do is just have a little cache of what type combinations have you type checked.
[4958.48 → 4958.80] That's it.
[4958.92 → 4961.06] There's no NOR code generation, nothing.
[4961.06 → 4963.02] Like, it's the exact same compiler otherwise.
[4963.26 → 4966.36] It just calls the type checker on more permutations.
[4966.68 → 4967.22] That's it.
[4967.36 → 4970.10] No, I understand what you're saying.
[4970.58 → 4973.32] But unfortunately, we are actually out of time for this episode.
[4973.56 → 4975.38] We have to shut this down.
[4976.64 → 4977.74] This was a long one.
[4978.04 → 4979.02] Thanks, trash.
[4979.08 → 4983.22] I'll come back, Casey, with a research opinion on this.
[4983.38 → 4985.24] I was just admiring the discussion.
[4985.24 → 4990.34] I'm going hard on this one because I want an actual explanation from somebody who could tell me why.
[4990.34 → 4991.44] We can't do this.
[4991.48 → 4993.36] Like, let's go do this in the compiler tomorrow.
[4993.80 → 4994.58] That's the stream.
[4994.76 → 4996.12] We add this type checker.
[4996.24 → 4997.24] Oh, I love that.
[4997.34 → 4997.78] There we go.
[4998.02 → 4998.20] Right?
[4998.30 → 4999.26] I would love to get it fixed.
[4999.32 → 5000.06] That would make me happy.
[5000.26 → 5001.40] This is doable, people.
[5001.58 → 5002.22] This is doable.
[5002.32 → 5002.48] Yeah.
[5002.72 → 5004.18] This is doable out there.
[5004.70 → 5005.36] Let's do it.
[5005.68 → 5005.88] Yeah.
[5006.00 → 5007.20] I mean, I love this.
[5007.40 → 5008.54] We can't add any more.
[5008.92 → 5009.68] I love you, Casey.
[5009.84 → 5010.58] Love you, Trash.
[5010.64 → 5011.20] Love you, TJ.
[5011.36 → 5012.14] Well, like you, TJ.
[5012.26 → 5014.00] You're always insulting everybody over here.
[5014.00 → 5016.98] Uh, insulting me on my time script take.
[5016.98 → 5017.54] All I said was happy things today.
[5017.76 → 5017.84] What?
[5018.30 → 5020.64] Though, hey, Trash, appreciate the talk.
[5020.76 → 5021.74] Thanks for taking the time.
[5023.04 → 5023.60] Thanks, Trash.
[5023.88 → 5024.56] That was awesome.
[5025.02 → 5026.08] By the way, this is actually pretty fun.
[5026.14 → 5030.24] We should do this again because the idea of having a presentation where we're going to stop and interrupt is actually pretty cool.
[5032.42 → 5033.08] Trash, you did awesome.
[5033.08 → 5037.62] I really appreciate that you all stopped, and we started having discussions because it would have been really awkward if I was just talking.
[5040.30 → 5041.38] Because I can't see anything.
[5041.38 → 5042.16] I'm like, was that good?
[5042.22 → 5042.68] Was that funny?
[5042.76 → 5043.30] Did you like it?
[5043.34 → 5043.76] I don't know.
[5045.10 → 5046.52] Let's go fix the TypeScript compiler.
[5046.56 → 5048.66] Let's not fix the TypeScript compiler.
[5048.66 → 5049.32] Good luck, buddy.
[5049.76 → 5052.00] It will be a lot harder than you realize it will be.
[5053.46 → 5054.12] Yeah, I'm sure.
[5054.32 → 5058.58] I don't necessarily want to look at the code, but we can do this.
[5058.66 → 5059.28] This is doable.
[5059.82 → 5060.36] This is doable.
[5060.36 → 5061.36] I believe in you, Casey.
[5061.36 → 5064.66] Casey, you got this, Casey.
[5064.82 → 5065.36] All you.
[5066.82 → 5067.20] All right.
[5067.42 → 5068.30] I'll go download it.
[5068.56 → 5068.94] That was fun.
[5069.90 → 5071.40] Love the presentation, Trash.
[5071.78 → 5072.26] Thank you.
[5072.32 → 5072.66] Thank you.
[5073.18 → 5073.64] It was fun.
[5073.82 → 5074.20] It was fun.
[5074.38 → 5074.88] I enjoyed it.
[5074.88 → 5075.08] All right.
[5075.60 → 5077.12] I am rating out right now.
[5077.22 → 5077.92] I'm going to.
[5078.04 → 5078.80] Why do we have to end?
[5078.86 → 5080.64] Because I have a meeting that I have to go to now.
[5082.40 → 5082.76] So.
[5083.12 → 5083.78] Big boy, thanks.
[5083.80 → 5084.76] Bye-bye, everybody.
[5085.64 → 5087.02] Bye-bye, bye-bye, bye-bye, bye-bye.
[5087.30 → 5087.62] Thanks.
[5087.80 → 5088.40] Thanks, Trash.
[5088.40 → 5088.80] See you, everybody.
[5088.80 → 5090.18] Boot up the day.
[5091.36 → 5095.12] Vibe code and errors on my screen.
[5096.32 → 5097.94] Terminal coffee.
[5098.94 → 5102.90] And here we live in the dream.
