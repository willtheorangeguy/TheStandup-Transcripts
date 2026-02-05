[0.00 --> 10.44]  Oh nice. Oh hey. Oh hey, I'm here. Hello. Wow on time. I am like right on the dot. That's incredible.
[10.44 --> 14.16]  It's you know there's a first time for everything. Welcome to the stand up.
[14.16 --> 21.48]  So I haven't eaten anything all day yet. That's good. We got all time. We got it's the stand up.
[21.48 --> 25.98]  We can eat. No you cannot. The last time I did stand up I used to eat like toast and
[25.98 --> 30.66]  stuff in the mornings. It was great. That sounds very British. It's been like seven years ago.
[30.66 --> 36.48]  Yeah. We eat toast in America too. No no no. Only we eat toast. Don't you know this?
[36.48 --> 40.66]  We invented the concept of toast. I had toast this morning. No you didn't TJ. And basted eggs.
[40.66 --> 44.76]  No it's lies. TJ's just trying to fit in. Don't listen to him.
[44.76 --> 48.66]  Drew. Sorry. I've never had toast before. I just wanted to be part of something.
[48.66 --> 51.94]  Yep. Okay. It's okay. Don't worry.
[51.94 --> 56.12]  Yeah yeah. Yeah yeah. Yeah yeah. Yeah yeah. Yeah yeah.
[56.12 --> 62.00]  Uh anyways. Sorry. All right. Today on the stand up we have with us uh Jose Valim and
[62.00 --> 68.42]  Ginger Bill creators of Elixir and Odin respectively. Today the stand up which is streamed every day
[68.42 --> 75.44]  Wednesday at 11 and Friday at 11 a.m. Montana time. That's the best time right? Uh we are now
[75.44 --> 80.94]  let's see what is the topic again? Oh yeah. Why didn't functional programming take off? And I we
[80.94 --> 85.38]  brought on two of the greatest language experts that I could possibly convince to come on to this
[85.38 --> 92.74]  show to tell us why this did not happen. So obviously Jose you probably have a slightly
[92.74 --> 97.96]  different perspective even on that statement considering the whole Elixir thing going on
[97.96 --> 102.16]  and probably the community you're surrounded by makes it feel like functional programming
[102.16 --> 109.24]  is quite successful. If that is true. But I guess. Is that implying it's not? I mean. Well I mean.
[109.24 --> 113.42]  He just won. Hey he's in top three most loved languages prime. Yeah that's true. Neil Vim's
[113.42 --> 119.80]  number one most uh loved editor. It doesn't mean it's popular. Well it was popular though anyways
[119.80 --> 123.42]  but that's fine. Sorry I couldn't hear you over Ginger Bill typing. What is this a stand up Ginger
[123.42 --> 128.30]  Bill? Yes it is. It's a stand up. I was just typing. Sorry just a friend on Discord. That was all
[128.30 --> 135.12]  so I should just tell him to go away. Uh uh hands hands there. DCs DCs I got a billion dollar
[135.12 --> 142.12]  idea. I got a billion dollar idea. I'm listening. What if we use state-of-the-art GPT wrappers
[142.12 --> 147.40]  to monitor live streams for API keys being leaked. Isn't that a little too niche? It's pronounced
[147.40 --> 152.56]  niche. And of course not according to my lived experience it's very common to leak API keys.
[152.56 --> 157.30]  I just need you to set up a database that can handle my scale. All right all right. I'll use neon
[157.30 --> 161.56]  so it can scale up in case this happens. On the rare chance you don't get any traffic
[161.56 --> 168.66]  it'll scale down so it doesn't cost you a fortune. Oh we'll need scale. Hey Teach uh you know that
[168.66 --> 173.36]  site we made about protecting API keys? Yeah dude you were totally right. We did need to
[173.36 --> 177.44]  have a database that could handle your scale. Um people are using that to steal API keys.
[177.44 --> 185.64]  Wait Prime I didn't notice you were live. I'm not live. Yeah yeah yeah yeah yeah a special deal
[185.64 --> 193.06]  only for today for every bit you buy I'll pay you back two bits. On the plus side your database is
[193.06 --> 199.62]  still up. When traffic spikes Neon's serverless Postgres auto scales to meet demands. Without
[199.62 --> 206.08]  all that extra ops work get the free plan at neon.com. Curious like why didn't why do we have
[206.08 --> 210.86]  like as the mainstream JavaScript is kind of like seems like number one why isn't it more of a functional
[210.86 --> 223.78]  approach? All right so I do have uh some opinions on this and um if you were like well so I there are
[223.78 --> 229.48]  many thoughts so one of the thoughts so the first thing I'm going to say like if if you were part of
[229.48 --> 237.98]  the functional programming community or kind of listening involved over the last you know um
[237.98 --> 246.96]  decade or even more very frequently you would hear that functional programming won because for
[246.96 --> 255.18]  example Java would get streams or Java would get lambdas uh or languages would bring more type
[255.18 --> 261.92]  inference right a lot of ideas that I'm not sure I'm not I'm going to use the word pioneered but very
[261.92 --> 267.86]  popular very widespread in functional uh programming cycles for a long time ago right
[267.86 --> 278.26]  and so a lot of the ideas in functional programming they became mainstream right so in in that way I
[278.26 --> 286.92]  would say that uh if we if we look at functional programming as a collection of ideas as we look at
[286.92 --> 293.88]  object orientation as a collection of ideas with time we look at those things and then usually we say
[293.88 --> 299.40]  objected objected object orientation each person that you ask you get a completely different definition
[299.40 --> 308.18]  uh Alan Kay uh I believe he's the one who came with the the the the word uh object orientation and
[308.18 --> 313.02]  it's like well I when I was not thinking when I said object orientation I was not thinking about
[313.02 --> 322.34]  what C++ has uh right so I think what we did is that we looked at those things we absorbed a lot of
[322.34 --> 327.92]  concepts and a lot of ideas from them many of those concepts and those ideas they became mainstream
[327.92 --> 337.42]  and then some parts of it did not become as mainstream as everything else right so so that's
[337.42 --> 344.62]  one of the one of the things that I I think about like well we we we got a lot from functional
[344.62 --> 350.40]  programming but the other thing that I think about so I was even mentioning to to Ginger Bill like
[350.40 --> 356.56]  just before we were chatting a little bit getting to know each other that uh I'm actually I'm not sure
[356.56 --> 362.40]  like the term functional programming like saying Elixir is a functional programming language is that quite
[362.40 --> 369.08]  useful today it's like and and there is like a technical discussion a marketing discussion that we
[369.08 --> 379.04]  that we that we can can can jump into it but yeah I think I think we we we learned uh a lot of the lessons
[379.04 --> 385.92]  that we had to learn and then if you look at Go or Rust those are not object-oriented languages
[385.92 --> 393.14]  but they are not they don't say they are functional programming languages either so like we're having those
[393.14 --> 400.92]  more recent languages that are fine with like oh we can say it's systems programming but C++ is systems
[400.92 --> 405.82]  programming but they say object like so there are new languages that are fine like not necessarily
[405.82 --> 412.14]  putting a label on them on the side of functional and object-oriented and and so and that comes back
[412.14 --> 418.86]  to me like well maybe in 2025 Elixir maybe doesn't have to put the label it is functional as well
[418.86 --> 424.44]  and then if we don't put that label what it is so I'll shut up for now
[424.44 --> 433.20]  I am I'm interested to know because I I agree with I think a lot of um a lot of ideas from functional
[433.20 --> 439.62]  programming are just very mainstream ideas now that lots of people think uh like oh yeah of course every
[439.62 --> 446.94]  language has whatever that might be I'd be interested to know from both of you what saying what ideas what
[446.94 --> 451.70]  well yeah every every language has yeah no no no no no not every language that was what I was that's
[451.70 --> 457.06]  what I wanted to ask though um because there are some great ones that don't have all the functional
[457.06 --> 465.04]  tropes inside of them uh that's a setup um yeah uh but I was interested to know like from each of you
[465.04 --> 471.78]  what are what are some like ideas from functional programming that you're happy got like are sort of
[471.78 --> 480.54]  catching uh uh like popularity and some that you are surprised haven't yet ginger bill ginger bill
[480.54 --> 485.80]  you first I have to first fight define what I mean by functional programming right great uh
[485.80 --> 490.64]  that's hard problem so again as Jose was kind of saying functional programming is not really a
[490.64 --> 495.62]  very useful term you could always use the joke definition where like uh most people think first
[495.62 --> 499.76]  functional they go it's pure functional programming where you must have stateless and no side effects
[499.76 --> 504.16]  and the reason why it has never caught on is because when I push a button that's a side effect
[504.16 --> 509.76]  so therefore functional programming useless right that that that's the joke answer but um
[509.76 --> 517.16]  the thing is the functional thing is like is it does it mean declarative programming that's like also
[517.16 --> 522.16]  oriented around like functions as functions is a first class thing you can pass functions around all
[522.16 --> 526.84]  you all you like and those functions also may have state associated so the closures and such
[526.84 --> 532.08]  so is it like oh is that what is functional programming fundamentally and if that's the case
[532.08 --> 537.92]  all object-oriented programming languages are functional right because what is an what is it
[537.92 --> 541.88]  actually what is a closure closure is an object right it's got state and an operation
[541.88 --> 547.64]  i'm not trying to say that is the case i'm just kind of saying like this term functional is getting a
[547.64 --> 552.58]  bit weird but again many people just think it's haskell and i don't know if some people would agree
[552.58 --> 558.04]  but there's a reason why haskell never took off why it is effective just it's just it's effectively a
[558.04 --> 563.86]  research project at the end of the day um it is mostly a pure pure functional language and as the
[563.86 --> 567.50]  joke kind of suggests it is kind of difficult if you want to do anything you mutating date and a lot
[567.50 --> 573.82]  you taking state and a lot of programs are fundamentally want to do that and also haskell is kind of a
[573.82 --> 578.24]  search project so has everything in it including the kitchen sink and your mother's dress or i don't
[578.24 --> 585.60]  know everything in it and it's just it does too much so it's really sometimes hard to read it and the
[585.60 --> 590.44]  people who enjoy it are usually so high iq i'm like i i don't understand anything you've just written
[590.44 --> 597.58]  i'm sorry um it's too complicated so it's kind of okay what features do i think accomplish well i already
[597.58 --> 603.90]  think closures are everywhere right every single language has got closures but um and then there's
[603.90 --> 610.20]  also obviously the immutability aspect which i don't necessarily think is good or bad it is depends
[610.20 --> 620.84]  on what you're doing right but to pass it on to jose again um yeah so uh you uh before you said that
[620.84 --> 627.42]  erlang is your favorite uh functional programming language yeah so what do you like about erlang i think
[627.42 --> 632.22]  that's a good and i i'm asking it because i would love to see like if the parts that you like
[632.22 --> 641.28]  are they what people would classify as a functional part or you know uh yeah there's another way of
[641.28 --> 647.88]  phrasing this um erlang is also my favorite oop language which is going to sound bizarre but the
[647.88 --> 652.96]  reason why i'm saying that is erlang is clearly got its its concurrency model is better describes like
[652.96 --> 659.22]  csp right you've got processes csp for people know um it's called communication sequential processing
[659.22 --> 664.82]  so you have processes which is just think of as a generalized thread green threads is another way of
[664.82 --> 669.12]  calling them uh this is what go routines are in go they're the same thing right at the end of the day
[669.12 --> 675.48]  and then you communicate them by sending messages cross them so in go they have channels in erlang you've
[675.48 --> 681.24]  got like the send and receive kind of operations um and the same with elixir as well don't you've got
[681.24 --> 687.14]  the send off the functions and then the receive blocks and such um and that kind of aspect there
[687.14 --> 692.20]  is is very and then everything's immutable by default as well so when everything is passage when you're
[692.20 --> 700.06]  passing all the messages there is immutability and also memory safety on a per process basis
[700.06 --> 705.98]  um so this is kind of a very nice way of dealing with things um a lot of other functional languages who
[705.98 --> 712.18]  are trying to deal with ideas of concurrency and such try and do other approaches and i personally
[712.18 --> 717.52]  don't like them that much um those kind of models i do like the csp style again while i go does
[717.52 --> 723.24]  the only problem is this it requires a very heavy run time and it doesn't really scale if you want to
[723.24 --> 728.82]  start then doing manual memory management like in odin so then you have to think ah damn it i can't have
[728.82 --> 741.26]  luxury yeah so to me the the the beautiful thing about erlang is that so we are talking about those
[741.26 --> 747.54]  things about well you know like uh functional well so if you take a functional programming language there
[747.54 --> 751.68]  are a couple things some people are going to say that a type system is kind of a requirement like
[751.68 --> 757.08]  having a hindler miller or similar type system is a requirement for being functional it's a separate
[757.08 --> 762.66]  discussion but if you get like the things that make a programming language functional like
[762.66 --> 770.10]  immutability pattern matching when they were designing erlang they didn't start with that
[770.10 --> 777.04]  they didn't say look we we want uh we want pattern matching we want immutability what they started was
[777.04 --> 785.54]  well we have to build a concurrent distributed reliable system and then they realized that well
[785.54 --> 792.18]  if we have if we have so for concurrency we need to have many things running at the same time
[792.18 --> 797.34]  processes right so you have all those processes which for those who are not familiar when we say
[797.34 --> 803.76]  process in erlang is lightweight threads of executions like go routines right so we have millions of those
[803.76 --> 808.56]  all running at the same time and then they realized that well if those things they have shared state
[808.56 --> 816.08]  if one of them break down maybe it broke down maybe something went wrong while it was
[816.08 --> 822.06]  mutating the shared state which means that now you have polluted state in your system
[822.06 --> 828.94]  and which may break all the other process so they were like well shared state in this case is going to
[828.94 --> 834.50]  get in the way of building a fault tolerant system because if you have a failure you can no longer trust that
[834.50 --> 840.04]  shared state right so so it's one of the things that keep going back like to discussions with the
[840.04 --> 844.48]  erlang team like people are like oh were you trying to do like function or like they're like no we wanted
[844.48 --> 850.52]  to build a resilient robust system and it just turned out that for the kind of system we wanted to build
[850.52 --> 858.96]  immutability was really essential and that's why it's immutable and people and for me like i had i had
[858.96 --> 866.60]  the opposite kind of introduction where i wanted to build concurrent software and i was doing ruby
[866.60 --> 872.60]  running into a lot of mutability issues and then i learned functional programming and then i was like
[872.60 --> 880.38]  oh immutability so for me like for me the thing that defines functional programming is immutability that's my
[880.38 --> 888.54]  interpretation right that's because that's what attracted me right but and then i ended up with erlang but
[888.54 --> 893.46]  you know they did not add immutability to be functional so i think those discussions are very
[893.46 --> 900.90]  interesting so so could an object-oriented style language like old java if it just was immutable like
[900.90 --> 908.76]  everything you passed around was copied wholesale would that be considered functional then well so
[908.76 --> 918.50]  okay a couple things did you know i'm going to regret saying this the first version of elixir which is
[918.50 --> 925.22]  was actually object-oriented i was trying to build like i was like coming from this object-oriented
[925.22 --> 931.66]  world like well what if i can have all those things it was not good for many reasons right but to your
[931.66 --> 938.22]  question to me it's like would it be a functional programming language well according to my criteria
[938.22 --> 944.34]  it it would it would it would it would it would be if that's my only criteria right
[944.34 --> 952.94]  but here is what i think about this so why do i like immutability for two reasons it makes the code easier to
[952.94 --> 959.06]  understand for me it's like well if i'm calling something and i know that that thing is not going to change
[959.06 --> 966.78]  somewhere in memory far away right i know that anything it needs if i have a piece of code and everything that it
[966.78 --> 972.68]  needs to function i give it as an input and it returns as output that code is clear to understand
[972.68 --> 977.96]  i know you know like joe armstrong one of the creators of verlang he was used to say like object
[977.96 --> 983.80]  orientation is like you think you are holding a banana but then you are holding the gorilla that is
[983.80 --> 988.28]  you're also holding the gorilla that is holding the banana and then the whole forest that the gorilla is
[988.28 --> 992.48]  in because you know you can call something but that thing can connect to the whole world and you just
[992.48 --> 998.10]  don't know so so to me that's one of the big benefits and the other one was concurrency right
[998.10 --> 1003.16]  if you have concurrency if you're building a concurrent system and you're not changing the same
[1003.16 --> 1008.58]  place in memory all the data races disappear and then there are languages like rust that already gives
[1008.58 --> 1014.62]  those benefits right through the type system where you can kind of like track the mutations and so you
[1014.62 --> 1021.24]  know according to my criteria i wouldn't say that rust is functional but according to the criteria that i set
[1021.24 --> 1028.40]  for myself of i like immutability and what are the properties i get from it i i should be happy with rust and
[1028.40 --> 1033.38]  what rust is offering because it's offering those similar properties but through different mechanism
[1033.38 --> 1041.44]  i wanted to ask actually about rust because uh i know like a lot of like josé you came from the ruby
[1041.44 --> 1047.46]  community and there was kind of i feel like kind of a big you know uh like parting of ways for some some
[1047.46 --> 1052.60]  people stayed in ruby some people went elixir and some people went rust like i'm interested to hear a
[1052.60 --> 1058.84]  little bit about like your perspective from as that was happening uh and like your thoughts on rust as a
[1058.84 --> 1063.04]  community where it's going if you want to share and then ginger bill i want to hear you rant about rust too
[1063.04 --> 1069.84]  i would love both i love both of these things yeah honestly i don't have a lot of opinions to be
[1069.84 --> 1077.12]  very honest nobody's listening nobody's listening you can tell us the truth here no i'm not i'm not
[1077.12 --> 1083.96]  trying to to to i just i have very limited experience don't follow it so i think we can
[1083.96 --> 1091.54]  jump straight to the rant wait hold on before we do that what why why was the ruby to rust pipeline
[1091.54 --> 1096.24]  even a thing because i've heard about this too that a bunch of rubyists went from ruby to rust like
[1096.24 --> 1101.72]  what because they don't strike me as super similar languages ruby seems fairly productive and
[1101.72 --> 1108.68]  rust it's like i don't quite understand like that like it just seems like a very bizarre pipeline
[1108.68 --> 1114.18]  right like i totally get c++ to rust because you're like oh i hate that language right and then you go
[1114.18 --> 1119.18]  and you do something different and you're like this fixes everything i hate about it or you claim to fix
[1119.18 --> 1123.12]  everything you hate about it i get that but i just i've never understood the ruby isn't it i would
[1123.12 --> 1126.74]  have just said the ruby people just hated python that much that they went i'll try anything but
[1126.74 --> 1134.84]  python oh okay that's reasonable yeah that's my guess actually right because um yeah that's usually
[1134.84 --> 1139.20]  what i find out when people like oh big ruby fans are going on i hate python so much and vice versa
[1139.20 --> 1144.84]  right oh so it's not that they're ruby fans they're just anti-python fans yes i think that's the case
[1144.84 --> 1154.48]  yeah so so okay so let me ask kind of um i don't know if this is true and then you hear it right so
[1154.48 --> 1160.78]  i heard i heard that a lot of people went from python to go for example yeah i saw that so why why would
[1160.78 --> 1166.22]  you think that happened and i'm just wondering if you have any thoughts because i don't think it's as
[1166.22 --> 1173.82]  drastic as going i think python and go are definitely closer than than ruby and rust and i think yeah most
[1173.82 --> 1178.38]  would agree with that but but why would you think somebody who is programming in python they're like
[1178.38 --> 1183.46]  okay i'm going to do go now i i actually have a pretty good answer for that one but ginger i i do
[1183.46 --> 1187.92]  want to hear yours first just because you're much my answer is probably similar to yours mine was
[1187.92 --> 1194.70]  like rob pike was a rob pike and ken thompson and uh robert griezmann who all created go mostly
[1194.70 --> 1198.48]  robert griezmann's main person not rob pike but they all made it because they're making super sports
[1198.48 --> 1201.90]  alternative and they thought that they were going to attract those people and then they were really
[1201.90 --> 1206.72]  surprised when the python people and stuff were coming to go i think it's mainly because people
[1206.72 --> 1212.22]  wanted backends on their servers and they wanted something that was simple language and fast and
[1212.22 --> 1218.02]  compiled and type statically typed as well pretty much and the if when you actually narrow that down
[1218.02 --> 1224.16]  you actually just get go or java um java is not compiled you know but i mean like they're the two
[1224.16 --> 1229.68]  options and i bet many of them also have been bit in the ass by using java before so they went okay go is
[1229.68 --> 1235.52]  actually it's that so my story is pretty similar we went from a python shop to a go shop in 2012
[1235.52 --> 1242.46]  and a huge and a huge amount of it was uh just because we're doing uh interning uh or string and
[1242.46 --> 1249.02]  turning on on the server and python just just stinks at you know at that whole thing so we're just like
[1249.02 --> 1254.76]  boom use go and so to me it was all about the fact that back then gay was really really popular
[1254.76 --> 1261.14]  google app engine so like either you like you were you're going from gay python to gay go and like
[1261.14 --> 1265.96]  that was the that was the big move there and it was for free practically you could have all the same
[1265.96 --> 1269.60]  data storage you could have all the same libraries you could have everything you could just transfer
[1269.60 --> 1274.04]  straight i just always wanted to say that but you could you could transfer all straight across
[1274.04 --> 1279.32]  uh with just go and you could go from python to go and it was like it was actually super amazing
[1279.32 --> 1285.12]  i also said interning which is not the correct term in my brain i'm just thinking interns
[1285.12 --> 1290.52]  but that is not the uh well string and turning i think like you just don't make any multiple copies
[1290.52 --> 1294.82]  of the string so you can then just keep bringing them back no no i i meant kerning in my head
[1294.82 --> 1301.10]  i said interning string kerning and he was so excited to make the second joke that he literally
[1301.10 --> 1307.54]  i fumbled the bag for the gay python i just always want to say that i have had no reason to say
[1307.54 --> 1314.12]  google app engine in the last 10 years okay i even forgot that even existed until you wrote yes
[1314.12 --> 1319.26]  and so google that's to me that's actually where a lot of these these python shops went from is they're
[1319.26 --> 1324.04]  like oh i could have all like i could literally have everything for free that i already have but
[1324.04 --> 1330.70]  just use go instead yes so let's do it and also go had a brilliant again at the time a brilliant
[1330.70 --> 1335.76]  just like web server built in straight away done and it just worked and it just worked and scaled
[1335.76 --> 1339.80]  well as well it was like much better than python so everything like oh python pico as well we just
[1339.80 --> 1345.28]  have to learn about be at static typing and then off you off the races you're there um so i can
[1345.28 --> 1349.70]  understand it completely understand why but i find it still funny that the go creators were surprised
[1349.70 --> 1356.04]  that they attracted python people and not the c and c plus programmers yeah i'm surprised that they
[1356.04 --> 1362.50]  thought that was surprising i meant yeah so i i would say going back to the original question i would say
[1362.50 --> 1368.40]  i would i would imagine that a lot of that was like the the ruby what what bill said you know like
[1368.40 --> 1374.86]  you know maybe you're doing ruby and every programming language has its pitfalls right and then at some
[1374.86 --> 1380.90]  point you're like well i want i don't want to be beaten by those kind of bugs i want better performance
[1380.90 --> 1390.00]  right and then i i think community also plays like a big factor you can see like the the ruby community
[1390.00 --> 1396.56]  was always like very grassroots like one of my favorite events uh in general programming language
[1396.56 --> 1403.86]  events is like eruko where uh the way it works is that every year they present uh the conference
[1403.86 --> 1410.86]  happens in a different european city and then at that event people and most often people who have not
[1410.86 --> 1417.00]  never organized an event in their entire life they say hey next year it should come it should happen at
[1417.00 --> 1422.66]  my city so they go they do a five minutes presentation people vote and then you have
[1422.66 --> 1428.96]  these people they have a gong that they always pass between events so it always felt like yeah so it's
[1428.96 --> 1435.40]  very nice like very grassroots very community involved so i think all those things like so technically
[1435.40 --> 1440.44]  may not be different right but like in terms of community there may be a lot of similarities and
[1440.44 --> 1447.24]  people who wanted something different on wanted other types of guarantees they they they would
[1447.24 --> 1455.02]  they would you know just uh try something else and and and i don't know like because i've been like
[1455.02 --> 1460.54]  mostly part of like two communities like really part of two communities in my life one was the ruby
[1460.54 --> 1467.08]  one and then the other one was the erlang and elixir one and and it's kind of hard for me to assess
[1467.08 --> 1473.80]  what is the the what is the elixir community because i play an important role in there so i don't know
[1473.80 --> 1481.38]  if i can do that job right but uh for ruby it at the time when i was involved and it was 15 years ago
[1481.38 --> 1492.92]  it was a very open community to ideas like any kind of idea people would try it out and sometimes to
[1492.92 --> 1498.12]  that can be a negative right like sometimes you need to have a filter right and not just try
[1498.12 --> 1503.80]  everything but very open to ideas especially when it came up like everything that was happening agile
[1503.80 --> 1510.54]  at the time right like people moving away from java so all that led to a community of people who just
[1510.54 --> 1517.84]  want to experiment and try out and i think all those things led to well like a lot of people going to
[1517.84 --> 1523.78]  elixir going to rust because i feel like a lot of them they are movers you know they are early
[1523.78 --> 1529.32]  adopters they are going to move anyway uh it was never necessarily meant to be a long stay
[1529.32 --> 1536.80]  uh we're still missing that ginger bill rant about rust do you have anything you want to say
[1536.80 --> 1540.84]  was just gonna say that i'm like you're not getting out of this yeah what am i what am i
[1540.84 --> 1544.80]  ranting about again exactly about rust anything anything you want to say
[1544.80 --> 1549.80]  it's the standard i mean i don't have to you know what i'm gonna be polite to rust programmers
[1549.80 --> 1556.24]  so i'll try my best not to be too in too insulting but i was if we go talk about the topic try and
[1556.24 --> 1561.82]  keep it on topic right um i would actually say rust is an ml in disguise pretending to be a c plus plus
[1561.82 --> 1568.02]  right true because if you look at it how its semantics works you've got all again not ignoring
[1568.02 --> 1572.08]  like the ownership semantics and lifetime semantics can be like ownership semantics bean and i find
[1572.08 --> 1575.12]  some sort of cruel type system right there's there's the nerdy shit just to get out there
[1575.12 --> 1580.02]  so apologize for my language and um well it's got all there and many semantics are there you've got
[1580.02 --> 1583.48]  all the pattern matching all that it's very ml like and then they've just gave it curly braces
[1583.48 --> 1588.68]  to make it feel more at home for the people who are used to the c plus plus and in many ways rust
[1588.68 --> 1593.80]  as you know the creation of rust is because of the people um who are using like modern c plus plus
[1593.80 --> 1597.68]  wanted something better because unfortunately with modern c plus you've got all the backwards
[1597.68 --> 1604.02]  compatibility of c and the other c plus plus stuff so rust is fundamentally in my view uh the
[1604.02 --> 1611.84]  an incarnation of what modern c plus plus tries to be plus all of the functional aspects of it as well
[1611.84 --> 1618.22]  my issue that's the reason why i don't like rust either uh i absolutely hate modern c plus plus i went
[1618.22 --> 1622.66]  through my phase of one c plus plus what like when when c plus plus 11 was coming out and just before
[1622.66 --> 1628.72]  that as well and i went through that entire phase oh can we can i just interrupt you is is it even
[1628.72 --> 1636.48]  fair to call c plus plus 11 modern c plus plus no that was modern c plus plus compared to before right
[1636.48 --> 1641.14]  okay okay right because you got to remember c was before that they had the next time was like c plus
[1641.14 --> 1649.24]  plus 03 and stuff like that and c plus plus 11 was like the big change at the time right it was showing
[1649.24 --> 1652.66]  all the brand new features they had all the ownership semantics the better into template
[1652.66 --> 1660.56]  improvements their s s for a improvements the new like smart pointers the uh all these new features
[1660.56 --> 1666.78]  which made it modern if you know what i mean right quote unquote modern um so in that sense that's what
[1666.78 --> 1672.70]  i would again saying c plus plus is modern very hard to say but you know i mean that's what they were
[1672.70 --> 1677.82]  trying to say but this thing is that's the reason why i don't like rust is fundamentally it feels like
[1677.82 --> 1683.44]  that and that's made i don't want to ever go back to that style of programming because i was actually
[1683.44 --> 1690.06]  typing more than i needed it was less productive um it just wasn't i wasn't getting stuff done
[1690.06 --> 1695.26]  is the best way of putting it so you're saying there's a lot of ceremony in the rust in the rust
[1695.26 --> 1701.62]  yeah yeah exactly yeah a lot of ceremony there's a lot of pardon for my language but i like using the
[1701.62 --> 1705.50]  phrase because it's the best way of explaining it but type masturbation yep i love that um
[1705.50 --> 1710.38]  um because it's literally you're doing something and you're not actually getting anything out of
[1710.38 --> 1714.98]  it now it's not as bad as sometimes the typescript stuff i've seen with the lm lm generated stuff oh
[1714.98 --> 1720.56]  my god that's horrific but the rust stuff is kind of like that's where people are going down the line
[1720.56 --> 1725.54]  and then you've got also the the macros on top in rust and it makes me laugh because the very first
[1725.54 --> 1729.06]  thing you ever write in rust it's like hello world right and the first thing you have to do when you do
[1729.06 --> 1735.52]  a print is a macro you don't know it at the time but this weird exclamation mark and then has anyone's
[1735.52 --> 1742.64]  ever actually looked at how the print macro works in rust just go look at it and then tell me you you
[1742.64 --> 1751.34]  are sane after reading it it's one of those where it's like i think they've got a problem here and if
[1751.34 --> 1755.48]  they think this is sane just to make a print but then people say no no we need it to be this case
[1755.48 --> 1759.94]  and i'm like look i'm pragmatic i would just add all that into the compiler directly i would have
[1759.94 --> 1765.50]  just said no don't make a generic macro just just just do the thing that this like that's very common
[1765.50 --> 1772.08]  if you if your if your type system isn't clever enough don't make a macro for it please but i think
[1772.08 --> 1775.72]  that's just my main criticism like i'm not criticizing people who use it if it's great for you great
[1775.72 --> 1785.42]  i just don't like using it at all okay so i have so many questions it's hard to just put
[1785.42 --> 1789.18]  them all together because i want to get jose in here because you also in elixir there's also
[1789.18 --> 1795.84]  some macro magic that you can kind of get on and so what why why macros why macros but i'm coming
[1795.84 --> 1801.90]  back for you bill with with some rust questions okay you didn't get out i want i want to go to bill
[1801.90 --> 1807.92]  and ask about macros first okay and then we can go back to elixir so tell me more like i think i
[1807.92 --> 1815.96]  already got part of your criticism about uh about macros and if i understand correctly part of it is
[1815.96 --> 1822.02]  well the reason why it has to be a macro is because of the type system and you have to make the type
[1822.02 --> 1828.84]  system satisfied one of the ways you basically have two options you make that print thing a special
[1828.84 --> 1834.66]  property of the language that the type system is going to be aware you special case it that's one way
[1834.66 --> 1839.90]  they went the macro route but is there anything else like uh when when you're thinking about
[1839.90 --> 1848.04]  macros is there uh are you like do you think there can be good macros you are there's that's the same
[1848.04 --> 1855.40]  right like necessarily against macros per se is there implementation of macros like yeah i'm just
[1855.40 --> 1859.66]  saying if you have a macro system you shouldn't do rust is it's not the way of the rust should do it
[1859.66 --> 1863.52]  um i know elixir's got it especially you've got the st modification stuff which again which is an
[1863.52 --> 1872.14]  erlang obviously um but i'm trying to weigh a phrase in this um macros are used if you're if
[1872.14 --> 1878.10]  you're having to use macros it's usually not always usually a sign of a deficiency in the language itself
[1878.10 --> 1883.46]  um like there's something missing in the language like if you keep going to using this macro all the
[1883.46 --> 1888.96]  time it's like hmm there's something missing in this language that i'm actually compensating with
[1888.96 --> 1894.14]  the same with c right the reason why c has lasted over 50 years is because of the macros as the
[1894.14 --> 1901.16]  pre-processor if you didn't have that um c i don't think c would be used anymore like it's there because
[1901.16 --> 1906.48]  it's a it gets around the deficiencies of language it gets me to do bodges makes you fix things that
[1906.48 --> 1911.84]  are missing and all this lot um and that i'm not saying that's a good thing or a bad thing it's just
[1911.84 --> 1917.96]  more of a sign of there's something missing i don't know if it makes any sense i love that and the
[1917.96 --> 1923.20]  reason why i love that so one there is that saying which is uh every programming language has at
[1923.20 --> 1928.84]  least one flaw either they either they have macros macros or they don't have macros right it's at
[1928.84 --> 1937.28]  least right so the reason i i the reason i really like what you said is because in elixir is the reason
[1937.28 --> 1944.84]  why we have macros is because i was like look i have to build this programming language and yes a
[1944.84 --> 1950.30]  programming language is a bunch of special definitions like you know a bunch of keywords so i was like
[1950.30 --> 1958.00]  well instead of hard coding all those things as part of my compiler i want to come up with these smaller
[1958.00 --> 1966.84]  subset of syntax and compiler code and have that as my foundation so macros are there so in elixir
[1966.84 --> 1973.38]  we have very few keywords like death module death none of those things are keywords those are regular
[1973.38 --> 1981.18]  macros and that was the design principle so like and and i'm not saying like you're wrong but i'm just
[1981.18 --> 1999.02]  like you know like it's very interesting like it's like it's a lot of like so so for me it's like it's
[1999.02 --> 2005.60]  very fascinating because yeah for us it's meant to be a feature right there is also the other aspect
[2005.60 --> 2010.84]  right and this is the issue with like a lot of metaprogramming in general is um how do i debug
[2010.84 --> 2019.22]  those macros macro compile time print statements next question yes you're tracing i don't can't put
[2019.22 --> 2023.16]  them into a debugger this is actually um something that's changed my mind because when i was creating
[2023.16 --> 2028.48]  odin i was going to have some form of like compile time execution so i could then inspect like the ast
[2028.48 --> 2031.42]  and do all this do all the magical stuff similar to what like what jonathan blow was doing with his
[2031.42 --> 2035.44]  language and then as i came on i never implemented it because i kept finding like i never
[2035.44 --> 2039.70]  kind of really needed it but then as i was realizing when i didn't need it it was very much like when i
[2039.70 --> 2042.68]  was set down okay i'm going to do this and then it was literally the first thing before i even typed
[2042.68 --> 2046.68]  to him wait a minute how am i going to put this to a debugger because i'm like live my life in a
[2046.68 --> 2056.24]  debugger really um and the answer is oh yeah that's gonna be difficult um because this is actually the
[2056.24 --> 2059.92]  hot this is really the biggest issue a lot of people love all this fancy compile time execution
[2059.92 --> 2063.82]  and they forget you know you can just write a program that writes a program right and you can just
[2063.82 --> 2070.74]  debug that meta program like any other program yes it's not as all one unified thing makes it all
[2070.74 --> 2075.58]  feel magical but also you know that meta program usually has to be run once in a blue moon and then
[2075.58 --> 2079.88]  you can carry on it doesn't have to be run every single time like other meta programming tools usually
[2079.88 --> 2084.02]  are and then they usually have to rely on caching if they've got caching and all this and it's just
[2084.02 --> 2089.96]  it's i i find it funny because a lot of people saying you just brought the printf debugging thing as a
[2089.96 --> 2095.28]  joke but i think a lot of people just only do printf debugging like that's all they do they don't
[2095.28 --> 2101.14]  even know that you can open up it like a a debugger like again rad debug is a brand new one you can
[2101.14 --> 2108.52]  out there or mdbg or visual studio or any of these visual ones i hate just gdb so much but um
[2108.52 --> 2114.52]  i am a printf debugger and i'm happy i'm proud yeah yeah this is the thing but i'm like i don't even
[2114.52 --> 2117.90]  know how my program other people's programs work and like how are you not just stepping through the
[2117.90 --> 2122.94]  like the statements or the instructions and going like that's how it works i know how it works now
[2122.94 --> 2129.04]  because i've just seen how the state is evolving um yeah i understand the printf like i do tracing as
[2129.04 --> 2134.14]  well right tracing is useful when you when you work in a compiler because you've got all these flows and
[2134.14 --> 2137.68]  you want to know how it goes through the flows and that tracing is a brilliant thing but if you're not
[2137.68 --> 2142.32]  kind of doing compiler work really like that maybe it works i'm in a debugger all the time
[2142.32 --> 2150.14]  yeah and that's there you go there's my little rant uh yes yeah so the thing about like macro
[2150.14 --> 2157.04]  execution and how you're going to debug macros and and that's going to be different per programming
[2157.04 --> 2163.34]  language uh maybe we can talk later about zig comp time i don't know if you have thoughts
[2163.34 --> 2169.82]  my criticism applied the same as that it's the same problem right okay yeah so but in elixir like
[2169.82 --> 2175.60]  there is really no difference between compile time and runtime so literally everything that you can
[2175.60 --> 2183.92]  use to debug a program at runtime you can also do it at compile time yes and so there is no distinction
[2183.92 --> 2191.58]  so uh you know yeah that's the benefit of what my complaint is made with compiled static languages rather
[2191.58 --> 2199.80]  than yes a dynamic language rang on like vm like beam obviously um but there's because in those
[2199.80 --> 2203.32]  languages when you're in a more dynamic language again in a vm language you have these abilities
[2203.32 --> 2208.44]  to introspect at runtime and insert code and if it's again the beam is effectively injected it's
[2208.44 --> 2212.72]  set effectively so everything is you've got that beauty that you can use the same tools because there is
[2212.72 --> 2218.64]  no real distinction between this compile time state and the runtime state anymore it's all runtime as
[2218.64 --> 2225.94]  you say the compile time state is mainly um the very very basics if you know what i mean the basic
[2225.94 --> 2234.10]  type checking before it goes run yep um and that's so my rant still kind of applies but it is the
[2234.10 --> 2238.68]  question of okay how if you were doing all this fancy meta programming how do you debug it and it is
[2238.68 --> 2243.04]  the question of tooling which a lot of people just especially when they're designing languages forget
[2243.04 --> 2248.50]  and it's like do you not actually work on projects where you have to be in a debugger or do you work on
[2248.50 --> 2252.82]  really complicated things and again this is kind of one of the beauty things is those sort of dynamic
[2252.82 --> 2259.26]  languages do work um it's just the compiled ones they kind of forget and that's why i again rust rust
[2259.26 --> 2265.24]  macros macro expressions proc macros whatever the whichever ones you want to use it's hell it's hell and
[2265.24 --> 2272.24]  just reading them let alone debugging them is it's not pearl levels of headache inducing but it's close
[2272.24 --> 2279.52]  um all right hold on jose i have to ask this question because i don't know how much uh all the macros
[2279.52 --> 2285.78]  throughout elixir slowdown compile time but if you were to go back today would you would you put say
[2285.78 --> 2290.30]  the if statement in def modules if you just had unlimited time would you put those as actual
[2290.30 --> 2295.62]  language constructs as opposed to macros or are you happy and you actually would want them to stick
[2295.62 --> 2303.06]  as macros so unlimited time you could unlimited time no i wouldn't that part i wouldn't change
[2303.06 --> 2309.54]  so there are a lot of things that so there there are a lot of criticism to macros and i think and i
[2309.54 --> 2313.70]  think there are like some misconceptions i don't know if we started doing phoenix so some people say
[2313.70 --> 2320.30]  like phoenix is mostly macros and i'm like no that's like it kind of feels that way right yeah but
[2320.30 --> 2328.84]  like i was like that's i'm like that's objectively a lie like i i can yeah prime yeah yeah prime dump
[2328.84 --> 2337.40]  liar liar like give give me any like give me any metric that you want to measure like invocations
[2337.40 --> 2345.08]  definitions api size macros are going to be like five percent the thing for is that the entry point
[2345.08 --> 2350.48]  of phoenix the router it's basically macros and then we can talk about why it's macros there
[2350.48 --> 2356.10]  right and but and and i think that gives the impression but then when you are in your controllers
[2356.10 --> 2362.18]  when you are in your templates when you are in your live views it's just regular code so the entry point
[2362.18 --> 2368.14]  but right but wait what was the question again if you had the unlimited amount of time and you could
[2368.14 --> 2372.40]  change anything would you bring in any of the macro stuff you've built throughout the language like if
[2372.40 --> 2380.06]  any of those things would you bring them in so so they are yes so i would i would not i would i
[2380.06 --> 2386.62]  wouldn't change that part of the language i think it's so essential for what elixir is like well the
[2386.62 --> 2392.26]  goal of the language was to be a small extensible language so you can go and do whatever the heck you
[2392.26 --> 2399.08]  want with it right and building the language in itself with its constructs like i i have to say like uh
[2399.08 --> 2407.96]  me as a my perspective is that me as the language author i cannot cheat i cannot add a construct that
[2407.96 --> 2414.02]  is just for me because i decided so so it's like no cheating rule like the rules that i have to create
[2414.02 --> 2422.60]  the language are the rules that you have to extend the language that that's it right and i do my best
[2422.60 --> 2429.10]  to not cheat right i should not be doing that and and it's such an essential part of the language that
[2429.10 --> 2435.66]  i think like if you remove that it's no longer elixir it's going to be something something else but on the
[2435.66 --> 2447.62]  point of macros i don't think they slow compile time um i think the issue and and so okay so so when i
[2447.62 --> 2453.00]  decided i'm going to have macros the other thing that i had is how do i make macros sane right like
[2453.00 --> 2459.10]  because depending on how you design the macro system it can be something that is impossibly hard
[2459.10 --> 2465.88]  to debug so when designing elixir i was like okay because i'm having macros it means that i'm not
[2465.88 --> 2472.48]  going to have a bunch of other features like uh global injection of code that's not a thing that you
[2472.48 --> 2478.36]  can have in elixir compile time discovery of modules so there are other kinds of metaprogramming
[2478.36 --> 2483.94]  that other programming languages have because i said look i'm having macros i'm saying no to all this
[2483.94 --> 2491.60]  stuff in order to keep the language simple right and again like the no cheating rule also means that
[2491.60 --> 2497.02]  because i could say no cheating and then i could bloat the language and add a thousand different
[2497.02 --> 2506.02]  things because i'm like okay right so all those things they act as balance and um yeah and i
[2506.02 --> 2510.74]  wouldn't change it but one thing that is very interesting there are there are two topics that
[2510.74 --> 2515.74]  i want i it's going through my head as we are discussing those things and one of them like going
[2515.74 --> 2524.58]  back to types is so i had like this no cheating rule kind of thing and it has worked out well so far
[2524.58 --> 2531.56]  but now we're working on a type system for elixir and it happens that the type system throws a huge
[2531.56 --> 2540.26]  wrench at the the no cheating rule exactly because what bill said like so if you think like about a
[2540.26 --> 2547.30]  type system the the thing that you can express in a type signature like what you can put in a type
[2547.30 --> 2552.40]  signature is actually just a subset of what the type system can actually do the type system can actually
[2552.40 --> 2557.94]  do more but the type theory just does not know how to express those things in the type system
[2557.94 --> 2563.30]  which means that now i have a dilemma in that i'm typing elixir and then we have all these features
[2563.30 --> 2571.96]  that we have used for a decade right and i cannot put a type signature in them but i can special case
[2571.96 --> 2578.86]  them in the type system and then it will work in the type system so that's kind of like the and i think
[2578.86 --> 2583.26]  it goes back to what bill was saying well if you're designing a programming language and you want to
[2583.26 --> 2590.14]  do println the type system doesn't know how to deal with that right so which side which trade-off are
[2590.14 --> 2594.64]  going to make and that's ultimately like the thing like you have to make all those decisions all those
[2594.64 --> 2600.32]  trade-offs right and make sure that at the end of the day you don't have like the frankenstein
[2600.32 --> 2605.98]  monster coming out of it right yeah but to explain like the printf one i probably skipped over that too
[2605.98 --> 2610.22]  much but like when i made odin the one of the first things i kind of wanted to add into language
[2610.22 --> 2616.76]  was runtime type introspection um now many people make something this what this means is at runtime
[2616.76 --> 2620.84]  you can actually say hey this is where this is the type of the thing like can you give the information
[2620.84 --> 2625.10]  about the type and in odin it's really dumb it's just a basic lookup table like oh this is a struct
[2625.10 --> 2628.98]  this has got the fields here's the names here's the types here's the tags is whatever or other
[2628.98 --> 2632.60]  properties of the field doesn't instruct it's that simple because it's the dumbest one you want to do
[2632.60 --> 2637.34]  it's ones that pretty much people want the thing is is that that's one approach to doing a print
[2637.34 --> 2641.40]  statement the other one is obviously the compile time one if you do the compile time language right
[2641.40 --> 2647.18]  where it will generate a new print procedure print function every time with the arguments you put into
[2647.18 --> 2654.30]  it and that's kind of what the rust approach is doing now there are arguments for both um and
[2654.30 --> 2658.76]  how do i explain this the rust one sounds great because it's like oh you only make the code for the
[2658.76 --> 2662.26]  your own generate the code for the code you actually need to print for for those types
[2662.26 --> 2671.84]  great yeah that's combatorial explosion um that's like n factorial it can be as bad as because you've
[2671.84 --> 2675.20]  got all these different things and then your executable size gets worse your compile times get worse
[2675.20 --> 2679.90]  and it's like you've gone screwed up well the the runtime type information approach like which odin does
[2679.90 --> 2685.82]  is um it's a giant fixed cost but it's a fixed cost i say it's giant it's tiny but it's like it's a fixed
[2685.82 --> 2690.60]  cost and you have one procedure that handles everything but then you have this giant lookup
[2690.60 --> 2694.54]  table so then you have these different things so the compile times is faster the code generation's
[2694.54 --> 2698.40]  faster and then actually you've only got one thing as well so it's actually easier to deal with
[2698.40 --> 2704.22]  so it's kind of like this is why having like i i know this problem from cpus plus other languages
[2704.22 --> 2708.92]  that do this kind of like compile time based printing things have that will hit and they will hit
[2708.92 --> 2714.64]  this problem of combatorial explosion very very quickly um and it's going to be
[2714.64 --> 2719.18]  this is why you got trade-offs when you have to think about it because you have to understand which
[2719.18 --> 2722.54]  trade-offs you take when you're doing design so that's kind of saying like when you do a print
[2722.54 --> 2724.96]  thing because there's there's multiple options you can do it the generic ways which is like
[2724.96 --> 2729.70]  runtime or compile time generation or you could just have hey we have built-in language like for
[2729.70 --> 2733.62]  instance anyone's used go they have a bootstrapping built-in procedure called print line
[2733.62 --> 2738.08]  like little locates or print line that's their bootstrapping thing so when they were making the
[2738.08 --> 2743.14]  compiler they kept that in to do stuff they recommend never using it for anything but it's
[2743.14 --> 2748.52]  like okay that's kind of useful um but then eventually they want you to use the thumped package
[2748.52 --> 2757.20]  um for everything and and and the annoying thing about those things is that um they are just going to
[2757.20 --> 2761.94]  bite you later on when people are actually using the language and they have large projects and it's like
[2761.94 --> 2767.76]  well now the the the explosions in your face like all the combinatorials
[2767.76 --> 2774.74]  yeah it's yeah so i actually i didn't realize that that rust creates a separate function kind
[2774.74 --> 2778.96]  of like some sort of templating style function for every single print statement you do from what i
[2778.96 --> 2782.36]  understand if i remember correctly yeah i think that's the case now please if the chat wants to
[2782.36 --> 2787.22]  correct me please tell me i'm wrong i don't mind being wrong um but i think that's kind of how it
[2787.22 --> 2793.26]  works for the general prints um it might be a bit clever in how it can reduce everything but i thought
[2793.26 --> 2801.04]  that's how it kind of worked okay wow um and and also jose just to when you say cheating is this
[2801.04 --> 2807.08]  cheating in the same way like uh make is cheating and go where it actually is generic when we don't
[2807.08 --> 2811.90]  have access to that level of generics and go for a long time where like they have they get the special
[2811.90 --> 2817.30]  one but you don't get the special one yes every time there is a language feature where you're like
[2817.30 --> 2821.92]  oh can i implement this myself which is all languages they are going to have right like
[2821.92 --> 2828.60]  there is always cheating right like there is always well but exactly things like that that's what i want
[2828.60 --> 2837.48]  i want to minimize and elixir allows us to minimize this considerably because we are we are bootstrapping
[2837.48 --> 2843.26]  ourselves on top of their virtual machine and a runtime right so we can really keep the amount of
[2843.26 --> 2850.78]  of uh cheating low but like for example places where elixir cheats is well uh data types right like
[2850.78 --> 2856.90]  we have our data types our lists tuples that come from our lane you can't create a data type like that
[2856.90 --> 2863.06]  one that is going to work on pattern matching and all of that right but when it comes to language
[2863.06 --> 2870.20]  constructs right like control flow all these sort of things in elixir there are very few they are very
[2870.20 --> 2876.00]  few and everything is built on top of that it's kind of it kind of reminds me of uh like in lua
[2876.00 --> 2881.30]  they have this idea of mechanisms over policies right so brazil mentioned shout out brazil you got
[2881.30 --> 2889.60]  to talk all the brazil languages um right but uh it's this idea that like instead of adding this huge
[2889.60 --> 2895.14]  set of language features and then figuring out how all of them interplay like lua is like no we're
[2895.14 --> 2900.56]  just gonna have like oh error handling that's just a function call you do p call and you get a result
[2900.56 --> 2904.88]  whether there was an error or not right it's like oh it's all just it's just functions oh what are
[2904.88 --> 2910.64]  files they're just they're just thunks right like everything is still just functions all the way down
[2910.64 --> 2915.32]  for lua right and like how do we store data oh it's tables all the way down uh which i think is a
[2915.32 --> 2920.68]  really nice like idea in lua there's like not a lot of cheating from the language either right like
[2920.68 --> 2927.14]  it kind of does the same thing there yeah i feel like odin is cheating a lot then if you're using
[2927.14 --> 2935.82]  this definition um i don't class it as cheating this is the thing oh it's fine when you do it i see
[2935.82 --> 2940.50]  how i know i think it's great because i don't feel i'm cheating this because i make up the rules of the
[2940.50 --> 2945.58]  game in my language so obviously that therefore it's not cheating oh house rules oh ginger mill's
[2945.58 --> 2951.84]  play yeah all right okay so so why is it not cheating or oh let me rephrase the question
[2951.84 --> 2958.98]  why is it good for a language author to have constructs only they control and not and allowing
[2958.98 --> 2962.22]  users to use it but not control it or create them themselves
[2962.22 --> 2968.74]  so i'm going to phrase it slightly differently and then answer your question if that makes any sense
[2968.74 --> 2974.52]  um so the first thing is when i approach language design in general i'm coming very pragmatic i'm
[2974.52 --> 2980.16]  literally asking what do the general things that people want and then i implement that right like
[2980.16 --> 2986.00]  in odin we have a built-in string type we have a built-in slice array type so slices um array
[2986.00 --> 2990.36]  programming as well you can just add two arrays together and they'll do element wise operations
[2990.36 --> 2995.00]  we've got matrices built into language we've got dynamic arrays built in we've got a hash map built
[2995.00 --> 3000.82]  in as in its syntax level it's not just thing now the thing is i added all these features because
[3000.82 --> 3004.66]  this is what people want when they're trying to use more high level things like when they try and
[3004.66 --> 3010.16]  use that in c plus plus operate overloading well most of the cases of operate overloading that they
[3010.16 --> 3017.90]  use are to create all of those things i've just listed or if they're trying to do um and this is
[3017.90 --> 3023.72]  the kind of the thing it's not that i don't want to give people loads of power is that if you or it is
[3023.72 --> 3029.16]  actually if you give people loads of power they will abuse it right but it's also don't you don't need to
[3029.16 --> 3034.62]  give them the power you can just give them the tools like the the direct things and they'll be
[3034.62 --> 3040.54]  polished they'll have better semantics better error messages better everything this is kind of thing
[3040.54 --> 3044.72]  why i'm saying i don't think it's cheating but here's the thing odin doesn't have macros you can't
[3044.72 --> 3048.66]  even produce even further you can't don't have operator loading and when you do need all these
[3048.66 --> 3054.98]  fancy things you're just using basic data types and procedures and that's it so you now know where the
[3054.98 --> 3059.94]  the base languages and then the custom stuff it's not merged into one it's not trying to be hidden
[3059.94 --> 3064.28]  and it's like some people like oh i'd really like to have this fancy syntax and i'm like
[3064.28 --> 3074.90]  no and um that's a very common answer i give most people is uh no yeah i i agree i agree with that i
[3074.90 --> 3081.48]  think that's exactly the trade-off and i think going back i think like everything cheats and they
[3081.48 --> 3087.76]  don't cheat to certain extent it's like what the language chooses as an extensibility mechanism like
[3087.76 --> 3092.44]  operator overloading are you going to have those things are you not going to have those things
[3092.44 --> 3102.14]  and i think the problem is when a language has too many constructs i feel like there is a line in there
[3102.14 --> 3108.24]  where the language has too many constructs that only the language can do and when a developer has to
[3108.24 --> 3115.56]  build a library they cannot build something that feels like that language that's that's you know
[3115.56 --> 3121.62]  like sticks out like a sore thumb that's when you know you that's that's where the friction appears
[3121.62 --> 3126.78]  and that's when people feel frustrated but if the thing so you you can do a lot of cheating right
[3126.78 --> 3131.00]  like according to my definition yeah but if at the end of the day you have the mechanism where
[3131.00 --> 3137.30]  people can go well maybe somebody wants to do a red black tree and it feels just as good as the
[3137.30 --> 3142.66]  hash maps in the language it doesn't feel like very dissonant from the rest of the language
[3142.66 --> 3147.86]  or you apply that to other things and they're they're going to be happy right even fold like
[3147.86 --> 3154.10]  you know they are not going to get all the way but if they get like 80 percent nine percent of the
[3154.10 --> 3159.42]  way then they'll be happy they'll feel like okay i feel like i'm i i'm expanding i am
[3159.42 --> 3166.08]  contributing i am extending uh the thing that i use every day yeah it's just just for me i've
[3166.08 --> 3170.50]  been seen so much abuse of like operative legend for example i've seen so much to the point where
[3170.50 --> 3176.80]  i'm like yeah you're not having it i can't even trust myself with it let alone others like seriously
[3176.80 --> 3182.38]  um i've seen people who have overloaded insane stuff and then other languages now allow custom
[3182.38 --> 3189.70]  operators i guess i'm looking at you swift um and oh my god it's actual hell it's hell and you're
[3189.70 --> 3194.12]  making it worse for everybody man it's like i'm now looking at what what am i looking at this this soup
[3194.12 --> 3200.00]  of punctuation everywhere and i don't know what it does i'm like can you just have a nice procedure
[3200.00 --> 3204.50]  or function call that just has a very long name that tells you what it is just say this is the
[3204.50 --> 3211.26]  thing that bakes the chicken just have that it would be wonderful rather than having the percent sign
[3211.26 --> 3215.54]  that tells you actually this is doing the fancy baking the chicken for you i'm like of course it's
[3215.54 --> 3221.76]  so obvious like no no it wasn't i have actually seen some really horrific operator overloading and
[3221.76 --> 3226.30]  yeah that's why i just no no so that's why i implemented the things that people 99 of use
[3226.30 --> 3230.52]  cases even probably higher than 9 and just added them and then most people are now happy
[3230.52 --> 3237.56]  yeah those are two things upset but yeah operator overloading custom operator those are two things
[3237.56 --> 3244.14]  that we like we strongly agree with i'm like yeah like if you feel need those there's probably
[3244.14 --> 3250.10]  something wrong somewhere right it's like but how can i have job security without those
[3250.10 --> 3254.86]  like i'm gonna write them in and then i'm the only one that can come in to this library
[3254.86 --> 3262.60]  ginger bill you're stealing my job dude you say that job security until someone tells you manage
[3262.60 --> 3265.22]  that they've done that and they're going oh shit we need to get rid of this guy now quick
[3265.22 --> 3270.84]  it's too late by then it's too late i know it's like damn we're gonna have to slowly it's like
[3270.84 --> 3278.62]  the time just that was the garden time is going to be a very long time um all right so speaking of
[3278.62 --> 3283.68]  too many features in a language i actually wanted to go back to ginger bill on rust here do you think
[3283.68 --> 3289.58]  rust ultimately will go in the same direction of c++ where it just feels like every feature in the
[3289.58 --> 3295.70]  universe is weighing it down where you think that you do you think i think it did it pretty much years
[3295.70 --> 3302.00]  ago oh really yeah yeah do you think that's a downfall in the language or do you think that
[3302.00 --> 3308.14]  it's a good sign no it's a downfall from the start but again as i said i hated c++ modern c++ and rust
[3308.14 --> 3313.82]  is kind of a the next step in that thing and it already does all that like there's also these other
[3313.82 --> 3322.70]  aspects where i'd be very careful what i mean by this statement um you don't have to be careful it's
[3322.70 --> 3328.04]  just the four of us no no no no no no no i have to be careful because i know the internet and they'll
[3328.04 --> 3333.24]  misinterpret me no matter what i say and how clear it is like i still get people saying oh don't you
[3333.24 --> 3338.24]  hate lsps and like i made a i was like i even caveated for that and like no i just don't use them
[3338.24 --> 3342.70]  if you use them whatever right this is the internet for you right right what i mean is i think rust
[3342.70 --> 3348.58]  as an idea should have been tested at a smaller scale like they should have had all of the
[3348.58 --> 3352.68]  ownership semantics lifetime semantics which are mathematically prudent obviously and then just had them in a
[3352.68 --> 3357.76]  very small c-like language with none of the actual other features and then they should have gone okay
[3357.76 --> 3363.58]  how do we make this effectively more ergonomic and then start thinking okay we need to add this then
[3363.58 --> 3368.66]  add this and then add this but they didn't they started effectively in the middle and went right
[3368.66 --> 3374.34]  we're gonna do all this we need all of the trait system we need all of the um macrosystem like they
[3374.34 --> 3378.84]  just started there and then went that's what we want and they didn't start from like okay where can we
[3378.84 --> 3383.50]  get because to me rust isn't that ergonomic i know it's for many people but like that's the thing
[3383.50 --> 3387.38]  is a lot of language design a lot languages aren't that ergonomic elixir is quite ergonomic actually
[3387.38 --> 3393.38]  that's one thing i'll praise about it um but it's like rust isn't rust is also fighting things and i'm
[3393.38 --> 3396.30]  not saying the borrower checker i'm fighting i'm usually fighting the lifetime system
[3396.30 --> 3403.78]  um and and i think that's a lot of the times people think like i actually wanted to i don't
[3403.78 --> 3407.96]  want to define my lifetimes based on a value most of the time which is how the whole rust thing wants
[3407.96 --> 3411.48]  i usually want to do with control flow like hey this language this this value is actually bound
[3411.48 --> 3416.94]  to a loop effectively so when the loop resets the lifetime is dead now i know you can do that with
[3416.94 --> 3422.02]  ghost cells and such kind of so you can get around those tricks now the magical invention of ghost cell
[3422.02 --> 3429.10]  but even then it's still a bit of a not really what i want um if that makes any sense i get it
[3429.10 --> 3432.52]  sometimes you just want like i want this thing to live for a function it's going to live for a
[3432.52 --> 3436.50]  function it's going to i'm going to hit some a sinks in here it's just it's here for this function
[3436.50 --> 3441.32]  that's all i want stopping annoying i'm going to pass it around it's alive for this much that's it
[3441.32 --> 3448.06]  that's it people i want to specify that and then doing that is hard yes yeah you're saying though
[3448.06 --> 3454.42]  you don't want the value to define a lifetime you want to define the lifetime of value gingerbill
[3454.42 --> 3455.78]  correct indeed
[3455.78 --> 3460.68]  put that one on a t-shirt i'm not god okay i'm not god
[3460.68 --> 3467.24]  okay i have i've got a quick question gingerbill since you're well known for hating lsps
[3467.24 --> 3475.28]  and uh and jose you you're well known for loving them and that's why elixir has three i'd love to
[3475.28 --> 3478.76]  hear what all of your opinions are on lsp in the modern landscape
[3478.76 --> 3490.66]  how long have you been sitting on that one i wrote that one before we got here boys and when
[3490.66 --> 3498.52]  gingerbill mentioned lsp i was like it's my top shot boys i love it i love it i could not wait for
[3498.52 --> 3503.68]  you love them so much there's three that better be a short one unofficial one
[3503.68 --> 3508.90]  i should think technically i'm just gonna get there's two unofficial ones in odin as well like
[3508.90 --> 3513.28]  this is an intellij one as well i think um but not official in odin that's all because
[3513.28 --> 3520.02]  official would mean i'd have to work on it that's about yeah and that's the is that the main thing
[3520.02 --> 3522.94]  for you you're just like i don't want to spend any time on it i don't want to ship it with
[3522.94 --> 3531.48]  i actually have a main job to deal with at jangra effects um so yeah if let's say i was a super big
[3531.48 --> 3539.22]  odin fan and i had a company you know rangra effects and i was like hey we want an lsp super
[3539.22 --> 3544.92]  bad i can donate either an engineer's time full-time ad infinitum for the next for however long
[3544.92 --> 3550.28]  or the amount of money that you would require to implement it would you say yes to that as an odin
[3550.28 --> 3556.44]  first class lsp or would you still say nah deal with the community this isn't where i'm gonna be
[3556.44 --> 3562.28]  we don't do that here depends on the map the price and i'm not even joking i'm not saying i'm being
[3562.28 --> 3567.64]  bored i'm just saying it's more of a like okay if you're gonna do this what i would have to do for
[3567.64 --> 3572.12]  odin's i'm gonna i'm gonna rewrite the the actual compiler completely so then it's going to be built
[3572.12 --> 3578.00]  up from the ground up to the compiler and the lsp are the same thing there is no separation so you've
[3578.00 --> 3581.86]  got that there now when i wrote the compiler i wasn't even thinking about it i should have it's
[3581.86 --> 3585.96]  one of those regrets where i should have made the compiler be a library as well like it should have
[3585.96 --> 3590.58]  been designed to be acted as a library i just wrote it to be a single thing that runs shoots off and be
[3590.58 --> 3595.38]  as fast as possible it is quite bodgy it's all interconnected it's not a library based thing
[3595.38 --> 3601.54]  but it's fast ish there's still slow bits in it and llvm really slows it down but that's the thing so
[3601.54 --> 3605.32]  if i was going to do the lsp route i would just rewrite the compiler so i could use it as a library so
[3605.32 --> 3610.06]  then you can get the lsp aspects and you've got all of that especially a lot of it that's what i'd do
[3610.06 --> 3615.60]  and i but that's the thing is next time i write the compiler we'll probably try and design it so
[3615.60 --> 3620.68]  we've got the lsp i know i've a friend of mine who wants to write new odin compiler calling it thor
[3620.68 --> 3626.34]  obviously because it's the son of odin and then um very cute and he wants to work on that and i'm like
[3626.34 --> 3630.58]  sure but he doesn't have any time because of course he works at jango effects as well so we have
[3630.58 --> 3640.12]  it's called lack of time um so that's half the problem yeah people bring up like lsp's right it's
[3640.12 --> 3645.74]  like oh why can't you have a good lsp right and then they and they usually yeah they would usually
[3645.74 --> 3651.52]  mention like uh typescript or something from microsoft and they're like oh you like why can't
[3651.52 --> 3656.82]  you have it they're like oh are you telling me that i should out of nowhere just do this project
[3656.82 --> 3663.08]  that microsoft spent millions on because they had to restructure the whole compiler and redo a bunch
[3663.08 --> 3668.28]  of things to support it right like that's the thing that people mean it's like it's actually a
[3668.28 --> 3675.58]  complex problem right and um i love that they picked typescript the one that like everyone has to
[3675.58 --> 3682.50]  restart constantly doesn't scale the big projects it's terrible categorically the worst known lsp
[3682.50 --> 3687.84]  also the inventor of the lsp yeah this is also the other thing about lsp is like this is actually
[3687.84 --> 3692.08]  like implementation detail i actually dislike about them they were designed by microsoft obviously and
[3692.08 --> 3696.58]  it's a protocol over json it was json or pc or whatever it is i can't remember the exact thing
[3696.58 --> 3700.12]  is but they're sending a json packet to send all this information and they've got a borderline like
[3700.12 --> 3703.72]  saying hey this is a this is kind of the general idea we think all most languages work on
[3703.72 --> 3708.26]  and it's kind of like great so if your language doesn't fit in that category very well you're a bit
[3708.26 --> 3713.88]  screwed or you want to do something else it doesn't work but this is microsoft so they kind of
[3713.88 --> 3717.00]  standardized it said it worked for all these different languages we kind of test it on and
[3717.00 --> 3724.10]  it's like great great or if you don't use unicode 16 which is definitely the most popular encoding
[3724.10 --> 3730.36]  it is it is the best utf 16 is the best because of course microsoft have been using it for the past 30
[3730.36 --> 3736.98]  years hold on a little bit longer hey javascript was originally all utf 16 okay buddy
[3736.98 --> 3743.68]  so is python that's why yeah 16 yeah yeah someone's like that's the reason why actually
[3743.68 --> 3751.62]  what is javascript written i think the reason why utf 16 is used is because um for most languages you
[3751.62 --> 3757.70]  can then index it and get the right code point however that's dangerous as hell because that means
[3757.70 --> 3765.38]  that's for code points okay i'll explain this i'm gonna explain you unicode okay but here ginger
[3765.38 --> 3774.70]  bill though i got a question so like 16 is bigger than 8 yeah explain that one ginger bill checkmate
[3774.70 --> 3782.18]  ginger bill i know that's mean man it's bigger unicode version 8 32 what about 32 man we should
[3782.18 --> 3790.10]  be using that you know what registered align unicode we should get unicode 64 and just start reading
[3790.10 --> 3798.10]  them like that that would be the true superiority utf 64 microsoft we're we're ready it's a little bit
[3798.10 --> 3803.84]  wasteful man come on come on and also we now we should nowadays we can just have even bigger
[3803.84 --> 3808.48]  registers like how big are the biggest things like 520 12 is the biggest register we have on some
[3808.48 --> 3813.54]  machines now right so that's a little great think how many emoji we can have that's what i was just
[3813.54 --> 3817.68]  gonna say there's so many emojis left you don't have to have all of the different things like the
[3817.68 --> 3822.32]  fitzpatrick color modifiers and the family modifiers and all that you could just have one giant emoji
[3822.32 --> 3829.18]  you have them all i think we solved it we did you're welcome microsoft yeah see i'll send my bill
[3829.18 --> 3835.86]  yeah we're gonna be charging you one microsoft salary for that oh i'd like that thank you
[3835.86 --> 3841.02]  it would have to be a distinguished engineer because only a distinguished engineer could come up with a
[3841.02 --> 3848.04]  with a plan this good oh yeah all right bill i'm glad that i i'm glad to hear that you also have
[3848.04 --> 3856.06]  feelings about unicode i'm glad to just see that spark spark happiness within you speaking of feelings
[3856.06 --> 3862.42]  that you have ginger bill let's talk package managers oh yes okay okay okay this is my last
[3862.42 --> 3866.60]  question that i had prepared so we can we can end that that's fine that's fine absolutely fine
[3866.60 --> 3871.94]  um i don't know if jose is gonna hate me or not for this uh well i figured if it goes bad well i
[3871.94 --> 3877.08]  just cut this from the end of the episode and then that's fine no no no we saved a clip and we put it
[3877.08 --> 3882.72]  on the clips channel there we go now and i'd be really serious voice looking into the camera going yeah
[3882.72 --> 3887.70]  yeah yeah whatever yeah you won't believe what ginger bill said about package managers
[3887.70 --> 3891.96]  even worse than lsbs
[3891.96 --> 3899.42]  i actually hate i think how do i put this i'm gonna use real words languages straight to the camera
[3899.42 --> 3907.64]  package managers are evil oh that's so crazy let's hear more that's why it's called hex
[3907.64 --> 3912.98]  i didn't put two tunes together but yeah
[3912.98 --> 3918.02]  i think we discovered something big chat
[3918.02 --> 3923.80]  all right ginger bill tell it tell us a little more i want to hear you and jose talk about it
[3923.80 --> 3927.92]  uh to explain what i mean i need to make some distinctions again because of course i like
[3927.92 --> 3933.48]  making distinctions i like aristotle um so the distinctions here i was like i need to make
[3933.48 --> 3939.08]  distinction what a package is the package manager package repository and the build system these are
[3939.08 --> 3942.30]  all separate and in fact you can have them all be separate and have no relation to each other
[3942.30 --> 3948.66]  pretty much right so i have nothing wrong with packages whatsoever in fact odin has packages built
[3948.66 --> 3952.48]  into the language i have nothing wrong with repositories because that's how a lot of people
[3952.48 --> 3957.50]  find discover new packages um it's effective just a search engine right okay there's nothing
[3957.50 --> 3962.82]  in search engine i use google go every day um and google and many other search engines because
[3962.82 --> 3967.56]  they're all pretty bad now so i have to keep swapping between them all um the other aspect is
[3967.56 --> 3972.70]  i don't build systems um that's usually like again that's language dependent if we're talking
[3972.70 --> 3977.44]  about languages here obviously so in odin i try and make it minimize the need for a build system
[3977.44 --> 3981.24]  entirely like odin build dot will compile even the most complicated stuff at jangr effects
[3981.24 --> 3987.00]  because we define all the linking stuff in the source code itself so in the language itself like
[3987.00 --> 3990.44]  it's not separate and if we don't use it doesn't get linked against and so on and so forth
[3990.44 --> 3996.06]  so that leads package managers what do they do separately well package manager effectively
[3996.06 --> 4002.82]  downloads the stuff from a repository and then handles the dependencies and tries to fix them
[4002.82 --> 4007.82]  around and everything like that and downloads its dependencies and its dependencies and you can
[4007.82 --> 4013.44]  probably see where my criticism is going this is automation of dependency hell
[4013.44 --> 4021.92]  and the problem is is i've said this before i even said this before on a stream here before like
[4021.92 --> 4028.48]  not everything needs to be automated especially hell and dependency hell is a real thing that i think
[4028.48 --> 4032.78]  many if any people's had been on a large project before they'll they'll be been in before right
[4032.78 --> 4038.60]  you've got literal thousands or tens of thousands of dependencies and you don't know if any of them
[4038.60 --> 4042.14]  work properly you don't even know what the bugs are you don't know how it's all going to be handling
[4042.14 --> 4047.84]  and it's awful and it's just like this is the wrong thing to automate if you actually had to do it
[4047.84 --> 4052.42]  manually it doesn't stop you getting into hell you can put yourself into hell that's really easy most
[4052.42 --> 4059.16]  people actually everyone puts themselves into hell yeah that's you do that voluntarily but the thing is
[4059.16 --> 4064.56]  it's more to do with how quickly you can get there and also makes you have to think like if you
[4064.56 --> 4068.68]  download it manually you start thinking maybe i don't want this or maybe i actually can do this and
[4068.68 --> 4072.86]  merge this and then when you update you just have to be very careful and do it independently and that
[4072.86 --> 4078.64]  stuff that's why general criticism is like it's automation for that problem and this is why if
[4078.64 --> 4082.04]  you look npm it's awful the other problem is also packet managers is a lot of package managers
[4082.04 --> 4086.54]  actually have to find what a package is because the language they're dealing with doesn't have a
[4086.54 --> 4091.58]  well-defined concept of a package either npm is the best cost a good example of this because also
[4091.58 --> 4097.38]  there's multiple other package managers for node that i can never remember because that now means you
[4097.38 --> 4098.84]  have to have a package manager manager
[4098.84 --> 4108.70]  yes that's apt that's apt apt yeah paru are the package this is where things get like because you
[4108.70 --> 4114.22]  haven't got a well-defined concept of what package is in the language that happens now luckily elixir
[4114.22 --> 4119.68]  has a well-defined concept of what a package is so elixir doesn't suffer from that problem uh but
[4119.68 --> 4124.50]  loads of languages don't have a well-defined one and it really really shows
[4124.50 --> 4129.70]  yeah this is why this is why i'm saying it's evil in the sense that it will send you to hell
[4129.70 --> 4134.22]  quicker okay hold on before you jump in there uh jose i have a quick question for this one with go
[4134.22 --> 4138.76]  go just seems to have this weird thing where i don't seem to need a lot of packages
[4138.76 --> 4144.88]  does go having a package manager but not seeming to have like the entrance to hell seems far and hard to
[4144.88 --> 4149.30]  get to is there something special about go that never quite arrived there because like i don't have
[4149.30 --> 4154.70]  400 dependencies when i do a go project yeah so go has a really good score library standard library
[4154.70 --> 4158.36]  right that's it has the batteries included like that's what i tried to do with odin like when you
[4158.36 --> 4162.80]  download in you can start doing pretty much anything in it right i just want to be able to download and
[4162.80 --> 4167.66]  here's the default color go is like that that's why like if you want to make a web server you pretty
[4167.66 --> 4172.02]  much don't need any third-party libraries if you just want to make a http server and you're done
[4172.02 --> 4178.80]  you may even write a whole lsp like i wrote a lsp yeah do you just write it from scratch
[4178.80 --> 4183.96]  yeah so the go standard library has a go compiler in it in fact it has two go compilers
[4183.96 --> 4191.08]  backup well it has the actual go compiler and then it has like the high level one that you can use
[4191.08 --> 4196.64]  yeah it's kind of in a sense it is kind of it's just like once the cling on oh god that's it
[4196.64 --> 4201.46]  that's a so nerdy joke man um and it's so bad that i know that joke um
[4201.46 --> 4207.72]  all right sorry yeah that's jose you're you're good i want to hear i want to hear the response
[4207.72 --> 4213.86]  on physiognomy here physiology i can't remember that one is that one no yeah i know i that's pretty good
[4213.86 --> 4222.58]  i i i i agree with a lot of that i like to say that the word dependency like lost all of its meaning
[4222.58 --> 4227.78]  to developers like in life if you say like you have a dependency it usually means like something
[4227.78 --> 4232.28]  you are responsible which is exactly what it means in programming right but in life like you have a
[4232.28 --> 4240.10]  dependency yes like something that you know you are responsible right if that thing do something
[4240.10 --> 4246.26]  wrong like you may potentially end up in jail like it's it's a thing it's a thing where you should
[4246.26 --> 4252.40]  worry about you have to take care about it every day and package dependencies they are kind of
[4252.40 --> 4257.64]  pretty much the same thing right so and and we don't we're just like oh i'm just going to add
[4257.64 --> 4264.26]  dependency i don't know what it what i don't know what it does it's just like this thing based on trust
[4264.26 --> 4272.86]  with no verification yeah and yeah and the package managers they they do automate that right so um
[4272.86 --> 4281.04]  if you if yeah i i i agree like you have to if you're going to have like a package manager you have
[4281.04 --> 4286.82]  to have counterbalances for this thing you need to have or a culture i don't know but you have or like
[4286.82 --> 4293.52]  discussions where you balance those things so when i'm starting a project i'm not automatically
[4293.52 --> 4305.06]  bringing 1000 potential like uh attacks into my into my app or uh you know 10 000 100 000 lines of code
[4305.06 --> 4311.46]  that i am kind of now on the hook to maintain it right if something goes wrong you know
[4311.46 --> 4316.34]  it it's not even security things like that's people so people say keep always bringing up security
[4316.34 --> 4321.40]  like a security risk i'm like they're not even the biggest worries like at work we use sdl2 for our
[4321.40 --> 4326.32]  window handling and input stuff and the amount of bugs that we have found and it's we absolutely hate
[4326.32 --> 4329.48]  it to the point where we're actually i'm actually going to probably write in the next couple of months
[4329.48 --> 4334.18]  just writing our own window handling map from scratch because then at least it's our code we can depend
[4334.18 --> 4338.44]  on it and we can trivially fix it and we're not relying on an extra dependency right i know many
[4338.44 --> 4341.94]  people but sdl is great it's used by millions of different things i'm like yeah but we keep hitting
[4341.94 --> 4351.70]  all the bugs but it's great yeah it's great though it's great though and it's like sdl3 might fix it all
[4351.70 --> 4356.68]  but it's like great but the time to integrate sdl3 in the same time i could just write it from scratch
[4356.68 --> 4361.42]  and that's fine and this in some sense i'm not saying i should abdicate everything we're written
[4361.42 --> 4366.84]  from scratch i wish there were just libraries that just worked but they still i have to depend
[4366.84 --> 4372.74]  on them and they're a liability and like not necessarily security liabilities just bug liabilities
[4372.74 --> 4375.68]  liability agree liability um
[4375.68 --> 4384.70]  do you think otp helps a lot in elixir just like there's a lot of things that come with
[4384.70 --> 4389.72]  the air laying like runtime and everything that like that creates more of a culture like
[4389.72 --> 4396.42]  i i mean when i'm doing elixir stuff i'm using phoenix a lot so like and phoenix is a wide ranging
[4396.42 --> 4402.56]  large scope thing you know you do a lot of stuff with it but it doesn't feel like it's
[4402.56 --> 4407.60]  you know infinite dependencies right it does feel like well after i get my first round of phoenix ones
[4407.60 --> 4414.14]  i'm not adding tons of dependencies every week to like mix those around so it seems like there is
[4414.14 --> 4420.50]  kind of a culture in elixir not to install a trillion things i don't know i'm not sure why
[4420.50 --> 4427.84]  yeah i think i mean i think part of it is exactly like i know i have this opinion the elixir core team
[4427.84 --> 4434.12]  has this opinion chris has this opinion so we are very careful we are not creating a bunch of
[4434.12 --> 4440.30]  dependencies right and that ends up reflecting on the initial experience of a lot of people and
[4440.30 --> 4447.32]  they end up like propagating it uh but regarding dependencies one of the things that uh i tell people
[4447.32 --> 4455.38]  is like look whenever you are going to add a dependency to your project go and read the source code
[4455.38 --> 4460.90]  like just read the source code go through the thing like the amount of times i think oh i needed
[4460.90 --> 4468.66]  this dependency and then i'm like oh actually i just if i get one third of three modules i have the
[4468.66 --> 4475.76]  whole thing in my app in my tests in a way that i can control without bringing all that other bloat
[4475.76 --> 4481.46]  right and then if the thing is good you you read it and they're like okay i actually i can actually
[4481.46 --> 4487.74]  trust this this is good code or you're going to learn something so a lot of my initial open source
[4487.74 --> 4493.64]  career came from that came from looking at dependencies seeing how it's done and say actually
[4493.64 --> 4500.22]  i can just do something smaller and i'm going to publish that instead or oh i i don't like the way
[4500.22 --> 4505.10]  this is implemented i can do something completely different which i think is going to work on these
[4505.10 --> 4511.74]  better ways and yeah just from reading dependency code i always read uh whenever i add something as a
[4511.74 --> 4518.48]  dependency i'm like that's my like uh that's my self-imposed tax you know it's like i have to read
[4518.48 --> 4523.96]  it if i'm going to add it i have to read it yeah if that's assuming you've got source code otherwise
[4523.96 --> 4531.58]  you have to reverse engineer it and i've done that a few times um but yeah that that is the the problem
[4531.58 --> 4536.88]  but yeah and if you this is the point people don't vet their code in general as well they don't
[4536.88 --> 4542.96]  check to see if it's good or bad they just assume it works there's this problem and it's a societal
[4542.96 --> 4549.98]  issue is it's a very program is a very high trusting um in in a place which is you should
[4549.98 --> 4556.54]  have the least amount of trust possible um but is this because to put it bluntly a lot of programmers
[4556.54 --> 4560.72]  are coming from very um developed countries which are very high trust for the most part and their
[4560.72 --> 4564.34]  cultures are like that so then we're applying that to the rest of their world and stuff like that and
[4564.34 --> 4568.32]  hopefully works and i'm like it's right great so you only need one person to do something malicious
[4568.32 --> 4572.04]  and everything you're these millions of people who depend on one thing you're screwed that's not
[4572.04 --> 4574.88]  necessarily a security thing it wouldn't say malicious they could just make a funny book
[4574.88 --> 4580.70]  where if you click one pixel on the screen it just now has rickrolling you but it could be
[4581.36 --> 4588.64]  next elixir release next elixir release think about it i know i like that think about it uh but but no i i
[4588.64 --> 4592.36]  would actually argue so i'm gonna i'm gonna put a separate argument for why i think that it
[4592.36 --> 4598.30]  why i think that exists um i think we've had a couple things one we've had a explosion of
[4598.30 --> 4603.36]  engineers over the last 10 years that are all coming into this just at the advent of really
[4603.36 --> 4608.80]  package managers coming out in all these languages right all at the same time and so programming felt
[4608.80 --> 4613.40]  very daunting right like when you don't know how something works it feels very daunting especially
[4613.40 --> 4617.34]  when you first start out like you don't know a lot about programming so things feel very daunting
[4617.34 --> 4620.98]  but the thing that i think is really confusing at least this high trust argument you make
[4620.98 --> 4626.60]  is that there's this weird uh it's almost like uh gentleman's amnesia if you've ever read this
[4626.60 --> 4630.16]  you go to a magazine you read about horses and you're like oh man i know all these facts about
[4630.16 --> 4633.58]  horses you flip to the next page it's about javascript and you're like man they got everything
[4633.58 --> 4636.88]  wrong about javascript you go to the next page it's about something else you're like man i know a lot
[4636.88 --> 4641.30]  about beetles but then you're like you just forgot that they were super wrong on the thing you
[4641.30 --> 4646.88]  understood but you think everything else is completely correct and so engineers like you will never find an
[4646.88 --> 4651.82]  engineer that doesn't go like this oh my co-workers dude some of them are so horrible hey let me
[4651.82 --> 4655.54]  download this library off the internet this is gonna be awesome right it's like it's crazy it's
[4655.54 --> 4659.60]  like they just they look and go oh wow yeah like one third of our staff can't program anything
[4659.60 --> 4663.82]  also i'm going to trust every open source package i've ever downloaded and so there's like definitely
[4663.82 --> 4668.78]  like a gentleman amnesia for programming code that i think we just put on that people who do open
[4668.78 --> 4674.82]  source or open things are the best of the engineers which there's no you know there's no gate there
[4674.82 --> 4679.02]  right it's just a thing it's because they're assuming programming is like any other industry
[4679.02 --> 4684.52]  like engineering that's been around for thousands of years or science which in modern
[4684.52 --> 4689.98]  components has been around what for 500 years um again like gilman murray explained in there he was
[4689.98 --> 4695.26]  a particle physicist right he is the guy who came up with and then came up with quarks these
[4695.26 --> 4700.22]  similar tumble particles that make up like protons and neutrons and such and the guy who came up with
[4700.22 --> 4705.10]  stuff up to make your point ginger bill ginger bill stop trying to sound smart okay yeah okay come
[4705.10 --> 4708.86]  on by the way the programming stay in your lane even more fancy because i know where the story
[4708.86 --> 4715.16]  comes from i know it comes from you meant quarts those crystals no no no the crystals
[4715.16 --> 4720.04]  okay now crystals have power ginger bill okay
[4720.04 --> 4727.36]  they had power it must be true okay look he was a smart dude he was also a wrestler so you want to want
[4727.36 --> 4733.80]  to mess with him so um but no yeah uh but this kind of thing is like this is a it was michael
[4733.80 --> 4738.50]  crichton did it you know the guy made like westworld or jurassic park he said he was friends with him
[4738.50 --> 4741.98]  and he was like he knows the show business this guy knows physics and when you read the newspaper
[4741.98 --> 4744.92]  they talk about it oh he's bad and then they all believe everything else and it's like yeah you do
[4744.92 --> 4750.60]  because you trust people you you believe because i know this is my expert like this would go back to
[4750.60 --> 4756.24]  my old one c plus plus ram um i was doing it because i was kind of trusting who i
[4756.24 --> 4759.86]  perceived to be the experts because they were all telling me this like on the internet you got all
[4759.86 --> 4764.88]  these articles and conference videos and books they all kind of tell you this and i'm like even
[4764.88 --> 4768.32]  at the time i was like this seems a bit weird but hey they might be right because it might be as a
[4768.32 --> 4772.34]  scale on as you go this will benefit me as i go along because i was just kind of trusting this
[4772.34 --> 4777.50]  what i perceive to be wisdom but then as i've now gotten through more programming i'm realizing
[4777.50 --> 4784.68]  there's no wisdom in in this industry non well very very little wisdom i would put and that
[4784.68 --> 4788.56]  we're in so many days and it makes sense because as i've gotten older i've gotten more knowledgeable
[4788.56 --> 4793.08]  about certain things like there's no evolutionary selection pressure this industry is probably 70
[4793.08 --> 4799.56]  years old 75 years at max so it's like this is not old enough to get rid of all the literally bad
[4799.56 --> 4804.68]  things we haven't it hasn't evolved quick enough it will find out in probably a few hundred years i
[4804.68 --> 4813.18]  mean hundreds um we'll find out where the the good stuff is and at the moment i don't know if we know
[4813.18 --> 4818.02]  any really good ones like um i think the only kind of law that we have in programming with like
[4818.02 --> 4822.52]  casey would say is like conway's law which is like the structure of an organization will
[4822.52 --> 4830.26]  effectively maps itself on how they structure their code um and their projects but that's
[4830.26 --> 4839.06]  that's about it does that make sense i got one last question to end i can't believe you didn't say
[4839.06 --> 4845.60]  this ginger bill books you shouldn't read books that's what he just said books are for stupid
[4845.60 --> 4854.00]  people well-known lsp and book hater ginger bill books what what are those things i don't know
[4854.00 --> 4860.12]  just don't kill a tree don't read books you're killing trees man you hate the environment smart i
[4860.12 --> 4867.22]  always quote the the simpsons meme i'm here to lead not to read so that's a great one that's a
[4867.22 --> 4874.08]  classic okay my last question short short answer i think you gotta boil it down to one sentence for
[4874.08 --> 4879.50]  each if you're giving advice to someone making their own programming language today what's the
[4879.50 --> 4883.66]  one piece of advice you'd give them don't do it you can't say don't ginger bill because i know that's
[4883.66 --> 4887.88]  the first thought i wasn't saying that i was never gonna beat you to it he was already like don't
[4887.88 --> 4896.50]  don't do it all right one sentence ginger bill and then jose uh learn the basics of how to do
[4896.50 --> 4900.92]  tokenization passing and when you're doing passing you only want recursive descent and practicing
[4900.92 --> 4906.96]  pretty much and then you start learning type stuff start with a very and and and and that's one
[4906.96 --> 4915.78]  with a very basic language that and i mean when i say basic i mean can it do arithmetic nothing else
[4915.78 --> 4922.82]  don't try and recreate python start even smaller than that okay so you said tokenization so start
[4922.82 --> 4930.88]  with a crypto coin got it jose you're up listen to bill oh great answer damn that is a good answer
[4930.88 --> 4938.34]  good answer good answer good answer also ginger bill i did catch that c.s lewis quote in there you
[4938.34 --> 4942.98]  know all people choose hell welcome in there i thought i was like look at that hey i love
[4942.98 --> 4951.32]  oh god i love that book the books in general uh but uh all right i i technically don't have any more
[4951.32 --> 4955.54]  questions i think i do actually have i have so many questions in some sense but i don't know if we
[4955.54 --> 4960.10]  should uh keep going or call it a day because we're actually i have to go yeah you have to go
[4960.10 --> 4965.36]  i have to go we'll come back we'll invite you guys back on again and you can argue some more
[4965.36 --> 4975.26]  yeah i mean uh talk yeah that was very fun yeah that was good all right are you gonna close the
[4975.26 --> 4980.18]  episode i mean i never close the episode i always forget hey thanks for watching the stand up with
[4980.18 --> 4988.14]  me today was tj was a jose velim creator of elixir and ginger bill creator of odin it's soon to be
[4988.14 --> 4990.24]  thor you're about that you're about to be a granddad
[4990.24 --> 4995.84]  is that a thing can you be a granddad in languages
[4995.84 --> 5007.78]  um maybe joe armstrong he the creator of erlang he considered you know he would say elixir it's
[5007.78 --> 5012.96]  like his grandchild he's a grandfather now so i mean at this point if that's also i mean
[5012.96 --> 5018.58]  nicholas via the creator of pascal and also worked on our goal and all that lot he so our goal pretty
[5018.58 --> 5023.72]  much the stemming of every single like the imperative language from now on yeah at that
[5023.72 --> 5028.64]  point he's not a grandfather he's like great great great great great great grandfather he's adam right
[5028.64 --> 5035.14]  adam and eve yeah he's the patriarch yeah he's adam now the question who is eve uh obviously fortran
[5035.14 --> 5039.18]  she's a little i know on the next episode of the stand up yeah there we go fortran now that is
[5039.18 --> 5046.32]  yeah there we go fortran all right well thank you very much for watching this this was another
[5046.32 --> 5049.72]  episode of the stand up i have never actually closed it this well i don't know if you were
[5049.72 --> 5052.60]  gonna say anything oh okay goodbye bye bye
[5052.60 --> 5061.64]  the day vibe caught and errors on my screen terminal coffee
[5061.64 --> 5066.52]  live in the dream
